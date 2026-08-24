---
name: theoretical-framework
description: Identify, evaluate, compare, select, adapt, and integrate scientific theories or legitimate disciplinary explanatory structures that can explain finalized research questions, validated gaps, audited novelty, mechanisms, constructs, or expected relationships. Use when theory is required or useful for explanatory, mechanism, hypothesis-driven, conceptual, mixed-method, or theory-testing research, but do not force a formal named theory when the scientific problem is primarily descriptive, exploratory, methodological, validation-oriented, or otherwise does not require one.
---

# Theoretical Framework

## Purpose

`theoretical-framework` determines whether explicit theoretical grounding is scientifically needed and, when appropriate, constructs a defensible explanation for the study.

Its central question is:

> Which established or emerging theoretical explanation, mechanism, model, or disciplinary principle best explains the phenomenon, relationship, or boundary condition that this study intends to investigate?

A theoretical framework should help explain:

- why a phenomenon occurs;
- why constructs or variables may relate;
- why a mechanism is plausible;
- when a relationship may change;
- how competing explanations differ;
- what theoretical proposition the study will test, extend, refine, challenge, or delimit.

The purpose is not to decorate a study with theory.

---

# Core Principle

Use:

> Theory should solve an explanatory need.

Do not add theory merely because:

- a manuscript template contains a theory section;
- a supervisor requests a named theory;
- SEM will be used;
- PLS-SEM will be used;
- many variables exist;
- a conceptual diagram needs arrows;
- a journal frequently publishes theory-driven studies.

A theoretical framework must contribute scientifically.

---

# Activation Gate

Check upstream output from:

`research-question-builder`

Possible statuses include:

- `THEORETICAL_FRAMEWORK_REQUIRED`
- `THEORETICAL_FRAMEWORK_USEFUL`
- `THEORETICAL_FRAMEWORK_NOT_CENTRAL`
- `UNKNOWN`

When:

`THEORETICAL_FRAMEWORK_REQUIRED`

construct an explicit framework.

When:

`THEORETICAL_FRAMEWORK_USEFUL`

evaluate whether theory materially improves explanation.

When:

`THEORETICAL_FRAMEWORK_NOT_CENTRAL`

do not force a formal theory.

---

# Common Cases Where Theory Is Useful

Theory is often useful for:

- explanatory research;
- mechanism research;
- behavioral research;
- social-science research;
- education research;
- organizational research;
- theory-testing research;
- mediation studies;
- moderation studies;
- implementation research;
- some intervention studies;
- some mixed-method studies.

---

# Common Cases Where Formal Theory May Be Less Central

A named theory may be unnecessary for:

- descriptive epidemiology;
- exploratory discovery;
- initial laboratory characterization;
- formulation development;
- some experimental material studies;
- purely methodological comparison;
- many diagnostic-accuracy studies;
- some validation studies;
- bibliometric mapping;
- early-stage biomedical discovery;
- some systematic reviews.

These studies may still require:

- mechanistic reasoning;
- empirical logic;
- biological models;
- physical principles;
- conceptual frameworks;

without requiring a formal named theory.

---

# 1. Required Upstream Context

Prefer inputs from:

`evidence-synthesis`
→ `sota-builder`
→ `gap-validator`
→ `novelty-auditor`
→ `research-question-builder`

and, where already appropriate:

`hypothesis-builder`

Important inputs include:

- finalized RQ;
- validated gap;
- audited novelty;
- question orientation;
- proposed mechanisms;
- constructs;
- boundary conditions;
- contradictory evidence;
- expected contribution;
- research maturity;
- context.

Do not select theory independently of the research problem.

---

# 2. Define the Explanatory Need

Before searching for theory, determine what must be explained.

Possible explanatory needs include:

- behavior;
- adoption;
- learning;
- motivation;
- decision making;
- biological mechanism;
- pharmacological mechanism;
- organizational change;
- technology acceptance;
- health behavior;
- implementation;
- social interaction;
- developmental process;
- material behavior;
- physiological response;
- system behavior.

Do not begin from a favorite theory.

