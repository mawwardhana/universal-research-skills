---
name: conceptual-framework
description: Construct a study-specific conceptual framework that organizes the key phenomena, constructs, variables, mechanisms, boundary conditions, contexts, outcomes, and proposed relationships needed to answer finalized research questions and deliver the audited scientific contribution. Use after research-question development and theoretical-framework evaluation when a study benefits from an explicit conceptual model, while avoiding unsupported variables, decorative arrows, arbitrary mediators or moderators, and method-driven model construction.
---

# Conceptual Framework

## Purpose

`conceptual-framework` constructs the study-specific conceptual structure that connects the research problem to the evidence the study intends to generate.

Its central question is:

> What concepts, constructs, mechanisms, contexts, and relationships must this study examine in order to answer the finalized research question and deliver the audited scientific contribution?

The conceptual framework translates:

- scientific evidence;
- theoretical explanation;
- validated gap;
- audited novelty;
- research questions;
- hypotheses where appropriate;

into a coherent study-specific model.

It is not merely a diagram.

---

# Core Principle

Use:

> Every element in the conceptual framework must have a scientific reason to be there.

Do not add:

- variables;
- mediators;
- moderators;
- arrows;
- constructs;
- controls;

merely because:

- they are available in the dataset;
- previous papers included them;
- SEM software allows them;
- a supervisor suggests a complex model;
- more arrows make the study appear sophisticated.

The framework must solve the scientific problem.

---

# Activation Gate

Check upstream status from:

`research-question-builder`

Possible conceptual-framework statuses include:

- `CONCEPTUAL_FRAMEWORK_REQUIRED`
- `CONCEPTUAL_FRAMEWORK_USEFUL`
- `CONCEPTUAL_FRAMEWORK_NOT_NECESSARY`

Proceed when a conceptual framework materially improves:

- study logic;
- construct organization;
- relationship clarity;
- mechanism specification;
- hypothesis structure;
- design planning.

Do not force a conceptual framework into every study.

---

# Studies Commonly Benefiting from a Conceptual Framework

A conceptual framework is often useful for:

- explanatory quantitative studies;
- SEM;
- PLS-SEM;
- mediation studies;
- moderation studies;
- mechanism research;
- behavioral research;
- education research;
- organizational research;
- implementation research;
- mixed-method research;
- multivariable prediction;
- complex intervention development;
- theory-informed qualitative research.

---

# Studies Where a Formal Conceptual Diagram May Be Less Necessary

A formal conceptual framework may be unnecessary for:

- simple prevalence estimation;
- descriptive laboratory characterization;
- some diagnostic-accuracy studies;
- some purely methodological comparisons;
- bibliometric mapping;
- exploratory qualitative studies;
- some systematic reviews;
- straightforward validation studies.

These studies still need scientific logic.

They simply may not require a variable-and-arrow diagram.

---

# 1. Required Upstream Context

Prefer inputs from:

`evidence-synthesis`
→ `sota-builder`
→ `gap-validator`
→ `novelty-auditor`
→ `research-question-builder`
→ `theoretical-framework` when useful
→ `hypothesis-builder` when appropriate

Important inputs include:

- finalized RQ;
- validated gap;
- audited novelty;
- selected theory or mechanistic rationale;
- hypotheses;
- constructs;
- proposed mechanisms;
- boundary conditions;
- target outcomes;
- relevant context;
- contradictory evidence;
- population boundaries;
- temporal logic.

Do not construct the framework from a tentative title alone.

---

# 2. Define the Framework Purpose

Determine what the conceptual framework must accomplish.

Possible purposes include:

- organize constructs;
- explain mechanisms;
- represent hypothesized relationships;
- distinguish predictors and outcomes;
- specify mediators;
- specify moderators;
- show contextual influences;
- organize mixed-method integration;
- structure intervention logic;
- structure implementation determinants;
- guide measurement;
- guide design;
- guide analysis.

Do not include elements unrelated to the purpose.

---

# 3. Start from the Research Question

Every major component should trace back to one or more RQs.

Conceptually:

```text
Research Question
      ↓
Required Concepts
      ↓
Required Relationships
      ↓
Required Evidence
      ↓
Conceptual Framework
```

