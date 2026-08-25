---
name: analysis-planner
description: Build a complete analysis architecture from an approved research question, methodology, sampling strategy, measurement system, protocol, and actual data-generating process before a specific statistical, qualitative, mixed-method, or meta-analytic technique is selected. Use when a study is design-ready and the researcher needs to define analysis targets, estimands, data structure, variable roles, descriptive requirements, assumption checks, missing-data strategy, multiplicity, sensitivity analyses, effect and uncertainty reporting, method-family routing, and software requirements without allowing p-values, normality tests, software menus, or familiar techniques to determine the scientific analysis.
---

# Analysis Planner

## Purpose

`analysis-planner` converts a design-ready study into a scientifically coherent analysis architecture.

Its central question is:

> What must be estimated, compared, modeled, interpreted, synthesized, or integrated from the data so that the research question is answered in a way that respects the actual study design, measurement system, sampling structure, and intended inference?

This skill operates after methodology and before specific analytical techniques are finalized.

It does not automatically choose:

- a statistical test;
- SEM;
- PLS-SEM;
- regression;
- machine learning;
- thematic analysis;
- meta-analysis;
- software.

Those decisions belong downstream when justified.

---

# Core Principle

Use:

> Design before analysis. Estimand before estimator. Question before test. Data structure before software.

The analysis should follow:

```text
Research Question
      ↓
Intended Inference
      ↓
Study Design
      ↓
Analysis Target / Estimand
      ↓
Data Structure
      ↓
Measurement Structure
      ↓
Assumptions & Design Features
      ↓
Analysis Family
      ↓
Specific Method
      ↓
Software
```

Do not reverse this sequence.

---

# Position in the Framework

Preferred architecture:

```text
DESIGN READY
    │
    ▼
analysis-planner
    │
    ├──────────────┬────────────────┬─────────────────┐
    ▼              ▼                ▼                 ▼
QUANTITATIVE   QUALITATIVE     MIXED METHOD      EVIDENCE
                                              SYNTHESIS
    │              │                │                 │
    ▼              ▼                ▼                 ▼
statistical-   qualitative-    mixed-method-      meta-analysis
method-selector  analysis        analysis         when justified
    │
    ▼
method-specific analysis
```

Not every study uses every branch.

---

# Required Upstream Context

Use established information from:

- `research-question-builder`;
- `hypothesis-builder`;
- `theoretical-framework`;
- `conceptual-framework`;
- `problem-solving-approach`;
- `methodology-architect`;
- `protocol-builder`;
- `sampling-strategy`;
- `instrument-design`.

Do not ask the researcher to repeat information already established.

Minimum useful context normally includes:

- primary RQ;
- secondary RQs;
- hypotheses when applicable;
- intended inference;
- study design;
- population;
- unit structure;
- sampling design;
- exposure / intervention;
- comparator;
- primary outcome or phenomenon;
- measurement scales;
- timing;
- clustering;
- repeated measures;
- missingness context;
- protocol deviations where relevant.

---

# Analysis Readiness Gate

Classify the project as:

- `READY_FOR_ANALYSIS_PLANNING`
- `DESIGN_NOT_READY`
- `OUTCOME_NOT_DEFINED`
- `ESTIMAND_NOT_DEFINED`
- `DATA_STRUCTURE_UNCLEAR`
- `MEASUREMENT_NOT_READY`
- `SAMPLING_STRUCTURE_UNCLEAR`
- `ANALYSIS_ALREADY_PLANNED`
- `ANALYSIS_REQUIRES_REASSESSMENT`

Do not select analytical methods when the data-generating design is not sufficiently specified.

---

# Analysis Purpose

Classify the dominant analytical purpose.

Possible purposes include:

- `DESCRIPTION`
- `ESTIMATION`
- `COMPARISON`
- `ASSOCIATION`
- `CAUSAL_EFFECT`
- `MECHANISM`
- `MEDIATION`
- `MODERATION`
- `PREDICTION`
- `DIAGNOSIS`
- `PROGNOSIS`
- `VALIDATION`
- `MEASUREMENT_MODEL`
- `LONGITUDINAL_CHANGE`
- `TIME_TO_EVENT`
- `CLUSTERED_INFERENCE`
- `REPEATED_MEASURES`
- `QUALITATIVE_INTERPRETATION`
- `THEORY_GENERATION`
- `MIXED_METHOD_INTEGRATION`
- `EVIDENCE_SYNTHESIS`
- `META_ANALYSIS`
- `OPTIMIZATION`
- `DOSE_RESPONSE`
- `FORMULATION_COMPARISON`
- `PHARMACOKINETIC_ESTIMATION`
- `PHARMACOGENETIC_ASSOCIATION`

More than one may apply.

Identify a primary analytical purpose.

---

# Analysis Target

Before selecting a method, define what the analysis must produce.

Possible targets include:

- mean;
- median;
- prevalence;
- proportion;
- incidence;
- risk;
- risk difference;
- risk ratio;
- odds ratio;
- mean difference;
- standardized difference;
- regression coefficient;
- correlation;
- treatment effect;
- mediation effect;
- interaction effect;
- trajectory;
- hazard;
- predictive probability;
- diagnostic accuracy;
- calibration;
- latent construct score;
- factor structure;
- reliability coefficient;
- qualitative theme;
- process explanation;
- integrated meta-inference;
- pooled effect;
- heterogeneity estimate.

