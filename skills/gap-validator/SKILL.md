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

Represent the candidate gap explicitly:

```yaml
gap:
  established_knowledge:
  unresolved_condition:
  boundary:
  scientific_consequence:
  proposed_gap_type:
  originating_sota_status:
  evidence_cutoff:
  closest_known_competitor:
  known_threats:
```

Unknown fields remain unknown.

Do not silently add a stronger boundary or stronger scientific consequence than the evidence supports.

---

# 3. Validation Principle

`gap-validator` is an adversarial falsification layer.

The default question is:

> What evidence would make this gap weaker, narrower, reframed, substantially resolved, or false?

The workflow must seek disconfirming evidence before supportive evidence.

---

# 4. Preferred Validation Architecture

Use:

```text
CANDIDATE_GAP
      ↓
Normalize Claim
      ↓
Terminology Expansion
      ↓
Current Literature Search
      ↓
Closest-Competitor Search
      ↓
Citation Chaining
      ↓
Adjacent-Discipline Search
      ↓
Methodological-Equivalent Search
      ↓
Population / Context Comparison
      ↓
Contradictory Evidence Review
      ↓
Evidence Synthesis
      ↓
Adversarial Judgment
      ↓
Validated / Partial / Reframed / Weak / Resolved / Rejected / Inconclusive
```

---

# 5. Required Upstream Context

Prefer inputs from:

- `sota-builder`;
- `gap-discovery`;
- `evidence-synthesis`;
- `literature-screening`;
- `citation-chaining`;
- `source-verification`;
- `reference-integrity-guard`.

If the upstream evidence is weak or outdated, do not pretend the gap can be robustly validated.

---

# 6. Candidate Gap Types

Validation should preserve the proposed gap type when appropriate:

- evidence;
- contradiction;
- replication;
- validation;
- mechanism;
- causal;
- theoretical;
- conceptual;
- methodological;
- measurement;
- population;
- context;
- temporal;
- implementation;
- translational;
- prediction;
- diagnostic;
- prognostic;
- generalizability;
- integration.

The validator may reclassify the gap if a different type better matches the surviving unresolved condition.

---

# 7. Status Vocabulary

Possible final statuses:

- `VALIDATED_STRONG_GAP`
- `VALIDATED_MODERATE_GAP`
- `PARTIALLY_VALIDATED_GAP`
- `REFRAMED_GAP`
- `WEAK_GAP`
- `GAP_SUBSTANTIALLY_RESOLVED`
- `GAP_REJECTED`
- `VALIDATION_INCONCLUSIVE`

Do not force a positive status.

---

# 8. Status Meaning — Validated Strong Gap

Use `VALIDATED_STRONG_GAP` only when:

- the unresolved condition is scientifically meaningful;
- current verified evidence still leaves it unresolved;
- close competitors do not substantially close it;
- terminology variants do not reveal hidden resolution;
- equivalent methods do not already answer it;
- adjacent disciplines do not substantially resolve it;
- the gap remains researchable and consequential.

Strong does not mean guaranteed novelty.

---

# 9. Status Meaning — Validated Moderate Gap

Use `VALIDATED_MODERATE_GAP` when the gap remains real but:

- evidence is narrower;
- the boundary is more limited;
- some competitors partially address it;
- scientific value is meaningful but not transformative.

---

# 10. Status Meaning — Partially Validated Gap

Use `PARTIALLY_VALIDATED_GAP` when only part of the original candidate survives.

Example:

```text
Original:
No evidence exists on X in population Y.

Finding:
Evidence on X exists, but external validation in subgroup Z is missing.

Outcome:
PARTIALLY_VALIDATED_GAP
```

---

# 11. Status Meaning — Reframed Gap

Use `REFRAMED_GAP` when the original gap claim is scientifically inaccurate but a different unresolved condition remains defensible.

Reframing is often preferable to defending a weak original claim.

---

# 12. Status Meaning — Weak Gap

Use `WEAK_GAP` when the unresolved condition exists but:

- importance is limited;
- evidence is nearly sufficient;
- contribution would be incremental;
- the proposed study would add little.

---

# 13. Status Meaning — Substantially Resolved

Use `GAP_SUBSTANTIALLY_RESOLVED` when current evidence addresses most of the original uncertainty.

A minor residual uncertainty may remain, but it is not strong enough to support the original gap claim.

---

# 14. Status Meaning — Gap Rejected

Use `GAP_REJECTED` when:

- credible current evidence already answers the proposed gap;
- the claim depends on false absence;
- equivalent studies clearly exist;
- the proposed difference is only superficial.

Do not invent a replacement gap unless evidence supports one.

---

# 15. Status Meaning — Validation Inconclusive

Use `VALIDATION_INCONCLUSIVE` when:

- key full text is unavailable;
- current search is incomplete;
- critical source identity is unresolved;
- terminology remains ambiguous;
- evidence is too sparse or unstable.

Inconclusive is better than false certainty.

---

# 16. Gap Claim Decomposition

Break the claim into testable components:

```text
What is known?
What is allegedly unknown?
Under what boundary?
Why does that boundary matter?
What evidence could falsify the claim?
```

