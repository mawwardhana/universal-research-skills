---
name: result-interpreter
description: Interpret completed research results into scientifically defensible findings after the analysis strategy and study design are sufficiently clear. Use when quantitative, qualitative, mixed-method, meta-analytic, experimental, predictive, diagnostic, validation, SEM, PLS-SEM, longitudinal, multilevel, survival, pharmacokinetic, pharmacogenetic, or other analytical outputs already exist and the researcher needs to determine what the results actually mean, how strong and uncertain the evidence is, which claims are supported or unsupported, how findings relate to hypotheses, theory, mechanisms, design boundaries, robustness, contradictions, and practical importance, and what must be carried forward into scientific discussion without allowing p-values, software labels, significance alone, or post-hoc storytelling to redefine the scientific conclusion.
---

# Result Interpreter

## Purpose

`result-interpreter` converts completed analytical outputs into scientifically defensible findings.

Its central question is:

> What do these results actually support, how strongly do they support it, under which assumptions and boundaries, what remains uncertain or contradicted, and which claims must not be made?

This skill operates after an analysis has been completed or sufficiently summarized.

It does not perform the primary analysis.

It does not replace:

- `analysis-planner`;
- `statistical-method-selector`;
- `qualitative-analysis`;
- `mixed-method-analysis`;
- `meta-analysis`.

It interprets their outputs.

---

# Core Principle

Use:

> Results are evidence, not conclusions by themselves.

A result must be interpreted through:

```text
Research Question
      ↓
Intended Inference
      ↓
Study Design
      ↓
Analysis Target / Estimand
      ↓
Observed Result
      ↓
Effect / Pattern / Mechanism
      ↓
Uncertainty
      ↓
Robustness
      ↓
Design Boundaries
      ↓
Scientifically Defensible Claim
```

Do not reverse this sequence.

---

# Position in the Framework

Preferred architecture:

```text
analysis-planner
      ↓
appropriate analysis
      ↓
result-interpreter
      ↓
scientific-discussion
      ↓
implication-builder
```

For mixed methods:

```text
quantitative result
      +
qualitative finding
      ↓
mixed-method-analysis
      ↓
meta-inference
      ↓
result-interpreter
```

For meta-analysis:

```text
meta-analysis
      ↓
pooled / non-pooled evidence
      ↓
result-interpreter
```

---

# Required Upstream Context

Use established information from:

- `research-question-builder`;
- `hypothesis-builder`;
- `theoretical-framework`;
- `conceptual-framework`;
- `problem-solving-approach`;
- `methodology-architect`;
- `analysis-planner`;
- `statistical-method-selector`;
- `qualitative-analysis`;
- `mixed-method-analysis`;
- `meta-analysis`;
- `instrument-design`;
- `sampling-strategy`;
- `protocol-builder`.

Minimum useful context may include:

- research question;
- hypothesis where applicable;
- study design;
- population;
- sampling structure;
- outcome;
- exposure, intervention, predictor, or phenomenon;
- comparator;
- effect measure;
- analysis method;
- estimates;
- confidence or credible intervals;
- p-values when available;
- model diagnostics;
- qualitative themes or categories;
- mixed-method meta-inferences;
- meta-analytic heterogeneity and prediction intervals;
- prespecified vs exploratory status;
- sensitivity analyses;
- missing-data handling;
- multiplicity;
- risk of bias;
- protocol deviations.

Do not ask the researcher to repeat information already established.

---

# Readiness Gate

Classify:

- `READY_FOR_INTERPRETATION`
- `RESULTS_INCOMPLETE`
- `ANALYSIS_METHOD_UNCLEAR`
- `STUDY_DESIGN_UNCLEAR`
- `ESTIMAND_UNCLEAR`
- `OUTPUT_WITHOUT_CONTEXT`
- `ROBUSTNESS_NOT_ASSESSED`
- `INTERPRETATION_ALREADY_ESTABLISHED`
- `RESULT_INTERPRETATION_REQUIRES_REASSESSMENT`

Do not interpret software output in isolation.

---

# Interpretation Unit

Before interpreting, define what the result refers to.

Possible units include:

- coefficient;
- mean difference;
- standardized mean difference;
- odds ratio;
- risk ratio;
- hazard ratio;
- correlation;
- indirect effect;
- interaction effect;
- factor loading;
- path coefficient;
- model fit;
- prediction metric;
- diagnostic metric;
- survival estimate;
- qualitative theme;
- mechanism;
- case pattern;
- meta-inference;
- pooled effect;
- heterogeneity estimate;
- prediction interval;
- pharmacokinetic parameter;
- pharmacogenetic association.

---

# Research-Question Alignment

Every interpretation should map back to the research question.

Use:

```yaml
result_alignment:
  research_question:
  analysis_target:
  observed_result:
  supports_answer:
  unsupported_elements:
  uncertainty:
```

Do not interpret results unrelated to the research question as if they were primary findings.

---

# Primary vs Secondary Findings

Classify:

- `PRIMARY_PRESPECIFIED`
- `SECONDARY_PRESPECIFIED`
- `EXPLORATORY`
- `POST_HOC`
- `INCIDENTAL`

Interpretive strength should differ across these categories.

---

# Confirmatory vs Exploratory Interpretation

Confirmatory results require:

- prespecified hypothesis;
- prespecified outcome;
- prespecified model or defensible analysis plan;
- controlled multiplicity where relevant.

Exploratory results may generate:

- candidate explanations;
- hypotheses;
- mechanisms;
- future study directions.

Do not present exploratory findings as confirmed evidence.

---

# Hypothesis Alignment

If a hypothesis exists, classify:

- `SUPPORTED`
- `PARTIALLY_SUPPORTED`
- `NOT_SUPPORTED`
- `CONTRADICTED`
- `INCONCLUSIVE`
- `NOT_TESTED_AS_SPECIFIED`

Do not equate:

`p > 0.05`

with:

`hypothesis disproven`.

---

# Null Hypothesis Guard

A non-significant result does not establish equivalence or no effect unless the design and analysis support such inference.

Possible interpretations include:

- insufficient evidence;
- imprecision;
- low power;
- small effect;
- model uncertainty;
- true absence of meaningful effect.

---

# Evidence Against Null

A small p-value indicates incompatibility with a statistical null under model assumptions.

It does not directly measure:

- effect magnitude;
- practical importance;
- probability the hypothesis is true;
- replication probability;
- causal validity.

---

# Effect Magnitude First

Interpret:

1. direction;
2. magnitude;
3. uncertainty;
4. practical or clinical relevance;
5. statistical evidence.

Do not lead with significance alone.

---

# Quantitative Interpretation Core

For quantitative results, use:

```text
Estimate
   ↓
Direction
   ↓
Magnitude
   ↓
Uncertainty
   ↓
Practical Meaning
   ↓
Robustness
   ↓
Design-Limited Claim
```

---

# Direction

Classify:

- positive;
- negative;
- null-like;
- nonlinear;
- threshold;
- heterogeneous;
- time-varying;
- context-dependent.

Direction alone is insufficient.

---

# Magnitude

Assess magnitude using scientifically meaningful scale.

Possible approaches:

- raw units;
- standardized units;
- relative risk;
- absolute risk;
- probability change;
- time ratio;
- rate ratio;
- hazard ratio;
- variance explained;
- predictive gain.

Prefer interpretable scale when possible.

---

# Raw Effects

Raw effects are often most interpretable when measurement scales are meaningful.

Example:

> Mean systolic blood pressure was 7.4 mmHg lower.

This is often more informative than a standardized effect alone.

---

# Standardized Effects

Interpret standardized effects with caution.

Avoid universal labels such as:

- small;
- medium;
- large;

unless domain-specific benchmarks justify them.

---

# Effect Size Benchmark Guard

Generic thresholds such as:

- 0.2;
- 0.5;
- 0.8;

must not replace domain-specific meaning.

---

# Absolute vs Relative Effects

Relative effects may appear large while absolute effects are small.

Where possible report both.

Example:

```text
Relative risk reduction: 50%
Absolute risk reduction: 2%
```

Interpretation should reflect both.

---

# Confidence Interval

A confidence interval reflects uncertainty around the estimate under repeated-sampling logic and model assumptions.

Interpret:

- width;
- direction compatibility;
- clinically meaningful values;
- null compatibility;
- extreme plausible values.

---

# Confidence Interval Guard

Do not interpret a 95% confidence interval as:

> There is a 95% probability the true value lies inside this interval.

unless using an appropriate Bayesian credible interval.

---

# Credible Interval

For Bayesian analyses, a credible interval may support probability statements about parameter values conditional on the model and prior.

State assumptions.

---

# Interval Width

Wide intervals may indicate:

- small sample;
- high variability;
- sparse events;
- weak identification;
- unstable model.

Do not treat imprecise estimates as definitive.

---

# Compatibility Interpretation

Prefer:

> The data are compatible with effects ranging from X to Y under the specified model.

This often communicates uncertainty better than significance labels.

---

# Statistical Significance Guard

Do not write:

> X has an effect because p < 0.05.

Prefer:

> The estimated effect was X, with uncertainty interval Y–Z; the result was inconsistent with the null under the specified model.

Then interpret scientific meaning.

---

# Non-Significance Guard

Do not write:

> There was no effect because p > 0.05.

Prefer:

> The estimate was imprecise and remained compatible with both negligible and potentially meaningful effects.

when appropriate.

---

# Practical Significance

Assess whether the observed magnitude matters for:

- patients;
- learners;
- organizations;
- policy;
- engineering performance;
- biological function;
- formulation quality;
- implementation.