Do not let software output determine the scientific target.

---

# Estimand

When applicable define the estimand before the estimator.

Recommended structure:

```yaml
estimand:
  population:
  treatment_or_exposure:
  comparator:
  outcome:
  summary_measure:
  time:
  intercurrent_event_strategy:
```

Not every study requires formal estimand terminology, but the target quantity should still be explicit.

---

# Estimand vs Estimator

Distinguish:

- estimand = what scientific quantity is targeted;
- estimator = how data are used to estimate it;
- estimate = numerical result.

Do not choose an estimator before the estimand is clear.

---

# Primary and Secondary Analyses

Separate:

- primary analysis;
- secondary analyses;
- exploratory analyses;
- sensitivity analyses;
- subgroup analyses.

Do not allow secondary analyses to redefine the primary objective after results are known.

---

# Confirmatory vs Exploratory

Classify:

- `CONFIRMATORY`
- `EXPLORATORY`
- `HYBRID`
- `VALIDATION`
- `REPLICATION`

Confirmatory analyses should align with preregistered or pre-specified hypotheses when applicable.

Exploratory analyses may generate hypotheses but should be labeled accordingly.

---

# Hypothesis Alignment

For each hypothesis record:

```yaml
hypothesis_analysis_map:
  hypothesis:
  outcome:
  predictor_or_exposure:
  comparator:
  estimand:
  timing:
  unit:
  analysis_family:
  confirmatory_status:
```

If the data structure cannot test a hypothesis, use:

`HYPOTHESIS_ANALYSIS_MISMATCH`

---

# Research Question Mapping

Create when useful:

| RQ | Analysis Purpose | Target | Data Structure | Analysis Family | Output |
|---|---|---|---|---|---|

This is the central bridge to downstream method selection.

---

# Variable Roles

Classify variables according to scientific role:

- primary outcome;
- secondary outcome;
- exposure;
- intervention;
- predictor;
- confounder;
- mediator;
- moderator;
- stratification variable;
- cluster variable;
- repeated-measure index;
- censoring indicator;
- time variable;
- offset;
- reference standard;
- latent construct indicator;
- process variable;
- safety outcome.

Do not treat every available variable as a covariate.

---

# Variable Type

Record actual measurement type.

Possible types:

- binary;
- nominal;
- ordinal;
- count;
- continuous;
- proportion;
- bounded score;
- date/time;
- survival time;
- recurrent event;
- repeated continuous;
- repeated categorical;
- text;
- image;
- sequence;
- high-dimensional feature vector.

Do not let spreadsheet formatting define scientific type.

---

# Measurement Scale

Distinguish:

- nominal;
- ordinal;
- interval-like;
- ratio;
- latent;
- composite;
- index;
- score.

Do not assume all Likert-derived variables are identical analytically.

---

# Likert Data Guard

Distinguish:

- single Likert-type item;
- summed or averaged multi-item scale;
- validated latent construct.

Do not route automatically to PLS-SEM merely because Likert responses are present.

---

# Data Structure

Identify the data-generating structure.

Possible structures include:

- independent observations;
- paired data;
- repeated measures;
- longitudinal;
- clustered;
- multilevel;
- nested;
- crossed;
- time series;
- survival;
- competing risks;
- recurrent events;
- matched;
- case-control;
- survey-weighted;
- compositional;
- high-dimensional;
- network;
- spatial;
- qualitative text;
- mixed data;
- evidence-level data.

---

# Independence

Ask:

> Which observations are statistically or substantively dependent?

Sources of dependence may include:

- repeated measurement;
- cluster sampling;
- matched pairs;
- family relationship;
- classroom;
- hospital;
- site;
- batch;
- rater;
- device;
- specimen;
- repeated technical measurement.

Do not analyze dependent observations as independent.

---

# Experimental Unit Guard

Analysis must respect the true experimental unit.

Do not inflate N using:

- technical replicates;
- multiple wells;
- repeated readings;
- subsamples;
- repeated time points.

Use:

`PSEUDOREPLICATION_ANALYSIS_RISK`

when necessary.

---

# Sampling Design

Preserve design information from `sampling-strategy`.

Possible features:

- strata;
- clusters;
- sampling weights;
- unequal probabilities;
- multistage selection;
- finite population;
- oversampling.

Do not discard sampling design in population-level analyses.

---

# Survey Analysis Readiness

If complex survey sampling is used, downstream method selection must account for:

- weights;
- strata;
- clusters;
- finite population if relevant.

---

# Longitudinal Structure

Record:

```yaml
longitudinal:
  unit:
  time_variable:
  number_of_waves:
  irregular_timing:
  baseline:
  follow_up:
  attrition:
  time_varying_covariates:
```

Do not collapse longitudinal data into cross-sectional analysis without justification.

---

# Repeated Measures

Repeated measurements may require methods that model within-unit correlation.

Do not analyze each time point separately by default.

---

# Clustered Data

Examples:

- students within classes;
- patients within hospitals;
- employees within organizations;
- specimens within batches.

Downstream analysis must preserve clustering.

---

# Multilevel Structure

Classify levels.

Example:

```yaml
levels:
  level_1: student
  level_2: classroom
  level_3: school
```

Do not aggregate or disaggregate constructs without scientific justification.

