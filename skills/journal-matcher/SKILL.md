---
name: journal-matcher
description: Identify, verify, compare, rank, and justify scientifically appropriate target journals for a scientifically stable manuscript using scope fit, article-type compatibility, audience relevance, evidence and method alignment, indexing status, publication model, editorial requirements, practical constraints, and current journal metadata without allowing prestige, quartile, APC status, acceptance pressure, target-journal citation strategy, or superficial keyword similarity to override scientific fit. Use when a manuscript has passed or substantially completed scientific audit and the researcher needs a defensible shortlist of journals, needs to compare candidate journals, needs to verify Scopus or other indexing claims, prefers journals without mandatory APC, wants to avoid predatory or discontinued journals, or needs a publication strategy that preserves the scientific record.
---

# Journal Matcher

## Purpose

`journal-matcher` identifies and prioritizes journals that are scientifically appropriate for a manuscript that is already sufficiently stable.

Its central question is:

> Which journals are genuinely compatible with this manuscript's scientific contribution, methods, evidence strength, article type, audience, reporting needs, and publication constraints — and why?

The goal is not to find the most prestigious journal.

The goal is to find the most defensible publication fit.

---

# Core Principle

Use:

> Scientific fit first. Publication strategy second.

Preferred logic:

```text
Scientifically Stable Manuscript
      ↓
Scientific Identity Extraction
      ↓
Journal Discovery
      ↓
Current Status Verification
      ↓
Scope & Article-Type Matching
      ↓
Audience & Method Compatibility
      ↓
Indexing & Publication Model Verification
      ↓
Risk Screening
      ↓
Constraint-Aware Ranking
      ↓
Target Journal Shortlist
      ↓
Submission Strategy
```

Do not reverse this order.

---

# Position in the Framework

Preferred architecture:

```text
manuscript-writer
      ↓
manuscript-auditor
      ↓
journal-matcher
      ↓
reviewer-simulator
      ↓
reviewer-response
```

`journal-matcher` should normally operate after scientific integrity has been sufficiently secured.

It must not be used to choose a journal that will tolerate unresolved scientific weaknesses.

---

# Publication Strategy Boundary

Journal matching may adapt:

- article packaging;
- title wording;
- abstract format;
- section organization;
- word count;
- table/figure allocation;
- supplementary strategy;
- cover-letter emphasis;
- submission metadata.

Journal matching must not alter:

- research question;
- study design;
- methods actually performed;
- primary outcome;
- numerical results;
- statistical interpretation;
- validated gap;
- audited novelty;
- causal status;
- scientific conclusion.

---

# Required Upstream Context

Use available information from:

- `manuscript-auditor`;
- `manuscript-architect`;
- `manuscript-writer`;
- `research-question-builder`;
- `methodology-architect`;
- `analysis-planner`;
- `result-interpreter`;
- `scientific-discussion`;
- `implication-builder`;
- `sota-builder`;
- `gap-validator`;
- `novelty-auditor`;
- `source-verification`;
- `reference-integrity-guard`;
- `research-intake`.

Do not ask the researcher to repeat information already present in the manuscript or audit record.

---

# Entry Modes

Classify the task as one or more of:

- `JOURNAL_DISCOVERY`
- `JOURNAL_SHORTLIST`
- `JOURNAL_COMPARISON`
- `JOURNAL_VERIFICATION`
- `SCOPUS_VERIFICATION`
- `INDEXING_VERIFICATION`
- `APC_SCREENING`
- `NO_MANDATORY_APC_SEARCH`
- `OPEN_ACCESS_MODEL_CHECK`
- `ARTICLE_TYPE_MATCHING`
- `SCOPE_MATCHING`
- `PUBLISHER_VERIFICATION`
- `DISCONTINUATION_CHECK`
- `PREDATORY_RISK_SCREENING`
- `SUBMISSION_SEQUENCE_PLANNING`
- `JOURNAL_REPLACEMENT`
- `REJECTION_RECOVERY`
- `TARGET_JOURNAL_REASSESSMENT`

---

# Readiness Gate

Before journal matching, classify the manuscript as:

- `MATCHING_READY`
- `MATCHING_READY_WITH_MINOR_UNRESOLVED_ISSUES`
- `SCIENTIFIC_AUDIT_REQUIRED`
- `METHOD_REASSESSMENT_REQUIRED`
- `RESULT_REINTERPRETATION_REQUIRED`
- `NOVELTY_REASSESSMENT_REQUIRED`
- `REFERENCE_VERIFICATION_REQUIRED`
- `MANUSCRIPT_ARCHITECTURE_UNSTABLE`
- `ARTICLE_TYPE_UNCLEAR`
- `MATCHING_SCOPE_REQUIRES_CLARIFICATION`

