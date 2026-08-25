---
name: statistical-method-selector
description: Select the scientifically appropriate quantitative statistical method after the analysis architecture is defined. Use when the research question, estimand or analysis target, study design, outcome type, predictor or exposure structure, sampling design, clustering, repeated measures, timing, missingness, multiplicity, measurement model, and inferential goal are sufficiently clear and the researcher needs to choose among descriptive, comparative, regression, longitudinal, multilevel, survival, diagnostic, predictive, causal, SEM, PLS-SEM, reliability, validation, or other quantitative methods without using normality tests, software menus, sample-size folklore, or p-value chasing as the primary decision rule.
---

# Statistical Method Selector

## Purpose

`statistical-method-selector` selects the specific quantitative statistical method or model family that best matches a completed analysis architecture.

Its central question is:

> Given the scientific estimand, study design, outcome distribution, predictor structure, sampling and dependency structure, measurement architecture, and inferential purpose, which statistical method can estimate the target quantity with the fewest unsupported assumptions and the clearest interpretation?

This skill operates after:

`analysis-planner`

It does not define:

- the research question;
- the scientific estimand;
- the study design;
- the sampling strategy;
- the measurement construct;
- the causal question.

Those belong upstream.

---

# Core Principle

Use:

> Estimand before estimator. Design before model. Data structure before software.

Do not select a method by asking only:

- Is the data normal?
- Is p < 0.05?
- Is N small?
- Is the questionnaire Likert?
- Is SmartPLS available?
- Is the method popular?

Method selection must begin from the scientific analysis target.

---

# Position in the Framework

Preferred route:

```text
Research Question
      ↓
Methodology
      ↓
Sampling / Measurement / Protocol
      ↓
analysis-planner
      ↓
statistical-method-selector
      ↓
method-specific execution
      ↓
result-interpreter
```

`statistical-method-selector` is a quantitative method-selection layer.

It is not the execution layer itself.

---

# Required Upstream Context

Use established information from:

- `analysis-planner`;
- `methodology-architect`;
- `sampling-strategy`;
- `instrument-design`;
- `protocol-builder`;
- `hypothesis-builder`;
- `conceptual-framework`.

Minimum useful context normally includes:

- primary RQ;
- analysis target or estimand;
- confirmatory vs exploratory status;
- study design;
- analysis population;
- outcome type;
- exposure / predictor / intervention type;
- comparator;
- unit of analysis;
- repeated measures;
- clustering;
- matching;
- sampling weights;
- time structure;
- missing-data context;
- multiplicity;
- measurement type;
- causal or predictive goal when relevant.

Do not ask the researcher to repeat information already established.

---

# Readiness Gate

Classify:

- `READY_FOR_STATISTICAL_METHOD_SELECTION`
- `ANALYSIS_TARGET_UNCLEAR`
- `DESIGN_STRUCTURE_UNCLEAR`
- `OUTCOME_TYPE_UNCLEAR`
- `DEPENDENCY_STRUCTURE_UNCLEAR`
- `MEASUREMENT_MODEL_UNCLEAR`
- `CAUSAL_TARGET_UNCLEAR`
- `PREDICTION_TARGET_UNCLEAR`
- `METHOD_ALREADY_SELECTED`
- `METHOD_REQUIRES_REASSESSMENT`

Do not select a method when the inferential target is not clear.

---

# Decision Hierarchy

Select methods in this order:

```text
1. What is the scientific target?
2. What design generated the data?
3. What is the unit of analysis?
4. What is the outcome type?
5. What dependence structure exists?
6. What predictor / exposure structure exists?
7. Is the goal description, estimation, explanation, causation, prediction, validation, or diagnosis?
8. What assumptions are scientifically plausible?
9. What method families can estimate the target?
10. Which method is most interpretable and robust?
11. Which software can implement it correctly?
```

Do not invert this hierarchy.

---

# Analysis Purpose Classes

Possible purposes:

- `DESCRIPTIVE`
- `ESTIMATION`
- `GROUP_COMPARISON`
- `ASSOCIATION`
- `EXPLANATION`
- `CAUSAL_EFFECT`
- `MEDIATION`
- `MODERATION`
- `PREDICTION`
- `DIAGNOSIS`
- `PROGNOSIS`
- `LONGITUDINAL_CHANGE`
- `TIME_TO_EVENT`
- `REPEATED_MEASURES`
- `MULTILEVEL`
- `MEASUREMENT_VALIDATION`
- `RELIABILITY`
- `LATENT_VARIABLE_MODELING`
- `DOSE_RESPONSE`
- `PHARMACOKINETIC`
- `PHARMACOGENETIC`
- `OPTIMIZATION`
- `AGREEMENT`
- `EQUIVALENCE`
- `NONINFERIORITY`

---

# Outcome Type

Classify the primary outcome as:

- binary;
- nominal multicategory;
- ordinal;
- count;
- rate;
- continuous;
- bounded continuous;
- proportion;
- repeated continuous;
- repeated binary;
- repeated ordinal;
- time-to-event;
- competing-risk;
- recurrent event;
- latent construct;
- score;
- diagnostic state;
- high-dimensional feature-derived outcome.

Outcome type is one major determinant of model family.

---

# Predictor Structure

Classify predictors or exposures as:

- binary;
- categorical;
- ordinal;
- continuous;
- time-varying;
- multilevel;
- repeated;
- latent;
- high-dimensional;
- intervention assignment;
- natural exposure;
- genetic variant;
- dose;
- interaction term.

---

# Comparison Structure

Possible comparison structures:

- one sample against reference;
- two independent groups;
- two paired conditions;
- more than two independent groups;
- more than two repeated conditions;
- factorial groups;
- longitudinal groups;
- matched case-control;
- cluster-randomized groups;
- observational exposure groups.

The comparison structure should be preserved.

---

# Descriptive Statistics

Choose summaries by variable meaning.

For continuous variables consider:

- mean;
- standard deviation;
- median;
- interquartile range;
- range;
- quantiles;
- confidence intervals.

For categorical variables consider:

- count;
- proportion;
- prevalence;
- confidence intervals.

Do not choose median solely because a normality test is significant.

---

# Distribution Description

Graphical tools may include:

- histogram;
- density plot;
- boxplot;
- Q-Q plot;
- empirical cumulative distribution.

Use graphics to understand data shape.

Do not treat one omnibus normality test as the only diagnostic.

---

# Normality Guard

Do not use:

```text
Shapiro-Wilk p > 0.05 → parametric
Shapiro-Wilk p < 0.05 → nonparametric
```

as an automatic rule.

For many regression models, the relevant assumption concerns residual structure rather than raw-variable normality.

---

# Parametric vs Nonparametric

Choose based on:

- estimand;
- design;
- sample structure;
- distribution;
- robustness;
- interpretability;
- assumptions.

Nonparametric methods estimate different targets in some settings.

Do not treat them as drop-in replacements automatically.

---

# One-Sample Continuous Outcome

Potential methods include:

- one-sample t procedure;
- Wilcoxon signed-rank;
- sign-based method;
- bootstrap confidence interval.

Selection depends on:

- target;
- symmetry;
- distribution;
- sample size;
- robustness;
- reference value.

---

# Two Independent Continuous Groups

Candidate methods may include:

- independent-samples t-test;
- Welch t-test;
- Mann-Whitney / Wilcoxon rank-sum;
- robust regression;
- permutation test;
- bootstrap methods.

Prefer Welch when unequal variance is plausible and the estimand is a mean difference.

Do not use Mann-Whitney automatically as a "non-normal t-test."

---

# Paired Continuous Data

Candidate methods may include:

- paired t-test;
- Wilcoxon signed-rank;
- permutation test for paired differences;
- mixed model when repeated structure is richer.

Analyze paired differences rather than treating observations as independent.

---

# More Than Two Independent Groups

Candidate methods may include:

- one-way ANOVA;
- Welch ANOVA;
- generalized linear model;
- Kruskal-Wallis;
- robust methods;
- regression framework.

Pairwise follow-up requires multiplicity awareness.

---

# More Than Two Repeated Conditions

Candidate methods may include:

- repeated-measures ANOVA;
- linear mixed model;
- generalized mixed model;
- Friedman test;
- GEE.

Prefer models that match covariance and missingness structure when repeated measures are complex.

---

# Factorial Designs

Potential methods include:

- factorial ANOVA;
- linear model with interactions;
- generalized linear model;
- mixed-effects model.

The key scientific question is often the interaction.

Do not interpret main effects without considering interaction when interaction is substantively central.

---

# Binary Outcomes

Potential models include:

- logistic regression;
- log-binomial regression;
- Poisson regression with robust variance for risk ratios;
- exact methods;
- mixed-effects logistic regression;
- GEE;
- conditional logistic regression for matched designs.

Choose effect measure according to scientific interpretation.

---

# Odds Ratio Guard

Odds ratios are not risk ratios.

When outcomes are common, the numerical difference can be substantial.

Do not describe odds ratio as relative risk automatically.

---

# Risk Difference

Risk difference may provide direct absolute effect interpretation.

Consider identity-link binomial or appropriate alternative estimators when feasible.

---

# Risk Ratio

Use methods that estimate risk ratio directly when that is the target.

Do not force logistic regression merely because it is familiar.

---

# Count Outcomes

Possible models include:

- Poisson regression;
- negative binomial regression;
- zero-inflated models;
- hurdle models;
- quasi-Poisson;
- mixed count models.

Check:

- overdispersion;
- excess zeros;
- exposure time;
- offset.

---

# Rate Outcomes

Use offset terms when counts arise over varying observation times or populations.

---

# Ordinal Outcomes

Possible methods include:

- ordinal logistic regression;
- proportional-odds model;
- partial proportional odds;
- ordinal mixed models;
- rank-based methods.

Do not collapse ordinal outcomes into binary categories without justification.

---

# Nominal Multicategory Outcomes

Possible methods include:

- multinomial logistic regression;
- multinomial mixed models;
- classification approaches for prediction.

---

# Continuous Regression

Linear regression may be appropriate when the conditional mean model is scientifically appropriate.

Check:

- functional form;
- residual variance;
- influential observations;
- independence;
- collinearity.

Raw outcome normality is not a prerequisite.

---

# Heteroskedasticity

Potential responses include:

- robust standard errors;
- variance modeling;
- weighted models;
- transformation when scientifically meaningful.

Do not transform automatically.

---

# Nonlinearity

Potential approaches include:

- polynomial terms;
- restricted cubic splines;
- generalized additive models;
- piecewise regression;
- nonlinear models.