---

# Time-to-Event Structure

For survival outcomes define:

- origin time;
- event;
- censoring;
- follow-up;
- competing event;
- recurrent event;
- time-varying exposure.

---

# Case-Control Structure

Remember that sampling is conditioned on outcome status.

Downstream analysis should respect the design.

Do not estimate prevalence directly from ordinary case-control sampling.

---

# Diagnostic Structure

Define:

- index test;
- reference standard;
- target condition;
- threshold;
- disease prevalence context;
- verification process.

Analysis may require:

- sensitivity;
- specificity;
- predictive values;
- likelihood ratios;
- ROC-related measures;
- calibration.

---

# Prediction Structure

Define:

- target population;
- outcome;
- prediction time;
- prediction horizon;
- candidate predictors;
- data split / resampling;
- internal validation;
- external validation;
- calibration;
- discrimination.

Prediction is not explanation.

---

# Causal Structure

If causal inference is intended, preserve:

- treatment / exposure;
- comparator;
- confounders;
- mediators;
- colliders;
- time order;
- identification assumptions;
- estimand.

Do not use statistical adjustment as a substitute for causal design reasoning.

---

# DAG Awareness

When causal adjustment is central, consider causal diagrams or equivalent structured reasoning.

Do not adjust automatically for all available variables.

---

# Confounder Selection

Potential confounders should be chosen based on causal knowledge, design, and evidence.

Do not use significance screening alone.

---

# Mediator Guard

Do not adjust for a mediator in the primary total-effect model unless the estimand requires it.

---

# Collider Guard

Avoid conditioning on colliders without clear justification.

---

# Baseline Adjustment

Baseline adjustment may improve precision or control confounding depending on design.

Do not choose baseline variables based solely on observed significance.

---

# Data Integrity Before Analysis

Before analysis planning is finalized, ensure:

- unique IDs;
- valid variable labels;
- coding documented;
- units documented;
- duplicates understood;
- date logic checked;
- impossible values identified;
- protocol deviations classified.

Detailed cleaning execution belongs to the relevant analysis environment.

---

# Data Cleaning Separation

Distinguish:

- data correction;
- data transformation;
- exclusion;
- recoding;
- derived variables.

Every transformation should have scientific or methodological rationale.

---

# Raw Data Preservation

Do not overwrite raw data.

Maintain an immutable or traceable raw-data source when possible.

---

# Derived Variables

Document:

```yaml
derived_variable:
  name:
  source_variables:
  formula:
  unit:
  rationale:
  timing:
```

---

# Outliers

Do not remove outliers automatically.

First determine whether they are:

- data errors;
- legitimate extreme values;
- influential observations;
- structural subgroups.

Use sensitivity analyses when appropriate.

---

# Outlier Guard

Do not exclude a value simply because it makes p > 0.05.

---

# Distribution Assessment

Distributional assumptions should be evaluated in relation to the intended model.

Do not use a normality test as an automatic method selector.

---

# Normality Test Guard

A significant Shapiro-Wilk test does not automatically require a nonparametric method.

A non-significant normality test does not prove perfect normality.

Consider:

- sample size;
- model residuals;
- robustness;
- outcome distribution;
- graphical diagnostics;
- estimand.

---

# Assumption Architecture

Possible assumptions include:

- independence;
- linearity;
- homoscedasticity;
- normal residuals;
- proportional hazards;
- proportional odds;
- no perfect multicollinearity;
- correct functional form;
- missing at random;
- positivity;
- exchangeability;
- consistency;
- measurement invariance.

Only check assumptions relevant to the intended method family.

---

# Assumptions Before P-Values

Do not interpret inferential output before major assumptions and design compatibility are assessed.

---

# Transformations

Transform variables when scientifically and statistically justified.

Possible reasons:

- functional form;
- variance stabilization;
- interpretability;
- distributional model fit.

Do not transform merely to "make data normal."

---

# Categorization

Avoid unnecessary categorization of continuous variables.

Categorization may:

- lose information;
- reduce power;
- create arbitrary thresholds;
- distort relationships.

---

# Missing Data

Classify:

- item missingness;
- unit nonresponse;
- attrition;
- missing outcome;
- missing predictor;
- censored measurement;
- below detection;
- structurally not applicable.

Do not encode all missing values as zero.

---

# Missingness Mechanism

Consider:

- MCAR;
- MAR;
- MNAR;

as conceptual models, not labels proven by one test.

---

# Missing Data Strategy

Possible strategies include:

- complete-case;
- available-case;
- multiple imputation;
- maximum likelihood;
- inverse probability weighting;
- model-based handling;
- sensitivity analysis.

Selection belongs downstream and must match design and assumptions.

---

# Complete-Case Guard

Complete-case analysis is not automatically unbiased.

---

# Single Imputation Guard

Avoid simple mean substitution as a default inferential strategy.

---

# Multiple Imputation Readiness

If multiple imputation may be required, preserve:

- variables related to missingness;
- outcome;
- predictors;
- design variables;
- auxiliary variables.

Detailed procedure belongs downstream.

---

# Detection Limits

For laboratory measurements distinguish:

- true zero;
- below detection;
- below quantification;
- missing.

Do not substitute zero without justification.

---

# Descriptive Analysis

Every quantitative study should normally begin with scientifically meaningful description.

