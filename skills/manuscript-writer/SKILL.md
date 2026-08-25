---
name: manuscript-writer
description: Write or revise a scientific manuscript from an approved manuscript architecture while preserving the underlying science exactly. Use when the manuscript blueprint, methods, interpreted results, scientific discussion, implications, evidence map, and relevant journal or reporting constraints are sufficiently stable and the researcher needs publication-ready prose, section drafting, controlled rewriting, compression, expansion, or scientific translation without inventing data or references, altering methods, changing outcome priority, upgrading exploratory findings to confirmatory claims, exaggerating novelty, hiding null or contradictory findings, or allowing stylistic polish, journal preferences, citation pressure, or AI-generated fluency to redefine the scientific record.
---

# Manuscript Writer

## Purpose

`manuscript-writer` turns an approved manuscript architecture into scientifically faithful prose.

Its central question is:

> How should the approved scientific content be written clearly, coherently, efficiently, and publication-readily without changing what the study actually asked, did, found, means, or legitimately implies?

This skill operates after:

- `manuscript-architect`.

It writes the manuscript.

It does not redesign the study.

---

# Core Principle

Use:

> Write the approved science. Do not rewrite the science.

Preferred sequence:

```text
Approved Manuscript Architecture
      ↓
Section Objective
      ↓
Approved Claims
      ↓
Verified Evidence
      ↓
Approved Results
      ↓
Calibrated Language
      ↓
Scientific Prose
      ↓
Consistency Check
      ↓
Manuscript Audit Handoff
```

---

# Position in the Framework

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
      ↓
