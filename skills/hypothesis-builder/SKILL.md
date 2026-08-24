---
name: hypothesis-builder
description: Construct theoretically justified, evidence-grounded, testable, and appropriately directional research hypotheses from finalized research questions when hypothesis testing is scientifically appropriate. Use for confirmatory quantitative, experimental, explanatory, mechanism, moderation, mediation, and theory-testing studies, but skip or limit hypothesis generation for exploratory, descriptive, qualitative, discovery-oriented, and many evidence-synthesis designs.
---

# Hypothesis Builder

## Purpose

`hypothesis-builder` constructs testable scientific hypotheses only when the research design and knowledge objective justify hypothesis testing.

Its central question is:

> Given the finalized research question, current evidence, theoretical or mechanistic explanation, and audited scientific contribution, what specific expectation should be tested?

A hypothesis is not simply:

> an expected significant relationship.

A scientifically useful hypothesis should express an evidence-grounded proposition about:

- direction;
- difference;
- association;
- mechanism;
- mediation;
- moderation;
- interaction;
- causal effect;
- prediction;
- longitudinal change;
- validation;
- equivalence or non-inferiority;

when appropriate.

---

# Core Principle

Use:

> Hypotheses follow scientific reasoning; they do not create scientific reasoning.

Do not construct hypotheses merely because:

- quantitative data will be collected;
- regression will be used;
- SEM will be used;
- PLS-SEM will be used;
- a thesis template requires H1, H2, H3;
- many variables exist.

The hypothesis must emerge from:

```text
Research Question
      ↓
Scientific Theory / Mechanism
      ↓
Prior Evidence
      ↓
Expected Relationship
      ↓
Testable Hypothesis
```

A formal named theory is not always required.

The explanatory basis may instead come from:

- biological mechanism;
- pharmacological mechanism;
- physical principle;
- established empirical evidence;
- validated scientific model.

---

# Required Upstream Context

Prefer inputs from:

`research-question-builder`

and, where relevant:

`theoretical-framework`

Additional evidence may come from:

`evidence-synthesis`
→ `sota-builder`
→ `gap-validator`
→ `novelty-auditor`

Important inputs include:

- finalized research question;
- question orientation;
- exploratory vs confirmatory status;
- validated gap;
- audited novelty;
- relevant theory;
- mechanistic rationale;
- prior empirical evidence;
- expected direction;
- population;
- context;
- temporal logic;
- proposed mediators;
- proposed moderators;
- competing explanations.

Do not generate hypotheses from variables alone.

---

# Activation Gate

Before constructing hypotheses, inspect the hypothesis status from:

`research-question-builder`

Possible values:

- `HYPOTHESIS_REQUIRED`
- `HYPOTHESIS_APPROPRIATE`
- `HYPOTHESIS_OPTIONAL`
- `HYPOTHESIS_NOT_APPROPRIATE`

When:

`HYPOTHESIS_REQUIRED`

construct explicit hypotheses.

When:

`HYPOTHESIS_APPROPRIATE`

construct hypotheses when they improve confirmatory reasoning.

When:

`HYPOTHESIS_OPTIONAL`

explain whether hypotheses add scientific value.

When:

`HYPOTHESIS_NOT_APPROPRIATE`

do not force hypothesis generation.

---

# When Hypotheses Are Commonly Appropriate

Hypotheses are commonly useful for:

- confirmatory quantitative research;
- experimental research;
- explanatory research;
- theory testing;
- mechanism testing;
- mediation;
- moderation;
- interaction;
- longitudinal directional relationships;
- equivalence testing;
- non-inferiority testing;
- confirmatory validation.

---

# When Hypotheses May Be Inappropriate

Formal hypotheses may be unnecessary or inappropriate for:

- exploratory qualitative research;
- phenomenology;
- many grounded-theory studies;
- purely descriptive studies;
- early discovery studies;
- exploratory bibliometric studies;
- many scoping reviews;
- open-ended evidence mapping;
- some methodological-development studies;
- some exploratory machine-learning studies.

Do not treat the absence of hypotheses as scientific weakness.

