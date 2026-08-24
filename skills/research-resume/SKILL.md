---

name: research-resume
description: Restore the state of an existing research project or research program from previous articles, theses, dissertations, proposals, datasets, reports, roadmaps, or other prior materials. Use when a researcher wants to continue previous work without restarting, recover what materials and stages already exist, determine what needs re-evaluation, and route the project toward scientific audit, current literature updating, continuation planning, or roadmap development.
---

# Research Resume

## Purpose

`research-resume` restores the working state of an existing research project or research program.

Its primary responsibility is **research continuity**, not deep scientific auditing.

It determines:

1. what previous research materials are available;
2. which research project or research line they belong to;
3. what stages of research have already been completed;
4. what decisions have already been made;
5. what outputs already exist;
6. what remains unresolved;
7. which downstream skill should examine the previous research in detail;
8. what information should be preserved in the Research Passport.

The researcher should not be forced to restart work that has already been completed.

---

# Core Principle

Use:

> Recover first. Audit second. Update evidence third. Continue fourth.

`research-resume` restores research context.

It does **not** independently determine that:

* a previous limitation is a current research gap;
* an old recommendation remains novel;
* an old theory remains State of the Art;
* a proposed continuation is scientifically justified.

Those decisions belong to downstream evidence and audit skills.

---

# Activation Conditions

Use this skill when the researcher:

* uploads a previous journal article;
* uploads a thesis or dissertation;
* provides a completed research report;
* provides a previous proposal;
* provides a dataset from earlier research;
* provides a research roadmap;
* provides several related publications;
* wants to continue previous research;
* asks what should be studied next;
* wants to build a research trajectory;
* returns to an interrupted research project.

Typical user requests include:

* "Continue my previous research."
* "This is my last article. What should I do next?"
* "I want to continue my dissertation topic."
* "Help me build a roadmap from my previous studies."
* "I already have several papers in this field."
* "I stopped this project last year. Help me continue."

---

# Research Resume Is Not a Summary Skill

Do not simply summarize the uploaded document.

The immediate goal is to establish:

* what the material represents;
* where the project stopped;
* what has already been completed;
* which scientific components require detailed audit;
* what should happen next.

Detailed scientific evaluation belongs to:

`prior-research-auditor`

---

# Material Inventory

Identify available materials.

Possible materials include:

## Research Outputs

* journal article;
* conference paper;
* thesis;
* dissertation;
* research report;
* monograph;
* book chapter;
* preprint.

## Research Planning Materials

* proposal;
* protocol;
* ethics application;
* grant application;
* conceptual framework;
* research roadmap.

## Data Materials

* dataset;
* codebook;
* laboratory data;
* survey data;
* qualitative transcripts;
* secondary data;
* analysis output.

## Research Instruments

* questionnaire;
* scale;
* interview guide;
* observation sheet;
* laboratory protocol;
* assessment instrument.

## Publication Materials

* manuscript;
* reviewer comments;
* response-to-reviewer file;
* journal decision letter.

Do not ask the user to re-enter information that can be recovered from these materials.

---

# Project Identification

Determine whether the provided materials represent:

* one completed study;
* one active study;
* several studies from the same research line;
* several unrelated studies;
* a thesis-to-publication project;
* a publication-to-follow-up project;
* a grant-funded research program;
* a long-term research portfolio.

When uncertain, ask only the minimum clarification needed.

---

# Research Continuity Status

Classify the project approximately as:

* `COMPLETED_SINGLE_STUDY`
* `ONGOING_STUDY`
* `INTERRUPTED_STUDY`
* `MULTI_STUDY_RESEARCH_LINE`
* `RESEARCH_PROGRAM`
* `MANUSCRIPT_STAGE`
* `REVISION_STAGE`
* `UNKNOWN`

---

# Existing Research Stage Detection

Determine which stages appear to have been completed.

Possible stages include:

* research interest identified;
* topic selected;
* research problem formulated;
* literature reviewed;
* State of the Art developed;
* research gap proposed;
* novelty proposed;
* research questions formulated;
* hypotheses formulated;
* theoretical framework developed;
* conceptual framework developed;
* methodology designed;
* protocol completed;
* ethics approval obtained;
* data collected;
* analysis completed;
* results interpreted;
* manuscript drafted;
* manuscript submitted;
* reviewer comments received;
* study published.

Do not mark a stage as completed unless the material supports it.

---

# Research Stage Status

For each relevant stage, use:

* `COMPLETED`
* `PARTIALLY_COMPLETED`
* `REQUIRES_REVALIDATION`
* `NOT_STARTED`
* `UNKNOWN`

Examples:

A research gap stated in a three-year-old paper may be:

`REQUIRES_REVALIDATION`

A completed dataset may indicate:

`DATA_COLLECTION: COMPLETED`

but:

`ANALYSIS: NOT_STARTED`

---

# Previous Research Material Age

Record publication or completion dates where available.

Older material does not automatically become invalid.

However, elements such as:

* literature review;
* State of the Art;
* research gap;
* novelty;
* journal landscape;

may require updating.

Use:

`CURRENT_LITERATURE_REFRESH_REQUIRED`

when appropriate.

---

# Do Not Trust Historical Gaps Automatically

If a previous article states:

"Few studies have examined X."

do not assume this remains true today.

Record:

`historical_gap_claim: REQUIRES_REVALIDATION`

Likewise, author recommendations for future research should initially be treated as:

`HISTORICAL_FUTURE_DIRECTION`

not:

`CURRENT_RESEARCH_OPPORTUNITY`

---

# Single Previous Study

When one previous study is provided, the typical route is:

`research-resume`
→ `prior-research-auditor`

The auditor will examine:

* what was actually established;
* methodological strength;
* major findings;
* limitations;
* negative findings;
* unexpected findings;
* continuation signals.

Do not duplicate that detailed audit here.

---

# Multiple Previous Studies

When multiple related studies are provided:

1. inventory all studies;
2. establish approximate chronology;
3. identify whether they belong to the same research line;
4. preserve their relationships;
5. route individual studies for necessary audit;
6. then route toward:

`research-trajectory-mapper`

Do not generate separate isolated summaries when the user's goal is a research trajectory.

---

# Research Portfolio Awareness

When several outputs appear related, record signals such as:

* recurring topic;
* recurring population;
* recurring methodology;
* recurring theoretical framework;
* sequence of studies;
* publication chronology.

Do not interpret the trajectory deeply here.

That belongs to:

`research-trajectory-mapper`

---

# Current Literature Refresh

A continuation workflow normally requires updated literature.

Typical route:

`prior-research-auditor`
→ `research-trajectory-mapper` when needed
→ `citation-chaining`
→ `scopus-literature-search`
→ `source-verification`
→ `research-landscape`
→ `sota-builder`

This determines how the field has evolved since the prior research.

---

# Scopus-First Policy

When the continuation workflow reaches literature updating, prioritize:

1. relevant peer-reviewed articles from active Scopus-indexed journals;
2. recent systematic reviews or meta-analyses when appropriate;
3. recent high-quality primary studies;
4. important seminal literature;
5. forward citations of the prior study;
6. contradictory and competing evidence.

Other scholarly services may be used for discovery and verification.

Never claim Scopus indexing without verification.

---

# Publication Awareness

If the researcher intends international publication, preserve:

`scopus_preference: true`

When publication cost is important, preserve:

`prefer_no_mandatory_apc: true`

These preferences should later inform journal matching.

Do not select the target journal during research resume unless journal selection is the user's immediate goal.

---

# No-Mandatory-APC Preference

The framework later prefers scientifically appropriate journals that offer publication without mandatory APC when comparable choices exist.

Possible status:

* `NO_MANDATORY_APC`
* `OPTIONAL_APC_HYBRID`
* `MANDATORY_APC`
* `APC_UNVERIFIED`

Current publication policy must be verified before making a recommendation.

---

# Target Journal Awareness

If the researcher already has a target journal, preserve that information.

Later skills may examine its relevant literature to understand:

* scholarly conversation;
* topic fit;
* methodological fit;
* unresolved questions;
* potential contribution alignment.

Do not add citations merely because they originate from the target journal.

---

# Research Resume Brief

When useful, produce:

## Research Resume Brief

**Project status:**
[...]

**Previous research materials identified:**
[...]

**Primary previous study/studies:**
[...]

**Approximate research line:**
[...]

**Completed stages:**
[...]

**Partially completed stages:**
[...]

**Stages requiring revalidation:**
[...]

**Existing data:**
[...]

**Existing analysis:**
[...]

**Existing manuscript:**
[...]

**Historical gap claims requiring revalidation:**
[...]

**Current literature refresh required:**
[...]

**Trajectory mapping required:**
[...]

**Publication preference:**
[...]

**Next recommended workflow:**
[...]

---

# Research Passport Update

When supported, update:

```yaml
research:
  entry_mode: CONTINUE_PREVIOUS_RESEARCH
  project_status:
  research_line:

prior_materials:
  publications:
  thesis_or_dissertation:
  proposals:
  datasets:
  instruments:
  analysis_outputs:
  manuscripts:
  roadmaps:

workflow:
  completed_stages:
  partially_completed_stages:
  stages_requiring_revalidation:
  current_stage:
  next_stage:

continuation:
  prior_research_audit_required:
  trajectory_mapping_required:
  current_literature_refresh_required:

publication:
  scopus_preference:
  prefer_no_mandatory_apc:
  target_journals:
```

Do not invent unknown values.

---

# Provenance

Maintain provenance whenever reconstructing project status.

Use:

* `USER_PROVIDED`
* `SOURCE_EXPLICIT`
* `SOURCE_INFERRED`
* `ANALYTICAL_INFERENCE`

Do not present inference as explicit source information.

---

# Routing Logic

## One prior study

Route to:

`prior-research-auditor`

## Several related studies

Route to:

`prior-research-auditor`
→ `research-trajectory-mapper`

## Literature is outdated

Route later to:

`citation-chaining`
→ `scopus-literature-search`
→ `source-verification`

## Current gap must be established

Route later to:

`sota-builder`
→ `gap-discovery`
→ `gap-validator`

## Continuation alternatives are needed

Route later to:

`continuation-opportunity-finder`

## Long-term agenda is needed

Route later to:

`research-program-builder`
→ `research-roadmap`

---

# Do Not Do These Things

Do not:

* repeat a full scientific audit already assigned to another skill;
* summarize previous research and stop;
* assume historical gaps remain current;
* assume previous future-research recommendations remain novel;
* invent missing project history;
* restart completed stages unnecessarily;
* discard previous valid work;
* select methodology before determining what remains scientifically unresolved;
* prioritize publication strategy over scientific validity.

---

# User-Friendly Behavior

Do not expose unnecessary internal skill names.

Instead of:

"I am routing from research-resume to prior-research-auditor."

Prefer:

"I've identified this as a continuation of your previous research. The next step is to examine what that study genuinely established and which parts still need to be checked against current literature."

---

# Success Criterion

`research-resume` succeeds when the framework has accurately recovered enough of the previous research state to continue from the correct stage, preserve valid prior work, identify what requires revalidation, and route the researcher toward the next scientifically appropriate workflow without unnecessary repetition.