manuscript-auditor
```

---

# Required Upstream Context

Use established information from:

- `manuscript-architect`;
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
- `phenomenon-evidence-builder`;
- `sota-builder`;
- `gap-validator`;
- `novelty-auditor`;
- `source-verification`;
- `reference-integrity-guard`;
- `citation-chaining`.

Do not ask the researcher to repeat information already available.

---

# Readiness Gate

Classify:

- `READY_TO_WRITE`
- `ARCHITECTURE_INCOMPLETE`
- `RESULTS_INCOMPLETE`
- `DISCUSSION_INCOMPLETE`
- `IMPLICATIONS_INCOMPLETE`
- `REFERENCE_SUPPORT_INCOMPLETE`
- `METHODS_UNSTABLE`
- `TARGET_JOURNAL_UNKNOWN_BUT_NOT_REQUIRED`
- `REPORTING_REQUIREMENTS_UNCLEAR`
- `EXISTING_MANUSCRIPT_REQUIRES_ALIGNMENT`
- `WRITING_REQUIRES_REVISION`

Do not generate polished prose when the scientific content is unresolved.

---

# Writing Modes

Classify the request as one or more of:

- `WRITE_NEW_MANUSCRIPT`
- `WRITE_SECTION`
- `CONTINUE_EXISTING_MANUSCRIPT`
- `REWRITE_SECTION`
- `COMPRESS_SECTION`
- `EXPAND_SECTION`
- `IMPROVE_COHERENCE`
- `IMPROVE_ACADEMIC_STYLE`
- `TRANSLATE_SCIENTIFICALLY`
- `ADAPT_TO_JOURNAL`
- `RESTRUCTURE_TO_BLUEPRINT`
- `WRITE_ABSTRACT`
- `WRITE_TITLE`
- `WRITE_CONCLUSION`

---

# Existing Manuscript Gate

When an existing manuscript is supplied:

1. preserve supported content;
2. identify architecture conflicts;
3. identify unsupported claims;
4. identify duplicated content;
5. identify missing required content;
6. revise only what the task requires.

Do not silently overwrite the scientific record.

---

# Approved Blueprint Requirement

Use the handoff from `manuscript-architect`.

Expected fields may include:

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

Unknown fields remain unknown.

---

# Scientific Fidelity Rule

Never change:

- sample size;
- group definitions;
- variable names;
- outcome priority;
- intervention;
- comparator;
- exposure;
- methods;
- analysis model;
- effect estimates;
- uncertainty;
- p-values;
- qualitative themes;
- hypothesis status;
- direction of findings;
- novelty boundary;
- causal status;
- limitations;

unless the user explicitly provides corrected source information.

---

# Data Integrity Guard

Do not invent:

- sample sizes;
- means;
- medians;
- standard deviations;
- confidence intervals;
- odds ratios;
- hazard ratios;
- regression coefficients;
- p-values;
- loading values;
- fit indices;
- themes;
- quotations;
- participant characteristics;
- laboratory parameters;
- sequence data;
- dates;
- ethics approval numbers.

If missing, mark it as missing.

---

# Reference Integrity Guard

Do not invent:

- authors;
- article titles;
- journals;
- years;
- DOIs;
- PMIDs;
- URLs;
- volume;
- issue;
- pages.

Use only references that are supplied, retrieved, verified, or explicitly marked as temporary placeholders.

---

# Citation Placeholder Rule

When evidence is required but no verified reference is available, use:

```text
[CITATION NEEDED: current evidence on ...]
```

Do not fabricate citations.

---

# Citation Claim Matching

Every citation should support the specific claim associated with it.

---

# Citation Roles

Classify references as:

- problem evidence;
- theory;
- mechanism;
- prior finding;
- direct comparator;
- contradictory evidence;
- methodology;
- reporting guideline;
- implication context.

---

# No Citation Padding

Do not add citations merely because:

- the target journal published them;
- an author is prominent;
- the journal is prestigious;
- more references appear more scholarly.

---

# APC Independence

APC status must not influence scientific content or reference selection.

---

# Journal Independence

Journal fit may affect:

- length;
- headings;
- abstract format;
- table count;
- reference style.

Journal fit must not affect:

- results;
- novelty;
- causal interpretation;
- effect magnitude;
- conclusion strength.

---

# Scientific Writing Standard

Prioritize:

- accuracy;
- clarity;
- traceability;
- coherence;
- economy;
- proportionality.

---

# Humanized Scientific Writing

Prefer:

- varied sentence structure;
- precise verbs;
- clear topic sentences;
- logical transitions;
- restrained emphasis;
- discipline-appropriate terminology.

Avoid:

- repetitive sentence openings;
- formulaic AI transitions;
- inflated vocabulary;
- unnecessary nominalization;
- ornamental complexity.

---

# Precision over Ornament

Prefer:

> MTX response differed across genotype groups.

over:

> A remarkably profound differentiation in MTX responsiveness was observed across distinct genotypic classifications.

---

# Voice

Use active voice when the actor matters.

Use passive voice when the process or result matters more.

Do not enforce one voice mechanically.

---

# Tense Logic

Typical use:

- established knowledge: present;
- methods performed: past;
- results observed: past;
- interpretation: present or cautious present;
- implications: modal or conditional.

---

# Terminology Consistency

Use approved terminology consistently.

Do not alternate between scientifically different terms for stylistic variety.

---

# Abbreviation Rule

Define abbreviations at first appropriate use.

Avoid unnecessary abbreviations.

---

# Statistical Reporting

Prefer:

```text
estimate
→ direction
→ uncertainty
→ p-value when relevant
```

Do not lead with significance alone.

---

# P-Value Guard

Avoid:

> X significantly affected Y.

when causal language is unsupported.

Prefer:

> X was associated with Y (β = ..., 95% CI ..., p = ...).

---

# Non-Significance Language

Avoid:

> There was no effect.

when evidence only shows non-significance.

Prefer:

> The estimate was imprecise and the confidence interval included the null.

---

# Clinical and Practical Significance

Do not infer clinical or practical importance from statistical significance alone.

---

# Causal Language Gate

Use causal verbs only if justified by:

- design;
- assumptions;
- analysis;
- interpretation.

---

# Associational Language

Prefer:

- associated with;
- related to;
- correlated with;
- linked to;
- predicted;
- differed by;

according to the analysis.

---

# Prediction Language

Prediction is not explanation.

Do not write:

> X explains Y

when the model only predicts Y.

---

# Mediation Language

Do not call a statistical indirect effect a proven mechanism unless temporal and causal assumptions support it.

---

# Moderation Language

Describe moderation as conditional association or effect modification according to design.

---

# SEM Writing Guard

Do not convert path coefficients automatically into causal claims.

---

# PLS-SEM Writing Guard

Do not treat:

- path significance;
- R²;
- Q²;
- f²;

as proof of causal or practical importance.

---

# Qualitative Writing Guard

Do not reduce qualitative findings to:

- frequency counting;
- generic themes;
- unsupported universality.

Preserve context, variation, negative cases, participant meaning, and analytic interpretation.

---

# Mixed-Method Writing Guard

Do not write quantitative and qualitative strands as two unrelated mini-studies when integration is required.

---

# Meta-Analysis Writing Guard

Do not treat pooled estimates as universally transportable.

Report heterogeneity, risk of bias, and prediction intervals where appropriate.

---

# Pharmacogenetic Writing Guard

Do not recommend routine genotyping unless clinical validity and utility support it.

---

# Pharmacokinetic Writing Guard

Do not convert PK differences directly into dose recommendations without adequate PK/PD or clinical evidence.

---

# Formulation Writing Guard

Do not convert physicochemical performance directly into clinical efficacy.

---

# Antimicrobial Writing Guard

Do not describe inhibition-zone findings as therapeutic efficacy.

---

# Introduction Writing

The Introduction should answer:

> Why was this study necessary?

Preferred logic:

```text
Problem
      ↓