---

# 3. Explanatory Structure Type

Determine what type of explanatory structure is legitimate for the discipline.

Possible types:

- `FORMAL_SCIENTIFIC_THEORY`
- `MIDDLE_RANGE_THEORY`
- `DOMAIN_SPECIFIC_THEORY`
- `MECHANISTIC_MODEL`
- `BIOLOGICAL_PATHWAY`
- `PHARMACOLOGICAL_MODEL`
- `PHYSICAL_PRINCIPLE`
- `ENGINEERING_MODEL`
- `MATHEMATICAL_MODEL`
- `EMPIRICALLY_DERIVED_EXPLANATORY_MODEL`
- `INTERPRETIVE_LENS`
- `FORMAL_THEORY_NOT_REQUIRED`

Do not force social-science theory conventions onto biomedical, pharmaceutical, engineering, or physical-science research.

---

# 4. Theory Search

When an appropriate theory is not already established, search scholarly literature for:

- original theory papers;
- seminal theoretical publications;
- authoritative books when essential;
- current theory reviews;
- theory-testing studies;
- theory refinements;
- competing theories;
- critiques;
- failed replications;
- boundary-condition studies.

Integrate with:

`scopus-literature-search`

and, where necessary:

`citation-chaining`

Do not claim a theory is established merely because many papers mention it.

---

# 5. Original Theory Source

When a named theory is used, identify the original or authoritative source where possible.

Record:

- theory name;
- original author or authors;
- original publication;
- core propositions;
- original domain;
- original assumptions.

Do not attribute a theory to a later review merely because that review discusses it.

---

# 6. Theory Evolution

Trace important refinements where relevant.

Conceptually:

```text
Original Theory
      ↓
Major Refinement
      ↓
Empirical Testing
      ↓
Critique
      ↓
Boundary Conditions
      ↓
Current Form
```

Do not assume the original version remains unchanged.

---

# 7. Current Theory Form

Determine whether the theory currently exists as:

- original formulation;
- revised formulation;
- extended formulation;
- integrated model;
- domain-specific adaptation.

Use the version scientifically appropriate to the current study.

Do not silently mix propositions from incompatible versions.

---

# 8. Candidate Theory Identification

Generate a focused set of candidate theories when alternatives genuinely exist.

Recommended:

2–4 serious candidates.

For each candidate identify:

- explanatory target;
- core constructs;
- assumptions;
- expected relationships;
- mechanism;
- empirical support;
- domain fit;
- known limitations;
- boundary conditions.

Do not generate long lists of loosely related theories.

---

# 9. Theory Candidate Card

For each candidate:

## Theory
[...]

## Core Proposition
[...]

## Original Source
[...]

## Current Form
[...]

## Constructs
[...]

## What It Explains
[...]

## Mechanism
[...]

## Assumptions
[...]

## Boundary Conditions
[...]

## Fit with Research Question
[...]

## Fit with Validated Gap
[...]

## Fit with Audited Novelty
[...]

## Relevant Evidence
[...]

## Contradictory Evidence
[...]

## Known Limitations
[...]

## Main Risk
[...]

---

# 10. Theory Selection Criteria

Evaluate candidate theories using:

1. explanatory relevance;
2. empirical support;
3. construct alignment;
4. context relevance;
5. compatibility with the RQ;
6. ability to explain the validated gap;
7. ability to support the audited novelty;
8. mechanistic plausibility;
9. boundary-condition fit;
10. parsimony.

Do not select theory because it is famous.

---

# 11. Theory Fit Status

Use:

- `STRONG_THEORY_FIT`
- `MODERATE_THEORY_FIT`
- `PARTIAL_THEORY_FIT`
- `WEAK_THEORY_FIT`
- `THEORY_NOT_NEEDED`

---

# 12. Competing Theories

When two theories provide different explanations, preserve the competition.

Possible outcomes:

- one theory selected;
- theories explicitly compared;
- competing hypotheses developed;
- integrative framework justified.

Do not combine theories automatically.

---

# 13. Theory Integration

