---
name: registration-preregistration-builder
description: Design, document, compare, and maintain transparent study registration and preregistration records that distinguish prespecified confirmatory decisions from exploratory or post-hoc decisions without treating registration as ethics approval, scientific validity, or an immutable contract. Use after the research question, design, outcomes, sampling logic, measurement plan, and analysis strategy are sufficiently stable and before data collection, outcome access, final analysis, major protocol changes, or submission where prospective registration or preregistration is scientifically useful or required. This skill supports protocol registration, trial registration, review registration, observational-study registration, analysis-plan preregistration, registered-report preparation, deviation tracking, amendment versioning, and final planned-vs-implemented comparison while preventing HARKing, undisclosed outcome switching, undisclosed analytic flexibility, retrospective preregistration, and fabricated registration identifiers.
---

# Registration Preregistration Builder

## Purpose

`registration-preregistration-builder` creates and maintains a transparent prospective record of what the researcher intended to do, what was actually done, what changed, when it changed, why it changed, and which analyses remain confirmatory, exploratory, amended, or post-hoc.

Its central question is:

> What scientific decisions should be fixed, time-stamped, versioned, registered, or preregistered before relevant evidence is observed, and how should later deviations, amendments, exploratory analyses, and final reporting be documented so that the scientific record remains transparent?

The core logic is:

```text
RESEARCH QUESTION
        ↓
OBJECTIVES / HYPOTHESES
        ↓
DESIGN
        ↓
OUTCOMES / VARIABLES
        ↓
SAMPLING
        ↓
ANALYSIS PLAN
        ↓
REGISTRATION / PREREGISTRATION
        ↓
IMPLEMENTATION
        ↓
DEVIATION TRACKING
        ↓
FINAL ANALYSIS
        ↓
TRANSPARENT REPORTING
```

---

# 1. Core Principles

Preserve the following distinctions:

```text
PREREGISTRATION ≠ ETHICS APPROVAL
REGISTRATION ≠ SCIENTIFIC VALIDITY
REGISTERED ≠ IMMUTABLE
DEVIATION ≠ AUTOMATIC MISCONDUCT
POST-HOC ≠ FORBIDDEN
EXPLORATORY ≠ CONFIRMATORY
UNREGISTERED ≠ AUTOMATICALLY INVALID
REGISTERED ≠ AUTOMATICALLY REPRODUCIBLE
TIMESTAMP ≠ QUALITY
```

The scientific goal is not ritual compliance.

The goal is transparency about what was planned, what was changed, and what was learned after observing evidence.

---

# 2. Activation Gate

Use `registration-preregistration-builder` when one or more of the following apply:

- a confirmatory study is being planned;
- a clinical trial requires prospective registration;
- a systematic review or meta-analysis should be registered;
- a study has multiple outcomes or analytic options;
- the researcher wants to reduce undisclosed analytic flexibility;
- a registered report is being prepared;
- an observational study would benefit from prospective specification;
- secondary-data analysis can still be preregistered before outcome analysis;
- a replication study is planned;
- a validation study is planned;
- a prediction model is being externally validated;
- a complex SEM or PLS-SEM model has multiple plausible specifications;
- a qualitative or mixed-method study uses prespecified procedural commitments;
- major reviewer-driven analyses are being added after initial registration;
- protocol amendments must be documented;
- or the manuscript needs a planned-vs-conducted transparency table.

Do not force preregistration onto every research activity.

If the study is purely exploratory, retrospective with all outcomes already inspected, or structurally unsuitable for meaningful prospective commitment, use transparent labeling instead of pretending preregistration occurred.

---

# 3. Required Upstream Context

Use, when available:

- research question;
- objectives;
- hypotheses;
- theoretical framework;
- conceptual framework;
- problem-solving approach;
- methodology;
- protocol;
- sampling strategy;
- instrument or measurement plan;
- outcome definitions;
- exposure definitions;
- predictor definitions;
- analysis plan;
- data-governance status;
- ethics/regulatory status;
- timeline;
- funding requirements;
- target registry requirements;
- current data-access status;
- and whether outcome data have already been inspected.

Do not invent missing scientific decisions.

---

# 4. Registration Family

Classify the intended record as one or more of:

- `STUDY_REGISTRATION`
- `CLINICAL_TRIAL_REGISTRATION`
- `PROTOCOL_REGISTRATION`
- `SYSTEMATIC_REVIEW_REGISTRATION`
- `META_ANALYSIS_REGISTRATION`
- `PREREGISTRATION`
- `ANALYSIS_PLAN_PREREGISTRATION`
- `SECONDARY_DATA_PREREGISTRATION`
- `REPLICATION_PREREGISTRATION`
- `REGISTERED_REPORT`
- `OBSERVATIONAL_STUDY_REGISTRATION`
- `QUALITATIVE_PROTOCOL_REGISTRATION`
- `MIXED_METHOD_REGISTRATION`
- `AMENDMENT_RECORD`
- `DEVIATION_RECORD`
- `FINAL_TRANSPARENCY_RECORD`

These are related but not identical.

---

# 5. Registration vs Preregistration

`registration` may primarily identify a study or protocol in a public or institutional registry.

`preregistration` emphasizes prospective specification of decisions before relevant outcomes or analyses are observed.

A study may be:

- registered but not meaningfully preregistered;
- preregistered without being a regulated clinical trial;
- prospectively registered with minimal analysis detail;
- or retrospectively registered.

Report the actual status.

---

# 6. Timing Status

Use:

- `PROSPECTIVE_BEFORE_DATA_COLLECTION`
- `PROSPECTIVE_BEFORE_OUTCOME_ACCESS`
- `PROSPECTIVE_BEFORE_ANALYSIS`
- `AFTER_PARTIAL_DATA_COLLECTION`
- `AFTER_FULL_DATA_COLLECTION`
- `AFTER_OUTCOME_INSPECTION`
- `AFTER_PRIMARY_ANALYSIS`
- `RETROSPECTIVE_REGISTRATION`
- `TIMING_UNKNOWN`

