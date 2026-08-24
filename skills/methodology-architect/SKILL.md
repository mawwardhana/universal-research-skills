---
name: methodology-architect
description: Design the complete methodological architecture required to answer a finalized research question and approved problem-solving approach. Use when the research logic is sufficiently stable and the researcher needs to determine the study design, setting, population, unit structure, exposure or intervention logic, comparator, timing, measurement architecture, sampling requirements, protocol structure, validity safeguards, bias control, feasibility, ethics, and downstream analysis requirements without allowing software or statistical preferences to dictate the design.
---

# Methodology Architect

## Purpose

`methodology-architect` converts an approved scientific problem-solving approach into a defensible study architecture.

Its central question is:

> What study design, population structure, timing, comparison logic, measurement system, sampling strategy, procedural architecture, and validity safeguards are required to generate evidence capable of answering the research question?

This skill operates after:

`problem-solving-approach`

and before detailed:

- protocol construction;
- sampling execution;
- instrument development;
- analysis planning.

It is the central design layer of Universal Research Skills.

---

# Core Principle

Use:

> Scientific question → evidence need → study architecture → protocol / sampling / measurement → analysis plan.

Do not reverse the sequence.

Do not begin with:

- statistical software;
- a preferred statistical test;
- SEM;
- PLS-SEM;
- regression;
- machine learning;
- thematic analysis;
- a familiar questionnaire;
- sample-size folklore.

The design must be capable of answering the research question before analysis is selected.

---

# Position in the Framework

Preferred architecture:

```text
Research Question
      ↓
Theory / Hypothesis / Conceptual Framework
when required
      ↓
problem-solving-approach
      ↓
methodology-architect
      │
      ├───────────────┬────────────────┐
      ▼               ▼                ▼
protocol-builder  sampling-strategy  instrument-design
      │               │                │
      └───────────────┴────────────────┘
                      ↓
                DESIGN READY
                      ↓
                analysis-planner
```

The branches are conditional.

Not every study requires every downstream skill in the same form.

---

# Required Upstream Context

Use established information from:

- `research-question-builder`;
- `hypothesis-builder`;
- `theoretical-framework`;
- `conceptual-framework`;
- `problem-solving-approach`;
- `phenomenon-evidence-builder`;
- `gap-validator`;
- `novelty-auditor`.

Do not ask the researcher to repeat information already known.

Minimum useful input normally includes:

- primary research question;
- research objective;
- intended inference;
- preferred problem-solving approach;
- target population or unit;
- outcome or phenomenon of interest;
- exposure / intervention / predictor when relevant;
- comparator when relevant;
- temporal logic;
- theory or mechanism when relevant;
- major feasibility constraints.

---

# Methodology Readiness Gate

Classify the project as:

- `READY_FOR_METHODOLOGY_ARCHITECTURE`
- `UPSTREAM_RQ_INCOMPLETE`
- `APPROACH_NOT_FINALIZED`
- `THEORY_DESIGN_MISMATCH`
- `HYPOTHESIS_DESIGN_MISMATCH`
- `CONCEPTUAL_FRAMEWORK_DESIGN_MISMATCH`
- `METHODOLOGY_ALREADY_ESTABLISHED`
- `METHODOLOGY_REQUIRES_REASSESSMENT`

Do not create a detailed study design when upstream scientific logic remains unstable.

---

# Research Design Function

Identify the dominant methodological function.

Possible design functions include:

- `DESCRIPTIVE`
- `ESTIMATIVE`
- `COMPARATIVE`
- `ASSOCIATIONAL`
- `CAUSAL`
- `MECHANISTIC`
- `PREDICTIVE`
- `DIAGNOSTIC`
- `PROGNOSTIC`
- `VALIDATION`
- `MEASUREMENT_DEVELOPMENT`
- `INTERVENTION_DEVELOPMENT`
- `INTERVENTION_EVALUATION`
- `IMPLEMENTATION`
- `QUALITATIVE_EXPLORATION`
- `QUALITATIVE_INTERPRETATION`
- `THEORY_BUILDING`
- `MIXED_METHOD_INTEGRATION`
- `EVIDENCE_SYNTHESIS`
- `BIBLIOMETRIC_MAPPING`
- `FORMULATION_DEVELOPMENT`
- `OPTIMIZATION`
- `STABILITY`
- `SAFETY`
- `PERFORMANCE_EVALUATION`

A study may contain secondary functions, but one primary function should normally be explicit.

---

# Methodological Paradigm

Classify the broad paradigm only when useful.

Possible statuses include:

- `QUANTITATIVE`
- `QUALITATIVE`
- `MIXED_METHOD`
- `EXPERIMENTAL_LABORATORY`
- `EVIDENCE_SYNTHESIS`
- `COMPUTATIONAL`
- `MULTIMETHOD`
- `PARADIGM_NOT_CENTRAL`

