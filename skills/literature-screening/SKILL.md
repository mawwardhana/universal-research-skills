---
name: literature-screening
description: Screen discovered and verified scholarly records for relevance and eligibility using transparent, research-purpose-specific inclusion and exclusion criteria. Use after database searching and citation chaining to create a defensible literature corpus for research landscapes, State-of-the-Art analysis, research-gap validation, novelty assessment, systematic reviews, meta-analyses, methodology development, and manuscript evidence synthesis.
---

# Literature Screening

## Purpose

`literature-screening` determines which scholarly records should enter a research evidence corpus for a specific scientific purpose.

Its central question is:

> Of all the literature we discovered and verified, which studies are actually relevant and eligible for the question we are trying to answer?

Literature screening protects the framework from:

- topic drift;
- irrelevant evidence;
- duplicate records;
- inappropriate document types;
- wrong populations;
- wrong outcomes;
- wrong methods;
- weak relevance;
- hidden selection bias;
- selective inclusion of supportive studies.

Screening must be transparent and reproducible.

---

# Core Principle

Use:

> Discovery finds possibilities. Screening determines eligibility.

A source can be:

- real;
- peer reviewed;
- Scopus indexed;

and still be irrelevant to the research question.

Verification does not equal inclusion.

---

# Activation Conditions

Use this skill after literature has been obtained through:

- `scopus-literature-search`;
- `citation-chaining`;
- OpenAlex;
- Crossref;
- PubMed;
- Semantic Scholar;
- publisher platforms;
- uploaded bibliographies;
- previous research materials.

Use before:

- `evidence-synthesis`;
- `sota-builder`;
- `gap-discovery`;
- `gap-validator`;
- `novelty-builder`;
- systematic review;
- meta-analysis;
- manuscript evidence integration.

---

# Screening Modes

Possible screening modes include:

- `EXPLORATORY`
- `LANDSCAPE`
- `TREND`
- `EMERGING_TOPIC`
- `SOTA`
- `GAP_VALIDATION`
- `NOVELTY_VALIDATION`
- `CONTINUATION_RESEARCH`
- `THEORY`
- `METHODOLOGY`
- `MEASUREMENT`
- `SYSTEMATIC_REVIEW`
- `META_ANALYSIS`
- `MANUSCRIPT_SUPPORT`

Screening strictness should depend on the purpose.

---

# 1. Define the Screening Question

Before screening, identify what the literature corpus is intended to support.

Examples:

- map a research field;
- assess current evidence;
- evaluate a mechanism;
- validate a research gap;
- identify competing studies;
- justify methodology;
- prepare a systematic review.

Do not screen without knowing the scientific purpose.

---

# 2. Define Eligibility Criteria

Eligibility criteria may include:

- population;
- phenomenon;
- intervention;
- exposure;
- comparator;
- outcome;
- study design;
- publication type;
- time period;
- language;
- context;
- methodology;
- peer-review status;
- indexing requirements.

Only include criteria that are scientifically necessary.

---

# 3. Use Question-Appropriate Frameworks

When useful, structure eligibility using appropriate frameworks.

Examples:

## PICO

- Population
- Intervention
- Comparator
- Outcome

Useful for many clinical questions.

## PECO

- Population
- Exposure
- Comparator
- Outcome

Useful for observational or exposure research.

## PCC

- Population
- Concept
- Context

Useful for scoping reviews.

## SPIDER

- Sample
- Phenomenon of Interest
- Design
- Evaluation
- Research type

Useful for qualitative or mixed-method research.

Do not force PICO onto every discipline.

---

# 4. Inclusion Criteria

Define explicit inclusion criteria.

Examples:

- directly relevant population;
- relevant outcome;
- specified study design;
- peer-reviewed article;
- relevant research period;
- appropriate language;
- relevant methodological approach.

Criteria should be determined before final study selection whenever possible.

---

# 5. Exclusion Criteria

Possible exclusions include:

- irrelevant population;
- wrong outcome;
- wrong context;
- purely editorial material;
- conference abstract without sufficient data;
- duplicate publication;
- retracted article;
- insufficient methodological detail;
- outside predefined scope.

Do not create exclusion criteria merely to remove contradictory studies.

---

# 6. Relevance Categories

Use:

- `DIRECTLY_RELEVANT`
- `HIGHLY_RELEVANT`
- `SUPPORTING`
- `CONTEXTUAL`
- `MARGINALLY_RELEVANT`
- `IRRELEVANT`

The same article may have different relevance depending on the research purpose.

---

# 7. Screening Stages

When appropriate, use:

```text
Identification
      ↓
Deduplication
      ↓
Title Screening
      ↓
Abstract Screening
      ↓
Full-Text Screening
      ↓
Final Inclusion
```

Not every research purpose requires every stage.

For exploratory landscape work, title and abstract screening may be sufficient for some records.

For systematic reviews, meta-analyses, gap validation, novelty auditing, and other high-stakes evidence tasks, full-text eligibility should be used whenever the decision depends on information unavailable from the abstract.

---

# 8. Stage Applicability

Possible stage configurations:

- `TITLE_ONLY_EXPLORATORY`
- `TITLE_ABSTRACT`
- `TITLE_ABSTRACT_FULL_TEXT`
- `FULL_TEXT_TARGETED`
- `SYSTEMATIC_MULTI_STAGE`
- `PURPOSE_SPECIFIC`

Do not call a workflow systematic merely because it contains several screening stages.

---

# 9. Screening Unit

Clarify the unit being screened.

Possible units include:

- bibliographic record;
- full article;
- study report;
- conference record;
- protocol;
- dataset paper;
- guideline;
- review article;
- thesis or dissertation;
- preprint;
- study family.

Do not confuse publication records with independent studies.

---

# 10. Screening Record

Use:

```yaml
screening_record:
  record_id:
  title:
  authors:
  year:
  source:
  doi:
  discovery_source:
  verification_status:
  integrity_status:
  screening_mode:
  title_decision:
  abstract_decision:
  full_text_decision:
  final_decision:
  exclusion_reason:
  evidence_role:
  notes:
```

Unknown fields remain unknown.

---

# 11. Screening Decision Vocabulary

Use consistent decisions:

- `INCLUDE`
- `EXCLUDE`
- `UNCERTAIN`
- `RETRIEVE_FULL_TEXT`
- `DUPLICATE`
- `AWAITING_VERIFICATION`
- `AWAITING_FULL_TEXT`
- `NOT_APPLICABLE`

Avoid free-text decisions when structured labels are practical.

---

# 12. Final Eligibility Status

Possible final statuses:

- `INCLUDED`
- `EXCLUDED`
- `PENDING_FULL_TEXT`
- `PENDING_VERIFICATION`
- `PENDING_CLARIFICATION`
- `DUPLICATE_RECORD`
- `RETRACTED_EXCLUDE`
- `SAME_STUDY_FAMILY_LINKED`

---

# 13. Screening Before Verification Guard

A record discovered through search or citation chaining should not automatically be treated as eligible evidence.

Preferred flow:

```text
discovered record
      ↓
source-verification
      ↓
reference-integrity-guard
      ↓
literature-screening
```

When identity is unresolved, use:

`AWAITING_VERIFICATION`

rather than `INCLUDE`.

---

# 14. Reference Integrity Handoff

If screening reveals:

- DOI mismatch;
- title-author mismatch;
- duplicate publication;
- retraction;
- citation mashup;
- study-family ambiguity;

route to:

`reference-integrity-guard`

before final eligibility when the issue affects scientific interpretation.

---

# 15. Deduplication

Deduplicate using the strongest available identifiers.

Possible matching fields:

- DOI;
- PMID;
- title;
- first author;
- year;
- journal;
- volume;
- article number;
- other persistent identifiers.

Do not deduplicate by title similarity alone when identity remains uncertain.

---

# 16. Duplicate Status

Use:

- `EXACT_DUPLICATE`
- `PROBABLE_DUPLICATE`
- `NOT_DUPLICATE`
- `DUPLICATE_STATUS_UNCERTAIN`

---

# 17. Version Deduplication

Distinguish:

- preprint vs version of record;
- conference abstract vs full article;
- accepted manuscript vs final publication;
- early online vs issue-assigned publication;
- corrected article vs original version.

Prefer the scientifically appropriate version rather than counting each version separately.

---

# 18. Study-Family Detection

Several publications may arise from one study.

Possible relationships include:

- protocol;
- baseline analysis;
- primary outcome;
- secondary outcome;
- subgroup analysis;
- follow-up;
- methodological paper;
- economic analysis.

Do not treat study-family publications as independent evidence unless they truly are independent.

---

# 19. Study-Family Record

Use:

```yaml
study_family:
  study_id:
  publications:
    - record_id:
      role:
      population_overlap:
      outcome:
      timepoint:
  independence_status:
  notes:
```

---

# 20. Title Screening

At title stage, exclude only when irrelevance is reasonably clear.

Possible title-stage decisions:

- `INCLUDE_FOR_ABSTRACT`
- `EXCLUDE_TITLE`
- `UNCERTAIN_REVIEW_ABSTRACT`

When uncertain, retain.

---

# 21. Title Screening Conservatism

Title screening should favor sensitivity over premature exclusion.

Do not exclude a potentially relevant paper solely because:

- terminology differs;
- the outcome is not named in the title;
- the population is described indirectly;
- a historical term is used.

---

# 22. Abstract Screening

Use the abstract to assess:

- population;
- intervention/exposure;
- outcome;
- design;
- context;
- scientific relevance;
- likely eligibility.

If critical eligibility information is missing:

`RETRIEVE_FULL_TEXT`

---

# 23. Abstract Limitation Guard

Do not infer from an abstract what it does not report.

Examples:

- exact confounder adjustment;
- full sampling procedure;
- detailed eligibility;
- instrument validity;
- exact subgroup definitions;
- full statistical methods.

---

# 24. Full-Text Retrieval

Retrieve full text when:

- eligibility is uncertain;
- a high-value claim depends on the paper;
- gap or novelty validation depends on exact details;
- methods must be compared;
- population overlap must be determined;
- inclusion in a systematic review is being decided.

---

# 25. Full-Text Availability Status

Use:

- `FULL_TEXT_AVAILABLE`
- `FULL_TEXT_PARTIAL`
- `FULL_TEXT_NOT_FOUND`
- `FULL_TEXT_ACCESS_RESTRICTED`
- `FULL_TEXT_REQUEST_NEEDED`
- `ABSTRACT_ONLY`

Do not fabricate full-text assessment when full text was unavailable.

---

# 26. Full-Text Screening

At full text, evaluate all pre-specified eligibility criteria.

Record the primary reason for exclusion.

When multiple reasons apply, one primary reason may be recorded with secondary notes.

---

# 27. Full-Text Exclusion Reasons

Possible reasons include:

- `WRONG_POPULATION`
- `WRONG_INTERVENTION`
- `WRONG_EXPOSURE`
- `WRONG_COMPARATOR`
- `WRONG_OUTCOME`
- `WRONG_CONTEXT`
- `WRONG_DESIGN`
- `WRONG_PUBLICATION_TYPE`
- `OUTSIDE_DATE_RANGE`
- `LANGUAGE_EXCLUSION`
- `INSUFFICIENT_DATA`
- `NOT_PRIMARY_RESEARCH`
- `NOT_PEER_REVIEWED`
- `DUPLICATE`
- `SAME_STUDY_FAMILY_NONPRIMARY`
- `RETRACTED`
- `FULL_TEXT_UNAVAILABLE`
- `OUTSIDE_SCOPE`
- `OTHER_PREDEFINED_REASON`

---

# 28. Exclusion Reason Integrity

Do not invent an exclusion reason after seeing inconvenient results.

Eligibility should depend on the protocol or scientific purpose, not whether findings support the preferred hypothesis.

---

# 29. Contradictory Evidence Guard

A study must not be excluded merely because it:

- reports a null result;
- contradicts the expected direction;
- challenges the preferred theory;
- weakens novelty;
- addresses part of the presumed gap.

Contradictory evidence may be especially important for:

- SoTA;
- gap validation;
- novelty auditing;
- scientific discussion.

---

# 30. Positive-Result Bias Guard

Do not preferentially include statistically significant studies.

Preserve:

```text
eligibility
≠
statistical significance
```

---

# 31. Citation Count Guard

Do not use citation count as an eligibility criterion unless explicitly justified for a specialized purpose.

Highly cited does not equal eligible.

Low cited does not equal irrelevant.

---

# 32. Journal Prestige Guard

Do not include or exclude a study based solely on:

- journal quartile;
- impact factor;
- publisher prestige;
- institutional prestige.

Scientific relevance and purpose-specific eligibility come first.

---

# 33. APC Independence

APC status must never influence evidence inclusion.

Preserve:

```text
evidence screening
≠
publication affordability
```

---

# 34. Target-Journal Independence

Do not screen literature to favor the target journal.

Relevant articles from the target journal may be included.

Irrelevant articles must not be added for strategic citation reasons.

---

# 35. Scopus Indexing Guard

Scopus status may be a predefined criterion for some research purposes.

If used, distinguish:

```text
source indexed in Scopus
≠
specific document verified in Scopus
```

Never claim direct Scopus verification unless it occurred.

---

# 36. Peer-Review Status

Possible statuses:

- `PEER_REVIEWED`
- `PREPRINT`
- `CONFERENCE_ABSTRACT`
- `THESIS`
- `REPORT`
- `GUIDELINE`
- `EDITORIAL`
- `LETTER`
- `UNKNOWN`

Whether these are eligible depends on the research purpose.

---

# 37. Publication-Type Eligibility

For systematic review or meta-analysis, publication type should be pre-specified.

For SoTA or theory work, reviews, commentaries, or foundational essays may be scientifically useful even if they are not primary empirical studies.

Screen according to purpose.

---

# 38. Primary vs Secondary Research

Classify when useful:

- `PRIMARY_RESEARCH`
- `SYSTEMATIC_REVIEW`
- `META_ANALYSIS`
- `SCOPING_REVIEW`
- `NARRATIVE_REVIEW`
- `GUIDELINE`
- `PROTOCOL`
- `METHOD_PAPER`
- `OTHER_SECONDARY`

Do not collapse evidence roles.

---

# 39. Study Design Classification

Possible designs include:

- randomized trial;
- cohort;
- case-control;
- cross-sectional;
- diagnostic study;
- prognostic study;
- qualitative study;
- mixed-methods study;
- laboratory experiment;
- animal study;
- in-vitro study;
- formulation study;
- simulation study;
- modeling study;
- systematic review;
- meta-analysis.