Prefer scientifically interpretable forms.

---

# Collinearity

Assess:

- design matrix;
- correlation;
- variance inflation;
- condition indices when useful.

Do not delete scientifically essential variables solely to lower a diagnostic statistic.

---

# Generalized Linear Models

GLMs connect:

- outcome distribution;
- link function;
- linear predictor.

Examples:

- Gaussian identity;
- binomial logit;
- Poisson log;
- Gamma log.

Choose based on outcome and estimand.

---

# Generalized Additive Models

Consider when nonlinear relationships are expected but a fully parametric functional form is uncertain.

Do not use excessive flexibility without validation.

---

# Robust Regression

May be useful when ordinary regression is unduly influenced by extreme values.

Do not use it to hide legitimate heterogeneity.

---

# Quantile Regression

Use when conditional quantiles are scientifically meaningful.

This can reveal effects beyond the conditional mean.

---

# Repeated Measures

Use methods that model within-unit dependence.

Potential families include:

- repeated-measures ANOVA;
- linear mixed models;
- generalized linear mixed models;
- GEE;
- multilevel models.

Do not run many paired tests at separate time points by default.

---

# Linear Mixed Models

Useful when:

- repeated measures;
- nested data;
- unequal numbers of observations;
- random intercepts or slopes;
- continuous outcome.

Define:

- fixed effects;
- random effects;
- covariance structure;
- time.

---

# Generalized Linear Mixed Models

Use for clustered or repeated non-Gaussian outcomes.

Examples:

- binary;
- count;
- ordinal.

---

# GEE

GEE targets population-average effects.

Mixed models often target conditional effects.

Do not treat them as interchangeable without considering estimand.

---

# Multilevel Models

Use when data have meaningful hierarchical structure.

Possible levels:

- repeated observations within persons;
- students within classes;
- patients within hospitals;
- employees within organizations.

Do not aggregate merely to avoid multilevel analysis.

---

# Random Effects

Random effects should correspond to actual grouping or repeated structure.

Do not add random effects mechanically.

---

# Random Slopes

Consider when the effect of time or exposure varies across clusters or individuals.

---

# Intraclass Correlation

ICC can describe clustering.

It does not by itself determine the full model.

---

# Cluster-Randomized Trials

Analysis should respect:

- cluster assignment;
- cluster count;
- stratification or matching;
- participant-level outcomes;
- baseline measures;
- small-number-of-cluster issues.

Do not analyze as individually randomized.

---

# Matched Data

Potential methods include:

- paired tests;
- conditional logistic regression;
- matched regression;
- mixed models.

The matching structure should be reflected.

---

# Case-Control Analysis

For unmatched case-control studies, logistic regression is common.

For matched case-control designs, conditional logistic regression may be appropriate.

Do not estimate population risk directly from ordinary case-control sampling.

---

# Cohort Analysis

Select models according to outcome:

- continuous;
- binary;
- count;
- time-to-event.

Preserve follow-up and censoring structure.

---

# Survival Analysis

Potential methods include:

- Kaplan-Meier;
- log-rank test;
- Cox proportional hazards;
- parametric survival models;
- accelerated failure-time models;
- flexible parametric models.

---

# Kaplan-Meier

Useful for descriptive survival functions.

Do not use it as the only analysis when covariate-adjusted inference is required.

---

# Cox Model

Check:

- proportional hazards;
- functional form;
- influential observations;
- time-varying covariates when relevant.

Hazard ratio is not a risk ratio.

---

# Proportional Hazards Guard

If proportional hazards fails, consider:

- time-varying effects;
- stratified Cox models;
- alternative summary measures;
- restricted mean survival time;
- parametric models.

---

# Restricted Mean Survival Time

RMST can provide an interpretable absolute survival-time contrast over a defined horizon.

---

# Competing Risks

When competing events preclude the event of interest, consider:

- cause-specific hazards;
- cumulative incidence;
- Fine-Gray-type models.

Choose according to the estimand.

---

# Recurrent Events

Potential methods include:

- Andersen-Gill;
- Prentice-Williams-Peterson;
- frailty models;
- count-based models.

Do not treat repeated events as independent first events.

---

# Longitudinal Continuous Outcomes

Possible methods include:

- mixed-effects models;
- GEE;
- growth curve models;
- latent growth models.

Choose based on inferential target and measurement structure.

---

# Change Scores vs Baseline Adjustment

Do not assume change-score analysis is always superior.

In randomized designs, baseline-adjusted outcome models can improve precision.

Choice depends on estimand and design.

---

# Difference-in-Differences

Use when:

- treatment and comparison groups exist;
- pre/post data exist;
- parallel-trends assumption is plausible.

Do not infer causality if parallel trends are unsupported.

---

# Interrupted Time Series

Requires:

- sufficient pre-intervention observations;
- sufficient post-intervention observations;
- modeled trend;
- autocorrelation;
- seasonality where relevant.

---

# Regression Discontinuity

Requires:

- assignment threshold;
- no manipulation around cutoff;
- continuity assumptions;
- appropriate bandwidth.

---

# Instrumental Variables

Use only when a credible instrument exists.

Core assumptions include:

- relevance;
- exclusion restriction;
- independence;
- monotonicity in some formulations.

Do not label a variable an instrument merely because it is correlated with exposure.

---

# Propensity Score Methods

Possible approaches include:

- matching;
- weighting;
- stratification;
- covariate adjustment.

Propensity scores address measured confounding only.

---

# Inverse Probability Weighting

Use when weighting targets a clearly defined population estimand.

Check:

- positivity;
- extreme weights;
- model specification.

---

# Doubly Robust Methods

May combine outcome and treatment models.

"Double robust" does not mean immune to all misspecification.

---

# Causal Inference Guard

Statistical adjustment cannot create causality from an invalid design.

Causal interpretation requires:

- explicit treatment / exposure;
- comparator;
- temporal order;
- causal assumptions;
- confounder strategy;
- estimand.

---

# Mediation Analysis

Potential methods include:

- regression-based mediation;
- counterfactual mediation;
- SEM-based mediation;
- longitudinal mediation.

Causal mediation requires stronger assumptions than association-based indirect effects.

---

# Moderation Analysis

Moderation is generally assessed through interaction terms.

Do not define moderation from separate subgroup significance tests.

---

# Interaction Interpretation

Interpret interactions on the scale of the model.

Additive and multiplicative interactions are different.

---

# Subgroup Analysis

Subgroup inference should use interaction or heterogeneity tests where appropriate.

Do not conclude subgroups differ because one subgroup has p < .05 and another does not.

---

# Prediction Modeling

Potential methods include:

- logistic regression;
- penalized regression;
- random forests;
- gradient boosting;
- support vector machines;
- neural networks;
- survival prediction models.

Method choice should follow:

- sample size;
- feature dimension;
- nonlinearity;
- interpretability;
- validation;
- clinical or practical use.

---

# Prediction Validation

Use:

- internal validation;
- bootstrap;
- cross-validation;
- external validation;
- temporal validation;
- geographic validation.

Do not report training performance as final model performance.

---

# Data Split Guard

Simple train/test splitting may waste data in small samples.

Consider resampling approaches.

---

# Cross-Validation Guard

Preserve:

- clusters;
- repeated observations;
- time order;
- participant IDs.

Prevent leakage.

---

# Calibration

For prediction, evaluate whether predicted probabilities agree with observed outcomes.

Possible measures include:

- calibration plot;
- calibration intercept;
- calibration slope;
- Brier score.

---

# Discrimination

Possible metrics include:

- ROC AUC;
- C-statistic;
- precision-recall measures.

Discrimination alone is insufficient.

---

# Clinical Utility

Prediction models may require decision-curve or utility analysis when clinical decisions are intended.

---

# Machine Learning Guard

Do not choose machine learning because it appears more advanced.

Prefer the simplest method that achieves the predictive objective adequately.

---

# Penalized Regression

Potential methods include:

- ridge;
- lasso;
- elastic net.

Useful for shrinkage and high-dimensional prediction.

Do not interpret variable selection from lasso as causal evidence.

---

# High-Dimensional Data

When predictors approach or exceed sample size, ordinary regression may be unstable.

Consider:

- regularization;
- dimension reduction;
- validation;
- strong multiplicity control.

---

# Principal Component Analysis

PCA is a dimension-reduction technique.

It is not a latent-variable measurement model by itself.

---

# Exploratory Factor Analysis

Use when the latent structure is not fully specified.

Consider:

- factorability;
- extraction method;
- rotation;
- number of factors;
- ordinal indicators.

---

# Confirmatory Factor Analysis

Use when a measurement model is prespecified.

Evaluate:

- identification;
- factor loadings;
- residual structure;
- global fit;
- local fit;
- theory.

---

# EFA vs CFA Guard

Do not perform EFA and then report the same-data CFA as fully independent confirmation.

Use split samples or external validation where feasible.

---

# Reliability Analysis

Select reliability methods according to measurement design.

Possible methods:

- Cronbach alpha;
- McDonald's omega;
- ICC;
- kappa;
- test-retest correlation;
- generalizability theory.

---

# Cronbach Alpha Guard

Alpha assumes a particular measurement structure.

Do not use alpha alone to establish reliability or validity.

---

# Inter-Rater Agreement

Potential measures include:

- Cohen kappa;
- weighted kappa;
- Fleiss kappa;
- ICC;
- agreement percentage;
- Krippendorff alpha.

Select according to:

- number of raters;
- scale type;
- design.

---

# Agreement vs Association

Correlation is not agreement.

For continuous-method comparison consider:

- Bland-Altman;
- concordance measures;
- measurement-error models.

---

# Diagnostic Accuracy

Potential methods include:

- sensitivity;
- specificity;
- predictive values;
- likelihood ratios;
- ROC analysis;
- calibration;
- diagnostic regression.

---

# Sensitivity / Specificity

Estimate with uncertainty.

Do not report only point estimates.

---

# Predictive Values

PPV and NPV depend on prevalence.

Do not transport them across populations without context.

---

# ROC AUC Guard

AUC does not tell the full story.

It does not measure calibration.

---

# Threshold Selection

Thresholds should follow:

- clinical purpose;
- cost of errors;
- prespecified use;
- decision analysis.

Do not choose a threshold solely to maximize sample-specific accuracy.

---

# Validation Studies

Validation may require:

- discrimination;
- calibration;
- agreement;
- construct validity;
- criterion validity;
- reliability;
- invariance.

The statistical method depends on what is being validated.

---

# Measurement Invariance

For latent constructs across groups or time, possible steps include:

- configural;
- metric;
- scalar;
- strict.

Selection depends on the comparison goal.

---

# SEM Readiness Gate

Consider SEM when:

- latent constructs are central;
- measurement error matters;
- structural relations are theory-driven;
- multiple simultaneous relations are required;
- sample and identification are adequate.

Do not use SEM merely because a path diagram is visually attractive.

---

# Covariance-Based SEM

May be appropriate when the goal includes:

- theory testing;
- latent-variable covariance structure;
- global model fit;
- parameter inference.

Assess:

- identification;
- estimator;
- measurement level;
- sample adequacy;
- model fit;
- residuals;
- modification indices cautiously.

---

# PLS-SEM Readiness Gate

Consider PLS-SEM only when the analysis goal and construct architecture justify component-based structural modeling.

Potential contexts may include:

- prediction-oriented structural modeling;
- complex composite models;
- formative measurement;
- exploratory theory extension where justified.

Do not select PLS-SEM solely due to:

- small sample;
- non-normality;
- many indicators;
- SmartPLS availability;
- thesis tradition.

---

# PLS-SEM Measurement Model

For reflective constructs consider:

- indicator reliability;
- internal consistency;
- convergent validity;
- discriminant validity.

For formative constructs consider:

- collinearity;
- indicator weights;
- indicator relevance.

Do not apply reflective criteria mechanically to formative constructs.

---

# PLS-SEM Structural Model

Potential elements include:

- path coefficients;
- uncertainty;
- R²;
- f²;
- predictive relevance;
- collinearity;
- prediction assessment.

Do not interpret R² as causal proof.

---

# HTMT

HTMT may support discriminant-validity assessment.

Do not use one threshold mechanically without context.

---

# Bootstrapping in PLS-SEM

Bootstrapping provides uncertainty for estimates.

It does not correct poor design or invalid measurement.

---

# PLS-SEM Sample Size Guard

Do not use the 10-times rule as the sole justification.

Use stronger planning methods based on:

- target effect;
- model structure;
- power;
- simulation;
- inverse square root;
- gamma-exponential approaches when appropriate.

---

# SEM / PLS-SEM Comparison

Select according to:

- construct type;
- theoretical maturity;
- measurement structure;
- prediction objective;
- inferential objective;
- model fit needs;
- estimator properties.

Do not frame the decision as a contest of prestige.

---

# Path Analysis

Path analysis models observed variables.

Do not call it latent-variable SEM when no latent variables exist.

---

# Structural Regression

Observed-variable structural models may often be fit using regression or path analysis.

Do not add latent-variable machinery without need.

---

# Partial Correlation

Partial correlation estimates association after controlling selected variables.

It is not automatically a causal effect.

---

# Correlation Selection

Possible measures:

- Pearson;
- Spearman;
- Kendall.

Choose according to:

- relationship form;
- scale;
- robustness;
- ties;
- scientific target.

---

# Pearson Correlation

Targets linear association.

Do not use it to prove agreement or causation.

---

# Spearman Correlation

Targets monotonic rank association.

It does not estimate the same quantity as Pearson correlation.

---

# Binary Association

Possible measures include:

- phi;
- odds ratio;
- risk ratio;
- risk difference.

Choose according to inference.

---

# Categorical Association

Potential methods include:

- chi-square;
- Fisher exact;
- multinomial models;
- log-linear models.

---

# Chi-Square Guard

Expected cell counts matter.

Use exact or alternative methods for sparse data.

---

# Multiple Response Data

Do not treat multiple-response categories as mutually exclusive ordinary categorical variables.

---

# Repeated Categorical Data

Potential methods include:

- McNemar;
- Cochran Q;
- GEE;
- mixed logistic models.

---

# Ordinal Paired Data

Potential methods include:

- Wilcoxon signed-rank;
- ordinal mixed models;
- cumulative-link models.

---

# Dose-Response Analysis

Potential methods include:

- trend test;
- regression;
- nonlinear dose-response;
- Emax-type models;
- spline models.

Do not reduce ordered exposure to many pairwise tests.

---

# Pharmacokinetic Analysis

Possible method families include:

- noncompartmental analysis;
- compartmental modeling;
- population PK;
- nonlinear mixed effects.

Selection depends on:

- sampling design;
- parameter target;
- population;
- sparse vs rich sampling.

---

# Population PK

May require nonlinear mixed-effects modeling.

Do not use ordinary regression to estimate full PK structure when the design requires population PK modeling.

---

# Pharmacogenetic Analysis

Potential methods include:

- genotype-based regression;
- allele-based tests;
- dominant / recessive / additive genetic models;
- haplotype analysis;
- survival models;
- mixed models.

Account for:

- ancestry;
- population stratification;
- multiple testing;
- rare genotype counts;
- treatment exposure.

---

# Hardy-Weinberg Equilibrium

HWE can be a quality-control or population-genetic check.

Do not use it as proof of no genotyping error.

---

# Multiple Genetic Models Guard

Testing additive, dominant, recessive, and genotypic models creates multiplicity.

Predefine scientifically plausible coding when possible.

---

# Omics Analysis

Potential families include:

- differential expression;
- penalized models;
- dimension reduction;
- pathway analysis;
- clustering;
- network analysis.

Multiplicity and validation are central.

---

# Batch Effect Adjustment

Account for assay or processing batches when they could confound biology.

