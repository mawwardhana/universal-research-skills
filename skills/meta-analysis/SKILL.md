---
name: meta-analysis
description: Determine whether quantitative evidence pooling is scientifically justified and, when appropriate, plan, conduct, document, and audit a meta-analysis from a sufficiently rigorous evidence-synthesis workflow. Use when a systematic review or comparable evidence corpus contains studies that may estimate meaningfully comparable effects and the researcher needs to define the synthesis question, effect measure, unit of analysis, dependency structure, heterogeneity model, weighting, fixed- versus random-effects logic, subgroup and meta-regression analyses, sensitivity analyses, risk-of-bias integration, small-study effects, publication-bias diagnostics, prediction intervals, robustness, and software implementation without forcing statistical pooling merely because multiple studies are available.
---

# Meta-Analysis

## Purpose

`meta-analysis` determines whether quantitative pooling is scientifically defensible and, when it is, constructs the quantitative synthesis architecture.

Its central question is:

> Are the available studies sufficiently comparable in question, population, intervention or exposure, comparator, outcome, design, and effect measure to estimate a meaningful pooled quantity, and if so, what model and diagnostics are required to represent both average effect and between-study uncertainty honestly?

This skill does not assume that every systematic review requires meta-analysis.

It can conclude:

- `META_ANALYSIS_JUSTIFIED`
- `META_ANALYSIS_POSSIBLE_WITH_LIMITATIONS`
- `NARRATIVE_SYNTHESIS_PREFERRED`
- `META_ANALYSIS_NOT_JUSTIFIED`

---

# Core Principle

Use:

> Pool only what is meaningfully combinable.

A statistically computable pooled estimate is not automatically a scientifically meaningful pooled estimate.

The sequence is:

```text
Review Question
      ↓
Eligible Evidence Corpus
      ↓
Clinical / Conceptual Comparability
      ↓
Methodological Comparability
      ↓
Effect-Measure Compatibility
      ↓
Dependency Structure
      ↓
Heterogeneity Assessment
      ↓
Pooling Decision
      ↓
Model Selection
      ↓
Robustness / Bias / Sensitivity
      ↓
Interpretation
```

Do not begin with software.

---

# Position in the Framework

Preferred route:

```text
systematic-review / evidence-synthesis workflow
                ↓
         analysis-planner
                ↓
           meta-analysis
                ↓
        result-interpreter
```

If pooling is not justified:

```text
meta-analysis
      ↓
NARRATIVE_SYNTHESIS_PREFERRED
```

---

# Required Upstream Context

Use established information from:

- `literature-screening`;
- `evidence-synthesis`;
- `source-verification`;
- `reference-integrity-guard`;
- `analysis-planner`;
- systematic-review methods when available.

Minimum useful context normally includes:

- review question;
- eligibility criteria;
- study designs;
- population;
- intervention / exposure;
- comparator;
- outcomes;
- effect measures;
- follow-up periods;
- risk-of-bias information;
- study-level data;
- duplicate-population information;
- multiple-outcome or multiple-time-point structure.

Do not ask the researcher to repeat information already established.

---

# Readiness Gate

Classify:

- `READY_FOR_META_ANALYSIS_REVIEW`
- `EVIDENCE_CORPUS_NOT_READY`
- `OUTCOME_HARMONIZATION_INCOMPLETE`
- `EFFECT_MEASURE_UNCLEAR`
- `DEPENDENCY_STRUCTURE_UNCLEAR`
- `RISK_OF_BIAS_INCOMPLETE`
- `META_ANALYSIS_ALREADY_PLANNED`
- `META_ANALYSIS_REQUIRES_REASSESSMENT`

Do not pool before the evidence corpus is stable enough.

---

# Meta-Analysis Justification Gate

Before any model is fit, answer:

1. Are the studies addressing sufficiently comparable scientific questions?
2. Are populations meaningfully comparable?
3. Are intervention / exposure definitions compatible?
4. Are comparators compatible?
5. Are outcomes measuring the same or transformably comparable constructs?
6. Are follow-up windows compatible?
7. Are study designs sufficiently compatible for the intended synthesis?
8. Can effect estimates be transformed to a common metric without distorting meaning?
9. Can dependencies be modeled or resolved?
10. Would a pooled result have a coherent scientific interpretation?