Current Knowledge
      ↓
Unresolved Evidence
      ↓
Validated Gap
      ↓
Audited Novelty
      ↓
Objective
```

---

# Introduction Paragraph Logic

### Paragraph 1
Problem significance.

### Paragraph 2
Current knowledge.

### Paragraph 3
Unresolved evidence.

### Paragraph 4
Validated gap and scientific need.

### Final Paragraph
Objective, research question, and hypothesis where appropriate.

---

# Introduction Novelty Guard

Do not write:

> No previous study has ever...

unless comprehensively verified.

Prefer:

> Evidence remains limited regarding...

when that is the defensible position.

---

# Introduction Citation Density

Use the minimum number of strong references needed to support the scientific logic.

---

# Methods Writing

The Methods section should enable a competent researcher to understand and, where possible, reproduce the study.

---

# Methods Fidelity

Write what was done.

Do not write what ideally should have been done.

---

# Methods Design Statement

State:

- design;
- setting;
- period;
- population or materials.

---

# Participant Writing

Report:

- inclusion;
- exclusion;
- recruitment;
- final sample.

---

# Sampling Writing

Describe:

- sampling approach;
- frame;
- unit;
- rationale.

---

# Variable Writing

Define:

- exposure;
- outcome;
- covariates;
- moderator;
- mediator;
- control variables.

---

# Instrument Writing

Report:

- instrument name;
- version;
- scoring;
- administration;
- validity;
- reliability;
- adaptation;

only when supported.

---

# Laboratory Writing

Report methods with sufficient detail for reproducibility.

Do not invent manufacturer information.

---

# Intervention Writing

Include:

- content;
- dose or intensity;
- frequency;
- duration;
- comparator;
- fidelity;

when applicable.

---

# Statistical Methods Writing

State:

- analysis objective;
- model;
- effect measure;
- assumptions;
- missing-data handling;
- multiplicity;
- sensitivity analyses;
- software.

---

# Software Rule

Write the method before the software.

Preferred:

> Multivariable logistic regression was used to estimate adjusted odds ratios. Analyses were performed in ...

---

# Qualitative Methods Writing

Describe:

- orientation;
- data generation;
- researcher role;
- coding;
- analytic process;
- reflexivity;
- trustworthiness.

---

# Mixed-Method Methods Writing

Explicitly describe:

- design;
- priority;
- timing;
- integration;
- meta-inference.

---

# Review Methods Writing

For systematic reviews preserve:

- search;
- selection;
- extraction;
- risk of bias;
- synthesis logic.

---

# Results Writing

The Results section answers:

> What was observed?

Do not explain why it happened.

---

# Result Ordering

Typical order:

1. sample flow;
2. participant characteristics;
3. primary outcome;
4. secondary outcomes;
5. mechanism or interaction;
6. robustness;
7. exploratory analyses.

---

# Primary Result Rule

Give the primary result clear prominence.

---

# Result Sentence Logic

A strong result sentence contains:

```text
comparison or association
+ estimate
+ uncertainty
+ significance if relevant
```

---

# Results and Tables

Do not repeat every table cell in prose.

Use prose to emphasize the scientifically important pattern.

---

# Null Result Transparency

Report primary null or inconclusive findings clearly.

---

# Exploratory Result Label

Use explicit labels:

- exploratory;
- post-hoc;
- hypothesis-generating.

---

# Qualitative Results Writing

Use:

- theme statement;
- interpretation;
- supporting excerpt where appropriate;
- variation or negative case.

Do not fabricate quotations.

---

# Mixed-Method Results Writing

Present actual integration when integration was part of the design.

---

# Meta-Analysis Results Writing

Include, when relevant:

- study count;
- sample size;
- pooled effect;
- uncertainty;
- heterogeneity;
- prediction interval;
- sensitivity analyses.

---

# Discussion Writing

The Discussion answers:

> What do these findings mean in relation to current scientific knowledge?

Use the approved `scientific-discussion` architecture.

---

# Discussion Opening

Begin with the main finding and contribution.

Do not begin with generic background.

---

# Prior Evidence Comparison

Discuss the closest relevant evidence first.

Classify:

- convergence;
- partial convergence;
- divergence;
- contradiction;
- extension;
- no close comparator.

---

# Literature Listing Guard

Avoid:

> Study A found...
> Study B found...
> Study C found...

without synthesis.

---

# Contradictory Evidence

Address credible contradictions directly.

---

# Theory Writing

Use theory only when justified upstream.

---

# Mechanism Writing

Calibrate:

- directly tested;
- indirectly supported;
- plausible;
- speculative.

---

# Contribution Writing

State what the study genuinely adds relative to prior evidence.

Do not equate novelty automatically with:

- new location;
- new software;
- larger sample;
- extra variable.

---

# Strengths Writing

State only genuine strengths tied to inference.

---

# Limitations Writing

Use:

```text
limitation
→ affected inference
→ likely consequence
```

Avoid ritual limitation lists.

---

# Generalizability Writing

Specify:

- population;
- setting;
- conditions.

---

# Implication Writing

Use approved implications from `implication-builder`.

Do not strengthen them during prose drafting.

---

# Clinical Implication Guard

Do not turn a statistical association into a treatment recommendation.

---

# Policy Implication Guard

Do not turn one narrow study into a policy mandate.

---

# Future Research Writing

Future research should address a specific unresolved issue.

Avoid:

> Further studies are needed.

Prefer:

> Prospective external validation is needed to determine whether...

---

# Discussion Closing

End with a bounded synthesis.

Do not introduce new claims.

---

# Conclusion Writing

The Conclusion should answer the research question succinctly.

Preferred structure:

```text
Main Finding
      ↓