---

# 17. Claim Precision Guard

A broad gap is easier to falsify.

Example:

Weak:

> No studies have investigated digital marketing and repurchase intention.

More testable:

> Existing studies assess digital marketing and repurchase intention, but independent evidence testing mechanism M under context C remains limited.

Do not narrow the gap opportunistically after every threat without recording the change.

---

# 18. Validation Audit Trail

Use:

```yaml
gap_validation:
  candidate_gap_id:
  original_statement:
  normalized_statement:
  proposed_type:
  search_update:
  terminology_expansion:
  competitor_search:
  citation_chaining:
  adjacent_discipline_search:
  method_equivalence_search:
  contradiction_review:
  surviving_uncertainty:
  final_status:
  final_gap_statement:
  rationale:
  limitations:
```

---

# 19. Terminology Expansion

Before claiming absence, search:

- synonyms;
- historical terms;
- abbreviations;
- alternative spellings;
- neighboring constructs;
- translated terms;
- technical aliases;
- older method labels.

False gaps often arise from semantic narrowness.

---

# 20. Terminology Expansion Record

Use:

```yaml
terminology_expansion:
  core_term:
  synonyms:
  historical_terms:
  abbreviations:
  adjacent_constructs:
  method_aliases:
  discipline_specific_terms:
```

---

# 21. Exact-Term Bias Guard

Do not validate a gap because the exact phrase is absent.

Scientific equivalence matters more than wording.

---

# 22. Construct Equivalence Test

Ask whether differently named constructs are:

- identical;
- overlapping;
- nested;
- functionally equivalent;
- merely related.

Route difficult construct questions to:

`conceptual-framework`.

---

# 23. Theory Equivalence Test

Ask whether a gap claimed under one theory has already been addressed under another explanatory framework.

Route formal theory comparison to:

`theoretical-framework`.

---

# 24. Method Equivalence Test

Ask:

> Has a different method already answered the same substantive scientific question?

Examples:

- SEM vs regression;
- one genotyping platform vs another;
- different validated assay;
- different causal estimator;
- qualitative method with equivalent phenomenon coverage.

Method labels alone do not protect a gap.

---

# 25. Software Independence

Preserve:

```text
SmartPLS vs AMOS vs R vs Python
≠
scientific gap
```

Software difference matters only if it enables substantively different inference.

---

# 26. Database Search Update

For scholarly evidence, use a current search appropriate to field velocity.

Prefer:

`scopus-literature-search`

for Scopus-first discovery.

If direct Scopus access is unavailable, fall back appropriately without claiming direct Scopus verification.

---

# 27. Search Freshness

Record:

```yaml
search_freshness:
  field_velocity:
  previous_cutoff:
  current_search_date:
  newest_relevant_record:
  update_status:
```

---

# 28. Fast-Moving Field Rule

In fast-moving fields:

- prioritize current primary studies;
- inspect online-first publications;
- forward-chain recent anchors;
- check recent reviews for newer primary evidence.

A gap may disappear quickly.

---

# 29. Slow-Moving Field Rule

In slower fields:

- seminal evidence may remain central;
- theoretical resolution may evolve slowly;
- old evidence can still defeat a gap.

Do not impose arbitrary recency.

---

# 30. Closest-Competitor Search

Identify studies with maximum overlap across:

- question;
- population;
- exposure/intervention;
- comparator;
- outcome;
- mechanism;
- method;
- theory;
- context.

---

# 31. Competitor Record

Use:

```yaml
competitor:
  reference:
  question_overlap:
  population_overlap:
  method_overlap:
  mechanism_overlap:
  outcome_overlap:
  context_overlap:
  contribution_overlap:
  gap_effect:
```

---

# 32. Competitor Threat Levels

Possible levels:

- `CRITICAL_THREAT`
- `MAJOR_THREAT`
- `MODERATE_THREAT`
- `MINOR_THREAT`
- `NOT_A_THREAT`

Do not classify based on journal prestige.

---

# 33. Closest-Competitor Matrix

Use:

| Competitor | Scientific Overlap | Key Difference | Threat Level | Gap Effect |
|---|---|---|---|---|

---

# 34. Citation Chaining

Use `citation-chaining` to test:

- earlier overlooked evidence;
- newer citing studies;
- replications;
- contradictions;
- methodological refinements.

Backward and forward citation tracing can expose false novelty or false absence.

---

# 35. Anchor Strategy

Good anchors include:

- closest competitor;
- seminal study;
- recent high-relevance study;
- systematic review;
- method-development paper.

Do not use citation count alone to choose anchors.

---

# 36. Adjacent-Discipline Search

Search neighboring disciplines when they may contain scientifically equivalent work.

Examples:

- pharmacy ↔ pharmacology;
- education ↔ psychology;
- engineering ↔ materials science;
- public health ↔ epidemiology;
- management ↔ consumer behavior.

---

# 37. Adjacent-Discipline Guard

Do not exclude an adjacent discipline merely because terminology differs.

If the scientific problem is materially equivalent, it can weaken the gap.

---

# 38. Population Comparison

