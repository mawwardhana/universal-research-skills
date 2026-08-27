---
name: novelty-auditor
description: Stress-test proposed scientific novelty claims against the closest verified competitor studies, current State-of-the-Art evidence, alternative terminology, overlapping methods, mechanisms, populations, contexts, validation studies, citation networks, and recent literature. Use after novelty construction and before research-question finalization, methodology lock-in, grant submission, manuscript positioning, journal submission, or any strong claim that a study provides a novel scientific contribution.
---

# Novelty Auditor

## Purpose

`novelty-auditor` determines whether a proposed novelty claim remains defensible after deliberate attempts to weaken or invalidate it.

Its central question is:

> If we compare this proposed contribution with the strongest and closest existing research, does the claimed scientific advancement still remain meaningful?

The auditor should challenge:

- first-study claims;
- novelty boundaries;
- competitor comparisons;
- methodological novelty;
- contextual novelty;
- mechanistic novelty;
- validation novelty;
- translational novelty;
- claims of uniqueness.

The goal is not to protect the proposed study.

The goal is to prevent exaggerated or false novelty.

---

# Core Principle

Use:

> Novelty must survive comparison with the strongest competitor, not merely differ from the average paper.

A novelty claim should be reduced, reframed, or rejected when existing literature already contains substantially equivalent work.

A rejected novelty claim is a successful integrity outcome.

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
→ `gap-validator`
→ `novelty-builder`

Important inputs include:

- validated gap;
- gap boundary;
- proposed novelty;
- novelty type;
- novelty boundary;
- closest competitor studies;
- competitor comparison;
- current State of the Art;
- proposed study design;
- scientific contribution;
- novelty risk.

Do not audit novelty from the study title alone.

---

# Activation Conditions

Use when the researcher asks:

- "Is this novelty strong enough?"
- "Can I claim this as novel?"
- "Has anyone already done this?"
- "Audit my novelty."
- "Is my contribution actually new?"
- "Will reviewers consider this novel?"
- "Is this study too similar to previous research?"
- "Can I say this is the first study?"

Use especially before:

- research-question finalization;
- methodology finalization;
- grant submission;
- dissertation proposal defense;
- manuscript submission;
- cover-letter novelty claims.

---

# Novelty Audit Status

Input should normally be:

`PROPOSED_NOVELTY`

Possible final outcomes:

- `NOVELTY_STRONGLY_DEFENSIBLE`
- `NOVELTY_DEFENSIBLE`
- `NOVELTY_DEFENSIBLE_WITH_NARROWER_CLAIM`
- `NOVELTY_PARTIALLY_SUPPORTED`
- `NOVELTY_REQUIRES_REFRAMING`
- `NOVELTY_WEAK`
- `LIKELY_DUPLICATIVE`
- `NOVELTY_REJECTED`
- `NOVELTY_INCONCLUSIVE`

Do not force a positive conclusion.

---

# 1. Restate the Proposed Novelty

Represent the claim explicitly.

Recommended structure:

```yaml
novelty_claim:
  validated_gap:
  proposed_advancement:
  novelty_type:
  scientific_contribution:
  novelty_boundary:
  primary_novelty:
  secondary_contributions:
  closest_competitors:
  what_is_novel:
  what_is_not_novel:
  evidence_cutoff:
  current_status:
```

Unknown fields remain unknown.

Do not strengthen the claim during restatement.

---

# 2. Novelty Audit Principle

`novelty-auditor` is adversarial.

Its default question is:

> What existing evidence would make this novelty claim weaker, narrower, incremental, duplicative, or false?

The auditor must search for disconfirming evidence before defending the claim.

---

# 3. Preferred Audit Architecture

Use:

```text
PROPOSED_NOVELTY
      ↓
Normalize Claim
      ↓
Verify Gap Status
      ↓
Identify Closest Competitors
      ↓
Expand Terminology
      ↓
Search Current Literature
      ↓
Citation Chaining
      ↓
Adjacent-Discipline Search
      ↓
Method / Theory / Mechanism Equivalence
      ↓
Population / Context Equivalence
      ↓
Priority-Claim Test
      ↓
Scientific-Gain Test
      ↓
Duplication Test
      ↓
Evidence Synthesis
      ↓
Adversarial Judgment
      ↓
Defensible / Narrower / Partial / Reframe / Weak / Duplicative / Rejected / Inconclusive
```

---

# 4. Required Upstream Context

Prefer inputs from:

- `gap-validator`;
- `novelty-builder`;
- `sota-builder`;
- `evidence-synthesis`;
- `literature-screening`;
- `citation-chaining`;
- `source-verification`;
- `reference-integrity-guard`.

Do not audit novelty from a title, abstract sentence, or proposed variable list alone.

---

# 5. Verify Gap Status First

Before auditing novelty, confirm whether the underlying gap is:

- `VALIDATED_STRONG_GAP`;
- `VALIDATED_MODERATE_GAP`;
- `PARTIALLY_VALIDATED_GAP`;
- `REFRAMED_GAP`;
- `WEAK_GAP`;
- `GAP_SUBSTANTIALLY_RESOLVED`;
- `GAP_REJECTED`;
- `VALIDATION_INCONCLUSIVE`.