---

# 1. Start from the Research Question

Every hypothesis must map to a finalized RQ.

Conceptually:

```text
Research Question
      ↓
Scientific Expectation
      ↓
Hypothesis
```

If a hypothesis cannot be connected to an RQ:

classify:

`HYPOTHESIS_RQ_MISALIGNMENT`

Do not allow hypotheses to create new research questions silently.

---

# 2. Determine Hypothesis Function

Classify the scientific function.

Possible types include:

- `ASSOCIATION`
- `DIFFERENCE`
- `DIRECTIONAL`
- `CAUSAL`
- `MEDIATION`
- `MODERATION`
- `INTERACTION`
- `MECHANISM`
- `LONGITUDINAL`
- `DOSE_RESPONSE`
- `VALIDATION`
- `PREDICTIVE`
- `NONINFERIORITY`
- `EQUIVALENCE`

The hypothesis type should reflect the RQ.

---

# 3. Evidence Before Direction

Do not assign:

- positive;
- negative;
- higher;
- lower;
- stronger;
- weaker;

without scientific justification.

Directional hypotheses should be supported by:

- theory;
- mechanism;
- consistent empirical evidence;
- established scientific principles.

When evidence is genuinely conflicting:

consider a non-directional hypothesis or preserve competing expectations.

---

# 4. Theory Prerequisite Gate

Before finalizing a theory-dependent hypothesis, determine whether the required theoretical framework has already been established.

Use:

- `THEORY_ALREADY_ESTABLISHED`
- `THEORY_NOT_REQUIRED`
- `THEORY_REQUIRED_BEFORE_HYPOTHESIS`
- `THEORY_STATUS_UNCLEAR`

When:

`THEORY_REQUIRED_BEFORE_HYPOTHESIS`

pause hypothesis finalization and route to:

`theoretical-framework`

first.

Conceptually:

```text
Research Question
      ↓
Theory-dependent expectation
      ↓
Has theoretical basis been established?
      │
      ├── YES
      │     ↓
      │ hypothesis-builder
      │
      └── NO
            ↓
      theoretical-framework
            ↓
      hypothesis-builder
```

Do not use:

```text
Create hypothesis
      ↓
Search for theory that supports it
```

when the hypothesis explicitly depends on a theoretical proposition.

This prevents post-hoc theoretical justification.

---

# 5. Non-Theory Hypothesis Path

A formal named theory is not mandatory for every hypothesis.

Hypotheses may be grounded legitimately in:

- biological mechanisms;
- pharmacological mechanisms;
- physiological principles;
- physical principles;
- established empirical evidence;
- validated scientific models;
- robust prior experiments.

In these cases use:

`THEORY_NOT_REQUIRED`

while preserving explicit scientific rationale.

Do not invent a theory merely to satisfy the workflow.

---

# 6. Association Hypothesis

Use when the RQ concerns whether variables are related.

Generic form:

```text
X is associated with Y.
```

Directional form:

```text
Higher X is associated with higher Y.
```

Use directional wording only when justified.

Do not interpret association as causation.

---

# 7. Difference Hypothesis

Use when comparing groups, conditions, or treatments.

Generic form:

```text
Outcome Y differs between group A and group B.
```

Directional form:

```text
Group A has higher Y than group B.
```

Direction requires prior justification.

---

# 8. Causal Hypothesis

Use only when the planned design can support causal inference.

Generic structure:

```text
Changing X causes a change in Y.
```

Possible support may include:

- randomized intervention;
- strong quasi-experimental design;
- defensible causal observational framework.

Do not use causal hypotheses merely because arrows appear in a model.

---

# 9. Mechanistic Hypothesis

Use when the scientific contribution concerns how an effect occurs.

Example logic:

```text
X
↓
Mechanism M
↓
Y
```

A mechanism is more than a statistical indirect effect.

It should reflect a scientifically meaningful process.

---

# 10. Mediation Hypothesis

A mediation hypothesis should answer:

> Through what process does X relate to Y?

Conceptually:

```text
X → M → Y
```

A defensible mediation hypothesis requires reasons why:

1. X should relate to M;
2. M should relate to Y;
3. the sequence is scientifically plausible.

Do not introduce M merely because mediation software can estimate an indirect effect.

---

# 11. Temporal Logic for Mediation

When mediation is intended to represent a process, temporal ordering matters.

Prefer designs conceptually consistent with:

```text
X at T1
↓
M at T2
↓
Y at T3
```

Cross-sectional mediation may estimate statistical patterns but should not automatically be described as evidence of temporal mechanism.

---

# 12. Moderation Hypothesis

A moderation hypothesis answers:

> Under what condition, or for whom, does the X–Y relationship differ?

Conceptually:

```text
X → Y
    ↑
    Z changes the relationship
```

Z should represent a scientifically plausible boundary condition.

Do not use moderators simply because subgroup variables exist.

---

# 13. Interaction Hypothesis

Interaction hypotheses should specify how the effect or association involving one factor changes across levels of another factor.

Do not use the word interaction merely because several predictors are present.

---

# 14. Dose-Response Hypothesis

Use when scientific reasoning predicts systematic change across exposure or dose.

Possible forms include:

- linear;
- monotonic;
- threshold;
- U-shaped;
- inverted U-shaped;
- saturation.

Do not assume linearity without evidence.

---

# 15. Longitudinal Hypothesis

Longitudinal hypotheses should explicitly preserve temporal sequence.

Example:

```text
X at baseline predicts subsequent change in Y.
```

Do not convert cross-sectional association into longitudinal expectation.

---

# 16. Predictive Hypothesis

Prediction should be distinguished from explanation.

A predictive hypothesis may concern:

- discrimination;
- calibration;
- generalization;
- improvement over a reference model.

Example:

> A model including X improves out-of-sample prediction of Y relative to the reference model.

Do not interpret predictive importance as causal importance.

---

# 17. Validation Hypothesis

Validation studies may test whether:

- an instrument retains validity;
- a model retains performance;
- a relationship replicates;
- measurement structure remains stable;
- estimates generalize.

Do not pretend validation is first discovery.

---

# 18. Non-Inferiority Hypothesis

Non-inferiority requires a scientifically justified margin.

Do not choose a margin merely to achieve statistical significance.

The margin should be grounded in:

- clinical relevance;
- scientific relevance;
- prior trials;
- regulatory guidance where appropriate.

---

# 19. Equivalence Hypothesis

Equivalence tests whether differences remain within predefined scientifically meaningful bounds.

Do not interpret a non-significant conventional difference test as equivalence.

---

# 20. Null Hypothesis

Do not confuse the statistical null hypothesis with the scientific research hypothesis.

Statistical testing may define:

`H0`

for mathematical inference.

The scientific hypothesis should communicate the substantive proposition.

---

# 21. Avoid Significant-Effect Wording

Weak:

> X has a significant effect on Y.

This mixes the scientific proposition with an unknown statistical result.

Prefer:

> Higher X is associated with higher Y.

or:

> Intervention X reduces Y relative to control.

Statistical significance is evaluated after data are analyzed.

---

# 22. Hypothesis Direction Status

Use:

- `DIRECTION_SUPPORTED`
- `DIRECTION_PARTIALLY_SUPPORTED`
- `DIRECTION_CONTESTED`
- `NON_DIRECTIONAL_PREFERRED`
- `DIRECTION_UNSUPPORTED`

Do not create directional certainty from ambiguous evidence.

---

# 23. Evidence Strength

Classify the evidence basis as:

- `STRONG`
- `MODERATE`
- `LIMITED`
- `CONFLICTING`
- `INSUFFICIENT`

Evidence strength should influence hypothesis confidence.

---

# 24. Theory–Hypothesis Alignment

When theory is relevant, map:

```text
Theory Proposition
      ↓
Expected Relationship
      ↓
Hypothesis
```

Use:

- `DIRECT_THEORY_ALIGNMENT`
- `PARTIAL_THEORY_ALIGNMENT`
- `WEAK_THEORY_ALIGNMENT`
- `THEORY_NOT_APPLICABLE`