Do not adjust away true biological variation blindly.

---

# Spatial Analysis

Potential methods include:

- spatial regression;
- geostatistics;
- spatial autocorrelation;
- mixed models with spatial structure.

---

# Time-Series Analysis

Potential methods include:

- ARIMA;
- state-space models;
- interrupted time series;
- dynamic regression;
- generalized time-series models.

Preserve temporal ordering.

---

# Autocorrelation

Do not apply ordinary independent-observation regression when strong serial correlation exists.

---

# Bayesian Methods

Bayesian methods may be selected when:

- prior information is scientifically meaningful;
- probability statements about parameters are desired;
- hierarchical structure is complex;
- small-sample regularization is useful.

Plan prior sensitivity.

---

# Bayesian Model Checking

Use:

- prior predictive checks;
- posterior predictive checks;
- convergence diagnostics;
- sensitivity analyses.

---

# Exact Methods

Exact methods may be appropriate for sparse small samples.

Do not assume exact methods solve poor design.

---

# Permutation Methods

Useful when exchangeability assumptions are appropriate.

Respect:

- pairing;
- clustering;
- randomization scheme.

---

# Bootstrap Methods

Bootstrap can estimate uncertainty under suitable resampling units.

Resample the true independent unit.

Do not bootstrap technical replicates as independent biological units.

---

# Robust Standard Errors

Robust standard errors may address heteroskedasticity or clustering under appropriate conditions.

They do not correct model misspecification universally.

---

# Small-Sample Corrections

For few clusters or small samples, standard asymptotic approximations may be poor.

Consider:

- small-sample degrees-of-freedom corrections;
- exact methods;
- bootstrap;
- permutation;
- Bayesian methods;
- simpler models.

---

# Missing Data Method Selection

Possible methods include:

- complete-case;
- multiple imputation;
- maximum likelihood;
- inverse probability weighting;
- Bayesian modeling.

Choice should reflect:

- missingness mechanism;
- analysis model;
- variable types;
- design;
- auxiliary information.

---

# Multiple Imputation

Ensure imputation model includes:

- outcomes;
- exposures;
- important covariates;
- predictors of missingness;
- design variables.

Respect multilevel and longitudinal structure when needed.

---

# Complete-Case Guard

Complete-case analysis can be biased even with modest missingness.

Do not select based on convenience alone.

---

# Sensitivity to MNAR

When missing-not-at-random is plausible, consider sensitivity analyses.

---

# Multiplicity

Possible methods include:

- Bonferroni;
- Holm;
- Hochberg;
- false discovery rate;
- hierarchical testing;
- gatekeeping.

Select based on the inferential family.

---

# FDR

Often relevant in high-dimensional exploratory testing.

Do not interpret FDR-controlled discoveries as individually definitive confirmations.

---

# Family-Wise Error

May be relevant for confirmatory multiple hypotheses.

---

# Effect Size and Confidence Interval

Plan both.

Do not use standardized effect sizes when raw-scale effects are more clinically interpretable unless standardization serves a purpose.

---

# Standardized Mean Difference

Useful when studies or scales differ.

Within a single study, raw-scale differences may be more interpretable.

---

# Confidence Interval Interpretation

A confidence interval is not a probability interval for the parameter under ordinary frequentist interpretation.

---

# p-Value Reporting

Prefer exact p-values when practical.

Avoid:

- p = 0.000;
- "highly significant" without effect context.

---

# Scientific Importance

Always separate:

- statistical evidence;
- effect magnitude;
- uncertainty;
- practical importance;
- clinical importance.

---

# Model Diagnostics

Select diagnostics according to model.

Examples:

## Linear model
- residual plots;
- functional form;
- heteroskedasticity;
- leverage;
- influence.

## Logistic model
- calibration;
- residuals;
- separation;
- influential points.

## Cox model
- proportional hazards;
- functional form;
- influential cases.

## Mixed model
- random-effect structure;
- residuals;
- convergence.

---

# Convergence

Do not interpret a model that failed to converge.

---

# Separation in Logistic Regression

Complete or quasi-separation may require:

- penalized likelihood;
- exact methods;
- Bayesian regularization.

---

# Sparse Data Bias

Sparse outcomes can bias ordinary maximum-likelihood estimates.

Consider appropriate small-sample methods.

---

# Overfitting

Prevent through:

- parsimonious modeling;
- shrinkage;
- validation;
- prespecified predictors;
- adequate sample.

---

# Stepwise Selection Guard

Do not use automatic stepwise selection as the default inferential strategy.

---

# Univariate Screening Guard

Do not select multivariable covariates solely because univariate p < 0.05.

---

# Confounder Selection

Use:

- causal knowledge;
- prior evidence;
- design;
- DAGs;
- substantive importance.

---

# Covariate Adjustment in Randomized Trials

Adjustment for strong prognostic baseline covariates can improve precision.

Do not choose covariates after inspecting treatment effects.

---

# Baseline Balance Tests Guard

Do not use significance tests of baseline characteristics to decide whether randomization succeeded.

---

# Model Comparison

Potential tools include:

- likelihood ratio tests;
- information criteria;
- cross-validation;
- predictive performance;
- substantive interpretability.

Use only when candidate models target compatible scientific questions.

---

# AIC / BIC Guard

Information criteria compare models under assumptions.

They do not prove scientific truth.

---

# Goodness-of-Fit

