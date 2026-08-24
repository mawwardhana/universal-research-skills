---
name: gap-validator
description: Stress-test candidate research gaps against current verified evidence by actively searching for studies, terminology, methods, populations, mechanisms, and adjacent research that could invalidate or substantially weaken the proposed gap. Use after gap discovery and before novelty construction, research-question finalization, continuation-study selection, research-roadmap development, or claims that a meaningful research gap exists.
---

# Research Gap Validator

## Purpose

`gap-validator` determines whether a candidate research gap remains scientifically defensible after deliberate attempts to disprove it.

Its central question is:

> If we actively search for evidence that could close, weaken, reframe, or invalidate this proposed gap, does the gap still remain?

The purpose is not to defend the researcher's preferred gap.

The purpose is to challenge it.

A candidate gap should survive:

- terminology expansion;
- current literature searching;
- closest-competitor searching;
- citation chaining;
- adjacent-discipline searching;
- methodological-equivalent searching;
- population and context comparison;
- evidence synthesis.

Only then may the framework classify it as a validated gap.

---

# Core Principle

Use:

> Try to falsify the gap before trying to publish it.

The framework should prefer:

> "This proposed gap is already substantially addressed."

over manufacturing novelty from incomplete searching.

A rejected gap is a successful validation outcome.

---

# Required Upstream Context

Prefer inputs from:

`scopus-literature-search`
→ `source-verification`
→ `reference-integrity-guard`
→ `citation-chaining`
→ `literature-screening`
→ `evidence-synthesis`
→ `sota-builder`
→ `gap-discovery`

Minimum useful inputs include:

- candidate gap statement;
- gap type;
- established knowledge;
- unresolved condition;
- scientific consequence;
- closest known studies;
- search terminology;
- evidence coverage;
- false-gap risks.

---

# Activation Conditions

Use when:

- a candidate research gap has been proposed;
- the user asks whether a gap is genuine;
- novelty depends on a specific gap;
- a previous paper's limitation is being reused;
- a future-research recommendation is being considered;
- a new population or context is proposed;
- a mediator or moderator is claimed as a gap;
- a method or technology is claimed as novel;
- continuation research requires confirmation that the issue remains open.

Typical requests include:

- "Is this really a research gap?"
- "Has anyone already studied this?"
- "Can I claim this as my gap?"
- "Validate my research gap."
- "Is this still novel?"
- "Has this limitation already been addressed?"
- "Can I use this gap in my manuscript?"

---

# Gap Validation Philosophy

Validation is adversarial.

Do not ask:

> What literature supports the gap?

First ask:

> What literature could invalidate the gap?

Only after attempting falsification should supporting evidence be synthesized.

---

# Candidate Gap Status

Input status should normally be:

`CANDIDATE_GAP`

Possible final statuses are:

- `VALIDATED_STRONG_GAP`
- `VALIDATED_MODERATE_GAP`
- `PARTIALLY_VALIDATED_GAP`
- `REFRAMED_GAP`
- `WEAK_GAP`
- `GAP_SUBSTANTIALLY_RESOLVED`
- `GAP_REJECTED`
- `VALIDATION_INCONCLUSIVE`

Do not force every candidate into a positive validation outcome.

---

# 1. Normalize the Gap Statement

Rewrite the candidate gap into a testable scientific structure.

Recommended form:

> Existing evidence establishes **A**, but remains insufficient or inconsistent regarding **B**, especially under **C**, limiting the ability to **D**.

Where:

- A = established knowledge;
- B = unresolved scientific condition;
- C = scientifically meaningful boundary;
- D = consequence.

Do not strengthen the gap during normalization.

Preserve its actual meaning.

---

# 2. Extract Gap Components

Represent conceptually:

```yaml
gap:
  established_knowledge:
  unresolved_condition:
  boundary:
  scientific_consequence:
  proposed_gap_type: