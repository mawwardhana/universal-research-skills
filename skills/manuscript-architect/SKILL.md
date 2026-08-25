---
name: manuscript-architect
description: Design the complete scientific manuscript architecture before prose drafting begins. Use when a study already has sufficiently stable research questions, methods, interpreted results, scientific discussion, contribution, implications, and evidence base, and the researcher needs to determine the article type, argument flow, IMRAD or other section structure, section objectives, claim hierarchy, evidence placement, citation roles, table and figure strategy, reporting-guideline alignment, target-journal constraints, word-budget allocation, title and abstract logic, and handoff requirements for manuscript writing without allowing journal preferences, formatting conventions, citation padding, stylistic polish, or prose generation to alter the scientific question, methods, results, novelty, or conclusions.
---

# Manuscript Architect

## Purpose

`manuscript-architect` designs the scientific manuscript before full prose is written.

Its central question is:

> What manuscript structure, argument sequence, evidence placement, table and figure architecture, reporting logic, and section-level claim hierarchy will communicate the completed study faithfully, efficiently, and transparently without changing the science?

This skill operates after the scientific logic is sufficiently stable.

It does not draft the full manuscript.

It does not silently change:

- research questions;
- hypotheses;
- study design;
- methods;
- results;
- interpretation;
- novelty;
- implications.

---

# Core Principle

Use:

> Architecture before prose.

Preferred sequence:

```text
Completed Scientific Work
      ↓
Article Type
      ↓
Reporting Standard
      ↓
Core Scientific Claim
      ↓
Argument Architecture
      ↓
Section Architecture
      ↓
Evidence Placement
      ↓
Tables / Figures
      ↓
Word Budget
      ↓
Writing Handoff
```

Do not reverse this sequence.

---

# Position in the Framework

Preferred architecture:

```text
result-interpreter
      ↓
scientific-discussion
      ↓
implication-builder
      ↓
manuscript-architect
      ↓
manuscript-writer
```

If a target journal is already known, journal requirements may constrain format, but they must never redefine the science.

---

# Required Upstream Context

Use established information from:

- `research-question-builder`;
- `hypothesis-builder`;
- `theoretical-framework`;
- `conceptual-framework`;
- `methodology-architect`;
- `protocol-builder`;
- `sampling-strategy`;
- `instrument-design`;
- `analysis-planner`;
- `statistical-method-selector`;
- `qualitative-analysis`;
- `mixed-method-analysis`;
- `meta-analysis`;
- `result-interpreter`;
- `scientific-discussion`;
- `implication-builder`;
- `sota-builder`;
- `gap-validator`;
- `novelty-auditor`;
- `source-verification`;
- `reference-integrity-guard`.

Do not ask the researcher to repeat information already established.

---

# Readiness Gate

Classify:

- `READY_FOR_MANUSCRIPT_ARCHITECTURE`
- `RESULTS_INCOMPLETE`
- `DISCUSSION_INCOMPLETE`
- `IMPLICATIONS_INCOMPLETE`
- `NOVELTY_UNCLEAR`
- `METHODS_UNSTABLE`
- `ARTICLE_TYPE_UNCLEAR`
- `REPORTING_STANDARD_UNCLEAR`
- `TARGET_JOURNAL_UNCLEAR_BUT_NOT_REQUIRED`
- `MANUSCRIPT_ARCHITECTURE_REQUIRES_REASSESSMENT`

Do not proceed to full writing if the scientific content is still unstable.

---

# Manuscript Architecture Is Not Manuscript Writing

`manuscript-architect` determines:

- what each section must accomplish;
- what claims belong where;
- which evidence supports each claim;
- which results deserve tables or figures;
- what should not be repeated;
- what should be omitted;
- how the argument should progress.

`manuscript-writer` later turns that architecture into prose.

---

# Article Type Classification

Classify the manuscript before structuring it.

Possible types include:

- original quantitative research;
- original qualitative research;
- mixed-method research;
- randomized trial;
- observational study;
- diagnostic accuracy study;
- prediction model study;
- validation study;
- genetic association study;
- pharmacokinetic study;
- pharmacogenetic study;
- formulation or experimental study;
- systematic review;
- meta-analysis;
- scoping review;
- narrative review;
- methodological paper;
- protocol paper;
- brief report;
- case report;
- implementation study.

---

# Article Type Gate

Do not force every article into the same IMRAD structure.

Use the structure appropriate to the study design and journal.

---

# IMRAD Default

For most original empirical research:

```text
Title
Abstract
Keywords
Introduction
Methods
Results
Discussion
Conclusion
Declarations
References
Tables
Figures
Supplementary Materials
```

---

# IMRAD Logic

Each major section answers a distinct question.

```text
Introduction
→ Why was the study needed?

Methods
→ How was the question answered?

Results
→ What was observed?

Discussion
→ What does it mean?

Conclusion
→ What is the bounded take-home message?
```

Do not mix these functions unnecessarily.

---

# Scientific Narrative Spine

Define the central manuscript logic:

```text
Phenomenon / Problem
      ↓
Current Knowledge
      ↓
Validated Gap
      ↓
Audited Novelty
      ↓
Research Question
      ↓
Methodological Answer
      ↓
Observed Findings
      ↓
Scientific Interpretation
      ↓
Contribution
      ↓
Implications
```

Every section should contribute to this spine.

---

# Core Manuscript Claim

Identify the single highest-level claim the paper can defend.

Use:

```yaml
core_claim:
  statement:
  evidence_basis:
  confidence:
  boundary:
  unsupported_extension:
```

---

# Claim Hierarchy

Classify claims as:

- primary claim;
- secondary claim;
- mechanistic claim;
- methodological claim;
- contextual claim;
- implication claim.

Do not allow secondary claims to overshadow the primary contribution.

---

# Claim Strength

Use:

- `STRONG_DIRECT`
- `MODERATE_DIRECT`
- `TENTATIVE`
- `EXPLORATORY`
- `UNSUPPORTED`

Manuscript language should match this classification.

---

# Research Question Mapping

Every research question should map to:

- method;
- result;
- interpretation;
- discussion;
- conclusion.

Use:

| Research Question | Method | Result | Interpretation | Discussion | Conclusion |
|---|---|---|---|---|---|

---

# Hypothesis Mapping

When hypotheses exist:

| Hypothesis | Analysis | Result | Status | Discussion Location |
|---|---|---|---|---|

Do not omit unsupported hypotheses.

---

# Gap-to-Conclusion Mapping

Use:

```text
Validated Gap
      ↓
Study Contribution
      ↓
Observed Evidence
      ↓
Bounded Conclusion
```

The conclusion should answer the gap, not merely restate statistics.

---

# Novelty Boundary

Import directly from `novelty-auditor`.

Explicitly distinguish:

- what is novel;
- what is not novel.

Do not create novelty during manuscript drafting.

---

# Introduction Architecture

A strong introduction usually progresses:

```text
1. Real-world or scientific problem
2. Current state of knowledge
3. What is established
4. What remains unresolved
5. Why the unresolved issue matters
6. Validated gap
7. Audited novelty
8. Study objective / research question
```

---

# Introduction Function

The introduction should justify the study.

It should not:

- review every article;
- preview every result;
- overstate novelty;
- contain excessive methods detail;
- contain final discussion conclusions.

---

# Introduction Paragraph Logic

Typical structure:

### Paragraph 1 — Problem Significance
Establish the real-world or scientific problem.

### Paragraph 2 — Current Knowledge
Summarize what is established.

### Paragraph 3 — Unresolved Evidence
Show contradiction, limitation, or uncertainty.

### Paragraph 4 — Gap and Novelty
State the validated gap and why the present study is needed.

### Final Paragraph — Objective
State objective, research question, and hypothesis where appropriate.

---

# Phenomenon Evidence in Introduction

Use authoritative phenomenon evidence when needed for:

- burden;
- prevalence;
- trend;
- policy context;
- service gap.

Do not use official statistics to prove scholarly novelty.

---

# Scholarly Evidence in Introduction

Use scholarly literature for:

- mechanisms;
- associations;
- effects;
- theory;
- prior findings;
- unresolved evidence.

---

# Citation Architecture for Introduction

Prioritize:

- foundational evidence where necessary;
- recent high-quality evidence;
- direct comparators;
- systematic reviews;
- current State of the Art.

Avoid citation accumulation.

---

# Introduction Compression

Remove evidence that does not contribute to:

- problem importance;
- current knowledge;
- gap;
- objective.

---

# Methods Architecture

Methods must support reproducibility and auditability.

Typical substructure:

```text
Study Design
Setting
Participants / Materials
Sampling
Variables / Measures
Intervention or Exposure
Data Collection
Laboratory or Field Procedures
Outcomes
Bias Control
Sample Size
Statistical / Qualitative Analysis
Ethics
```

Use only relevant subsections.

---

# Methods Design Fidelity

Methods must match the study actually conducted.

Do not rewrite imperfect methods into idealized methods.

---

# Methods Chronology

Where useful, present methods in the order the study occurred.

---

# Study Design Naming

Use accepted design terminology.

Do not call a study:

- experimental;
- longitudinal;
- prospective;
- causal;

unless the design supports that label.

---

# Participant Architecture

Clarify:

- target population;
- source population;
- eligibility;
- recruitment;
- exclusions;
- final analyzed sample.

---

# Sampling Architecture

Specify:

- sampling frame;
- sampling method;
- sampling unit;
- clustering;
- stratification;
- sample-size rationale.

---

# Measurement Architecture

For each major variable or construct include:

- conceptual definition;
- operational definition;
- instrument;
- units;
- scoring;
- timing;
- validity or reliability when relevant.

---

# Instrument Provenance

State whether instruments were:

- adopted;
- adapted;
- translated;
- modified;
- newly developed.

---

# Intervention Architecture

When applicable specify:

- intervention components;
- dose or intensity;
- duration;
- delivery;
- comparator;
- adherence;
- fidelity.

---

# Laboratory Methods

May include:

- materials;
- equipment;
- manufacturer;
- calibration;
- assay method;
- controls;
- replicate structure;
- detection limits.

---

# Pharmacokinetic Methods

May include:

- dosing;
- sampling schedule;
- bioanalysis;
- PK model;
- compartment assumptions;
- parameter estimation.

---

# Pharmacogenetic Methods

May include:

- DNA extraction;
- genotyping;
- quality control;
- SNP selection;
- genetic model;
- HWE;
- phenotype definition;
- multiple testing.

---

# Qualitative Methods

May include:

- epistemological orientation;
- participant selection;
- data source;
- interview or observation process;
- researcher role;
- transcription;
- coding;
- reflexivity;
- saturation or information power where appropriate;
- trustworthiness.

---

# Mixed-Method Methods

Must state:

- design family;
- priority;
- timing;
- strand relationship;
- integration points;
- joint-display or meta-inference strategy.

---

# Meta-Analysis Methods

May include:

- review question;
- eligibility;
- search;
- screening;
- extraction;
- risk of bias;
- effect measure;
- synthesis model;
- heterogeneity;
- subgroup;
- sensitivity;
- publication bias.

---

# Statistical Analysis Architecture

Methods should report:

- estimand or analysis target;
- statistical model;
- effect measure;
- uncertainty;
- missing data;
- multiplicity;
- diagnostics;
- sensitivity analysis;
- software version.

Do not let software name substitute for statistical method.

---

# Software Placement

Software belongs after the analytical method, not before it.

---

# Reporting Guideline Gate

Determine whether a reporting guideline applies.

Examples include:

- CONSORT;
- STROBE;
- PRISMA;
- STARD;
- TRIPOD;
- CARE;
- COREQ;
- SRQR;
- ARRIVE;
- CHEERS;
- SPIRIT;
- RECORD;
- SAGER.

Use the most appropriate current guideline.

---

# Reporting Guideline Role

Reporting guidelines improve completeness.

They do not determine the scientific design after the fact.

---

# Results Architecture

Results should follow:

- research questions;
- prespecified outcomes;
- analysis logic.

Do not organize results by software output order.

---

# Results Priority

Typical order:

1. sample flow;
2. participant characteristics;
3. primary outcome;
4. secondary outcomes;
5. mechanism, mediation, or moderation;
6. robustness;
7. exploratory analyses.

---

# Results Neutrality

Results should report what was observed.

Avoid:

- causal explanation;
- literature comparison;
- recommendation;
- theoretical storytelling.

Those belong downstream.

---

# Descriptive Results

Use descriptive results to characterize:

- sample;
- distributions;
- exposure;
- outcome;
- baseline.

Do not overload the text with every descriptive statistic.

---

# Primary Result Placement

The primary result should appear early and clearly.

---

# Effect Size First

Report:

- estimate;
- direction;
- magnitude;
- uncertainty.

Then p-value if needed.

---

# Null Results

Report null or inconclusive primary results transparently.

Do not hide them behind secondary findings.

---

# Exploratory Results

Label clearly.

---

# Qualitative Results

Organize around:

- themes;
- categories;
- mechanisms;
- cases.

Use quotations selectively to substantiate findings.

---

# Mixed-Method Results

May present:

- strand-specific results;
- integrated findings;
- joint displays.

Do not call juxtaposition integration.

---

# Meta-Analysis Results

May include:

- PRISMA flow;
- study characteristics;
- risk of bias;
- pooled effects;
- heterogeneity;
- prediction intervals;
- sensitivity;
- publication-bias diagnostics.

---

# Table Strategy

Tables should contain dense structured information.

Good candidates:

- participant characteristics;
- variable definitions;
- model estimates;
- subgroup results;
- sensitivity analyses;
- study characteristics;
- qualitative theme matrix.

---

# Figure Strategy

Figures should clarify relationships or patterns.

Good candidates:

- participant flow;
- conceptual framework;
- path model;
- trend;
- interaction;
- survival curve;
- forest plot;
- funnel plot;
- joint display;
- mechanism diagram.

---

# Table-Figure Redundancy Guard

Do not present identical information in:

- text;
- table;
- figure.

Choose the most efficient representation.

---

# Table Independence

Tables should be interpretable without reading the full manuscript.

---

# Figure Independence

Figures should have clear:

- titles;
- labels;
- legends;
- units;
- abbreviations.

---

# Supplementary Material

Move secondary detail to supplementary material when it improves readability without hiding essential evidence.

Possible items:

- full search strings;
- secondary models;
- sensitivity tables;
- questionnaires;
- detailed protocols;
- additional figures.

---

# Discussion Architecture

Import logic from `scientific-discussion`.

Typical structure:

```text
1. Main finding
2. Comparison with closest evidence
3. Theory / mechanism
4. Divergence / contradiction
5. Secondary findings
6. Robustness
7. Contribution
8. Strengths and limitations
9. Implications
```

---

# Discussion Repetition Guard

Do not repeat the Results section numerically.

---

# Closest Evidence First

Discuss the most scientifically comparable evidence before broad background literature.

---

# Contradictory Evidence

Do not hide contradictory studies.

---

# Theory Placement

Use theory when scientifically justified.

Do not force theory into every manuscript.

---

# Mechanism Placement

Distinguish:

- directly tested;
- indirectly supported;
- plausible;
- speculative.

---

# Implications Placement

Use implications imported from `implication-builder`.

Do not invent recommendations in the writing stage.

---

# Limitations Architecture

Limitations should state:

- limitation;
- affected inference;
- likely consequence.

Avoid ritual limitation lists.

---

# Strengths Architecture

Include only genuine design strengths.

---

# Conclusion Architecture

A conclusion should answer:

- What did the study establish?
- Under what conditions?
- What remains unresolved?

---

# Conclusion Guard

Do not introduce:

- new data;
- new references;
- new theories;
- new claims.

---

# Conclusion Compression

Prefer a bounded conclusion over a broad summary.

---

# Abstract Architecture

Abstract architecture should mirror the manuscript.

Typical structured abstract:

- Background;
- Objective;
- Methods;
- Results;
- Conclusion.

---

# Abstract Fidelity

The abstract must not contain claims absent from the manuscript.

---

# Abstract Result Priority

Include the primary result and meaningful uncertainty.

Do not select only favorable results.

---

# Abstract Conclusion Guard

The abstract conclusion must be no stronger than the full conclusion.

---

# Title Architecture

A strong title reflects:

- primary phenomenon;
- key relationship or intervention;
- population or context when necessary;
- design when useful.

---

# Title Guard

Avoid titles that claim:

- causation from association;
- universal relevance from one context;
- mechanism when not tested.

---

# Keyword Architecture

Keywords should support discoverability.

Prioritize:

- core phenomenon;
- population;
- method;
- major construct;
- discipline-specific indexing term.

Avoid repeating every word from the title.

---

# Word Budget

Allocate words by scientific importance, not habit.

Example for a full original article:

```text
Introduction    12–18%
Methods         20–30%
Results         20–30%
Discussion      25–35%
Conclusion       3–7%
```

Adjust to journal requirements.

---

# Word Budget Guard

Do not compress Methods below reproducibility needs merely to preserve a long Discussion.

---

# Journal-Aware Architecture

If a target journal exists, inspect:

- scope;
- article type;
- word limit;
- abstract format;
- heading structure;
- reference style;
- table and figure limits;
- supplementary policy;
- reporting requirements.

---

# Journal Constraint Hierarchy

Use:

```text
Scientific Integrity
      >
Reporting Completeness
      >
Journal Requirements
      >
Stylistic Preference
```

---

# Journal Scope Guard

Do not distort the scientific question to fit a journal.

---

# Citation Strategy

Citation strategy should follow evidence need.

Do not cite for:

- prestige;
- editorial appeasement;
- target-journal padding;
- APC strategy.

---

# Reference Architecture

Map references by role:

- problem evidence;
- theory;
- mechanism;
- direct comparator;
- contradiction;
- method;
- reporting standard;
- implication context.

---

# Reference Claim Map

Use:

| Claim | Reference | Evidence Role | Verification Status |
|---|---|---|---|

---

# Reference Integrity Gate

No manuscript section should rely on:

- unverifiable sources;
- fabricated citations;
- citation mashups;
- irrelevant references.

---

# Source Recency

Use current evidence where the field changes rapidly.

Retain seminal sources when historically or theoretically necessary.

---

# Citation Chaining

Use citation chaining when a key study has important predecessors or descendants.

---

# No Citation Padding

Target-journal articles may be cited only when scientifically relevant.

---

# Authorship Architecture

Do not infer authorship automatically.

If needed, collect:

- author names;
- order;
- affiliations;
- corresponding author;
- contributions.

---

# CRediT Roles

When required, map contributions using the CRediT taxonomy.

---

# Ethics Statement

Plan placement for:

- ethics approval;
- informed consent;
- trial registration;
- animal approval;
- data privacy.

---

# Funding Statement

Include funding source accurately.

Do not infer funding.

---

# Conflict of Interest

Include conflict declaration according to journal requirements.

---

# Data Availability

Plan a data-availability statement when appropriate.

Possible statuses:

- public repository;
- available on request;
- restricted;
- not applicable.

---

# Code Availability

Include when analysis code is relevant and shareable.

---

# AI Disclosure

If required by journal or institution, include appropriate AI-use disclosure.

Do not invent undisclosed tool use.

---

# Reporting Checklist

When applicable, create a reporting-checklist handoff.

---

# Section Dependency Map

Use:

```yaml
manuscript_sections:
  introduction:
    depends_on:
      - phenomenon_evidence
      - sota
      - gap
      - novelty
      - research_question
  methods:
    depends_on:
      - methodology
      - protocol
      - sampling
      - instrument
      - analysis_plan
  results:
    depends_on:
      - completed_analysis
      - result_interpretation
  discussion:
    depends_on:
      - result_interpretation
      - scientific_discussion
  conclusion:
    depends_on:
      - contribution
      - implications
      - boundaries
```

---

# Section Claim Map

For each section define:

```yaml
section_claim:
  section:
  claim:
  evidence:
  citation_required:
  table_or_figure:
  confidence:
```

---

# Manuscript Logic Audit

Check:

- gap matches objective;
- objective matches methods;
- methods match results;
- results answer objective;
- discussion interprets results;
- conclusion reflects discussion;
- implications reflect evidence strength.

---

# Internal Consistency Audit

Verify repeated values across:

- abstract;
- methods;
- results;
- tables;
- figures;
- discussion;
- conclusion.

---

# Number Consistency

Do not allow different sample sizes, percentages, estimates, or p-values across sections without explanation.

---

# Terminology Consistency

Use one stable term for each construct unless a distinction is intentional.

---

# Acronym Consistency

Define acronyms once and use consistently.

---

# Outcome Naming

Primary and secondary outcomes should retain consistent names.

---

# Population Naming

Do not alternate between broader and narrower population labels carelessly.

---

# Humanized Scientific Writing

Readable scientific writing may:

- vary sentence structure;
- use active voice where appropriate;
- avoid unnecessary nominalization;
- avoid formulaic AI-sounding transitions.

But stylistic naturalness must not alter scientific meaning.

---

# Overclaim Guard

Flag words such as:

- proves;
- confirms;
- demonstrates;
- establishes;
- causes;
- guarantees;

when evidence is weaker than the wording.

---

# Underclaim Guard

Do not weaken a well-supported result merely to sound cautious.

Calibration is preferable to ritual hedging.

---

# Result-to-Discussion Bridge

Each important result should have a corresponding discussion interpretation.

---

# Discussion-to-Implication Bridge

Each implication should trace back to a supported discussion conclusion.

---

# Introduction-to-Discussion Symmetry

The discussion should return to the major unresolved issue introduced earlier.

---

# Abstract-to-Manuscript Symmetry

Every abstract claim should be traceable to the manuscript.

---

# Table-to-Text Symmetry

Text should highlight key results from tables, not duplicate entire tables.

---

# Figure-to-Text Symmetry

Text should interpret figures without narrating every plotted point.

---

# Supplementary Transparency

Do not hide unfavorable results in supplementary material merely to improve narrative.

---

# Outcome Switching Guard

Primary outcomes defined upstream remain primary.

---

# Hypothesis Switching Guard

Prespecified hypotheses remain distinguishable from exploratory hypotheses.

---

# Post-Hoc Analysis Label

Label post-hoc analyses clearly.

---

# Exploratory Manuscript Architecture

Exploratory studies may use a more discovery-oriented narrative.

Do not impose confirmatory language.

---

# Qualitative Manuscript Architecture

A qualitative paper may emphasize:

- context;
- reflexivity;
- analytic process;
- themes;
- conceptual development.

Do not force quantitative conventions.

---

# Mixed-Method Manuscript Architecture

Mixed-method manuscripts should show actual integration.

Possible architecture:

```text
Methods
  Quantitative strand
  Qualitative strand
  Integration

Results
  Quantitative findings
  Qualitative findings
  Joint interpretation

Discussion
  Meta-inferences
```

---

# Review Manuscript Architecture

Review articles require architecture based on review type.

Do not force primary-study Methods conventions when inappropriate.

---

# Systematic Review Architecture

Use PRISMA-aligned structure.

---

# Meta-Analysis Architecture

Include synthesis logic and heterogeneity interpretation.

---

# Narrative Review Architecture

Narrative reviews require transparent scope and evidence-selection logic.

Do not masquerade as systematic review.

---

# Methodological Paper Architecture

May emphasize:

- problem;
- method development;
- validation;
- benchmarking;
- limitations.

---

# Short Communication Architecture

Prioritize one clear contribution.

Remove secondary material.

---

# Multi-Study Paper Architecture

When several studies appear in one paper, maintain:

- shared introduction;
- study-specific methods and results;
- integrated discussion.

---

# Manuscript Blueprint

Recommended output:

```yaml
manuscript_blueprint:
  article_type:
  reporting_guideline:
  target_journal:
  core_claim:
  validated_gap:
  audited_novelty:
  research_questions:
  hypotheses:
  title_logic:
  abstract_structure:
  introduction_plan:
  methods_plan:
  results_plan:
  discussion_plan:
  conclusion_plan:
  tables:
  figures:
  supplementary_materials:
  word_budget:
  reference_strategy:
  declaration_sections:
  unresolved_inputs:
  manuscript_writer_handoff:
```

---

# Introduction Blueprint

Use:

```yaml
introduction:
  paragraph_1_problem:
  paragraph_2_current_knowledge:
  paragraph_3_unresolved_issue:
  paragraph_4_gap_and_novelty:
  final_objective:
```

---

# Methods Blueprint

Use:

```yaml
methods:
  design:
  setting:
  participants_or_materials:
  sampling:
  measurement:
  intervention_or_exposure:
  procedures:
  outcomes:
  bias_control:
  sample_size:
  analysis:
  ethics:
```

---

# Results Blueprint

Use:

```yaml
results:
  sample_flow:
  descriptive_results:
  primary_results:
  secondary_results:
  mechanism_results:
  robustness_results:
  exploratory_results:
```

---

# Discussion Blueprint

Use:

```yaml
discussion:
  main_finding:
  closest_evidence:
  theory:
  mechanism:
  contradiction:
  secondary_findings:
  robustness:
  contribution:
  limitations:
  implications:
```

---

# Table Blueprint

Use:

```yaml
table:
  number:
  title:
  scientific_role:
  variables:
  notes:
  source_results:
```

---

# Figure Blueprint

Use:

```yaml
figure:
  number:
  title:
  scientific_role:
  data_source:
  visual_form:
  required_labels:
```

---

# Writing Handoff

Pass to `manuscript-writer`:

```yaml
manuscript_writer_handoff:
  article_type:
  target_journal:
  reporting_guideline:
  word_limit:
  core_claim:
  section_order:
  section_objectives:
  paragraph_plan:
  claim_map:
  citation_map:
  tables:
  figures:
  supplementary_materials:
  terminology:
  required_declarations:
  prohibited_claims:
  uncertainty_language:
```

---

# Minimal Output

For a simple request provide:

## Article Type
[...]

## Core Claim
[...]

## Recommended Structure
[...]

## Introduction Logic
[...]

## Methods Logic
[...]

## Results Logic
[...]

## Discussion Logic
[...]

## Tables / Figures
[...]

## Writing Handoff
[...]

---

# Comprehensive Output

When a full architecture is requested provide:

## A. Article Type
[...]

## B. Reporting Guideline
[...]

## C. Target Journal Constraints
[...]

## D. Core Claim
[...]

## E. Validated Gap
[...]

## F. Audited Novelty
[...]

## G. Research Question Map
[...]

## H. Hypothesis Map
[...]

## I. Title Architecture
[...]

## J. Abstract Architecture
[...]

## K. Introduction Blueprint
[...]

## L. Methods Blueprint
[...]

## M. Results Blueprint
[...]

## N. Discussion Blueprint
[...]

## O. Conclusion Blueprint
[...]

## P. Table Plan
[...]

## Q. Figure Plan
[...]

## R. Supplementary Plan
[...]

## S. Word Budget
[...]

## T. Citation Architecture
[...]

## U. Reporting Checklist
[...]

## V. Declarations
[...]

## W. Consistency Checks
[...]

## X. Manuscript Writer Handoff
[...]

---

# Relationship with Implication Builder

`implication-builder` determines what the findings legitimately imply.

`manuscript-architect` decides where and how those implications belong in the manuscript.

---

# Relationship with Result Interpreter

Import only supported claims.

Do not reconstruct interpretation from raw software output.

---

# Relationship with Scientific Discussion

Use the discussion logic already established.

Do not create new explanatory mechanisms merely for narrative elegance.

---

# Relationship with SOTA Builder

Use the State of the Art to structure Introduction and Discussion evidence.

---

# Relationship with Gap Validator

The validated gap anchors the Introduction and contribution.

---

# Relationship with Novelty Auditor

The audited novelty defines the contribution boundary.

---

# Relationship with Methodology Architect

Methods architecture must remain faithful to the actual study design.

---

# Relationship with Analysis Planner

Results architecture should reflect the intended analyses and estimands.

---

# Relationship with Reference Integrity Guard

Only verified and claim-relevant references should enter the manuscript architecture.

---

# Relationship with Journal Matcher

If a target journal is not yet chosen, manuscript architecture may remain journal-neutral.

A later `journal-matcher` may identify suitable journals.

---

# Relationship with Manuscript Writer

`manuscript-architect` defines what must be written.

`manuscript-writer` writes it.

The writer must not silently change the architecture.

---

# User-Friendly Behavior

Prefer:

> Your study is ready for manuscript architecture, but not yet for full prose. I will first map the validated gap, primary result, discussion claim, and implication into a section-by-section blueprint. This prevents the writing stage from changing the science.

Or:

> The journal requires a 3,000-word original article. The scientific content should therefore be compressed mainly by moving secondary analyses to supplementary material, not by removing reproducibility-critical methods.

Or:

> The study has three research questions, but only one central manuscript claim. I will structure the Results around the three questions while keeping the Discussion centered on the single contribution that connects them.

---

# Avoid These Behaviors

Do not:

- start full prose before architecture is stable;
- invent missing results;
- invent references;
- invent novelty;
- change the research question for narrative convenience;
- change the method to make it look stronger;
- hide null results;
- hide contradictory results;
- elevate secondary findings over primary findings;
- rewrite exploratory results as confirmatory;
- use journal preferences to alter science;
- use APC status to alter scientific content;
- add target-journal citations for strategic padding;
- organize Results by software output order;
- repeat the same data in text, tables, and figures;
- force IMRAD when another architecture is scientifically appropriate;
- force theory when theory is not central;
- make causal titles from associational studies;
- write stronger abstract conclusions than full-manuscript conclusions;
- place new claims in the conclusion;
- compress Methods below reproducibility needs;
- hide unfavorable evidence in supplementary material.

---

# Stop Conditions

Do not classify the architecture as ready when:

- research question is unstable;
- methods are incomplete;
- results are incomplete;
- interpretation is incomplete;
- discussion is incomplete;
- implications are incomplete;
- validated gap is unknown;
- audited novelty is unknown;
- primary claim cannot be identified;
- article type is incompatible with the study;
- reporting standard is required but unknown;
- tables and figures cannot be mapped to results;
- internal numerical inconsistencies remain unresolved;
- unsupported claims are being preserved for publication strategy.

Use:

- `RETURN_TO_RESEARCH_QUESTION_BUILDER`
- `RETURN_TO_METHODOLOGY_ARCHITECT`
- `RETURN_TO_ANALYSIS_PLANNER`
- `RETURN_TO_RESULT_INTERPRETER`
- `RETURN_TO_SCIENTIFIC_DISCUSSION`
- `RETURN_TO_IMPLICATION_BUILDER`
- `RETURN_TO_GAP_VALIDATOR`
- `RETURN_TO_NOVELTY_AUDITOR`
- `MANUSCRIPT_ARCHITECTURE_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`manuscript-architect` succeeds when a scientifically stable study has been converted into a complete, transparent, journal-compatible but science-preserving manuscript blueprint that explicitly defines the article type, reporting guideline, core claim, validated gap, audited novelty, research-question and hypothesis mapping, title logic, abstract architecture, Introduction logic, Methods structure, Results sequence, Discussion logic, Conclusion boundaries, citation roles, table and figure strategy, supplementary-material plan, word budget, declaration requirements, internal-consistency checks, prohibited claims, and a complete handoff to `manuscript-writer`, while preventing writing convenience, journal preferences, citation padding, stylistic polish, software output, target-journal strategy, or publication pressure from redefining the research question, methods, results, interpretation, novelty, or conclusions.