Use multiple theories only when each contributes a distinct and necessary explanatory function.

Example:

```text
Theory A
explains individual mechanism

+

Theory B
explains contextual boundary
```

Integration requires:

- non-redundant contribution;
- conceptual compatibility;
- explicit integration logic.

Do not stack theories merely to increase academic complexity.

---

# 14. Theory Redundancy Guard

If two theories explain essentially the same mechanism:

prefer the more appropriate, parsimonious, or better-supported framework.

Flag unnecessary combinations as:

`THEORY_STACKING`

Do not retain redundant theories without scientific benefit.

---

# 15. Theory Scope

Determine whether the theory is:

- broad;
- middle-range;
- domain-specific;
- mechanism-specific.

Use the narrowest framework that adequately explains the scientific problem.

Do not invoke grand theory when a precise explanatory structure exists.

---

# 16. Theory Assumptions

Identify important assumptions.

Examples:

- rational decision making;
- social interaction;
- individual agency;
- resource availability;
- environmental stability;
- biological pathway integrity;
- equilibrium conditions.

Ask whether these assumptions fit the target study.

---

# 17. Theory Boundary Conditions

Identify circumstances under which the theory may or may not operate.

Possible boundaries include:

- population;
- age;
- developmental stage;
- disease status;
- institutional setting;
- cultural context;
- resource conditions;
- technological conditions;
- exposure range;
- environmental conditions.

Boundary conditions may themselves constitute part of the validated gap.

---

# 18. Theory and Context

Do not assume a theory validated in one context automatically generalizes everywhere.

But do not claim a gap simply because the location differs.

Ask whether contextual differences change:

- assumptions;
- construct meaning;
- mechanism;
- boundary conditions;
- expected direction;
- expected magnitude.

---

# 19. Theory and Mechanism

A theoretical framework should identify explanatory mechanisms when appropriate.

Conceptually:

```text
Construct X
      ↓
Theoretical Mechanism
      ↓
Construct Y
```

A mechanism is not merely:

> X statistically predicts Y.

Do not label simple association as mechanism.

---

# 20. Theory and Mediators

A mediator should correspond to a theoretically or mechanistically meaningful process.

Ask:

> Why should X change M?

and:

> Why should M change Y?

If these questions cannot be answered scientifically:

the mediation proposition may be weak.

---

# 21. Theory and Moderators

A moderator should represent a meaningful boundary condition.

Ask:

> Why should the X–Y relationship differ depending on Z?

Do not use theory post hoc to justify arbitrary interactions.

---

# 22. Theory and Temporal Logic

If theory implies temporal sequence:

make the sequence explicit.

Example:

```text
X at T1
↓
Mechanism at T2
↓
Y at T3
```

Do not claim a strongly temporal mechanism from simultaneous measurement without caution.

---

# 23. Theory and Causal Language

Theory may propose causality.

Study design determines whether causal inference can be supported empirically.

Do not let theoretical arrows automatically justify causal conclusions.

---

# 24. Theory and Prediction

A theory may explain relationships without generating strong out-of-sample prediction.

Distinguish:

- explanatory theory;
- predictive model.

Do not assume a theory-driven model will necessarily predict well.

---

# 25. Theory and Validation Research

Validation research may use theory to explain:

- expected generalizability;
- invariance;
- boundary conditions;
- model transportability.

But external validation does not always require new theory.

Do not force theory into straightforward validation.

---

# 26. Theory and Experimental Research

For experimental studies, theory or mechanism may explain:

- manipulation logic;
- expected response;
- dose-response;
- mechanism;
- boundary conditions.

The design must meaningfully test the proposition.

---

# 27. Biomedical and Pharmaceutical Frameworks

In biomedical or pharmaceutical research, theoretical grounding may take the form of:

- biological pathways;
- receptor models;
- molecular interaction models;
- pharmacokinetic models;
- pharmacodynamic models;
- physiological mechanisms;
- disease-mechanism models.

A named behavioral theory is not required.

Use the discipline's legitimate explanatory structure.

---

# 28. Formulation and Materials Research