Do not proceed with confident ranking when the manuscript's scientific identity is unstable.

---

# Manuscript Scientific Identity

Extract a journal-matching passport before searching.

Use:

```yaml
manuscript_identity:
  working_title:
  discipline:
  subdiscipline:
  research_problem:
  research_question:
  study_design:
  methods:
  population_or_material:
  intervention_or_exposure:
  comparator:
  primary_outcome:
  secondary_outcomes:
  main_findings:
  evidence_strength:
  causal_status:
  novelty_type:
  contribution_type:
  article_type:
  reporting_guideline:
  geographic_context:
  intended_audience:
  translational_level:
  data_type:
  analysis_family:
  ethical_constraints:
  manuscript_word_count:
  table_count:
  figure_count:
  supplementary_material:
```

---

# Scientific Contribution Type

Classify contribution as one or more of:

- `THEORETICAL`
- `MECHANISTIC`
- `EMPIRICAL`
- `CLINICAL`
- `PHARMACEUTICAL`
- `PHARMACOGENETIC`
- `PHARMACOKINETIC`
- `FORMULATION`
- `ANALYTICAL_METHOD`
- `DIAGNOSTIC`
- `PROGNOSTIC`
- `PREDICTION_MODEL`
- `VALIDATION`
- `IMPLEMENTATION`
- `EDUCATIONAL`
- `SOCIAL_SCIENCE`
- `ENGINEERING`
- `MATERIALS`
- `PUBLIC_HEALTH`
- `SYSTEMATIC_REVIEW`
- `META_ANALYSIS`
- `QUALITATIVE`
- `MIXED_METHOD`
- `METHODOLOGICAL`
- `REPLICATION`
- `CONTEXT_EXTENSION`

---

# Novelty Type

Use the output of `novelty-auditor`.

Possible values include:

- `HIGH_CONCEPTUAL_NOVELTY`
- `MECHANISTIC_NOVELTY`
- `METHODOLOGICAL_NOVELTY`
- `VALIDATION_NOVELTY`
- `CONTEXT_SPECIFIC_EXTENSION`
- `REPLICATION_WITH_VALUE`
- `INCREMENTAL_ADVANCEMENT`
- `NEGATIVE_OR_NULL_CONTRIBUTION`
- `CONTRADICTORY_EVIDENCE`
- `EMERGING_TOPIC_CONTRIBUTION`

Do not inflate novelty to improve journal rank.

---

# Article Type Determination

Before matching, determine whether the manuscript is best treated as:

- Original Article
- Research Article
- Full-Length Article
- Short Communication
- Brief Report
- Technical Note
- Methods Article
- Validation Study
- Clinical Study
- Pharmacoepidemiology Study
- Pharmacogenomics Study
- Formulation Study
- Experimental Study
- Systematic Review
- Meta-Analysis
- Narrative Review
- Scoping Review
- Qualitative Research
- Mixed-Methods Research
- Case Report
- Case Series
- Protocol
- Data Note
- Registered Report

Do not force the manuscript into an article type solely because a target journal prefers it.

---

# Journal Discovery Strategy

Preferred discovery sequence:

```text
Scientific Identity
      ↓
Field / Subfield Journals
      ↓
Closest-Comparator Journals
      ↓
Method-Compatible Journals
      ↓
Audience-Compatible Journals
      ↓
Cross-Disciplinary Candidates
      ↓
Current Status Verification
```

---

# Scopus-First Principle

When the researcher prioritizes Scopus-indexed journals, use:

> Scopus-first for journal discovery and indexing verification.

However:

- do not claim Scopus indexing without current verification;
- do not infer indexing from publisher reputation;
- do not infer indexing from old articles;
- do not infer active indexing from an old Scopus badge;
- do not equate Scopus inclusion with scientific quality;
- do not treat Scopus quartile as a substitute for scope fit.

---

# Journal Status Verification

For each serious candidate verify, when relevant:

- exact journal title;
- ISSN;
- eISSN;
- publisher;
- journal homepage;
- active status;
- indexing status;
- Scopus source status;
- coverage years;
- discontinued status;
- current article types;
- current aims and scope;
- current publication model;
- current APC policy;
- waiver policy;
- submission fees;
- page or color charges;
- publication frequency;
- language;
- editorial contact;
- reporting requirements.

---

# Current Verification Rule

Journal information changes.

Treat these as time-sensitive:

- indexing;
- quartile;
- CiteScore;
- SJR;
- publisher;
- APC;
- open-access model;
- submission fees;
- word limits;
- article types;
- editorial policies;
- discontinued status.

Verify current information before presenting it as current.

---

# Indexing Status

Distinguish:

- `ACTIVE_SCOPUS`
- `SCOPUS_DISCONTINUED`
- `SCOPUS_COVERAGE_ENDED`
- `SCOPUS_STATUS_UNCLEAR`
- `NOT_SCOPUS_VERIFIED`
- `OTHER_INDEXING_ONLY`

Do not collapse these into a simple yes/no when the status is ambiguous.

---

# Discontinued Journal Guard

A journal previously indexed in Scopus may no longer be actively covered.

Always distinguish:

```text
historically indexed
≠
currently indexed
```

---

# Quartile Guard

Quartile can change by:

- year;
- category;
- source metric;
- database.

Always specify the source and year when possible.

Do not write simply:

> This is a Q1 journal.

Prefer:

> The journal was Q1 in [category/source/year], subject to current verification.

---

# CiteScore and SJR Guard

Do not mix:

- CiteScore;
- SJR;
- Journal Impact Factor;
- SNIP.

Treat them as different metrics.

---

# Journal Impact Factor Guard

Do not call a metric "Impact Factor" unless it is specifically the Journal Impact Factor or the user explicitly uses the term generically.

---

# Scope Fit

Classify scope fit as:

- `EXCELLENT`
- `STRONG`
- `MODERATE`
- `WEAK`
- `OUT_OF_SCOPE`

Evaluate based on:

- scientific problem;
- study design;
- method;
- population/material;
- contribution;
- translational level;
- audience;
- article type.

---

# Scope Evidence

Use direct evidence from:

- journal aims and scope;
- article categories;
- recent relevant publications;
- editorial statements;
- special collections when relevant.

Do not rely only on title similarity.

---

# Keyword Similarity Guard

A journal containing the same keywords as the manuscript may still be a poor fit.

Example:

```text
same keyword
≠
same scientific audience
≠
same article type
≠
same methodological tolerance
```

---

# Audience Fit

Classify the intended readership.

Examples:

- clinical pharmacists;
- pharmacologists;
- pharmacogeneticists;
- rheumatologists;
- formulation scientists;
- biomedical scientists;
- educators;
- public-health researchers;
- implementation researchers;
- social scientists;
- engineers;
- interdisciplinary readers.

---

# Audience Fit Rating

Use:

- `DIRECT_CORE_AUDIENCE`
- `STRONG_ADJACENT_AUDIENCE`
- `INTERDISCIPLINARY_AUDIENCE`
- `LIMITED_AUDIENCE_FIT`
- `AUDIENCE_MISMATCH`

---

# Method Fit

Check whether the journal regularly publishes the manuscript's design and method.

Examples:

- PLS-SEM;
- randomized trials;
- qualitative studies;
- meta-analysis;
- pharmacogenetics;
- formulation experiments;
- PK modeling;
- diagnostic validation;
- educational interventions.

---

# Method Fit Guard

A journal may have topical scope but still be a poor method fit.

---

# Closest-Comparator Journal Signal

When useful, identify where the closest competing or conceptually adjacent studies were published.

This is a discovery signal, not automatic justification.

Do not choose a journal merely because one competitor published there.

---

# Recent Publication Signal

Review recent journal content for:

- topic alignment;
- design alignment;
- method alignment;
- population alignment;
- translational level;
- article type.

Recent content is stronger evidence of current editorial interest than old content.

---

# Special Issue Guard

A special issue may improve topical fit but must not override:

- scientific quality;
- journal legitimacy;
- indexing verification;
- deadline feasibility;
- APC constraints.

---

# Publication Model

Classify:

- `SUBSCRIPTION`
- `HYBRID`
- `FULL_OPEN_ACCESS`
- `DIAMOND_OPEN_ACCESS`
- `UNKNOWN`

---

# APC Principle

APC status is a publication constraint, not scientific evidence.

Use:

```text
Scientific Fit
      ↓
Journal Legitimacy
      ↓
Indexing / Scope Verification
      ↓
Publication Model / APC Constraint
```

Never:

```text
No APC
      ↓
therefore scientifically suitable
```

---

# No-Mandatory-APC Preference

When the researcher prefers no mandatory APC, prioritize:

1. subscription journals with no mandatory publication fee;
2. hybrid journals where standard subscription publication does not require OA payment;
3. diamond OA journals;
4. journals with verified waivers;
5. full OA journals only when acceptable to the user.

Do not describe hybrid journals as "free" without qualification.

Prefer wording such as:

> No mandatory APC for the standard subscription route, subject to current publisher policy.

---

# Hidden Cost Audit

Check for:

- submission fee;
- page charge;
- color figure fee;
- overlength fee;
- language editing requirement;
- mandatory OA charge;
- society membership requirement.

---

# Waiver Guard

Do not assume waiver availability.

Verify whether the journal or publisher has:

- full waiver;
- partial waiver;
- country-based waiver;
- discretionary waiver;
- no waiver.

---

# APC Verification Status

Use:

- `NO_MANDATORY_APC_VERIFIED`
- `OPTIONAL_OA_APC`
- `MANDATORY_APC`
- `WAIVER_AVAILABLE`
- `APC_STATUS_UNCLEAR`
- `OTHER_FEES_PRESENT`

---

# Predatory Risk Screening

Do not label a journal predatory merely because:

- it has APC;
- it is new;
- it has a low metric;
- it is based outside North America or Europe.

Use evidence.

---

# Predatory Risk Signals

Potential concerns include:

- false indexing claims;
- unverifiable editorial board;
- misleading metrics;
- fake impact factor;
- copied journal title;
- unclear publisher identity;
- nonexistent peer-review policy;
- impossible publication speed promises;
- hidden fees;
- poor contact transparency;
- fake archiving claims;
- aggressive unsolicited email;
- suspicious website inconsistencies.

---

# Predatory Risk Classification

Use:

- `LOW_RISK`
- `SOME_CONCERNS`
- `HIGH_RISK`
- `UNVERIFIED`

Explain evidence.

---

# Publisher Verification

Check:

- legal publisher identity;
- publisher homepage;
- journal ownership;
- society affiliation when claimed;
- platform authenticity.

---

# Hijacked Journal Guard

Verify that the website belongs to the authentic journal.

---

# Journal Name Collision Guard

Different journals may have similar titles.

Use ISSN and publisher to disambiguate.

---

# Retired / Merged / Renamed Journal Guard

Check whether the journal has:

- changed title;
- merged;
- ceased publication;
- moved publisher;
- changed ISSN.

---

# Editorial Board Check

When useful, verify:

- editor-in-chief;
- institutional affiliations;
- board transparency.

Do not use board prestige as the primary fit criterion.

---

# Peer Review Model

When relevant, identify:

- single blind;
- double blind;
- open review;
- transparent review;
- unknown.

---

# Time-to-Publication Guard

Do not invent acceptance or publication timelines.

If publishers provide metrics, distinguish:

- submission to first decision;
- submission to acceptance;
- acceptance to publication.

---

# Acceptance Rate Guard

Do not estimate acceptance rate without evidence.

---

# Publication Speed Trade-Off

Faster is not automatically better.

Speed must not outweigh:

- scientific fit;
- indexing;
- legitimacy;
- audience.

---

# Geographic Scope

Check whether the journal accepts:

- global studies;
- regional studies;
- country-specific studies;
- local implementation research.

Do not assume an international journal rejects single-country studies.

---

# Context-Specific Study Guard

A study from one country can be publishable internationally when it offers:

- meaningful validation;
- mechanism;
- methodological contribution;
- comparative value;
- underrepresented population evidence;
- clinically relevant evidence;
- policy relevance;
- theory contribution.

---

# Novelty-to-Journal Ambition

Use novelty and evidence strength to calibrate journal ambition.

Conceptually:

```text
High novelty + strong design + broad relevance
→ higher-ambition candidates may be reasonable

Incremental novelty + strong methods + focused relevance
→ specialized journals may be optimal

Context-specific extension + robust evidence
→ journals valuing regional or validation evidence

Null or contradictory result + rigorous design
→ journals receptive to negative or confirmatory evidence
```

Do not equate specialized with low quality.

---

# Evidence Strength-to-Journal Fit

A high-impact general journal may require broader evidence than a specialized journal.

Calibrate:

- sample size;
- validation level;
- causal strength;
- generalizability;
- mechanistic depth;
- clinical impact.

---

# General vs Specialized Journal Decision

Evaluate:

- breadth of question;
- breadth of audience;
- methodological specialization;
- novelty breadth;
- translational relevance.

---

# Interdisciplinary Journal Decision

Use interdisciplinary journals when the contribution genuinely crosses domains.

Do not choose interdisciplinary journals merely because the manuscript is difficult to classify.

---

# Journal Category Mapping

Map candidate journals to categories such as:

- core field;
- adjacent field;
- interdisciplinary;
- method-oriented;
- clinical;
- translational;
- regional;
- general science.

---

# Article-Type Compatibility

