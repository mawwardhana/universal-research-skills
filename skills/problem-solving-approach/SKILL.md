---
name: problem-solving-approach
description: Determine the scientifically appropriate strategy for answering a finalized research question before detailed methodology is selected. Use when a researcher has a sufficiently defined research problem, validated gap, audited novelty, and research question, and needs to decide what kind of evidence, comparison, observation, intervention, mechanism test, prediction, validation, qualitative inquiry, review, or mixed-method strategy can actually answer it. This skill translates the research question into an evidence-generating problem-solving approach while preventing method-first, software-first, and design-by-convenience decisions.
---

# Problem-Solving Approach

## Purpose

`problem-solving-approach` determines the scientific strategy required to answer a finalized research question.

Its central question is:

> What kind of evidence must be generated, compared, observed, tested, modeled, interpreted, or synthesized to answer this research question defensibly?

This skill operates after the research logic is sufficiently clear and before detailed methodological architecture.

It is not a statistical-method selector.
It is not a software selector.
It is not a protocol generator.
It is not a sampling calculator.
It is not an instrument-construction tool.

Those functions belong downstream.

---

# Core Principle

Use:

> Question before method. Evidence need before design. Design before software.

The research question should determine the problem-solving approach.

Do not begin with SPSS, Jamovi, R, Python, SmartPLS, AMOS, NVivo, SEM, PLS-SEM, machine learning, a favorite statistical test, or a convenient dataset.

Begin with:

> What evidence would actually answer the research question?

---

# Position in the Framework

Preferred upstream logic:

```text
Validated Gap
      ↓
Audited Novelty
      ↓
Research Question
      ↓
Theory / Hypothesis / Conceptual Framework
when scientifically required
      ↓
problem-solving-approach
      ↓
methodology-architect
```

This skill bridges research logic and research design.

---

# Required Upstream Context

Use whatever is already available from:

- `research-question-builder`;
- `hypothesis-builder`;
- `theoretical-framework`;
- `conceptual-framework`;
- `phenomenon-evidence-builder`;
- `gap-validator`;
- `novelty-auditor`.

Do not ask the researcher to repeat information already established.

Minimum useful context normally includes:

- research question;
- research objective;
- target phenomenon;
- target population or unit;
- intended inference;
- key constructs or outcomes;
- whether hypotheses exist;
- whether theory or mechanism is central;
- practical constraints when they materially affect feasibility.

---

# Entry Status

Classify the request as:

- `READY_FOR_PROBLEM_SOLVING_APPROACH`
- `RQ_REQUIRES_REFINEMENT`
- `UPSTREAM_LOGIC_INCOMPLETE`
- `APPROACH_ALREADY_ESTABLISHED`
- `APPROACH_REQUIRES_REASSESSMENT`

Do not force downstream design when the RQ is not sufficiently answerable.

---

# Research Question Function

First determine what kind of knowledge the RQ seeks.

Possible functions include:

- `DESCRIBE`
- `ESTIMATE`
- `COMPARE`
- `ASSOCIATE`
- `EXPLAIN`
- `TEST_CAUSAL_EFFECT`
- `TEST_MECHANISM`
- `PREDICT`
- `DIAGNOSE`
- `VALIDATE`
- `DEVELOP_MEASURE`
- `OPTIMIZE`
- `FORMULATE`
- `EVALUATE_INTERVENTION`
- `EVALUATE_IMPLEMENTATION`
- `EXPLORE_EXPERIENCE`
- `UNDERSTAND_PROCESS`
- `INTERPRET_MEANING`
- `BUILD_THEORY`
- `INTEGRATE_EVIDENCE`
- `MAP_LITERATURE`
- `SYNTHESIZE_EFFECTS`
- `ASSESS_FEASIBILITY`
- `ASSESS_SAFETY`
- `ASSESS_STABILITY`
- `ASSESS_PERFORMANCE`

More than one function may apply.

Identify the dominant function.

---

# Evidence Need

Translate the RQ into the type of evidence needed.