Do not cite theory that does not actually support the proposition.

---

# 25. Mechanism–Hypothesis Alignment

When the basis is mechanistic rather than formal theory, map:

```text
Scientific Mechanism
      ↓
Expected Change
      ↓
Hypothesis
```

Examples may involve:

- biological pathways;
- pharmacodynamics;
- material properties;
- physiological responses.

Do not force social-science theory onto biomedical or engineering mechanisms.

---

# 26. Evidence–Hypothesis Alignment

Each hypothesis should be traceable to supporting evidence.

Recommended internal structure:

```yaml
hypothesis:
  id:
  research_question:
  proposition:
  direction:
  theoretical_basis:
  mechanistic_basis:
  empirical_basis:
  contradictory_evidence:
  gap_relevance:
  novelty_relevance:
  status:
```

Unknown values remain unknown.

---

# 27. Gap–Hypothesis Alignment

Ask:

> Does testing this hypothesis help resolve the validated gap?

Use:

- `DIRECT_GAP_ALIGNMENT`
- `PARTIAL_GAP_ALIGNMENT`
- `NO_GAP_ALIGNMENT`

Remove hypotheses that do not contribute to the scientific problem unless clearly labeled secondary or exploratory.

---

# 28. Novelty–Hypothesis Alignment

Ask:

> Does testing this hypothesis generate evidence relevant to the audited novelty?

Use:

- `DIRECT_NOVELTY_ALIGNMENT`
- `SUPPORTING_NOVELTY_ALIGNMENT`
- `NO_NOVELTY_ALIGNMENT`

Do not claim every hypothesis as novel.

---

# 29. What Is Not Novel

A study may test established relationships as supporting pathways.

Example:

```text
H1: X → Y
already strongly established

H2: X → M → Y
mechanism remains unresolved
```

In this case H1 may be necessary but is not the primary novelty.

Preserve that distinction.

---

# 30. Primary vs Supporting Hypotheses

Classify hypotheses as:

- `PRIMARY`
- `SECONDARY`
- `MECHANISTIC`
- `BOUNDARY`
- `VALIDATION`
- `EXPLORATORY`

Do not present all hypotheses as equally central.

---

# 31. Hypothesis Quantity Guard

More hypotheses do not mean stronger research.

Avoid generating:

- H1 through H20;

unless the scientific design genuinely requires them.

Prefer the smallest set necessary to answer the RQs.

---

# 32. Hypothesis Redundancy Guard

Do not create separate hypotheses that simply restate the same proposition.

Flag:

`HYPOTHESIS_REDUNDANCY`

when necessary.

---

# 33. Construct Definition Guard

Hypothesis validity depends on conceptual clarity.

Before stating:

```text
X → Y
```

ensure X and Y have defensible conceptual meanings.

Do not use ambiguous construct labels.

---

# 34. Construct Overlap Guard

If two constructs substantially overlap conceptually:

flag:

`CONSTRUCT_OVERLAP_RISK`

Do not create artificial hypotheses between nearly synonymous constructs merely because separate scales exist.

---

# 35. Confounder Guard

A confounder is not automatically a substantive hypothesis variable.

Adjustment variables may belong in methodology rather than hypothesis development.

Do not transform every covariate into an H-numbered proposition.

---

# 36. Control Variable Guard

Do not hypothesize control-variable effects simply because the variable will be included statistically.

Controls should have a scientific reason for adjustment.

---

# 37. Causal Language Guard

Words such as:

- causes;
- affects;
- leads to;
- increases;
- decreases;

may imply causality.

Use them only when:

- scientific theory supports the causal proposition;
- design is likely capable of evaluating it.

Otherwise use relational language.

---

# 38. Prediction vs Causation Guard

Do not assume:

> X predicts Y

means:

> X causes Y.

Prediction may be accurate without causal interpretation.

---

# 39. Cross-Sectional Guard

Cross-sectional data may support:

- association;
- covariance;
- some prediction.

They are generally weaker for:

- temporal precedence;
- causal mechanisms;
- developmental trajectories.

Hypothesis language should reflect this limitation.

