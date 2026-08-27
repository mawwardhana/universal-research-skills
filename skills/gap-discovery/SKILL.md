---
name: gap-discovery
description: Discover and structure candidate research gaps from a verified State of the Art by examining unresolved questions, contradictory evidence, theoretical limitations, methodological weaknesses, missing validation, measurement problems, contextual boundary conditions, temporal uncertainty, implementation failures, and translational discontinuities. Use after State-of-the-Art development and before formal gap validation or novelty construction.
---

# Research Gap Discovery

## Purpose

`gap-discovery` converts unresolved scientific conditions identified in the State of the Art into explicit candidate research gaps.

Its central question is:

> Which unresolved conditions in the current scientific evidence may represent meaningful and researchable gaps?

The purpose is not to declare every unanswered question a research gap.

The purpose is to identify, classify, and prioritize:

`CANDIDATE_RESEARCH_GAPS`

that can later be stress-tested through:

`gap-validator`

A candidate gap remains provisional until validated against current evidence.

---

# Core Principle

Use:

> Unresolved does not automatically mean gap, and gap does not automatically mean worthwhile research.

A defensible research gap should eventually demonstrate:

1. a meaningful unresolved scientific condition;
2. evidence that the condition remains unresolved;
3. scientific or practical consequences of that uncertainty;
4. a plausible research pathway capable of addressing it.

`gap-discovery` addresses primarily points 1, 3, and 4.

`gap-validator` determines point 2 rigorously.

---

# Required Upstream Context

Prefer outputs from:

`scopus-literature-search`
→ `source-verification`
→ `reference-integrity-guard`
→ `citation-chaining`
→ `literature-screening`
→ `evidence-synthesis`
→ `sota-builder`

Important SoTA inputs include:

- established knowledge;
- emerging evidence;
- contested evidence;
- unresolved questions;
- scientific frontiers;
- methodological limitations;
- measurement limitations;
- contextual boundaries;
- evidence maturity;
- closest competitor studies.

Do not generate gaps from memory when a verified SoTA is available.

---

# Activation Conditions

Use this skill when the researcher asks:

- "What is the research gap?"
- "Which gaps exist in this literature?"
- "What remains unanswered?"
- "Where can I position my study?"
- "What should be researched next?"
- "Which unresolved issue could become my research problem?"
- "What gap remains after my previous study?"
- "Which part of the State of the Art creates a research opportunity?"

Do not use this skill as a substitute for literature search.

---

# Gap Discovery Status

All outputs from this skill should initially use:

`CANDIDATE_GAP`

or:

`POTENTIAL_GAP_SIGNAL`

Do not use:

`VALIDATED_RESEARCH_GAP`

until `gap-validator` has completed the validation process.

---

# 1. Start from the SoTA

The preferred discovery logic is:

```text
ESTABLISHED
What is already sufficiently known?

EMERGING
What is developing but still immature?

CONTESTED
Where does evidence disagree?

UNRESOLVED
What important scientific questions remain unanswered?

FRONTIER
Where is the field actively advancing?
```

Candidate gaps should arise from relationships among these states, not isolated absence statements.

---

# 2. Gap Discovery Logic

```text
Verified Evidence
      ↓
Evidence Synthesis
      ↓
State of the Art
      ↓
Unresolved Scientific Condition
      ↓
Candidate Gap Signal
      ↓
Scientific Importance
      ↓
Researchability
      ↓
CANDIDATE_GAP
      ↓
gap-validator
```

Do not skip validation.

---

# 3. Core Distinctions

Preserve:

```text
few papers ≠ scientific gap
research gap ≠ novelty
research gap ≠ research question
methodological difference ≠ methodological gap
new geography ≠ strong scientific gap
new software ≠ scientific contribution
additional variables ≠ meaningful novelty
```

A gap must describe a scientifically meaningful unresolved condition.

---

# 4. Candidate Gap Record

```yaml
candidate_gap:
  gap_id:
  statement:
  gap_type:
  originating_sota_status:
  evidence_basis:
  scientific_importance:
  practical_importance:
  affected_population:
  affected_context:
  closest_competitors:
  known_gap_threats:
  researchability:
  feasibility:
  validation_required:
  validation_priority:
  notes:
```