Possible outputs include:

- counts;
- percentages;
- means;
- standard deviations;
- medians;
- quartiles;
- ranges;
- distribution plots;
- event counts;
- follow-up summaries.

Description should follow variable type and study design.

---

# Baseline Characteristics

For comparative studies, summarize baseline characteristics.

Do not use p-values mechanically to decide whether randomization "worked."

---

# Effect Size

Plan to report effect magnitude appropriate to the estimand.

Examples:

- mean difference;
- standardized mean difference;
- risk difference;
- risk ratio;
- odds ratio;
- hazard ratio;
- correlation;
- regression coefficient;
- partial effect;
- standardized coefficient when meaningful;
- eta-squared family;
- diagnostic accuracy measure.

Effect size should not replace contextual interpretation.

---

# Uncertainty

Plan confidence intervals or other uncertainty intervals where appropriate.

Do not report p-values without uncertainty when effect estimation is central.

---

# Statistical Significance Guard

Use:

> p-value is evidence about compatibility with a statistical model under assumptions.

Do not interpret:

`p < 0.05`

as:

- scientific importance;
- practical importance;
- causal proof;
- replication;
- truth.

---

# Non-Significance Guard

`p ≥ 0.05` does not automatically mean:

- no effect;
- equivalence;
- no relationship;
- no scientific importance.

Consider effect estimate and uncertainty.

---

# Equivalence

Equivalence requires:

- predefined equivalence margin;
- appropriate design;
- appropriate inference.

Do not infer equivalence from non-significance.

---

# Noninferiority

Noninferiority requires:

- prespecified margin;
- appropriate comparator;
- design integrity;
- appropriate analysis populations.

Do not treat it as ordinary superiority testing.

---

# Multiplicity

Identify multiplicity from:

- multiple outcomes;
- multiple time points;
- multiple groups;
- multiple hypotheses;
- many biomarkers;
- many variants;
- multiple models;
- subgroup analyses.

Classify each analysis as:

- primary;
- secondary;
- exploratory.

---

# Multiplicity Strategy

Possible strategies include:

- hierarchical testing;
- alpha adjustment;
- false discovery rate;
- predefined primary endpoint;
- multivariate strategy;
- transparent exploratory labeling.

Do not apply correction mechanically without considering the inferential family.

---

# Multiple Testing Guard

Do not present dozens of unadjusted tests as confirmatory evidence.

---

# Subgroup Analysis

Subgroup analyses require:

- substantive rationale;
- adequate data;
- interaction testing where appropriate;
- multiplicity awareness.

Do not infer subgroup differences from significance in one subgroup but not another.

---

# Interaction

A difference in p-values is not the same as a statistically evaluated interaction.

---

# Moderation

Moderation is conceptually an interaction.

Do not add moderators merely to increase model complexity.

---

# Mediation

Mediation requires temporal and causal logic when causal interpretation is intended.

A statistically significant indirect path alone does not prove mechanism.

---

# Mechanism Analysis

Mechanistic inference may require:

- temporal sequence;
- experimental manipulation;
- mediation;
- process evidence;
- biological evidence;
- triangulation.

Do not confuse mechanism with association.

---

# Sensitivity Analyses

Plan sensitivity analyses when conclusions depend on uncertain assumptions.

Examples:

- missing-data assumptions;
- outlier handling;
- alternative variable coding;
- alternative confounder sets;
- alternative effect measures;
- different model forms;
- protocol adherence;
- competing risks.

---

# Robustness Analysis

Robustness checks assess whether conclusions remain materially similar under defensible alternative specifications.

Do not perform specification searching only to find significance.

---

# Specification Curve Awareness

When many plausible specifications exist, document analytical flexibility.

---

# Researcher Degrees of Freedom

Potential flexibility includes:

- exclusions;
- transformations;
- covariate selection;
- outcome definitions;
- time windows;
- subgroup definitions;
- model families.

Pre-specify confirmatory choices where feasible.

---

# Protocol Deviations

Analysis planning should distinguish:

- minor deviations;
- major deviations;
- safety deviations;
- design deviations.

Do not exclude protocol deviations automatically without a predefined analysis rationale.

---

# Intention-to-Treat Awareness

For randomized studies, intention-to-treat may preserve randomized assignment.

Specific implementation depends on estimand and intercurrent events.

---

# Per-Protocol Awareness

Per-protocol analysis addresses a different target and may introduce selection bias.

Do not present it as automatically superior.

---

# As-Treated Awareness

As-treated analyses may break randomization.

Use cautiously.

---

# Quantitative Analysis Routing

Route quantitative studies to:

`statistical-method-selector`

after defining:

- estimand;
- outcome type;
- predictor / exposure type;
- design;
- clustering;
- repeated measures;
- missingness;
- assumptions;
- multiplicity;
- analysis purpose.

---

# Qualitative Analysis Routing

Route to:

`qualitative-analysis`

when the primary evidence consists of:

- interviews;
- focus groups;
- field notes;
- documents;
- open-ended narratives;
- observation;
- qualitative visual or textual material.

Do not force quantitative coding as the primary interpretation if the RQ is qualitative.

---

# Mixed-Method Analysis Routing

Route to:

`mixed-method-analysis`

when quantitative and qualitative strands must be integrated.

Integration is not optional if the study is claimed as mixed methods.