For formulation or materials studies, explanatory grounding may derive from:

- polymer science;
- rheology;
- diffusion;
- thermodynamics;
- intermolecular interactions;
- material structure-property relationships.

Conceptually:

```text
Composition
      ↓
Material Property
      ↓
Functional Behavior
      ↓
Observed Outcome
```

Do not force unrelated formal theory.

---

# 29. Engineering and Physical Sciences

Theoretical frameworks may derive from:

- physical laws;
- system models;
- engineering principles;
- mathematical formulations;
- material-behavior mechanisms.

Use legitimate disciplinary reasoning.

---

# 30. Education and Social Sciences

Formal theories may be especially useful for explaining:

- cognition;
- behavior;
- motivation;
- learning;
- social interaction;
- institutions;
- culture;
- organizational processes.

Theory selection must still remain evidence-based.

---

# 31. Qualitative Research

Qualitative studies may use theory as:

- sensitizing framework;
- interpretive lens;
- deductive coding framework;
- comparative explanatory structure.

Some qualitative approaches intentionally delay theoretical commitment.

Respect methodological tradition.

Do not force theory testing where the design is theory-generating.

---

# 32. Mixed-Methods Research

Theory may connect:

- quantitative hypotheses;
- qualitative exploration;
- integration.

Use theory only when it genuinely supports the relevant evidence strands or their integration.

---

# 33. Systematic Review and Meta-Analysis

A systematic review may:

- synthesize theory use;
- compare theoretical explanations;
- identify theory gaps.

It does not always need a new theoretical framework.

A meta-analysis may test theory-derived moderators when justified.

---

# 34. Theoretical Proposition

For each selected theory or explanatory structure, identify relevant propositions.

Recommended structure:

```yaml
theoretical_proposition:
  theory_or_model:
  proposition:
  construct_a:
  mechanism:
  construct_b:
  boundary_condition:
  supporting_evidence:
  contradictory_evidence:
```

Unknown values remain unknown.

---

# 35. Theory–RQ Alignment

Audit:

```text
Research Question
      ↕
Theoretical Explanation
```

Use:

- `DIRECT_THEORY_RQ_ALIGNMENT`
- `PARTIAL_ALIGNMENT`
- `WEAK_ALIGNMENT`
- `MISALIGNED`

A theory that cannot explain the RQ should not be central.

---

# 36. Theory–Gap Alignment

Ask:

> Does this theoretical framework clarify why the validated uncertainty exists?

Possible roles:

- theory is incomplete;
- theory predicts contradictory evidence;
- mechanism remains unresolved;
- boundary condition remains untested;
- theoretical assumptions may not hold.

If theory is unrelated to the validated gap:

downgrade its importance.

---

# 37. Theory–Novelty Alignment

Ask:

> Does the audited novelty test, extend, refine, integrate, delimit, or challenge the theory?

Classify:

- `THEORY_TEST`
- `THEORY_EXTENSION`
- `THEORY_REFINEMENT`
- `THEORY_BOUNDARY_TEST`
- `THEORY_INTEGRATION`
- `THEORY_CHALLENGE`
- `THEORY_CONTEXT_APPLICATION`
- `NO_THEORETICAL_NOVELTY`

Do not invent theoretical novelty when the actual contribution is:

- empirical;
- methodological;
- validation-based;
- translational.

---

# 38. Theory–Hypothesis Alignment

Each theory-driven hypothesis should be traceable to a theoretical proposition.

Conceptually:

```text
Theory Proposition
      ↓
Expected Relationship
      ↓
Hypothesis
```

Do not reverse-engineer theory after preferred hypotheses have already been chosen.

---

# 39. Theory-Before-Hypothesis Rule

When a hypothesis depends on a specific theoretical proposition:

prefer:

```text
research-question-builder
        ↓
theoretical-framework
        ↓
hypothesis-builder
```

Do not prefer:

```text
research-question-builder
        ↓
hypothesis-builder
        ↓
search for theory afterward
```

Use:

`THEORY_READY_FOR_HYPOTHESIS`