Strong novelty should not be built on a rejected gap.

---

# 6. Gap Re-entry Rule

If novelty auditing reveals evidence that undermines the validated gap:

route back to:

`gap-validator`

Do not preserve the novelty claim by ignoring gap-threatening evidence.

---

# 7. Audit Status Vocabulary

Possible final outcomes:

- `NOVELTY_STRONGLY_DEFENSIBLE`
- `NOVELTY_DEFENSIBLE`
- `NOVELTY_DEFENSIBLE_WITH_NARROWER_CLAIM`
- `NOVELTY_PARTIALLY_SUPPORTED`
- `NOVELTY_REQUIRES_REFRAMING`
- `NOVELTY_WEAK`
- `LIKELY_DUPLICATIVE`
- `NOVELTY_REJECTED`
- `NOVELTY_INCONCLUSIVE`

Do not force a positive outcome.

---

# 8. Strongly Defensible Novelty

Use `NOVELTY_STRONGLY_DEFENSIBLE` only when:

- the gap remains validated;
- the closest competitors do not substantially duplicate the proposed contribution;
- the scientific gain is explicit and meaningful;
- terminology variants do not reveal hidden overlap;
- adjacent disciplines do not already contain equivalent work;
- method equivalence does not erase the contribution;
- priority claims are proportionate;
- evidence is sufficiently current.

---

# 9. Defensible Novelty

Use `NOVELTY_DEFENSIBLE` when the contribution remains meaningful but is not necessarily field-changing.

This status is appropriate for:

- solid validation;
- meaningful replication;
- mechanistic clarification;
- improved generalizability;
- contextual extension with scientific justification.

---

# 10. Defensible with Narrower Claim

Use `NOVELTY_DEFENSIBLE_WITH_NARROWER_CLAIM` when the broad claim is too strong but a more precise contribution survives.

Example:

```text
Broad claim:
First study of X and Y.

Audit finding:
X and Y have been studied, but not externally validated under condition Z.

Narrower claim:
External validation of X–Y under condition Z.
```

Do not retain the original priority wording.

---

# 11. Partially Supported Novelty

Use `NOVELTY_PARTIALLY_SUPPORTED` when some claimed elements are novel and others are not.

Separate them explicitly.

---

# 12. Novelty Requires Reframing

Use `NOVELTY_REQUIRES_REFRAMING` when:

- the claimed novelty type is wrong;
- discovery novelty is actually validation novelty;
- geographic novelty is actually generalizability novelty;
- method novelty is actually measurement novelty;
- mechanism novelty is only association novelty.

---

# 13. Weak Novelty

Use `NOVELTY_WEAK` when:

- the difference is scientifically small;
- competitors already cover most of the contribution;
- the remaining advancement is incremental and low-impact;
- the claim depends on superficial differences.

---

# 14. Likely Duplicative

Use `LIKELY_DUPLICATIVE` when the proposed study substantially reproduces an existing study without a meaningful new scientific contribution.

Replication may still be valuable, but it should be described as replication rather than novel discovery.

---

# 15. Novelty Rejected

Use `NOVELTY_REJECTED` when the claimed advancement is not supported because:

- equivalent prior work exists;
- the supposed difference is cosmetic;
- the gap is resolved;
- the claimed mechanism/method/contribution already exists.

---

# 16. Novelty Inconclusive

Use `NOVELTY_INCONCLUSIVE` when:

- current literature coverage is insufficient;
- critical full texts are unavailable;
- competitor identity is uncertain;
- terminology is unresolved;
- evidence is moving too quickly;
- source verification is incomplete.

---

# 17. Normalize the Claim

Break novelty into:

```text
What prior work already established
What the proposal claims to add
What exact difference exists
Why that difference matters
What evidence could defeat the claim
```

Do not allow rhetorical phrases such as "innovative" or "unique" to substitute for scientific content.

---

# 18. Novelty Claim Versioning

Use:

```yaml
novelty_version:
  version:
  claim:
  reason_for_change:
  threatening_evidence:
  surviving_component:
  status:
```

Record every major narrowing or reframing.

---

# 19. Closest-Competitor Search

Identify the studies with maximum scientific overlap across:

- research question;
- theory;
- mechanism;
- population;
- context;
- design;
- exposure/intervention;
- outcome;
- measurement;
- analytical strategy;
- validation stage;
- translational stage.

---

# 20. Competitor Record

Use:

```yaml
competitor:
  reference:
  question_overlap:
  theory_overlap:
  mechanism_overlap:
  population_overlap:
  method_overlap:
  measurement_overlap:
  outcome_overlap:
  validation_overlap:
  context_overlap:
  contribution_overlap:
  novelty_threat:
```

---

# 21. Competitor Threat Levels

Use:

- `CRITICAL_THREAT`
- `MAJOR_THREAT`
- `MODERATE_THREAT`
- `MINOR_THREAT`
- `NOT_A_THREAT`

Threat level reflects scientific overlap, not prestige.

---

# 22. Closest-Competitor Matrix

Use:

| Competitor | Scientific Overlap | Existing Contribution | Remaining Difference | Threat Level |
|---|---|---|---|---|

---