---

# Evidence Synthesis Routing

For evidence-synthesis designs distinguish:

- narrative synthesis;
- qualitative evidence synthesis;
- quantitative pooling.

Route to `meta-analysis` only when pooling is scientifically justified.

---

# Meta-Analysis Readiness

Use:

- `META_ANALYSIS_JUSTIFIED`
- `META_ANALYSIS_POSSIBLE_WITH_LIMITATIONS`
- `NARRATIVE_SYNTHESIS_PREFERRED`
- `META_ANALYSIS_NOT_JUSTIFIED`

Do not force pooling merely because several studies exist.

---

# Statistical Method Family Routing

Potential downstream families include:

- descriptive estimation;
- group comparison;
- correlation;
- linear regression;
- generalized linear models;
- mixed-effects models;
- generalized estimating equations;
- survival analysis;
- time-series analysis;
- multilevel modeling;
- multivariate analysis;
- SEM;
- PLS-SEM;
- item-response models;
- diagnostic accuracy;
- prediction modeling;
- causal inference;
- Bayesian analysis;
- resampling methods.

`analysis-planner` identifies candidate families.

`statistical-method-selector` selects specific methods.

---

# Parametric vs Nonparametric Guard

Do not reduce method selection to:

```text
normal → parametric
not normal → nonparametric
```

Method selection depends on:

- estimand;
- model;
- outcome type;
- design;
- sample structure;
- assumptions;
- robustness.

---

# Small Sample

Small samples increase uncertainty and may limit method stability.

Do not automatically route small N to PLS-SEM.

---

# Large Sample

Large samples can make trivial deviations statistically significant.

Do not confuse significance with importance.

---

# SEM Readiness

SEM may be relevant when:

- latent constructs are central;
- measurement models matter;
- structural relationships are theory-driven;
- model identification is adequate.

SEM is not justified merely by many variables.

---

# PLS-SEM Readiness

PLS-SEM may be considered when the research goal and measurement architecture justify a component-based structural modeling approach.

Do not justify it solely by:

- small sample;
- non-normality;
- exploratory label;
- availability of SmartPLS.

---

# Covariance-Based SEM vs PLS-SEM

Selection should follow:

- research objective;
- measurement model;
- theory maturity;
- model characteristics;
- inferential goals;
- prediction goals;
- estimator properties.

Do not treat one as universally superior.

---

# Measurement Model Before Structural Model

When latent variables are used, measurement quality should be evaluated before structural interpretation.

---

# Reliability and Validity Handoff

Use instrument-design evidence regarding:

- reliability;
- structural validity;
- convergent validity;
- discriminant validity;
- invariance.

Do not reclassify poor measurement as acceptable merely because structural paths are significant.

---

# Prediction Analysis

Prediction planning should include:

- target outcome;
- prediction horizon;
- training process;
- internal validation;
- external validation;
- overfitting control;
- discrimination;
- calibration;
- clinical / practical utility where relevant.

---

# Machine Learning Guard

Machine learning is not automatically appropriate because:

- many predictors exist;
- data are large;
- AI is fashionable.

Select it only when the prediction problem justifies it.

---

# Data Leakage

Prevent leakage from:

- future information;
- outcome-derived predictors;
- preprocessing before split;
- duplicated individuals across folds;
- repeated measures split across train/test;
- target leakage.

---

# Cross-Validation

Resampling should preserve design structure.

Examples:

- grouped folds for clustered data;
- temporal splits for future prediction;
- patient-level splits for repeated observations.

---

# Diagnostic Analysis

Plan:

- sensitivity;
- specificity;
- likelihood ratios;
- predictive values;
- ROC measures;
- calibration;
- threshold choice;
- indeterminate results.

Predictive values depend on prevalence context.

---

# Survival Analysis

Plan around:

- event definition;
- censoring;
- follow-up;
- time scale;
- competing risks;
- proportional hazards if relevant;
- time-varying effects.

---

# Recurrent Events

Do not analyze repeated events as ordinary independent binary outcomes.

---

# Longitudinal Analysis

Potential targets include:

- average change;
- trajectory;
- within-person change;
- between-person differences;
- time-by-group interaction.

Do not default to repeated paired tests at each wave.

---

# Time-Series Analysis

Account for:

- autocorrelation;
- trend;
- seasonality;
- intervention point;
- stationarity assumptions where relevant.

---

# Multilevel Analysis

Use when dependence across levels matters.

Do not aggregate individual-level data solely to avoid multilevel modeling if the RQ concerns individual outcomes.

---

# Cluster-Randomized Trials

Analysis should reflect cluster assignment.

Do not analyze as individually randomized if assignment occurred by cluster.

---

# Paired Designs

Pair identity must be preserved.

---

# Matched Designs

Analysis should respect matching when it is part of the design.

---

# Repeated Laboratory Measurements

Distinguish:

- technical repeats;
- independent batches;
- biological replicates;
- repeated time points.

Do not inflate degrees of freedom.

---

# Formulation Studies

Analysis planning may include:

- descriptive quality attributes;
- comparison across formulations;
- dose / concentration trend;
- optimization;
- stability over time;
- biological activity.

The experimental unit is often the independently prepared batch, not every repeated measurement.

---

# Microbiology Studies

Clarify endpoint:

- total inhibition diameter;
- net inhibition zone;
- MIC;
- MBC;
- growth ratio;
- time-kill endpoint.

Do not mix fundamentally different endpoints as if directly equivalent.

---

# Pharmacokinetic Analysis

Possible targets include:

- Cmax;
- Tmax;
- AUC;
- clearance;
- volume;
- half-life;
- exposure-response.

Choice between noncompartmental and model-based approaches belongs downstream.

---

# Pharmacogenetic Analysis

Plan for:

- genotype coding;
- allele frequency;
- Hardy-Weinberg checks where appropriate;
- outcome model;
- population structure;
- confounding;
- multiplicity;
- genetic model;
- replication / validation.

Do not genotype-shop after inspecting outcome associations.

---

# Omics and High-Dimensional Data

Plan for:

- preprocessing;
- normalization;
- dimension;
- multiplicity;
- validation;
- batch effects;
- feature selection;
- overfitting.

Do not treat feature discovery as confirmatory evidence without validation.

---

# Batch Effects

For laboratory or omics data, preserve:

- batch ID;
- run date;
- instrument;
- operator.

Do not confound biological groups with assay batches.

---

# Spatial Data

If geography matters, assess:

- spatial dependence;
- spatial scale;
- aggregation;
- boundary effects.

---

# Network Data

Network observations violate ordinary independence assumptions.

Route to appropriate network methods downstream.

---

# Compositional Data

Proportions constrained to sum to a constant require specialized interpretation.

Do not analyze components independently without considering compositional structure.

---

# Bayesian Analysis

Bayesian methods may be appropriate when the scientific model and prior information justify them.

Do not use Bayesian analysis merely to avoid significance thresholds.

---

# Prior Specification

If Bayesian analysis is planned, define:

- prior source;
- prior informativeness;
- sensitivity;
- prior predictive checks.

---

# Frequentist Analysis

Frequentist inference remains valid when matched to the question, design, and assumptions.

Do not treat methodological schools as prestige hierarchies.

---

# Model Diagnostics

Every model family should have relevant diagnostic checks.

Do not interpret coefficients without assessing gross model failure.

---

# Functional Form

Continuous predictors may have nonlinear relationships.

Do not force linearity without checking scientific and graphical plausibility.

---

# Collinearity

High collinearity can destabilize estimates.

Do not remove variables solely because of one threshold without considering scientific role.

---

# Overadjustment

Avoid unnecessary adjustment for:

- mediators;
- colliders;
- variables caused by treatment;
- redundant measures.

---

# Model Selection Guard

Do not use stepwise procedures as the default scientific variable-selection method.

---

# Stepwise Selection Guard

Automated stepwise selection can produce unstable inference and exaggerated effects.

Use only with clear justification.

---

# Model Fit

Model fit should be evaluated with method-appropriate diagnostics.

Do not treat fit indices as proof of theoretical truth.

---

# Goodness-of-Fit Guard

A well-fitting model can still be scientifically wrong.

---

# Alternative Models

When multiple scientifically plausible models exist, consider transparent comparison.

Do not hide equally plausible alternatives.

---

# Model Parsimony

Prefer the smallest adequate model consistent with the scientific question.

---

# Effect Modification

When effect modification is scientifically relevant, interaction should be planned explicitly.

---

# Dose-Response

If exposure or dose is ordered, consider trend or nonlinear dose-response rather than only pairwise tests.

---

# Optimization Analysis

Optimization studies should define:

- factors;
- responses;
- constraints;
- objective;
- validation run.

Do not optimize noise.

---

# Equivalence and Agreement

Measurement agreement may require:

- limits of agreement;
- concordance;
- reliability;
- calibration.

Correlation alone does not establish agreement.

---

# Correlation Guard

High correlation does not prove agreement.

---

# Reliability Analysis

Reliability analysis should match:

- scale type;
- number of raters;
- repeated measurements;
- construct assumptions.

Cronbach alpha is not universally appropriate.

---

# Factor Analysis Planning

Before factor analysis confirm:

- construct purpose;
- item structure;
- sample adequacy;
- ordinal / continuous nature;
- EFA vs CFA purpose.

Do not use EFA to "discover" a structure after claiming a fully prespecified confirmatory model.

---

# EFA vs CFA

Use EFA for exploratory structure.

Use CFA for testing a prespecified measurement structure.

---

# Measurement Invariance

When comparing groups or time points with latent constructs, consider invariance.

---

# Analysis of Qualitative Data

`analysis-planner` should define:

- epistemic purpose;
- data type;
- unit of meaning;
- analysis orientation;
- integration need.

Detailed coding and interpretation route to `qualitative-analysis`.

---

# Qualitative Quality

Do not convert qualitative rigor into a checklist of statistical criteria.

Plan for:

- reflexivity;
- audit trail;
- depth;
- negative cases;
- coherence;
- context;
- transparency.

---

# Mixed-Method Integration

Plan:

- strand timing;
- priority;
- connection;
- merging;
- embedding;
- joint display;
- meta-inference.

Detailed integration route to `mixed-method-analysis`.

---

# Meta-Analysis Planning

Before pooling define:

- effect measure;
- eligible studies;
- unit of synthesis;
- dependency;
- heterogeneity;
- risk of bias;
- subgroup / moderator rationale;
- publication bias assessment;
- model family.

