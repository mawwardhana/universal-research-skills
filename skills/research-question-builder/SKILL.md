---
name: research-question-builder
description: Construct precise, researchable, evidence-grounded research questions from validated research gaps, audited novelty, current State-of-the-Art evidence, research objectives, theoretical logic, research maturity, and feasible study boundaries. Use after scientific positioning and before hypothesis development, theoretical or conceptual framework construction, methodology design, protocol development, or manuscript objective formulation.
---

# Research Question Builder

## Purpose

`research-question-builder` translates a validated scientific problem into one or more precise research questions that can actually be answered by a defensible study.

Its central question is:

> Given what is already known, what remains genuinely unresolved, and what contribution is scientifically defensible, what exactly must this study ask?

The skill must ensure alignment among:

```text
State of the Art
      ↓
Validated Gap
      ↓
Audited Novelty
      ↓
Research Question
      ↓
Methodology
      ↓
Analysis
      ↓
Scientific Conclusion
```

A research question is not merely a grammatically correct question.

It is the logical bridge between:

`UNRESOLVED SCIENCE`

and:

`EVIDENCE TO BE GENERATED`

---

# Core Principle

Use:

> Ask only what the study needs to answer to resolve the validated scientific uncertainty.

Do not create research questions merely because:

- variables are available;
- software can analyze them;
- a questionnaire contains them;
- a previous paper recommends them;
- a supervisor prefers a method;
- a journal frequently publishes them.

The scientific problem comes first.

---

# Required Upstream Context

Prefer inputs from:

`evidence-synthesis`
→ `sota-builder`
→ `gap-discovery`
→ `gap-validator`
→ `novelty-builder`
→ `novelty-auditor`

Important inputs include:

- validated gap statement;
- gap boundary;
- established knowledge;
- unresolved condition;
- scientific consequence;
- audited novelty;
- closest competitor studies;
- what is novel;
- what is not novel;
- remaining uncertainty;
- research-program context;
- feasibility constraints.

Do not build a high-confidence research question from an unvalidated research gap when gap validation is essential to the study's positioning.

---

# Activation Conditions

Use this skill when the researcher asks:

- "What should my research question be?"
- "Help me formulate the research problem."
- "Create RQ1, RQ2, and RQ3."
- "What question should this study answer?"
- "Turn this gap into a research question."
- "Are my research questions aligned with novelty?"
- "Refine my research objectives."
- "Should this study be exploratory or confirmatory?"

---

# 1. Start from the Validated Gap

Represent the gap as:

```yaml
validated_gap:
  established_knowledge:
  unresolved_condition:
  boundary:
  scientific_consequence:
  confidence:
```

The research question should directly target the:

`UNRESOLVED_CONDITION`

Do not simply restate the broad topic.

---

# 2. Incorporate the Audited Novelty

The research question should be capable of generating the evidence required for the audited contribution.

Ask:

> If this research question is answered successfully, will the audited novelty actually be delivered?

If no:

classify:

`NOVELTY_RQ_MISALIGNMENT`

and revise the question.

---

# 3. Define the Knowledge Function

Determine what kind of knowledge the study needs to generate.

Possible functions include:

- `DISCOVER`
- `DESCRIBE`
- `CHARACTERIZE`
- `COMPARE`
- `ASSOCIATE`
- `EXPLAIN`
- `TEST`
- `VALIDATE`
- `PREDICT`
- `DEVELOP`
- `OPTIMIZE`
- `EVALUATE`
- `INTERVENE`
- `IMPLEMENT`
- `TRANSLATE`
- `UNDERSTAND`
- `SYNTHESIZE`

Do not assume every research question seeks causal explanation.

---

# 4. Research Maturity Alignment

Match the RQ to the scientific maturity of the field.

Example:

```text
Discovery
→ What exists?

Characterization
→ What are its properties?

Association
→ How are X and Y related?

Mechanism
→ Through what process?

Validation
→ Does the finding generalize?

Prediction
→ Can the outcome be predicted?

Intervention
→ Can the outcome be changed?

Implementation
→ Can the intervention work in practice?

Translation
→ How can the evidence be applied?
```

Do not jump from immature discovery evidence directly to intervention without justification.

---