Do not force philosophical labels where they do not help design decisions.

---

# Design Family Selection

Candidate design families may include:

## Quantitative observational

- cross-sectional;
- cohort;
- case-control;
- longitudinal panel;
- registry-based;
- administrative-data;
- ecological;
- multilevel;
- repeated-measures observational.

## Experimental

- randomized controlled trial;
- cluster randomized trial;
- crossover trial;
- factorial experiment;
- laboratory experiment;
- formulation experiment;
- dose-response experiment;
- controlled bench study;
- simulation experiment.

## Quasi-experimental

- interrupted time series;
- controlled before-after;
- difference-in-differences;
- regression discontinuity;
- natural experiment;
- matched comparison.

## Qualitative

- phenomenology;
- grounded theory;
- case study;
- ethnography;
- narrative inquiry;
- qualitative description;
- interpretive description;
- framework-based inquiry.

## Mixed methods

- convergent;
- explanatory sequential;
- exploratory sequential;
- embedded;
- multiphase.

## Evidence synthesis

- systematic review;
- scoping review;
- rapid review;
- umbrella review;
- qualitative evidence synthesis;
- diagnostic review;
- prognostic review;
- meta-analysis when appropriate.

## Development and validation

- instrument development;
- diagnostic validation;
- prediction model development;
- external validation;
- intervention development;
- formulation development;
- implementation evaluation.

Do not choose a design family by popularity.

Choose it by scientific capability.

---

# Design Selection Logic

For each candidate design ask:

1. Can it answer the primary RQ?
2. Can it support the intended inference?
3. Does it preserve temporal logic?
4. Does it allow valid comparison when comparison is required?
5. Does it measure the necessary constructs or outcomes?
6. Can it handle the relevant unit structure?
7. Are major sources of bias manageable?
8. Is it ethically defensible?
9. Is it feasible?
10. Does it create analyzable evidence without distorting the RQ?

Select the smallest scientifically adequate design.

---

# Minimal Sufficient Design

Prefer:

`MINIMAL_SCIENTIFICALLY_ADEQUATE_DESIGN`

over unnecessary complexity.

A more complicated design is not automatically better.

Do not add:

- extra waves;
- extra groups;
- extra constructs;
- extra experiments;
- extra qualitative strands;
- extra algorithms;

unless they materially improve answerability.

---

# Primary and Secondary Research Questions

Separate:

- primary RQ;
- secondary RQs;
- exploratory RQs.

The design must primarily protect the primary RQ.

Do not sacrifice primary-study validity to accommodate too many secondary questions.

---

# Primary Outcome or Primary Phenomenon

Identify the central outcome, phenomenon, construct, or target performance measure.

Use:

```yaml
primary_target:
  type:
  definition:
  measurement_role:
  timing:
```

Do not define multiple co-primary outcomes casually.

---

# Exposure / Intervention / Predictor Logic

When relevant, define:

```yaml
exposure_or_intervention:
  name:
  operational_definition:
  assignment_or_occurrence:
  timing:
  dose_or_intensity:
  duration:
  fidelity_need:
```

Distinguish:

- assigned intervention;
- naturally occurring exposure;
- predictor;
- risk factor;
- covariate.

Do not call all predictors exposures.

---

# Comparator Architecture

When comparison is required, define:

- no intervention;
- placebo;
- standard care;
- alternative intervention;
- baseline;
- unexposed;
- matched comparator;
- reference formulation;
- reference method;
- historical control;
- within-subject comparison.

The comparator must be scientifically meaningful.

---

# Counterfactual Logic

For causal studies, explicitly identify:

> What would have happened to the same or comparable unit under the alternative condition?

The study architecture should approximate this counterfactual as defensibly as possible.

Do not use causal terminology when no credible counterfactual logic exists.

---

# Randomization

Use randomization when:

- assignment is feasible;
- ethical;
- scientifically meaningful;
- the intervention can be controlled.

Specify whether randomization is:

- individual;
- cluster;
- block;
- stratified;
- factorial;
- crossover-order.

Detailed implementation belongs to `protocol-builder`.

---

# Allocation Concealment

When relevant, distinguish allocation concealment from blinding.

Allocation concealment prevents foreknowledge of assignment before allocation.

Do not treat it as synonymous with participant blinding.

---

# Blinding / Masking

Determine whether blinding is relevant for:

- participants;
- investigators;
- outcome assessors;
- laboratory analysts;
- statisticians.

If blinding is impossible, identify alternative bias-control strategies.

---

# Experimental Unit

For experiments, define the experimental unit.

Possible examples:

- person;
- class;
- hospital;
- animal;
- specimen;
- plate;
- formulation batch;
- well;
- device;
- production batch.

Do not confuse technical replicates with independent experimental units.

---

# Biological vs Technical Replication

For laboratory studies distinguish:

- biological replicate;
- technical replicate;
- batch replicate;
- repeated measurement.

Technical replicates improve measurement precision.

They do not automatically increase independent sample size.

---

# Pseudoreplication Guard

Flag:

`PSEUDOREPLICATION_RISK`

when repeated measurements or subsamples are treated as independent experimental units.

---

# Cross-Sectional Architecture

Use cross-sectional designs when the evidence need concerns:

- prevalence;
- characteristics;
- contemporaneous association;
- measurement structure under appropriate conditions.

Do not claim temporal sequence from one-time measurement without external justification.

---

# Cohort Architecture

Specify:

- source population;
- entry point;
- baseline;
- exposure definition;
- follow-up;
- outcome ascertainment;
- censoring;
- loss to follow-up.

Use prospective or retrospective cohort logic according to data provenance.

---

# Case-Control Architecture

Specify:

- case definition;
- control source;
- source population;
- exposure ascertainment;
- matching if used;
- selection safeguards.

Controls should represent the population that generated the cases.

---

# Longitudinal Architecture

Specify:

- number of waves;
- interval;
- follow-up duration;
- outcome timing;
- exposure timing;
- repeated measures;
- attrition strategy.

Timing should follow the mechanism or process being studied.

---

# Time-Series Architecture

For time-series designs specify:

- time unit;
- number of pre-event observations;
- number of post-event observations;
- intervention or event time;
- seasonality;
- secular trend;
- autocorrelation considerations.

Detailed modeling belongs downstream.

---

# Quasi-Experimental Identification

For quasi-experimental designs identify:

- treatment assignment mechanism;
- comparison basis;
- identification assumption;
- falsification or placebo checks where appropriate;
- pre-intervention comparability;
- spillover risk.

Do not use quasi-experimental labels without design-specific identification logic.

---

# Qualitative Architecture

For qualitative designs specify:

- phenomenon of interest;
- epistemic purpose;
- participant or case type;
- context;
- data source;
- unit of meaning;
- sampling logic;
- saturation or information-power logic where appropriate;
- reflexivity needs;
- analytic orientation.

Do not force statistical representativeness onto qualitative inquiry.

---

# Qualitative Tradition Fit

Select a named tradition only when it changes:

- question framing;
- sampling;
- data collection;
- interpretation;
- analytic logic.

Otherwise use a clear generic qualitative design.

---

# Case Study Architecture

For case study research define:

- case boundary;
- unit of case;
- embedded units where relevant;
- context;
- data sources;
- within-case logic;
- cross-case logic when multiple cases exist.

Do not call any small-sample study a case study.

---

# Grounded Theory Architecture

Use grounded theory when the goal is substantive theory generation from iterative data collection and analysis.

The architecture should allow:

- theoretical sampling;
- constant comparison;
- category development;
- iterative refinement.

Do not use grounded theory merely because interviews are conducted.

---

# Phenomenological Architecture

Use phenomenological approaches when the RQ genuinely concerns lived experience and meaning.

Sampling, interviewing, and interpretation should align with the chosen phenomenological orientation.

---

# Mixed-Method Architecture

For mixed methods define:

```yaml
mixed_method:
  purpose:
  quantitative_strand:
  qualitative_strand:
  sequence:
  priority:
  integration_point:
  integration_product:
```

Integration must be explicit.

---

# Mixed-Method Integration

Possible integration points include:

- design;
- sampling;
- data collection;
- analysis;
- interpretation;
- joint display;
- meta-inference.

Do not label parallel studies as mixed methods without integration.

---

# Systematic Review Architecture

Define:

- review question;
- eligibility framework;
- information sources;
- search strategy requirements;
- screening process;
- extraction architecture;
- risk-of-bias appraisal;
- synthesis approach.

Do not duplicate detailed literature-search mechanics already handled by evidence skills.

---

# Scoping Review Architecture

Use when the purpose is mapping:

- concepts;
- evidence types;
- definitions;
- methods;
- research distribution;
- knowledge structure.

Do not use a scoping review to make effect estimates that require systematic quantitative synthesis.

---

# Meta-Analysis Readiness

Flag:

- `META_ANALYSIS_POSSIBLE`
- `META_ANALYSIS_NOT_YET_JUSTIFIED`
- `META_ANALYSIS_INAPPROPRIATE`

based on comparability of studies, outcomes, estimands, and quantitative information.

Detailed meta-analysis belongs downstream.

---

# Bibliometric Architecture

Specify:

- corpus definition;
- database;
- time range;
- document types;
- bibliometric unit;
- network type;
- normalization needs;
- reproducibility strategy.

Bibliometric architecture studies literature structure, not substantive causal effect.

---

# Secondary-Data Architecture

For existing datasets define:

- data owner;
- dataset version;
- collection purpose;
- population coverage;
- observation period;
- variables;
- missingness;
- measurement quality;
- linkage structure;
- access conditions.