A construct that does not help answer an RQ should be reconsidered.

---

# 4. Start from the Validated Gap

Ask:

> Which conceptual relationship, mechanism, or uncertainty must be represented to resolve the validated gap?

The framework should make visible:

- what is already established;
- what remains unresolved;
- what this study will test, explore, develop, or validate.

Do not recreate the entire literature landscape.

---

# 5. Incorporate the Audited Novelty

The framework should visibly support the audited novelty when that novelty is:

- conceptual;
- mechanistic;
- theoretical;
- integrative;
- validation-based;
- predictive;
- implementation-oriented;
- contextual with genuine scientific boundary significance.

Ask:

> Which part of the framework represents the actual scientific advancement?

If novelty cannot be located conceptually:

flag:

`NOVELTY_FRAMEWORK_MISALIGNMENT`

---

# 6. Theory-to-Framework Translation

When a theoretical framework exists:

translate only the theoretical components relevant to the study.

Conceptually:

```text
THEORY
Broad explanatory structure

      ↓

SELECTED PROPOSITIONS
Relevant to this study

      ↓

CONCEPTUAL FRAMEWORK
Study-specific constructs and relationships
```

Do not reproduce an entire theory when only part is needed.

---

# 7. No-Theory Conceptual Framework

A conceptual framework may still be legitimate without a formal named theory.

It may be grounded in:

- empirical evidence;
- biological mechanisms;
- pharmacological mechanisms;
- physical principles;
- clinical logic;
- engineering principles;
- implementation logic;
- validated predictive structures.

Use:

`EVIDENCE_DERIVED_CONCEPTUAL_FRAMEWORK`

when appropriate.

Do not force a named theory.

---

# 8. Framework Type

Classify the framework as appropriate:

- `THEORY_DERIVED_FRAMEWORK`
- `MECHANISM_DERIVED_FRAMEWORK`
- `EVIDENCE_DERIVED_FRAMEWORK`
- `PREDICTIVE_FRAMEWORK`
- `VALIDATION_FRAMEWORK`
- `INTERVENTION_FRAMEWORK`
- `IMPLEMENTATION_FRAMEWORK`
- `QUALITATIVE_CONCEPTUAL_FRAMEWORK`
- `MIXED_METHOD_FRAMEWORK`
- `MULTILEVEL_FRAMEWORK`
- `SYSTEMS_FRAMEWORK`
- `FRAMEWORK_NOT_REQUIRED`

The framework type should follow the research problem.

---

# 9. Concept Identification

Identify only concepts needed to answer the RQ.

Possible roles include:

- exposure;
- predictor;
- intervention;
- outcome;
- mediator;
- moderator;
- confounder;
- contextual factor;
- implementation determinant;
- mechanism;
- latent construct;
- observed variable;
- comparison condition;
- temporal factor.

Do not assign roles based on software conventions.

---

# 10. Construct vs Variable

Distinguish:

`CONSTRUCT`

from:

`VARIABLE`

A construct may be theoretical or latent, such as:

- motivation;
- trust;
- learning culture;
- perceived value.

A variable may be directly observed, such as:

- age;
- dosage;
- blood pressure;
- concentration.

Do not use the terms interchangeably when the distinction matters.

---

# 11. Latent Construct

A latent construct is not directly observed.

It is inferred through indicators.

Examples:

- satisfaction;
- perceived quality;
- organizational culture;
- self-efficacy.

Do not classify directly observed demographic or laboratory variables as latent without justification.

---

# 12. Focal Phenomenon

Identify the primary phenomenon or outcome.

Ask:

> What is the principal condition the study seeks to explain, predict, compare, validate, develop, optimize, or understand?

Do not allow multiple unrelated outcomes to compete with the primary RQ.

---

# 13. Predictor or Exposure Identification

Include predictors or exposures only when:

- theoretically justified;
- mechanistically justified;
- empirically supported;
- necessary for the RQ;
- necessary for prediction;
- necessary for adjustment.

Do not include every available variable.

---

# 14. Mechanism Identification

When a mechanism is central:

show the process explicitly.