| RQ Function | Evidence Need |
|---|---|
| Describe | distribution, frequency, characteristics |
| Estimate | parameter estimate with uncertainty |
| Compare | comparable groups or conditions |
| Associate | covariation with appropriate control |
| Explain | mechanism, pathway, process, or explanatory pattern |
| Test causal effect | counterfactual contrast or strong causal design |
| Predict | out-of-sample predictive performance |
| Diagnose | discrimination, calibration, diagnostic accuracy |
| Validate | reproducibility, criterion, construct, or external performance |
| Explore experience | rich participant accounts |
| Understand process | temporal, contextual, procedural evidence |
| Integrate evidence | systematically selected prior studies |
| Optimize | performance under controlled variation |
| Formulate | composition–property–performance evidence |
| Implement | adoption, fidelity, acceptability, feasibility, sustainability |

Do not select a design until the evidence need is explicit.

---

# Intended Inference

Classify the primary inference.

Use:

- `DESCRIPTIVE_INFERENCE`
- `ESTIMATIVE_INFERENCE`
- `COMPARATIVE_INFERENCE`
- `ASSOCIATIONAL_INFERENCE`
- `CAUSAL_INFERENCE`
- `MECHANISTIC_INFERENCE`
- `PREDICTIVE_INFERENCE`
- `DIAGNOSTIC_INFERENCE`
- `VALIDATION_INFERENCE`
- `INTERPRETIVE_INFERENCE`
- `THEORY_BUILDING_INFERENCE`
- `IMPLEMENTATION_INFERENCE`
- `SYNTHESIS_INFERENCE`
- `OPTIMIZATION_INFERENCE`

The selected problem-solving approach must be capable of supporting the intended inference.

---

# Causal Inference Guard

If the RQ uses language such as effect, impact, cause, influence, leads to, produces, or determines, determine whether causal inference is actually intended.

Do not silently weaken or strengthen causal language.

If causal inference is intended, ask:

- What is the intervention or exposure?
- What is the comparator?
- What is the relevant counterfactual?
- What sources of confounding exist?
- Is temporal ordering identifiable?
- Can randomization occur?
- If not, what quasi-experimental or observational identification strategy is defensible?

Do not route a causal RQ to a simple cross-sectional association design without explicitly flagging the mismatch.

---

# Association Guard

If the available design can only support association, use:

`ASSOCIATIONAL_APPROACH`

Do not describe the approach as causal.

---

# Prediction Guard

Prediction is not explanation.

Prediction-oriented studies require:

- target outcome;
- prediction horizon where relevant;
- candidate predictors;
- training and evaluation strategy;
- internal validation;
- external validation where feasible;
- discrimination or performance metrics;
- calibration when relevant;
- overfitting control.

Do not choose predictors only because they are statistically significant.

Do not call an explanatory regression model a prediction model automatically.

---

# Diagnostic Approach

For diagnostic questions, identify:

- index test;
- reference standard;
- target condition;
- target population;
- threshold strategy;
- sensitivity;
- specificity;
- predictive values where relevant;
- likelihood ratios where relevant;
- discrimination;
- calibration where relevant.

Do not confuse diagnostic accuracy with etiological association.

---

# Validation Approach

Validation may concern:

- instrument;
- measurement;
- prediction model;
- diagnostic test;
- intervention protocol;
- formulation;
- computational model;
- theoretical model;
- implementation strategy.

Possible validation types:

- internal;
- external;
- temporal;
- geographic;
- cross-population;
- criterion;
- construct;
- convergent;
- discriminant;
- content;
- predictive;
- reproducibility;
- robustness.

Specify what is being validated and against what standard.

---

# Mechanism-Oriented Approach

When the RQ asks how or why something occurs, identify the mechanism evidence required.

Possible mechanism evidence includes:

- biological pathway;
- pharmacological pathway;
- molecular interaction;
- mediation;
- temporal sequence;
- process tracing;
- qualitative process evidence;
- material-property relationship;
- engineering failure mechanism;
- behavioral process;
- organizational mechanism.

Mechanism claims require more than simple association.

---

# Experimental Approach

Use an experimental problem-solving approach when:

- manipulation is scientifically justified;
- the manipulated condition can meaningfully test the RQ;
- assignment or exposure can be controlled;
- safety and ethics permit intervention;
- outcome measurement can capture the intended effect.

Possible experimental forms include randomized experiments, controlled laboratory experiments, formulation experiments, factorial experiments, dose-response experiments, repeated-measures experiments, bench experiments, material-performance experiments, biological assays, and simulation experiments.

Detailed design belongs to `methodology-architect`.

---

# Quasi-Experimental Approach

Consider quasi-experimental strategies when randomization is not feasible but stronger causal inference is required.

Possible strategies may include:

- interrupted time series;
- difference-in-differences;
- regression discontinuity;
- matched comparison;
- natural experiment;
- controlled before-after;
- instrumental-variable design where defensible.

Do not select these by name alone.

Confirm that their identification assumptions are plausible.

---

# Observational Approach

Use observational strategies when the researcher cannot or should not assign exposure.

Possible orientations include:

- descriptive;
- cross-sectional;
- cohort;
- case-control;
- longitudinal;
- registry-based;
- routine-data;
- ecological;
- multilevel.

The design must match the timing and inference required.

---

# Cross-Sectional Guard

Cross-sectional data may support:

- description;
- prevalence estimation;
- association;
- construct evaluation under some conditions.

They usually do not establish:

- temporal precedence;
- longitudinal change;
- strong causal effects.

Do not use effect language merely because regression coefficients are estimated.

---

# Longitudinal Approach

Use longitudinal strategies when the RQ concerns:

- change;
- trajectory;
- incidence;
- temporal ordering;
- repeated measurement;
- delayed outcome;
- persistence;
- transition;
- within-person or within-unit dynamics.

Specify the relevant time structure before detailed design.

---

# Cohort-Oriented Approach

Use cohort logic when exposure or baseline status precedes outcome assessment, incidence or risk is relevant, and follow-up is required.

Clarify:

- prospective vs retrospective;
- entry criteria;
- follow-up period;
- censoring;
- repeated measures;
- outcome ascertainment.

---

# Case-Control-Oriented Approach

Use case-control logic when outcome status defines sampling, the outcome is relatively uncommon or retrospective exposure assessment is appropriate, and valid controls can represent the source population.

Do not estimate risk directly without appropriate methods.

---

# Ecological Approach

Use ecological designs only when the unit of analysis is genuinely aggregate.

Guard against ecological fallacy.

Do not infer individual-level relationships from group-level associations.

---

# Multilevel Approach

Use multilevel problem-solving logic when observations are nested, for example:

- students within classrooms;
- patients within hospitals;
- employees within organizations;
- repeated observations within individuals;
- regions within countries.

The approach should preserve the level at which constructs and inferences operate.

---

# Qualitative Problem-Solving Approach

Use qualitative inquiry when the RQ seeks:

- lived experience;
- meaning;
- process;
- perception;
- context;
- social interaction;
- implementation experience;
- theory generation;
- interpretation.

Possible orientations include:

- phenomenology;
- grounded theory;
- case study;
- ethnography;
- narrative inquiry;
- qualitative description;
- thematic inquiry;
- content analysis;
- framework analysis.

Do not select a named qualitative tradition merely for prestige.

The tradition should match epistemic goal, data type, unit of interpretation, and analytic logic.

---

# Qualitative Depth Guard

If the RQ asks how many or how strong an effect is, qualitative data alone may not answer it.

If the RQ asks how something is experienced or how a process unfolds, a purely quantitative design may be insufficient.

---

# Mixed-Method Problem-Solving Approach

Use mixed methods when integration of quantitative and qualitative evidence is necessary to answer the RQ more completely.

Possible strategic purposes include:

- explanation;
- exploration;
- triangulation;
- development;
- complementarity;
- implementation understanding;
- intervention development;
- validation.

Possible broad structures include:

- convergent;
- explanatory sequential;
- exploratory sequential;
- embedded;
- multiphase.

Do not use mixed methods merely to appear comprehensive.

There must be an explicit integration purpose.

---

# Mixed-Method Integration Guard

State:

- what each strand contributes;
- where integration occurs;
- why one strand alone is insufficient;
- what combined inference is expected.

Without integration, two parallel methods are not necessarily mixed-method research.

---

# Systematic Review Approach

Use a systematic-review strategy when the RQ can be answered primarily from existing studies and requires transparent evidence identification and synthesis.

Possible forms include systematic review, scoping review, rapid review, umbrella review, diagnostic review, prognostic review, qualitative evidence synthesis, and mixed-method review.

Do not call a narrative literature summary a systematic review.

---

# Meta-Analysis Approach

Meta-analysis is appropriate when sufficiently comparable quantitative studies exist, effect estimates can be meaningfully synthesized, outcome definitions are sufficiently compatible, and heterogeneity can be investigated.

Meta-analysis is not mandatory for every systematic review.

Detailed synthesis methodology belongs downstream.

---

# Bibliometric Approach

Use bibliometric strategies when the RQ concerns the structure or development of scholarly literature itself.

Possible questions include:

- publication growth;
- co-authorship;
- citation structure;
- co-citation;
- bibliographic coupling;
- keyword networks;
- thematic evolution.

Bibliometric mapping does not directly establish treatment effectiveness, causal mechanisms, clinical benefit, or substantive research gaps.

---

# Formulation Research Approach

For pharmaceutical, biomaterial, cosmetic, food, or formulation-oriented studies, distinguish:

- formulation development;
- optimization;
- physicochemical characterization;
- stability;
- release or diffusion;
- mechanical performance;
- biological activity;
- safety;
- comparative performance.

A formulation study should connect:

```text
Composition
    ↓
Process
    ↓
Material / physicochemical properties
    ↓
Performance
    ↓
Biological or functional outcome
```

Do not treat formulation variation alone as scientific contribution.

---

# Laboratory and Biomedical Approach

For laboratory research, identify whether the RQ requires analytical characterization, biochemical assay, cell-based assay, microbiological assay, molecular measurement, pharmacological testing, toxicological testing, ex vivo study, in vivo study, or mechanistic experimentation.

Clarify the biological level of inference.

Do not generalize in vitro results directly to clinical effectiveness.

---

# Pharmacological Approach

For pharmacological questions, possible evidence needs include:

- pharmacokinetics;
- pharmacodynamics;
- exposure-response;
- dose-response;
- metabolism;
- interaction;
- safety;
- efficacy;
- effectiveness;
- pharmacogenetics;
- pharmacogenomics.

Distinguish drug property from patient outcome.

---

# Education Research Approach

For education research, clarify whether the study aims to:

- describe learning conditions;
- evaluate an intervention;
- understand learner or teacher experience;
- validate an instrument;
- examine associations;
- test a theoretical model;
- assess implementation;
- develop educational media or technology;
- evaluate learning outcomes.

Do not select SEM or PLS-SEM before deciding what educational inference is required.

---

# Social-Science and Organizational Approach

Possible evidence strategies include survey, longitudinal survey, experiment, quasi-experiment, qualitative interview, focus group, ethnography, organizational case study, multilevel design, mixed methods, and secondary-data analysis.

Construct-rich research does not automatically require SEM.

---

# Policy Research Approach

Policy questions may require:

- policy analysis;
- implementation analysis;
- comparative policy study;
- natural experiment;
- interrupted time series;
- stakeholder inquiry;
- administrative-data analysis;
- mixed-method evaluation.

Regulatory text can establish policy content.

It cannot alone establish policy effectiveness.

---

# Implementation Research Approach

If the RQ concerns real-world uptake or implementation, consider evidence about:

- adoption;
- acceptability;
- appropriateness;
- feasibility;
- fidelity;
- penetration;
- reach;
- sustainability;
- implementation cost;
- context;
- barriers;
- facilitators.

Do not substitute efficacy evidence for implementation evidence.

---

# Intervention Development Approach

For early-stage intervention research, possible stages include:

```text
Needs Assessment
      ↓
Intervention Logic
      ↓
Prototype / Development
      ↓
Feasibility
      ↓
Pilot
      ↓
Effectiveness
      ↓
Implementation
```