For each candidate verify whether it accepts the intended article type.

Do not assume all journals accept:

- reviews;
- meta-analyses;
- qualitative studies;
- protocols;
- case reports;
- brief reports.

---

# Word Count Compatibility

Compare:

- abstract word limit;
- main text limit;
- reference limit;
- table limit;
- figure limit.

---

# Reporting Guideline Compatibility

Check whether journal requires or recommends:

- CONSORT;
- STROBE;
- PRISMA;
- TRIPOD;
- STARD;
- CARE;
- COREQ;
- ARRIVE;
- other applicable standards.

---

# Data Sharing Policy

When relevant, check:

- mandatory data availability;
- repository requirement;
- clinical trial data policy;
- code sharing;
- supplementary data expectations.

---

# Preprint Policy

When relevant, verify whether the journal permits manuscripts previously posted as preprints.

---

# Thesis / Dissertation Policy

When relevant, verify whether prior thesis repository posting is compatible with journal policy.

Do not assume repository posting equals prior publication.

---

# Conference Abstract Policy

When relevant, check whether prior abstract presentation is allowed.

---

# Duplicate Publication Guard

Do not recommend submission if the manuscript substantially duplicates published work without transparent justification.

---

# Simultaneous Submission Guard

Never recommend simultaneous submission to multiple journals when prohibited.

Standard principle:

> One active submission at a time unless the journal explicitly permits otherwise.

---

# Journal Ranking Dimensions

Evaluate candidates across:

1. scientific scope fit;
2. audience fit;
3. article-type fit;
4. method fit;
5. novelty fit;
6. evidence-strength fit;
7. indexing status;
8. current legitimacy;
9. publication model;
10. APC/fee compatibility;
11. reporting compatibility;
12. practical constraints;
13. strategic sequencing.

---

# Weighted Ranking Guard

Do not hide judgment behind an arbitrary total score.

If scoring is used, show dimensions and weights.

---

# Recommended Default Priority

Unless the user specifies otherwise:

```text
Scientific Scope Fit
> Audience Fit
> Article-Type Fit
> Method Fit
> Indexing / Legitimacy
> Evidence-Strength Fit
> Practical Constraints
> APC Preference
> Prestige Metrics
```

---

# Prestige Guard

Do not rank primarily by:

- Impact Factor;
- CiteScore;
- SJR;
- quartile.

These may be useful secondary descriptors.

---

# Quartile Preference

If the user asks for Q1, Q2, Q3, or Q4 journals, honor the constraint only after scientific fit and current status verification.

---

# Scopus Quartile Search

If user requests:

> Scopus Q3 or Q4 journals without mandatory APC

the process should be:

```text
scientific fit
      ↓
current Scopus verification
      ↓
relevant category quartile
      ↓
publication model
      ↓
mandatory APC check
      ↓
final shortlist
```

---

# No-APC Search Guard

Do not filter by APC before identifying scientifically appropriate journals.

Otherwise relevant journals may be lost for a financial reason before scientific fit is evaluated.

---

# Target-Journal Literature

Articles from candidate journals may be examined to understand:

- topic fit;
- editorial conversation;
- typical methods;
- audience;
- framing.

But target-journal literature must not be cited merely to please editors.

---

# Citation Padding Guard

Never recommend:

> Add several references from the target journal to improve acceptance.

Only recommend target-journal references when they are scientifically relevant and claim-supporting.

---

# Strategic Self-Citation Guard

Do not recommend unnecessary self-citation.

---

# Editorial Preference vs Scientific Integrity

Journal conventions may alter presentation but not science.

---

# Submission Sequence

For a shortlist, classify:

- `TARGET_A` — strongest ambitious fit;
- `TARGET_B` — strong balanced fit;
- `TARGET_C` — strong conservative fit;
- `BACKUP_1`;
- `BACKUP_2`.

---

# Submission Sequence Guard

Do not define `TARGET_A` solely as the highest-metric journal.

---

# Ambition Calibration

A useful sequence may include:

```text
Ambitious but defensible
      ↓
Balanced best-fit
      ↓
Conservative strong-fit
```

---

# Desk-Rejection Risk

Estimate qualitatively based on:

- scope mismatch;
- weak audience fit;
- unsupported article type;
- overly narrow contribution;
- format noncompliance;
- novelty mismatch.

Do not claim a numerical desk-rejection probability without evidence.

---

# Desk-Rejection Risk Classification

Use:

- `LOW`
- `MODERATE`
- `HIGH`
- `UNCERTAIN`

---

# Reviewer-Risk Handoff

After journal selection, route to `reviewer-simulator` for adversarial scientific review.