Do not infer practical importance from statistical significance alone.

---

# Minimal Clinically Important Difference

When a validated threshold exists, compare the confidence interval with that threshold.

Possible categories:

- clearly exceeds;
- may exceed;
- clearly below;
- uncertain.

---

# Equivalence

Equivalence requires prespecified equivalence margins and appropriate analysis.

Do not infer equivalence from non-significance.

---

# Noninferiority

Noninferiority requires:

- prespecified margin;
- direction;
- appropriate confidence interval;
- design integrity.

Do not infer from a conventional null-hypothesis test.

---

# Superiority

Superiority is distinct from noninferiority.

Do not conflate them.

---

# Correlation

A correlation describes association strength and direction.

Do not infer:

- causation;
- mechanism;
- intervention effect;

from correlation alone.

---

# Regression Coefficients

Interpret coefficients conditional on the model.

Record:

- outcome scale;
- predictor scale;
- adjustment variables;
- interaction terms;
- transformations.

---

# Adjusted Effects

An adjusted coefficient estimates a conditional relationship given covariates.

Do not call it "controlled" in a causal sense unless the confounding strategy is defensible.

---

# Odds Ratio

Interpret odds ratio as odds, not risk.

Avoid:

> 2 times more likely

unless approximation to risk ratio is justified.

---

# Risk Ratio

Risk ratio is directly interpretable as relative risk.

Complement with absolute risk where possible.

---

# Risk Difference

Risk difference expresses absolute probability change.

Often important for decision-making.

---

# Hazard Ratio

A hazard ratio compares instantaneous event rates under model assumptions.

Do not interpret as:

> participants lived X times longer.

---

# Incidence Rate Ratio

Interpret using person-time rates.

---

# Time-to-Event Results

Consider:

- median survival;
- cumulative incidence;
- hazard ratio;
- proportional-hazards assumption;
- competing risks;
- censoring.

---

# Proportional Hazards Guard

If proportional hazards are violated, a single hazard ratio may be misleading.

Consider time-varying interpretation.

---

# Repeated Measures

Interpret:

- within-person change;
- between-group difference;
- time effect;
- group × time interaction.

Do not interpret repeated observations as independent.

---

# Interaction

An interaction indicates that an effect differs across another variable.

Interpret the interaction itself.

Do not infer interaction because:

- one subgroup is significant;
- another subgroup is not.

---

# Moderator

A moderator changes the strength or direction of a relationship.

Require evidence from an interaction or equivalent model.

---

# Mediation

Mediation interpretation requires:

- temporal or causal logic;
- indirect effect;
- assumptions;
- confounding considerations.

Do not infer mechanism solely from a significant indirect effect.

---

# Indirect Effect

Interpret the indirect effect directly.

Do not require every component path to be individually significant under outdated stepwise rules.

---

# Total and Direct Effects

Distinguish:

- total effect;
- direct effect;
- indirect effect.

Do not interpret direct effect as "effect after removing mediation" without care.

---

# Suppression

If direct and total effects differ in sign or magnitude, investigate suppression or inconsistent mediation.

---

# Nonlinear Effects

Interpret the shape:

- U-shaped;
- inverted U;
- threshold;
- saturation;
- plateau;
- exponential.

Do not summarize nonlinear relationships with one linear coefficient.

---

# Dose-Response

Describe:

- monotonicity;
- threshold;
- plateau;
- toxicity;
- optimal range.

---

# Longitudinal Effects

Interpret:

- baseline;
- slope;
- trajectory;
- within-person change;
- between-person differences;
- time-varying effects.

---

# Multilevel Effects

Separate levels:

- individual;
- group;
- institution;
- region.

Do not make cross-level claims without support.

---

# Ecological Fallacy Guard

Group-level associations do not automatically apply to individuals.

---

# Atomistic Fallacy Guard

Individual-level associations do not automatically apply to groups.

---

# Prediction

Prediction answers:

> How accurately can the model predict new observations?

Interpret using:

- discrimination;
- calibration;
- error;
- external validation;
- decision utility.

Do not treat predictive accuracy as causal explanation.

---

# Predictive Performance

Possible metrics include:

- AUC;
- accuracy;
- sensitivity;
- specificity;
- RMSE;
- MAE;
- R²;
- Brier score;
- calibration slope;
- calibration intercept.

Interpret each according to purpose.

---

# AUC

AUC measures ranking discrimination.

It does not measure:

- calibration;
- clinical utility;
- causal validity.

---

# Accuracy Guard

Accuracy can be misleading with class imbalance.

Consider:

- sensitivity;
- specificity;
- precision;
- recall;
- balanced accuracy.

---

# Calibration

Calibration evaluates agreement between predicted and observed risk.

A model may discriminate well but calibrate poorly.

---

# External Validation

Performance in development data does not guarantee external performance.

Interpret external validation separately.