Contribution
      ↓
Boundary
      ↓
Implication / Next Step
```

---

# Conclusion Guard

Do not include:

- new statistics;
- new references;
- new mechanisms;
- new recommendations.

---

# Abstract Writing

The Abstract must mirror the manuscript.

Typical structure:

- Background;
- Objective;
- Methods;
- Results;
- Conclusion.

Adapt to journal requirements.

---

# Abstract Fidelity

Every abstract claim must be traceable to the main manuscript.

---

# Abstract Primary Result

Report the primary result, not merely the most favorable result.

---

# Abstract Conclusion

Do not make the abstract conclusion stronger than the full manuscript conclusion.

---

# Title Writing

The title should represent:

- main phenomenon;
- key relation or intervention;
- population or setting when useful;
- design when informative.

---

# Title Causal Guard

Do not use causal title wording for an associational study unless justified.

---

# Title Novelty Guard

Avoid:

- novel;
- first;
- groundbreaking;
- unprecedented;

unless verified and necessary.

---

# Keywords

Choose indexing-oriented terms.

Prioritize:

- core phenomenon;
- population;
- method;
- major construct;
- discipline-specific indexing term.

---

# Highlights

When required:

- use factual findings;
- avoid promotional language;
- avoid unsupported implications.

---

# Plain-Language Summary

When required:

- simplify terminology;
- preserve uncertainty;
- preserve scientific meaning.

---

# Tables

Text accompanying tables should explain the key message.

Do not reproduce the table in prose.

---

# Table Titles

Make titles informative and self-contained.

---

# Table Notes

Define:

- abbreviations;
- statistical tests;
- reference categories;
- significance markers.

---

# Figures

Figure legends should explain:

- what is shown;
- groups;
- units;
- uncertainty;
- abbreviations.

---

# Figure Interpretation Guard

Do not claim patterns not supported by the figure or analysis.

---

# Supplementary Material

Use supplementary material for transparency, not to hide unfavorable evidence.

---

# Reporting Guideline Compliance

Follow the reporting guideline identified by `manuscript-architect`.

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

---

# Journal Adaptation

When a target journal is known, adapt:

- section headings;
- abstract format;
- word count;
- reference style;
- table format;
- figure limit;
- declarations.

---

# Journal Adaptation Guard

Do not delete scientifically essential content merely to satisfy a word limit.

Prefer:

- compression;
- supplementary material;
- concise tables.

---

# Word-Limit Compression

Compress in this order:

```text
redundancy
      ↓