If several answers are no, pooling may be inappropriate.

---

# Scientific Comparability

Evaluate:

- clinical comparability;
- conceptual comparability;
- methodological comparability;
- measurement comparability;
- temporal comparability;
- population comparability;
- intervention / exposure comparability;
- comparator comparability.

Statistical similarity is secondary to scientific comparability.

---

# Clinical Heterogeneity

Potential sources include:

- age;
- disease severity;
- setting;
- dose;
- intervention intensity;
- co-interventions;
- baseline risk;
- follow-up;
- population composition.

Clinical heterogeneity should be examined before statistical heterogeneity.

---

# Methodological Heterogeneity

Potential sources include:

- randomized vs observational design;
- blinded vs unblinded outcome assessment;
- outcome definition;
- measurement instrument;
- adjustment set;
- analytic model;
- missing-data strategy;
- risk of bias.

---

# Statistical Heterogeneity

Statistical heterogeneity reflects variation in observed effects beyond sampling error under the chosen model.

Do not reduce heterogeneity to one statistic.

---

# Pooling Decision Status

Use one of:

- `POOLING_APPROPRIATE`
- `POOLING_CONDITIONALLY_APPROPRIATE`
- `POOLING_BY_SUBGROUP_ONLY`
- `POOLING_NOT_APPROPRIATE`
- `MORE_HARMONIZATION_REQUIRED`

---

# Unit of Synthesis

Define the unit actually being pooled.

Examples:

- one independent effect per study;
- one effect per trial arm comparison;
- one effect per outcome domain;
- one effect per time point;
- one effect per cohort;
- one effect per genetic contrast.

Do not assume one paper equals one independent study.

---

# Study vs Report

Multiple publications may represent the same underlying study population.

Use:

`DUPLICATE_POPULATION_RISK`

when needed.

Merge or select effects transparently.

---

# Multiple Effects per Study

A study may contribute multiple effects because of:

- multiple outcomes;
- multiple time points;
- multiple intervention arms;
- multiple subgroups;
- multiple instruments.

These effects are often dependent.

Do not treat them as independent automatically.

---

# Dependency Handling

Possible strategies include:

- select one prespecified effect;
- combine correlated outcomes;
- multilevel meta-analysis;
- multivariate meta-analysis;
- robust variance estimation;
- cluster by study;
- sensitivity analyses.

The strategy should match the scientific question.

---

# Effect Measure

Choose a common effect measure that preserves scientific meaning.

Possible measures include:

- mean difference;
- standardized mean difference;
- response ratio;
- risk ratio;
- odds ratio;
- risk difference;
- hazard ratio;
- incidence rate ratio;
- correlation;
- Fisher z;
- diagnostic accuracy measures;
- prevalence;
- proportion;
- single-group mean;
- genetic odds ratio.

---

# Mean Difference

Use when outcomes share the same scale and meaning.

Prefer raw mean difference when it is directly interpretable.

---

# Standardized Mean Difference

Use when studies measure the same underlying construct using different scales.

Potential forms include:

- Cohen d;
- Hedges g.

Do not standardize merely because scales have different numerical ranges if constructs are not truly comparable.

---

# Standardized Mean Difference Guard

SMD can be influenced by between-study differences in standard deviation.

Interpret carefully.

---

# Response Ratio

May be useful for some biological or ecological outcomes when ratio-scale interpretation is meaningful.

---

# Risk Ratio

Useful for binary outcomes when risk ratio is interpretable.

---

# Odds Ratio

Common in case-control studies and logistic models.

Do not describe odds ratio as risk ratio automatically.

---

# Risk Difference

Provides absolute difference in event probability.

Can be highly interpretable but sensitive to baseline risk.

---

# Hazard Ratio

Appropriate for time-to-event effects under compatible definitions.

Do not combine hazard ratios with risk ratios as if they were equivalent.

---

# Correlation Meta-Analysis

Transform correlations when appropriate, commonly using Fisher z.

Back-transform for interpretation.

---

# Proportion Meta-Analysis

Pooling proportions requires care because:

- variance depends on proportion;
- rare events may create instability;
- transformations alter interpretation.