---

# Machine Learning Interpretation

Distinguish:

- predictive importance;
- association;
- causal effect.

Feature importance is not causal importance.

---

# SHAP / Explainability Guard

SHAP values and similar tools explain model predictions, not necessarily biological or causal mechanisms.

---

# Diagnostic Accuracy

Interpret:

- sensitivity;
- specificity;
- likelihood ratios;
- predictive values;
- ROC;
- threshold;
- prevalence context.

---

# Sensitivity

Sensitivity is the probability of a positive test among those with the condition.

---

# Specificity

Specificity is the probability of a negative test among those without the condition.

---

# Predictive Values

PPV and NPV depend strongly on prevalence.

Do not transport them across populations without caution.

---

# Reliability

Reliability reflects consistency, not validity.

Do not write:

> The instrument is valid because Cronbach's alpha is high.

---

# Cronbach Alpha

Alpha depends on:

- item count;
- inter-item covariance;
- assumptions.

High alpha may indicate redundancy.

---

# Validity

Validity concerns interpretation and use of scores.

Possible evidence:

- content;
- structural;
- convergent;
- discriminant;
- criterion;
- predictive;
- known-groups;
- measurement invariance.

---

# Factor Analysis

Interpret:

- loading pattern;
- factor structure;
- cross-loadings;
- communalities;
- model fit;
- theoretical coherence.

---

# CFA

CFA interpretation should integrate:

- model fit;
- parameter estimates;
- residuals;
- theory;
- modification history.

Do not claim construct validity from fit indices alone.

---

# SEM

For SEM distinguish:

- measurement model;
- structural model;
- direct effects;
- indirect effects;
- total effects;
- model fit;
- R²;
- residuals.

---

# SEM Fit Guard

No single fit index determines model validity.

Consider:

- CFI/TLI;
- RMSEA;
- SRMR;
- residuals;
- parameter plausibility.

---

# PLS-SEM

Interpret separately:

- measurement model;
- structural model;
- predictive relevance.

Possible outputs include:

- outer loadings;
- reliability;
- AVE;
- HTMT;
- VIF;
- path coefficients;
- R²;
- f²;
- Q²;
- PLSpredict.

Do not infer causal validity from significant paths alone.

---

# Outer Loadings

Evaluate magnitude, reliability contribution, content relevance, and theoretical necessity.

Do not delete indicators mechanically to improve statistics.

---

# AVE

AVE reflects average variance captured by the construct.

Interpret alongside construct content and reliability.

---

# HTMT

HTMT assesses discriminant validity under specific assumptions.

A threshold is a diagnostic, not a substitute for conceptual distinctness.

---

# VIF

High VIF may indicate collinearity.

Do not remove theoretically important variables automatically.

---

# Path Coefficients

Interpret:

- direction;
- magnitude;
- confidence interval;
- theoretical meaning;
- design limits.

---

# R-Squared

R² reflects explained variance in the sample/model.

Do not equate high R² with causal truth.

---

# F-Squared

f² reflects change in explained variance associated with a predictor under the model.

Do not overuse generic thresholds.

---

# Q-Squared

Q² may reflect predictive relevance under specific procedures.

Interpret with the prediction design.

---

# Pharmacokinetic Results

Potential parameters:

- Cmax;
- Tmax;
- AUC;
- half-life;
- clearance;
- volume of distribution;
- bioavailability.

Interpret relative to:

- dose;
- formulation;
- sampling schedule;
- population;
- uncertainty;
- model.

---

# Pharmacogenetic Results

Potential interpretations include:

- genotype association;
- allele effect;
- treatment interaction;
- toxicity association;
- dose-response modification.

Consider:

- ancestry;
- HWE;
- genotype model;
- multiple testing;
- population stratification;
- phenotype definition;
- replication.

---

# Genetic Model Interpretation

Distinguish:

- codominant;
- dominant;
- recessive;
- overdominant;
- additive.

Do not switch models post hoc to obtain significance without labeling exploratory status.

---

# Hardy-Weinberg Equilibrium

HWE deviation may reflect:

- genotyping error;
- population structure;
- selection;
- chance.

It is not automatically grounds for exclusion.

---

# Experimental Results

Interpret relative to:

- randomization;
- control;
- intervention fidelity;
- blinding;
- compliance;
- attrition;
- protocol deviations.

---

# Intention-to-Treat

ITT generally preserves treatment assignment comparisons.

Interpret as assignment effect under trial conditions.

---

# Per-Protocol

Per-protocol estimates may be more vulnerable to selection bias.

Do not treat as automatically superior.

---

# Experimental Replicates

Distinguish:

- biological replicates;
- technical replicates.

Technical replicates do not increase independent biological sample size.

---

# Laboratory Assay Results

Interpret relative to:

- calibration;
- detection limits;
- controls;
- batch effects;
- replicate structure;
- assay precision.