Use design labels appropriate to the discipline.

---

# 40. Study-Design Eligibility

Do not reject a study merely because it uses a different method label if it addresses an equivalent scientific question.

This is especially important for:

- gap validation;
- novelty assessment;
- interdisciplinary research.

---

# 41. Method Equivalence Guard

Different analytical approaches may address the same underlying question.

Before exclusion, ask:

> Is the method scientifically equivalent enough to threaten the proposed gap or novelty?

Route difficult methodological equivalence questions to:

`methodology-architect`

or:

`statistical-method-selector`

---

# 42. Population Eligibility

Population criteria may include:

- age;
- sex;
- disease;
- occupation;
- educational level;
- species;
- geography;
- setting;
- risk group.

Avoid over-narrow population criteria unless scientifically justified.

---

# 43. Population Overlap

A paper may include a broader population containing the target subgroup.

Possible decisions:

- include;
- include if subgroup data are extractable;
- exclude;
- uncertain.

Document the rationale.

---

# 44. Geographic Eligibility

Geography may matter when the scientific question is context-sensitive.

Possible statuses:

- `GEOGRAPHY_MATCH`
- `GEOGRAPHY_PARTIAL`
- `GEOGRAPHY_OUTSIDE_SCOPE`
- `GEOGRAPHY_NOT_RELEVANT`

Do not use geography as a superficial novelty device.

---

# 45. Context Eligibility

Context may include:

- healthcare system;
- education system;
- workplace;
- community;
- laboratory;
- regulatory environment;
- cultural setting.

Context relevance should be explicit.

---

# 46. Outcome Eligibility

Define what outcomes are:

- primary;
- secondary;
- surrogate;
- exploratory;
- process outcomes.

Do not exclude a study because it reports an unexpected outcome if that outcome remains within the predefined scope.

---

# 47. Outcome Terminology Expansion

Equivalent outcomes may use different terminology.

Update screening dictionaries when terminology expansion is scientifically justified.

Do not change criteria simply to rescue or remove particular studies.

---

# 48. Exposure and Intervention Eligibility

Clarify whether the corpus concerns:

- intervention;
- exposure;
- treatment;
- dose;
- behavior;
- policy;
- technology;
- formulation;
- biomarker;
- genetic variant.

Do not merge distinct exposures without rationale.

---

# 49. Comparator Eligibility

Comparator requirements may include:

- placebo;
- usual care;
- untreated;
- alternate intervention;
- no comparator required.

Do not require a comparator for designs where one is not scientifically necessary.

---

# 50. Date Eligibility

Date limits should be justified.

Possible reasons:

- technology introduced after a date;
- policy period;
- contemporary evidence window;
- search update;
- historical analysis.

Avoid arbitrary recency cutoffs.

---

# 51. Seminal Evidence Exception

Older foundational sources may remain essential even if the primary contemporary search window is recent.

Handle seminal sources explicitly rather than silently violating date criteria.

---

# 52. Language Eligibility

Language restrictions should be declared.

Do not imply language-comprehensive coverage when only selected languages were screened.

---

# 53. Translation Guard

If machine translation or summary translation is used, label it.

Do not claim detailed full-text verification if translation quality prevents it.

---

# 54. Contextual Evidence

`CONTEXTUAL` literature may be retained separately from the core evidence set.

Examples:

- policy background;
- historical context;
- related population;
- adjacent mechanism;
- methodological context.

Do not mix contextual and directly eligible evidence without labels.

---

# 55. Evidence-Tier Separation

A screened corpus may contain layers:

```text
Core Evidence
      +
Supporting Evidence
      +
Contextual Evidence
```

Keep these roles explicit.

---

# 56. Core Evidence Criteria

Core evidence should directly address the research purpose.

Possible features:

- direct population match;
- direct construct match;
- direct method relevance;
- direct outcome relevance;
- high interpretive value.

---

# 57. Supporting Evidence Criteria

Supporting evidence may:

- explain mechanisms;
- support theory;
- validate methods;
- provide analogous findings;
- help interpret context.

It should not be represented as direct evidence when it is indirect.

---

# 58. Contextual Evidence Criteria

Contextual evidence may help explain:

- magnitude;
- history;
- setting;
- policy;
- adjacent disciplines.

Contextual evidence is not a substitute for direct evidence.

---

# 59. Purpose-Specific Screening Matrix

Use:

| Criterion | Required? | Allowed Variation | Exclusion Rule |
|---|---|---|---|

This helps prevent ad hoc decisions.

---

# 60. Eligibility Protocol

For high-stakes screening, record criteria before final selection.

Example:

```yaml
eligibility_protocol:
  purpose:
  population:
  concept_or_intervention:
  comparator:
  outcomes:
  designs:
  publication_types:
  dates:
  languages:
  indexing:
  exclusion_rules:
```

---

# 61. Protocol Change Log

If criteria must change:

```yaml
protocol_change:
  date:
  criterion:
  previous_rule:
  new_rule:
  reason:
  studies_affected:
```

Do not hide post-hoc changes.

---

# 62. Post-Hoc Eligibility Change Guard

Changing criteria after seeing study results can introduce selection bias.

When scientifically necessary:

- document the change;
- justify it;
- reassess all potentially affected records.

---

# 63. Screening Calibration

For multi-reviewer workflows, calibrate on a sample of records before full screening.

Purpose:

- clarify ambiguous criteria;
- harmonize interpretations;
- reduce inconsistent exclusions.

---

# 64. Dual Screening

For systematic reviews and high-stakes evidence syntheses, independent dual screening may be appropriate.

Record whether screening was:

- single reviewer;
- dual independent;
- dual with verification;
- consensus-based.

Do not claim independent screening if it did not occur.

---

# 65. Conflict Resolution

When reviewers disagree:

```text
Reviewer A decision
      +
Reviewer B decision
      ↓
Reason comparison
      ↓
Consensus / Third Reviewer
```

Do not resolve disagreement by automatically preferring exclusion.

---

# 66. Inter-Rater Metrics

Agreement metrics may be reported when appropriate.

Examples:

- percent agreement;
- Cohen's kappa.

Do not compute or report them unless data support it.

---

# 67. Screening Reviewer Record

Use:

```yaml
screening_review:
  record_id:
  reviewer_1:
  decision_1:
  reviewer_2:
  decision_2:
  conflict:
  resolution:
  final_decision:
```

---

# 68. Blind Screening

Blinding reviewer identity, journal, or authors may reduce some biases but is not mandatory for most workflows.

Do not claim blinding unless implemented.

---

# 69. Automation Assistance

Automation may help:

- deduplicate;
- prioritize likely relevance;
- identify keywords;
- triage records.

Automation must not silently replace scientific eligibility decisions.

---

# 70. AI-Assisted Screening Guard

If AI assists screening:

- preserve criteria;
- preserve human-verifiable rationale;
- do not invent full-text content;
- label uncertainty;
- audit exclusions.

AI confidence is not eligibility evidence.

---

# 71. Prioritization vs Exclusion

Machine-learning or relevance ranking may prioritize records.

It must not automatically exclude records unless the workflow explicitly validates that approach.

Preserve:

```text
priority score
≠
eligibility decision
```

---

# 72. Search-to-Screen Handoff

From:

`scopus-literature-search`

screening should receive:

- search scope;
- query;
- search date;
- records;
- source status;
- deduplication information when available.

---

# 73. Citation-Chaining Handoff

From:

`citation-chaining`

screening should receive:

- candidate source;
- anchor;
- discovery path;
- citation relationship;
- verification status.

Citation relevance is not automatically eligibility.

---

# 74. Uploaded Bibliography Intake

When the user provides a bibliography or spreadsheet:

- preserve original identifiers;
- detect duplicates;
- verify critical sources;
- screen against explicit criteria.

Do not assume uploaded references are already eligible.

---

# 75. Previous Research Materials

For continuation research, prior studies may enter screening as anchors or context.

Do not automatically include all references from a previous thesis or article.

---

# 76. Research Landscape Mode

For `LANDSCAPE` screening, eligibility may be broader.

Goal:

- map domain structure;
- identify themes;
- characterize methods;
- understand major streams.

Do not apply clinical-review narrowness unless needed.

---

# 77. Trend Mode

For `TREND` screening, ensure records truly represent the target concept over time.

Guard against terminology changes that create false trends.

Route trend synthesis to:

`trend-detection`

---

# 78. Emerging Topic Mode

For `EMERGING_TOPIC`, include sufficiently recent and directly relevant evidence while preserving earlier precursors.

Route interpretation to:

`emerging-topic-discovery`

---

# 79. SoTA Mode

For `SOTA`, screening should intentionally capture:

- established evidence;
- emerging evidence;
- contested evidence;
- unresolved questions;
- frontier studies.

Do not screen only for supportive evidence.

Route to:

`sota-builder`

---

# 80. Gap Validation Mode

For `GAP_VALIDATION`, screening should be adversarial.

Include literature that could:

- close the gap;
- partially address it;
- use alternative terminology;
- use equivalent methods;
- test the same concept in adjacent disciplines;
- contradict the presumed absence.

Route final judgment to:

`gap-validator`

---

# 81. Gap-Validation Inclusion Bias Guard

Do not exclude a study merely because it makes the proposed gap less attractive.

A gap-validation corpus should maximize the chance of defeating a weak gap.

---

# 82. Novelty Validation Mode

For `NOVELTY_VALIDATION`, prioritize:

- closest competitors;
- recent related studies;
- methodological equivalents;
- cross-disciplinary analogues;
- earlier priority claims.

Route final novelty assessment to:

`novelty-auditor`

---

# 83. Novelty Competitor Eligibility

A paper can threaten novelty even if it differs in one dimension.

Do not exclude it merely because geography, software, or terminology differs.

Assess substantive overlap.

---

# 84. Continuation Research Mode

For `CONTINUATION_RESEARCH`, include:

- original prior work;
- citing studies;
- replications;
- extensions;
- contradictions;
- recent competitors.

Route continuation synthesis to:

`continuation-opportunity-finder`

---

# 85. Theory Mode

For `THEORY`, include:

- original theory sources;
- major refinements;
- empirical tests;
- competing theories;
- critiques;
- boundary-condition studies.

Route to:

`theoretical-framework`

---

# 86. Methodology Mode

For `METHODOLOGY`, include:

- method origin;
- validation;
- comparisons;
- refinements;
- limitations;
- current applications.

Route method selection to:

`methodology-architect`

---

# 87. Measurement Mode

For `MEASUREMENT`, include when relevant:

- instrument development;
- translation;
- adaptation;
- reliability;
- validity;
- measurement invariance;
- responsiveness.

Route instrument design questions to:

`instrument-design`

---

# 88. Systematic Review Mode

For `SYSTEMATIC_REVIEW`, screening should follow the review protocol.

At minimum preserve:

- search results;
- deduplication;
- title/abstract decisions;
- full-text decisions;
- exclusion reasons;
- final included studies.

---

# 89. Meta-Analysis Mode

For `META_ANALYSIS`, eligibility must ensure studies provide:

- relevant outcome;
- compatible design;
- extractable effect data or estimable effect;
- sufficient methodological information.

Route quantitative synthesis to:

`meta-analysis`

---

# 90. Manuscript Support Mode

For `MANUSCRIPT_SUPPORT`, screen references according to the claim being supported.

Do not build an oversized literature corpus merely to increase citation volume.

---

# 91. Background Screening

Background evidence may support:

- magnitude;
- context;
- historical development.

For phenomenon evidence, consider:

`phenomenon-evidence-builder`

Do not force official statistics through scholarly eligibility rules.

---

# 92. Scholarly vs Phenomenon Screening

Preserve:

```text
Scholarly Literature Screening
      ≠
Phenomenon Evidence Verification
```

Official statistics, policies, and regulations follow authority-first verification rather than Scopus-first scholarly screening.

---

# 93. Phenomenon Evidence Boundary

A policy or official report may be useful for real-world context but should not be treated as a scholarly study unless it actually is one.

Route to:

`phenomenon-evidence-builder`

when appropriate.

---

# 94. Retraction Screening

Retracted literature should normally be excluded from evidentiary synthesis.

Possible exception:

- historical analysis of the retraction itself;
- integrity research;
- citation-contamination research.

Label clearly.

---

# 95. Correction and Erratum Screening

If a study has a correction:

- determine whether the corrected version remains eligible;
- use corrected data;
- preserve the correction relationship.

---

# 96. Expression of Concern

A study under expression of concern may require special handling.

Use:

- `INCLUDE_WITH_INTEGRITY_FLAG`
- `EXCLUDE_PENDING_RESOLUTION`
- `CONTEXT_ONLY`

depending on purpose.

Route integrity assessment to:

`reference-integrity-guard`

---

# 97. Predatory or Unverifiable Source Guard

If source legitimacy cannot be established:

`PENDING_VERIFICATION`

Do not automatically treat unusual publishers as invalid without evidence.

---

# 98. Grey Literature

Grey literature may be eligible for some purposes.

Examples:

- reports;
- theses;
- government documents;
- trial registries.

Predefine whether and why it is included.

---

# 99. Conference Abstracts

Conference abstracts may be useful for:

- emerging evidence;
- publication-bias assessment;
- locating later full papers.

They may be insufficient for detailed methodological synthesis.

---

# 100. Preprints

Preprints may be relevant for rapidly evolving fields.

Label them as preprints.

Do not represent them as peer-reviewed journal evidence.

---

# 101. Protocols

Protocols may clarify:

- planned methods;
- outcomes;
- preregistration;
- deviations.

Do not treat protocols as evidence of study results.

---

# 102. Guidelines

Guidelines can be eligible for:

- practice recommendations;
- policy context;
- evidence hierarchy;
- clinical standards.

Do not treat guideline recommendations as primary empirical evidence.

---

# 103. Narrative Reviews

Narrative reviews can be useful for:

- conceptual orientation;
- terminology;
- citation discovery.

Do not assume comprehensive search coverage.

---

# 104. Systematic Reviews

Systematic reviews may be eligible as:

- evidence summaries;
- search anchors;
- evidence-map sources.

Do not double-count review conclusions and their primary studies as independent evidence without careful handling.

---

# 105. Umbrella Reviews

Umbrella reviews may be useful for broad evidence synthesis.

Record overlap among included reviews when relevant.

---

# 106. Meta-Analyses

Meta-analyses should be screened for:

- population;
- included designs;
- outcome;
- search date;
- overlap;
- methodological relevance.

A pooled estimate may not apply to the exact target context.

---

# 107. Reviews as Search Anchors

When a relevant review is included for discovery purposes, forward-chain beyond its search date.

Route to:

`citation-chaining`

---

# 108. Screening Search Updates

When time has passed since the original search:

- update the database search;
- forward-chain recent anchors;
- rescreen new records.

Do not claim current coverage from an outdated search.

---

# 109. Search Date Integrity

Record the date literature was searched or retrieved.

Do not confuse article publication date with search date.

---

# 110. Screening Date

For reproducibility, record screening period when practical.

Example:

```yaml
screening_period:
  start:
  end:
```

---

# 111. Corpus Versioning

A screened corpus may change after search updates.

Use:

```yaml
corpus_version:
  version:
  search_cutoff:
  records_identified:
  records_included:
  update_reason:
```

Do not fabricate counts.

---

# 112. Screening Counts

For formal reviews, track:

- identified;
- duplicates removed;
- title/abstract screened;
- full texts assessed;
- excluded;
- included.

Counts should reconcile.

---

# 113. Count Reconciliation

Use:

```text
identified
- duplicates
= screened

screened
- title/abstract exclusions
= full-text candidates

full-text candidates
- full-text exclusions
= included
```

Adapt when workflow differs.

---

# 114. PRISMA-Compatible Tracking

For systematic reviews, counts and exclusion reasons should support PRISMA flow reporting.

Do not claim PRISMA compliance unless the full review workflow meets relevant requirements.

---

# 115. Screening Flow Record

Use:

```yaml
screening_flow:
  identified:
  duplicates_removed:
  screened_title_abstract:
  excluded_title_abstract:
  full_text_assessed:
  full_text_excluded:
  included:
  unresolved:
```

Unknown counts remain unknown.

---

# 116. Screening Log

Use:

```yaml
screening_log:
  record_id:
  stage:
  decision:
  reason:
  reviewer:
  date:
  notes:
```

---

# 117. Exclusion Log

For full-text exclusion, preserve:

```yaml
exclusion:
  record_id:
  stage:
  primary_reason:
  secondary_reason:
  reviewer:
  notes:
```

---

# 118. Decision Traceability

Every final inclusion or exclusion should be explainable from:

- criteria;
- record information;
- screening stage;
- decision rationale.

---

# 119. Uncertain Decisions

Use:

`UNCERTAIN`

rather than forcing a decision when information is insufficient.

Resolve by:

- full-text retrieval;
- source verification;
- author information;
- protocol lookup;
- team consensus.

---

# 120. Missing Abstract

A missing abstract is not automatically an exclusion reason.

Retrieve full text or other verified metadata when the record may be relevant.

---

# 121. Missing Full Text

If full text cannot be obtained:

- record the limitation;
- do not fabricate eligibility;
- decide according to protocol.

Possible status:

`FULL_TEXT_UNAVAILABLE`

---

# 122. Author Contact

For systematic reviews, contacting authors may be appropriate when key eligibility or data are unavailable.

Do not claim author contact unless it occurred.

---

# 123. Translation Need

If full text is in an unfamiliar language:

use:

`TRANSLATION_REQUIRED`

rather than excluding silently when language is otherwise eligible.

---

# 124. Ambiguous Study Design

If design is unclear:

`DESIGN_UNCERTAIN`

Retrieve methods information before exclusion when design is an eligibility criterion.

---

# 125. Ambiguous Population

If the target population is only a subset:

determine whether relevant subgroup data are available.

Do not infer subgroup results that are not reported.

---

# 126. Mixed Population Studies

Possible statuses:

- `INCLUDE_FULL_SAMPLE`
- `INCLUDE_SUBGROUP`
- `EXCLUDE_MIXED_POPULATION`
- `UNCERTAIN`

Use the predefined rule.

---

# 127. Mixed Intervention Studies

When several interventions are bundled:

determine whether the target intervention effect can be isolated.

---

# 128. Multiple Outcomes

A study may be eligible if at least one target outcome is reported.

Do not exclude it because other outcomes are irrelevant.

---

# 129. Secondary Outcomes

If secondary outcomes are eligible, label them.

Do not present them as preregistered primary outcomes unless verified.

---

# 130. Surrogate Outcomes

If surrogate outcomes are eligible:

label them separately from clinical outcomes.

---

# 131. Composite Outcomes

Determine whether the composite matches the eligibility definition.

Do not assume all components are reported separately.

---

# 132. Multiple Timepoints

Define whether:

- all timepoints;
- final timepoint;
- prespecified timepoint;
- closest compatible timepoint;

are eligible.

---

# 133. Longitudinal Follow-Up

Different follow-up reports from the same cohort may represent study-family publications.

Link them rather than double-count.

---

# 134. Sample Overlap

When databases or cohorts overlap:

assess whether records represent independent samples.

Route complex overlap issues to:

`reference-integrity-guard`

---

# 135. Dataset Reuse

Several papers may use the same public dataset.

This does not automatically make them duplicates if questions and analyses differ.

But they are not independent population replications.

---

# 136. Multicenter Publications

A multicenter study may have site-specific reports.

Assess overlap carefully.

---

# 137. Secondary Data Analyses

Secondary analyses may be eligible if they answer the target question.

Label the data source.

---

# 138. Mechanistic Evidence Screening

For mechanistic questions, include studies capable of informing mechanism.

Do not treat association-only studies as equivalent to mechanistic experiments.

---

# 139. Causal Evidence Screening

For causal questions, ensure eligible designs match the intended causal inference.

Do not screen solely on topic keywords.

---

# 140. Prediction Evidence Screening

For prediction questions, prioritize studies reporting predictive performance and validation.

Prediction evidence is not causal evidence.

---

# 141. Diagnostic Evidence Screening

For diagnostic research, consider:

- index test;
- reference standard;
- target condition;
- population;
- accuracy measures.

---

# 142. Prognostic Evidence Screening

For prognosis, consider:

- population;
- prognostic factor/model;
- outcome;
- time horizon;
- validation status.

---

# 143. Pharmacogenetic Screening

Potential criteria may include:

- target gene/SNP;
- population;
- treatment;
- outcome;
- genotype model;
- genotyping method;
- clinical covariates.

Do not exclude alternative genetic models if they are relevant to the scientific question.

---

# 144. Pharmacokinetic Screening

Potential criteria may include:

- population;
- drug;
- route;
- dose;
- sampling;
- PK parameters;
- model type;
- assay.

---

# 145. Pharmaceutical Formulation Screening

Potential criteria may include:

- active ingredient;
- polymer/excipient;
- formulation type;
- preparation method;
- physicochemical outcomes;
- biological testing;
- comparator/control.

---

# 146. Experimental Study Screening

For laboratory evidence, distinguish:

- in vitro;
- ex vivo;
- animal;
- human;
- simulation.

Do not generalize across levels without explicit rationale.

---

# 147. Education Research Screening

Possible criteria include:

- learner group;
- intervention;
- educational setting;
- learning outcome;
- study design.

---

# 148. Social-Science Screening

Possible criteria include:

- population;
- construct;
- context;
- theoretical perspective;
- qualitative/quantitative design.

Do not force biomedical frameworks when inappropriate.

---

# 149. Engineering Screening

Possible criteria include:

- system;
- material;
- process;
- performance metric;
- experimental or simulation method.

---

# 150. Qualitative Evidence Screening

For qualitative research, assess:

- phenomenon;
- sample;
- setting;
- design;
- analytic approach.

Do not require statistical outcomes.

---

# 151. Mixed-Methods Evidence Screening

Mixed-methods studies may be eligible based on:

- quantitative component;
- qualitative component;
- integration;
- whole-study contribution.

Specify which component matters.

---

# 152. Evidence-Synthesis Eligibility

A study included in the broader screened corpus may not be eligible for every synthesis.

Use subset eligibility for:

- meta-analysis;
- mechanism synthesis;
- qualitative synthesis;
- subgroup analysis.

---

# 153. Nested Corpora

Conceptually:

```text
Broad Relevant Corpus
      ↓
SoTA Corpus
      ↓
Gap-Validation Corpus
      ↓
Novelty-Competitor Corpus
```

These corpora may overlap but need not be identical.

---

# 154. Corpus Purpose Labels

Use:

- `LANDSCAPE_CORPUS`
- `SOTA_CORPUS`
- `GAP_CORPUS`
- `NOVELTY_CORPUS`
- `METHOD_CORPUS`
- `SYSTEMATIC_REVIEW_CORPUS`
- `META_ANALYSIS_CORPUS`
- `MANUSCRIPT_CORPUS`

---

# 155. Multi-Purpose Screening

One record may be:

- included for SoTA;
- excluded from meta-analysis;
- included as a novelty competitor;
- contextual for discussion.

Record purpose-specific status.

---

# 156. Purpose-Specific Decision Record

Use:

```yaml
purpose_decision:
  record_id:
  purpose:
  decision:
  reason:
```

---

# 157. Avoid Universal Eligibility

There is no single permanent inclusion status for every research purpose.

Eligibility is question-dependent.

---

# 158. Evidence Role Assignment

After inclusion, assign when useful:

- `DIRECT_EVIDENCE`
- `SUPPORTING_EVIDENCE`
- `CONTEXTUAL_EVIDENCE`
- `CONTRADICTORY_EVIDENCE`
- `METHOD_EVIDENCE`
- `THEORY_EVIDENCE`
- `NOVELTY_COMPETITOR`
- `GAP_THREAT`
- `REPLICATION`
- `VALIDATION`

---

# 159. Screening Does Not Grade Quality

Screening asks:

> Is the study eligible?

Quality or risk-of-bias assessment asks:

> How trustworthy is the study?

Do not conflate them.

---

# 160. Quality Assessment Handoff

Formal appraisal may be performed by the appropriate downstream methodology or synthesis workflow.

Do not invent quality scores inside screening.

---

# 161. Risk-of-Bias Boundary

Risk of bias may affect whether evidence is emphasized or synthesized, but it should not be converted into hidden eligibility criteria unless pre-specified.

---

# 162. Evidence Strength Boundary

Evidence strength is not determined merely by inclusion.

Route synthesis and strength interpretation to:

`evidence-synthesis`

---

# 163. Evidence Synthesis Handoff

Preferred flow:

```text
literature-screening
      ↓
included corpus
      ↓
evidence-synthesis
```

Pass:

- eligibility rationale;
- study roles;
- verification status;
- study-family links;
- unresolved limitations.

---

# 164. State-of-the-Art Handoff

For SoTA:

```text
literature-screening
      ↓
evidence-synthesis
      ↓
sota-builder
```

Do not declare established/emerging/contested/frontier categories during screening alone.

---

# 165. Gap Discovery Handoff

Screening may reveal areas with sparse literature.

Route candidate-gap generation to:

`gap-discovery`

Do not call sparsity a validated gap.

---

# 166. Gap Validation Handoff

For gap validation, send:

- direct competitors;
- gap threats;
- recent studies;
- methodological equivalents;
- adjacent terminology;
- contradictions.

Route to:

`gap-validator`

---

# 167. Novelty Builder Handoff

After a validated or reframed gap:

route to:

`novelty-builder`

with the screened competitor corpus.

---

# 168. Novelty Auditor Handoff

All serious priority or novelty claims should be stress-tested by:

`novelty-auditor`

Screening should retain studies that threaten novelty.

---

# 169. Research Landscape Handoff

Broad screened corpora may route to:

`research-landscape`

for mapping major themes and structures.

---

# 170. Trend Detection Handoff

Time-labeled screened corpora may route to:

`trend-detection`

Do not infer trends from uncleaned or duplicated records.

---

# 171. Emerging Topic Handoff

Recent screened evidence may route to:

`emerging-topic-discovery`

---

# 172. Theoretical Framework Handoff

Theory-focused screened evidence may route to:

`theoretical-framework`

---

# 173. Conceptual Framework Handoff

When screened studies clarify construct relationships, route to:

`conceptual-framework`

---

# 174. Methodology Handoff

Method-focused evidence may route to:

`methodology-architect`

---

# 175. Instrument Handoff

Measurement evidence may route to:

`instrument-design`

---

# 176. Analysis Planning Handoff

Analytical-method evidence may route to:

`analysis-planner`

or:

`statistical-method-selector`

---

# 177. Meta-Analysis Handoff

When a meta-analysis-eligible subset exists:

route to:

`meta-analysis`

Do not pool merely because studies are broadly related.

---

# 178. Scientific Discussion Handoff

A balanced screened corpus supports:

`scientific-discussion`

especially for:

- supporting studies;
- contradictory studies;
- mechanistic comparisons;
- context differences.

---

# 179. Manuscript Handoff

For manuscript evidence integration, downstream writing should receive only:

- verified;
- integrity-cleared;
- scientifically relevant;
- purpose-appropriate references.

Route prose construction to:

`manuscript-writer`

---

# 180. Manuscript Audit Handoff

`manuscript-auditor` may use screening provenance to evaluate whether literature selection is defensible.

---

# 181. Reviewer Simulator Handoff

`reviewer-simulator` may challenge:

- unexplained exclusions;
- missing contradictory evidence;
- outdated corpus;
- selection bias;
- inappropriate inclusion criteria.

---

# 182. Reviewer Response Handoff

If reviewers question literature selection:

route to:

`reviewer-response`

with:

- criteria;
- screening decisions;
- exclusion reasons;
- updated search evidence.

---

# 183. Search Update After Review

If a reviewer requests newer literature:

- update discovery;
- verify new records;
- rescreen;
- update synthesis.

Do not add references directly without screening when eligibility matters.

---

# 184. Screening Matrix

Recommended:

| Record | Population | Concept/Exposure | Outcome | Design | Final Decision | Reason |
|---|---|---|---|---|---|---|

---

# 185. Full-Text Exclusion Table

Recommended:

| Record | Exclusion Reason | Criterion | Notes |
|---|---|---|---|

---

# 186. Purpose-Specific Corpus Table

Recommended:

| Record | SoTA | Gap | Novelty | Method | Meta-analysis |
|---|---|---|---|---|---|

---

# 187. Study-Family Table

Recommended:

| Study Family | Publication | Role | Independent Evidence? |
|---|---|---|---|

---

# 188. Verification Table

Recommended:

| Record | Source Verified | Integrity Cleared | Full Text | Screening Status |
|---|---|---|---|---|

---

# 189. Conflict Table

For multi-reviewer screening:

| Record | Reviewer 1 | Reviewer 2 | Resolution |
|---|---|---|---|

---

# 190. Screening Passport

Use:

```yaml
literature_screening:
  purpose:
  screening_mode:
  framework:
  criteria_defined:
  protocol_version:
  search_cutoff:
  records_identified:
  duplicates_removed:
  title_abstract_screened:
  full_text_assessed:
  included:
  excluded:
  unresolved:
  reviewers:
  dual_screening:
  study_family_review:
  retraction_check:
  verification_complete:
  saturation_or_completion_status:
  next_stage:
```

Do not fabricate counts.

---

# 191. Screening Status

Possible workflow statuses:

- `NOT_STARTED`
- `CRITERIA_REQUIRED`
- `DEDUPLICATION_REQUIRED`
- `TITLE_ABSTRACT_SCREENING`
- `FULL_TEXT_RETRIEVAL`
- `FULL_TEXT_SCREENING`
- `CONFLICT_RESOLUTION`
- `VERIFICATION_REQUIRED`
- `SCREENING_COMPLETE`
- `READY_FOR_SYNTHESIS`

---

# 192. High-Stakes Screening Gate

Before declaring `READY_FOR_SYNTHESIS`, verify:

- criteria are explicit;
- duplicates are resolved;
- critical records are verified;
- full-text decisions are complete where required;
- exclusion reasons are traceable;
- study-family relationships do not distort counts;
- retracted sources are handled;
- unresolved records are documented.

---

# 193. Systematic Review Readiness

For systematic reviews, also verify:

- protocol consistency;
- search-update status;
- dual-reviewer requirements when planned;
- PRISMA-compatible counts;
- full-text exclusion log.

---

# 194. Gap Validation Readiness

For gap validation, verify:

- latest close competitors screened;
- citation-chain discoveries screened;
- terminology variants considered;
- adjacent methods considered;
- studies threatening the gap retained.

Use:

`READY_FOR_GAP_VALIDATION`

only when defensible.

---

# 195. Novelty Audit Readiness

Verify:

- closest competitors retained;
- recent priority threats screened;
- cross-disciplinary analogues considered;
- no competitor excluded for convenience.

Use:

`READY_FOR_NOVELTY_AUDIT`

---

# 196. SoTA Readiness

Verify the corpus contains enough evidence to distinguish:

- established;
- emerging;
- contested;
- unresolved;
- frontier.

Use:

`READY_FOR_SOTA`

---

# 197. Evidence-Synthesis Readiness

Use:

`READY_FOR_SYNTHESIS`

when eligibility is sufficiently resolved for the intended synthesis.

Do not imply all evidence-quality questions are solved.

---

# 198. Screening Completeness Wording

Prefer:

> Screening was completed according to the defined criteria for this corpus.

Avoid:

> All relevant literature was found.

No screening workflow can guarantee absolute completeness unless the claim is carefully bounded.

---

# 199. Screening Limitations

Possible limitations include:

- language restriction;
- database restriction;
- unavailable full text;
- single-reviewer screening;
- date restriction;
- grey-literature exclusion;
- indexing restriction.

Report material limitations transparently.

---

# 200. Sensitivity Screening

When an eligibility criterion is debatable, consider a sensitivity corpus.

Example:

```text
Primary Corpus
      +
Broader Sensitivity Corpus
```

This can show whether conclusions depend on a narrow screening choice.

---

# 201. Borderline Record Set

Retain borderline records separately when useful.

Possible status:

`BORDERLINE_INCLUDED_FOR_SENSITIVITY`

Do not hide borderline decisions.

---

# 202. Screening Audit Trail

A defensible audit trail should allow another researcher to understand:

- what was considered;
- why records were excluded;
- why records were included;
- what changed;
- what remained uncertain.

---

# 203. Reproducibility Guard

For formal reviews, screening decisions should be reproducible enough that another qualified reviewer could apply the same criteria.

Perfect agreement is not required.

Transparent criteria are required.

---

# 204. Selective Citation Guard

Screening should not be reverse-engineered from the references already preferred for the manuscript.

Start from criteria and evidence discovery.

---

# 205. Citation Padding Guard

Do not include sources merely to:

- increase citation count;
- cite influential authors;
- cite reviewers;
- cite the target journal;
- appear comprehensive.

---

# 206. Prestige Bias Guard

Do not preferentially retain famous studies when equally relevant less-famous evidence exists.

---

# 207. Geographic Bias Guard

Do not exclude non-target-country evidence automatically when it can still inform:

- mechanism;
- method;
- theory;
- external comparison;
- gap validation.

---

# 208. Confirmation Bias Guard

Actively inspect excluded records that challenge preferred conclusions if there is any concern the exclusion criteria may have been applied asymmetrically.

---

# 209. Adversarial Screening Check

Before finalizing a gap or novelty corpus, ask:

> Which excluded paper would most threaten our preferred conclusion if it were eligible?

Recheck that exclusion.

---

# 210. Screening Integrity Review

Audit a sample of exclusions for:

- criterion consistency;
- outcome blindness;
- design consistency;
- contradictory-evidence handling.

---

# 211. Criteria Drift Detection

Criteria drift occurs when the applied rule changes gradually during screening.

Potential signals:

- similar studies receive different decisions;
- later records are screened more narrowly;
- preferred findings are retained more often.

Correct by recalibration and re-review.

---

# 212. Decision Consistency Check

Compare similar records.

If two near-identical studies receive different decisions:

- explain the difference;
- correct inconsistency;
- update the log.

---

# 213. Evidence Role Consistency

Do not label one indirect study `DIRECT_EVIDENCE` while similar studies are `CONTEXTUAL` without rationale.

---

# 214. Screening Outcome Integrity

Final inclusion should reflect:

```text
scientific purpose
      +
predefined criteria
      +
verified record information
```

not preferred results.

---

# 215. Dynamic Screening

New evidence may require corpus updates.

When new literature is added:

- verify;
- deduplicate;
- screen using the same criteria;
- update counts and synthesis.

---

# 216. Living Review Boundary

Repeated updates do not make the workflow a living systematic review unless formal living-review procedures are used.

---

# 217. Legacy Corpus Migration

When an old literature corpus is reused:

- verify metadata;
- update searches;
- rescreen using current criteria;
- identify retractions and corrections.

Do not assume an old corpus remains current.

---

# 218. Imported Review Corpus

If records come from another review:

- verify the source;
- inspect its eligibility criteria;
- do not automatically inherit inclusion decisions.

---

# 219. Screening from Citation Manager

Citation-manager folders may reflect prior manual selection.

Treat folder membership as provenance, not eligibility.

---

# 220. Spreadsheet Screening

When screening in a spreadsheet, recommended columns include:

- ID;
- title;
- DOI;
- duplicate status;
- title decision;
- abstract decision;
- full-text decision;
- exclusion reason;
- reviewer;
- notes.

---

# 221. Database Export Integrity

Exports may contain duplicate or incomplete records.

Verify critical metadata before final inclusion.

---

# 222. Screening Error Types

Common errors include:

- false exclusion;
- false inclusion;
- duplicate inclusion;
- study-family double-counting;
- wrong publication version;
- retraction contamination;
- inconsistent criteria.

---

# 223. False Exclusion Risk

High false-exclusion risk occurs when title screening is too aggressive.