Use only if the dataset can answer the RQ.

---

# Administrative and Registry Data

Identify:

- coverage;
- coding practices;
- reporting lag;
- eligibility;
- data-generating process;
- changes in definitions;
- completeness;
- linkage error;
- ascertainment bias.

Large datasets are not automatically unbiased.

---

# Laboratory Architecture

For laboratory research define:

- material or biological system;
- experimental unit;
- batch structure;
- control;
- comparator;
- concentration or dose;
- incubation or exposure conditions;
- environmental conditions;
- assay timing;
- replicate structure;
- instrument calibration;
- quality-control needs.

---

# Pharmaceutical Formulation Architecture

For formulation studies define:

```text
Material / Active Ingredient
          ↓
Formulation Factors
          ↓
Processing Conditions
          ↓
Physicochemical Properties
          ↓
Performance
          ↓
Biological / Functional Evaluation
```

Specify:

- formulation factors;
- fixed components;
- varied components;
- batch number;
- control formulation;
- quality attributes;
- stability conditions;
- biological testing when relevant.

Do not treat formulation variation as replication.

---

# Optimization Architecture

For optimization studies identify:

- factors;
- factor ranges;
- responses;
- constraints;
- optimization objective;
- confirmation run;
- validation strategy.

Do not optimize before scientifically meaningful responses are defined.

---

# Stability Study Architecture

Specify:

- storage conditions;
- packaging;
- time points;
- critical quality attributes;
- acceptance criteria;
- degradation indicators;
- stress conditions if appropriate.

Do not infer long-term stability from a single short observation without justification.

---

# Microbiological Study Architecture

Define:

- organism;
- strain;
- inoculum;
- growth conditions;
- test method;
- positive control;
- negative control;
- solvent control;
- replicate structure;
- endpoint;
- diffusion limitations where relevant.

Distinguish screening assays from quantitative susceptibility testing.

---

# Pharmacokinetic Architecture

Define:

- population;
- dose;
- route;
- sampling schedule;
- analyte;
- matrix;
- assay;
- exposure metrics;
- covariates;
- repeated-measure structure.

PK sampling must reflect the intended parameter estimation.

---

# Pharmacogenetic / Pharmacogenomic Architecture

Define:

- gene / variant;
- genotype method;
- phenotype / clinical outcome;
- treatment exposure;
- population ancestry or relevant population structure;
- confounding;
- multiple-testing implications;
- quality control;
- Hardy–Weinberg evaluation where appropriate;
- replication or validation plan.

Do not infer pharmacogenetic causality from genotype association alone.

---

# Diagnostic Study Architecture

Define:

- target condition;
- index test;
- reference standard;
- target population;
- case spectrum;
- threshold;
- blinding;
- timing between tests;
- indeterminate results;
- verification pathway.

Avoid spectrum and verification bias.

---

# Prediction Model Architecture

Define:

- target population;
- outcome;
- prediction time point;
- prediction horizon;
- candidate predictors;
- model-development dataset;
- internal validation;
- external validation;
- missing-data strategy;
- overfitting safeguards.

Do not select algorithms before the prediction problem is defined.

---

# Instrument Development Architecture

Define phases:

```text
Construct Definition
      ↓
Item / Indicator Generation
      ↓
Content Evaluation
      ↓
Pilot
      ↓
Structural Evaluation
      ↓
Reliability
      ↓
Validity
      ↓
External / Cross-Group Validation
```

Do not begin with statistical factor analysis before content validity.

---

# Intervention Development Architecture

Possible phases:

```text
Needs Assessment
      ↓
Intervention Logic
      ↓
Prototype
      ↓
Feasibility
      ↓
Pilot
      ↓
Efficacy
      ↓
Effectiveness
      ↓
Implementation
```

Match design maturity to evidence maturity.

---

# Implementation Research Architecture

Define:

- intervention or practice;
- implementation strategy;
- setting;
- actors;
- context;
- implementation outcomes;
- service outcomes;
- clinical or educational outcomes where relevant;
- fidelity;
- adaptation;
- sustainability.

Do not collapse implementation outcomes into effectiveness outcomes.

---

# Education Research Architecture

Potential units include:

- student;
- teacher;
- classroom;
- school;
- program.

Define:

- educational intervention or exposure;
- learning outcome;
- timing;
- classroom nesting;
- instructor effects;
- implementation fidelity;
- contextual factors.

Do not ignore clustering when students are nested in classes.

---

# Organizational Research Architecture

Potential units include:

- employee;
- team;
- department;
- organization.

Define whether constructs operate at:

- individual level;
- team level;
- organizational level.

Do not aggregate individual data to organizational constructs without justification.

---

# Policy Evaluation Architecture

Define:

- policy;
- implementation date;
- jurisdiction;
- affected population;
- comparator;
- pre-policy period;
- post-policy period;
- competing policy changes;
- outcome;
- spillover.

Policy publication alone does not establish impact.

---

# Population Definition

Define:

```yaml
population:
  target_population:
  source_population:
  accessible_population:
  inclusion_criteria:
  exclusion_criteria:
  setting:
  recruitment_source:
```

Do not conflate target population with accessible sample.

---

# Eligibility Criteria

Eligibility criteria should follow:

- research question;
- safety;
- target population;
- measurement feasibility;
- design validity.

Do not exclude participants merely to simplify analysis unless scientifically justified.

---

# Setting

Specify:

- country;
- region;
- institution;
- clinical setting;
- educational setting;
- laboratory;
- online environment;
- community;
- organizational environment.

Setting is a boundary condition.

---

# Unit Structure

Record separately:

```yaml
unit_structure:
  unit_of_observation:
  unit_of_analysis:
  unit_of_assignment:
  unit_of_inference:
  clustering:
  repeated_measurement:
```

These may differ.

---

# Sampling Handoff

`methodology-architect` defines what sampling must achieve.

`sampling-strategy` determines how to achieve it.

Handoff should include:

- target population;
- source population;
- unit;
- sampling frame;
- required representativeness;
- strata;
- clusters;
- expected effect or precision need where relevant;
- attrition expectations;
- feasibility constraints.

Do not calculate final sample size here unless needed only to test design feasibility.

---

# Measurement Architecture

Define what must be measured.

Possible categories:

- exposure;
- intervention;
- outcome;
- mediator;
- moderator;
- confounder;
- context;
- process;
- fidelity;
- safety;
- qualitative phenomenon;
- laboratory property.

For each important variable or construct record:

```yaml
measurement_requirement:
  concept:
  role:
  operational_definition:
  timing:
  source:
  quality_requirement:
```

Detailed instrument construction belongs to `instrument-design`.

---

# Measurement Timing

Measurement time points should reflect:

- causal order;
- mechanism;
- intervention exposure;
- expected response time;
- clinical relevance;
- educational cycle;
- formulation stability;
- longitudinal trajectory.

Do not choose timing only because it is convenient.

---

# Measurement Source

Possible sources include:

- self-report;
- observer rating;
- clinical record;
- laboratory assay;
- device;
- registry;
- interview;
- focus group;
- document;
- administrative system;
- direct observation;
- sensor;
- validated scale.

Each source has different bias implications.

---

# Instrument Handoff

Provide `instrument-design` with:

- construct definition;
- measurement role;
- respondent / specimen;
- timing;
- required precision;
- validity need;
- language / cultural context;
- existing instrument availability;
- adaptation need;
- new-development need.

---

# Protocol Handoff

Provide `protocol-builder` with:

- study design;
- setting;
- participant flow;
- intervention or exposure;
- comparator;
- measurement schedule;
- randomization;
- blinding;
- data collection;
- safety;
- quality control;
- data management;
- deviations;
- monitoring.

---

# Temporal Architecture

Specify:

- study start;
- enrollment window;
- baseline;
- exposure period;
- intervention duration;
- follow-up;
- measurement waves;
- endpoint;
- long-term follow-up where required.

Do not add follow-up duration without mechanism or clinical justification.

---

# Participant / Unit Flow

When useful define:

```text
Eligible
  ↓
Approached
  ↓
Consented / Included
  ↓
Assigned / Classified
  ↓
Measured
  ↓
Followed
  ↓
Analyzed
```

For non-human studies adapt terminology accordingly.

---

# Attrition

For longitudinal designs identify:

- expected attrition;
- reasons;
- differential attrition risk;
- retention strategy;
- outcome ascertainment after dropout when possible.

Do not wait until analysis to consider attrition.

---

# Missing Data Prevention

Design should prevent avoidable missingness through:

- measurement scheduling;
- instrument design;
- data validation;
- follow-up;
- required-field logic;
- laboratory quality control.

Missing-data analysis strategies belong downstream.

---

# Data Quality Architecture

Specify relevant quality safeguards:

- training;
- calibration;
- pilot testing;
- standard operating procedures;
- duplicate measurement;
- inter-rater agreement;
- laboratory controls;
- audit trail;
- data validation;
- range checks;
- version control.

---

# Validity Architecture

Assess:

- internal validity;
- external validity;
- construct validity;
- measurement validity;
- ecological validity;
- statistical conclusion validity as a downstream concern.

Not every design optimizes all forms equally.

Make trade-offs explicit.

---

# Bias Architecture

Identify likely design-stage bias:

- selection bias;
- confounding;
- performance bias;
- detection bias;
- recall bias;
- measurement bias;
- attrition bias;
- interviewer bias;
- observer bias;
- contamination;
- co-intervention;
- reporting bias;
- spectrum bias;
- verification bias.