Do not apply arbitrary transformations mechanically.

---

# Diagnostic Meta-Analysis

Diagnostic sensitivity and specificity are paired quantities.

Do not pool them independently without considering threshold and correlation.

Potential models include:

- bivariate random-effects models;
- hierarchical summary ROC models.

---

# Rare Events

Potential issues include:

- zero cells;
- double-zero studies;
- sparse estimates;
- unstable normal approximations.

Do not add continuity corrections automatically without sensitivity analysis.

---

# Zero Events

Strategies depend on effect measure and model.

Document handling explicitly.

---

# Conversion of Effect Measures

If conversion is necessary:

- preserve formula;
- document assumptions;
- assess whether conversion changes meaning;
- perform sensitivity analysis if uncertain.

Do not convert incompatible estimands merely to enable pooling.

---

# Direction Harmonization

Ensure all effects point in the same conceptual direction.

Example:

```text
positive = better outcome
negative = worse outcome
```

Document any sign reversal.

---

# Outcome Harmonization

For each outcome record:

```yaml
outcome_harmonization:
  study:
  original_outcome:
  original_scale:
  harmonized_construct:
  harmonized_effect:
  transformation:
  direction:
  assumptions:
```

---

# Follow-Up Harmonization

Do not pool:

- immediate post-treatment;
- 3-month;
- 12-month;

as one time point unless scientifically justified.

Possible approach:

- short-term;
- medium-term;
- long-term;

with prespecified windows.

---

# Intervention Harmonization

Consider:

- dose;
- intensity;
- route;
- duration;
- co-intervention.

Pooling may require subgrouping.

---

# Comparator Harmonization

Do not combine:

- placebo;
- no treatment;
- active comparator;
- usual care;

as one comparator without justification.

---

# Study Design Harmonization

Possible strategies:

- pool RCTs separately;
- pool observational studies separately;
- combine only under explicit assumptions;
- use design as moderator.

Do not automatically merge fundamentally different design classes.

---

# Adjusted vs Unadjusted Effects

For observational studies, adjusted and unadjusted estimates target different conditional relationships.

Prefer prespecified adjusted estimates when confounding control is scientifically required.

Do not mix adjusted and unadjusted estimates without justification.

---

# Adjustment Set Compatibility

Different studies may adjust for different confounders.

Document this as methodological heterogeneity.

---

# Primary Effect Selection Rule

Before examining pooled significance, define rules for selecting:

- outcome;
- time point;
- adjusted model;
- intervention comparison;
- subgroup.

Avoid significance-driven effect selection.

---

# Effect Extraction

For each study retain:

```yaml
study_effect:
  study_id:
  effect_measure:
  estimate:
  standard_error:
  lower_ci:
  upper_ci:
  sample_size:
  events:
  outcome:
  time:
  comparison:
  adjusted:
  model:
  notes:
```

---

# Variance Recovery

When standard errors are unavailable, they may sometimes be derived from:

- confidence intervals;
- p-values;
- test statistics;
- standard deviations;
- sample sizes.

Document formulas and assumptions.

---

# Imputed Variance

If variance must be imputed, label it clearly.

Use sensitivity analysis.

---

# Fixed-Effect Model

A fixed-effect model assumes all included studies estimate one common underlying effect, conditional on the model.

Use only when scientifically plausible.

Do not choose fixed-effect merely because heterogeneity test p > 0.05.

---

# Random-Effects Model

Random-effects models allow true effects to vary across studies.

This does not mean all heterogeneity is explained.

The pooled estimate represents an average across a distribution of effects.

---

# Fixed vs Random Guard

Do not use:

```text
I² < 50% → fixed
I² ≥ 50% → random
```

as an automatic rule.

Model choice should follow the scientific assumption about effect variation.

---

# Random-Effects Estimator

Possible estimators include:

- REML;
- Paule-Mandel;
- DerSimonian-Laird;
- ML;
- empirical Bayes approaches.

Prefer estimators with sound statistical properties.

Do not default mechanically to DerSimonian-Laird.

---

# Hartung-Knapp Adjustment

For random-effects meta-analysis, Hartung-Knapp-type adjustments may improve uncertainty estimation in some settings, especially with few studies.