Mitigation:

- retain uncertain records;
- use terminology expansion;
- calibrate reviewers.

---

# 224. False Inclusion Risk

High false-inclusion risk occurs when broad relevance is mistaken for direct eligibility.

Mitigation:

- full-text screening;
- purpose-specific criteria;
- evidence-role labeling.

---

# 225. Screening Burden

Large corpora may require prioritization.

Prioritization can improve workflow efficiency.

It must not compromise scientific eligibility.

---

# 226. Screening Efficiency

Use:

- deduplication;
- keyword highlighting;
- calibrated exclusion reasons;
- batch decision review;
- relevance prioritization.

Do not sacrifice traceability for speed.

---

# 227. Minimum Documentation for Exploratory Screening

Even exploratory screening should preserve:

- purpose;
- basic inclusion logic;
- major exclusion logic;
- final retained set.

---

# 228. Minimum Documentation for Gap Validation

Preserve:

- candidate gap;
- adversarial criteria;
- close competitors;
- recent literature;
- exclusions threatening the gap;
- final gap corpus.

---

# 229. Minimum Documentation for Novelty Audit

Preserve:

- novelty claim;
- competitor criteria;
- closest included competitors;
- borderline competitors;
- exclusion rationale.

---

# 230. Minimum Documentation for Systematic Review

Preserve the full screening audit trail appropriate to the review protocol.

---

# 231. Screening Output — Criteria

Provide:

```text
Scientific purpose:
Screening mode:
Inclusion criteria:
Exclusion criteria:
Special rules:
```

---

# 232. Screening Output — Record Decisions

Provide a table such as:

| ID | Title | Stage | Decision | Reason |
|---|---|---|---|---|

---

# 233. Screening Output — Included Corpus

Provide:

| ID | Study | Design | Population | Evidence Role |
|---|---|---|---|---|

---

# 234. Screening Output — Excluded Full Text

Provide:

| ID | Study | Primary Exclusion Reason |
|---|---|---|

---

# 235. Screening Output — Uncertain Records

Provide:

| ID | Study | Missing Information | Required Action |
|---|---|---|---|

---

# 236. Screening Output — Study Families

Provide:

| Study Family | Publications | Primary Report | Overlap |
|---|---|---|---|

---

# 237. Screening Output — Corpus Summary

Summarize:

- corpus purpose;
- screening scope;
- included evidence roles;
- limitations;
- unresolved records;
- next stage.

---

# 238. Full Output

For a comprehensive screening task provide:

## A. Screening Purpose
[...]

## B. Eligibility Framework
[...]

## C. Inclusion Criteria
[...]

## D. Exclusion Criteria
[...]

## E. Deduplication
[...]

## F. Title / Abstract Screening
[...]

## G. Full-Text Screening
[...]

## H. Full-Text Exclusion Reasons
[...]

## I. Study-Family Review
[...]

## J. Included Evidence Corpus
[...]

## K. Contradictory / Gap-Threat Evidence
[...]

## L. Uncertain Records
[...]

## M. Screening Limitations
[...]

## N. Readiness Status
[...]

## O. Recommended Next Skill
[...]

---

# 239. Compact Output

For a small task provide:

```text
Purpose:
Criteria:
Record:
Decision:
Reason:
Evidence role:
Next step:
```

---

# 240. User-Friendly Behavior

Prefer:

> This article is real and relevant to the topic, but it does not meet the population criterion for the core corpus. I would keep it as contextual evidence rather than exclude it from all downstream use.

Or:

> This 2025 paper directly tests the mechanism that the proposed gap says has not been studied. It should remain in the gap-validation corpus even though it weakens the original gap claim.

Or:

> These two publications appear to come from the same cohort. I would link them as one study family rather than count them as two independent studies.

Or:

> The abstract is insufficient to decide eligibility. The defensible status is `RETRIEVE_FULL_TEXT`, not exclusion.

---

# 241. Avoid These Behaviors

Do not:

- exclude studies because their results are inconvenient;
- include studies only because they support the preferred hypothesis;
- treat verification as inclusion;
- treat indexing as inclusion;
- use quartile as evidence eligibility;
- use APC status as evidence eligibility;
- add target-journal papers for citation strategy;
- count duplicates as separate studies;
- count multiple reports from one cohort as independent evidence;
- fabricate full-text assessment;
- invent exclusion reasons;
- change criteria silently after seeing results;
- claim dual screening when it did not occur;
- claim PRISMA compliance without the required workflow;
- treat preprints as peer-reviewed articles;
- treat protocols as results;
- treat citation count as study quality;
- remove contradictory evidence;
- validate gaps during screening;
- certify novelty during screening;
- claim exhaustive literature completeness from a limited corpus.

---

# Stop Conditions

Do not mark screening complete when:

- eligibility criteria are undefined;
- duplicate status materially affects the corpus;
- critical source identities remain unresolved;
- required full texts remain pending;
- major reviewer conflicts remain unresolved;
- exclusion reasons are not traceable;
- study-family overlap materially distorts evidence counts;
- retraction status is unresolved for critical studies;
- a gap-validation corpus excludes close competitors without defensible reasons;
- a novelty corpus excludes studies that could materially threaten priority;
- a systematic-review corpus has unreconciled screening counts;
- criteria changed materially without re-reviewing affected records.

Use:

- `CRITERIA_REQUIRED`
- `SOURCE_VERIFICATION_REQUIRED`
- `REFERENCE_INTEGRITY_REQUIRED`
- `DEDUPLICATION_REQUIRED`
- `FULL_TEXT_REQUIRED`
- `CONFLICT_RESOLUTION_REQUIRED`
- `STUDY_FAMILY_REVIEW_REQUIRED`
- `SCREENING_INCOMPLETE`
- `GAP_CORPUS_REVIEW_REQUIRED`
- `NOVELTY_CORPUS_REVIEW_REQUIRED`
- `NOT_READY_FOR_SYNTHESIS`

as appropriate.

---

# Success Criterion

`literature-screening` succeeds when a discovered and sufficiently verified scholarly record set is transformed into a transparent, purpose-specific, scientifically defensible evidence corpus through explicit eligibility criteria, consistent deduplication, conservative title and abstract screening, full-text assessment when required, traceable exclusion reasons, study-family and publication-version handling, retraction awareness, and clear evidence-role assignment; when eligibility is determined by the research question rather than statistical significance, journal prestige, citation count, target-journal strategy, APC status, or preference for supportive findings; when contradictory evidence, close competitors, methodological equivalents, and studies that could weaken a proposed gap or novelty claim are deliberately retained when eligible; when uncertain records remain explicitly uncertain rather than being forced into inclusion or exclusion; when systematic-review workflows preserve auditable counts, conflict resolution, and PRISMA-compatible decision provenance; when exploratory, SoTA, gap-validation, novelty-validation, continuation, theory, methodology, measurement, meta-analysis, and manuscript-support corpora are screened according to their distinct purposes rather than one universal rule; when newly discovered or problematic records are routed through `source-verification` and `reference-integrity-guard`; when included evidence is handed to `evidence-synthesis`, `sota-builder`, `gap-validator`, `novelty-auditor`, `meta-analysis`, or other appropriate downstream skills without prematurely declaring synthesis conclusions; and when the final corpus is sufficiently traceable, balanced, reproducible, and current to support the next scientific workflow.