Example:

```text
X
↓
Mechanism M
↓
Y
```

Mechanism must be scientifically justified.

Do not treat statistical association as mechanism.

---

# 15. Mediator Logic

A mediator answers:

> Through what process might X relate to Y?

Use a mediator only when:

- theory supports it;
- mechanism supports it;
- evidence supports it;
- temporal logic is plausible;
- the validated gap concerns mechanism.

Do not add mediators simply because indirect effects can be estimated.

---

# 16. Moderator Logic

A moderator answers:

> Under what conditions or for whom does the X–Y relationship differ?

Use moderators only when they represent meaningful boundary conditions.

Possible examples:

- age;
- developmental stage;
- environmental exposure;
- organizational support;
- treatment intensity;
- disease status;
- resource availability.

Do not create moderators from arbitrary subgroup availability.

---

# 17. Confounder Logic

A confounder is not the same as a moderator.

Confounders may need adjustment because they threaten valid estimation.

They do not necessarily require hypotheses or central placement in the conceptual framework.

Do not treat every covariate as a substantive construct.

---

# 18. Control Variable Logic

Control variables should be included only when scientifically justified.

Avoid:

`CONTROL_VARIABLE_DUMP`

Do not add controls merely because prior papers used them.

---

# 19. Direct Relationship

Represent:

```text
X → Y
```

only when the study examines a scientifically justified direct relationship.

An arrow does not automatically imply causality.

Specify what the arrow means.

---

# 20. Arrow Semantics

Possible meanings include:

- hypothesized association;
- theoretical influence;
- causal effect;
- predictive relationship;
- mediation pathway;
- temporal sequence;
- process flow.

Every arrow should have an explicit scientific meaning.

Avoid semantic ambiguity.

---

# 21. Causal Arrow Guard

Do not use causal interpretation merely because a diagram contains arrows.

Study design determines causal interpretability.

Use:

`CAUSAL_RELATIONSHIP`

only when:

- causal reasoning is scientifically justified;
- downstream design can support causal inference.

Otherwise use relational or predictive language.

---

# 22. Bidirectional Relationships

Use:

```text
X ↔ Y
```

only when scientific evidence supports reciprocal processes.

Do not use bidirectional arrows merely because variables are correlated.

---

# 23. Feedback Loops

Feedback loops may be appropriate in:

- systems research;
- organizational processes;
- biological regulation;
- implementation science;
- ecological systems.

They require clear scientific justification.

---

# 24. Temporal Ordering

When timing matters, represent it explicitly.

Example:

```text
X at T1
   ↓
M at T2
   ↓
Y at T3
```

This may be more scientifically accurate than a static diagram.

---

# 25. Cross-Sectional Model Guard

Do not depict strong temporal mechanisms when all variables are measured simultaneously without acknowledging limitation.

Cross-sectional structure may represent:

- association;
- covariance;
- exploratory pathway hypotheses.

It should not automatically imply temporal mechanism.

---

# 26. Multiple-Level Frameworks

Some studies involve:

- individual;
- classroom;
- organization;
- hospital;
- region;
- country.

Represent levels explicitly.

Example:

```text
Organizational Context
        ↓
Individual Mechanism
        ↓
Individual Outcome
```

Do not collapse multilevel phenomena into a flat framework.

---

# 27. Ecological Fallacy Guard

Do not infer individual-level relationships from group-level data without justification.

Likewise, do not infer population-level effects automatically from individual-level relationships.

---

# 28. Contextual Framework Components

Context may be represented when it changes:

- mechanism;
- exposure;
- access;
- interpretation;
- implementation;
- effect magnitude;
- generalizability.

Do not include geography merely to make the model appear context-specific.

---

# 29. Population Boundary

The framework should preserve scientifically meaningful population boundaries.

Examples:

- age group;
- disease group;
- educational stage;
- occupational group;
- developmental stage.

Do not treat population itself as novelty unless justified upstream.

---

# 30. Biological Framework

For biomedical or pharmaceutical research, frameworks may include:

- molecular targets;
- biological pathways;
- pharmacokinetics;
- pharmacodynamics;
- biomarkers;
- physiological responses;
- toxicity pathways.