Do not jump directly to effectiveness testing when the intervention is not yet sufficiently developed.

---

# Instrument Development Approach

When the RQ concerns measurement development, possible evidence phases include:

```text
Construct Definition
      ↓
Item / Indicator Generation
      ↓
Content Evaluation
      ↓
Pilot Testing
      ↓
Measurement Structure
      ↓
Reliability
      ↓
Validity
      ↓
Cross-Population Validation
```

Do not begin factor analysis before the construct and measurement domain are clear.

---

# Secondary-Data Approach

Secondary data may be appropriate when variables align with the RQ, population aligns with target inference, timing is suitable, measurement quality is adequate, missingness is manageable, and provenance is known.

Do not redefine the RQ silently to fit whatever variables happen to exist.

If compromise is necessary, flag:

`RQ_DATA_ALIGNMENT_REQUIRES_REVISION`

---

# Existing Dataset Guard

Ask:

> Can this dataset answer the RQ?

not:

> What research question can I force onto this dataset?

Data-driven discovery may be valid, but it should be explicitly labeled as exploratory rather than retrofitted as confirmatory.

---

# Feasibility

Assess feasibility after the evidence need is clear.

Possible constraints include:

- time;
- budget;
- equipment;
- expertise;
- participant access;
- sample availability;
- ethics;
- data access;
- laboratory capacity;
- follow-up duration;
- institutional approval.

Use feasibility to refine implementation.

Do not allow feasibility to redefine the scientific question silently.

---

# Feasibility Outcomes

Use:

- `FEASIBLE_AS_PROPOSED`
- `FEASIBLE_WITH_ADAPTATION`
- `SCIENTIFICALLY_VALID_BUT_NOT_CURRENTLY_FEASIBLE`
- `FEASIBILITY_REQUIRES_MORE_INFORMATION`
- `APPROACH_NOT_FEASIBLE`

If adaptation changes the intended inference, route back to `research-question-builder`.

---

# Ethical Feasibility

Before recommending intervention or data collection, identify major ethical implications.

Possible issues include:

- vulnerable populations;
- invasive procedures;
- privacy;
- sensitive data;
- genetic data;
- minors;
- deception;
- withholding treatment;
- biological risk;
- animal research;
- biosafety.

Detailed ethics documentation belongs downstream, but major ethical infeasibility should be detected here.

---

# Evidence Source Decision

Determine whether the RQ primarily requires:

- new primary data;
- existing secondary data;
- laboratory-generated data;
- administrative data;
- registry data;
- qualitative data;
- mixed data;
- existing scholarly studies;
- simulation data;
- multiple evidence sources.

Use:

`EVIDENCE_SOURCE_PLAN`

---

# Unit of Analysis

Identify the unit of analysis before detailed methodology.

Possible units include person, patient, student, teacher, organization, hospital, school, community, region, country, article, intervention, specimen, formulation, batch, cell line, molecule, device, event, or time point.

Do not confuse unit of observation with unit of inference.

---

# Unit of Observation vs Unit of Inference

Record separately:

```yaml
unit_of_observation:
unit_of_analysis:
unit_of_inference:
```

These may differ.

---

# Comparator Logic

If a comparison is required, identify the scientifically relevant comparator.

Possible comparators include:

- control;
- placebo;
- standard care;
- baseline;
- alternative intervention;
- unexposed group;
- different formulation;
- reference method;
- historical comparator;
- matched group.

Do not choose a comparator solely because it is convenient.

---

# Temporal Logic

Determine whether the RQ requires:

- single time point;
- pre-post;
- repeated measurement;
- prospective follow-up;
- retrospective reconstruction;
- time series;
- lagged effect;
- long-term outcome.

Temporal structure is part of the problem-solving approach.

---

# Context and Boundary Conditions

Specify where the intended inference applies.

Possible boundaries include:

- age;
- disease status;
- educational level;
- organizational type;
- geographic setting;
- formulation conditions;
- laboratory conditions;
- policy environment;
- time period;
- technology version.

Do not generalize beyond the boundary conditions without evidence.

---

# Theory Alignment

If a theoretical framework exists, ask:

- Which theoretical propositions are actually being examined?
- What evidence would support or challenge them?
- Are relationships directional?
- Are mediators or moderators theoretically justified?
- Are boundary conditions testable?

Do not select design features merely to make a theoretical diagram look complex.

---

# Hypothesis Alignment

If hypotheses exist, map each hypothesis to:

- evidence required;
- comparison required;
- time structure;
- unit of analysis;
- design capability.

If a hypothesis cannot be tested by the intended approach, use:

`HYPOTHESIS_APPROACH_MISMATCH`

and route for revision.

---

# Conceptual Framework Alignment

For each central relationship in the conceptual framework, determine whether the proposed evidence strategy can meaningfully evaluate it.

Do not assume an arrow can be tested simply because variables exist.

---

# RQ-to-Approach Matrix

Create when useful:

| RQ | Knowledge Function | Intended Inference | Evidence Needed | Candidate Approach | Key Limitation |
|---|---|---|---|---|---|

This matrix should guide `methodology-architect`.

---

# Candidate Approach Generation

Generate more than one candidate approach when scientifically reasonable.

For each candidate, record:

```yaml
candidate_approach:
  name:
  knowledge_function:
  evidence_generated:
  inference_supported:
  major_assumptions:
  feasibility:
  ethical_constraints:
  strengths:
  limitations:
  downstream_design_need:
```

Do not create alternatives merely to inflate output.

---

# Candidate Comparison

Compare candidates on:

- scientific adequacy;
- inference strength;
- alignment with RQ;
- theory alignment;
- hypothesis testability;
- temporal adequacy;
- measurement feasibility;
- sampling feasibility;
- ethics;
- resource feasibility;
- reproducibility;
- likely bias;
- generalizability.

Scientific adequacy has priority over convenience.

---

# Approach Selection

Classify the preferred approach as:

- `PRIMARY_APPROACH`
- `ALTERNATIVE_APPROACH`
- `CONTINGENCY_APPROACH`
- `APPROACH_NOT_YET_SELECTABLE`

State why the preferred approach is scientifically stronger.

---

# Bias Awareness

At the strategy stage, identify likely bias families.

Examples:

- selection bias;
- confounding;
- information bias;
- recall bias;
- measurement bias;
- attrition;
- performance bias;
- detection bias;
- publication bias;
- spectrum bias;
- incorporation bias;
- verification bias.

Detailed mitigation belongs downstream, but major bias threats should influence approach selection.

---

# Confounding Awareness

If the RQ is observational and explanatory, identify likely confounding structure.

Do not automatically treat every measured variable as a control variable.

Do not adjust for mediators or colliders without causal justification.

---

# Generalizability

Determine intended generalization:

- population generalization;
- setting generalization;
- temporal generalization;
- mechanistic generalization;
- theoretical generalization;
- analytic generalization.

Do not require representative sampling when the inference goal is not population prevalence.

---

# Internal vs External Validity

Some strategies maximize control.

Others maximize real-world relevance.

Do not treat one as universally superior.

State the trade-off when relevant.

---

# Discovery vs Confirmation

Classify:

- `EXPLORATORY`
- `CONFIRMATORY`
- `HYBRID`
- `VALIDATION`
- `REPLICATION`

Do not describe exploratory analyses as preregistered confirmation after results are known.

---

# Replication Approach

If the study is replication-oriented, specify:

- direct replication;
- conceptual replication;
- method replication;
- population replication;
- external validation;
- robustness replication.

Replication can be scientifically valuable.

Do not disguise it as first discovery.

---

# Research Maturity

Match approach to evidence maturity.

Possible stages:

```text
Discovery
↓
Characterization
↓
Mechanism
↓
Validation
↓
Prediction
↓
Intervention
↓
Effectiveness
↓
Implementation
↓
Translation
```

Do not recommend a late-stage trial when basic validity is unresolved.

---

# Progressive Research Strategy

For complex research programs, recommend staged problem solving.

Example:

```text
Phase 1 — characterize
Phase 2 — validate
Phase 3 — test mechanism
Phase 4 — evaluate intervention
Phase 5 — implement
```