Timing must be explicit.

---

# 7. Evidence Access Status

Record whether the researcher has seen:

- no study data;
- only recruitment counts;
- only blinded data;
- only baseline data;
- partial outcomes;
- full outcomes;
- preliminary analyses;
- final analyses.

Use:

```yaml
evidence_access:
  data_collected:
  outcome_access:
  group_labels_unblinded:
  preliminary_analysis_seen:
  date:
  notes:
```

---

# 8. Confirmatory Status

Use:

- `CONFIRMATORY`
- `EXPLORATORY`
- `MIXED_CONFIRMATORY_EXPLORATORY`
- `REPLICATION`
- `VALIDATION`
- `DESCRIPTIVE`
- `PREDICTIVE`
- `METHOD_DEVELOPMENT`
- `QUALITATIVE`
- `MIXED_METHOD`
- `EVIDENCE_SYNTHESIS`

Do not force confirmatory language where it does not fit.

---

# 9. Research Question Lock

A preregistration should state the research question before detailed analytical choices whenever feasible.

Record:

```yaml
research_question:
  rq_id:
  wording:
  knowledge_function:
  confirmatory_status:
  version:
```

Do not allow a method or software choice to redefine the question silently.

---

# 10. Objective Lock

Distinguish:

- primary objective;
- secondary objective;
- exploratory objective.

Avoid multiple “primary” objectives without justification.

---

# 11. Hypothesis Record

Where hypotheses are appropriate, record:

```yaml
hypothesis:
  hypothesis_id:
  statement:
  direction:
  variables:
  comparison:
  mechanism_or_theory:
  confirmatory_status:
  planned_test:
  version:
```

Do not generate hypotheses after seeing results and label them preregistered.

---

# 12. No-Hypothesis Path

Preregistration can still be useful for:

- descriptive research;
- qualitative research;
- validation;
- replication;
- prediction;
- systematic review;
- methodological research.

Do not force hypotheses.

---

# 13. Study Design Record

Record:

```yaml
study_design:
  design_family:
  prospective_or_retrospective:
  experimental_or_observational:
  cross_sectional_or_longitudinal:
  groups:
  allocation:
  blinding:
  followup:
  unit_of_analysis:
  version:
```

---

# 14. Population Record

Document:

- target population;
- source population;
- inclusion criteria;
- exclusion criteria;
- setting;
- recruitment source;
- recruitment period;
- geography;
- relevant subgroups.

---

# 15. Eligibility Lock

Eligibility criteria should be specified before outcome-dependent selection where feasible.

If changed later, log amendment and effect.

---

# 16. Sampling Record

Record:

```yaml
sampling:
  target_population:
  sampling_frame:
  sampling_method:
  recruitment_method:
  planned_sample_size:
  sample_size_basis:
  stopping_rule:
  oversampling:
  stratification:
  clustering:
  attrition_assumption:
```

---

# 17. Sample Size Status

Use:

- `A_PRIORI_POWER_BASED`
- `PRECISION_BASED`
- `FEASIBILITY_BASED`
- `CENSUS`
- `FIXED_AVAILABLE_SAMPLE`
- `SIMULATION_BASED`
- `QUALITATIVE_INFORMATION_POWER`
- `SEQUENTIAL`
- `OTHER`
- `UNRESOLVED`

Do not pretend every sample size comes from power analysis.

---

# 18. Stopping Rule

Where applicable define:

- fixed N;
- fixed recruitment period;
- event count;
- saturation/information threshold;
- sequential boundary;
- resource limit;
- all eligible cases.

Do not stop because significance is reached unless that rule was validly planned.

---

# 19. Outcome Hierarchy

Classify:

- primary outcome;
- secondary outcome;
- exploratory outcome;
- safety outcome;
- process outcome;
- surrogate outcome.

---

# 20. Outcome Definition

For each major outcome record:

```yaml
outcome:
  outcome_id:
  name:
  role:
  operational_definition:
  measurement_tool:
  unit:
  timepoint:
  aggregation:
  threshold:
  source:
  missing_rule:
  version:
```

---

# 21. Outcome Timing

Specify outcome timing precisely.

Avoid:

```text
after treatment
at follow-up
later
```

Prefer explicit time windows where scientifically appropriate.

---

# 22. Outcome Switching Guard

If primary or secondary outcome changes after registration, preserve:

- original outcome;
- new outcome;
- date;
- reason;
- evidence access at time of change;
- approval/amendment status;
- reporting impact.

Do not overwrite history.

---

# 23. Predictor / Exposure Record

For each important predictor or exposure record:

- definition;
- unit;
- timing;
- coding;
- transformation;
- role;
- source.

---

# 24. Covariate Record

Distinguish:

- prespecified confounder;
- precision covariate;
- stratification variable;
- exploratory covariate;
- data-driven variable.

Do not disguise post-hoc adjustment as prespecified.

---

# 25. Mediator and Moderator Record

Where applicable define:

- variable;
- theoretical rationale;
- temporal relationship;
- planned model;
- interpretation.

Avoid opportunistic mediator/moderator additions after results.

---

# 26. Measurement Plan

Record:

- instrument;
- version;
- administration;
- scoring;
- reliability requirements;
- validity requirements;
- translation/adaptation;
- calibration;
- laboratory procedure;
- quality-control plan.

---

# 27. Derived Variable Plan

Predefine, where possible:

- formula;
- source variables;
- units;
- threshold;
- missingness behavior;
- transformation.

---

# 28. Data Exclusion Plan

Define data-level exclusions separately from participant eligibility.

Examples:

- corrupted sample;
- invalid assay;
- failed quality control;
- impossible timestamp;
- incomplete primary outcome.

Do not use vague language such as:

> “Outliers will be removed if necessary.”

---

# 29. Outlier Plan

If outlier handling is planned, specify:

- detection method;
- scientific verification;
- decision rule;
- sensitivity analysis.

Do not equate statistical unusualness with invalidity.

---

# 30. Missing Data Plan

Record:

- expected missingness;
- coding;
- primary handling;
- complete-case rule if justified;
- imputation plan;
- sensitivity analysis;
- missingness diagnostics.

---

# 31. Data Transformation Plan

Specify planned transformations such as:

- log transformation;
- standardization;
- centering;
- normalization;
- categorization;
- score construction.

Do not leave transformations entirely outcome-driven.

---

# 32. Analysis Target

Before selecting software, define what is to be estimated, compared, modeled, interpreted, or synthesized.

---

# 33. Primary Analysis

Record:

```yaml
primary_analysis:
  analysis_id:
  research_question:
  outcome:
  predictor_or_exposure:
  estimand_or_target:
  model_family:
  adjustment:
  interaction:
  clustering:
  repeated_measures:
  missing_data:
  uncertainty:
  effect_measure:
  decision_rule:
  software_optional:
```

---

# 34. Secondary Analysis

Secondary analyses should be labeled explicitly.

---

# 35. Exploratory Analysis

Exploratory analyses are legitimate.

They should be labeled:

`EXPLORATORY`

not hidden.

---

# 36. Analysis Flexibility Inventory

List meaningful researcher degrees of freedom.

Examples:

- alternative outcome definitions;
- alternative covariate sets;
- transformation choices;
- exclusion thresholds;
- interaction choices;
- subgroup choices;
- multiple timepoints;
- alternative estimators;
- missing-data approaches.

The goal is not to eliminate all flexibility.

The goal is to disclose it.

---

# 37. Decision Rules

Where inferential thresholds matter, define:

- alpha;
- confidence level;
- multiplicity adjustment;
- equivalence margin;
- noninferiority margin;
- clinical threshold;
- predictive threshold.

Do not overemphasize p-values.

---

# 38. Statistical Method Record

For quantitative studies preserve enough detail to distinguish the planned model.

---

# 39. Qualitative Preregistration

Qualitative research may preregister:

- sampling logic;
- recruitment;
- data source;
- interview guide;
- analytic orientation;
- coding approach;
- reflexivity plan;
- saturation/information-power logic;
- negative-case strategy.

Do not rigidly predefine emergent interpretations if doing so undermines the qualitative design.

---

# 40. Mixed-Method Preregistration

Record:

- design type;
- strand priority;
- timing;
- integration points;
- connecting/building/merging logic;
- joint displays;
- meta-inference plan.

---

# 41. Systematic Review Registration

Record, where applicable:

- review question;
- eligibility;
- information sources;
- search approach;
- screening;
- extraction;
- risk-of-bias assessment;
- synthesis plan;
- subgroup plan;
- meta-analysis criteria;
- certainty assessment.

---

# 42. Meta-Analysis Registration

Predefine:

- effect measure;
- dependency handling;
- fixed/random-effects rationale;
- heterogeneity estimator;
- subgroup;
- meta-regression;
- publication-bias diagnostics;
- sensitivity analyses.

---

# 43. Bibliometric Study Registration

May specify:

- database;
- search query;
- date;
- document types;
- deduplication;
- inclusion rules;
- network construction;
- normalization;
- clustering;
- interpretation plan.

---

# 44. Replication Preregistration

Record whether replication is:

- direct;
- close;
- conceptual;
- registered replication report.

Specify which elements are intentionally held constant and which differ.

---

# 45. Validation Preregistration

For external validation specify:

- locked model;
- predictors;
- preprocessing;
- validation population;
- primary performance metrics;
- calibration;
- discrimination;
- threshold metrics;
- subgroup checks.

---

# 46. Prediction Model Preregistration

Where model development is confirmatory enough to benefit, specify:

- outcome;
- candidate predictors;
- feature engineering;
- splitting/resampling;
- tuning;
- model selection;
- internal validation;
- performance metrics.

---

# 47. SEM Preregistration

Predefine:

- measurement model;
- structural model;
- estimator;
- latent-variable specification;
- correlated residual rules;
- fit indices;
- modification policy;
- missing-data handling.

---

# 48. PLS-SEM Preregistration

Predefine, where relevant:

- reflective/formative specification;
- indicators;
- path model;
- mediation;
- moderation;
- algorithm settings;
- bootstrapping;
- reliability/validity criteria;
- structural assessment;
- predictive assessment.

Do not modify model only to improve significance or fit without disclosure.

---

# 49. Experimental Study Preregistration

Specify:

- intervention;
- control;
- randomization;
- blinding;
- replicate structure;
- batch;
- outcome;
- exclusions;
- stopping;
- primary analysis.

---

# 50. Laboratory Study Preregistration

Record:

- sample source;
- assay;
- reagent;
- instrument;
- replicate logic;
- QC;
- normalization;
- calculation;
- exclusion.

---

# 51. Pharmacokinetic Study Preregistration

Specify:

- dose;
- route;
- sampling schedule;
- PK outcomes;
- BLQ handling;
- NCA/modeling approach;
- covariates;
- primary comparisons.

---

# 52. Pharmacogenetic Study Preregistration

Specify:

- SNPs or loci;
- genetic model;
- outcome;
- covariates;
- HWE use;
- multiple-testing handling;
- genotype coding;
- sensitivity analysis.

---

# 53. Genomic Study Preregistration

Specify:

- reference build;
- variant filters;
- QC;
- ancestry handling;
- association model;
- correction for multiplicity;
- replication/validation.

---

# 54. AI / ML Study Preregistration

Specify:

- data split;
- feature engineering;
- model families;
- tuning;
- leakage controls;
- performance metrics;
- threshold selection;
- external validation.

---

# 55. Secondary Data Preregistration

Secondary-data preregistration is strongest when made before relevant outcome analysis.

Record what has already been observed.

---

# 56. Existing Dataset Transparency

Use:

```yaml
existing_data:
  dataset_exists:
  researcher_has_access:
  outcomes_seen:
  descriptive_results_seen:
  inferential_results_seen:
  prior_related_analyses:
  prior_publications:
  timing_status:
```

---

# 57. Retrospective Registration

Retrospective registration can improve discoverability but must not be described as prospective preregistration.

---

# 58. Registered Report

A registered report typically separates:

```text
STAGE 1
question
rationale
methods
analysis plan
in-principle acceptance

STAGE 2
results
deviations
interpretation
```

Do not assume every journal uses identical procedures.

---

# 59. Registry Selection

Choose registry based on:

- study type;
- jurisdiction;
- funder;
- journal;
- disciplinary norms;
- legal requirements;
- registry eligibility.

Do not choose registry based only on convenience.

---

# 60. Registry Verification

Verify current requirements from authoritative registry sources when needed.

Do not rely on memory for changing forms or policies.

---

# 61. Registration Identifier

Never fabricate an identifier.

Record:

```yaml
registration:
  registry:
  identifier:
  url:
  submission_date:
  registration_date:
  status:
  version:
  verification_status:
```

---

# 62. Registration Status

Use:

- `DRAFT`
- `SUBMITTED`
- `REGISTERED`
- `APPROVED`
- `PUBLIC`
- `EMBARGOED`
- `AMENDED`
- `CLOSED`
- `WITHDRAWN`
- `REJECTED`
- `UNKNOWN`

Do not conflate registry status with ethics approval.

---

# 63. Embargo

If embargo is used, document:

- reason;
- duration;
- public release date;
- registry rules.

---

# 64. Versioning

Every material amendment should create a version trail.

Example:

```text
v1.0 preregistered
v1.1 administrative correction
v2.0 scientific amendment
```

---

# 65. Amendment Record

```yaml
amendment:
  amendment_id:
  prior_version:
  new_version:
  date:
  component:
  original_plan:
  revised_plan:
  reason:
  evidence_access_at_change:
  ethics_implication:
  registration_updated:
  reporting_required:
```

---

# 66. Administrative vs Scientific Amendment

Administrative change:

- contact update;
- typo;
- formatting;
- nonmaterial date correction.

Scientific change:

- outcome;
- sample;
- eligibility;
- model;
- intervention;
- measurement;
- exclusion;
- subgroup.

Distinguish them.

---

# 67. Deviation Record

A deviation is what happened differently from the registered plan.

Record:

```yaml
deviation:
  deviation_id:
  registered_component:
  implemented_component:
  date_detected:
  reason:
  planned_or_unplanned:
  evidence_access:
  consequence:
  confirmatory_status_after_change:
  reporting_location:
```

---

# 68. Deviation Categories

Use:

- `METHOD_DEVIATION`
- `SAMPLING_DEVIATION`
- `OUTCOME_DEVIATION`
- `ANALYSIS_DEVIATION`
- `TIMING_DEVIATION`
- `MEASUREMENT_DEVIATION`
- `DATA_QUALITY_DEVIATION`
- `ETHICS_DRIVEN_DEVIATION`
- `FEASIBILITY_DEVIATION`
- `REGULATORY_DEVIATION`
- `REVIEWER_REQUESTED_DEVIATION`

---

# 69. Deviation Is Not Automatically Misconduct

A scientifically justified deviation may be appropriate.

The issue is undisclosed deviation.

---

# 70. HARKing Guard

HARKing means presenting a hypothesis as if specified before results when it was generated after results.

If a hypothesis emerged later, label:

`POST_HOC_HYPOTHESIS`

or:

`EXPLORATORY_HYPOTHESIS`

as appropriate.

---

# 71. Outcome Switching Guard

Do not silently promote a secondary or exploratory outcome to primary after seeing results.

If changed, disclose.

---

# 72. Analysis Switching Guard

Do not silently replace a prespecified model with a favorable alternative.

---

# 73. Covariate Switching Guard

Do not present data-driven covariate choices as prespecified.

---

# 74. Subgroup Switching Guard

Unexpected subgroup findings can be valuable.

Label them exploratory unless prespecified.

---

# 75. Exclusion Switching Guard

Do not redefine exclusions after seeing which records affect significance without transparent rationale.

---

# 76. Multiplicity Transparency

If many analyses were possible or performed, preserve the multiplicity context.

---

# 77. Selective Reporting Guard

The final manuscript should not report only favorable registered outcomes.

---

# 78. Null Result Protection

Registered null findings remain scientifically reportable.

Do not redefine success as significance.

---

# 79. Negative Findings

Negative or contradictory results should not be hidden because they conflict with preregistered expectations.

---

# 80. Analysis Failure

If a preregistered analysis cannot be performed:

- state why;
- preserve the original plan;
- document alternative;
- label alternative status.

---

# 81. Data Quality-Driven Amendment

If `data-quality-auditor` identifies a scientifically necessary change, document it.

Do not erase the preregistered plan.

---

# 82. Ethics-Driven Amendment

If `ethics-regulatory-gate` requires changes, record:

- original plan;
- ethics requirement;
- revised plan;
- timing;
- approval status.

---

# 83. Reviewer-Driven Amendment

A reviewer request can create:

- new exploratory analysis;
- robustness analysis;
- additional subgroup;
- new experiment.

Preserve its post-submission status.

---

# 84. Preregistration Freeze

Before relevant data access, create a freeze record:

```yaml
preregistration_freeze:
  version:
  date:
  research_question:
  hypotheses:
  design:
  outcomes:
  sampling:
  analysis_plan:
  evidence_access_status:
  repository_or_registry:
```

---

# 85. Data Lock Relationship

Preregistration timing and dataset lock are related but distinct.

Record both.

---

# 86. Analysis Plan Freeze

A separate analysis-plan freeze may occur after data collection but before unblinding or outcome analysis.

Label timing accurately.

---

# 87. Blinded Analysis Planning

Where feasible, analysis plans may be finalized using blinded data.

Document what was visible.

---

# 88. Simulation-Based Planning

Simulation may inform analysis choices without revealing observed outcomes.

Document simulation assumptions.

---

# 89. Pilot Data

Pilot data may be used for planning.

Distinguish:

- independent pilot;
- internal pilot;
- main-study data.

---

# 90. Feasibility Study

A feasibility study may be preregistered around feasibility outcomes rather than efficacy.

---

# 91. Exploratory Study Transparency

For fully exploratory studies, create an exploration plan if helpful but do not overstate prespecification.

---

# 92. Confirmatory-Exploratory Separation

Use:

```text
CONFIRMATORY
- prespecified questions
- prespecified primary outcomes
- prespecified primary analysis

EXPLORATORY
- unexpected patterns
- new subgroups
- alternate models
- mechanism-generating analyses
```

---

# 93. Planned vs Implemented Matrix

| Component | Registered Plan | Implemented | Changed? | Reason | Final Status |
|---|---|---|---|---|---|

---

# 94. Planned vs Reported Matrix

| Component | Registered | Analyzed | Reported | Omitted? | Explanation |
|---|---|---|---|---|---|

---

# 95. Registration Completeness Matrix

| Domain | Complete | Partial | Missing | Action |
|---|---|---|---|---|
| Research question | | | | |
| Objectives | | | | |
| Hypotheses | | | | |
| Design | | | | |
| Population | | | | |
| Sampling | | | | |
| Outcomes | | | | |
| Predictors/exposures | | | | |
| Covariates | | | | |
| Exclusions | | | | |
| Missing data | | | | |
| Primary analysis | | | | |
| Secondary analyses | | | | |
| Multiplicity | | | | |
| Deviations | | | | |

---

# 96. Registration Readiness

Use:

- `READY_TO_REGISTER`
- `READY_WITH_MINOR_GAPS`
- `REQUIRES_SCIENTIFIC_REVISION`
- `REQUIRES_ETHICS_REVIEW`
- `REQUIRES_ANALYSIS_PLAN`
- `NOT_READY`
- `NOT_APPLICABLE`

---

# 97. Preregistration Strength

Use:

- `STRONG_PROSPECTIVE`
- `MODERATE_PROSPECTIVE`
- `LIMITED_PROSPECTIVE`
- `RETROSPECTIVE_TRANSPARENCY_ONLY`
- `NOT_PREREGISTERED`

Do not overstate strength.

---

# 98. Timing Strength

Strongest timing generally occurs before exposure to outcome-relevant evidence.

But design-specific exceptions exist.

---

# 99. Registration Quality

Quality depends on specificity and scientific coherence, not word count.

---

# 100. Vagueness Guard

Avoid vague commitments such as:

> “Appropriate statistical tests will be used.”

> “Outliers will be removed.”

> “Covariates may be included.”

> “Missing data will be handled appropriately.”

These do not meaningfully constrain analytic flexibility.

---

# 101. Over-Specification Guard

Do not preregister scientifically irrelevant detail merely to appear rigorous.

---

# 102. Impossible Commitment Guard

Do not commit to procedures that depend on unknown data structure without conditional rules.

---

# 103. Conditional Analysis Rules

Use explicit conditional rules when appropriate.

Example:

```text
If convergence fails under the primary model,
use the prespecified alternative estimator.
```

---

# 104. Decision Tree Preregistration

Complex studies may preregister a decision tree.

---

# 105. Alternative Model Plan

Predefine acceptable alternatives where needed.

---

# 106. Robustness Plan

Specify robustness analyses separately from primary analysis.

---

# 107. Sensitivity Plan

Examples:

- alternate missing-data assumptions;
- alternate outlier inclusion;
- alternate exposure definition;
- alternate time window;
- alternate estimator.

---

# 108. Multiplicity Plan

Where needed specify:

- family of hypotheses;
- correction method;
- hierarchy;
- gatekeeping;
- exploratory exception.

---

# 109. Interim Analysis

If interim analysis is planned, specify:

- timing;
- stopping boundary;
- who sees results;
- adjustment;
- decision authority.

---

# 110. Adaptive Design

Adaptive decisions require explicit prespecification where confirmatory inference depends on them.

---

# 111. Sequential Analysis

Record stopping boundaries and error control.

---

# 112. Bayesian Preregistration

Specify:

- model;
- prior;
- likelihood;
- decision threshold;
- sensitivity priors;
- stopping rule.

---

# 113. Equivalence / Noninferiority

Specify margins prospectively and justify them.

---

# 114. Causal Inference Preregistration

Specify:

- treatment/exposure;
- outcome;
- estimand;
- confounders;
- causal assumptions;
- adjustment method;
- positivity;
- missingness;
- sensitivity.

---

# 115. Mediation Preregistration

Specify:

- exposure;
- mediator;
- outcome;
- temporal order;
- estimand;
- assumptions;
- model.

---

# 116. Moderation Preregistration

Specify moderator and interaction before result inspection where confirmatory.

---

# 117. Longitudinal Preregistration

Specify:

- timepoints;
- trajectory model;
- baseline;
- time coding;
- attrition;
- repeated-measure covariance.

---

# 118. Survival Analysis Preregistration

Specify:

- time origin;
- event;
- censoring;
- competing risk;
- model;
- proportional-hazards handling.

---

# 119. Diagnostic Study Preregistration