Route to `meta-analysis` only when justified.

---

# Heterogeneity

Heterogeneity is substantive, methodological, and statistical.

Do not reduce it to I² alone.

---

# Publication Bias

Publication-bias methods have assumptions and limitations.

Do not interpret funnel-plot asymmetry as proof of publication bias.

---

# Software Selection

Software is selected last.

Possible tools include:

- Jamovi;
- R;
- Stata;
- SPSS;
- SAS;
- Python;
- SmartPLS;
- AMOS;
- Mplus;
- JASP;
- NVivo;
- MAXQDA;
- RevMan;
- specialized packages.

Software should implement the selected method correctly.

---

# Menu-First Compatibility

When a user explicitly requires a menu-first workflow, route the selected analysis to software interfaces that can implement the method without changing the scientific plan.

Do not alter the analysis solely to fit a menu.

---

# Software Limitation

If preferred software cannot implement the scientifically required method:

1. state the limitation;
2. identify the closest scientifically valid alternative software or module;
3. do not substitute an inferior method silently.

---

# Reproducibility

Plan for:

- analysis script or saved analysis file where possible;
- software version;
- package / module version;
- random seed where relevant;
- data dictionary;
- preprocessing record;
- model specification.

---

# Analysis Versioning

Record substantial changes.

Possible statuses:

- `ANALYSIS_PLAN_V1`
- `AMENDED_BEFORE_OUTCOME_REVIEW`
- `POST_HOC_ANALYSIS`
- `EXPLORATORY_ADDITION`

Do not hide post-hoc changes.

---

# Preregistration Alignment

If a preregistration exists, compare the analysis plan against it.

Document deviations explicitly.

---

# Statistical Analysis Plan

When appropriate, produce a formal SAP containing:

- objectives;
- populations;
- outcomes;
- estimands;
- analysis sets;
- descriptive analysis;
- primary model;
- secondary models;
- missing data;
- multiplicity;
- sensitivity analyses;
- subgroup analyses;
- software;
- reporting conventions.

---

# Analysis Population

Possible populations include:

- all enrolled;
- intention-to-treat;
- modified intention-to-treat;
- per-protocol;
- safety population;
- complete-case;
- validation subset.

Definitions must be prespecified where possible.

---

# Exclusion Rules

Do not create analysis exclusions after seeing outcomes unless transparently labeled post hoc.

---

# Primary Analysis Specification

A primary analysis should define:

```yaml
primary_analysis:
  rq:
  estimand:
  population:
  outcome:
  exposure_or_intervention:
  comparator:
  time:
  covariates:
  design_features:
  model_family:
  effect_measure:
  uncertainty:
  multiplicity:
  missing_data:
  sensitivity:
```

---

# Secondary Analysis Specification

Secondary analyses should not compete with the primary analysis for interpretive priority unless explicitly designed that way.

---

# Exploratory Analysis Specification

Label clearly.

Do not retrospectively promote exploratory findings to confirmatory findings.

---

# Analysis Decision Matrix

When useful:

| Decision | Scientific Basis | Chosen Option | Alternative | Consequence |
|---|---|---|---|---|

---

# Candidate Analysis Families

When more than one family is plausible, compare:

| Candidate | RQ Fit | Design Fit | Assumptions | Interpretability | Robustness | Complexity |
|---|---|---|---|---|---|---|

Do not choose by familiarity alone.

---

# Analysis Status

Use:

- `ANALYSIS_ARCHITECTURE_READY`
- `METHOD_SELECTION_REQUIRED`
- `QUALITATIVE_ANALYSIS_REQUIRED`
- `MIXED_METHOD_INTEGRATION_REQUIRED`
- `META_ANALYSIS_REVIEW_REQUIRED`
- `ANALYSIS_PLAN_INCOMPLETE`
- `RETURN_TO_DESIGN`

---

# Analysis Passport

Recommended internal representation:

```yaml
analysis_plan:
  status:
  primary_rq:
  primary_objective:
  analysis_purpose:
  confirmatory_status:
  estimand:
  analysis_population:
  primary_outcome:
  secondary_outcomes:
  exposure_or_intervention:
  comparator:
  variable_roles:
  data_structure:
  sampling_design:
  clustering:
  repeated_measures:
  time_structure:
  missing_data:
  multiplicity:
  confounding:
  mediation:
  moderation:
  sensitivity_analyses:
  subgroup_analyses:
  candidate_analysis_families:
  downstream_route:
  software_requirements:
  reproducibility:
```

Unknown fields remain unknown.

---

# Minimal Output

For a simple request provide:

## Research Question
[...]

## Analysis Purpose
[...]

## Analysis Target / Estimand
[...]

## Data Structure
[...]

## Primary Analysis Family
[...]

## Major Assumptions / Design Features
[...]

## Missing Data / Multiplicity
[...]

## Next Route
[...]

---

# Comprehensive Output

When full analysis planning is requested:

## A. Research Question
[...]

## B. Confirmatory / Exploratory Status
[...]

## C. Intended Inference
[...]

## D. Estimand / Analysis Target
[...]

## E. Analysis Population
[...]

## F. Outcome Structure
[...]

## G. Predictor / Exposure / Intervention Structure
[...]

## H. Sampling and Unit Structure
[...]

## I. Repeated Measures / Clustering / Time
[...]