# 23. Terminology Expansion

Search:

- synonyms;
- historical terms;
- abbreviations;
- alternative spellings;
- neighboring constructs;
- translated terms;
- technical aliases;
- old method names.

Priority claims can fail because the same work exists under different terminology.

---

# 24. Terminology Record

Use:

```yaml
novelty_terminology:
  core_term:
  synonyms:
  historical_terms:
  abbreviations:
  adjacent_constructs:
  method_aliases:
  theory_aliases:
  discipline_specific_terms:
```

---

# 25. Exact-Phrase Bias Guard

Do not claim novelty because the exact phrase is absent.

Scientific equivalence matters more than wording.

---

# 26. Construct Equivalence Test

Ask whether a differently named construct is:

- identical;
- overlapping;
- nested;
- functionally equivalent;
- merely related.

Route complex construct questions to:

`conceptual-framework`

---

# 27. Theory Equivalence Test

Ask whether the claimed theoretical contribution already exists under:

- another theory;
- a refinement;
- an adjacent explanatory model;
- a different disciplinary tradition.

Route formal theory comparison to:

`theoretical-framework`

---

# 28. Mechanism Equivalence Test

Ask whether the claimed new mechanism has already been tested through:

- another mediator;
- another pathway label;
- biological analogues;
- equivalent process measures;
- direct experiments.

---

# 29. Method Equivalence Test

Ask:

> Has another method already produced the same scientific inference?

A method label alone does not establish novelty.

---

# 30. Software Independence

Preserve:

```text
SmartPLS
AMOS
SPSS
Jamovi
R
Python
Stata
SAS
```

are tools.

Changing software does not create scientific novelty.

---

# 31. Search Currentness

Novelty is highly time-sensitive.

Use current scholarly search appropriate to field velocity.

Prefer:

`scopus-literature-search`

for Scopus-first discovery when available.

Do not claim direct Scopus verification unless it actually occurred.

---

# 32. Field Velocity

Classify:

- `FAST_MOVING`
- `MODERATE`
- `SLOW_MOVING`
- `UNKNOWN`

Use field velocity to determine how aggressively current evidence must be updated.

---

# 33. Search Freshness Record

Use:

```yaml
novelty_search:
  field_velocity:
  prior_cutoff:
  current_search_date:
  newest_relevant_record:
  currentness_status:
```

---

# 34. Fast-Moving Field Rule

In fast-moving fields:

- inspect recent primary studies;
- forward-chain recent anchors;
- check online-first publications;
- verify newest competitor studies;
- do not rely on old reviews alone.

---

# 35. Slow-Moving Field Rule

In slower fields:

- seminal work may remain decisive;
- older theory may still defeat novelty;
- recency should not replace scientific relevance.

---

# 36. Citation Chaining

Use `citation-chaining` to find:

- precursor work;
- follow-up work;
- replications;
- extensions;
- contradictions;
- prior priority.

Backward and forward chaining are central to novelty auditing.

---

# 37. Anchor Strategy

Useful anchors include:

- closest competitor;
- seminal study;
- recent high-overlap study;
- major systematic review;
- method-development study.

Do not choose anchors by citation count alone.

---

# 38. Adjacent-Discipline Search

Search neighboring fields when equivalent scientific work may exist.

Examples:

- pharmacy ↔ pharmacology;
- education ↔ psychology;
- management ↔ consumer behavior;
- engineering ↔ materials science;
- public health ↔ epidemiology.

---

# 39. Adjacent-Discipline Guard

Do not preserve novelty by excluding relevant adjacent disciplines.

---

# 40. Population Equivalence Test

For population novelty ask whether the target population differs meaningfully in:

- biology;
- ancestry;
- age;
- exposure;
- risk;
- treatment response;
- education context;
- social environment.

If not, the novelty may be weak.

---

# 41. Geography Equivalence Test

Country-specific novelty requires scientifically meaningful differences.

Assess:

- population structure;
- genetics;
- healthcare system;
- policy;
- environment;
- culture;
- market;
- implementation.

---

# 42. Context Equivalence Test

Context novelty is defensible only when context plausibly changes the phenomenon, mechanism, or implementation.

---

# 43. Validation Novelty Test

Check whether the work truly adds a new validation layer:

- external;
- temporal;
- geographic;
- prospective;
- clinical;
- cross-cultural.

If prior work already provides equivalent validation, the claim weakens.

---

# 44. Replication Novelty Test

Replication may be meaningful when:

- original evidence is fragile;
- independent replication is missing;
- context plausibly matters;
- clinical importance is high.

Do not disguise replication as discovery.

---

# 45. Mechanistic Novelty Test

Mechanistic novelty should involve direct evidence about how or why an effect occurs.

Association plus mediation statistics may be insufficient.

---

# 46. Causal Novelty Test

If causal novelty is claimed, inspect whether prior studies already use:

- randomized designs;
- quasi-experimental designs;
- longitudinal causal models;
- natural experiments;
- target-trial emulation;
- other credible causal strategies.

---

# 47. Methodological Novelty Test

Ask whether the method changes:

- validity;
- inference;
- resolution;
- reproducibility;
- causal identification;
- measurement quality.

If not, methodological novelty is weak.