Fit metrics are not substitutes for scientific validity.

---

# Sensitivity Analysis Selection

Choose sensitivity analyses that challenge important assumptions.

Examples:

- alternative confounder sets;
- alternative outcome definitions;
- alternative missing-data assumptions;
- alternative time windows;
- robust estimators;
- exclusion of influential points;
- per-protocol vs intention-to-treat.

---

# Robustness Check Guard

Do not run dozens of models until significance appears.

---

# Subgroup Interaction

Use explicit interaction terms or hierarchical models when appropriate.

---

# Multiplicity in Subgroups

Subgroup analyses multiply false-positive opportunities.

Treat exploratory subgroup findings cautiously.

---

# Equivalence Testing

Potential methods include:

- two one-sided tests;
- confidence-interval approach.

Requires a prespecified equivalence margin.

---

# Noninferiority Testing

Requires:

- margin;
- comparator;
- analysis population;
- design integrity.

---

# Superiority Testing

Do not switch from failed noninferiority to superiority post hoc without transparent labeling.

---

# Agreement Analysis

Continuous agreement may use:

- Bland-Altman;
- concordance correlation;
- ICC.

Categorical agreement may use:

- kappa family.

---

# Measurement Error Models

Consider when predictor measurement error is substantial and relevant to inference.

---

# Calibration Models

Use for method comparison or prediction when calibration is the target.

---

# Optimization Studies

Potential methods include:

- response surface methodology;
- factorial design analysis;
- desirability functions;
- nonlinear optimization.

Do not optimize before defining meaningful responses.

---

# Design of Experiments

For experimental-factor studies consider:

- factorial designs;
- fractional factorial;
- central composite;
- Box-Behnken;
- mixture designs.

Selection depends on factor structure and scientific objective.

---

# Mixture Designs

Use when component proportions sum to a fixed total.

Ordinary factorial designs may be inappropriate.

---

# Formulation Optimization

Potential methods include:

- response surface;
- mixture design;
- desirability analysis;
- confirmation runs.

Do not claim optimality without validation.

---

# Stability Analysis

Potential methods include:

- repeated-measures models;
- regression over time;
- degradation modeling;
- survival-like shelf-life estimation.

Follow domain standards when relevant.

---

# Microbiology Analysis

For zone measurements consider:

- independent batch structure;
- control groups;
- concentration trend;
- repeated plates;
- net vs total zone definition.

Do not treat multiple technical plate readings as independent biological observations.

---

# MIC / MBC

MIC and MBC are often interval or ordinal-like dilution endpoints.

Analyze with methods appropriate to dilution structure and replicate design.

---

# Quality Control Data

QC replicates are not always part of the inferential sample.

Distinguish analytical QC from biological evidence.

---

# Software Selection

Select software after method selection.

Possible software includes:

- Jamovi;
- R;
- Stata;
- SPSS;
- SAS;
- Python;
- JASP;
- Mplus;
- AMOS;
- SmartPLS;
- specialized PK software.

Software should implement the chosen method correctly.

---

# Jamovi Compatibility

If the user requires Jamovi-first analysis:

1. select the scientifically correct method first;
2. identify whether Jamovi or an installed module supports it;
3. use menu-based execution where available;
4. use Rj only when the required method is unavailable through menus/modules;
5. do not replace the scientific method merely because a menu is missing.

---

# SmartPLS Compatibility

Use SmartPLS only when PLS-SEM is scientifically justified.

Do not route all latent-variable studies automatically to SmartPLS.

---

# SPSS Compatibility

SPSS can implement many classical methods.

Its menu structure should not define the scientific model.

---

# R Compatibility

R supports broad methods and reproducible workflows.

Do not select R merely because another tool lacks a menu if the user explicitly requires menu-first workflow and an appropriate GUI module exists.

---

# Method Selection Matrix

When useful:

| Scientific Target | Outcome | Design | Dependency | Candidate Method | Key Assumption |
|---|---|---|---|---|---|

---

# Candidate Method Record

For each candidate:

```yaml
candidate_method:
  name:
  estimand:
  outcome_type:
  design_fit:
  dependency_fit:
  assumptions:
  effect_measure:
  uncertainty:
  strengths:
  limitations:
  software:
```

---

# Method Comparison

Compare candidates on:

- estimand alignment;
- design alignment;
- outcome compatibility;
- dependency handling;
- assumptions;
- robustness;
- interpretability;
- sample adequacy;
- software availability;
- reproducibility.

Scientific alignment has priority.

---

# Method Status

Use:

- `PREFERRED_STATISTICAL_METHOD`
- `VALID_ALTERNATIVE_METHOD`
- `ROBUSTNESS_METHOD`
- `SENSITIVITY_METHOD`
- `EXPLORATORY_METHOD`
- `METHOD_NOT_YET_SELECTABLE`

---

# Statistical Method Passport

Recommended internal structure:

```yaml
statistical_method:
  status:
  rq:
  estimand:
  analysis_population:
  outcome:
  exposure_or_intervention:
  comparator:
  unit:
  design:
  sampling_structure:
  clustering:
  repeated_measures:
  time_structure:
  candidate_methods:
  selected_method:
  effect_measure:
  uncertainty_measure:
  assumptions:
  diagnostics:
  missing_data_method:
  multiplicity_method:
  sensitivity_methods:
  software:
  reporting:
```