Unknown values remain unknown.

---

# 5. Gap Taxonomy

Candidate gaps may include:

- `EVIDENCE_GAP`
- `CONTRADICTION_GAP`
- `REPLICATION_GAP`
- `VALIDATION_GAP`
- `MECHANISM_GAP`
- `CAUSAL_GAP`
- `THEORETICAL_GAP`
- `CONCEPTUAL_GAP`
- `METHODOLOGICAL_GAP`
- `MEASUREMENT_GAP`
- `POPULATION_GAP`
- `CONTEXT_GAP`
- `TEMPORAL_GAP`
- `IMPLEMENTATION_GAP`
- `TRANSLATIONAL_GAP`
- `PREDICTION_GAP`
- `DIAGNOSTIC_GAP`
- `PROGNOSTIC_GAP`
- `GENERALIZABILITY_GAP`
- `INTEGRATION_GAP`

A candidate may legitimately have more than one type.

---

# 6. Evidence Gap

`EVIDENCE_GAP` means relevant evidence remains insufficient for an important proposition. Potential signals include too few independent studies, inadequate diversity, insufficient follow-up, missing outcomes, or weak replication. Do not define it only by publication count.

---

# 7. Contradiction Gap

`CONTRADICTION_GAP` arises when credible evidence points in different directions and the reason remains unresolved. Investigate population, measurement, design, dose, context, analysis, time, and theory.

---

# 8. Replication Gap

`REPLICATION_GAP` exists when an important finding lacks adequate independent replication. Distinguish direct, conceptual, external, and cross-context replication.

---

# 9. Validation Gap

`VALIDATION_GAP` occurs when a finding, model, instrument, biomarker, algorithm, or method lacks adequate internal, external, temporal, geographic, prospective, or clinical validation.

---

# 10. Mechanism Gap

`MECHANISM_GAP` occurs when a relationship or effect is observed but the explanatory process remains insufficiently tested. Do not infer mechanism from association alone.

---

# 11. Causal Gap

`CAUSAL_GAP` occurs when association is known but causal inference remains unresolved because of confounding, reverse causation, weak temporality, or inadequate causal design.

---

# 12. Theoretical Gap

`THEORETICAL_GAP` occurs when theory fails to explain evidence, produces competing predictions, lacks boundary conditions, or has not been tested in critical contexts. Route formal theory work to `theoretical-framework`.

---

# 13. Conceptual Gap

`CONCEPTUAL_GAP` occurs when constructs or relationships are inadequately defined, distinguished, or integrated. Route formal organization to `conceptual-framework`.

---

# 14. Methodological Gap

`METHODOLOGICAL_GAP` requires a methodological weakness that materially limits scientific inference. A different software package alone is not enough.

---

# 15. Measurement Gap

`MEASUREMENT_GAP` occurs when measurement is inadequate in validity, reliability, sensitivity, specificity, invariance, assay quality, or standardization. Route instrument issues to `instrument-design`.

---

# 16. Population Gap

`POPULATION_GAP` exists when evidence cannot be generalized to a scientifically important population. The population difference must plausibly matter.

---

# 17. Context Gap

`CONTEXT_GAP` occurs when context may alter the phenomenon and evidence is insufficient.

---

# 18. Temporal Gap

`TEMPORAL_GAP` occurs when evidence does not adequately address time, duration, latency, follow-up, or evolving systems.

---

# 19. Implementation Gap

`IMPLEMENTATION_GAP` occurs when efficacy or effectiveness evidence exists but adoption, fidelity, sustainability, scalability, or real-world implementation remains unresolved.

---

# 20. Translational Gap

`TRANSLATIONAL_GAP` occurs at a meaningful transition such as mechanism → preclinical, preclinical → human, human → clinical, or clinical → implementation.

---

# 21. Prediction Gap

`PREDICTION_GAP` occurs when prediction models lack calibration, external validation, transportability, prospective evaluation, or clinical utility. Prediction gaps are not causal gaps.

---

# 22. Diagnostic Gap

`DIAGNOSTIC_GAP` may involve unresolved accuracy, thresholds, reference standards, spectrum effects, or external validation.