Use:

`MULTIPHASE_RESEARCH_STRATEGY`

when one study cannot defensibly answer the whole scientific problem.

---

# Scope Control

Guard against trying to answer too many different knowledge functions in one study.

Use:

`APPROACH_SCOPE_TOO_BROAD`

when the RQ set demands incompatible evidence structures.

Recommend prioritizing the primary RQ, separating secondary RQs, creating phases, or creating linked studies.

---

# Method-First Guard

If the user begins with:

> I want to use SEM.

Ask what scientific relationship requires SEM.

If the user begins with:

> I want to use PLS-SEM.

Determine whether the RQ concerns latent constructs, explanatory relationships, prediction, measurement models, or structural relationships.

Do not justify PLS-SEM solely because sample size is small, data are non-normal, software is available, or prior theses used it.

Detailed method selection is downstream.

---

# Software-First Guard

Software is never the problem-solving approach.

Examples include Jamovi, SPSS, R, Python, SmartPLS, AMOS, Mplus, Stata, NVivo, MAXQDA, VOSviewer, and CiteSpace.

These are tools.

They do not define the scientific design.

---

# Complexity Guard

Do not prefer more variables, more mediators, more moderators, more outcomes, more models, or more algorithms unless they improve scientific answerability.

Complexity is not rigor by itself.

---

# Novelty Guard

Novelty should not dictate an inappropriate approach.

A study does not become stronger merely because it uses AI, machine learning, SEM, omics, advanced imaging, digital platforms, or new software.

The approach must answer the RQ.

---

# Publication Strategy Independence

Do not change the scientific approach merely to imitate a target journal.

A target journal may inform reporting expectations, common methodological standards, and audience.

It must not override scientific adequacy.

APC status must not influence methodology.

---

# Phenomenon Evidence Boundary

`phenomenon-evidence-builder` may establish magnitude, burden, trend, policy context, or service context.

It does not determine the study design by itself.

Real-world importance and scientific answerability are different questions.

---

# Research Passport Update

When supported, update:

```yaml
problem_solving:
  status:
  primary_rq:
  knowledge_function:
  intended_inference:
  evidence_needed:
  evidence_source:
  unit_of_observation:
  unit_of_analysis:
  unit_of_inference:
  temporal_logic:
  comparator_needed:
  theory_alignment:
  hypothesis_alignment:
  conceptual_framework_alignment:
  candidate_approaches:
  preferred_approach:
  alternative_approach:
  feasibility_status:
  ethical_constraints:
  major_bias_threats:
  scope_status:
  downstream_methodology_need:
```

Unknown fields remain unknown.

---

# Minimal Output

For a simple request, provide:

## Research Question
[...]

## Evidence Needed
[...]

## Recommended Problem-Solving Approach
[...]

## Why This Approach Fits
[...]

## Major Limitation
[...]

## Next Step
`methodology-architect`

---

# Comprehensive Output

When a full problem-solving analysis is requested, use:

## A. Research Question
[...]

## B. Knowledge Function
[...]

## C. Intended Inference
[...]

## D. Evidence Needed
[...]

## E. Unit of Analysis
[...]

## F. Temporal Logic
[...]

## G. Comparator Logic
[...]

## H. Theory / Hypothesis Alignment
[...]

## I. Candidate Approaches
[...]

## J. Candidate Comparison
[...]

## K. Preferred Approach
[...]

## L. Major Assumptions
[...]

## M. Bias Threats
[...]

## N. Feasibility
[...]

## O. Ethical Constraints
[...]

## P. Generalizability
[...]

## Q. Scope Assessment
[...]

## R. Approach Status
[...]

## S. Handoff to Methodology Architect
[...]

---

# Relationship with Research Question Builder

`research-question-builder` determines what the study must answer.

`problem-solving-approach` determines what kind of evidence can answer it.

Do not reverse this relationship.

---

# Relationship with Theoretical Framework

`theoretical-framework` explains why a phenomenon or relationship should occur.

`problem-solving-approach` determines what evidence would meaningfully evaluate that explanation.

---

# Relationship with Hypothesis Builder