# 5. Determine Question Orientation

Classify the RQ as appropriate:

- `EXPLORATORY`
- `DESCRIPTIVE`
- `COMPARATIVE`
- `RELATIONAL`
- `EXPLANATORY`
- `MECHANISTIC`
- `CAUSAL`
- `PREDICTIVE`
- `VALIDATION`
- `EVALUATIVE`
- `IMPLEMENTATION`
- `QUALITATIVE_INTERPRETIVE`
- `MIXED_METHOD`
- `SYNTHESIS`

This classification should guide downstream methodology.

---

# 6. Question Before Method

Do not formulate:

> Can PLS-SEM demonstrate...

Prefer a scientific question such as:

> To what extent does X relate to Y through mechanism M under condition Z?

Then determine later whether PLS-SEM is appropriate.

Likewise, do not formulate research questions around:

- SPSS;
- SmartPLS;
- machine learning;
- NVivo;
- Jamovi;
- R.

Software is downstream.

---

# 7. Question Before Statistical Test

Avoid:

> Is there a significant difference...?

unless statistical significance itself is genuinely the scientific focus.

Prefer a scientific question such as:

> How do outcomes differ between A and B?

The analysis later determines:

- effect magnitude;
- uncertainty;
- statistical evidence.

---

# 8. Research Question Components

Where relevant, clarify:

- phenomenon;
- population;
- exposure or intervention;
- comparator;
- outcome;
- mechanism;
- context;
- time.

Do not force all components into one sentence.

---

# 9. Population Precision

Use a population only as narrowly as scientifically justified.

Population definition should follow:

- scientific mechanism;
- external-validity boundary;
- feasibility;
- study purpose.

Do not use a narrow population solely to create apparent novelty.

---

# 10. Context Precision

Include context when it matters scientifically.

Weak:

> How does X affect Y in City A?

Stronger when justified:

> How does X relate to Y under health-system conditions characterized by C?

Location may define the setting without being the novelty itself.

---

# 11. Time Dimension

Include time explicitly when the gap concerns:

- temporal ordering;
- longitudinal change;
- persistence;
- delayed effects;
- follow-up;
- trajectories.

A temporal gap should not be answered by an inherently cross-sectional RQ.

---

# 12. Mechanistic Research Question

When the validated gap is mechanistic, the RQ should ask:

> Through what scientifically justified process does X relate to or influence Y?

The mechanism must already have scientific justification.

Do not invent mediators simply to create complexity.

---

# 13. Moderation or Boundary Question

When the gap concerns boundary conditions, ask:

> Under what conditions, or for whom, does the relationship differ?

Moderators require:

- theory;
- prior evidence;
- plausible boundary logic.

---

# 14. Validation Research Question

When novelty is external validation, ask directly whether an existing:

- model;
- instrument;
- intervention;
- relationship;

generalizes to independent evidence.

Do not disguise validation as original discovery.

---

# 15. Predictive Research Question

Prediction questions should distinguish:

> Can we explain Y?

from:

> Can we accurately predict Y in unseen observations?

Predictive RQs may require:

- discrimination;
- calibration;
- external validation;
- out-of-sample performance.

Do not turn explanatory models into prediction claims automatically.

---

# 16. Intervention Research Question

A strong intervention RQ identifies, where relevant:

- intervention;
- comparator;
- outcome;
- population;
- time horizon.

The question should reflect whether the objective concerns:

- efficacy;
- effectiveness;
- feasibility;
- mechanism.

---

# 17. Implementation Research Question

Implementation questions may focus on:

- adoption;
- acceptability;
- feasibility;
- fidelity;
- scalability;
- sustainability;
- contextual determinants.

Do not confuse implementation outcomes with intervention efficacy.

---

# 18. Qualitative Research Questions

Qualitative questions may ask:

- how participants experience a phenomenon;
- how a process unfolds;
- how meaning is constructed;
- what mechanisms participants perceive;
- how context shapes experience.

Prefer open forms such as:

> How...

> In what ways...

> How do participants understand...

Do not force hypotheses into qualitative research.

---

# 19. Mixed-Methods Research Questions

Mixed-method studies should justify why integration is necessary.

Possible architecture:

```text
RQ1 Quantitative
What pattern or effect exists?

RQ2 Qualitative
How or why does that pattern occur?

RQ3 Integration
How do both forms of evidence jointly explain the phenomenon?
```

Do not label a study mixed methods merely because it uses two data types.

---

# 20. Systematic Review Research Questions

For systematic reviews, questions may focus on:

- effectiveness;
- prevalence;
- association;
- mechanisms;
- experiences;
- methods;
- evidence configuration.

Use an appropriate framework such as:

- PICO;
- PECO;
- PCC;
- SPIDER;

when relevant.

Do not force PICO universally.

---

# 21. Meta-Analysis Research Questions

A meta-analysis RQ should define sufficiently compatible:

- effect;
- population;
- exposure or intervention;
- outcome;
- comparator where relevant.

Do not promise quantitative pooling before eligibility and heterogeneity are assessed.

---

# 22. Experimental Research Questions

Experimental RQs should distinguish whether the objective is:

- causal effect;
- dose-response;
- optimization;
- mechanism;
- performance comparison.

Avoid vague questions such as:

> Is formulation A good?

Prefer measurable scientific outcomes.

---

# 23. Methodological Research Questions

A methodological RQ should focus on whether the method improves:

- validity;
- precision;
- reliability;
- bias;
- efficiency;
- scientific inference.

Do not frame:

> Can method X be used?

if the real contribution concerns better measurement or inference.

---

# 24. Measurement Research Questions

Possible directions include:

- validity;
- reliability;
- measurement invariance;
- responsiveness;
- sensitivity;
- specificity;
- construct representation.

Instrument use alone is not instrument validation.

---

# 25. Theoretical Research Questions

Theoretical questions may test:

- prediction;
- mechanism;
- boundary condition;
- integration;
- contradiction.

Do not ask merely:

> Does Theory X apply?

Specify what theoretical proposition is actually being tested.

---

# 26. Primary Research Question

Prefer one clear:

`PRIMARY_RESEARCH_QUESTION`

when the study has one central scientific purpose.

The primary RQ should directly represent:

- validated gap;
- audited novelty;
- main scientific contribution.

---

# 27. Secondary Research Questions

Add secondary RQs only when they:

- contribute directly to the central problem;
- explain mechanism;
- test boundary conditions;
- support validation;
- provide necessary contextual evidence.

Do not fragment one study into many unrelated questions.

---

# 28. RQ Quantity Guard

More RQs do not mean stronger research.

Typical studies may require:

- one primary RQ;
- a small number of secondary RQs.

Avoid unnecessary RQ1–RQ12 structures.

Research programs may contain more questions across multiple studies.

---

# 29. Scope Guard

Reject questions that are too broad to answer.

Weak:

> How does technology affect education?

Better:

a bounded question tied to:

- population;
- phenomenon;
- evidence need;
- outcome.

Do not over-narrow before design requirements are understood.

---

# 30. Double-Barreled Question Guard

Avoid asking several distinct scientific questions in one RQ.

Example:

> How does X affect Y and Z and why does it occur and how should it be implemented?

Split the question when these require different evidence.

---

# 31. Presupposition Guard

Do not embed an unproven conclusion into the question.

Weak:

> Why does X improve Y?

when improvement itself is uncertain.

Prefer:

> How is X associated with Y, and what mechanisms may explain any observed relationship?

or an appropriately causal form only when causality is justified.

---

# 32. Causal Language Guard

Use causal RQs only when the study design can support causal inference.

Do not ask:

> What is the effect of X on Y?

if the planned evidence is purely cross-sectional and confounding cannot be addressed adequately.

---

# 33. Association vs Explanation vs Prediction vs Causation

Distinguish:

```text
Association
Does X relate to Y?

Explanation
Why does X relate to Y?

Prediction
Can X predict Y in new observations?

Causation
Does changing X change Y?
```

These require different designs and analyses.

---

# 34. Feasibility Check

Before finalizing an RQ, assess whether necessary evidence can realistically be obtained.

Consider:

- population access;
- data availability;
- laboratory capability;
- sample requirements;
- follow-up time;
- ethical requirements;
- collaboration;
- funding.

Use:

- `HIGH_FEASIBILITY`
- `MODERATE_FEASIBILITY`
- `LOW_FEASIBILITY`
- `UNKNOWN`