---

# 48. Measurement Novelty Test

Check whether the proposed instrument, assay, biomarker, or measurement approach is truly new or meaningfully improved.

Require validation evidence where appropriate.

---

# 49. Analytical Novelty Test

Analytical novelty is defensible when it yields scientifically meaningful new inference.

Using a complex model is insufficient.

---

# 50. Prediction Novelty Test

Check:

- external validation;
- calibration;
- discrimination;
- transportability;
- prospective evaluation;
- decision utility.

A small improvement in derivation AUC alone may be weak.

---

# 51. Diagnostic Novelty Test

Assess whether the contribution improves:

- accuracy;
- thresholds;
- reference-standard comparison;
- external validation;
- clinical utility.

---

# 52. Prognostic Novelty Test

Assess whether the contribution improves:

- prognostic factor evidence;
- model calibration;
- time horizon;
- external validation;
- utility.

---

# 53. Intervention Novelty Test

Assess whether the intervention differs meaningfully in:

- mechanism;
- efficacy;
- safety;
- delivery;
- comparative effectiveness.

Minor delivery changes may be incremental.

---

# 54. Implementation Novelty Test

Implementation novelty may concern:

- adoption;
- fidelity;
- scalability;
- sustainability;
- implementation mechanisms;
- real-world delivery.

---

# 55. Translational Novelty Test

Check whether the study genuinely advances:

```text
Mechanism
   ↓
Preclinical
   ↓
Human
   ↓
Clinical
   ↓
Implementation
```

Do not claim translational novelty when prerequisites are absent.

---

# 56. Integrative Novelty Test

Ask whether the study connects previously disconnected evidence streams in a way that changes understanding.

Examples:

- molecular + clinical;
- quantitative + qualitative;
- theory + mechanism;
- lab + real world.

---

# 57. Technological Novelty Test

Technology is scientifically novel only when it enables meaningful new evidence or inference.

New hardware/software alone is insufficient.

---

# 58. Superficial Novelty Test

Check whether the only difference is:

- country;
- institution;
- sample;
- year;
- one extra variable;
- one concentration;
- one questionnaire;
- one software package;
- a newer algorithm.

If yes, novelty is probably weak unless the difference changes inference.

---

# 59. Variable-Combination Guard

Preserve:

```text
new combination of X + Y + Z
≠
meaningful novelty by default
```

The combination must clarify an unresolved scientific mechanism, boundary, prediction, or integration problem.

---

# 60. Mediator Guard

A mediator supports novelty only when:

- the pathway is scientifically plausible;
- evidence supports its role;
- it addresses the validated gap.

---

# 61. Moderator Guard

A moderator supports novelty only when:

- boundary conditions remain unresolved;
- effect modification is plausible;
- it helps explain contradiction or heterogeneity.

---

# 62. Complexity Guard

Do not reward complexity.

More variables, pathways, interactions, or model layers do not automatically improve novelty.

---

# 63. Sample-Size Guard

Larger sample size improves precision.

It is not itself novelty.

---

# 64. Statistical-Significance Guard

Novelty is not defined by:

- p < 0.05;
- smaller p-values;
- more significant paths;
- more significant predictors.

---

# 65. AI Guard

Using AI is not itself novel.

Meaningful AI novelty may involve:

- external validation;
- robust generalization;
- calibration;
- interpretability;
- scientifically useful measurement;
- decision utility.

---

# 66. New Dataset Guard

A new dataset may create novelty only when it enables:

- new population inference;
- external validation;
- rare-outcome analysis;
- temporal insight;
- new mechanism testing;
- improved generalizability.

---

# 67. New Biomarker Guard

A new biomarker must be:

- biologically plausible;
- analytically valid;
- clinically/scientifically meaningful;
- not already adequately evaluated.

---

# 68. New Formulation Guard

A new formulation may be novel if it advances:

- stability;
- release;
- efficacy;
- safety;
- mechanism;
- manufacturability;
- scale-up;
- reproducibility.

A new ingredient combination alone may be weak.

---

# 69. Qualitative Novelty Guard

Qualitative novelty may involve:

- missing stakeholder perspective;
- new explanatory mechanism;
- implementation barrier;
- cultural meaning;
- conceptual refinement.

A new interview location alone is weak.

---

# 70. Mixed-Methods Novelty Guard

Mixed methods are novel only when integration produces knowledge not obtainable from one strand alone.

---

# 71. Interdisciplinary Novelty Guard

Combining disciplines is not inherently novel.

The integration must advance understanding.

---

# 72. State-of-the-Art Comparison

Use `sota-builder` to verify:

- what is established;
- what is emerging;
- what is contested;
- what is unresolved;
- where the frontier lies.

Novelty should advance beyond the current frontier.

---

# 73. Gap-to-Novelty Consistency

Check:

```text
Validated Gap
      ↓
Proposed Novelty
```

The proposed contribution must actually address the surviving gap.

Do not build novelty on a different unstated problem.

---

# 74. Scientific-Gain Test

Ask:

> If this study succeeds, what scientific understanding changes?

If no meaningful answer exists, novelty is weak.

---

# 75. Negative-Result Test

Ask:

> If the expected effect is not found, does the study still meaningfully advance knowledge?

Strong scientific novelty often survives null or contradictory outcomes.

---

# 76. Falsifiability Test

A novelty claim should be capable of being disproven.

Avoid claims that remain "novel" regardless of outcome.

---

# 77. Duplication Test

Ask:

> Could an existing study be described almost identically after removing superficial differences?

If yes, classify the contribution as likely duplicative unless a meaningful scientific boundary remains.

---

# 78. Replication vs Duplication

Preserve:

```text
Replication
can be scientifically valuable

Duplication
adds little without justification
```

If replication is the true contribution, label it transparently.

---

# 79. Priority-Claim Test

Claims such as:

- "first";
- "first-ever";
- "never studied";
- "unprecedented";
- "unique";

require the strongest evidence.

Do not certify priority from absence in a limited search.

---

# 80. First-Study Claim Standard

Before allowing a "first" claim, check:

- synonyms;
- adjacent disciplines;
- equivalent methods;
- historical terminology;
- recent literature;
- citation chains;
- conference/preprint context when scientifically relevant.

If uncertainty remains, avoid the claim.

---

# 81. Safer Priority Language

Prefer:

> To our knowledge, within the defined search scope and evidence cutoff...

only when the search is sufficiently documented.

Even this wording should be used sparingly.

---

# 82. Priority-Claim Rejection

If evidence is insufficient for "first", keep the scientific novelty but remove the priority claim.

---

# 83. Novelty Threat Record

Use:

```yaml
novelty_threat:
  claim_component:
  source:
  threat_type:
  overlap:
  scientific_effect:
  severity:
  resolution:
```

---

# 84. Threat Types

Possible:

- `PRIOR_ART`
- `TERMINOLOGY_EQUIVALENCE`
- `METHOD_EQUIVALENCE`
- `THEORY_EQUIVALENCE`
- `MECHANISM_EQUIVALENCE`
- `POPULATION_EQUIVALENCE`
- `CONTEXT_EQUIVALENCE`
- `RECENT_COMPETITOR`
- `ADJACENT_DISCIPLINE`
- `GAP_INVALIDATION`
- `DUPLICATION`
- `INCREMENTALISM`

---

# 85. Threat Matrix

Use:

| Threat | Evidence | Severity | Effect on Claim | Required Action |
|---|---|---|---|---|

---

# 86. Source Verification Gate

Critical competitor evidence must pass:

`source-verification`

Do not let an unverified citation defeat or support novelty.

---

# 87. Reference Integrity Gate

Use:

`reference-integrity-guard`

to verify:

- source identity;
- DOI metadata;
- claim support;
- duplicates;
- study-family relationships;
- retractions.

---

# 88. Literature Screening Gate

New competitor evidence should pass:

`literature-screening`

Do not use merely topically related papers as novelty threats.

---

# 89. Evidence Synthesis Gate

Use:

`evidence-synthesis`

when novelty depends on a body of evidence rather than one competitor.

---

# 90. Citation Chaining Gate

Use:

`citation-chaining`

to verify priority lineage and scientific evolution.

---

# 91. Search Update Gate

If the evidence cutoff is stale:

route to:

`scopus-literature-search`

then re-audit.

---

# 92. SoTA Update Gate

If new evidence changes the scientific frontier:

route back to:

`sota-builder`

---

# 93. Gap Revalidation Gate

If new evidence undermines the gap:

route back to:

`gap-validator`

---

# 94. Novelty Builder Re-entry

If the claim must be reconstructed substantially:

route back to:

`novelty-builder`

before re-auditing.

---

# 95. Audit Evidence Order

Preferred order:

```text
1. strongest threats
2. closest competitors
3. equivalent terminology/methods
4. adjacent evidence
5. supportive novelty evidence
```

This reduces confirmation bias.

---

# 96. Confirmation-Bias Check

Ask:

> Which source is most dangerous to this novelty claim?

Read that source carefully.

---

# 97. Publication-Bias Awareness

Do not assume the published literature represents all attempted work.

This limitation should reduce confidence in absolute priority claims.

---

# 98. Citation-Bias Awareness

Highly cited work may dominate perception.

Citation count does not define novelty.

---

# 99. Prestige Independence

Do not privilege:

- high-impact journals;
- famous authors;
- famous institutions.

Scientific overlap and evidence quality matter.

---

# 100. Scopus Independence

Scopus indexing supports discoverability and source-status checking.

It does not prove scientific novelty.

---

# 101. Quartile Independence

Quartile does not determine whether a contribution is novel.

---

# 102. APC Independence

APC preferences must not influence novelty auditing.

---

# 103. Target-Journal Independence

Do not reshape novelty to fit a journal.

Journal matching comes later.

---

# 104. Citation-Padding Guard

Do not add target-journal citations merely to make novelty appear aligned with a journal.

---

# 105. Reviewer-Pleasing Guard

Do not preserve or exaggerate novelty merely because reviewers might prefer a stronger claim.

---

# 106. HARKing Guard

Do not redefine novelty after observing study results merely to make those results look unique.

---

# 107. Post-Hoc Novelty

If novelty was identified only after results:

label it as post-hoc positioning when appropriate.