For population gaps ask:

- Does biology differ?
- Does exposure differ?
- Does baseline risk differ?
- Does health system differ?
- Does culture alter mechanism?
- Does genotype distribution differ?
- Does development stage matter?

If none plausibly matter, the population gap may be weak.

---

# 39. Geography Validation

A country-specific gap requires more than geographic absence.

Validate whether location changes:

- population structure;
- context;
- environment;
- regulation;
- healthcare delivery;
- education system;
- market behavior;
- implementation.

---

# 40. Context Comparison

For context gaps test whether context is a plausible moderator or boundary condition.

Do not assume every institutional or national setting produces scientifically distinct evidence.

---

# 41. Mechanism-Gap Validation

For a proposed mechanism gap:

1. identify the observed relationship;
2. identify proposed pathways;
3. search for direct mechanism tests;
4. search for equivalent mediators/pathways under other terminology;
5. assess whether mechanism is already substantially known.

---

# 42. Causal-Gap Validation

For causal gaps ask whether the literature already contains:

- randomized evidence;
- quasi-experimental evidence;
- longitudinal designs;
- instrumental variables;
- natural experiments;
- target-trial emulation;
- other credible causal strategies.

Do not call a causal gap merely because most papers are cross-sectional.

---

# 43. Replication-Gap Validation

Verify whether replications are truly independent.

Check:

- cohort identity;
- dataset identity;
- research group;
- overlapping sample;
- publication family.

Route ambiguity to `reference-integrity-guard`.

---

# 44. Validation-Gap Validation

Distinguish:

- internal validation;
- temporal validation;
- geographic validation;
- external validation;
- prospective validation;
- clinical validation.

A model with external validation may defeat a claimed validation gap even if it uses another software environment.

---

# 45. Measurement-Gap Validation

Search for:

- alternative validated instruments;
- translations;
- adaptations;
- objective measures;
- assays;
- measurement invariance studies.

A measurement gap may disappear if an equivalent validated tool exists.

---

# 46. Theory-Gap Validation

Search:

- original theory;
- refinements;
- empirical tests;
- competing theories;
- boundary-condition studies;
- critiques.

A theory gap may survive as a boundary-condition gap rather than a complete absence.

---

# 47. Conceptual-Gap Validation

Check whether the allegedly unintegrated constructs have already been linked under:

- another framework;
- another discipline;
- another construct name;
- a higher-order model.

---

# 48. Methodological-Gap Validation

A methodological gap survives only if existing designs materially prevent answering an important scientific question.

Ask:

> Would the proposed methodological change improve inference, validity, resolution, or reproducibility?

If not, the gap is weak.

---

# 49. Temporal-Gap Validation

Check whether longer-term or longitudinal studies already exist.

A short-follow-up literature does not automatically imply a gap if the scientific outcome is inherently short-term.

---

# 50. Implementation-Gap Validation

Ensure that prior efficacy/effectiveness evidence is mature enough for implementation to be the next meaningful stage.

Search:

- adoption;
- fidelity;
- feasibility;
- acceptability;
- sustainability;
- scale-up.

---

# 51. Translational-Gap Validation

Check whether prerequisite evidence exists at the preceding translational stage.

Do not validate a human translational gap if preclinical evidence is not sufficiently stable.

---

# 52. Prediction-Gap Validation

Search for:

- external validation;
- calibration;
- discrimination;
- transportability;
- prospective evaluation;
- decision utility.

Do not mistake model derivation for validated prediction.

---

# 53. Diagnostic-Gap Validation

Check:

- index test;
- reference standard;
- accuracy;
- thresholds;
- spectrum;
- external validation;
- clinical utility.

---

# 54. Prognostic-Gap Validation

Check:

- factor/model;
- time horizon;
- calibration;
- discrimination;
- external validation;
- utility.

---

# 55. Generalizability-Gap Validation

Ask whether the target population/context differs enough to plausibly alter:

- effect;
- mechanism;
- prediction;
- measurement;
- implementation.

If not, "untested here" may be only a weak geographic extension.

---

# 56. Integration-Gap Validation

Check whether evidence streams are truly disconnected.

Examples:

- mechanism and clinical outcome;
- quantitative and qualitative evidence;
- molecular and population evidence.

A review or multimethod study may already provide integration.

---

# 57. Contradictory Evidence Review

Actively retrieve studies that:

- disagree with the candidate gap;
- report null results;
- show prior resolution;
- challenge the proposed boundary;
- use alternative methods.

Do not suppress inconvenient evidence.

---

# 58. Contradiction Matrix

Use:

| Study | Finding | Threat to Gap | Why It Matters | Resolution |
|---|---|---|---|---|

---

# 59. Supporting Evidence Comes Second

After adversarial searching, summarize evidence supporting the remaining gap.

Do not reverse the order.

---

# 60. Evidence-Synthesis Handoff

Use `evidence-synthesis` to integrate:

- competitors;
- supportive studies;
- contradictions;
- replication;
- methodological equivalents;
- contextual differences.

Validation should not rely on article-by-article impressions.

---

# 61. Source Verification Gate