Do not weaken an important RQ automatically when collaboration can solve feasibility.

---

# 35. Answerability

Classify:

- `CLEARLY_ANSWERABLE`
- `ANSWERABLE_WITH_REFINEMENT`
- `DIFFICULT_TO_ANSWER`
- `NOT_CURRENTLY_ANSWERABLE`

An interesting question may still be empirically unanswerable.

---

# 36. Evidence Requirement Mapping

For each RQ identify conceptually:

> What evidence would answer this question?

```text
RQ
↓
Needed observations
↓
Design requirements
↓
Measurement requirements
↓
Analysis requirements
```

Do not select detailed methods yet.

---

# 37. RQ–Gap Alignment

Audit:

```text
Validated Gap
     ↕
Research Question
```

Possible status:

- `DIRECT_ALIGNMENT`
- `PARTIAL_ALIGNMENT`
- `WEAK_ALIGNMENT`
- `MISALIGNED`

A research question that does not resolve the validated gap should be revised.

---

# 38. RQ–Novelty Alignment

Audit:

```text
Audited Novelty
      ↕
Research Question
```

Ask:

> Will answering this RQ actually create the audited scientific advancement?

If not:

`NOVELTY_RQ_MISALIGNMENT`

---

# 39. RQ–Contribution Alignment

The anticipated answer should have a plausible contribution.

Possible contributions:

- explanation;
- validation;
- prediction;
- measurement;
- intervention;
- implementation;
- translation.

Avoid questions whose answers would add little scientifically.

---

# 40. RQ–Research Maturity Alignment

Audit whether the RQ is appropriate to current evidence maturity.

Example:

If the field is still:

`VERY_EARLY`

a large implementation trial may be premature.

Use:

- `MATURITY_ALIGNED`
- `POSSIBLY_PREMATURE`
- `MATURE_FOR_NEXT_STAGE`

---

# 41. RQ–Trajectory Alignment

For continuation research, assess whether the question:

- deepens previous work;
- validates previous work;
- translates previous work;
- intentionally opens a new branch.

Use:

- `TRAJECTORY_CONTINUATION`
- `TRAJECTORY_DEEPENING`
- `TRAJECTORY_VALIDATION`
- `TRAJECTORY_TRANSLATION`
- `NEW_RESEARCH_BRANCH`

Do not force continuity when a new research line is scientifically justified.

---

# 42. Question Hierarchy

When several RQs are needed, establish logical order.

Example:

```text
RQ1
Does the phenomenon occur?

      ↓

RQ2
Through what mechanism?

      ↓

RQ3
Under what conditions?
```

or:

```text
RQ1
Develop model

RQ2
Internally validate model

RQ3
Externally validate model
```

Do not create arbitrary numbered lists.

---

# 43. Exploratory vs Confirmatory Status

Classify each RQ:

- `EXPLORATORY`
- `CONFIRMATORY`
- `MIXED`

This helps determine whether hypotheses are appropriate.

---

# 44. Hypothesis Eligibility

After RQ formulation, determine:

- `HYPOTHESIS_REQUIRED`
- `HYPOTHESIS_APPROPRIATE`
- `HYPOTHESIS_OPTIONAL`
- `HYPOTHESIS_NOT_APPROPRIATE`

Hypotheses are commonly appropriate for:

- confirmatory quantitative testing;
- theory-driven relational research;
- experimental research;
- mechanism testing.

They may be inappropriate for:

- exploratory qualitative studies;
- descriptive discovery;
- many scoping reviews;
- some methodological development studies.

Do not generate hypotheses automatically.

---

# 45. Theoretical Framework Need

Determine whether the study requires explicit theoretical grounding.

Use:

- `THEORETICAL_FRAMEWORK_REQUIRED`
- `THEORETICAL_FRAMEWORK_USEFUL`
- `THEORETICAL_FRAMEWORK_NOT_CENTRAL`
- `UNKNOWN`

Do not invent theory to make a study appear sophisticated.

---

# 46. Conceptual Framework Need

A conceptual framework may be useful when the study must organize:

- constructs;
- relationships;
- mechanisms;
- context;
- evidence flow.

Use:

- `CONCEPTUAL_FRAMEWORK_REQUIRED`
- `CONCEPTUAL_FRAMEWORK_USEFUL`
- `CONCEPTUAL_FRAMEWORK_NOT_NECESSARY`

---

# 47. Objective Generation

After RQs are finalized, construct objectives.

Each objective should correspond directly to an RQ.

Example:

```text
RQ:
To what extent does X predict Y?

Objective:
To evaluate the predictive contribution of X to Y...
```

Do not create objectives unrelated to the RQs.

---

# 48. General Objective

When institutional formats require a general objective:

derive it from the primary RQ.

Do not create a broader aim than the study can answer.

---

# 49. Specific Objectives

Specific objectives should correspond to:

- secondary RQs;
- logically necessary analytic or scientific stages.

Avoid objectives that merely describe procedural activities such as:

> distribute questionnaires.

Data collection is not usually a scientific objective.

---

# 50. Objective Verb Guard

Use verbs reflecting the knowledge goal.

Examples:

- characterize;
- estimate;
- compare;
- evaluate;
- examine;
- explain;
- test;
- validate;
- predict;
- develop;
- assess;
- explore;
- understand.

Avoid vague verbs such as:

- know;
- learn about;
- see.

---

# 51. RQ Formulation Quality Test

A strong RQ should be:

- clear;
- specific;
- scientifically meaningful;
- answerable;
- feasible;
- evidence-aligned;
- gap-aligned;
- novelty-aligned.

Do not use acronym frameworks mechanically if they distort the science.

---

# 52. FINER Awareness

When helpful, consider:

- Feasible
- Interesting
- Novel
- Ethical
- Relevant

Interpret:

`Novel`

according to the audited novelty workflow already completed.

Do not treat FINER as a substitute for gap and novelty validation.

---

# 53. PICOT Awareness

Use PICOT where appropriate:

- Population
- Intervention
- Comparator
- Outcome
- Time

Especially useful for certain clinical intervention questions.

Do not force PICOT onto:

- qualitative studies;
- exploratory studies;
- conceptual research.

---

# 54. PCC Awareness

For scoping and mapping questions, PCC may be appropriate:

- Population
- Concept
- Context

Use method-specific frameworks only when helpful.

---

# 55. SPIDER Awareness

For some qualitative and mixed-method questions:

- Sample
- Phenomenon of Interest
- Design
- Evaluation
- Research type

may help clarify the question.

The framework serves the RQ.

The RQ does not serve the framework.

---

# 56. Research Question Candidate Generation

When the gap can be approached in multiple ways, generate a small set of candidate RQs.

Recommended:

2–4 candidates.

Examples may differ by:

- mechanism;
- validation;
- prediction;
- intervention.

Do not generate many superficial variants.

---

# 57. Candidate RQ Card

For each candidate:

## Research Question
[...]

## Knowledge Function
[...]

## Validated Gap Addressed
[...]

## Audited Novelty Addressed
[...]

## Evidence Needed
[...]

## Feasibility
[...]

## Hypothesis Status
[...]

## Main Strength
[...]

## Main Limitation
[...]

---

# 58. Candidate Comparison

When useful:

| Candidate RQ | Gap Alignment | Novelty Alignment | Scientific Value | Feasibility | Maturity Fit |
|---|---|---|---|---|---|

Do not score mechanically unless useful.

---

# 59. Primary RQ Selection

Choose the primary RQ based on:

1. direct gap resolution;
2. novelty delivery;
3. scientific importance;
4. study maturity;
5. feasibility.

Do not prioritize ease alone.

---

# 60. RQ Status

Use:

- `DRAFT_RQ`
- `REFINED_RQ`
- `EVIDENCE_ALIGNED_RQ`
- `READY_FOR_DESIGN`
- `REQUIRES_REVISION`

---

# 61. Full Output Structure

When comprehensive RQ development is requested, use:

## A. Validated Scientific Gap
[...]

## B. Audited Novelty
[...]

## C. Knowledge Function
[...]

## D. Primary Research Question
[...]

## E. Secondary Research Questions
[...]

## F. Rationale for Each RQ
[...]

## G. Evidence Required to Answer Each RQ
[...]