For each major threat record:

```yaml
bias_control:
  threat:
  design_source:
  prevention:
  residual_risk:
```

---

# Confounding Architecture

For observational causal or explanatory research identify:

- potential causes of exposure;
- potential causes of outcome;
- mediators;
- colliders;
- baseline prognostic factors.

Do not adjust indiscriminately for every available variable.

---

# Causal Diagram Handoff

If a causal structure is central, recommend explicit causal diagrams or equivalent reasoning before analysis planning.

Do not create arrows solely from correlation.

---

# Contamination

When comparison groups can influence each other, assess contamination risk.

Possible controls include:

- cluster assignment;
- separation;
- scheduling;
- standardized instructions;
- monitoring.

---

# Intervention Fidelity

For intervention research define whether fidelity must capture:

- adherence;
- dose delivered;
- dose received;
- quality;
- participant responsiveness;
- protocol deviations.

---

# Safety Architecture

When relevant define:

- adverse events;
- serious adverse events;
- stopping criteria;
- laboratory safety;
- biosafety;
- participant escalation;
- device failures;
- product defects.

---

# Ethics Architecture

Identify whether the design requires:

- informed consent;
- assent;
- parental permission;
- waiver;
- privacy safeguards;
- sensitive-data controls;
- genetic-data safeguards;
- clinical-risk management;
- animal ethics;
- biosafety approval.

Do not invent jurisdiction-specific requirements without verification.

---

# Privacy and Data Protection

Design data flow according to minimum necessary access.

Consider:

- direct identifiers;
- coded identifiers;
- pseudonymization;
- anonymization;
- access control;
- secure storage;
- linkage keys;
- retention.

Detailed regulatory compliance depends on jurisdiction.

---

# Feasibility Architecture

Assess:

- participant access;
- recruitment rate;
- follow-up burden;
- equipment;
- laboratory capacity;
- costs;
- investigator expertise;
- data availability;
- timeline;
- approvals;
- logistics.

Classify:

- `FEASIBLE`
- `FEASIBLE_WITH_MODIFICATION`
- `FEASIBILITY_UNCERTAIN`
- `NOT_FEASIBLE`

---

# Pilot Need

Recommend a pilot when major uncertainty exists about:

- recruitment;
- intervention delivery;
- instrument usability;
- laboratory workflow;
- data capture;
- adherence;
- timing;
- feasibility.

Do not describe a pilot as a definitive effectiveness study.

---

# Preregistration

Recommend preregistration or protocol registration where appropriate for:

- confirmatory hypotheses;
- clinical trials;
- systematic reviews;
- major observational analyses;
- registered reports.

Do not claim preregistration after data analysis has begun.

---

# Reproducibility

A design is not sufficiently specified if another competent researcher cannot understand:

- who or what was studied;
- how units were selected;
- what was done;
- what was measured;
- when it was measured;
- what comparison was made;
- how quality was protected.

---

# Open Science

When appropriate consider:

- protocol availability;
- preregistration;
- code sharing;
- data dictionary;
- de-identified data sharing;
- materials;
- analysis scripts.

Do not promise data sharing when ethical or legal constraints prohibit it.

---

# Analysis Readiness Handoff

Do not choose the final analysis method here.

Instead define the analysis requirements that downstream planning must satisfy.

Record:

```yaml
analysis_requirements:
  primary_estimand_or_target:
  outcome_type:
  exposure_or_intervention_type:
  repeated_measures:
  clustering:
  time_to_event:
  latent_constructs:
  prediction_goal:
  causal_goal:
  missing_data_context:
  multiplicity_context:
  qualitative_data_type:
  integration_need:
```

Then route to:

`analysis-planner`

---

# Estimand Awareness

For intervention or causal studies, define what effect is scientifically targeted.

Examples include:

- average treatment effect;
- effect among treated;
- intention-to-treat contrast;
- per-protocol contrast;
- risk difference;
- risk ratio;
- mean difference;
- change difference.

Do not select estimands solely because software reports them.

Detailed statistical specification belongs downstream.

---

# Precision vs Power

Sampling may be driven by:

- estimation precision;
- hypothesis power;
- event availability;
- saturation / information power;
- model validation needs;
- laboratory replication.

Do not assume every sample-size problem is a power calculation.

---

# Multiplicity Awareness

Identify design-level multiplicity from:

- multiple primary outcomes;
- multiple groups;
- multiple time points;
- multiple hypotheses;
- many biomarkers;
- many genetic variants.

Detailed correction belongs downstream.

---

# Data Structure

Record whether the design generates:

- independent observations;
- paired observations;
- repeated measures;
- clustered data;
- hierarchical data;
- longitudinal data;
- survival data;
- network data;
- compositional data;
- high-dimensional data;
- qualitative text;
- image data;
- sensor streams;
- mixed data.