Use with judgment.

---

# Number of Studies

Few studies create substantial uncertainty in:

- tau²;
- heterogeneity;
- prediction intervals;
- meta-regression;
- funnel asymmetry tests.

Do not overinterpret precise-looking pooled estimates from very few studies.

---

# Between-Study Variance

Commonly denoted:

`tau²`

This quantifies estimated between-study variance on the chosen effect scale.

---

# Tau

`tau`

is the standard deviation of the distribution of true effects on the chosen scale.

---

# I²

I² describes the proportion of observed variation attributable to heterogeneity rather than within-study sampling error under the model.

Do not treat thresholds such as:

- 25%;
- 50%;
- 75%;

as universal scientific categories.

---

# Q Statistic

Cochran's Q tests whether observed variability exceeds what is expected from sampling error under a common-effect model.

It has low power with few studies and excessive power with many studies.

Do not use Q alone to decide model type.

---

# Prediction Interval

A prediction interval estimates the range in which a true effect from a new comparable study may plausibly lie under a random-effects model.

When heterogeneity is meaningful, prediction intervals can be more informative than the pooled confidence interval.

---

# Prediction Interval Guard

With very few studies or unstable tau², prediction intervals may be imprecise.

Interpret accordingly.

---

# Forest Plot

A forest plot should display:

- study estimate;
- confidence interval;
- study weight;
- pooled estimate;
- heterogeneity metrics when appropriate.

Do not let visual appearance replace numerical interpretation.

---

# Weighting

Inverse-variance weighting is common.

Weights depend on:

- within-study variance;
- between-study variance under random effects.

Large studies do not always dominate strongly under random-effects models.

---

# Heterogeneity Exploration

Potential moderators include:

- population;
- intervention dose;
- follow-up;
- setting;
- risk of bias;
- study design;
- measurement tool;
- geography;
- baseline severity;
- age;
- publication year.

Moderators should be scientifically justified.

---

# Subgroup Meta-Analysis

Subgroups may be appropriate when categories are prespecified and scientifically meaningful.

Do not conclude subgroup differences because one subgroup is significant and another is not.

Use a formal test of subgroup difference where appropriate.

---

# Meta-Regression

Meta-regression models study-level moderators.

Potential limitations:

- ecological bias;
- low power;
- multiple testing;
- collinearity;
- sparse moderator distribution.

Do not interpret study-level meta-regression as individual-level causal evidence.

---

# Meta-Regression Sample Size Guard

Meta-regression with very few studies is unstable.

Do not add many moderators to a small evidence base.

---

# Ecological Bias

Study-level associations may differ from participant-level associations.

Do not infer individual-level effects from study-level moderator results.

---

# Continuous Moderators

Avoid arbitrary categorization when continuous moderator modeling is feasible.

---

# Nonlinear Moderator Effects

Consider when scientifically plausible and data support it.

Do not overfit.

---

# Multiple Moderators

Multiplicity and collinearity matter.

Predefine key moderators where possible.

---

# Sensitivity Analysis

Plan analyses that challenge key decisions.

Possible sensitivity analyses:

- exclude high-risk-of-bias studies;
- alternative effect conversions;
- alternative tau² estimators;
- Hartung-Knapp vs conventional intervals;
- leave-one-out;
- exclude imputed data;
- exclude outliers;
- adjusted vs unadjusted effects;
- alternative time windows;
- alternative outcome definitions.

---

# Leave-One-Out Analysis

Assess whether one study disproportionately drives the pooled result.

Do not interpret instability as proof that the influential study is invalid.

---

# Influence Diagnostics

Possible diagnostics include:

- externally standardized residuals;
- Cook-like distances;
- hat values;
- DFBETAS;
- Baujat plots.

Use them as diagnostics, not automatic exclusion rules.

---

# Outlier Study Guard

Do not remove studies merely because they increase heterogeneity or change significance.

First assess:

- data extraction;
- design;
- population;
- outcome;
- methodological differences.

---

# Robustness

A robust conclusion should not depend entirely on one arbitrary modeling choice.

---

# Risk of Bias Integration

Risk of bias should inform interpretation and sensitivity analysis.