## H. Gap–RQ Alignment
[...]

## I. Novelty–RQ Alignment
[...]

## J. Research Maturity Alignment
[...]

## K. Feasibility
[...]

## L. Hypothesis Eligibility
[...]

## M. Theoretical Framework Need
[...]

## N. Conceptual Framework Need
[...]

## O. Research Objectives
[...]

## P. Remaining Uncertainty
[...]

## Q. Next Recommended Workflow
[...]

---

# 62. RQ Alignment Matrix

When useful:

| RQ | Validated Gap | Novelty | Evidence Needed | Objective | Downstream Design Need |
|---|---|---|---|---|---|

This may serve as a control document throughout the study.

---

# 63. Research Passport Update

When supported, update:

```yaml
research_questions:
  validated_gap:
  audited_novelty:
  knowledge_function:
  primary_rq:
  secondary_rqs:
  question_orientation:
  maturity_alignment:
  trajectory_alignment:
  feasibility:
  answerability:
  hypothesis_status:
  theoretical_framework_status:
  conceptual_framework_status:
  objectives:
  alignment_status:
  remaining_uncertainty:
  next_stage:
```

Unknown fields remain unknown.

---

# 64. Research Question Consistency Guard

Once an RQ is locked, downstream:

- hypotheses;
- variables;
- methodology;
- analysis;
- results;
- discussion;
- conclusion;

must remain aligned with it.

If downstream work introduces a different scientific question:

flag:

`RQ_DRIFT`

---

# 65. Scope Creep Guard

During study design, new variables or analyses may appear attractive.

Ask:

> Does this directly help answer an existing RQ?

If not:

classify as:

`EXPLORATORY_ADDITIONAL_ANALYSIS`

or remove it.

Do not silently enlarge the study.

---

# 66. Outcome Switching Awareness

For confirmatory studies, downstream outcomes should not be changed opportunistically after seeing results.

Preserve:

- primary outcome;
- secondary outcomes;

when protocol logic requires it.

Do not fabricate preregistration.

---

# 67. Manuscript Consistency

The manuscript should preserve the same scientific logic:

```text
Introduction
→ Gap

Final Introduction Paragraph
→ RQ / Objective

Methods
→ Evidence generation

Results
→ Answer RQ

Discussion
→ Interpret answer

Conclusion
→ Respond to RQ
```

Do not allow discussion to answer a different question.

---

# 68. Publication Strategy Independence

Do not rewrite the RQ merely because a target journal appears to prefer another topic.

Scientific question comes first.

Journal matching comes downstream.

---

# 69. Scopus-First Evidence Awareness

RQ development should rely on the validated evidence base already built through the Scopus-first scholarly pipeline.

Do not introduce unsupported scientific assumptions at this stage.

---

# 70. Phenomenon Evidence Awareness

When real-world magnitude, burden, trend, policy, regulation, or institutional context matters, use:

`phenomenon-evidence-builder`

as a complementary evidence source.

Maintain:

```text
Phenomenon Evidence
= authority-first real-world evidence

Scholarly Evidence
= Scopus-first scientific evidence
```

Phenomenon evidence may support:

- problem relevance;
- magnitude;
- burden;
- trend;
- policy context;
- regulatory context.

It does not replace scholarly evidence for:

- theory;
- mechanism;
- State of the Art;
- research-gap validation;
- novelty.

---

# 71. Target-Journal Literature

Relevant target-journal evidence may inform terminology or framing later.

It must not redefine the underlying scientific question without evidence.

---

# 72. APC Independence

Publication cost has no role in research-question quality.

No-mandatory-APC preference belongs downstream to publication strategy.

---

# 73. Avoid These Behaviors

Do not:

- start from statistical software;
- start from available variables alone;
- manufacture mediators or moderators;
- force hypotheses into exploratory research;
- create causal questions for weak observational designs;
- create predictive claims from explanatory models;
- use geographic novelty as the question's main justification;
- generate excessive RQs;
- combine unrelated questions;
- ignore audited novelty;
- ignore validated gap;
- optimize RQs for a journal before scientific validity;
- use methods as novelty;
- fabricate theoretical relationships.

---

# Stop Conditions

Do not classify an RQ as ready for design when:

- the research gap remains inadequately validated;
- novelty is materially unresolved and central to the study;
- question scope is too broad;
- required evidence is unavailable;
- causal wording exceeds likely design capability;
- primary outcome or phenomenon is unclear;
- multiple RQs are scientifically disconnected.

Return to the appropriate upstream stage.

---

# Downstream Routing Priority

After research questions are finalized, do not assume a universal sequence of:

```text
Research Question
↓
Hypothesis
↓
Theory
```

The correct downstream route depends on the scientific logic of the study.

Assess:

- theoretical-framework need;
- hypothesis eligibility;
- conceptual-framework need.

Then route conditionally.

---

## Route A — Theory-Driven Confirmatory Research

When:

`THEORETICAL_FRAMEWORK_REQUIRED`

and hypotheses are:

`HYPOTHESIS_REQUIRED`

or:

`HYPOTHESIS_APPROPRIATE`

prefer:

```text
research-question-builder
        ↓
theoretical-framework
        ↓
hypothesis-builder
        ↓
conceptual-framework
```

Theory should establish the explanatory propositions before final directional hypotheses are locked.

Do not construct hypotheses first and then search for a theory that justifies them.

---

## Route B — Empirically Grounded Confirmatory Research

When a formal theory is:

`THEORETICAL_FRAMEWORK_NOT_CENTRAL`

but hypotheses are scientifically appropriate:

```text
research-question-builder
        ↓
hypothesis-builder
        ↓
conceptual-framework
```

Hypotheses may be grounded in:

- established empirical evidence;
- mechanistic evidence;
- biological plausibility;
- physical principles;
- validated models;

without forcing a named theory.

---

## Route C — Exploratory or Qualitative Research

When:

`HYPOTHESIS_NOT_APPROPRIATE`

route toward:

```text
research-question-builder
        ↓
theoretical-framework
        if useful as interpretive lens
        ↓
conceptual-framework
        if useful
        ↓
methodology-architect
```

Do not manufacture hypotheses.

---

## Route D — Descriptive, Validation, or Methodological Research

When neither formal theory nor hypotheses are central:

```text
research-question-builder
        ↓
conceptual-framework
        if needed
        ↓
methodology-architect
```

A study does not become scientifically weaker merely because it does not require a named theory or formal hypotheses.

---

# Theory-Before-Hypothesis Safeguard

When a hypothesis depends on a specific theoretical proposition that has not yet been established for the study:

route first to:

`theoretical-framework`

before finalizing the hypothesis.

Use:

`THEORY_REQUIRED_BEFORE_HYPOTHESIS`

This safeguard prevents post-hoc theory selection.

---

# Relationship with Hypothesis Builder

After the RQ is established, determine whether hypotheses are appropriate.

If:

`HYPOTHESIS_REQUIRED`

or:

`HYPOTHESIS_APPROPRIATE`

route to:

`hypothesis-builder`

unless the hypothesis depends on a theoretical proposition that still needs to be established.

In that case route first to:

`theoretical-framework`

and then return to:

`hypothesis-builder`

Do not force the sequence:

RQ → Hypothesis

for every research design.

---

# Relationship with Theoretical Framework

When a theory is central to explaining the RQ:

route to:

`theoretical-framework`

The framework should help explain:

> Why should the proposed relationship or mechanism occur?

When the hypothesis itself depends on that theoretical proposition, establish the theoretical framework before locking the hypothesis.

---

# Relationship with Conceptual Framework

When constructs and relationships need to be organized visually or logically:

route to:

`conceptual-framework`

A conceptual framework may be useful:

- after theory selection;
- after hypothesis construction;
- directly after RQ formulation;

depending on the study.

Do not treat the conceptual framework as mandatory.

---

# Relationship with Methodology Architect

The finalized RQ eventually becomes the primary input to:

`methodology-architect`

The methodology must generate the evidence required to answer the RQ.

Do not allow methodology to redefine the RQ merely because a preferred method or software is available.

---

# Success Criterion

`research-question-builder` succeeds when a validated scientific gap and audited novelty have been translated into a small, coherent set of precise and answerable research questions whose scientific purpose, required evidence, feasibility, research maturity, objectives, and downstream hypothesis/framework needs are explicit and aligned.