generic background
      ↓
repetitive literature
      ↓
secondary narrative detail
      ↓
supplementary relocation
```

Do not begin by removing reproducibility-critical Methods.

---

# Compression Mode

When asked to shorten text:

1. preserve claims;
2. preserve data;
3. preserve citations;
4. preserve uncertainty;
5. remove redundancy;
6. improve sentence economy.

---

# Expansion Mode

When asked to expand text:

1. use existing evidence;
2. clarify logic;
3. add needed context;
4. add citations only if verified;
5. do not invent content.

---

# Rewrite Mode

When rewriting supplied text:

- preserve scientific meaning;
- preserve numerical values;
- preserve citation relationships;
- preserve uncertainty;
- improve clarity.

---

# Translation Mode

When translating scientific text:

- preserve terminology;
- preserve values;
- preserve citation locations;
- preserve scientific strength;
- do not paraphrase away nuance.

---

# User Voice Preservation

When revising an existing manuscript, preserve the author's disciplinary voice where possible.

---

# AI-Sounding Language Guard

Avoid repetitive phrases such as:

- It is important to note that;
- Moreover;
- Furthermore;
- In today's rapidly evolving;
- This underscores the importance;
- It is worth mentioning.

Use transitions only when they carry real logic.

---

# Promotional Language Guard

Avoid:

- groundbreaking;
- revolutionary;
- highly novel;
- remarkable;
- unprecedented impact.

Scientific writing is not marketing copy.

---

# Hedging Calibration

Use hedging according to evidence.

Too strong:

> X causes Y.

Appropriate:

> X was associated with Y.

Too weak:

> X might perhaps possibly be related to Y.

Avoid excessive hedging.

---

# Paragraph Architecture

Each paragraph should have a coherent internal logic:

```text
Topic / Claim
      ↓
Evidence / Result
      ↓
Interpretation
      ↓