when the required theoretical propositions are sufficiently established.

Use:

`THEORETICAL_FRAMEWORK_REQUIRES_REVISION`

when they are not.

---

# 40. Non-Theory Hypothesis Path

A hypothesis does not always require a formal named theory.

It may be grounded in:

- biological mechanisms;
- pharmacological mechanisms;
- physical principles;
- robust empirical evidence;
- validated scientific models.

When formal theory is not needed:

use:

`FORMAL_THEORY_NOT_REQUIRED`

Do not invent theory merely to justify a hypothesis.

---

# 41. Theory–Construct Alignment

Ensure construct definitions match the selected theory.

Do not combine constructs from multiple theories while silently changing their meanings.

Use:

`CONSTRUCT_DEFINITION_CONFLICT`

when necessary.

---

# 42. Theory Adaptation

A theory may be used through:

- application;
- adaptation;
- extension;
- refinement;
- modification.

Distinguish these explicitly.

Do not call routine application a theory extension.

---

# 43. Theory Modification

Theory modification requires evidence that the original framework is insufficient.

Possible reasons include:

- missing construct;
- missing mechanism;
- failed prediction;
- new boundary condition;
- systematic contradictory evidence.

Do not modify theory simply to fit available variables.

---

# 44. Theory Falsifiability

Where appropriate, identify:

> What evidence would be inconsistent with this theoretical explanation?

The framework should permit empirical challenge.

---

# 45. Confirmation Bias Guard

Do not select only theories supporting the preferred hypothesis.

Search for:

- competing theories;
- theoretical criticism;
- failed replications;
- boundary-condition failures;
- contradictory evidence.

---

# 46. Theory Evidence Strength

Classify support as:

- `STRONG_THEORETICAL_SUPPORT`
- `MODERATE_THEORETICAL_SUPPORT`
- `LIMITED_THEORETICAL_SUPPORT`
- `CONTESTED_THEORY`
- `THEORY_SUPPORT_UNCLEAR`

Do not equate citation count with theoretical validity.

---

# 47. Theory Maturity

Possible statuses:

- `FOUNDATIONAL`
- `MATURE`
- `DEVELOPING`
- `EMERGING`
- `CONTESTED`

This helps distinguish:

- theory testing;
- theory refinement;
- theory building.

---

# 48. Seminal vs Current Evidence

A theoretical framework should often integrate:

```text
Original Theory Source
+
Major Refinements
+
Current Empirical Evidence
+
Current Critique
```

Do not rely only on the original publication when the theory has evolved substantially.

---

# 49. Scopus-First Theory Evidence

Prefer verified scholarly evidence for:

- theory testing;
- theory refinement;
- current applications;
- current critiques.

Seminal theory sources may:

- predate Scopus;
- be books;
- come from foundational publications outside current indexing.

Retain them when scientifically essential.

---

# 50. Citation Chaining for Theory

Use:

`citation-chaining`

to trace:

- original theory;
- major refinements;
- critiques;
- later empirical applications;
- competing theories.

This reduces incorrect secondary attribution.

---

# 51. Theory Source Verification

Critical theoretical sources should pass:

`source-verification`

where applicable.

Maintain:

```text
Claim
↓
Theory Source
↓
Verified Reference
```

Do not cite secondary descriptions as if they were the original theory source.

---

# 52. Theory Comparison Matrix

When multiple candidates exist:

| Theory | Explains RQ | Gap Fit | Mechanism Fit | Evidence Support | Boundary Fit | Limitations | Overall Fit |
|---|---|---|---|---|---|---|---|

Do not select theory based solely on popularity.

---

# 53. Theory Selection Output

State explicitly:

## Selected Theory or Explanatory Structure
[...]

## Why It Fits
[...]

## Original Source
[...]

## Current Form
[...]

## Core Proposition
[...]

## Constructs Used
[...]

## Mechanism
[...]

## Assumptions
[...]

## Boundary Conditions
[...]

## Supporting Evidence
[...]

## Contradictory Evidence
[...]

## Limitations
[...]

## Role in This Study
[...]