---

# Formulation Studies

Interpret:

- pH;
- viscosity;
- spreadability;
- adhesiveness;
- stability;
- release;
- antimicrobial activity;

relative to formulation purpose and benchmark.

Do not infer clinical efficacy from physicochemical performance alone.

---

# Qualitative Interpretation

For qualitative results, interpretation should preserve:

- context;
- participant meaning;
- analytic orientation;
- variation;
- negative cases;
- reflexivity;
- relationship between data and claim.

---

# Qualitative Finding Unit

Possible units include:

- code;
- category;
- theme;
- pattern;
- mechanism;
- narrative;
- discourse;
- case;
- theoretical proposition.

---

# Theme Interpretation

A theme should express a meaningful pattern related to the research question.

Do not treat frequently mentioned topics automatically as themes.

---

# Frequency Guard

Frequency may support description but does not determine qualitative importance.

A rare finding may be analytically critical.

---

# Negative Case

Negative or discrepant cases should be considered explicitly.

They may:

- refine a theme;
- challenge a mechanism;
- reveal boundary conditions.

---

# Reflexivity

Interpretation should acknowledge how researcher position and analytic decisions may shape findings.

---

# Trustworthiness

Consider:

- credibility;
- dependability;
- confirmability;
- transferability;

when methodologically appropriate.

---

# Mixed-Method Interpretation

Use integrated meta-inference from `mixed-method-analysis`.

Interpret:

- convergence;
- complementarity;
- expansion;
- discordance;
- silence.

---

# Convergence

Convergence strengthens confidence only when strands are independently credible and conceptually aligned.

---

# Discordance

Discordance is not an analytical failure.

It may reveal:

- measurement mismatch;
- perception-behavior difference;
- contextual heterogeneity;
- temporal differences;
- subgroup variation;
- implementation problems.

---

# Meta-Analysis Interpretation

Interpret:

- pooled effect;
- confidence interval;
- heterogeneity;
- prediction interval;
- study quality;
- risk of bias;
- sensitivity;
- small-study effects.

---

# Pooled Effect Guard

A pooled estimate is an average under the model.

It may not represent every setting.

---

# Heterogeneity

Do not interpret I² alone.

Consider:

- tau²;
- tau;
- Q;
- prediction interval;
- clinical heterogeneity;
- methodological heterogeneity.

---

# Prediction Interval

A prediction interval may be more informative than the pooled confidence interval for future settings.

---

# Sensitivity Analysis

Sensitivity analyses test robustness to assumptions and decisions.

Classify:

- `ROBUST`
- `MODERATELY_ROBUST`
- `SENSITIVE`
- `HIGHLY_SENSITIVE`
- `NOT_ASSESSED`

---

# Robustness

A result is more credible when it persists across reasonable alternative specifications.

---

# Missing Data

Interpret results relative to:

- amount;
- pattern;
- mechanism assumptions;
- imputation;
- complete-case analysis.

---

# Multiplicity

Multiple outcomes, subgroups, models, or hypotheses increase false-positive risk.

Record correction strategy.

---

# Multiplicity Status

Classify:

- `CONTROLLED`
- `PARTIALLY_CONTROLLED`
- `EXPLORATORY`
- `UNCONTROLLED`

---

# P-Hacking Guard

Do not privilege a significant model selected from many unreported alternatives.

---

# HARKing Guard

Do not rewrite hypotheses after seeing results without labeling them post hoc.

---

# Post-Hoc Findings

Label clearly:

`EXPLORATORY_POST_HOC`

They may motivate future study.

---

# Subgroup Results

Require:

- scientific rationale;
- interaction evidence;
- adequate sample;
- multiplicity consideration.

---

# Subgroup Significance Guard

Do not conclude groups differ because:

- subgroup A p < 0.05;
- subgroup B p > 0.05.

Test the difference directly.

---

# Unexpected Findings

Unexpected findings should be:

1. verified;
2. checked for error;
3. assessed for robustness;
4. compared with theory;
5. treated as exploratory if not prespecified.

---

# Contradictory Findings

Contradiction may occur:

- within study;
- across outcomes;
- across subgroups;
- across methods;
- across studies.

Do not hide contradictions.

---

# Bias Interpretation

Consider relevant bias domains.

Potential examples:

- selection bias;
- confounding;
- information bias;
- measurement error;
- attrition bias;
- performance bias;
- detection bias;
- reporting bias.

---

# Residual Confounding

Even adjusted observational results may retain residual confounding.

Do not overstate causality.

---

# Reverse Causation

Temporal ordering matters.

Cross-sectional associations may permit reverse causation.

---

# External Validity

Separate:

- internal validity;
- external validity.

A strong internal estimate may still have limited generalizability.

---

# Generalizability

Do not claim universal applicability from one context without support.

---

# Causal Interpretation Gate

Before causal language, check:

- intervention or natural experiment;
- temporal order;
- exchangeability;
- confounding;
- measurement;
- selection;
- positivity;
- interference;
- consistency.

---

# Causal Language

Use causal terms only when design and assumptions justify them.

Possible causal terms:

- effect;
- impact;
- causes;
- leads to.

Otherwise prefer:

- associated with;
- related to;
- predicts;
- corresponds to.

---

# Prediction vs Causation

A variable can predict an outcome without causing it.

Do not equate predictive importance with intervention target.

---

# Mechanism Interpretation

Mechanisms should be classified as:

- directly tested;
- indirectly supported;
- plausible;
- speculative.

Do not present plausible mechanism as established mechanism.

---

# Theory Relationship

Classify finding-theory relationship:

- `SUPPORTS`
- `PARTIALLY_SUPPORTS`
- `REFINES`
- `EXTENDS`
- `CONTRADICTS`
- `OUTSIDE_THEORY_SCOPE`
- `INCONCLUSIVE`

Do not force theory support.

---

# Conceptual Framework Relationship

Record whether findings:

- confirm relationship;
- weaken relationship;
- reveal moderation;
- reveal mediation;
- reveal nonlinearity;
- reveal boundary;
- reveal missing construct.

---

# Novelty Relationship

Do not claim novelty from a result merely because it is statistically significant.

Novelty remains tied to the audited research contribution.

---

# Negative Results

Negative results can be valuable.

Possible meanings:

- theory not supported;
- effect smaller than expected;
- context boundary;
- measurement limitation;
- insufficient precision.

---

# Null Result Taxonomy

Classify:

- `PRECISE_NULL_LIKE`
- `IMPRECISE`
- `UNDERPOWERED`
- `MODEL_DEPENDENT`
- `CONTEXT_DEPENDENT`
- `TRUE_ABSENCE_POSSIBLE`
- `INCONCLUSIVE`

---

# Precision

Precision is not the same as validity.

A precise biased estimate remains biased.

---

# Data Consistency Guard

If conflicting numbers appear, stop interpretation and resolve discrepancy.

Use:

`RESULT_INCONSISTENCY_REQUIRES_RESOLUTION`

---

# Unit Check

Verify units before interpreting.

Common errors:

- mg vs µg;
- percentage vs proportion;
- per 1000 vs per 100000;
- log scale vs raw scale.

---

# Direction Check

Verify coding direction.

Examples:

- higher score = worse symptom;
- reversed Likert scale;
- reference category.

---

# Model Fit vs Scientific Fit

Good numerical fit does not guarantee scientific validity.

---

# Overadjustment

Adjusting for mediators or colliders can distort causal effects.

Interpret adjusted estimates in light of the causal model.

---

# Bayesian Interpretation

For Bayesian results consider:

- posterior estimate;
- credible interval;
- posterior probability;
- prior sensitivity;
- Bayes factor when used.

---

# Clinical Relevance

For health studies, interpret relation to:

- patient benefit;
- harm;
- treatment burden;
- clinical thresholds;
- absolute effect.

---

# Educational Relevance

For educational research consider:

- score meaning;
- learning outcomes;
- pedagogical relevance;
- classroom feasibility.

---

# Organizational Relevance

For organizational studies consider:

- effect size;
- implementation;
- productivity;
- employee outcomes;
- decision relevance.

---

# Engineering Relevance

For engineering studies consider:

- tolerance;
- performance threshold;
- safety margin;
- efficiency;
- reliability.

---

# Biological Relevance

Statistical significance does not guarantee biological relevance.

Interpret mechanism, dose, and magnitude.

---

# Policy Relevance

Policy relevance depends on:

- population impact;
- feasibility;
- equity;
- cost;
- implementation.

---

# Claim Strength

Classify claim strength:

- `STRONG_DIRECT`
- `MODERATE_DIRECT`
- `TENTATIVE`
- `EXPLORATORY`
- `UNSUPPORTED`

---

# Claim Boundary

Every interpretation should state:

- population;
- setting;
- time;
- outcome;
- design;
- analytic assumptions.

---

# Claim Escalation Guard

Do not escalate:

```text
association
→ mechanism
→ causation
→ recommendation
```

without evidence at each step.

---

# Result Interpretation Matrix

Recommended:

| Result | Direction | Magnitude | Uncertainty | Robustness | Design Boundary | Claim Strength |
|---|---|---|---|---|---|---|

---

# Hypothesis Interpretation Matrix

| Hypothesis | Result | Status | Evidence Strength | Caveat |
|---|---|---|---|---|

---

# Robustness Matrix

| Analysis | Estimate | Interval | Key Assumption | Conclusion Change |
|---|---|---|---|---|

---

# Contradiction Matrix

| Result A | Result B | Relationship | Possible Explanation | Interpretation |
|---|---|---|---|---|

---

# Result Passport

Recommended internal representation:

```yaml
result_interpretation:
  status:
  research_question:
  hypothesis:
  prespecification_status:
  study_design:
  population:
  analysis_target:
  method:
  estimate:
  effect_measure:
  direction:
  magnitude:
  uncertainty:
  practical_importance:
  statistical_evidence:
  robustness:
  sensitivity:
  missing_data:
  multiplicity:
  bias_risk:
  causal_status:
  mechanism_status:
  theory_relationship:
  conceptual_framework_relationship:
  contradictory_results:
  unexpected_results:
  external_validity:
  claim_strength:
  claim_boundary:
  unsupported_claims:
  scientific_discussion_handoff:
```

Unknown fields remain unknown.

---

# Result Interpretation Workflow

Use:

```text
1. Identify the research question
2. Identify intended inference
3. Identify study design
4. Identify estimand / analysis target
5. Verify result consistency
6. Interpret direction
7. Interpret magnitude
8. Interpret uncertainty
9. Assess practical importance
10. Assess robustness
11. Assess bias and design boundaries
12. Assess hypothesis / theory relationship
13. Identify contradictions
14. Identify unsupported claims
15. Create defensible result statement
16. Hand off to scientific-discussion
```

---

# Quantitative Result Statement Template

Prefer:

> [Exposure/intervention] was associated with [direction and magnitude] in [outcome], estimated as [effect measure and value] with [interval], in [population/design]. The estimate was [robust/not robust] to [key sensitivity], but interpretation is limited by [main design limitation].

---

# Experimental Result Statement Template

Prefer:

> Participants assigned to [intervention] experienced [magnitude] difference in [outcome] compared with [control], with [interval]. The randomized design supports causal interpretation under assumptions of [key conditions], although [limitations] constrain generalization.

---

# Qualitative Result Statement Template

Prefer:

> Participants described [theme/pattern], characterized by [key dimensions], with variation across [cases/context]. Negative cases indicated [boundary], suggesting that [interpretive claim] applies primarily under [conditions].

---

# Mixed-Method Result Statement Template

Prefer:

> Quantitative evidence showed [pattern], while qualitative evidence identified [mechanism/context]. Their [convergence/complementarity/discordance] suggests [meta-inference], although [boundary or unresolved contradiction] limits the strength of the integrated claim.

---

# Meta-Analysis Result Statement Template

Prefer:

> Across [k] studies, the average effect was [estimate] with [interval]. Between-study heterogeneity was [description], and the prediction interval [range] indicates that effects may vary substantially across comparable settings. Sensitivity analyses [result], while [risk-of-bias/small-study limitation] reduces confidence in the pooled estimate.

---

# Minimal Output

For a simple request provide:

## Research Question
[...]

## Main Result
[...]

## Direction and Magnitude
[...]

## Uncertainty
[...]

## Scientific Meaning
[...]

## Robustness
[...]

## Limitations
[...]

## Supported Claim
[...]

## Unsupported Claim
[...]

---

# Comprehensive Output

When full interpretation is requested:

## A. Research Question
[...]

## B. Hypothesis Status
[...]

## C. Study Design
[...]

## D. Analysis Target
[...]

## E. Main Findings
[...]

## F. Direction
[...]

## G. Magnitude
[...]

## H. Uncertainty
[...]

## I. Practical / Clinical Importance
[...]

## J. Robustness
[...]

## K. Sensitivity Analyses
[...]

## L. Missing Data
[...]

## M. Multiplicity
[...]

## N. Bias and Validity
[...]

## O. Causal Status
[...]

## P. Mechanism Status
[...]

## Q. Theory Relationship
[...]

## R. Conceptual Framework Relationship
[...]

## S. Unexpected Findings
[...]

## T. Contradictions
[...]

## U. External Validity
[...]

## V. Claim Boundaries
[...]

## W. Unsupported Claims
[...]

## X. Scientific Discussion Handoff
[...]

---

# Scientific Discussion Handoff

Pass downstream to `scientific-discussion`:

```yaml
scientific_discussion_handoff:
  main_findings:
  effect_magnitudes:
  uncertainty:
  practical_importance:
  hypothesis_status:
  theory_relationship:
  mechanism_status:
  robustness:
  contradictions:
  unexpected_findings:
  boundary_conditions:
  external_validity:
  limitations:
  unsupported_claims:
```

Do not carry raw software output without interpretation.

---

# Relationship with Analysis Planner

`analysis-planner` defines what should be estimated or interpreted.

`result-interpreter` interprets what the completed analysis produced.

Use:

```text
analysis-planner
      ↓
analysis
      ↓
result-interpreter
```

---

# Relationship with Statistical Method Selector

`statistical-method-selector` selects the quantitative method.

`result-interpreter` interprets the resulting estimate according to that method.

---

# Relationship with Qualitative Analysis

`qualitative-analysis` develops qualitative findings.