---

# 23. Prognostic Gap

`PROGNOSTIC_GAP` may involve prognostic-factor uncertainty, calibration, time horizon, external validation, or clinical utility.

---

# 24. Generalizability Gap

`GENERALIZABILITY_GAP` occurs when evidence is strong in one setting but transportability to another scientifically important setting is uncertain.

---

# 25. Integration Gap

`INTEGRATION_GAP` occurs when meaningful evidence streams remain disconnected, such as molecular and clinical evidence, quantitative and qualitative evidence, or theory and empirical evidence.

---

# 26. Replication Independence Guard

Do not call several publications from one cohort, database, or research group independent replication.

Route study-family ambiguity to `reference-integrity-guard`.

---

# 27. Gap Signals from SoTA

Use:

```text
ESTABLISHED → boundary, mechanism, validation, implementation
EMERGING → replication, validation, maturity
CONTESTED → contradiction, measurement, method, theory
UNRESOLVED → evidence, causal, mechanism, population
FRONTIER → next substantive scientific boundary
```

Do not repeat an already-established question.

---

# 28. Gap Signals from Evidence Maturity

Examples:

```text
mature association
+
immature mechanism
=
candidate mechanism gap
```

```text
mature derivation
+
weak external validation
=
candidate validation gap
```

---

# 29. Gap Signals from Boundaries

A finding may be established only within one population, context, measurement, dose, or time window. Boundary uncertainty can become a candidate gap when the boundary is scientifically meaningful.

---

# 30. Gap Signals from Failed Replication

Failed replication may indicate a contradiction, boundary-condition, measurement, or mechanism gap. Do not propose another identical replication without diagnosing why findings differ.

---

# 31. Gap Signals from Previous Research

For previous work ask:

- What did the study resolve?
- What scientific limitation remained?
- What later evidence changed the field?
- What has been replicated or contradicted?
- What continuation would now advance the field?

Use `research-resume`, `prior-research-auditor`, `research-trajectory-mapper`, and `continuation-opportunity-finder` when appropriate.

---

# 32. Scientific Importance

Every candidate gap should answer:

> Why does resolving this uncertainty matter scientifically?

Possible reasons include improving theory, causal understanding, mechanism, measurement, validation, generalizability, translation, implementation, or reproducibility.

---

# 33. Practical Importance

Practical relevance may involve clinical decisions, policy, education, industry, implementation, safety, or resource allocation. Practical importance does not substitute for scientific importance.

---

# 34. Researchability

A candidate gap is researchable when it can be converted into an answerable scientific question using feasible evidence.

Assess measurable outcomes, population access, defensible design, ethical feasibility, and analytical feasibility.

Possible statuses:

- `HIGH`
- `MODERATE`
- `LOW`
- `UNCERTAIN`
- `NOT_CURRENTLY_RESEARCHABLE`

---

# 35. Feasibility Boundary

Scientific gap quality and project feasibility are separate. A high-value gap may be infeasible. Do not redefine the science merely to fit current resources.

---

# 36. Gap Priority

Prioritize using scientific importance, evidence need, impact, researchability, feasibility, translational relevance, theoretical leverage, and replication need.

Do not prioritize solely because a study is easy, cheap, fashionable, publication-friendly, or likely to produce significance.

---

# 37. Gap Threat

A `GAP_THREAT` is existing evidence that may weaken, narrow, reframe, or defeat a candidate gap.

Threats include:

- recent competitors;
- alternative terminology;
- equivalent methods;
- adjacent disciplines;
- hidden replication;
- updated reviews.

---

# 38. Gap Threat Record

```yaml
gap_threat:
  candidate_gap:
  source:
  threat_type:
  overlap:
  difference:
  potential_effect:
  verification_status:
```

---

# 39. Closest Competitor

Every important candidate gap should identify the closest known studies.

Compare question, population, exposure/intervention, mechanism, method, outcome, and contribution.

---

# 40. Search Freshness

Candidate gaps are sensitive to recent literature.

In fast-moving fields, update the search and forward-chain recent anchors using `scopus-literature-search` and `citation-chaining`.