---

# 40. Reverse-Causality Guard

For observational relationships, ask whether:

```text
X → Y
```

could plausibly instead reflect:

```text
Y → X
```

or reciprocal influence.

Do not ignore reverse causality when scientifically plausible.

---

# 41. Competing Explanations

Identify credible alternative explanations.

When relevant:

```text
Preferred explanation:
X → Y

Alternative:
C → X
C → Y
```

Hypothesis development should not suppress plausible competing mechanisms.

---

# 42. Competing Hypotheses

When theories predict different outcomes, preserve them.

Possible architecture:

```text
Theory A
→ H1a

Theory B
→ H1b
```

Do not choose the preferred theory merely because it supports the desired result.

---

# 43. HARKing Guard

Do not formulate confirmatory hypotheses after observing the results and present them as if they were specified beforehand.

If the hypothesis arose after data inspection:

classify:

`POST_HOC_HYPOTHESIS`

or:

`EXPLORATORY_HYPOTHESIS`

Do not fabricate preregistration or prior specification.

---

# 44. Data-Driven Hypothesis Discovery

Exploratory analysis may legitimately generate hypotheses.

Use:

```text
Exploratory Analysis
      ↓
Candidate Pattern
      ↓
New Hypothesis
      ↓
Independent Future Test
```

Do not confuse generation with confirmation.

---

# 45. Confirmatory vs Exploratory Status

Classify each hypothesis:

- `CONFIRMATORY`
- `EXPLORATORY`
- `POST_HOC`
- `FUTURE_TEST`

This distinction should remain visible downstream.

---

# 46. Hypothesis and Research Design

A hypothesis may imply certain design requirements.

Examples:

Mechanistic temporal hypothesis:

```text
requires evidence of sequence
```

Causal intervention hypothesis:

```text
requires valid causal design
```

Moderation hypothesis:

```text
requires adequate interaction information
```

Do not choose detailed methods here.

Pass requirements downstream.

---

# 47. Hypothesis and Measurement

A hypothesis is only testable if its constructs can be measured appropriately.

Check whether:

- variables can be observed;
- constructs can be operationalized;
- required timing is feasible;
- relevant variation exists.

Detailed operationalization belongs downstream.

---

# 48. Hypothesis and Population

A hypothesis may be scientifically valid only within defined population boundaries.

Do not generalize beyond the target population implicitly.

---

# 49. Hypothesis and Context

Context may affect:

- mechanism;
- direction;
- magnitude;
- boundary conditions.

However, location alone does not automatically create a new hypothesis.

---

# 50. Hypothesis and Time

When time matters, specify it.

Example:

> Higher baseline X predicts greater decline in Y over 12 months.

Do not leave essential temporal logic implicit.

---

# 51. Hypothesis Testability

Classify:

- `CLEARLY_TESTABLE`
- `TESTABLE_WITH_REFINEMENT`
- `DIFFICULT_TO_TEST`
- `NOT_TESTABLE_AS_WRITTEN`

A proposition may be scientifically interesting but too vague to test.

---

# 52. Hypothesis Falsifiability

Where appropriate, ask:

> What observation would be inconsistent with this hypothesis?

A good hypothesis should allow empirical challenge.

---

# 53. Hypothesis Precision

Avoid vague wording such as:

- influences;
- relates somehow;
- plays a role;
- impacts;

when the intended scientific relationship can be described more precisely.

---

# 54. Directional Hypothesis Example

Use conceptually:

```text
H1:
Higher X is associated with higher Y.
```

Only when direction is justified.

---

# 55. Non-Directional Hypothesis Example

When evidence supports a relationship but not direction:

```text
H1:
X is associated with Y.
```

This may be stronger scientifically than inventing direction.

---

# 56. Mediation Hypothesis Example

Conceptually:

```text
H2:
The relationship between X and Y is mediated by M.
```

When possible, make the theoretical process more explicit.

---

# 57. Moderation Hypothesis Example

Conceptually:

```text
H3:
The association between X and Y differs according to Z.
```

Direction of moderation should be stated only if evidence supports it.

---

# 58. Experimental Hypothesis Example

Conceptually:

```text
Participants receiving intervention X will show a greater improvement in Y over the defined follow-up period than participants receiving the comparator.
```

Specify meaningful outcome and time.

---

# 59. Biomedical Mechanism Example

Conceptually:

```text
Increased exposure to X is expected to alter pathway M, resulting in change in outcome Y.
```

Scientific mechanism should support the sequence.

---

# 60. Formulation Research Example

Conceptually:

```text
Increasing polymer concentration is expected to increase viscosity and adhesion while reducing spreadability within the evaluated formulation range.
```

Do not force a named behavioral theory into formulation research.

---

# 61. Validation Hypothesis Example

Conceptually:

```text
The model will retain acceptable discrimination and calibration in an independent population.
```

Specific performance criteria belong to protocol and analysis planning.

---

# 62. Hypothesis Candidate Generation

When several scientifically plausible propositions exist, generate a focused set.

Recommended:

2–4 candidates when alternatives genuinely matter.

Do not generate superficial wording variants.

---

# 63. Hypothesis Candidate Card

For each candidate provide:

## Hypothesis
[...]

## RQ
[...]

## Type
[...]

## Direction
[...]

## Scientific Rationale
[...]

## Theory or Mechanism
[...]

## Empirical Evidence
[...]

## Contradictory Evidence
[...]

## Gap Alignment
[...]

## Novelty Alignment
[...]

## Testability
[...]

## Main Risk
[...]

---

# 64. Candidate Comparison

When useful:

| Hypothesis | RQ Fit | Evidence | Theory/Mechanism | Testability | Novelty Relevance |
|---|---|---|---|---|---|

Do not score mechanically unless useful.

---

# 65. Hypothesis Status

Use:

- `DRAFT_HYPOTHESIS`
- `EVIDENCE_GROUNDED`
- `THEORY_GROUNDED`
- `MECHANISM_GROUNDED`
- `READY_FOR_FRAMEWORK`
- `READY_FOR_DESIGN`
- `REQUIRES_REVISION`
- `HYPOTHESIS_NOT_REQUIRED`

---

# 66. Full Output Structure

When comprehensive hypothesis development is requested, use:

## A. Research Question
[...]

## B. Hypothesis Eligibility
[...]

## C. Theory Prerequisite Status
[...]

## D. Scientific Rationale
[...]

## E. Primary Hypothesis
[...]

## F. Secondary Hypotheses
[...]

## G. Hypothesis Type
[...]

## H. Directional Justification
[...]

## I. Theory or Mechanism
[...]

## J. Supporting Evidence
[...]

## K. Contradictory Evidence
[...]

## L. Gap Alignment
[...]

## M. Novelty Alignment
[...]

## N. Competing Explanations
[...]

## O. Confirmatory vs Exploratory Status
[...]

## P. Testability
[...]

## Q. Design Requirements
[...]

## R. Remaining Uncertainty
[...]

## S. Next Recommended Workflow
[...]

---

# 67. Hypothesis Alignment Matrix

When useful:

| Hypothesis | RQ | Theory/Mechanism | Evidence | Gap | Novelty | Status |
|---|---|---|---|---|---|---|

This may serve as a control document for later framework and methodology stages.

---

# 68. Research Passport Update

When supported, update:

```yaml
hypotheses:
  eligibility:
  theory_prerequisite_status:
  primary:
    id:
    rq:
    proposition:
    type:
    direction:
    theoretical_basis:
    mechanistic_basis:
    empirical_basis:
    contradictory_evidence:
    gap_alignment:
    novelty_alignment:
    confirmatory_status:
    testability:
  secondary:
  competing_hypotheses:
  alternative_explanations:
  design_requirements:
  hypothesis_status:
  next_stage:
```

Unknown fields remain unknown.

---

# 69. Relationship with Research Question Builder

`research-question-builder` determines:

> What must the study ask?

`hypothesis-builder` determines:

> What scientifically justified answer or relationship should be tested, if hypothesis testing is appropriate?

Every hypothesis should trace to a finalized RQ.

Do not allow hypothesis generation to silently change the RQ.

---

# 70. Relationship with Theoretical Framework

When a hypothesis depends on a formal theoretical proposition:

prefer:

```text
research-question-builder
        ↓
theoretical-framework
        ↓
hypothesis-builder
```

When a formal theory is not central, hypotheses may instead be grounded in:

- mechanism;
- established empirical evidence;
- physical principles;
- biological principles.

Do not force theory into every study.

---

# 71. Relationship with Conceptual Framework

When hypotheses specify relationships among constructs, pass them to:

`conceptual-framework`

The conceptual framework may represent:

- direct relationships;
- mechanisms;
- mediators;
- moderators;
- temporal ordering;
- boundary conditions.

The diagram does not replace the written hypotheses.

---

# 72. Relationship with Methodology Architect

Pass to:

`methodology-architect`

the scientific requirements implied by each hypothesis.

Examples include:

- causal design need;
- temporal sequencing;
- comparison structure;
- repeated measurements;
- validation sample;
- mediation timing;
- moderation variation.

Do not choose software here.

---

# 73. Analysis Independence

Do not construct hypotheses to fit a preferred:

- regression;
- SEM;
- PLS-SEM;
- ANOVA;
- machine-learning algorithm.

Analysis follows the hypothesis and design.

---

# 74. SmartPLS and SEM Guard

Do not create:

- H1;
- H2;
- H3;
- mediator hypotheses;
- moderator hypotheses;

simply because SmartPLS or SEM software can estimate them.

Scientific rationale comes before model estimation.

---

# 75. Publication Strategy Independence

Do not construct extra hypotheses merely because:

- another journal article has many hypotheses;
- a target journal often publishes complex SEM models;
- reviewers might prefer a larger model.

Scientific coherence comes first.

---

# 76. Scopus-First Evidence Awareness

The scholarly evidence supporting hypotheses should normally derive from the verified Scopus-first evidence pipeline when applicable.

Use:

`source-verification`

for critical references.

Do not claim evidence strength from unverified citations.

---

# 77. Phenomenon Evidence Boundary

`phenomenon-evidence-builder` may establish:

- prevalence;
- magnitude;
- trend;
- policy context;
- real-world burden.

Such evidence may justify why the research problem matters.

It does not automatically justify:

- hypothesis direction;
- mechanism;
- causality.

Those require scholarly or mechanistic evidence.

---

# 78. Avoid These Behaviors

Do not:

- force hypotheses into every study;
- equate hypotheses with statistical significance;
- create hypotheses from software capabilities;
- invent directional expectations;
- add arbitrary mediators;
- add arbitrary moderators;
- use controls as substantive hypotheses without reason;
- use causal language beyond design capability;
- choose theory after constructing preferred hypotheses;
- hide post-hoc hypotheses as confirmatory;
- create excessive hypotheses;
- claim all hypotheses are novel;
- ignore competing explanations;
- confuse prediction with causation;
- optimize hypothesis structure for a target journal.

---

# Stop Conditions

Do not classify hypotheses as ready for design when:

- the RQ remains unresolved;
- hypothesis testing is inappropriate for the study;
- theory-dependent propositions lack an established theoretical basis;
- direction is unsupported;
- central constructs are undefined;
- mediation lacks mechanistic logic;
- moderation lacks boundary-condition logic;
- causal language exceeds likely design capability;
- hypotheses do not address the validated gap;
- hypotheses contradict audited novelty boundaries;
- testability is inadequate.

Use:

`HYPOTHESIS_REQUIRES_REVISION`

or:

`HYPOTHESIS_NOT_REQUIRED`

when appropriate.

---

# Success Criterion

`hypothesis-builder` succeeds when hypotheses are created only when scientifically appropriate, each proposition is explicitly traceable to a finalized research question and defensible theory, mechanism, or empirical evidence, direction is justified rather than invented, confirmatory and exploratory hypotheses are distinguished, post-hoc theoretical justification is prevented, and the resulting hypotheses are sufficiently precise and testable to guide conceptual-framework and methodology development.