Do not simply assign numeric quality scores and weight studies by those scores.

---

# Quality Score Guard

Avoid generic composite study-quality scores as meta-analytic weights unless a validated method explicitly justifies them.

---

# High Risk of Bias Studies

Possible strategies:

- include but flag;
- sensitivity analysis excluding;
- subgroup analysis;
- downgrade confidence.

Do not exclude solely because results are inconvenient.

---

# Certainty of Evidence

Certainty frameworks such as GRADE may be used downstream.

Meta-analysis alone does not determine certainty.

---

# Small-Study Effects

Small-study effects refer to systematic differences between smaller and larger studies.

They can arise from:

- publication bias;
- selective reporting;
- methodological differences;
- true heterogeneity;
- chance.

---

# Funnel Plot

Funnel plots visualize relation between effect and precision.

Do not interpret asymmetry as proof of publication bias.

---

# Funnel Plot Readiness

Funnel plots are usually weakly informative with very few studies.

Avoid overinterpretation.

---

# Egger-Type Tests

Regression-based asymmetry tests may be used when appropriate.

They can have low power.

---

# Begg-Type Tests

Rank-based asymmetry tests may also be considered.

Do not treat a non-significant test as proof of no publication bias.

---

# Trim-and-Fill Guard

Trim-and-fill is an exploratory method with strong assumptions.

Do not use it as a definitive correction for publication bias.

---

# Selection Models

Selection models can evaluate publication-selection mechanisms under explicit assumptions.

Use cautiously.

---

# P-Curve / Related Methods

These methods have narrow applicability and assumptions.

Do not use them as universal publication-bias diagnostics.

---

# Registered Reports / Unpublished Studies

When available, these may help assess selective publication.

---

# Outcome Reporting Bias

Publication bias is not the only reporting problem.

Within-study selective outcome reporting may also distort synthesis.

---

# Duplicate Publication

Check whether multiple papers report overlapping participants.

Do not double-count participants.

---

# Multiple Arms

In multi-arm trials, avoid double-counting shared comparator groups.

Possible approaches:

- combine intervention arms;
- split comparator group;
- multivariate model;
- select one prespecified comparison.

---

# Cluster-Randomized Trials

Account for clustering if original estimates do not already do so.

Do not treat participant counts as independent when cluster design is ignored.

---

# Cross-Over Trials

Cross-over designs require paired-data handling.

Do not treat arms as independent parallel groups.

---

# Pre-Post Studies

Pre-post designs require change-score or paired information.

Do not pool with parallel-group post-only effects without compatible effect definition.

---

# Change Score Meta-Analysis

If change scores are used, preserve correlation assumptions when reconstructing variances.

---

# Standard Error Harmonization

Ensure all variances correspond to the effect measure being pooled.

---

# Log Scale

Some effects are analyzed on log scale:

- RR;
- OR;
- HR;
- IRR.

Pool on log scale and back-transform for interpretation.

---

# Correlation Between Effects

When multiple correlated effects are included, use a method that respects dependency.

---

# Multilevel Meta-Analysis

Useful when effects are nested within:

- studies;
- cohorts;
- outcomes;
- time points.

---

# Multivariate Meta-Analysis

Useful when multiple correlated outcomes are synthesized jointly.

Requires covariance information or assumptions.

---

# Robust Variance Estimation

RVE can handle dependent effect sizes under certain conditions.

Small-sample corrections may be needed.

---

# Network Meta-Analysis Boundary

Network meta-analysis is a specialized extension.

Do not perform it unless assumptions such as:

- transitivity;
- consistency;
- connected network;

are defensible.

Route to a specialized method if needed.

---

# Individual Participant Data Meta-Analysis Boundary

IPD meta-analysis requires participant-level datasets and specialized modeling.

Do not treat aggregate-data meta-analysis as equivalent.

---

# Meta-Analysis of Observational Studies

Potential issues include:

- confounding;
- heterogeneous adjustment;
- selection bias;
- reverse causation;
- exposure misclassification.

Pooling does not remove these biases.

---

# Genetic Association Meta-Analysis

Potential issues include:

- allele coding;
- strand alignment;
- ancestry;
- HWE;
- genotype model;
- population stratification;
- multiple testing.