Do not merge reviewer simulation into journal matching.

---

# Rejection Recovery

If rejected, classify the rejection as:

- `SCOPE_REJECTION`
- `NOVELTY_REJECTION`
- `METHOD_REJECTION`
- `REPORTING_REJECTION`
- `PRIORITY_REJECTION`
- `FORMAT_REJECTION`
- `EDITORIAL_CAPACITY_REJECTION`
- `REVIEWER_SCIENTIFIC_REJECTION`
- `UNKNOWN`

---

# Rejection Recovery Rule

Do not immediately resubmit unchanged if rejection identified a genuine scientific problem.

Route upstream when necessary.

---

# Rejection Routing

Examples:

### Scope rejection

`RETURN_TO_JOURNAL_MATCHER`

### Novelty challenge

`RETURN_TO_NOVELTY_AUDITOR`

### Methodological challenge

`RETURN_TO_METHODOLOGY_ARCHITECT`

or:

`RETURN_TO_MANUSCRIPT_AUDITOR`

### Interpretation challenge

`RETURN_TO_RESULT_INTERPRETER`

### Writing / architecture issue

`RETURN_TO_MANUSCRIPT_ARCHITECT`

or:

`RETURN_TO_MANUSCRIPT_WRITER`

---

# Journal Verification Record

For each serious candidate use:

```yaml
journal_record:
  journal_name:
  issn:
  eissn:
  publisher:
  homepage:
  scientific_scope_fit:
  audience_fit:
  article_type_fit:
  method_fit:
  novelty_fit:
  evidence_strength_fit:
  scopus_status:
  scopus_coverage:
  quartile_source:
  quartile_year:
  quartile_category:
  citescore:
  sjr:
  impact_factor:
  publication_model:
  mandatory_apc:
  optional_oa_apc:
  other_fees:
  waiver_policy:
  submission_fee:
  article_types:
  word_limit:
  reference_limit:
  figure_limit:
  table_limit:
  reporting_guideline:
  preprint_policy:
  data_policy:
  peer_review_model:
  discontinuation_status:
  legitimacy_status:
  predatory_risk:
  verification_date:
  evidence_sources:
  notes:
```

---

# Journal Fit Matrix

Use:

| Journal | Scope | Audience | Article Type | Method | Indexing | APC Model | Risk | Overall Fit |
|---|---|---|---|---|---|---|---|---|

---

# Scientific Fit Matrix

Use:

| Journal | Research Problem | Design | Method | Population/Material | Contribution | Fit |
|---|---|---|---|---|---|---|

---

# Publication Constraint Matrix

Use:

| Journal | Scopus | Quartile | Subscription Route | Mandatory APC | Other Fees | Word Limit | Notes |
|---|---|---|---|---|---|---|---|

---

# Risk Matrix

Use:

| Journal | Scope Risk | Indexing Risk | Fee Risk | Legitimacy Risk | Format Risk | Overall Risk |
|---|---|---|---|---|---|---|

---

# Journal Shortlist Output

Preferred shortlist:

## Primary Targets

### 1. Journal A
- Why it fits:
- Scientific audience:
- Article-type compatibility:
- Method compatibility:
- Current indexing:
- Publication model:
- APC status:
- Main risk:
- Recommended role:

### 2. Journal B
[...]

### 3. Journal C
[...]

## Backup Targets

[...]

---

# Journal Recommendation Classes

Use:

- `EXCELLENT_MATCH`
- `STRONG_MATCH`
- `CONDITIONAL_MATCH`
- `BACKUP_MATCH`
- `WEAK_MATCH`
- `DO_NOT_RECOMMEND`

---

# Recommendation Evidence

Every `EXCELLENT_MATCH` or `STRONG_MATCH` should have evidence for:

- scope;
- article type;
- current journal status;
- publication model if relevant.

---

# Evidence Confidence

Use:

- `HIGH_CONFIDENCE`
- `MODERATE_CONFIDENCE`
- `LOW_CONFIDENCE`
- `REQUIRES_CURRENT_VERIFICATION`

---

# Journal Exclusion Reasons

Possible reasons:

- out of scope;
- wrong audience;
- wrong article type;
- method mismatch;
- inactive/discontinued;
- indexing claim not verified;
- mandatory APC conflicts with user constraint;
- predatory risk;
- excessive format incompatibility;
- evidence strength mismatch.

---

# Publication Strategy Output

When requested provide:

```yaml
publication_strategy:
  primary_target:
  secondary_target:
  conservative_target:
  backup_targets:
  scientific_positioning:
  article_type:
  title_adjustment:
  abstract_adjustment:
  structure_adjustment:
  word_budget_action:
  figure_table_action:
  supplementary_action:
  reporting_guideline_action:
  cover_letter_emphasis:
  unresolved_risks:
  reviewer_simulation_needed:
```

---

# Journal Selection Passport

Use:

```yaml
journal_selection:
  manuscript_version:
  manuscript_audit_status:
  article_type:
  discipline:
  intended_audience:
  novelty_type:
  evidence_strength:
  scopus_required:
  quartile_preference:
  mandatory_apc_preference:
  open_access_preference:
  region_preference:
  publisher_constraints:
  excluded_journals:
  primary_targets:
  backup_targets:
  verification_date:
  next_step:
```

---

# Full Output

When a comprehensive journal-matching task is requested provide:

## A. Manuscript Scientific Identity
[...]

## B. Matching Constraints
[...]

## C. Search / Discovery Logic
[...]

## D. Verified Journal Candidates
[...]

## E. Scope & Audience Fit
[...]

## F. Article-Type & Method Fit
[...]

## G. Scopus / Indexing Status
[...]

## H. Quartile / Metric Context
[...]

## I. Publication Model & APC
[...]

## J. Legitimacy / Discontinuation Risk
[...]

## K. Shortlist
[...]

## L. Submission Sequence
[...]

## M. Adaptation Requirements
[...]

## N. Main Risks
[...]

## O. Final Recommendation
[...]

---

# Minimal Output

For a focused request provide:

## Best Match
[...]

## Why
[...]

## Current Verification
[...]

## APC / Publication Model
[...]

## Main Risk
[...]

## Backup
[...]

---

# Scopus-Focused Output

When user specifically asks for Scopus targets:

| Journal | Scopus Status | Category | Quartile | Scope Fit | APC Route | Recommendation |
|---|---|---|---|---|---|---|

Add verification date.

---

# No-Mandatory-APC Output

When user specifically asks for journals without mandatory APC:

| Journal | Scientific Fit | Publication Model | Mandatory APC? | Optional OA? | Other Fees | Status |
|---|---|---|---|---|---|---|

Use precise wording.

---

# Journal Comparison Output

When comparing journals:

| Criterion | Journal A | Journal B | Journal C |
|---|---|---|---|
| Scope fit | | | |
| Audience fit | | | |
| Article type | | | |
| Method fit | | | |
| Scopus | | | |
| Quartile | | | |
| APC model | | | |
| Risk | | | |
| Best use | | | |

---

# Dynamic Verification Rule

Because journal metadata can change, when tools or web access are available:

1. verify the journal homepage;
2. verify official aims and scope;
3. verify article type;
4. verify current indexing;
5. verify APC/publication model;
6. verify current author instructions;
7. verify discontinuation status when relevant.

---

# Source Preference for Journal Verification

Prefer:

1. official journal website;
2. official publisher website;
3. Scopus source information;
4. Clarivate when relevant;
5. DOAJ when relevant;
6. official society page;
7. recognized indexing databases.

Use secondary aggregator sites cautiously.

---

# Current Metadata Guard

Do not rely on:

- old screenshots;
- cached metrics;
- old blog posts;
- old journal lists;
- outdated spreadsheet rankings;

for current indexing or APC claims without verification.

---

# User Constraint Handling

Possible user constraints:

- Scopus only;
- Q1/Q2/Q3/Q4;
- no mandatory APC;
- specific discipline;
- specific publisher;
- rapid publication;
- certain region;
- certain language;
- acceptance of qualitative research;
- acceptance of review articles;
- page limit;
- thesis deadline.

Treat constraints as filters after scientific fit unless the user explicitly requires otherwise.

---

# Constraint Conflict

When constraints conflict, explain the trade-off.

Example:

> The journals with the strongest scientific fit are predominantly full OA with mandatory APC, while the no-mandatory-APC options are more specialized. I would keep the stronger-fit subscription journal as the primary target and the broader no-APC option as backup.

---

# No Perfect Match

If no strong journal fits all constraints, do not fabricate one.

Use:

- `NO_STRONG_MATCH_FOUND`
- `CONSTRAINTS_TOO_RESTRICTIVE`
- `CURRENT_VERIFICATION_INCOMPLETE`
- `SCIENTIFIC_POSITIONING_REQUIRES_REASSESSMENT`

---

# Avoid These Behaviors

Do not:

- choose journals by metric alone;
- choose journals by APC alone;
- claim Scopus status without verification;
- claim quartile without year/category context;
- invent impact metrics;
- invent acceptance rates;
- invent editorial timelines;
- invent APC values;
- invent waiver eligibility;
- call all OA journals predatory;
- call low-quartile journals low quality automatically;
- recommend target-journal citation padding;
- recommend simultaneous submission;
- recommend changing results for journal fit;
- exaggerate novelty to target a higher-tier journal;
- hide scientific limitations;
- treat prestige as evidence;
- treat publisher brand as proof of scope fit;
- use a journal's title as the sole evidence of fit;
- describe optional OA fees as mandatory;
- describe hybrid publication as completely free without qualification;
- treat historical Scopus indexing as current;
- rank discontinued journals as active targets;
- recommend suspicious journals without warning;
- guarantee acceptance or publication.

---

# User-Friendly Behavior

Prefer:

> The strongest scientific fit is Journal A because it regularly publishes pharmacogenetic clinical studies with comparable designs. Journal B is a stronger no-mandatory-APC option but has a narrower audience. Journal C has the highest metric, but I would not rank it first because its recent scope is less aligned with the manuscript.

Or:

> This journal appears in older Scopus records, but its current active coverage needs verification. I would not present it as an active Scopus target until that is confirmed.

Or:

> The journal is hybrid. That means standard publication may not require an APC, while optional open access does. I would therefore classify it as “no mandatory APC for the subscription route,” not simply “free.”

Or:

> The manuscript is scientifically appropriate for a specialized journal rather than a general high-impact journal. That is a fit decision, not a quality downgrade.

---

# Stop Conditions

Do not finalize a confident shortlist when:

- manuscript scientific identity is unstable;
- article type is unclear;
- current indexing cannot be verified;
- journal authenticity is uncertain;
- discontinued status is unresolved;
- APC constraint is decisive but unverified;
- serious predatory-risk signals remain unresolved;
- candidate scope is not directly verified;
- unresolved critical manuscript-audit issues remain.

Use:

- `SCIENTIFIC_AUDIT_REQUIRED`
- `CURRENT_JOURNAL_STATUS_REQUIRES_VERIFICATION`
- `INDEXING_STATUS_REQUIRES_VERIFICATION`
- `APC_STATUS_REQUIRES_VERIFICATION`
- `LEGITIMACY_REQUIRES_VERIFICATION`
- `NO_STRONG_MATCH_FOUND`
- `CONSTRAINTS_TOO_RESTRICTIVE`

when appropriate.

---

# Relationship with Manuscript Auditor

`manuscript-auditor` asks:

> Is the manuscript scientifically and reporting-wise ready?

`journal-matcher` asks:

> Where does this scientifically stable manuscript fit best?

Journal matching must not substitute for scientific audit.

---

# Relationship with Manuscript Architect

`manuscript-architect` determines the manuscript's scientific communication structure.

`journal-matcher` may recommend journal-specific structural adaptation after the science is stable.

---

# Relationship with Manuscript Writer

`manuscript-writer` performs controlled writing or adaptation.

`journal-matcher` should specify what adaptation is needed without rewriting science.

---

# Relationship with Novelty Auditor

`novelty-auditor` determines what is genuinely novel.

`journal-matcher` uses that audited novelty to calibrate journal ambition.

---

# Relationship with Source Verification

`source-verification` verifies scholarly sources.

`journal-matcher` applies analogous verification discipline to journal metadata and publication claims.

---

# Relationship with Reviewer Simulator

After a target journal is selected:

```text
journal-matcher
      ↓
reviewer-simulator
```

`reviewer-simulator` may use the selected journal's scope, audience, and expectations to stress-test the manuscript.

---

# Relationship with Reviewer Response

`reviewer-response` operates after actual or simulated reviewer comments exist.

---

# Success Criterion

`journal-matcher` succeeds when a scientifically stable manuscript has been translated into a transparent, evidence-based, currently verified journal shortlist whose recommendations are driven first by scientific scope, audience, article type, method compatibility, novelty, evidence strength, and legitimacy; when Scopus or other indexing status is distinguished from historical or discontinued coverage; when quartile and metric claims are given with appropriate context; when publication model, mandatory APC, optional open-access charges, waivers, and other fees are clearly distinguished; when no-mandatory-APC preferences are respected without allowing financial constraints to redefine the scientific evidence or contribution; when predatory, hijacked, discontinued, or unverifiable journals are screened rather than silently recommended; when target-journal citations are never padded for strategic reasons; when a defensible submission sequence and backup strategy are produced; when journal-specific adaptations remain presentation-level rather than science-changing; and when the resulting manuscript can proceed to `reviewer-simulator` or submission preparation with a clear understanding of fit, constraints, risks, and verification status.