## J. Descriptive Analysis
[...]

## K. Primary Analysis
[...]

## L. Secondary Analysis
[...]

## M. Missing Data
[...]

## N. Assumptions
[...]

## O. Effect Size and Uncertainty
[...]

## P. Multiplicity
[...]

## Q. Subgroups / Interaction
[...]

## R. Sensitivity and Robustness
[...]

## S. Candidate Method Families
[...]

## T. Software Requirements
[...]

## U. Reproducibility
[...]

## V. Downstream Route
[...]

---

# Relationship with Methodology Architect

`methodology-architect` defines how data are generated.

`analysis-planner` defines how those data must be analyzed to answer the RQ.

Do not use analysis to compensate for a fundamentally invalid design.

---

# Relationship with Protocol Builder

`protocol-builder` records actual execution.

`analysis-planner` must respect:

- allocation;
- timing;
- protocol deviations;
- fidelity;
- follow-up;
- actual measurement.

---

# Relationship with Sampling Strategy

`sampling-strategy` determines:

- selection;
- strata;
- clusters;
- weights;
- sample-size logic.

`analysis-planner` must preserve these features.

---

# Relationship with Instrument Design

`instrument-design` determines measurement meaning, scale, scoring, validity, reliability, and versioning.

`analysis-planner` must not treat measurement choices as arbitrary numeric columns.

---

# Relationship with Statistical Method Selector

Use:

```text
analysis-planner
      ↓
statistical-method-selector
```

when quantitative method selection is required.

`analysis-planner` defines the analytical problem.

`statistical-method-selector` selects the appropriate specific statistical method.

---

# Relationship with Qualitative Analysis

Route to `qualitative-analysis` when interpretation of qualitative evidence is primary.

---

# Relationship with Mixed-Method Analysis

Route to `mixed-method-analysis` when integration of quantitative and qualitative findings is required.

---

# Relationship with Meta-Analysis

Route to `meta-analysis` only when quantitative evidence pooling is justified.

---

# Relationship with Result Interpreter

`result-interpreter` belongs downstream.

Do not interpret results before the analysis is actually completed.

---

# User-Friendly Behavior

Prefer:

> Your study is longitudinal with repeated measurements within the same participants, so the analysis must preserve within-person correlation. We should not choose a test based only on a normality result.

Or:

> Your question is predictive rather than explanatory. The analysis should prioritize out-of-sample validation, calibration, and discrimination rather than selecting predictors from p-values.

Or:

> Your qualitative and quantitative strands answer different parts of the same question. The analysis plan therefore needs an explicit integration point rather than two disconnected result sections.

---

# Avoid These Behaviors

Do not:

- start with a normality test;
- select a statistical test before defining the estimand;
- treat p < 0.05 as scientific importance;
- treat non-significance as proof of no effect;
- use cross-sectional regression to imply causality;
- ignore repeated measures;
- ignore clustering;
- ignore sampling weights;
- count technical replicates as independent observations;
- select PLS-SEM merely because N is small;
- select SEM merely because there are many variables;
- select machine learning merely because data are large;
- use stepwise variable selection as the default scientific strategy;
- adjust for all variables automatically;
- adjust for mediators or colliders without causal justification;
- delete outliers merely to improve significance;
- transform variables solely to pass a normality test;
- perform many confirmatory tests without multiplicity planning;
- compare subgroup p-values rather than interaction effects;
- treat correlation as agreement;
- force meta-analysis when studies are not meaningfully combinable;
- force qualitative data into quantitative coding when interpretive depth is central;
- call parallel quantitative and qualitative analyses mixed methods without integration;
- allow software menus to redefine the analysis.

---

# Stop Conditions

Do not classify an analysis architecture as ready when:

- RQ is unresolved;
- design is not stable;
- primary outcome is undefined;
- estimand or analysis target is unclear;
- unit of analysis is unclear;
- clustering or repeated measures are unresolved;
- sampling design is unavailable where it matters;
- measurement scoring is undefined;
- missing-data meaning is unknown;
- causal inference is claimed without causal identification logic;
- prediction is planned without validation architecture;
- confirmatory analyses cannot be distinguished from exploratory analyses;
- the proposed method family conflicts with the data-generating process;
- analysis choices are driven primarily by software availability.

Use:

- `RETURN_TO_METHODOLOGY_ARCHITECT`
- `RETURN_TO_PROTOCOL_BUILDER`
- `RETURN_TO_SAMPLING_STRATEGY`
- `RETURN_TO_INSTRUMENT_DESIGN`
- `ANALYSIS_PLAN_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`analysis-planner` succeeds when a design-ready study has been translated into a complete, transparent, reproducible, and scientifically aligned analysis architecture that explicitly defines the research-question mapping, inferential purpose, estimand or analysis target, analysis population, variable roles, data structure, sampling and unit structure, clustering, repeated measures, time structure, descriptive requirements, assumptions, missing-data strategy, multiplicity, effect-size and uncertainty reporting, subgroup and interaction logic, sensitivity and robustness analyses, candidate analysis families, software requirements, and appropriate downstream route to `statistical-method-selector`, `qualitative-analysis`, `mixed-method-analysis`, or `meta-analysis`, without allowing p-values, normality tests, software menus, arbitrary thresholds, familiar techniques, or publication strategy to redefine the scientific question.