In slower fields, do not let recency erase foundational literature.

---

# 41. Terminology Expansion

Before validating a gap, identify synonyms, historical terms, neighboring constructs, and alternative method labels. Terminology mismatch can create a false gap.

---

# 42. Adjacent Discipline and Method Equivalence

A gap may already be addressed in another discipline or through another scientifically equivalent method.

Do not restrict evidence to the home discipline or exact method label merely to protect novelty.

---

# 43. Candidate Gap Statement

A good candidate gap statement includes:

```text
what is known
+
what remains unresolved
+
why it matters
+
what evidence is needed
```

Template:

> Although [established knowledge], evidence remains insufficient or inconsistent regarding [specific unresolved condition], particularly under [boundary/context], limiting [scientific consequence]. This suggests a candidate [gap type] requiring validation against the latest and adjacent evidence.

Do not present it as validated.

---

# 44. Weak vs Strong Gap Statements

Weak:

> Few studies have examined X.

Stronger:

> Existing studies consistently demonstrate X, but most rely on cross-sectional designs, leaving temporal ordering unresolved. This creates a candidate causal/temporal gap rather than a simple evidence-count gap.

---

# 45. Candidate Gap Strength

Possible discovery-stage labels:

- `WEAK_SIGNAL`
- `PLAUSIBLE_CANDIDATE`
- `PROMISING_CANDIDATE`
- `HIGH_PRIORITY_CANDIDATE`
- `VALIDATION_REQUIRED`

Do not use `VALIDATED_RESEARCH_GAP` here.

---

# 46. Gap Discovery Matrix

| Candidate Gap | Type | SoTA Basis | Scientific Importance | Main Threat | Validation Priority |
|---|---|---|---|---|---|

---

# 47. Gap Logic Chain

```text
Evidence
      ↓
SoTA Status
      ↓
Unresolved Condition
      ↓
Scientific Consequence
      ↓
Candidate Gap
      ↓
Validation Need
```

---

# 48. Gap Validation Brief

Prepare for `gap-validator`:

```yaml
gap_validation_brief:
  candidate_gap:
  gap_type:
  evidence_basis:
  strongest_support:
  closest_competitors:
  known_threats:
  alternative_terms:
  adjacent_methods:
  adjacent_disciplines:
  latest_search_status:
  critical_uncertainties:
```

---

# 49. Validation Gates

Before `READY_FOR_GAP_VALIDATION`:

- ensure the evidence cutoff is current enough;
- identify closest competitors;
- expand terminology;
- inspect adjacent methods and disciplines;
- verify mechanism/theory/measurement alternatives where relevant;
- explain why population or context could alter inference;
- verify prerequisite evidence for implementation or translation;
- specify why existing evidence cannot answer causal, prediction, diagnostic, or prognostic questions.

---

# 50. Gap Portfolio

A research program may contain linked gaps.

```text
Mechanism Gap
      ↓
Validation Gap
      ↓
Implementation Gap
```

Route multi-study progression to `research-trajectory-mapper`.

Some gaps may instead run in parallel when scientifically independent.

---

# 51. Research Value and Redundancy Tests

For each candidate gap ask:

1. Would answering it change scientific understanding?
2. Would it resolve meaningful uncertainty?
3. Would it improve validity, mechanism, generalizability, or application?
4. Would a null result still be informative?
5. Would the proposed study mostly repeat what is already known?

If the study is only one more variable, location, sample, or software package, require stronger scientific justification.

---

# 52. Domain Adaptation

Apply the same logic across disciplines.

Examples:

- pharmacogenetics: replication, response/toxicity validation, functional mechanism;
- pharmacokinetics: population PK, covariates, exposure-response, external validation;
- formulation: stability, mechanism, scale-up, translation;
- qualitative research: missing perspectives, context, implementation mechanism;
- education: learning mechanism, transfer, longitudinal outcome;
- social sciences: theory boundaries, construct validity, contextual mechanism;
- engineering: robustness, scalability, validation, safety;
- computational work: calibration, external validation, robustness, interpretability.

Do not use discipline-specific complexity to bypass the core rules.

---

# 53. Phenomenon Evidence Boundary