Every critical threat or supporting source should pass `source-verification`.

A plausible citation is not enough.

---

# 62. Reference Integrity Gate

Use `reference-integrity-guard` to ensure:

- source identity is correct;
- DOI metadata are consistent;
- claim-to-source support is valid;
- no reference mashups occur;
- study families are understood.

---

# 63. Literature Screening Gate

Newly discovered evidence should pass purpose-specific `literature-screening`.

Do not include a paper merely because it mentions the topic.

---

# 64. Study-Family Guard

Preserve:

```text
multiple publications
≠
multiple independent studies
```

Study-family inflation can falsely weaken or strengthen a gap.

---

# 65. Review-Date Guard

An older review may no longer represent the current evidence frontier.

Check its search cutoff and update beyond it.

---

# 66. Systematic-Review Threat

A high-quality recent systematic review can be a major gap threat when it directly covers the proposed unresolved condition.

Do not stop at the review; inspect relevant primary evidence when needed.

---

# 67. Meta-Analysis Threat

A meta-analysis may substantially resolve:

- effect direction;
- magnitude;
- heterogeneity.

But it may leave mechanism, causality, generalizability, or implementation unresolved.

Reframe accordingly.

---

# 68. Evidence Hierarchy Guard

Use question-appropriate evidence.

Examples:

- RCTs for intervention efficacy;
- qualitative evidence for lived experience;
- mechanism studies for pathways;
- external-validation studies for prediction.

Do not apply one hierarchy universally.

---

# 69. Significance Guard

Do not validate a gap because prior studies were statistically non-significant.

Non-significance does not mean absence of evidence.

---

# 70. Citation-Count Guard

Do not validate or reject a gap based on citation count.

---

# 71. Prestige Guard

Do not privilege or dismiss evidence because of:

- journal prestige;
- author prestige;
- institution prestige;
- quartile.

---

# 72. Scopus Guard

Scopus status supports discoverability and source-status verification.

It does not prove the scientific claim.

---

# 73. APC Independence

APC status must not influence gap validation.

---

# 74. Target-Journal Independence

Journal scope, editor preference, or target-journal citation strategy must not determine whether a gap is scientifically real.

---

# 75. Publication Convenience Guard

Do not preserve a gap merely because it makes the study easier to publish.

---

# 76. Confirmation-Bias Audit

Ask:

> Which source is most dangerous to the gap?

Review that source carefully.

---

# 77. Gap-Falsification Questions

For every candidate ask:

- Has it already been studied?
- Has it been studied under another term?
- Has another method answered it?
- Has another population provided equivalent evidence?
- Has an adjacent discipline addressed it?
- Has recent work changed the state?
- Is the unresolved condition still scientifically important?

---

# 78. False-Absence Test

Strong absence language such as:

- "no studies";
- "never investigated";
- "first study";

requires broad evidence.

If not supported, downgrade or reframe.

---

# 79. "First Study" Boundary

Gap validation does not certify a priority claim.

Route explicit "first" claims to `novelty-auditor`.

---

# 80. Reframing Logic

Use:

```text
Original Gap
      ↓
Threat Evidence
      ↓
What Actually Remains Unresolved?
      ↓
Reframed Gap
```

Reframing is a scientific correction, not failure.

---

# 81. Reframed Gap Record

```yaml
reframed_gap:
  original:
  defeated_component:
  surviving_component:
  new_boundary:
  evidence_basis:
  scientific_consequence:
  validation_status:
```

---

# 82. Gap-Narrowing Guard

Do not repeatedly narrow a gap until something survives without documenting each change.

Version the claim.

---

# 83. Gap Versioning

Use:

```yaml
gap_version:
  version:
  statement:
  reason_for_change:
  threatening_evidence:
  status:
```

---

# 84. Strong Gap Criteria

A strong validated gap should be:

- current;
- scientifically meaningful;
- nontrivial;
- not substantially resolved;
- bounded;
- researchable;
- consequential;
- defensible against close competitors.

---

# 85. Moderate Gap Criteria

A moderate gap may be:

- narrower;
- context-bound;
- partially addressed;
- still useful for a focused study.

Do not inflate it.

---

# 86. Weak Gap Criteria

A weak gap often depends on:

- another location;
- another variable;
- another software package;
- a tiny subgroup;
- minor method variation;
- literature count rather than unresolved science.

---

# 87. Gap Rejection Criteria

Reject when:

- the unresolved claim is false;
- the literature already answers it;
- the boundary is scientifically meaningless;
- the proposed difference is cosmetic;
- the candidate is not researchable.

---

# 88. Gap Importance Reassessment

Threat evidence may reduce or increase scientific importance.

Example:

```text
broad association gap rejected
      ↓
mechanism contradiction discovered
      ↓
narrower but stronger mechanism gap
```

---

# 89. Gap Researchability Reassessment

After reframing, reassess whether the remaining gap can be answered.

Do not validate an interesting but currently unresearchable statement as a ready project gap.

---

# 90. Feasibility Boundary

Gap validity and project feasibility remain separate.

A valid gap may be infeasible for a specific researcher.