Do not combine incompatible genetic models without clear transformation.

---

# Pharmacogenetic Meta-Analysis

Consider:

- treatment consistency;
- drug dose;
- phenotype definition;
- genotype coding;
- ancestry;
- interaction vs main-effect estimates.

---

# Prevalence Meta-Analysis

Potential issues include:

- sampling frame;
- diagnostic criteria;
- geography;
- time period;
- age distribution;
- transformation.

A pooled prevalence may be meaningless under extreme contextual heterogeneity.

---

# Incidence Meta-Analysis

Preserve person-time units and comparable definitions.

---

# Diagnostic Accuracy Meta-Analysis

Consider:

- threshold effects;
- spectrum;
- reference standard;
- partial verification;
- differential verification.

Prefer hierarchical models.

---

# Dose-Response Meta-Analysis

Potential approaches:

- categorical dose comparisons;
- linear dose-response;
- nonlinear dose-response.

Requires compatible dose information.

---

# Time-to-Event Meta-Analysis

Prefer hazard ratios when the target is relative event rate over time under compatible definitions.

Do not substitute odds ratios without justification.

---

# Adverse Event Meta-Analysis

Rare events and inconsistent reporting are common.

Use appropriate sparse-data methods.

---

# Continuous Outcome Scale Direction

Ensure higher scores mean the same conceptual direction across studies.

---

# Composite Outcomes

Do not pool different composite outcomes as one construct without checking component compatibility.

---

# Surrogate Outcomes

Surrogate and clinical outcomes should not be pooled together automatically.

---

# Selective Inclusion Guard

Do not select only studies with extractable favorable results.

Document unavailable data.

---

# Missing Study Data

Possible actions:

- contact authors;
- derive from reported statistics;
- impute cautiously;
- exclude with explanation.

---

# Author Contact

Document:

- date;
- request;
- response;
- data received.

---

# Data Extraction Verification

Meta-analysis is highly sensitive to extraction errors.

Use independent checking when feasible.

---

# Double Data Extraction

May reduce errors for:

- effect estimates;
- sample sizes;
- variances;
- event counts;
- study characteristics.

---

# Calculation Audit

Preserve formulas for:

- effect conversion;
- variance recovery;
- group combination;
- direction reversal;
- standardization.

---

# Reproducibility

Record:

- software;
- package;
- version;
- model;
- estimator;
- code;
- data file;
- random seed where relevant.

---

# Software

Possible tools include:

- R;
- Stata;
- RevMan;
- Jamovi modules;
- JASP;
- Comprehensive Meta-Analysis;
- specialized diagnostic meta-analysis software.

Software is selected after the model is justified.

---

# R Ecosystem

Common R packages may include:

- `metafor`;
- `meta`;
- `clubSandwich`;
- `dosresmeta`;
- specialized diagnostic or network packages.

Do not choose a package before selecting the model.

---

# Jamovi Compatibility

If the user requires Jamovi-first workflow:

1. determine the scientifically appropriate synthesis model;
2. identify available Jamovi meta-analysis modules;
3. use menu-based analysis when the required model is supported;
4. use Rj only when necessary;
5. do not simplify the scientific model merely to fit an available menu.

---

# RevMan Compatibility

RevMan supports many standard pairwise meta-analyses.

It may not support all advanced dependency or meta-regression structures.

Do not alter the research question to fit software limitations.

---

# Forest Plot Reporting

Include where appropriate:

- study labels;
- effect estimates;
- confidence intervals;
- weights;
- pooled effect;
- heterogeneity.

Avoid visual clutter.

---

# Funnel Plot Reporting

Only when scientifically interpretable.

State limitations explicitly.

---

# Model Reporting

Report:

- effect measure;
- fixed or random logic;
- tau² estimator;
- interval method;
- number of studies;
- heterogeneity;
- prediction interval where appropriate.

---

# Heterogeneity Reporting

Prefer reporting:

- Q;
- tau²;
- tau;
- I²;
- prediction interval;

when relevant.

Do not rely on I² alone.

---

# Interpretation of Average Effect

The pooled effect is an average under the model.

It may not represent every population or setting.

---

# Significance Guard

Do not interpret:

`pooled p < 0.05`

as proof of universal effectiveness.

---

# Non-Significance Guard

A non-significant pooled result may still be compatible with clinically meaningful effects.

Consider interval width and heterogeneity.

---

# Prediction Interval Interpretation

A prediction interval crossing the null may indicate substantial uncertainty in effect direction across future comparable settings even when the average effect is statistically significant.

---

# Clinical Importance

Separate:

- statistical significance;
- average effect magnitude;
- clinical relevance;
- heterogeneity;
- certainty.

---

# Narrative Synthesis Exit

When pooling is not justified, return:

`NARRATIVE_SYNTHESIS_PREFERRED`

with reasons such as:

- incompatible outcomes;
- incompatible designs;
- severe clinical heterogeneity;
- insufficient comparable data;
- irreducible dependency;
- effect measures not harmonizable.

---

# Narrative Synthesis Is Not Failure

A rigorous narrative synthesis can be scientifically superior to an incoherent pooled estimate.

---

# Meta-Analysis Plan

Recommended structure:

```yaml
meta_analysis_plan:
  status:
  review_question:
  eligible_studies:
  unit_of_synthesis:
  population:
  intervention_or_exposure:
  comparator:
  outcome:
  follow_up:
  effect_measure:
  effect_selection_rule:
  dependency:
  fixed_or_random_logic:
  tau2_estimator:
  interval_method:
  heterogeneity:
  prediction_interval:
  subgroup_analyses:
  meta_regression:
  sensitivity_analyses:
  risk_of_bias_integration:
  small_study_effects:
  software:
  reproducibility:
```

---

# Study-Level Data Table

Recommended:

| Study | Design | Population | Comparison | Outcome | Effect | SE | Follow-Up | Risk of Bias |
|---|---|---|---|---|---|---|---|---|

---

# Harmonization Table

| Study | Original Measure | Converted Measure | Transformation | Assumption | Status |
|---|---|---|---|---|---|

---

# Dependency Table

| Study | Number of Effects | Dependency Source | Resolution Strategy |
|---|---:|---|---|

---

# Heterogeneity Table

| Moderator | Scientific Rationale | Prespecified | Analysis Type |
|---|---|---|---|

---

# Sensitivity Table

| Sensitivity Analysis | Assumption Challenged | Result Impact | Interpretation |
|---|---|---|---|

---

# Minimal Output

For a simple request provide:

## Pooling Decision
[...]

## Effect Measure
[...]

## Model
[...]

## Heterogeneity
[...]

## Dependency Handling
[...]

## Sensitivity Analyses
[...]

## Bias / Small-Study Effects
[...]

## Interpretation
[...]

---

# Comprehensive Output

When full meta-analysis planning is requested:

## A. Review Question
[...]

## B. Pooling Justification
[...]

## C. Eligible Study Set
[...]

## D. Unit of Synthesis
[...]

## E. Clinical Comparability
[...]

## F. Methodological Comparability
[...]

## G. Outcome Harmonization
[...]

## H. Effect Measure
[...]

## I. Dependency Structure
[...]

## J. Fixed / Random Logic
[...]

## K. Between-Study Variance
[...]

## L. Heterogeneity
[...]

## M. Prediction Interval
[...]

## N. Subgroups
[...]

## O. Meta-Regression
[...]

## P. Sensitivity Analyses
[...]

## Q. Risk of Bias Integration
[...]

## R. Small-Study Effects
[...]

## S. Publication-Bias Diagnostics
[...]

## T. Software
[...]

## U. Reproducibility
[...]

## V. Interpretation Boundaries
[...]

---

# Relationship with Analysis Planner

`analysis-planner` determines that quantitative evidence synthesis is a candidate analytical route.

`meta-analysis` determines whether pooling is justified and how to perform it.

Use:

```text
analysis-planner
      ↓
meta-analysis
```

---

# Relationship with Evidence Synthesis

`evidence-synthesis` organizes the scholarly evidence base.

`meta-analysis` is one possible quantitative synthesis of that evidence.

Meta-analysis must not replace conceptual synthesis.

---

# Relationship with Literature Screening

Eligibility decisions should be finalized or sufficiently stable before pooling.

Do not include studies because their results are convenient.