Real-world significance may come from `phenomenon-evidence-builder`.

Phenomenon evidence can establish magnitude, burden, trend, policy, regulation, or implementation shortfall.

It does not independently establish a scholarly research gap.

```text
Phenomenon Evidence → Why the problem matters
Scholarly Evidence  → What science knows and does not know
```

---

# 54. Evidence Chain Relationships

The preferred scholarly evidence chain is:

```text
scopus-literature-search
      ↓
source-verification
      ↓
reference-integrity-guard
      ↓
citation-chaining
      ↓
literature-screening
      ↓
evidence-synthesis
      ↓
sota-builder
      ↓
gap-discovery
      ↓
gap-validator
```

New evidence discovered during gap work must re-enter verification and screening before substantive use.

---

# 55. Relationship with Gap Validator

`gap-discovery` proposes candidate gaps.

`gap-validator` attempts to defeat, narrow, reframe, or validate them.

Do not skip this adversarial checkpoint.

---

# 56. Relationship with Novelty

After validation:

```text
validated or reframed gap
      ↓
novelty-builder
      ↓
novelty-auditor
```

Do not build strong novelty claims from an unvalidated candidate gap.

---

# 57. Relationship with Research Question and Hypothesis

After gap and novelty are sufficiently clear, route to `research-question-builder`.

Do not build hypotheses directly from gap wording.

When confirmatory hypotheses are appropriate:

```text
research-question-builder
      ↓
theoretical-framework when required
      ↓
hypothesis-builder
```

The downstream hypothesis skill is `hypothesis-builder`.

---

# 58. Relationship with Theory, Conceptual Framework, and Methodology

If the gap is theoretical or mechanism-dependent, route to `theoretical-framework`.

If it concerns construct relationships, route to `conceptual-framework`.

Do not select methodology merely because a methodological gap was identified. First define the scientific question, then route to `methodology-architect`.

Population gaps may later inform `sampling-strategy`.

Measurement gaps may later inform `instrument-design`.

Analytical issues may later inform `analysis-planner` or `statistical-method-selector`.

---

# 59. Relationship with Previous Research

Use `research-resume`, `prior-research-auditor`, `research-trajectory-mapper`, and `continuation-opportunity-finder` for continuation workflows.

Do not mechanically extend older work.

---

# 60. Relationship with Manuscript and Reviewer Workflows

`manuscript-auditor` may identify unsupported gap statements and route them back here or to `gap-validator`.

If actual reviewer feedback challenges a gap claim, route scientific reassessment through `reviewer-response`.

---

# 61. Gap Discovery Passport

```yaml
gap_discovery:
  source_sota:
  evidence_cutoff:
  candidate_gaps:
  gap_types:
  priority_candidates:
  weak_candidates:
  known_threats:
  closest_competitors:
  terminology_expansion_needed:
  search_update_needed:
  validation_status:
  next_stage:
```

---

# 62. Gap Discovery Status

Possible statuses:

- `NOT_STARTED`
- `SOTA_REQUIRED`
- `CANDIDATE_GAPS_IDENTIFIED`
- `SEARCH_UPDATE_REQUIRED`
- `THREAT_REVIEW_REQUIRED`
- `READY_FOR_GAP_VALIDATION`
- `NO_MEANINGFUL_CANDIDATE_GAP`
- `INSUFFICIENT_EVIDENCE`

---

# 63. No-Gap Outcome and Reframing

A scientifically valid outcome may be:

`NO_MEANINGFUL_CANDIDATE_GAP`

Do not invent a gap merely because the researcher expects one.

Reframing example:

```text
Original:
"No studies examined X."

Reframed:
"Evidence on X exists, but external validation in Y remains limited."
```

A narrower gap is often more defensible.

---

# 64. Full Output

For a comprehensive task provide:

## A. SoTA Basis
[...]

## B. Unresolved Scientific Conditions
[...]

## C. Candidate Gap Types
[...]

## D. Candidate Gap Statements
[...]

## E. Scientific Importance
[...]

## F. Practical Importance
[...]

## G. Closest Competitors
[...]

## H. Known Gap Threats
[...]

## I. Researchability
[...]