---

# 91. Gap Priority after Validation

Priority may consider:

- gap strength;
- scientific importance;
- researchability;
- feasibility;
- translational value;
- theory leverage;
- replication need.

Do not use publication attractiveness as priority.

---

# 92. Validation Matrix

Use:

| Test | Threat Found? | Effect on Gap | Required Action |
|---|---|---|---|

---

# 93. Final Judgment Matrix

Use:

| Candidate | Status | Surviving Gap | Confidence | Main Limitation |
|---|---|---|---|---|

---

# 94. Validation Confidence

Possible confidence:

- `HIGH`
- `MODERATE`
- `LOW`
- `INCONCLUSIVE`

Confidence should reflect search breadth, currentness, source verification, and competitor coverage.

---

# 95. Validation Confidence Record

```yaml
validation_confidence:
  search_currentness:
  terminology_coverage:
  competitor_coverage:
  adjacent_discipline_coverage:
  method_equivalence_coverage:
  source_verification:
  contradiction_coverage:
  overall:
```

---

# 96. Search Expansion Trigger

If validation remains uncertain because coverage is weak:

route to:

`scopus-literature-search`

---

# 97. Citation Expansion Trigger

If key anchors exist but the lineage is incomplete:

route to:

`citation-chaining`

---

# 98. Verification Trigger

If critical records are uncertain:

route to:

`source-verification`

---

# 99. Integrity Trigger

If metadata, duplication, study-family, or claim-support issues remain:

route to:

`reference-integrity-guard`

---

# 100. Screening Trigger

If newly discovered records have not been eligibility-screened:

route to:

`literature-screening`

---

# 101. Synthesis Trigger

If the validation evidence is complex or contradictory:

route to:

`evidence-synthesis`

---

# 102. SoTA Rebuild Trigger

If the validation process substantially changes the field classification:

route back to:

`sota-builder`

A rejected gap may require an updated SoTA.

---

# 103. Gap Discovery Re-entry

If validation reveals a different unresolved condition:

route back to:

`gap-discovery`

for explicit candidate-gap reconstruction before revalidation.

---

# 104. Novelty Builder Handoff

Only after the gap is validated, partially validated, or appropriately reframed should it route to:

`novelty-builder`

---

# 105. Novelty Auditor Handoff

After novelty construction:

route to:

`novelty-auditor`

Priority claims, "first" claims, and contribution claims must be stress-tested separately.

---

# 106. Research Question Handoff

After gap validation and novelty clarification:

route to:

`research-question-builder`

Do not formulate a final RQ from a rejected gap.

---

# 107. Hypothesis Handoff

Hypotheses remain downstream of the research question and, when required, the theory/mechanism framework.

Route to:

`hypothesis-builder`

only when confirmatory hypotheses are scientifically appropriate.

---

# 108. Theory Handoff

If the surviving gap is theoretical or mechanism-dependent:

route to:

`theoretical-framework`

when theory is required.

---

# 109. Conceptual Framework Handoff

If the surviving gap concerns construct organization or relationships:

route to:

`conceptual-framework`

---

# 110. Methodology Handoff

Methodology comes after the scientific question is clear.

Route to:

`methodology-architect`

Do not select a method merely to preserve a methodological gap.

---

# 111. Sampling Handoff

Population gaps may later inform:

`sampling-strategy`

after the RQ and design are established.

---

# 112. Instrument Handoff

Measurement gaps may later inform:

`instrument-design`

---

# 113. Analysis Handoff

Analytical needs may later route to:

`analysis-planner`

or:

`statistical-method-selector`

---

# 114. Continuation Research Handoff

For continuing previous research, validated gaps may route to:

`continuation-opportunity-finder`

---

# 115. Research Trajectory Handoff

For multi-study programs:

route to:

`research-trajectory-mapper`

A sequence of mechanism → validation → implementation gaps may form a roadmap.

---

# 116. Prior Research Audit Handoff

If the candidate comes from a prior thesis, dissertation, article, or project:

use `prior-research-auditor` when needed to clarify what the earlier study truly resolved.

---

# 117. Research Resume Handoff

Use `research-resume` when the user's current continuation stage is unclear.

---

# 118. Phenomenon Evidence Boundary

Real-world evidence from `phenomenon-evidence-builder` can establish:

- burden;
- magnitude;
- trend;
- policy;
- implementation shortfall.

It cannot by itself validate a scholarly research gap.

---

# 119. Dual Evidence Architecture

Preserve:

```text
Phenomenon Evidence
      ↓
Problem Importance

Scholarly Evidence
      ↓
Knowledge State

Adversarial Gap Validation
      ↓
Defensible Scientific Gap
```

---

# 120. Manuscript Positioning Handoff

Only validated or properly reframed gaps should support manuscript statements.

Route manuscript-level structure to:

`manuscript-architect`

and prose to:

`manuscript-writer`.

---

# 121. Manuscript Audit Handoff

`manuscript-auditor` should reject unsupported gap claims such as:

- "no studies";
- "first study";
- "little is known";

when validation evidence does not support them.

---

# 122. Journal Matcher Boundary