Do not rewrite the pre-study scientific rationale dishonestly.

---

# 108. Research-Question Consistency

The novelty claim must match the planned research question.

If novelty changes materially:

revisit:

`research-question-builder`

---

# 109. Theory Consistency

If novelty depends on theoretical advancement:

route to:

`theoretical-framework`

The theory must be scientifically warranted.

---

# 110. Hypothesis Consistency

Hypotheses must not be invented merely to make novelty appear stronger.

Use:

`hypothesis-builder`

only when confirmatory hypotheses are appropriate.

---

# 111. Conceptual Consistency

If novelty depends on construct relationships:

route to:

`conceptual-framework`

---

# 112. Methodology Consistency

Methodology must be capable of testing the proposed advancement.

Route to:

`methodology-architect`

after the RQ is clear.

---

# 113. Sampling Consistency

If population novelty is claimed, verify that `sampling-strategy` can validly represent the intended population.

---

# 114. Instrument Consistency

Measurement novelty requires appropriate `instrument-design` or validated measurement.

---

# 115. Analysis Consistency

Analytical novelty or inferential claims may require:

- `analysis-planner`;
- `statistical-method-selector`.

Do not claim analytical advancement that the planned analysis cannot support.

---

# 116. Result Interpretation Boundary

After study completion:

`result-interpreter`

must determine whether the anticipated novelty was actually realized.

Planned novelty is not guaranteed novelty.

---

# 117. Scientific Discussion Boundary

`scientific-discussion` should compare actual findings with the competitor evidence used in the novelty audit.

---

# 118. Implication Boundary

Use `implication-builder` only after the contribution is supported by results.

Do not infer practical impact from planned novelty alone.

---

# 119. Previous Research Audit

For continuation studies:

use `prior-research-auditor` to determine:

- original contribution;
- what has become established;
- what has been superseded;
- what remains open.

---

# 120. Research Resume

Use `research-resume` when the user's continuation stage is unclear.

---

# 121. Continuation Opportunity

Use `continuation-opportunity-finder` to identify next studies after novelty is defensible.

---

# 122. Research Trajectory

Use `research-trajectory-mapper` for multi-study novelty progression.

Example:

```text
Study 1: mechanism
Study 2: external validation
Study 3: implementation
```

---

# 123. Phenomenon Evidence Boundary

`phenomenon-evidence-builder` can show why a problem matters.

Phenomenon magnitude does not prove novelty.

---

# 124. Dual Evidence Architecture

Preserve:

```text
Phenomenon Evidence
      ↓
Problem Significance

Scholarly Evidence
      ↓
Knowledge State

Validated Gap
      ↓
Unresolved Science

Novelty Audit
      ↓
Defensible Contribution
```

---

# 125. Manuscript Architecture Handoff

After the novelty claim survives auditing:

route positioning to:

`manuscript-architect`

---

# 126. Manuscript Writing Handoff

Use:

`manuscript-writer`

for calibrated novelty language.

Do not use exaggerated adjectives.

---

# 127. Manuscript Audit Handoff

`manuscript-auditor` should check that novelty claims remain consistent with:

- evidence;
- actual methods;
- actual results;
- closest competitors;
- validated gap.

---

# 128. Journal Matching Handoff

Only after the scientific contribution is stable should it inform:

`journal-matcher`

Journal fit is downstream of science.

---

# 129. Reviewer Simulation Handoff

Use:

`reviewer-simulator`

to challenge the manuscript-specific novelty presentation.

This does not replace novelty auditing.

---

# 130. Reviewer Response Handoff

If actual reviewers challenge novelty:

route to:

`reviewer-response`

Reassess the scientific claim before drafting rebuttal language.

---

# 131. Grant Proposal Use

Before grant submission, novelty auditing should check:

- gap validity;
- competitor coverage;
- priority claims;
- contribution magnitude;
- feasibility;
- alignment between aims and novelty.

---

# 132. Dissertation Use

Before proposal defense, ensure:

- novelty is not only geography;
- contribution can support doctoral-level progression;
- theory/mechanism/validation logic is clear;
- closest competitors are identified.

---

# 133. Manuscript Use

For manuscripts, novelty should be proportional to the actual completed study.

Do not retain proposal-stage claims that results did not support.

---

# 134. Systematic Review Novelty Audit

For reviews, test whether novelty is truly:

- updated evidence;
- new question;
- unresolved contradiction;
- methodological improvement;
- important synthesis gap.

A newer search date alone is usually weak.

---

# 135. Meta-Analysis Novelty Audit

Check whether the contribution is more than:

- another software package;
- another forest plot;
- another pooling method.

Meaningful novelty may involve new evidence, subgroup resolution, heterogeneity explanation, or improved methodology.

---

# 136. Qualitative Novelty Audit

Test whether the claimed novelty reflects:

- missing perspective;
- explanatory mechanism;
- contextual meaning;
- conceptual refinement.

Do not force first-study logic.

---

# 137. Mixed-Methods Novelty Audit

Test whether integration itself produces new understanding.

If strands merely coexist, mixed-method novelty may be weak.

---

# 138. Pharmacogenetic Novelty Audit

Check:

- gene/SNP;
- drug;
- outcome;
- ancestry;
- genotype model;
- replication;
- functional evidence;
- validation;
- predictive utility.

Country-only claims are weak unless scientifically justified.

---

# 139. Pharmacokinetic Novelty Audit

Check:

- drug;
- dose;
- route;
- population;
- PK parameters;
- covariates;
- model;
- validation;
- exposure–response;
- PK/PD linkage.

---

# 140. Pharmaceutical Formulation Novelty Audit

Check whether contribution exceeds:

- another polymer concentration;
- another botanical combination;
- another preparation method.

Look for meaningful stability, release, mechanism, activity, reproducibility, scale-up, or translation.

---

# 141. Education Novelty Audit

Check:

- learner group;
- mechanism;
- intervention;
- outcome;
- longitudinal transfer;
- implementation;
- measurement.

---

# 142. Social-Science Novelty Audit

Check:

- construct equivalence;
- theory lineage;
- context;
- causal inference;
- longitudinal evidence;
- measurement.

---

# 143. Engineering Novelty Audit

Check:

- benchmark;
- robustness;
- scalability;
- real-world validation;
- safety;
- degradation;
- operating conditions.

---

# 144. Computational / AI Novelty Audit

Check:

- external validation;
- calibration;
- benchmark fairness;
- data leakage;
- robustness;
- generalization;
- interpretability;
- scientific utility.

---

# 145. Novelty Audit Matrix

Use:

| Audit Dimension | Evidence | Threat | Effect on Novelty | Status |
|---|---|---|---|---|

---

# 146. Competitor Audit Matrix

Use:

| Competitor | Overlap | Existing Contribution | Remaining Difference | Threat |
|---|---|---|---|---|

---

# 147. Claim Audit Matrix

Use:

| Claim Component | Novel? | Evidence | Threat | Final Wording |
|---|---|---|---|---|

---

# 148. What-Is-Novel / What-Is-Not-Novel Audit

Explicitly report:

```text
WHAT IS NOVEL
[...]

WHAT IS NOT NOVEL
[...]
```

This distinction must survive the audit.

---

# 149. Final Claim Wording

A defensible novelty statement should be specific.

Prefer:

> The contribution lies in externally validating X under Y and testing mechanism Z, rather than in the geographic setting alone.

Avoid:

> This is a completely novel study.

---

# 150. Final Claim Calibration

Match wording to status.

For `NOVELTY_STRONGLY_DEFENSIBLE`:

> The study provides a distinct scientific advancement by...

For `NOVELTY_DEFENSIBLE`:

> The study extends existing knowledge by...

For narrower claims:

> The defensible contribution is specifically...

For weak novelty:

> The study is primarily incremental and should not be positioned as a major novel advance.

---

# 151. Audit Confidence

Use:

- `HIGH`
- `MODERATE`
- `LOW`
- `INCONCLUSIVE`

Confidence should reflect:

- currentness;
- competitor coverage;
- terminology coverage;
- adjacent-discipline coverage;
- source verification;
- citation chaining;
- evidence synthesis.

---

# 152. Audit Confidence Record

Use:

```yaml
novelty_audit_confidence:
  search_currentness:
  competitor_coverage:
  terminology_coverage:
  citation_chain_coverage:
  adjacent_discipline_coverage:
  method_equivalence_coverage:
  source_verification:
  integrity_check:
  overall:
```

---

# 153. Novelty Audit Passport

Use:

```yaml
novelty_audit:
  proposed_novelty:
  validated_gap:
  gap_status:
  evidence_cutoff:
  field_velocity:
  closest_competitors:
  terminology_expanded:
  citation_chaining_complete:
  adjacent_disciplines_checked:
  method_equivalence_checked:
  theory_equivalence_checked:
  mechanism_equivalence_checked:
  population_context_checked:
  priority_claim_checked:
  duplication_checked:
  scientific_gain_checked:
  what_is_novel:
  what_is_not_novel:
  final_status:
  final_novelty_statement:
  confidence:
  limitations:
  next_stage:
```

---

# 154. Audit Readiness Status

Possible workflow statuses:

- `NOT_STARTED`
- `GAP_REVALIDATION_REQUIRED`
- `SEARCH_UPDATE_REQUIRED`
- `COMPETITOR_SEARCH_REQUIRED`
- `TERMINOLOGY_EXPANSION_REQUIRED`
- `CITATION_CHAINING_REQUIRED`
- `ADJACENT_DISCIPLINE_REVIEW_REQUIRED`
- `METHOD_EQUIVALENCE_REVIEW_REQUIRED`
- `SOURCE_VERIFICATION_REQUIRED`
- `REFERENCE_INTEGRITY_REQUIRED`
- `NOVELTY_AUDIT_IN_PROGRESS`
- `NOVELTY_AUDIT_COMPLETE`

---

# 155. Full Audit Output

For a comprehensive task provide:

## A. Proposed Novelty
[...]

## B. Underlying Validated Gap
[...]

## C. Current SoTA Position
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

## I. Method / Theory / Mechanism Equivalence
[...]

## J. Population / Context Equivalence
[...]

## K. Priority-Claim Test
[...]

## L. Duplication Test
[...]

## M. Scientific-Gain Test
[...]