## J. Feasibility
[...]

## K. Priority Ranking
[...]

## L. Validation Requirements
[...]

## M. Recommended Next Skill
[...]

---

# 65. Compact Output

```text
Candidate gap:
Type:
What is known:
What remains unresolved:
Why it matters:
Main threat:
Validation needed:
```

---

# 66. User-Friendly Behavior

Prefer:

> The strongest candidate gap is not that the topic has never been studied. Relevant studies already exist. The more defensible gap is that the finding has not been externally validated in the target population.

Or:

> The literature already supports the association, so another association study would add little. The unresolved issue is mechanism, making a mechanism gap more defensible.

Or:

> This is still a candidate gap. Before using it in a proposal or manuscript, it should be attacked by `gap-validator`.

---

# 67. Avoid These Behaviors

Do not:

- fabricate a gap;
- treat unanswered curiosity as a scientific gap;
- treat few papers as proof of a gap;
- treat geography alone as strong novelty;
- treat software novelty as a gap;
- treat variable combinations as gaps;
- ignore competitors;
- ignore contradictory evidence;
- ignore equivalent terminology;
- ignore adjacent disciplines;
- ignore method equivalence;
- hide evidence that weakens the gap;
- declare a candidate gap validated;
- build novelty before validation;
- formulate a final research question from a weak gap;
- build hypotheses before the question and theory requirements are clear;
- choose methodology before the scientific question is sufficiently clear;
- let APC, journal prestige, quartile, citation count, or target-journal strategy influence scientific gap identification.

---

# Stop Conditions

Do not mark gap discovery ready for validation when:

- no verified SoTA or adequate evidence base exists;
- the unresolved condition is not scientifically meaningful;
- the candidate is based only on literature scarcity;
- a major recent search update is required;
- the closest competitor is unknown;
- terminology expansion has not been considered where needed;
- an adjacent discipline or equivalent method may already address the issue;
- the candidate depends only on geography, software, or adding variables;
- study-family dependence materially distorts the evidence;
- critical contradictory evidence remains unexplored;
- the candidate cannot be converted into a researchable scientific question;
- the gap statement already claims "first," "never," or "no studies" without validation.

Use:

- `SOTA_REQUIRED`
- `SEARCH_UPDATE_REQUIRED`
- `SOURCE_VERIFICATION_REQUIRED`
- `REFERENCE_INTEGRITY_REQUIRED`
- `COMPETITOR_REVIEW_REQUIRED`
- `TERMINOLOGY_EXPANSION_REQUIRED`
- `ADJACENT_DISCIPLINE_REVIEW_REQUIRED`
- `WEAK_CANDIDATE_GAP`
- `NO_MEANINGFUL_CANDIDATE_GAP`
- `NOT_READY_FOR_GAP_VALIDATION`

as appropriate.

---

# Success Criterion

`gap-discovery` succeeds when unresolved scientific conditions are extracted from a sufficiently verified, screened, synthesized, and current State of the Art and transformed into explicit `CANDIDATE_GAP` statements that are scientifically meaningful, researchable, bounded, and transparent about uncertainty; when candidate gaps are classified by substantive type rather than superficial novelty; when what is established is clearly separated from what remains unresolved; when the scientific consequence of uncertainty is explained; when closest competitors, gap threats, alternative terminology, equivalent methods, adjacent disciplines, contradictory evidence, study-family dependence, field velocity, and evidence cutoff are considered; when literature scarcity, new geography, added variables, software choice, journal strategy, citation count, prestige, quartile, or APC status are not mistaken for scientific gaps; when candidate gaps are prioritized according to scientific value, researchability, feasibility, validation need, and contribution potential; when `NO_MEANINGFUL_CANDIDATE_GAP` is accepted as a valid outcome; when previous research can be converted into defensible continuation signals without mechanical extension; when all candidate gaps remain provisional until adversarially tested by `gap-validator`; and when the resulting gap portfolio provides a traceable, balanced, evidence-grounded basis for downstream `novelty-builder`, `novelty-auditor`, `research-question-builder`, `hypothesis-builder` when appropriate, `research-trajectory-mapper`, `methodology-architect`, and manuscript positioning.