Do not force social-science terminology onto biological mechanisms.

---

# 31. Pharmaceutical Framework

Possible conceptual structure:

```text
Exposure / Dose
      ↓
Pharmacokinetics
      ↓
Target Exposure
      ↓
Pharmacodynamic Response
      ↓
Clinical / Biological Outcome
```

or:

```text
Genetic Variant
      ↓
Protein / Enzyme Function
      ↓
Drug Exposure or Response
      ↓
Clinical Outcome
```

Use only when scientifically relevant.

---

# 32. Formulation and Materials Framework

A conceptual framework may represent:

```text
Material Composition
      ↓
Physicochemical Properties
      ↓
Functional Performance
      ↓
Biological / Practical Outcome
```

Possible properties include:

- viscosity;
- pH;
- adhesion;
- spreadability;
- mechanical strength;
- diffusion;
- release;
- stability.

Do not force a behavioral theory.

---

# 33. Experimental Framework

Experimental frameworks may represent:

```text
Intervention
      ↓
Mechanism
      ↓
Response
```

and relevant comparison conditions.

Do not overcrowd the model with unrelated variables.

---

# 34. Prediction Framework

Predictive frameworks should distinguish:

```text
Predictor Inputs
      ↓
Prediction Model
      ↓
Predicted Outcome
      ↓
Internal Validation
      ↓
External Validation
```

Do not interpret predictor inclusion as causal explanation.

---

# 35. Validation Framework

Validation studies may show:

```text
Existing Model / Instrument
        ↓
Independent Population
        ↓
Validation Performance
```

Novelty may lie in validation rather than new relationships.

---

# 36. Intervention Framework

Intervention research may require:

```text
Intervention
      ↓
Mechanism
      ↓
Primary Outcome
      ↓
Secondary Consequences
```

Context may affect effectiveness.

---

# 37. Implementation Framework

Implementation studies may represent:

- intervention;
- implementation strategy;
- organizational determinants;
- individual determinants;
- implementation outcomes;
- service outcomes;
- clinical outcomes.

Do not confuse implementation outcomes with clinical outcomes.

---

# 38. Qualitative Conceptual Framework

For qualitative research, frameworks may organize:

- sensitizing concepts;
- context;
- process;
- experience;
- meaning;
- interaction.

Do not impose fixed causal arrows when the study is exploratory.

---

# 39. Mixed-Methods Framework

A mixed-method framework may represent:

```text
Quantitative Strand
        ↓
Integration
        ↑
Qualitative Strand
```

or sequential relationships.

The framework should make integration explicit.

---

# 40. Systematic Review Framework

A conceptual framework may help organize:

- intervention;
- mechanism;
- outcome;
- population;
- context;
- evidence categories.

Do not invent empirical relationships that included studies did not test.

---

# 41. Conceptual Framework Evidence Basis

Every important relationship should have a scientific basis.

Possible statuses:

- `THEORY_SUPPORTED`
- `EMPIRICALLY_SUPPORTED`
- `MECHANISTICALLY_SUPPORTED`
- `VALIDATED_MODEL_DERIVED`
- `EXPLORATORY_RELATIONSHIP`
- `USER_PROPOSED`
- `UNSUPPORTED`

Avoid `UNSUPPORTED` relationships in the final framework.

---

# 42. Relationship Evidence Record

When useful, represent:

```yaml
relationship:
  from:
  to:
  role:
  arrow_meaning:
  theoretical_basis:
  mechanistic_basis:
  empirical_basis:
  contradictory_evidence:
  gap_relevance:
  novelty_relevance:
  hypothesis:
  status:
```

Unknown values remain unknown.

---

# 43. Hypothesis Mapping

When hypotheses exist:

each hypothesis should correspond to a relationship in the framework.

Example:

```text
H1
X → Y

H2
X → M → Y

H3
Z moderates X → Y
```

Do not create framework arrows without research logic.

---

# 44. Research Question Mapping

Every primary conceptual relationship should map to an RQ.

Use:

- `DIRECT_RQ_ALIGNMENT`
- `PARTIAL_RQ_ALIGNMENT`
- `NO_RQ_ALIGNMENT`