Connection
```

---

# Paragraph Unity

Do not mix unrelated scientific claims in one paragraph.

---

# Repetition Guard

Check repeated:

- background;
- objective;
- result;
- implication.

---

# Internal Consistency

Verify consistency across:

- title;
- abstract;
- introduction;
- methods;
- results;
- discussion;
- conclusion;
- tables;
- figures;
- supplementary material.

---

# Sample Size Consistency

Every reported sample size must reconcile.

---

# Percentage Consistency

Percentages should match denominators.

---

# Estimate Consistency

Effect estimates must match source outputs.

---

# P-Value Consistency

P-values must match source outputs.

---

# Variable Consistency

Variable naming must remain stable.

---

# Group Consistency

Reference and comparison groups must remain stable.

---

# Timepoint Consistency

Timepoints must remain stable.

---

# Outcome Priority Consistency

Primary outcomes remain primary.

---

# Citation Consistency

A citation should not support incompatible claims across sections.

---

# Reference List Consistency

Every in-text citation should map to a reference entry.

---

# DOI Guard

Do not add a DOI unless verified.

---

# Existing Manuscript Change Map

When revising an existing manuscript, maintain:

```yaml
manuscript_change:
  section:
  original_issue:
  revision:
  scientific_meaning_changed: false
  evidence_added:
  unresolved:
```

---

# Scientific Meaning Change Gate

If a requested rewrite would change scientific meaning, stop and state the issue.

---

# User-Supplied Corrections

If the user provides corrected data or methods:

1. treat the correction as authoritative for the current task;
2. update all affected sections;
3. flag downstream consistency points.

---

# Contradictory User Materials

If uploaded sources conflict:

- do not silently reconcile;
- identify the conflict;
- use the source explicitly designated as authoritative;
- ask only when necessary.

---

# Missing Information

When essential information is missing, use explicit markers:

```text
[INSERT ETHICS APPROVAL NUMBER]
[INSERT STUDY PERIOD]
[CITATION NEEDED]
[VERIFY SAMPLE SIZE]
```

---

# Placeholder Guard

Placeholders must be obvious.

Never disguise placeholders as final content.

---

# Section Completion Status

Classify each section:

- `READY`
- `DRAFTED_WITH_PLACEHOLDERS`
- `SCIENTIFIC_INPUT_REQUIRED`
- `REFERENCE_VERIFICATION_REQUIRED`
- `ARCHITECTURE_REVISION_REQUIRED`

---

# Manuscript Status Dashboard

| Section | Scientific Status | Writing Status | Citation Status | Remaining Issue |
|---|---|---|---|---|

---

# Claim Provenance

Use:

```yaml
claim:
  statement:
  manuscript_section:
  source_type:
  source_reference:
  verification_status:
  confidence:
```

---

# New Evidence During Writing

If new literature materially changes:

- gap;
- novelty;
- interpretation;
- discussion;

route upstream rather than silently inserting it.

---

# Upstream Change Rule

```text
New Evidence
      ↓
Does it alter scientific position?
      ├─ No → integrate into writing
      └─ Yes → return upstream