`result-interpreter` evaluates their meaning, boundaries, variation, and confidence before discussion.

---

# Relationship with Mixed-Method Analysis

`mixed-method-analysis` generates meta-inferences.

`result-interpreter` determines what those meta-inferences support and where they remain uncertain.

---

# Relationship with Meta-Analysis

`meta-analysis` generates pooled or non-pooled evidence.

`result-interpreter` evaluates the scientific meaning of average effect, heterogeneity, prediction interval, and bias.

---

# Relationship with Hypothesis Builder

Compare findings with prespecified hypotheses.

Do not rewrite hypotheses after seeing results.

---

# Relationship with Theoretical Framework

Interpret whether results support, refine, extend, or contradict theory.

---

# Relationship with Conceptual Framework

Interpret whether conceptual relationships are supported, weakened, or require revision.

---

# Relationship with Scientific Discussion

`result-interpreter` should stop at defensible interpretation of the study's own results.

`scientific-discussion` then compares those interpreted results with:

- prior literature;
- State of the Art;
- competing explanations;
- theory;
- mechanisms;
- context.

---

# Relationship with Implication Builder

Implications should follow only after interpretation and discussion.

Do not jump directly from significance to recommendation.

---

# User-Friendly Behavior

Prefer:

> The coefficient is statistically significant, but the more important result is that the estimated effect is small and the confidence interval excludes large effects. The data therefore support a modest association, not a strong practical effect.

Or:

> The p-value is above 0.05, but the confidence interval is wide and still includes effects that could be clinically important. This is better interpreted as inconclusive rather than evidence of no effect.

Or:

> The PLS-SEM path is significant, but because the study is cross-sectional, the result supports an association between the constructs rather than a causal effect.

Or:

> The qualitative theme was not the most frequent code, but it consistently explained why several participants deviated from the dominant pattern. That makes it analytically important as a boundary condition.

Or:

> The meta-analysis shows a positive average effect, but the prediction interval crosses the null. The average finding therefore should not be interpreted as evidence that the intervention will work in every comparable setting.

---

# Avoid These Behaviors

Do not:

- equate p-value with scientific importance;
- equate non-significance with no effect;
- report only significance without magnitude;
- ignore confidence intervals;
- ignore practical importance;
- infer causality from cross-sectional association;
- infer mechanism from mediation alone;
- infer subgroup differences from separate significance tests;
- treat predictive importance as causal importance;
- call a model valid because fit indices are acceptable;
- call a measure valid because reliability is high;
- delete indicators merely to improve PLS-SEM statistics;
- treat qualitative frequency as importance;
- hide negative cases;
- force mixed-method convergence;
- hide discordance;
- interpret pooled meta-analysis effects as universal;
- ignore heterogeneity or prediction intervals;
- ignore missing data;
- ignore multiplicity;
- reinterpret exploratory findings as confirmatory;
- HARK;
- outcome switch;
- elevate secondary outcomes because primary outcomes are null;
- overgeneralize beyond the population;
- exaggerate novelty;
- transform association into recommendation without evidence;
- let software-generated labels determine the conclusion.

---

# Stop Conditions

Do not classify interpretation as ready when:

- research question is unknown;
- study design is unclear;
- analysis target is unclear;
- effect measure is unclear;
- units are inconsistent;
- coding direction is unknown;
- tables and figures conflict;
- software output appears incomplete;
- robustness has not been assessed when required;
- multiplicity is substantial but unaddressed;
- missing-data handling is unknown and potentially consequential;
- causal interpretation exceeds design;
- post-hoc findings are being presented as prespecified;
- theory is being retrofitted solely to explain preferred results;
- contradictions are being ignored;
- the interpretation depends only on p-values.

Use:

- `RETURN_TO_ANALYSIS_PLANNER`
- `RETURN_TO_STATISTICAL_METHOD_SELECTOR`
- `RETURN_TO_QUALITATIVE_ANALYSIS`
- `RETURN_TO_MIXED_METHOD_ANALYSIS`
- `RETURN_TO_META_ANALYSIS`
- `RESULT_INCONSISTENCY_REQUIRES_RESOLUTION`
- `RESULT_INTERPRETATION_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`result-interpreter` succeeds when completed analytical outputs have been translated into scientifically defensible findings that explicitly identify the research question, intended inference, study design, analysis target, result direction, effect or pattern magnitude, uncertainty, practical importance, robustness, sensitivity to assumptions, missing-data and multiplicity context, bias and validity constraints, causal status, mechanism status, hypothesis relationship, theory relationship, conceptual-framework relationship, contradictions, unexpected findings, external-validity boundaries, supported claims, unsupported claims, and downstream scientific-discussion handoff, while preventing significance alone, non-significance alone, software labels, post-hoc storytelling, unsupported causal escalation, selective interpretation, or methodological fashion from determining the scientific conclusion.