## N. What Is Novel
[...]

## O. What Is Not Novel
[...]

## P. Final Status
[...]

## Q. Final Novelty Statement
[...]

## R. Confidence
[...]

## S. Limitations
[...]

## T. Recommended Next Skill
[...]

---

# 156. Compact Audit Output

Use:

```text
Proposed novelty:
Closest competitor:
Strongest threat:
What remains novel:
What is NOT novel:
Final status:
Final wording:
Confidence:
Next step:
```

---

# 157. User-Friendly Behavior

Prefer:

> The broad "first study" claim does not survive. Two earlier studies already examine the same relationship. What remains defensible is external validation in a clinically distinct population plus direct testing of the proposed mechanism.

Or:

> The use of SmartPLS is not novel. The defensible contribution lies in testing an unresolved boundary condition that prior studies did not address.

Or:

> The novelty is mainly validation rather than discovery. Positioning it accurately will make the study more defensible, not weaker.

Or:

> The proposed novelty should be rejected because the closest existing study already performs the same scientific test. A different study question would be needed.

---

# 158. Avoid These Behaviors

Do not:

- defend the user's preferred novelty;
- manufacture a positive audit outcome;
- rely on exact-term absence;
- rely on one database only;
- ignore recent literature;
- ignore adjacent disciplines;
- ignore equivalent methods;
- ignore equivalent theories or mechanisms;
- hide closest competitors;
- count software choice as novelty;
- count geography alone as novelty;
- count extra variables as novelty;
- count larger sample size alone as novelty;
- count statistical significance as novelty;
- overstate validation as discovery;
- use journal prestige as scientific evidence;
- use Scopus status as novelty evidence;
- let APC influence scientific judgment;
- pad citations for target-journal strategy;
- claim "first" without sufficient audit;
- choose methodology to rescue weak novelty;
- create hypotheses merely to enhance novelty;
- rewrite pre-study novelty post-hoc to fit results.

---

# Stop Conditions

Do not finalize novelty auditing when:

- the underlying gap is rejected, unresolved, or requires revalidation;
- the evidence cutoff is inappropriate to field velocity;
- closest competitors remain unidentified;
- terminology expansion is incomplete where needed;
- citation chaining is required but incomplete;
- adjacent disciplines may contain equivalent work;
- method, theory, or mechanism equivalence remains unresolved;
- critical competitor sources are unverified;
- study-family relationships materially affect interpretation;
- priority claims cannot be supported;
- the scientific gain cannot be articulated;
- what is novel and what is not novel cannot be separated;
- the final status depends primarily on publication prestige, quartile, citation count, target journal, or APC.

Use:

- `GAP_REVALIDATION_REQUIRED`
- `SEARCH_UPDATE_REQUIRED`
- `COMPETITOR_SEARCH_REQUIRED`
- `TERMINOLOGY_EXPANSION_REQUIRED`
- `CITATION_CHAINING_REQUIRED`
- `ADJACENT_DISCIPLINE_REVIEW_REQUIRED`
- `METHOD_EQUIVALENCE_REVIEW_REQUIRED`
- `SOURCE_VERIFICATION_REQUIRED`
- `REFERENCE_INTEGRITY_REQUIRED`
- `NOVELTY_INCONCLUSIVE`
- `NOT_READY_FOR_RESEARCH_QUESTION_FINALIZATION`

as appropriate.

---

# Success Criterion

`novelty-auditor` succeeds when a proposed scientific contribution is subjected to a deliberate adversarial audit against the current verified State of the Art, the validated gap, the strongest and closest competitor studies, terminology variants, citation lineage, adjacent disciplines, equivalent methods, theories, mechanisms, populations, contexts, validation studies, translational stages, and recent literature; when critical evidence is source-verified, integrity-cleared, purpose-screened, and synthesized rather than judged from isolated citations; when claims of discovery, validation, replication, mechanism, causality, method, measurement, prediction, intervention, implementation, translation, integration, context, and theory are distinguished accurately; when geographic location, institution, additional variables, larger sample size, software choice, model complexity, statistical significance, newer technology, journal prestige, quartile, citation count, Scopus status, target-journal strategy, and APC preference do not masquerade as scientific novelty; when broad priority claims such as "first," "never studied," or "unprecedented" are either supported by sufficiently broad evidence or removed; when the closest prior work is treated as the primary adversarial benchmark rather than selectively weaker comparators; when `WHAT IS NOVEL` and `WHAT IS NOT NOVEL` remain explicit; when the novelty claim is preserved, narrowed, partially supported, reframed, weakened, classified as likely duplicative, rejected, or left inconclusive according to the evidence rather than researcher preference; when gap revalidation and SoTA updates are triggered whenever new evidence changes the scientific basis of the claim; when a scientifically valid outcome may be `NOVELTY_REJECTED` or `LIKELY_DUPLICATIVE`; and when only a calibrated, comparator-grounded, evidence-current contribution claim is handed downstream to `research-question-builder`, `hypothesis-builder` when appropriate, `theoretical-framework`, `conceptual-framework`, `methodology-architect`, research-trajectory planning, manuscript construction, journal matching, reviewer simulation, or reviewer response.