---

# 54. No-Theory Outcome

A legitimate output may be:

`FORMAL_THEORY_NOT_REQUIRED`

When this occurs, explain what guides the study instead.

Possible alternatives include:

- biological mechanism;
- mechanistic rationale;
- empirical framework;
- physical model;
- clinical logic;
- validated predictive model;
- methodological framework;
- conceptual framework.

Do not treat absence of a formal named theory as academic weakness automatically.

---

# 55. Theoretical Framework Narrative

When writing the framework narrative, use:

```text
Theory or explanatory model origin
      ↓
Core propositions
      ↓
Current evidence
      ↓
Relevant mechanism
      ↓
Application to current RQ
      ↓
Gap or boundary
      ↓
Expected contribution
```

Avoid textbook-style descriptions unrelated to the study.

---

# 56. Theory Paragraph Guard

Do not write several paragraphs explaining theory without connecting it to:

- RQ;
- constructs;
- mechanisms;
- hypotheses;
- validated gap;
- audited novelty.

Every theoretical section should serve the study.

---

# 57. Theoretical Framework Diagram

A theoretical diagram may show:

```text
Theory
  ↓
Construct A
  ↓
Mechanism
  ↓
Construct B
```

or more complex relationships where justified.

Do not create arrows unsupported by theoretical propositions.

---

# 58. Theory vs Conceptual Framework

Distinguish:

```text
THEORETICAL FRAMEWORK
Why should the phenomenon or relationship occur?

CONCEPTUAL FRAMEWORK
How will this specific study organize and investigate
the relevant constructs, mechanisms, and boundaries?
```

They may overlap.

They are not identical.

---

# 59. Comprehensive Output Structure

When comprehensive development is requested, use:

## A. Explanatory Need
[...]

## B. Theory Requirement Status
[...]

## C. Candidate Theories or Explanatory Models
[...]

## D. Theory Comparison
[...]

## E. Selected Theory or Explanatory Structure
[...]

## F. Original and Current Sources
[...]

## G. Core Constructs
[...]

## H. Core Propositions
[...]

## I. Mechanism
[...]

## J. Assumptions
[...]

## K. Boundary Conditions
[...]

## L. Empirical Support
[...]

## M. Contradictory Evidence
[...]

## N. Fit with Validated Gap
[...]

## O. Fit with Audited Novelty
[...]

## P. Fit with Research Questions
[...]

## Q. Fit with Hypotheses
[...]

## R. Theoretical Contribution
[...]

## S. Limitations
[...]

## T. Next Recommended Step
[...]

---

# 60. Research Passport Update

When supported, update:

```yaml
theoretical_framework:
  need_status:
  explanatory_need:
  framework_type:
  candidate_theories:
  selected_theory_or_model:
  original_source:
  current_sources:
  core_constructs:
  propositions:
  mechanism:
  assumptions:
  boundary_conditions:
  empirical_support:
  contradictory_evidence:
  theory_maturity:
  rq_alignment:
  gap_alignment:
  novelty_alignment:
  hypothesis_alignment:
  theoretical_contribution:
  limitations:
  confidence:
  next_stage:
```

Unknown values remain unknown.

---

# 61. Framework Confidence

Use:

- `HIGH_CONFIDENCE`
- `MODERATE_CONFIDENCE`
- `LOW_CONFIDENCE`
- `CONTESTED`
- `NOT_APPLICABLE`

Confidence should reflect:

- source quality;
- empirical support;
- construct fit;
- mechanism fit;
- boundary fit;
- competing explanations.

---

# 62. Phenomenon Evidence Boundary

`phenomenon-evidence-builder` may establish:

- magnitude;
- prevalence;
- incidence;
- burden;
- trend;
- policy context;
- regulatory context;
- institutional conditions.

Such evidence may establish why a problem matters.

It does not automatically establish:

- theory;
- mechanism;
- hypothesis direction;
- scientific gap;
- novelty.

Maintain:

```text
Phenomenon Evidence
= authority-first real-world evidence

Theoretical Evidence
= scholarly explanatory evidence
```