Specify:

- index test;
- reference standard;
- threshold;
- analysis population;
- sensitivity/specificity;
- indeterminate results.

---

# 120. Reliability Study Preregistration

Specify:

- construct;
- instrument;
- reliability metric;
- repeated measurement;
- raters;
- interpretation.

---

# 121. Measurement Validation Preregistration

Specify:

- factor structure;
- item treatment;
- estimator;
- fit criteria;
- invariance tests;
- modification rules.

---

# 122. Qualitative Flexibility Guard

Do not convert interpretive qualitative research into rigid pseudo-confirmatory analysis merely to preregister it.

Preregister procedural commitments and epistemic stance proportionally.

---

# 123. Mixed-Method Flexibility Guard

Integration decisions should be explicit without erasing legitimate emergent integration.

---

# 124. Evidence Synthesis Update

For living reviews or updates, preregister:

- update date;
- search changes;
- eligibility changes;
- synthesis changes.

---

# 125. Registration Citation

In manuscripts, cite or link the actual registry record where appropriate.

Do not cite a draft as if publicly registered.

---

# 126. Registration Date Reporting

Report registration date accurately.

---

# 127. Retrospective Registration Disclosure

If registration was retrospective, say so.

---

# 128. Amendment Disclosure

Material amendments should be disclosed in the manuscript or supplement where relevant.

---

# 129. Deviation Table

A manuscript-ready deviation table may include:

| Registered Plan | Final Implementation | Reason | Timing | Impact |
|---|---|---|---|---|

---

# 130. Manuscript Language

Prefer:

> “The primary analysis was preregistered before outcome data were accessed.”

when true.

Avoid:

> “The study was preregistered”

if only a minimal registry entry existed after analysis.

---

# 131. Transparency Language

Useful labels:

- prespecified;
- preregistered;
- amended;
- exploratory;
- post-hoc;
- sensitivity;
- reviewer-requested;
- secondary.

---

# 132. Registered Result Interpretation

Registration status does not make a result correct.

It changes the evidential context.

---

# 133. Preregistered Null Results

Do not downgrade them because they are non-significant.

---

# 134. Exploratory Positive Results

Do not upgrade them to confirmatory merely because they are significant.

---

# 135. Replication Status

A replication may test preregistered original findings with stronger confirmatory value.

---

# 136. Registration and Reproducibility

Preregistration supports transparency.

It does not prove reproducibility.

Coordinate with `reproducibility-auditor`.

---

# 137. Registration and Ethics

Preregistration does not grant permission to recruit, intervene, access data, or collect specimens.

Coordinate with `ethics-regulatory-gate`.

---

# 138. Registration and Data Governance

Registration should specify enough data logic to support `research-data-governance`.

---

# 139. Registration and Data Quality

Quality decisions should be distinguished as:

- prespecified;
- protocol-driven;
- discovered during audit;
- post-hoc.

---

# 140. Registration and Analysis Planner

`analysis-planner` provides the analytical architecture.

This skill captures and freezes that architecture when appropriate.

---

# 141. Registration and Statistical Method Selector

The chosen statistical method should correspond to the registered analysis target.

---

# 142. Registration and Qualitative Analysis

Preserve methodological openness without pretending interpretive outcomes were prespecified.

---

# 143. Registration and Mixed-Method Analysis

Record integration strategy and distinguish prespecified vs emergent integration.

---

# 144. Registration and Meta-Analysis

Use registration to reduce post-hoc eligibility and synthesis flexibility.

---

# 145. Registration and Result Interpreter

`result-interpreter` should know whether findings are:

- prespecified;
- amended;
- exploratory;
- post-hoc.

---

# 146. Registration and Scientific Discussion

Discussion should not present exploratory findings as preregistered confirmatory evidence.

---

# 147. Registration and Implication Builder

Implication strength should consider prespecification status.

---

# 148. Registration and Manuscript Architect

`manuscript-architect` should plan transparent reporting of:

- registration;
- protocol;
- deviations;
- exploratory analyses.

---

# 149. Registration and Manuscript Writer

`manuscript-writer` must not invent:

- registry name;
- identifier;
- registration date;
- prospective timing;
- amendment status.

---

# 150. Registration and Manuscript Auditor

`manuscript-auditor` should compare manuscript claims with the actual record.

---

# 151. Registration and Reviewer Simulator

Reviewer simulation may challenge:

- retrospective registration;
- outcome switching;
- unexplained deviations;
- analytic flexibility.

---

# 152. Registration and Reviewer Response

Reviewer-requested changes should be labeled according to their timing and evidential status.

---

# 153. Registration and Research Roadmap

A long-term program may preregister key validation, replication, or confirmatory stages.

---

# 154. Registration and Research Resume

When resuming prior work, identify whether previous registered commitments remain active or have been superseded.

---

# 155. Registration and Prior Research Auditor

A previous paper may be compared with its registration to detect undisclosed divergence.

---

# 156. Research Router Relationship

`research-router` should route here when the user asks:

- “Should I preregister this study?”
- “What should I register before collecting data?”
- “Can I preregister a secondary-data analysis?”
- “How do I document a protocol change?”
- “This outcome changed—what do I do?”
- “Can I add an exploratory analysis?”
- “How do I separate confirmatory and exploratory findings?”
- “How do I report deviations from my protocol?”
- “Does registration replace ethics approval?”
- “Can reviewer-requested analysis still be called preregistered?”

---

# 157. Research Intake Relationship

`research-intake` should capture:

- whether data collection started;
- whether outcomes have been seen;
- whether analysis has started;
- whether registration exists;
- registry;
- identifier;
- version;
- ethics status.

---

# 158. Registration Decision Logic