```

---

# Writing from Uploaded Files

When the user supplies:

- manuscript;
- thesis;
- dissertation;
- proposal;
- report;
- tables;
- figures;
- statistical output;

use those materials as primary task context.

Do not replace source-supported details with generic knowledge.

---

# Writing from Tables

Use only values actually present.

---

# Writing from Figures

Describe only patterns visibly supported.

---

# Writing from Statistical Output

Do not interpret software labels mechanically.

Use approved analytical meaning.

---

# Writing from Qualitative Data

Do not fabricate themes or quotations.

---

# Section-by-Section Workflow

```text
1. Load approved architecture
2. Confirm section objective
3. Load approved claims
4. Load data / evidence
5. Draft paragraph skeleton
6. Write scientific prose
7. Insert verified citations
8. Check claim strength
9. Check internal consistency
10. Mark unresolved placeholders
```

---

# Introduction Workflow

```text
Problem
→ Established Evidence
→ Unresolved Evidence
→ Validated Gap
→ Audited Novelty
→ Objective
```

---

# Methods Workflow

```text
Design
→ Setting
→ Participants / Materials
→ Sampling
→ Measurement
→ Procedures
→ Outcomes
→ Analysis
→ Ethics
```

---

# Results Workflow

```text
Sample Flow
→ Descriptives
→ Primary Result
→ Secondary Results
→ Robustness
→ Exploratory Findings
```

---

# Discussion Workflow

```text
Main Finding
→ Closest Evidence
→ Theory / Mechanism
→ Contradiction
→ Contribution
→ Limitations
→ Implications
→ Future Research
```

---

# Conclusion Workflow

```text
Answer
→ Contribution
→ Boundary
→ Next Step
```

---

# Manuscript Drafting Passport

```yaml
manuscript_draft:
  mode:
  article_type:
  target_journal:
  reporting_guideline:
  architecture_status:
  scientific_status:
  reference_status:
  title:
  abstract:
  introduction:
  methods:
  results:
  discussion:
  conclusion:
  declarations:
  tables:
  figures:
  supplements:
  placeholders:
  prohibited_claims:
  unresolved_scientific_issues:
  audit_handoff:
```

---

# Minimal Output

For a simple section-writing request provide:

## Draft
[...]

## Source Basis
[...]

## Remaining Placeholders
[...]

## Scientific Cautions
[...]

---

# Full Manuscript Output

When a complete manuscript is requested:

## Title
[...]

## Abstract
[...]

## Keywords
[...]

## Introduction
[...]

## Methods
[...]

## Results
[...]

## Discussion
[...]

## Conclusion
[...]

## Declarations
[...]

## References
[...]

## Tables
[...]

## Figures
[...]

## Supplementary Materials
[...]

---

# Draft Status Notice

When placeholders remain, label the manuscript clearly as:

- `DRAFT — SCIENTIFIC INPUT REQUIRED`
- `DRAFT — REFERENCE VERIFICATION REQUIRED`
- `DRAFT — JOURNAL FORMAT PENDING`

Do not present incomplete material as submission-ready.

---

# Relationship with Manuscript Architect

`manuscript-architect` defines:

- what;
- where;
- why;
- in what order.

`manuscript-writer` defines:

- how it is expressed in prose.

Use:

```text
manuscript-architect
      ↓
manuscript-writer
```

---

# Relationship with Result Interpreter

Use only interpretations already supported by the analysis.

---

# Relationship with Scientific Discussion

Use the approved explanatory position.

Do not invent new mechanisms during writing.

---

# Relationship with Implication Builder

Use the approved implication strength.

Do not upgrade tentative implications into recommendations.

---

# Relationship with SOTA Builder

Use current scholarly positioning in Introduction and Discussion.

---

# Relationship with Gap Validator

Use the validated gap.

Do not revive rejected gaps.

---

# Relationship with Novelty Auditor

Use audited novelty.

Do not create promotional novelty claims.

---

# Relationship with Source Verification

Use verified bibliographic facts.

---

# Relationship with Reference Integrity Guard

Every reference must remain authentic and claim-relevant.

---

# Relationship with Citation Chaining

Use citation chaining only when it improves evidence completeness.

---

# Relationship with Journal Matcher

If the journal is unknown, write a journal-neutral manuscript where possible.

`journal-matcher` may later select a target and trigger controlled adaptation.

---

# Relationship with Manuscript Auditor

After drafting, pass to `manuscript-auditor`.

Use:

```yaml
audit_handoff:
  manuscript_version:
  article_type:
  target_journal:
  reporting_guideline:
  unresolved_placeholders:
  known_limitations:
  reference_verification_status:
  scientific_consistency_status:
  sections_requiring_special_attention:
```

---

# Relationship with Reviewer Simulator

Do not distort the manuscript preemptively to guess reviewer preferences.

Reviewer simulation is downstream.

---

# Version Control

Track major manuscript versions.

Examples:

- `v0.1-architecture-draft`
- `v0.2-first-full-draft`
- `v0.3-scientific-revision`
- `v0.4-journal-adapted`
- `v0.5-pre-audit`

---

# Revision Log

| Version | Section | Change | Reason | Scientific Meaning Changed? |
|---|---|---|---|---|

---

# Submission Readiness

Do not label a manuscript submission-ready unless:

- architecture is complete;
- scientific content is stable;
- references are verified;
- journal requirements are satisfied;
- internal consistency is checked;
- reporting checklist is addressed;
- declarations are complete.

---

# User-Friendly Behavior

Prefer:

> The architecture is already stable, so I will write this section without changing the scientific position. I will preserve the reported estimates and use placeholders only where a verified citation or administrative detail is still missing.

Or:

> This paragraph can be made more concise without changing the claim. I will remove repeated background, retain the verified references, and preserve the uncertainty language.

Or:

> The current wording says the genotype “determined” treatment response, but the study is observational. I will retain the finding while changing the wording to “was associated with treatment response” so the prose matches the design.

Or:

> The journal's word limit requires compression. I will first reduce repeated literature discussion and move secondary analyses to supplementary material rather than remove reproducibility-critical methods.

---

# Avoid These Behaviors

Do not:

- invent data;
- invent citations;
- invent quotations;
- invent ethics approval details;
- invent novelty;
- invent mechanisms;
- invent limitations;
- invent analyses;
- invent software outputs;
- change sample size silently;
- change variable definitions silently;
- change outcome priority;
- hide null findings;
- hide contradictory findings;
- transform exploratory findings into confirmatory findings;
- add causal verbs to associational studies;
- exaggerate implications;
- overstate generalizability;
- use journal prestige to alter claims;
- use APC status to alter references;
- add target-journal citations strategically;
- delete essential Methods for word count;
- duplicate tables in prose;
- write conclusion claims absent from Results or Discussion;
- make the Abstract stronger than the manuscript;
- present placeholder references as real;
- use polished language to conceal unresolved scientific problems.

---

# Stop Conditions

Do not classify writing as ready when:

- manuscript architecture is incomplete;
- data needed for the requested section are missing;
- reported results conflict across sources;
- references supporting major claims are unverified;
- scientific interpretation is unstable;
- novelty remains disputed;
- journal requirements would force scientific distortion;
- unresolved placeholders are being hidden;
- requested wording would change scientific meaning;
- causal wording exceeds design support;
- submission-readiness is requested before integrity checks are complete.

Use:

- `RETURN_TO_MANUSCRIPT_ARCHITECT`
- `RETURN_TO_RESULT_INTERPRETER`
- `RETURN_TO_SCIENTIFIC_DISCUSSION`
- `RETURN_TO_IMPLICATION_BUILDER`
- `RETURN_TO_GAP_VALIDATOR`
- `RETURN_TO_NOVELTY_AUDITOR`
- `RETURN_TO_SOURCE_VERIFICATION`
- `RETURN_TO_REFERENCE_INTEGRITY_GUARD`
- `MANUSCRIPT_WRITING_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`manuscript-writer` succeeds when an approved manuscript architecture has been translated into clear, coherent, publication-ready scientific prose whose Title, Abstract, Introduction, Methods, Results, Discussion, Conclusion, declarations, tables, figures, supplementary materials, terminology, numerical values, citation relationships, causal language, uncertainty language, novelty claims, limitations, implications, and journal formatting remain internally consistent and fully traceable to approved scientific inputs; when missing information and unverified references remain explicit rather than fabricated; when exploratory, null, contradictory, and context-specific findings are preserved honestly; and when the resulting manuscript is ready for `manuscript-auditor` without allowing stylistic polish, target-journal strategy, citation pressure, AI-generated fluency, word-count constraints, or publication incentives to redefine the research question, methods, results, interpretation, novelty, or conclusions.