---

# 63. Publication Strategy Independence

Do not choose a theory merely because:

- the target journal frequently publishes it;
- reviewers may recognize it;
- it makes the manuscript appear sophisticated.

Scientific explanatory fit comes first.

---

# 64. APC Independence

Publication-cost preferences have no role in theory selection.

Do not allow APC considerations to influence theoretical evidence.

---

# 65. User-Friendly Behavior

Prefer:

> This study does not need a theory merely because it uses SEM. Theory X is useful only if it genuinely explains why construct A should influence B through mechanism M.

Or:

> A formal named theory is not necessary here. The study is primarily an external-validation study, so the scientific logic is better grounded in the established model and its expected generalizability.

Or:

> In this pharmaceutical formulation study, a mechanistic structure-property explanation is more appropriate than forcing a behavioral theory.

---

# 66. Avoid These Behaviors

Do not:

- force theory into every study;
- choose theory because it is famous;
- choose theory merely because another paper used it;
- stack multiple theories unnecessarily;
- invent theoretical constructs;
- alter theory merely to fit available variables;
- describe theory without applying it;
- use theory to justify unsupported causal claims;
- ignore competing theories;
- claim theoretical novelty when only context changes;
- confuse theoretical and conceptual frameworks;
- optimize theory choice for a target journal;
- use theory post hoc to justify preferred hypotheses;
- treat official statistics as proof of theoretical mechanism.

---

# Stop Conditions

Do not finalize a theoretical framework when:

- the RQ is unclear;
- the explanatory need is undefined;
- the selected theory does not address the scientific problem;
- a clearly stronger competing explanation has not been considered;
- critical theory sources remain unverified;
- constructs are inconsistent with the theory;
- the theory is being used only decoratively;
- the proposed mechanism is unsupported;
- theory-dependent hypotheses have been written without establishing the required propositions.

Use:

`THEORETICAL_FRAMEWORK_REQUIRES_REVISION`

or:

`FORMAL_THEORY_NOT_REQUIRED`

when appropriate.

---

# Relationship with Research Question Builder

`research-question-builder` determines:

> What must the study ask?

`theoretical-framework` determines:

> Why should the proposed phenomenon, relationship, or mechanism occur?

The RQ should define the explanatory need.

Theory should not redefine a scientifically valid RQ merely to fit a preferred framework.

---

# Relationship with Hypothesis Builder

When hypotheses depend on explicit theoretical propositions:

prefer:

```text
research-question-builder
        ↓
theoretical-framework
        ↓
hypothesis-builder
```

Pass to `hypothesis-builder`:

- relevant theoretical propositions;
- expected mechanism;
- boundary conditions;
- directional logic;
- contradictory evidence;
- degree of confidence.

When formal theory is not central:

`hypothesis-builder`

may instead use:

- biological mechanisms;
- pharmacological mechanisms;
- physical principles;
- strong empirical evidence.

---

# Relationship with Conceptual Framework

The next step may be:

`conceptual-framework`

The theoretical framework provides:

- explanatory logic;
- relevant constructs;
- mechanisms;
- assumptions;
- boundary conditions.

The conceptual framework translates these into a study-specific structure.

Do not require the conceptual framework to reproduce the entire theory.

---

# Relationship with Methodology Architect

Theory may later influence:

- construct operationalization;
- timing;
- mediator measurement;
- moderator measurement;
- intervention mechanism;
- experimental manipulation;
- analysis requirements.

Theory should not directly dictate statistical software.

Pass scientific requirements to:

`methodology-architect`

---

# Success Criterion

`theoretical-framework` succeeds when formal theory is used only where scientifically justified, legitimate disciplinary explanatory structures are accepted where more appropriate, candidate explanations have been compared rather than selected decoratively, the chosen framework clearly addresses the finalized research question and validated uncertainty, its propositions, mechanisms, assumptions, and boundary conditions are explicit, post-hoc theoretical justification is prevented, and its relationship to audited novelty, hypotheses, conceptual-framework development, and downstream methodology is scientifically coherent.