Remove or reclassify components with no RQ function.

---

# 45. Validated Gap Mapping

The framework should indicate which part addresses the validated gap.

Examples:

If the gap concerns:

`MECHANISM`

highlight:

`M`

If the gap concerns:

`BOUNDARY CONDITION`

highlight:

`Z`

If the gap concerns:

`EXTERNAL VALIDATION`

highlight:

independent validation.

---

# 46. Audited Novelty Mapping

Identify:

- `NOVELTY_NODE`
- `NOVELTY_RELATIONSHIP`
- `NOVELTY_BOUNDARY`
- `NOVELTY_VALIDATION`
- `NOVELTY_MECHANISM`

when useful.

Do not label every component novel.

---

# 47. What Is Not Novel

Preserve upstream novelty boundaries.

Example:

```text
X → Y
Already established

X → M → Y
Mechanism remains unresolved
```

This strengthens scientific positioning.

---

# 48. Framework Parsimony

Prefer the smallest framework that adequately answers the scientific question.

Use:

`PARSIMONIOUS_FRAMEWORK`

Avoid:

`OVERCOMPLEX_FRAMEWORK`

Complexity should be scientifically necessary.

---

# 49. Model Decoration Guard

Reject:

- unnecessary mediators;
- unnecessary moderators;
- unrelated controls;
- repeated constructs;
- decorative arrows;
- duplicated mechanisms.

Ask:

> If this element is removed, does the study lose its ability to answer the RQ or deliver the audited contribution?

If no:

consider removing it.

---

# 50. Variable Availability Bias

Do not include a construct simply because data are already available.

Available data should not silently redefine the research problem.

---

# 51. Instrument Bias

Do not construct the framework around questionnaire items already available.

First define constructs.

Then select or develop measurements downstream.

---

# 52. Software Bias

Do not construct models based on:

- SmartPLS capabilities;
- AMOS;
- SPSS;
- R;
- Jamovi;
- Python.

Software follows the conceptual framework.

The conceptual framework does not follow software.

---

# 53. SEM Bias Guard

Not every conceptual framework requires SEM.

Use the simplest valid analytical approach later.

Do not create latent constructs merely to justify SEM.

---

# 54. PLS-SEM Guard

Do not construct:

- mediators;
- moderators;
- formative constructs;
- second-order constructs;

merely because PLS-SEM supports them.

Scientific rationale comes first.

---

# 55. Machine-Learning Guard

Machine-learning models may include many predictors without representing a causal conceptual framework.

Distinguish:

`PREDICTIVE_FRAMEWORK`

from:

`CAUSAL_EXPLANATORY_FRAMEWORK`

Do not force causal arrows onto predictive features.

---

# 56. Conceptual Definition

For every central construct, provide:

## Construct
[...]

## Conceptual Definition
[...]

## Role in the Study
[...]

## Theoretical, Mechanistic, or Empirical Basis
[...]

Detailed operationalization belongs later to:

`instrument-design`

or:

`methodology-architect`

---

# 57. Construct Boundary

Clarify how related constructs differ.

Example:

```text
Job satisfaction
≠
Work engagement
≠
Organizational commitment
```

Avoid conceptual overlap that creates measurement ambiguity.

---

# 58. Construct Redundancy

If two constructs are conceptually indistinguishable:

flag:

`CONSTRUCT_REDUNDANCY`

Do not retain both simply because separate scales exist.

---

# 59. Construct Definition Conflict

If a construct has incompatible meanings across theories or literatures:

flag:

`CONSTRUCT_DEFINITION_CONFLICT`

Resolve the definition before finalizing the framework.

---

# 60. Conceptual Framework Candidate Generation

When several frameworks could answer the RQ:

generate 2–3 serious candidates.

Possible candidates:

- parsimonious mechanism model;
- theory-extension model;
- validation model;
- multilevel model;
- predictive model.

Do not create superficial variants.

---

# 61. Framework Candidate Card

For each candidate:

## Framework Purpose
[...]

## Main Constructs
[...]

## Core Relationships
[...]

## Theory or Mechanism Basis
[...]