```text
Is prospective specification scientifically useful or required?
        │
   ┌────┴────┐
   │         │
  No        Yes
   │         │
TRANSPARENCY  Have relevant outcomes already been inspected?
ONLY            │
           ┌────┴────┐
           │         │
          No        Yes
           │         │
PREREGISTER    Is meaningful prospective commitment still possible?
                  │
             ┌────┴────┐
             │         │
            No        Yes
             │         │
RETROSPECTIVE   PREREGISTER REMAINING
TRANSPARENCY    DECISIONS + DISCLOSE ACCESS
```

---

# 159. Registration Completeness Status

Use:

- `COMPLETE`
- `SUBSTANTIALLY_COMPLETE`
- `PARTIAL`
- `INSUFFICIENT`
- `NOT_APPLICABLE`

---

# 160. Registration Risk Flags

Possible flags:

- `OUTCOME_SWITCHING_RISK`
- `HARKING_RISK`
- `ANALYSIS_FLEXIBILITY_RISK`
- `EXCLUSION_FLEXIBILITY_RISK`
- `SUBGROUP_FLEXIBILITY_RISK`
- `RETROSPECTIVE_REGISTRATION`
- `TIMING_UNCLEAR`
- `REGISTRY_UNVERIFIED`
- `DEVIATION_UNDOCUMENTED`
- `AMENDMENT_UNRECORDED`

---

# 161. Critical Registration Failures

Examples:

- falsely claiming prospective registration;
- fabricated registration number;
- hiding material outcome changes;
- hiding major analysis deviations;
- presenting post-hoc hypothesis as preregistered.

---

# 162. Major Registration Issues

Examples:

- primary outcome underspecified;
- analysis plan too vague;
- timing unclear;
- major amendment not recorded;
- exploratory analysis mislabeled.

---

# 163. Moderate Issues

Examples:

- incomplete secondary outcome detail;
- missing software version where not essential;
- unclear sensitivity-analysis status.

---

# 164. Minor Issues

Examples:

- formatting inconsistencies;
- nonmaterial administrative omissions.

---

# 165. Registration Repair

Possible actions:

- clarify timing;
- add missing specification before outcome access;
- amend registry;
- create deviation log;
- relabel exploratory findings;
- reconstruct planned-vs-implemented table;
- verify registry identifier;
- disclose retrospective timing.

---

# 166. No Retrospective Preregistration Fiction

Never backdate a plan conceptually.

If written after seeing results, it is not preregistration of those results.

---

# 167. No Registry Fabrication

Never invent:

- registry;
- identifier;
- URL;
- date;
- status.

---

# 168. No Approval Substitution

Do not use registration as a substitute for:

- ethics approval;
- regulatory approval;
- data-use authorization.

---

# 169. No Quality Substitution

A preregistered bad method remains a bad method.

---

# 170. No Rigidity Worship

Amendments are allowed when scientifically justified.

Transparency matters.

---

# 171. No P-Value Ritual

Preregistration is not primarily about forcing every study into significance testing.

---

# 172. No Exploratory Stigma

Exploration is scientifically legitimate.

Mislabeling is the problem.

---

# 173. No Software Lock-In

Do not preregister a software package as if it were the scientific method unless implementation depends on it.

---

# 174. No Journal-Driven Distortion

Journal expectations may shape reporting but should not redefine what was actually preregistered.

---

# 175. No APC Influence

Publication-cost preferences must not change the scientific registration record.

---

# 176. No Silent Amendment

Material changes must remain traceable.

---

# 177. No Outcome-Dependent Registration Editing

Do not edit registration to align with favorable results without preserving amendment history.

---

# 178. No Deviation Erasure

Deviation records should remain visible even if the final method is defensible.

---

# 179. Registration Passport

```yaml
registration_preregistration_passport:
  status:
  registration_family:
  registry:
  identifier:
  version:
  timing_status:
  evidence_access_status:
  research_question_status:
  objective_status:
  hypothesis_status:
  design_status:
  population_status:
  sampling_status:
  outcome_status:
  analysis_plan_status:
  multiplicity_status:
  amendment_status:
  deviation_status:
  confirmatory_exploratory_status:
  registry_verification:
  ethics_linkage:
  unresolved_issues:
  next_action:
```

---

# 180. Registration Record Template

```yaml
registration_record:
  project:
  study_title:
  registry:
  identifier:
  version:
  registration_date:
  timing_status:
  evidence_access:
  research_questions:
  objectives:
  hypotheses:
  design:
  population:
  sampling:
  outcomes:
  predictors:
  covariates:
  exclusions:
  missing_data:
  primary_analysis:
  secondary_analyses:
  exploratory_analyses:
  multiplicity:
  amendments:
  deviations:
  ethics_status:
  data_governance_status:
```

---

# 181. Analysis Plan Template

```yaml
analysis_plan:
  analysis_id:
  research_question:
  confirmatory_status:
  dataset:
  unit_of_analysis:
  outcome:
  predictors:
  covariates:
  estimator_or_method:
  effect_measure:
  uncertainty:
  missing_data:
  exclusions:
  interactions:
  subgroup:
  multiplicity:
  sensitivity:
  decision_rule:
  alternative_if_failure:
```

---

# 182. Deviation Log Template

| ID | Registered Plan | Implemented | Reason | Timing | Outcome Seen? | Final Label |
|---|---|---|---|---|---|---|

---

# 183. Amendment Log Template

| Version | Date | Component | Original | Revision | Reason | Registered? |
|---|---|---|---|---|---|---|

---

# 184. Final Transparency Summary

```yaml
final_transparency:
  preregistered_primary:
  preregistered_secondary:
  amended:
  exploratory:
  reviewer_requested:
  post_hoc:
  not_performed:
  omitted_with_reason:
  deviations_reported:
```

---

# 185. User-Facing Example