---

# Relationship with Source Verification

Only verified sources should support the synthesis.

Unverified references should not silently enter pooled estimates.

---

# Relationship with Reference Integrity Guard

Study identity, DOI, publication, and duplicate-population integrity should be verified before effect extraction.

---

# Relationship with Statistical Method Selector

Primary-study statistical methods are distinct from meta-analytic methods.

Do not route study-level regression choices into this skill unless they affect extracted effect interpretation.

---

# Relationship with Result Interpreter

Pass downstream:

- pooled estimate;
- uncertainty;
- heterogeneity;
- prediction interval;
- risk-of-bias context;
- sensitivity results;
- small-study-effect diagnostics;
- limitations.

---

# User-Friendly Behavior

Prefer:

> These studies all examine the same intervention, but they use different outcome instruments that measure the same construct. A standardized mean difference may permit pooling, but we should first verify that higher scores have the same conceptual direction and that follow-up windows are comparable.

Or:

> The I² value alone should not determine fixed versus random effects. Here the populations, settings, and intervention intensity differ meaningfully, so a random-effects model is scientifically more plausible even before looking at I².

Or:

> There are only three studies and their populations and outcomes differ substantially. A pooled number would be easy to compute but difficult to interpret, so narrative synthesis is the stronger option.

---

# Avoid These Behaviors

Do not:

- force meta-analysis because several studies exist;
- use I² thresholds as the only model-selection rule;
- default automatically to DerSimonian-Laird;
- treat one paper as one independent study without checking overlapping populations;
- double-count shared control groups;
- treat multiple effects from one study as independent;
- mix incompatible effect measures;
- mix incompatible time points;
- mix adjusted and unadjusted estimates without justification;
- pool RCTs and observational studies automatically;
- remove studies merely to reduce heterogeneity;
- exclude unfavorable studies;
- use subgroup significance differences instead of interaction tests;
- fit many meta-regression moderators with few studies;
- infer participant-level relationships from study-level moderators;
- interpret funnel asymmetry as proof of publication bias;
- use trim-and-fill as a definitive correction;
- treat pooled significance as universal effectiveness;
- ignore prediction intervals when heterogeneity is meaningful;
- let software defaults determine the model;
- treat narrative synthesis as methodological failure.

---

# Stop Conditions

Do not classify a meta-analysis as ready when:

- the evidence corpus is unstable;
- study identity or duplicate populations are unresolved;
- outcomes are not conceptually comparable;
- effect measures cannot be harmonized defensibly;
- follow-up windows are incompatible;
- dependency is ignored;
- the unit of synthesis is unclear;
- risk-of-bias information is unavailable where it materially affects interpretation;
- the planned moderator model is too complex for the number of studies;
- software limitations are driving the scientific model;
- a pooled estimate would not have a coherent scientific interpretation.

Use:

- `RETURN_TO_EVIDENCE_SYNTHESIS`
- `RETURN_TO_LITERATURE_SCREENING`
- `RETURN_TO_ANALYSIS_PLANNER`
- `OUTCOME_HARMONIZATION_REQUIRED`
- `DEPENDENCY_RESOLUTION_REQUIRED`
- `META_ANALYSIS_REQUIRES_REVISION`
- `NARRATIVE_SYNTHESIS_PREFERRED`

when appropriate.

---

# Success Criterion

`meta-analysis` succeeds when a sufficiently rigorous evidence corpus has been evaluated for scientific poolability and, where pooling is justified, translated into a transparent, reproducible, and statistically coherent synthesis architecture that explicitly defines the unit of synthesis, study independence, outcome and follow-up harmonization, effect measure, effect-selection rule, dependency handling, fixed- or random-effects logic, between-study variance estimator, interval method, heterogeneity assessment, prediction interval, subgroup and meta-regression strategy, risk-of-bias integration, sensitivity analyses, small-study-effect and publication-bias diagnostics, software implementation, and interpretation boundaries, while allowing `NARRATIVE_SYNTHESIS_PREFERRED` when pooling would be scientifically misleading and preventing I² thresholds, software defaults, significance chasing, arbitrary study exclusion, or the mere existence of multiple studies from forcing an incoherent pooled estimate.