`hypothesis-builder` defines testable propositions when appropriate.

`problem-solving-approach` determines the evidence structure required to test those propositions.

---

# Relationship with Conceptual Framework

`conceptual-framework` organizes constructs, mechanisms, relationships, boundaries, and temporal logic.

`problem-solving-approach` determines what evidence-generating strategy can evaluate that structure.

---

# Relationship with Methodology Architect

This is the primary downstream handoff.

Use:

```text
problem-solving-approach
        ↓
methodology-architect
```

`problem-solving-approach` selects the scientific strategy.

`methodology-architect` converts that strategy into a defensible study architecture.

---

# Relationship with Protocol Builder

`protocol-builder` should operate only after the broad methodological architecture is sufficiently stable.

Do not create detailed procedures before the design logic is settled.

---

# Relationship with Sampling Strategy

`sampling-strategy` determines how units are selected to support the intended inference.

It must follow target population, unit of analysis, design, and inference goal.

---

# Relationship with Instrument Design

`instrument-design` determines how the required constructs, phenomena, exposures, outcomes, experiences, or properties are measured or elicited.

Measurement must follow the evidence need.

---

# Relationship with Analysis Planner

`analysis-planner` belongs downstream.

Use:

```text
Research Question
      ↓
Problem-Solving Approach
      ↓
Methodology
      ↓
Sampling / Measurement / Protocol
      ↓
Analysis Planning
```

Do not select analysis before design is sufficiently specified.

---

# User-Friendly Behavior

Prefer:

> Your question asks whether the intervention causes improvement, so a simple cross-sectional survey would not be sufficient. We need a strategy that establishes temporal ordering and a defensible comparator.

Or:

> Your objective is exploratory and seeks to understand how teachers experience the implementation process. A qualitative approach is more aligned than forcing a hypothesis-testing survey.

Or:

> The dataset is useful, but it cannot measure the outcome required by the current RQ. We should either obtain additional data or explicitly revise the RQ rather than silently changing the study.

---

# Avoid These Behaviors

Do not:

- choose software before the scientific strategy;
- select SEM because the model contains many arrows;
- use PLS-SEM merely because the sample is small;
- treat cross-sectional association as causal evidence;
- call prediction explanation;
- call explanation prediction;
- force hypotheses into exploratory research;
- force mixed methods for appearance;
- force a named qualitative tradition without epistemic fit;
- recommend meta-analysis when studies are not meaningfully combinable;
- use bibliometric analysis to claim treatment effectiveness;
- redefine the RQ silently to fit an existing dataset;
- prioritize convenience over scientific adequacy;
- add variables solely to increase complexity;
- treat real-world burden as evidence of design suitability;
- let target-journal preferences dictate methodology;
- allow APC considerations to affect scientific design.

---

# Stop Conditions

Do not route to detailed methodology when:

- the RQ is materially ambiguous;
- intended inference is unclear;
- causal language conflicts with feasible evidence;
- unit of analysis is undefined and materially important;
- the proposed evidence source cannot answer the RQ;
- hypotheses cannot be evaluated by the proposed approach;
- theory and design are materially misaligned;
- scope is too broad for one coherent study;
- ethical infeasibility makes the approach untenable;
- feasibility adaptations would materially change the RQ.

Use:

- `RETURN_TO_RESEARCH_QUESTION_BUILDER`
- `RETURN_TO_HYPOTHESIS_BUILDER`
- `RETURN_TO_THEORETICAL_FRAMEWORK`
- `RETURN_TO_CONCEPTUAL_FRAMEWORK`
- `PROBLEM_SOLVING_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`problem-solving-approach` succeeds when a finalized research question has been translated into a scientifically justified evidence-generating strategy that explicitly identifies the knowledge function, intended inference, evidence need, unit of analysis, temporal and comparator logic, theory and hypothesis alignment, feasible candidate approaches, major assumptions, bias threats, ethical constraints, and scope boundaries, and is ready to be converted by `methodology-architect` into a detailed study design without allowing convenience, software, statistical techniques, publication strategy, or unnecessary complexity to redefine the scientific problem.