## Gap Alignment
[...]

## Novelty Alignment
[...]

## Hypothesis Alignment
[...]

## Main Strength
[...]

## Main Limitation
[...]

## Complexity
[...]

## Feasibility
[...]

---

# 62. Framework Comparison

When useful:

| Candidate | Gap Fit | Novelty Fit | Theory Fit | Parsimony | Feasibility |
|---|---|---|---|---|---|

Do not select based on complexity.

---

# 63. Framework Status

Use:

- `DRAFT_FRAMEWORK`
- `EVIDENCE_ALIGNED`
- `THEORY_ALIGNED`
- `RQ_ALIGNED`
- `NOVELTY_ALIGNED`
- `READY_FOR_METHOD_DESIGN`
- `REQUIRES_REVISION`
- `FRAMEWORK_NOT_REQUIRED`

---

# 64. Diagram Specification

When a visual framework is requested, define the scientific diagram before rendering.

Record:

- nodes;
- node roles;
- arrows;
- arrow meanings;
- mediators;
- moderators;
- levels;
- context;
- temporal ordering;
- novelty boundary.

Do not generate an attractive but scientifically ambiguous diagram.

---

# 65. Moderator Visualization

Moderation may be represented conceptually as:

```text
X ─────→ Y
    ↑
    Z
```

where Z modifies the X–Y relationship.

Diagram conventions may vary.

The scientific meaning matters more than appearance.

---

# 66. Mediation Visualization

Conceptually:

```text
X → M → Y
```

A direct path:

```text
X → Y
```

may also be shown when scientifically relevant.

Do not infer full or partial mediation before data are analyzed.

---

# 67. Control Visualization

Control variables do not always need prominent placement in the main conceptual diagram.

They may instead appear in:

- methodology;
- adjustment plan;
- analysis plan.

Keep the central contribution visually clear.

---

# 68. Multilevel Visualization

When levels differ, make them visible.

Example:

```text
ORGANIZATION LEVEL
Organizational Support
        ↓

INDIVIDUAL LEVEL
Motivation
        ↓
Performance
```

Do not hide clustering or hierarchy when it is scientifically central.

---

# 69. Conceptual Framework Narrative

A narrative should explain:

1. focal phenomenon;
2. central constructs;
3. relationships;
4. mechanisms;
5. boundary conditions;
6. gap relevance;
7. novelty relevance;
8. alternative explanations.

Avoid merely describing where boxes appear in the diagram.

---

# 70. Framework Narrative Logic

Use when appropriate:

```text
Existing evidence establishes X → Y
        ↓
Current mechanism remains unresolved
        ↓
Theory or mechanism proposes M
        ↓
Study examines X → M → Y
        ↓
Context Z may alter the pathway
```

Only when evidence supports these elements.

---

# 71. Framework–Method Separation

The conceptual framework identifies:

> what must be studied.

`methodology-architect` determines:

> how it should be studied.

Do not include:

- sample size;
- statistical tests;
- software choices;

inside the conceptual framework unless conceptually relevant.

---

# 72. Framework–Analysis Separation

An arrow does not automatically determine:

- regression;
- SEM;
- PLS-SEM;
- mediation software;
- machine learning.

Analysis is selected later based on:

- design;
- measurement;
- data structure;
- assumptions;
- inferential objective.

---

# 73. Framework–Measurement Separation

A construct may be conceptually valid before an instrument is selected.

Do not choose constructs merely because validated questionnaires happen to exist.

Measurement comes downstream.

---

# 74. Framework–Sampling Separation

Sampling decisions should reflect:

- population;
- inference;
- study design;
- practical feasibility.

Sampling should not redefine the conceptual model.

---

# 75. Framework Falsifiability

Where appropriate, ask:

> What evidence would show that this proposed relationship is unsupported?

The framework should permit empirical challenge.

---

# 76. Alternative Explanations

Identify credible alternative explanations.

Example:

```text
Preferred:
X → Y

Alternative:
C → X
C → Y
```

This may reveal confounding or competing mechanism.

Do not assume the preferred model is the only explanation.

---

# 77. Competing Model Awareness

When scientific evidence supports alternative structures, preserve them.

