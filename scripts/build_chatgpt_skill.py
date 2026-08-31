#!/usr/bin/env python3
"""
Build the ChatGPT distribution package for Universal Research Skills.

Design goals
------------
1. GitHub repository files under skills/*/SKILL.md remain the canonical source.
2. The 56 canonical skill files are NEVER edited by this script.
3. Canonical skill bytes are copied unchanged to references/<skill-name>.md.
4. The only SKILL.md inside the generated ZIP is the ChatGPT orchestration entry
   point from templates/chatgpt-integrated-skill/SKILL.md.
5. A SHA-256 manifest proves source/reference identity.
6. --release mode requires a clean Git working tree and an exact version tag.

Standard-library only; no third-party Python packages required.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Optional


EXPECTED_SKILL_COUNT = 56
PLUGIN_MANIFEST = Path(".codex-plugin") / "plugin.json"
ENTRY_TEMPLATE = Path("templates") / "chatgpt-integrated-skill" / "SKILL.md"
SKILLS_DIR = Path("skills")
DIST_DIR = Path("dist")


def fail(message: str, exit_code: int = 1) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(exit_code)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run_git(repo_root: Path, *args: str) -> Optional[str]:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo_root,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )
        return result.stdout.strip()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None


def git_state(repo_root: Path) -> dict:
    commit = run_git(repo_root, "rev-parse", "HEAD")
    status = run_git(repo_root, "status", "--porcelain")
    exact_tag = run_git(repo_root, "describe", "--tags", "--exact-match", "HEAD")
    branch = run_git(repo_root, "branch", "--show-current")

    return {
        "commit": commit,
        "branch": branch,
        "exact_tag": exact_tag,
        "working_tree_clean": status == "" if status is not None else None,
        "git_available": commit is not None,
    }


def parse_frontmatter(text: str, source: Path) -> tuple[str, str]:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        fail(f"Invalid or missing YAML front matter: {source}")

    block = match.group(1)

    name_match = re.search(r"(?m)^name:\s*(.+?)\s*$", block)
    desc_match = re.search(r"(?m)^description:\s*(.+?)\s*$", block)

    if not name_match:
        fail(f"Missing front-matter 'name': {source}")
    if not desc_match:
        fail(f"Missing front-matter 'description': {source}")

    return name_match.group(1).strip(), desc_match.group(1).strip()


def validate_entry_skill(entry_bytes: bytes, source: Path) -> dict:
    try:
        text = entry_bytes.decode("utf-8")
    except UnicodeDecodeError:
        fail(f"Entry SKILL.md is not valid UTF-8: {source}")

    name, description = parse_frontmatter(text, source)

    if name != "universal-research-skills":
        fail(
            "ChatGPT entry skill name must be 'universal-research-skills'; "
            f"found '{name}'"
        )

    if not (1 <= len(description) <= 1024):
        fail(
            "ChatGPT entry skill description must be 1-1024 characters; "
            f"found {len(description)}"
        )

    fence_count = len(re.findall(r"(?m)^```", text))
    if fence_count % 2:
        fail(f"Unbalanced Markdown code fences in {source}")

    success_count = len(
        re.findall(r"(?m)^#{1,6}\s+Success Criterion\s*$", text)
    )
    if success_count != 1:
        fail(
            f"Expected exactly one Success Criterion in {source}; "
            f"found {success_count}"
        )

    return {
        "name": name,
        "description_chars": len(description),
        "bytes": len(entry_bytes),
        "lines": len(text.splitlines()),
        "sha256": sha256_bytes(entry_bytes),
    }


def validate_canonical_skill(skill_path: Path, slug: str) -> dict:
    source_bytes = skill_path.read_bytes()

    try:
        text = source_bytes.decode("utf-8")
    except UnicodeDecodeError:
        fail(f"Canonical skill is not valid UTF-8: {skill_path}")

    name, description = parse_frontmatter(text, skill_path)

    if name != slug:
        fail(
            f"Folder/front-matter name mismatch: folder '{slug}', "
            f"name '{name}' in {skill_path}"
        )

    success_count = len(
        re.findall(r"(?m)^#{1,6}\s+Success Criterion\s*$", text)
    )
    if success_count != 1:
        fail(
            f"Expected exactly one Success Criterion in {skill_path}; "
            f"found {success_count}"
        )

    fence_count = len(re.findall(r"(?m)^```", text))
    if fence_count % 2:
        fail(f"Unbalanced Markdown code fences in {skill_path}")

    return {
        "name": slug,
        "source_path": skill_path.as_posix(),
        "description_chars": len(description),
        "bytes": len(source_bytes),
        "lines": len(text.splitlines()),
        "sha256": sha256_bytes(source_bytes),
        "bytes_data": source_bytes,
    }


def load_plugin_version(repo_root: Path) -> str:
    manifest_path = repo_root / PLUGIN_MANIFEST
    if not manifest_path.is_file():
        fail(f"Plugin manifest not found: {manifest_path}")

    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        fail(f"Invalid plugin manifest {manifest_path}: {exc}")

    version = str(data.get("version", "")).strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version):
        fail(f"Invalid or missing semantic version in {manifest_path}: '{version}'")

    if data.get("skills") != "./skills/":
        fail(
            f"{manifest_path} must declare \"skills\": \"./skills/\"; "
            f"found {data.get('skills')!r}"
        )

    return version


def collect_canonical_skills(repo_root: Path) -> list[dict]:
    skills_root = repo_root / SKILLS_DIR
    if not skills_root.is_dir():
        fail(f"Skills directory not found: {skills_root}")

    skill_dirs = sorted(p for p in skills_root.iterdir() if p.is_dir())
    missing = [p.name for p in skill_dirs if not (p / "SKILL.md").is_file()]
    if missing:
        fail(
            "Skill folders missing SKILL.md: "
            + ", ".join(missing)
        )

    canonical = []
    for skill_dir in skill_dirs:
        canonical.append(
            validate_canonical_skill(skill_dir / "SKILL.md", skill_dir.name)
        )

    if len(canonical) != EXPECTED_SKILL_COUNT:
        fail(
            f"Expected {EXPECTED_SKILL_COUNT} canonical skills; "
            f"found {len(canonical)}"
        )

    names = [item["name"] for item in canonical]
    if len(names) != len(set(names)):
        fail("Duplicate canonical skill names detected")

    if "research-router" not in names:
        fail("Required canonical skill 'research-router' not found")

    return canonical


def write_json(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def make_deterministic_zip(source_dir: Path, output_zip: Path) -> None:
    """
    Create a deterministic ZIP:
    - lexicographically sorted entries
    - fixed timestamp
    - fixed POSIX file permissions
    """
    output_zip.parent.mkdir(parents=True, exist_ok=True)

    if output_zip.exists():
        output_zip.unlink()

    fixed_time = (1980, 1, 1, 0, 0, 0)

    with zipfile.ZipFile(
        output_zip,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for file_path in sorted(p for p in source_dir.rglob("*") if p.is_file()):
            rel = file_path.relative_to(source_dir).as_posix()
            data = file_path.read_bytes()

            info = zipfile.ZipInfo(rel, date_time=fixed_time)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16

            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def verify_zip(
    output_zip: Path,
    entry_sha256: str,
    canonical: list[dict],
) -> dict:
    with zipfile.ZipFile(output_zip, "r") as archive:
        bad_file = archive.testzip()
        if bad_file is not None:
            fail(f"ZIP integrity failure at entry: {bad_file}")

        names = archive.namelist()

        # Exactly one SKILL.md must exist in the ChatGPT package.
        skill_md_entries = [n for n in names if Path(n).name == "SKILL.md"]
        if skill_md_entries != ["SKILL.md"]:
            fail(
                "Generated package must contain exactly one SKILL.md at archive root; "
                f"found {skill_md_entries}"
            )

        if sha256_bytes(archive.read("SKILL.md")) != entry_sha256:
            fail("Root SKILL.md hash mismatch after ZIP creation")

        reference_entries = [
            n for n in names
            if re.fullmatch(r"references/[^/]+\.md", n)
        ]
        if len(reference_entries) != EXPECTED_SKILL_COUNT:
            fail(
                f"Expected {EXPECTED_SKILL_COUNT} reference .md files in ZIP; "
                f"found {len(reference_entries)}"
            )

        mismatches = []
        for item in canonical:
            ref_name = f"references/{item['name']}.md"
            if ref_name not in names:
                mismatches.append(f"{item['name']}: missing reference")
                continue

            ref_hash = sha256_bytes(archive.read(ref_name))
            if ref_hash != item["sha256"]:
                mismatches.append(
                    f"{item['name']}: source/reference SHA-256 mismatch"
                )

        if mismatches:
            fail(
                "Canonical source/reference identity check failed:\n- "
                + "\n- ".join(mismatches)
            )

        if "references/MANIFEST.json" not in names:
            fail("references/MANIFEST.json missing from ZIP")

        if "BUILD_INFO.json" not in names:
            fail("BUILD_INFO.json missing from ZIP")

    return {
        "zip_sha256": sha256_bytes(output_zip.read_bytes()),
        "zip_bytes": output_zip.stat().st_size,
        "canonical_reference_matches": EXPECTED_SKILL_COUNT,
        "integrity": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Build one integrated ChatGPT Skill package from the 56 canonical "
            "Universal Research Skills without modifying canonical files."
        )
    )
    parser.add_argument(
        "--release",
        action="store_true",
        help=(
            "Build a release asset. Requires a clean Git working tree and "
            "HEAD tagged exactly v<plugin-version>."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional output ZIP path.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    version = load_plugin_version(repo_root)
    git = git_state(repo_root)

    if args.release:
        if not git["git_available"]:
            fail("--release requires Git to be available")
        if git["working_tree_clean"] is not True:
            fail("--release requires a clean Git working tree")
        expected_tag = f"v{version}"
        if git["exact_tag"] != expected_tag:
            fail(
                f"--release requires HEAD to be tagged exactly '{expected_tag}'; "
                f"found {git['exact_tag']!r}"
            )

    entry_path = repo_root / ENTRY_TEMPLATE
    if not entry_path.is_file():
        fail(f"ChatGPT entry template not found: {entry_path}")

    entry_bytes = entry_path.read_bytes()
    entry_validation = validate_entry_skill(entry_bytes, entry_path)

    canonical = collect_canonical_skills(repo_root)

    suffix = "" if args.release else "-PREVIEW"
    default_name = (
        f"Universal-Research-Skills-v{version}-ChatGPT{suffix}.zip"
    )
    output_zip = (
        args.output.resolve()
        if args.output is not None
        else (repo_root / DIST_DIR / default_name)
    )

    with tempfile.TemporaryDirectory(prefix="urs-chatgpt-build-") as temp_name:
        package_root = Path(temp_name)
        references_dir = package_root / "references"
        references_dir.mkdir(parents=True)

        # Root ChatGPT orchestration skill.
        (package_root / "SKILL.md").write_bytes(entry_bytes)

        # Canonical references: exact byte-for-byte copies, renamed only.
        manifest_skills = []
        for item in canonical:
            reference_path = references_dir / f"{item['name']}.md"
            reference_path.write_bytes(item["bytes_data"])

            copied_hash = sha256_bytes(reference_path.read_bytes())
            if copied_hash != item["sha256"]:
                fail(
                    f"Byte identity failure while copying {item['name']}"
                )

            manifest_skills.append(
                {
                    "name": item["name"],
                    "repository_source": f"skills/{item['name']}/SKILL.md",
                    "package_reference": f"references/{item['name']}.md",
                    "sha256": item["sha256"],
                    "bytes": item["bytes"],
                    "lines": item["lines"],
                    "source_reference_byte_identical": True,
                }
            )

        manifest = {
            "framework": "Universal Research Skills",
            "framework_version": version,
            "canonical_skill_count": EXPECTED_SKILL_COUNT,
            "router": "research-router",
            "entry_skill": "SKILL.md",
            "canonical_reference_rule": (
                "Every references/<skill>.md file is a byte-for-byte copy of "
                "skills/<skill>/SKILL.md from the repository working tree used "
                "for this build."
            ),
            "skills": manifest_skills,
        }
        write_json(references_dir / "MANIFEST.json", manifest)

        build_info = {
            "framework": "Universal Research Skills",
            "framework_version": version,
            "distribution": "ChatGPT integrated skill",
            "build_mode": "release" if args.release else "preview",
            "git_commit": git["commit"],
            "git_branch": git["branch"],
            "git_exact_tag": git["exact_tag"],
            "working_tree_clean": git["working_tree_clean"],
            "entry_template": ENTRY_TEMPLATE.as_posix(),
            "entry_sha256": entry_validation["sha256"],
            "canonical_skill_count": EXPECTED_SKILL_COUNT,
            "canonical_skill_bodies_modified": False,
        }
        write_json(package_root / "BUILD_INFO.json", build_info)

        make_deterministic_zip(package_root, output_zip)

    verification = verify_zip(
        output_zip=output_zip,
        entry_sha256=entry_validation["sha256"],
        canonical=canonical,
    )

    print()
    print("Universal Research Skills — ChatGPT Build")
    print("=" * 48)
    print(f"Mode                         : {'RELEASE' if args.release else 'PREVIEW'}")
    print(f"Framework version            : {version}")
    print(f"Canonical skills             : {len(canonical)}")
    print(f"Canonical files modified     : 0")
    print(f"Byte-identical references    : {verification['canonical_reference_matches']}/56")
    print(f"Only root SKILL.md           : PASS")
    print(f"Entry description chars      : {entry_validation['description_chars']}")
    print(f"Git commit                   : {git['commit'] or 'unavailable'}")
    print(f"Git exact tag                : {git['exact_tag'] or 'none'}")
    print(f"Working tree clean           : {git['working_tree_clean']}")
    print(f"ZIP integrity                : {verification['integrity']}")
    print(f"ZIP SHA-256                  : {verification['zip_sha256']}")
    print(f"Output                       : {output_zip}")
    print()

    if not args.release:
        print(
            "PREVIEW ONLY: do not publish this ZIP as a GitHub Release asset. "
            f"For the official release, commit the reviewed v{version} changes, "
            f"tag HEAD v{version}, then run this script with --release."
        )


if __name__ == "__main__":
    main()