`journal-matcher` may use the validated scientific contribution for fit.

Journal selection must not change gap validity.

---

# 123. Reviewer Simulator Handoff

`reviewer-simulator` may attack the validated gap from a reviewer perspective.

This is additional stress testing, not a substitute for `gap-validator`.

---

# 124. Reviewer Response Handoff

If actual reviewers challenge the gap:

route to:

`reviewer-response`

Scientific reassessment comes before rebuttal wording.

---

# 125. Rejection-Recovery Logic

If a journal rejection argues the gap is weak:

```text
Reviewer / Editor Criticism
      ↓
Verify Criticism
      ↓
gap-validator
      ↓
Keep / Reframe / Reject
```

Do not defend the old gap automatically.

---

# 126. User-Provided Gap

When the user supplies a gap statement:

do not accept it at face value.

First classify it as:

`CANDIDATE_GAP`

unless validation evidence is already available.

---

# 127. User-Provided References

Uploaded references may support validation but should still pass:

- source verification;
- integrity review;
- purpose-specific screening.

Do not assume a user-provided citation is correct merely because it is supplied.

---

# 128. User-Provided Dataset

A dataset may demonstrate a phenomenon or enable a study.

It does not by itself establish a scholarly gap.

---

# 129. User-Provided Regulation

A regulation can establish policy context.

It does not prove an unresolved scientific question.

---

# 130. Systematic Review Mode

For candidate gaps derived from systematic reviews, check:

- review search date;
- inclusion criteria;
- later studies;
- unresolved heterogeneity;
- subgroup evidence;
- methodological limitations.

---

# 131. Meta-Analysis Mode

For gaps derived from meta-analysis, distinguish:

- unresolved effect;
- unexplained heterogeneity;
- missing subgroup evidence;
- mechanism;
- generalizability;
- publication bias concerns.

Do not call heterogeneity itself a gap without explanation.

---

# 132. Qualitative Gap Validation

For qualitative gaps search whether the allegedly missing perspective, experience, meaning, or implementation mechanism has already been explored under different terminology.

Do not force quantitative absence logic.

---

# 133. Mixed-Methods Gap Validation

For mixed-method opportunities validate whether integration is genuinely missing.

Existing multimethod or explanatory-sequential work may defeat the claimed integration gap.

---

# 134. Pharmacogenetic Gap Validation

Check:

- gene/SNP;
- treatment;
- outcome;
- ancestry;
- genetic model;
- genotyping method;
- replication;
- functional evidence;
- validation.

Do not validate a gap merely because the SNP has not been studied in one country.

---

# 135. Pharmacokinetic Gap Validation

Check:

- drug;
- dose;
- route;
- population;
- sampling;
- PK parameters;
- model;
- covariates;
- PK/PD relationship;
- external validation.

---

# 136. Pharmaceutical Formulation Gap Validation

Check whether the claimed contribution is more than:

- another polymer concentration;
- another extract combination;
- another preparation method.

Look for unresolved formulation mechanism, stability, reproducibility, scale-up, or biological-performance questions.

---

# 137. Education Gap Validation

Check:

- learner population;
- intervention;
- mechanism;
- learning outcome;
- context;
- longitudinal evidence;
- implementation.

---

# 138. Social-Science Gap Validation

Check:

- construct equivalence;
- theory lineage;
- context dependence;
- causal evidence;
- longitudinal evidence;
- measurement.

---

# 139. Engineering Gap Validation

Check:

- benchmark;
- robustness;
- scalability;
- real-world validation;
- operating conditions;
- degradation;
- safety.

---

# 140. Computational / AI Gap Validation

Check:

- external validation;
- benchmark comparability;
- data leakage;
- calibration;
- generalization;
- robustness;
- fairness;
- interpretability.

Using AI is not itself a gap.

---

# 141. Validation Error — Defending the Gap

Avoid searching only for literature that supports the gap.

Validation is adversarial.

---

# 142. Validation Error — Search Failure

Avoid:

> I did not find it, therefore the gap is validated.

Search failure is not proof.

---

# 143. Validation Error — Exact-Phrase Search

Avoid validating absence because exact wording is missing.

---

# 144. Validation Error — Database Narrowness

Do not rely on one database when the claim requires broader confidence.

---

# 145. Validation Error — Discipline Narrowness

Do not ignore adjacent disciplines.

---

# 146. Validation Error — Method Narrowness

Do not ignore equivalent methods.

---

# 147. Validation Error — Geography Bias

Do not preserve a gap simply because evidence comes from another country.

---

# 148. Validation Error — Variable Decoration

Do not preserve a gap because the exact variable combination is new.

---

# 149. Validation Error — Reviewer Appeasement

Do not change the scientific judgment merely to satisfy reviewer preference.

---

# 150. Validation Error — Prestige Bias

Do not let journal or author prestige determine the result.

---

# 151. Validation Error — Citation Padding

Do not add target-journal or famous references that are not scientifically relevant.

---

# 152. Validation Error — APC Pressure

APC and publication cost must remain separate from evidence.

---

# 153. Validation Error — Premature Novelty