```text
Registration status: READY WITH MINOR GAPS

What is already clear
- Research question and primary objective are stable.
- Primary outcome is defined.
- Planned sample size and eligibility rules are documented.
- Primary regression model is specified.

What still needs clarification before preregistration
- How missing primary-outcome data will be handled.
- Whether age and sex are prespecified adjustment covariates or exploratory.
- The rule for one planned sensitivity analysis.

Timing
- Outcome data have not yet been inspected.

Next action
Clarify those three decisions, freeze version 1.0, then submit the preregistration.
```

---

# 186. User-Friendly Behavior

Instead of:

> “Your study is not preregistered.”

Prefer:

> “The study does not currently have a prospective preregistration record. Because the outcome data have not yet been inspected, there is still an opportunity to preregister the remaining confirmatory decisions.”

Instead of:

> “You violated preregistration.”

Prefer:

> “The final analysis differs from the registered plan in two places. Those changes can be reported transparently as amendments or deviations rather than being presented as if they were prespecified.”

---

# 187. Stop Conditions

Stop and request clarification when:

- registration timing is unknown;
- outcome access is unclear;
- primary outcome is unresolved;
- sample stopping rule is unresolved;
- primary analysis cannot be identified;
- ethics approval is being confused with registration;
- the user asks to fabricate a registry number;
- the user wants to label a post-hoc plan as prospective;
- major deviations are known but undocumented;
- registry requirements depend on current rules that have not been verified.

Use:

- `REGISTRATION_REQUIRES_REVISION`
- `TIMING_STATUS_UNRESOLVED`
- `OUTCOME_STATUS_UNRESOLVED`
- `ANALYSIS_PLAN_UNRESOLVED`
- `REGISTRY_VERIFICATION_REQUIRED`
- `RETURN_TO_ETHICS_REGULATORY_GATE`
- `RETURN_TO_ANALYSIS_PLANNER`
- `RETROSPECTIVE_TRANSPARENCY_ONLY`

---

# 188. Completion Gate

The builder succeeds operationally when:

- registration family is identified;
- timing is explicit;
- evidence access is explicit;
- research question is stable;
- outcomes are specified;
- sampling is specified;
- primary analysis is specified where appropriate;
- confirmatory and exploratory components are separated;
- amendments and deviations are versioned;
- registry status is verified where relevant;
- final reporting can compare planned vs implemented.

---

# 189. Relationship with Research Data Governance

If preregistration specifies data handling, `research-data-governance` should preserve its implementation.

---

# 190. Relationship with Data Quality Auditor

If quality findings require changes, preserve them as documented deviations or amendments.

---

# 191. Relationship with Reproducibility Auditor

`reproducibility-auditor` should compare:

```text
REGISTERED PLAN
      ↓
IMPLEMENTED ANALYSIS
      ↓
REPORTED RESULT
```

---

# 192. Relationship with Ethics Regulatory Gate

`ethics-regulatory-gate` determines whether activity is permitted.

This skill determines whether planning and deviations are transparently recorded.

---

# 193. Relationship with Research Router

`research-router` should route here for prospective planning, registration questions, deviation tracking, or planned-vs-conducted comparisons.

---

# 194. Relationship with Research Resume

When continuing an old project, determine:

- whether registration exists;
- whether it remains active;
- whether the current study is a new registration;
- whether old commitments still apply.

---

# 195. Relationship with Research Roadmap

Future confirmatory, replication, validation, or clinical stages may include registration as a scientific milestone.

---

# 196. Relationship with Manuscript Workflow

`manuscript-architect`, `manuscript-writer`, and `manuscript-auditor` should receive:

- registry;
- identifier;
- timing;
- amendments;
- deviations;
- exploratory status.

---

# 197. Relationship with Reviewer Response

Reviewer-driven analyses should be labeled accurately rather than retroactively preregistered.

---

# 198. Relationship with Journal Matcher

Journal registration requirements may influence submission readiness but must not alter registration history.

---

# 199. Registration Output Package

Produce, as needed:

1. Registration Type
2. Timing Status
3. Evidence Access Statement
4. Registration Readiness
5. Registration Record
6. Primary Analysis Plan
7. Outcome Hierarchy
8. Sampling and Stopping Plan
9. Missing-Data Plan
10. Sensitivity Plan
11. Amendment Log
12. Deviation Log
13. Planned-vs-Implemented Matrix
14. Planned-vs-Reported Matrix
15. Final Transparency Statement
16. Research Passport Update

---

# 200. Final Registration Rule

Never rewrite history.

Never call a post-hoc decision preregistered.

Never let registration replace scientific judgment.

Never hide justified amendments.

Never penalize honest exploration.

The purpose is prospective clarity and retrospective transparency.

---

# Success Criterion

`registration-preregistration-builder` succeeds when the study's registration or preregistration record transparently distinguishes prospective commitments, later amendments, deviations, exploratory analyses, post-hoc decisions, and final implementation; when the timing of registration and the researcher's access to outcome-relevant evidence are explicit; when research questions, objectives, hypotheses where appropriate, design, population, sampling, stopping rules, outcomes, predictors, exclusions, missing-data handling, primary analysis, secondary analyses, multiplicity, robustness, and sensitivity procedures are specified to the degree scientifically useful without overconstraining legitimate exploratory or qualitative inquiry; when registration is clearly separated from ethics approval, regulatory authorization, scientific validity, data quality, and reproducibility; when retrospective registration is never misrepresented as prospective preregistration; when registry identifiers, dates, and statuses are verified rather than fabricated; when outcome switching, HARKing, undisclosed analytic flexibility, subgroup switching, covariate switching, and silent exclusion changes are prevented or transparently labeled; when scientifically justified protocol amendments remain possible but versioned; when reviewer-driven analyses retain their true timing and evidential status; and when the final manuscript and research record can show exactly what was planned, what changed, why it changed, what remained confirmatory, what became exploratory, and how those distinctions should affect interpretation of the evidence.