---

# Design Documentation Schema

Recommended internal structure:

```yaml
methodology:
  status:
  primary_rq:
  primary_objective:
  design_function:
  paradigm:
  preferred_design:
  alternative_design:
  setting:
  target_population:
  source_population:
  eligibility:
  unit_of_observation:
  unit_of_analysis:
  unit_of_assignment:
  unit_of_inference:
  exposure_or_intervention:
  comparator:
  primary_target:
  secondary_targets:
  temporal_structure:
  sampling_requirements:
  measurement_requirements:
  protocol_requirements:
  randomization:
  blinding:
  clustering:
  repeated_measurement:
  bias_threats:
  validity_strategy:
  feasibility:
  ethics:
  pilot_need:
  reproducibility:
  analysis_requirements:
  downstream_handoff:
```

Unknown fields remain unknown.

---

# Candidate Design Comparison

When more than one design is defensible, compare:

| Candidate | RQ Fit | Inference Strength | Bias Risk | Feasibility | Ethics | Measurement Fit | Reproducibility |
|---|---|---|---|---|---|---|---|

Do not compare designs by prestige.

---

# Methodology Decision

Use:

- `PREFERRED_DESIGN`
- `ALTERNATIVE_DESIGN`
- `CONTINGENCY_DESIGN`
- `DESIGN_NOT_YET_SELECTABLE`

Explain why.

---

# Design Revision

If feasibility requires modification, distinguish:

`IMPLEMENTATION_ADAPTATION`

from:

`SCIENTIFIC_DESIGN_CHANGE`

If scientific inference changes, route back upstream.

---

# Scope Control

Use:

`METHODOLOGY_SCOPE_TOO_BROAD`

when one study is expected to perform incompatible functions such as:

- instrument development;
- causal evaluation;
- long-term implementation;
- external validation;

all at once without sufficient phases.

Recommend staged research when needed.

---

# Multiphase Architecture

Possible structure:

```text
Phase 1 — development
Phase 2 — feasibility
Phase 3 — validation
Phase 4 — effectiveness
Phase 5 — implementation
```

Each phase should have its own RQ and design logic where necessary.

---

# Domain Adaptation

This skill is universal.

Adapt terminology according to domain without changing core design logic.

Supported examples include:

- health;
- pharmacy;
- biomedical science;
- education;
- psychology;
- social science;
- organizational research;
- engineering;
- computer science;
- public policy;
- environmental science;
- laboratory science;
- formulation research;
- implementation science.

---

# Method Adapter Awareness

Detailed domain- or method-specific modules may later refine:

- quantitative;
- qualitative;
- mixed-method;
- systematic review;
- meta-analysis;
- SEM;
- PLS-SEM;
- bibliometric;
- experimental.

`methodology-architect` should define the design requirements before handing off.

---

# Software Independence

Do not allow:

- Jamovi;
- SPSS;
- SmartPLS;
- AMOS;
- Mplus;
- R;
- Python;
- Stata;
- NVivo;
- MAXQDA;

to define the study architecture.

Software compatibility is downstream.

---

# SEM Guard

SEM is an analytical modeling family.

It is not a study design.

A study using SEM still requires:

- valid RQ;
- design;
- population;
- sampling;
- measurement;
- timing;
- bias control.

---

# PLS-SEM Guard

PLS-SEM is not justified solely by:

- small sample;
- non-normality;
- exploratory wording;
- software availability.

Its use must be evaluated downstream according to the measurement and structural modeling goal.

---

# Machine-Learning Guard

Machine learning is not a methodology by itself.

Prediction research still requires:

- target population;
- outcome;
- prediction timing;
- data provenance;
- validation architecture;
- leakage prevention;
- generalization target.

---

# Target Journal Independence

Target-journal preferences may inform reporting standards.

They must not change the design merely to imitate published articles.

Do not add complexity for perceived publication attractiveness.

---

# APC Independence

Publication cost does not affect scientific design.

---

# User-Friendly Behavior

Prefer:

> Your research question requires a causal contrast. The design therefore needs a defensible comparator and temporal ordering; a one-time survey would not be sufficient.

Or:

> Your study is primarily instrument development. Before choosing factor analysis, we first need a design that establishes the construct domain, content validity, pilot testing, structural evaluation, reliability, and external validation.

Or:

> Because students are nested within classrooms, the design must preserve clustering from the beginning. This is a design issue, not something to fix only at the analysis stage.

---

# Minimal Output

For a simple request, provide:

## Recommended Design
[...]

## Why It Fits
[...]

## Population / Unit
[...]

## Comparator / Timing
[...]

## Measurement Need
[...]

## Major Bias Safeguard
[...]

## Next Handoff
`protocol-builder`, `sampling-strategy`, and/or `instrument-design`

---

# Comprehensive Output

When full methodology architecture is requested:

## A. Research Question
[...]

## B. Intended Inference
[...]

## C. Design Function
[...]

## D. Recommended Design
[...]

## E. Alternative Design
[...]

## F. Setting
[...]

## G. Population
[...]

## H. Unit Structure
[...]

## I. Exposure / Intervention
[...]

## J. Comparator
[...]

## K. Outcomes / Phenomena
[...]

## L. Temporal Architecture
[...]

## M. Sampling Requirements
[...]

## N. Measurement Architecture
[...]

## O. Protocol Requirements
[...]

## P. Bias and Validity Safeguards
[...]

## Q. Ethics
[...]

## R. Feasibility
[...]

## S. Pilot Need
[...]

## T. Reproducibility
[...]

## U. Analysis Requirements
[...]

## V. Downstream Handoff
[...]

---

# Relationship with Problem-Solving Approach

`problem-solving-approach` determines what evidence-generating strategy is scientifically appropriate.

`methodology-architect` turns that strategy into a complete study architecture.

Do not reverse the relationship.

---

# Relationship with Research Question Builder

The RQ defines what must be answered.

Methodology defines how the necessary evidence will be generated.

If methodology cannot answer the RQ, route back upstream.

---

# Relationship with Theoretical Framework

Theory may determine:

- expected mechanism;
- relevant constructs;
- temporal order;
- boundary conditions.

Methodology should make those scientifically observable where appropriate.

---

# Relationship with Hypothesis Builder

Each confirmatory hypothesis must map to a design capable of evaluating it.

If not, use:

`HYPOTHESIS_DESIGN_MISMATCH`

---

# Relationship with Conceptual Framework

The conceptual framework organizes study-specific relationships.

Methodology determines how those relationships are observed, manipulated, measured, or interpreted.

---

# Relationship with Protocol Builder

`protocol-builder` operationalizes the methodology into reproducible procedures.

Use:

```text
methodology-architect
      ↓
protocol-builder
```

when procedural detail is needed.

---

# Relationship with Sampling Strategy

`methodology-architect` defines the population, units, design structure, and sampling requirements.

`sampling-strategy` determines the specific selection and sample-size plan.

---

# Relationship with Instrument Design

`methodology-architect` defines what must be measured.

`instrument-design` determines how valid measurement will be achieved.

---

# Relationship with Analysis Planner

`methodology-architect` defines the data-generating design and analysis requirements.

`analysis-planner` later selects an analysis strategy compatible with those requirements.

---

# Avoid These Behaviors

Do not:

- select a statistical test before the study architecture;
- treat SEM or PLS-SEM as research designs;
- use cross-sectional designs for causal claims without qualification;
- ignore clustering;
- count technical replicates as independent samples;
- ignore temporal ordering;
- use convenience sampling when population inference is central without acknowledging the limitation;
- select a familiar questionnaire before defining the construct;
- add outcomes merely because they are available;
- overcomplicate the study for publication appearance;
- let software availability dictate methodology;
- call a pilot study definitive effectiveness evidence;
- confuse diagnostic, predictive, explanatory, and causal studies;
- confuse policy content with policy impact;
- confuse qualitative sample adequacy with statistical power;
- change the RQ silently to fit existing data;
- claim external validity beyond the source population;
- ignore ethics until after design completion.

---

# Stop Conditions

Do not classify methodology as ready when:

- primary RQ is unresolved;
- intended inference is unclear;
- preferred design cannot support the intended inference;
- population is undefined;
- experimental unit is ambiguous where relevant;
- comparator is required but absent;
- temporal logic conflicts with the RQ;
- measurement requirements are undefined;
- sampling requirements cannot support the intended inference;
- major bias is structurally unavoidable without redesign;
- ethical constraints invalidate the design;
- feasibility changes would materially alter the scientific question;
- design depends primarily on software preference.

Use:

- `RETURN_TO_PROBLEM_SOLVING_APPROACH`
- `RETURN_TO_RESEARCH_QUESTION_BUILDER`
- `RETURN_TO_THEORETICAL_FRAMEWORK`
- `RETURN_TO_HYPOTHESIS_BUILDER`
- `RETURN_TO_CONCEPTUAL_FRAMEWORK`
- `METHODOLOGY_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`methodology-architect` succeeds when an approved problem-solving approach has been translated into the smallest scientifically adequate, ethically defensible, feasible, and reproducible study architecture that explicitly defines the design function, study design, setting, population, unit structure, exposure or intervention, comparator, outcomes or phenomena, temporal logic, sampling requirements, measurement requirements, protocol requirements, validity and bias safeguards, feasibility constraints, and downstream analysis requirements, and is ready to hand off to `protocol-builder`, `sampling-strategy`, `instrument-design`, and ultimately `analysis-planner` without allowing software, statistical preferences, publication strategy, or unnecessary complexity to redefine the research question.