Do not turn a partially validated gap into a strong novelty claim.

---

# 154. Validation Error — Premature RQ

Do not finalize a research question before the gap outcome is known when the question depends on that gap.

---

# 155. Validation Error — Premature Method

Do not choose methodology to rescue a weak gap.

---

# 156. Validation Error — HARKing

Do not redefine the gap after observing the user's study results merely to make those results appear novel.

---

# 157. Validation Error — False Consensus

Do not reject a gap merely because many papers agree if the unresolved mechanism or boundary still matters.

---

# 158. Validation Error — False Absence

Do not validate a gap from low publication volume alone.

---

# 159. Validation Error — False Generalization

Do not assume evidence transfers globally without checking scientifically meaningful boundaries.

---

# 160. Validation Error — Study-Family Inflation

Do not treat repeated publications from one study as multiple independent closures of the gap.

---

# 161. Validation Error — Review Substitution

Do not let a review citation replace primary evidence when priority or exact scope depends on primary studies.

---

# 162. Validation Error — Outdated Review

Do not treat an old review as current without checking literature after its search cutoff.

---

# 163. Validation Error — Unverified Source

Do not let an unverified citation defeat or support a critical gap.

---

# 164. Validation Error — Unsupported Reframing

Do not invent a better gap when the evidence does not support one.

A valid outcome may be `GAP_REJECTED`.

---

# 165. Full Validation Output

For a comprehensive task provide:

## A. Original Candidate Gap
[...]

## B. Normalized Gap
[...]

## C. Gap Type
[...]

## D. Search Currentness
[...]

## E. Terminology Expansion
[...]

## F. Closest Competitors
[...]

## G. Citation-Chaining Findings
[...]

## H. Adjacent-Discipline Findings
[...]

## I. Methodological Equivalents
[...]

## J. Contradictory Evidence
[...]

## K. Evidence Synthesis
[...]

## L. Gap Threats
[...]

## M. Surviving Uncertainty
[...]

## N. Final Gap Status
[...]

## O. Validated / Reframed Gap Statement
[...]

## P. Validation Confidence
[...]

## Q. Limitations
[...]

## R. Recommended Next Skill
[...]

---

# 166. Compact Validation Output

Use:

```text
Original gap:
Strongest threat:
Closest competitor:
What survives:
Final status:
Validated/reframed statement:
Confidence:
Next step:
```

---

# 167. Gap Validation Matrix

Recommended:

| Test | Evidence Found | Effect on Gap | Status |
|---|---|---|---|

---

# 168. Competitor Matrix

Recommended:

| Competitor | Overlap | Difference | Threat Level | Interpretation |
|---|---|---|---|---|

---

# 169. Terminology Matrix

Recommended:

| Core Term | Alternative Term | Relevant Evidence | Gap Effect |
|---|---|---|---|

---

# 170. Adjacent-Discipline Matrix

Recommended:

| Discipline | Equivalent Problem | Evidence | Gap Effect |
|---|---|---|---|

---

# 171. Method-Equivalence Matrix

Recommended:

| Proposed Method | Existing Equivalent | Same Scientific Question? | Gap Effect |
|---|---|---|---|

---

# 172. Contradiction Matrix

Recommended:

| Evidence Stream | Finding | Conflict | Surviving Question |
|---|---|---|---|

---

# 173. Validation Passport

Use:

```yaml
gap_validation:
  original_gap:
  normalized_gap:
  gap_type:
  evidence_cutoff:
  field_velocity:
  terminology_expanded:
  competitor_search_complete:
  citation_chaining_complete:
  adjacent_discipline_checked:
  method_equivalence_checked:
  contradictions_checked:
  critical_sources_verified:
  integrity_checked:
  surviving_uncertainty:
  final_status:
  final_gap_statement:
  confidence:
  limitations:
  next_stage:
```

Do not fabricate status fields.

---

# 174. Validation Readiness Status

Possible workflow statuses:

- `NOT_STARTED`
- `SEARCH_UPDATE_REQUIRED`
- `TERMINOLOGY_EXPANSION_REQUIRED`
- `COMPETITOR_SEARCH_REQUIRED`
- `CITATION_CHAINING_REQUIRED`
- `ADJACENT_DISCIPLINE_REVIEW_REQUIRED`
- `METHOD_EQUIVALENCE_REVIEW_REQUIRED`
- `SOURCE_VERIFICATION_REQUIRED`
- `REFERENCE_INTEGRITY_REQUIRED`
- `VALIDATION_IN_PROGRESS`
- `VALIDATION_COMPLETE`

---

# 175. Final Gap Wording

Validated gap wording should be precise and proportional.

Prefer:

> Existing evidence supports A, but independent external validation of B under C remains limited, leaving uncertainty regarding D.

Avoid:

> No one has ever studied B.

unless that extraordinary claim is actually validated.

---

# 176. Research Contribution Boundary

Gap validation identifies what remains unresolved.

It does not define the final contribution.

Route contribution design to `novelty-builder`.

---

# 177. Novelty Boundary

Even a strong validated gap may support only moderate novelty if the proposed study contributes little beyond prior work.