Possible examples:

- direct effect vs mediation;
- reciprocal relationship;
- alternative mediator;
- competing theoretical mechanism.

Do not choose the preferred model solely because it is easier to analyze.

---

# 78. Framework Confidence

Use:

- `HIGH_CONFIDENCE`
- `MODERATE_CONFIDENCE`
- `LOW_CONFIDENCE`
- `EXPLORATORY`

Confidence depends on:

- theory strength;
- empirical support;
- gap validation;
- novelty audit;
- construct clarity;
- mechanism plausibility;
- contradictory evidence.

---

# 79. Phenomenon Evidence Boundary

`phenomenon-evidence-builder` may support:

- magnitude;
- prevalence;
- incidence;
- burden;
- trend;
- policy context;
- regulatory context;
- institutional conditions.

This evidence can establish:

> Why does the research problem matter in the real world?

It does not automatically justify:

- conceptual relationships;
- theoretical mechanisms;
- causal arrows;
- mediators;
- moderators;
- novelty.

Maintain:

```text
Phenomenon Evidence
= authority-first real-world evidence

Conceptual Relationship Evidence
= theory / mechanism / scholarly evidence
```

---

# 80. Scopus-First Evidence Awareness

Relationships in the conceptual framework should preferably be grounded in the verified scholarly evidence pipeline when applicable.

Use:

`scopus-literature-search`
→ `source-verification`
→ `evidence-synthesis`

Do not introduce unsupported relationships at the framework stage.

---

# 81. Target-Journal Independence

Do not add constructs or relationships because:

- a target journal frequently publishes them;
- reviewers may recognize them;
- they make the framework resemble recent papers.

Scientific logic comes first.

---

# 82. APC Independence

Publication-cost preferences have no role in conceptual-framework construction.

Do not alter the scientific model for publication economics.

---

# 83. Comprehensive Output Structure

When full conceptual-framework development is requested, use:

## A. Research Question
[...]

## B. Validated Gap
[...]

## C. Audited Novelty
[...]

## D. Framework Purpose
[...]

## E. Framework Type
[...]

## F. Theoretical or Mechanistic Basis
[...]

## G. Core Constructs
[...]

## H. Construct Definitions
[...]

## I. Construct Roles
[...]

## J. Proposed Relationships
[...]

## K. Arrow Meanings
[...]

## L. Mechanisms
[...]

## M. Mediators
[...]

## N. Moderators
[...]

## O. Confounders
[...]

## P. Contextual Factors
[...]

## Q. Temporal Structure
[...]

## R. Levels
[...]

## S. Hypothesis Mapping
[...]

## T. Research Question Mapping
[...]

## U. Gap Mapping
[...]

## V. Novelty Mapping
[...]

## W. Alternative Explanations
[...]

## X. Conceptual Diagram Specification
[...]

## Y. Conceptual Framework Narrative
[...]

## Z. Framework Limitations
[...]

## Framework Status
[...]

## Next Recommended Step
[...]

---

# 84. Compact Construct Table

When useful:

| Construct | Definition | Role | Evidence Basis | RQ |
|---|---|---|---|---|

---

# 85. Relationship Table

When useful:

| From | To | Relationship | Arrow Meaning | Basis | Hypothesis | Novelty |
|---|---|---|---|---|---|---|

---

# 86. Research Passport Update

When supported, update:

```yaml
conceptual_framework:
  need_status:
  purpose:
  framework_type:
  theory_basis:
  mechanism_basis:
  constructs:
    - name:
      definition:
      role:
      evidence_basis:
  relationships:
    - from:
      to:
      type:
      arrow_meaning:
      basis:
      hypothesis:
      rq:
  mechanisms:
  mediators:
  moderators:
  confounders:
  contextual_factors:
  temporal_structure:
  levels:
  gap_mapping:
  novelty_mapping:
  alternative_explanations:
  parsimony_status:
  confidence:
  framework_status:
  next_stage:
```

Unknown values remain unknown.

---

# 87. User-Friendly Behavior

Prefer:

> The direct X–Y relationship is already established, so it should not dominate the framework as though it were new. The key contribution is the proposed mechanism M. M should therefore occupy the central conceptual position.