---

# Minimal Output

For a simple request provide:

## Analysis Target
[...]

## Recommended Method
[...]

## Why It Fits
[...]

## Effect Measure
[...]

## Key Assumptions
[...]

## Diagnostics
[...]

## Alternative / Sensitivity Method
[...]

## Software
[...]

---

# Comprehensive Output

When full statistical method selection is requested:

## A. Research Question
[...]

## B. Estimand
[...]

## C. Study Design
[...]

## D. Outcome Type
[...]

## E. Predictor / Exposure Structure
[...]

## F. Dependency Structure
[...]

## G. Candidate Methods
[...]

## H. Preferred Method
[...]

## I. Effect Measure
[...]

## J. Uncertainty
[...]

## K. Assumptions
[...]

## L. Diagnostics
[...]

## M. Missing Data
[...]

## N. Multiplicity
[...]

## O. Interaction / Subgroups
[...]

## P. Sensitivity Analyses
[...]

## Q. Software
[...]

## R. Reporting
[...]

---

# Relationship with Analysis Planner

`analysis-planner` defines the analytical problem.

`statistical-method-selector` chooses the quantitative statistical method.

Use:

```text
analysis-planner
      ↓
statistical-method-selector
```

Do not reverse this relationship.

---

# Relationship with Methodology Architect

Method selection must respect the data-generating design.

A statistical model cannot repair fundamental design invalidity.

---

# Relationship with Sampling Strategy

The method must account for:

- clustering;
- stratification;
- weighting;
- pairing;
- repeated units;
- event structure.

---

# Relationship with Instrument Design

The method must respect:

- measurement scale;
- score construction;
- reliability;
- validity;
- latent structure;
- detection limits.

---

# Relationship with Hypothesis Builder

Confirmatory hypotheses should map to a method capable of estimating the corresponding target.

---

# Relationship with Conceptual Framework

Structural relationships must not be modeled merely because arrows exist.

The analysis should reflect scientifically justified relationships.

---

# Relationship with Qualitative Analysis

Do not route qualitative RQs here merely because some coding frequencies exist.

---

# Relationship with Mixed-Method Analysis

Quantitative strand methods may be selected here, but cross-strand integration belongs to `mixed-method-analysis`.

---

# Relationship with Meta-Analysis

Primary-study statistics and meta-analysis are different levels of inference.

Route evidence pooling to `meta-analysis`.

---

# Relationship with Result Interpreter

Statistical output is passed downstream for scientific interpretation.

Do not conflate method selection with conclusion writing.

---

# User-Friendly Behavior

Prefer:

> Your outcome is binary, the study is a prospective cohort, and the scientific target is a risk ratio. Logistic regression is not the only option; a log-binomial model or robust Poisson approach may align more directly with the estimand.

Or:

> These are repeated measurements from the same participants, so the observations are not independent. A mixed model or GEE is more appropriate than separate t-tests at each time point.

Or:

> Your model contains latent constructs, but that alone does not justify PLS-SEM. We should first decide whether the goal is covariance-based theory testing, prediction-oriented component modeling, or an observed-variable regression model.

---

# Avoid These Behaviors

Do not:

- select a method from normality alone;
- select PLS-SEM because sample size is small;
- select SEM because there are many variables;
- use odds ratio and call it risk ratio;
- treat repeated observations as independent;
- ignore cluster randomization;
- ignore sampling weights;
- use stepwise selection as the default;
- choose confounders by univariate p-values;
- remove outliers to obtain significance;
- use subgroup significance differences as interaction evidence;
- infer equivalence from non-significance;
- report training prediction performance as validation;
- use correlation to claim agreement;
- claim mediation proves mechanism without causal logic;
- use fit indices as proof of theory;
- use Cronbach alpha as proof of validity;
- use the PLS-SEM 10-times rule as the sole sample-size basis;
- allow software availability to determine the scientific method;
- use advanced methods merely for publication appearance.

---

# Stop Conditions

Do not classify a statistical method as selected when:

- estimand is unclear;
- outcome type is unknown;
- design is unstable;
- unit of analysis is undefined;
- clustering or repeated measures are ignored;
- causal interpretation lacks identification logic;
- prediction lacks validation architecture;
- measurement structure is unresolved;
- missing-data handling is impossible to specify;
- multiplicity materially affects confirmatory inference but is ignored;
- candidate methods target different scientific quantities and the target has not been chosen;
- software preference is driving the decision.

Use:

- `RETURN_TO_ANALYSIS_PLANNER`
- `RETURN_TO_METHODOLOGY_ARCHITECT`
- `RETURN_TO_SAMPLING_STRATEGY`
- `RETURN_TO_INSTRUMENT_DESIGN`
- `STATISTICAL_METHOD_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`statistical-method-selector` succeeds when a completed quantitative analysis architecture has been translated into a scientifically justified statistical method choice that explicitly matches the estimand, study design, outcome distribution, predictor or exposure structure, unit and dependency structure, sampling design, repeated measures, timing, measurement properties, causal or predictive goal, missing-data context, multiplicity, effect measure, uncertainty reporting, assumptions, diagnostics, sensitivity analyses, and software implementation, while clearly distinguishing preferred, alternative, robustness, and exploratory methods and preventing normality tests, p-value chasing, arbitrary sample-size rules, software menus, methodological fashion, or publication strategy from determining the analysis.