Therefore:

```text
VALIDATED GAP
≠
AUDITED NOVELTY
```

---

# 178. RQ Boundary

A validated gap may support several different research questions.

Route question construction to `research-question-builder`.

---

# 179. Theory Boundary

A validated mechanism or theoretical gap may require theory before hypotheses.

Use `theoretical-framework` when theory is necessary.

---

# 180. Hypothesis Boundary

Hypotheses are optional and design-dependent.

Use `hypothesis-builder` only when appropriate.

---

# 181. Method Boundary

Methodology must solve the research question.

It must not be chosen merely because a method appears novel.

---

# 182. Publication Boundary

Scientific validity must remain independent from:

- target journal;
- quartile;
- APC;
- impact factor;
- prestige;
- editor preferences.

---

# 183. User-Friendly Behavior

Prefer:

> The original gap does not survive in its broad form because two recent studies already address the association. A narrower gap remains: neither study provides external validation in the target clinical population. I would classify this as `REFRAMED_GAP`, not a completely new evidence gap.

Or:

> I found no verified study that directly tests the proposed mechanism, but several papers examine closely related pathways. The mechanism gap remains plausible, although the claim should be narrowed and validated with those equivalent terms included.

Or:

> The gap should be rejected. Existing evidence already answers the proposed question, and the remaining difference is only software choice.

---

# 184. Avoid These Behaviors

Do not:

- defend the user's preferred gap;
- manufacture novelty;
- rely on exact-term absence;
- rely on one database;
- ignore recent literature;
- ignore adjacent disciplines;
- ignore method equivalence;
- ignore contradictory evidence;
- count study-family publications as independent;
- let prestige determine evidence;
- let APC influence scientific judgment;
- add target-journal citations strategically;
- turn a rejected gap into an invented replacement;
- claim "first" without novelty auditing;
- finalize a research question from a rejected gap;
- choose methodology to rescue a weak gap.

---

# Stop Conditions

Do not finalize gap validation when:

- the candidate gap is not normalized;
- the evidence cutoff is inappropriate to field velocity;
- terminology expansion is incomplete where needed;
- closest competitors have not been checked;
- citation chaining is required but incomplete;
- adjacent disciplines may contain equivalent evidence;
- method equivalence remains unresolved;
- critical sources are unverified;
- study-family dependence materially affects interpretation;
- contradictory evidence has not been examined;
- the remaining gap cannot be clearly stated;
- the final status would depend primarily on publication prestige, citation count, target-journal strategy, or APC;
- strong priority language would be required without a separate novelty audit.

Use:

- `SEARCH_UPDATE_REQUIRED`
- `TERMINOLOGY_EXPANSION_REQUIRED`
- `COMPETITOR_SEARCH_REQUIRED`
- `CITATION_CHAINING_REQUIRED`
- `ADJACENT_DISCIPLINE_REVIEW_REQUIRED`
- `METHOD_EQUIVALENCE_REVIEW_REQUIRED`
- `SOURCE_VERIFICATION_REQUIRED`
- `REFERENCE_INTEGRITY_REQUIRED`
- `VALIDATION_INCONCLUSIVE`
- `NOT_READY_FOR_NOVELTY_DEVELOPMENT`

as appropriate.

---

# Success Criterion

`gap-validator` succeeds when a `CANDIDATE_GAP` is subjected to a deliberate falsification-oriented validation process that actively searches for current evidence, terminology variants, closest competitors, citation-lineage evidence, adjacent-discipline studies, methodological equivalents, population and context analogues, replication, validation, mechanisms, contradictions, and other evidence capable of closing or weakening the proposed gap; when critical sources are sufficiently verified and integrity-cleared, newly discovered evidence is purpose-screened, and complex evidence is synthesized rather than judged from isolated papers; when the original gap is preserved, narrowed, reframed, weakened, substantially resolved, rejected, or left inconclusive according to the evidence rather than researcher preference; when final statuses such as `VALIDATED_STRONG_GAP`, `VALIDATED_MODERATE_GAP`, `PARTIALLY_VALIDATED_GAP`, `REFRAMED_GAP`, `WEAK_GAP`, `GAP_SUBSTANTIALLY_RESOLVED`, `GAP_REJECTED`, and `VALIDATION_INCONCLUSIVE` are used proportionally; when literature scarcity, exact-phrase absence, geography alone, variable combinations, software differences, journal prestige, quartile, citation count, target-journal strategy, and APC status do not masquerade as scientific gap evidence; when false absence, study-family inflation, review-date staleness, disciplinary narrowness, method-label narrowness, confirmation bias, and premature novelty are actively guarded against; when the surviving unresolved condition is scientifically meaningful, bounded, current, researchable, and traceable to the evidence; when gap rejection is accepted as a scientifically valid outcome; and when only validated, partially validated, or appropriately reframed gaps are handed downstream to `novelty-builder`, `novelty-auditor`, `research-question-builder`, `hypothesis-builder` when appropriate, theory and conceptual framework skills, continuation and research-trajectory planning, methodology design, manuscript positioning, reviewer simulation, or reviewer response.