Or:

> The study does not need several moderators merely because the dataset contains them. Only Z has a clear scientific role as a boundary condition.

Or:

> This formulation study is better represented as composition → physicochemical properties → functional performance than by forcing a behavioral theory.

---

# 88. Avoid These Behaviors

Do not:

- create frameworks from variables alone;
- create arrows without scientific basis;
- add mediators arbitrarily;
- add moderators arbitrarily;
- confuse confounders with moderators;
- use theory decoratively;
- create complexity to justify SEM;
- let SmartPLS determine the framework;
- force causal interpretation;
- include every available variable;
- ignore alternative explanations;
- confuse framework with methodology;
- claim every element as novel;
- optimize the model for a target journal;
- treat official statistics as evidence of mechanism;
- convert predictive features into causal variables without justification.

---

# Stop Conditions

Do not classify a framework as ready for methodology when:

- the RQ remains unresolved;
- validated gap and framework do not align;
- audited novelty cannot be located in the framework;
- central constructs remain undefined;
- critical relationships lack scientific basis;
- mediator logic is weak;
- moderator logic is weak;
- construct overlap remains unresolved;
- arrow meanings are ambiguous;
- temporal ordering is scientifically inconsistent;
- framework complexity exceeds scientific necessity.

Use:

`CONCEPTUAL_FRAMEWORK_REQUIRES_REVISION`

or:

`FRAMEWORK_NOT_REQUIRED`

when appropriate.

---

# Relationship with Research Question Builder

`research-question-builder` determines:

> What must the study ask?

`conceptual-framework` determines:

> What study-specific concepts, mechanisms, and relationships must be organized in order to answer that question?

Every central framework element should trace to an RQ.

Do not allow the framework to silently create new research questions.

---

# Relationship with Theoretical Framework

`theoretical-framework` asks:

> Why should the phenomenon or relationship occur?

`conceptual-framework` asks:

> How will this specific study organize and investigate the relevant constructs, mechanisms, boundaries, and relationships?

The conceptual framework may use:

- all;
- part;
- or none;

of a formal theory depending on the scientific problem.

Do not reproduce theory mechanically.

---

# Relationship with Hypothesis Builder

When hypotheses exist:

the conceptual framework provides their structural representation.

Conceptually:

```text
Theoretical or Mechanistic Proposition
        ↓
Hypothesis
        ↓
Conceptual Relationship
```

The diagram does not replace written hypotheses.

Do not add framework relationships that contradict finalized hypotheses without explicit revision.

---

# Relationship with Methodology Architect

A finalized conceptual framework should pass to:

`methodology-architect`

explicit information about:

- constructs;
- variables;
- relationships;
- mechanisms;
- temporal logic;
- population boundaries;
- levels;
- contextual conditions;
- evidence requirements;
- causal vs associative interpretation.

Methodology then determines:

- study design;
- measurement;
- sampling;
- data collection;
- analytical approach.

Do not choose statistical software at the conceptual-framework stage.

---

# Relationship with Instrument Design

Central constructs requiring measurement may later route to:

`instrument-design`

The conceptual framework determines:

> what needs to be measured.

`instrument-design` determines:

> how it can be validly measured.

Do not select constructs because convenient instruments already exist.

---

# Relationship with Analysis Planner

The conceptual framework may inform:

- required comparisons;
- mediation structure;
- moderation structure;
- temporal sequence;
- multilevel structure;
- prediction objective.

However:

`analysis-planner`

must still determine the appropriate analytical strategy from:

- RQ;
- design;
- measurement;
- data structure;
- assumptions.

Do not convert arrows automatically into statistical models.

---

# Success Criterion

`conceptual-framework` succeeds when the finalized research question, validated gap, audited novelty, relevant theory or mechanism, constructs, relationships, boundary conditions, hypotheses, temporal logic, and contextual structure have been translated into the smallest scientifically adequate study-specific framework, with every element evidence-justified, clearly defined, semantically explicit, and ready to guide methodology without allowing available variables, statistical software, publication strategy, or unnecessary complexity to redefine the research problem.