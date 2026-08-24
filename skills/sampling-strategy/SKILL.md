---
name: sampling-strategy
description: Design a scientifically defensible sampling strategy that connects the target population, source population, sampling frame, unit structure, recruitment or selection mechanism, sample-size rationale, representativeness needs, clustering, stratification, attrition, qualitative information needs, laboratory replication, and feasibility to the approved methodology and intended inference. Use after methodology architecture is sufficiently stable and before final data collection or analysis planning.
---

# Sampling Strategy

## Purpose

`sampling-strategy` determines:

> Who, what, or which units should be selected, from where, by what mechanism, and in what quantity so that the resulting evidence can support the intended scientific inference?

This skill converts methodological sampling requirements into a defensible selection strategy.

It does not define the research question.

It does not select the statistical model.

It does not invent a sampling frame.

It does not force probability sampling when the inference goal does not require population representativeness.

It does not treat convenience as scientific justification.

---

# Core Principle

Use:

> Sampling must match the intended inference.

The correct sampling strategy depends on:

- target population;
- source population;
- unit of analysis;
- unit of observation;
- study design;
- estimand or inference target;
- prevalence or event structure where relevant;
- clustering;
- repeated measurements;
- measurement burden;
- feasibility;
- ethics;
- expected attrition;
- analysis requirements.

Do not begin with a desired sample size.

Begin with:

> What population or units must the study validly represent or inform?

---

# Position in the Framework

Preferred flow:

```text
Research Question
      ↓
problem-solving-approach
      ↓
methodology-architect
      ↓
sampling-strategy
      │
      ├───────────────┐
      ▼               ▼
protocol-builder  instrument-design
      │               │
      └───────┬───────┘
              ↓
        DESIGN READY
              ↓
        analysis-planner
```

Sampling may be refined iteratively with protocol and measurement development.

---

# Required Upstream Context

Use available information from:

- `methodology-architect`;
- `problem-solving-approach`;
- `research-question-builder`;
- `protocol-builder` when already available;
- `instrument-design` when already available.

Minimum useful context normally includes:

- primary research question;
- study design;
- target population;
- source population;
- unit of analysis;
- unit of observation;
- unit of assignment when relevant;
- intended inference;
- primary outcome or phenomenon;
- setting;
- temporal structure;
- clustering;
- expected feasibility constraints.

Do not ask the user to repeat already-established context.

---

# Sampling Readiness Gate

Classify:

- `READY_FOR_SAMPLING_STRATEGY`
- `TARGET_POPULATION_UNCLEAR`
- `SOURCE_POPULATION_UNCLEAR`
- `SAMPLING_FRAME_UNCLEAR`
- `UNIT_STRUCTURE_UNCLEAR`
- `DESIGN_NOT_STABLE`
- `SAMPLE_SIZE_INPUTS_INCOMPLETE`
- `SAMPLING_ALREADY_ESTABLISHED`
- `SAMPLING_REQUIRES_REASSESSMENT`

Do not calculate sample size if the sampling target itself is unclear.

---

# Population Architecture

Distinguish:

```text
Target Population
      ↓
Source Population
      ↓
Accessible Population
      ↓
Sampling Frame
      ↓
Eligible Units
      ↓
Selected Sample
      ↓
Analyzed Sample
```

These are not interchangeable.

---

# Target Population

The target population is the broader population to which the researcher intends to generalize or apply the inference.

Record:

```yaml
target_population:
  definition:
  geography:
  time_period:
  relevant_characteristics:
  intended_generalization:
```

Do not define the target population only after observing who was easy to recruit.

---

# Source Population

The source population is the population from which study units actually arise.

It should be compatible with the target inference.

Record:

```yaml
source_population:
  definition:
  setting:
  coverage:
  relationship_to_target_population:
```

---

# Accessible Population

The accessible population is the portion of the source population practically reachable during the study.

Do not assume accessible population equals target population.

---

# Sampling Frame

A sampling frame may be:

- registry;
- patient list;
- school list;
- employee roster;
- household listing;
- census block;
- database;
- clinic attendance list;
- laboratory batch list;
- article corpus;
- administrative register.

Assess:

- completeness;
- duplication;
- outdated entries;
- missing groups;
- coverage error;
- access restrictions.

Use:

`SAMPLING_FRAME_COVERAGE_RISK`

when needed.

---

# Sampling Unit

Specify the unit actually selected.

Possible examples:

- person;
- household;
- classroom;
- school;
- hospital;
- organization;
- specimen;
- formulation batch;
- animal;
- article;
- event;
- geographic cluster.

The sampling unit may differ from the unit of analysis.

---

# Unit of Analysis

Record separately.

Example:

```yaml
sampling_unit: school
unit_of_observation: student
unit_of_analysis: student
unit_of_inference: student population
cluster: school
```

Do not ignore the implications of selecting clusters when analysis occurs at the individual level.

---

# Unit of Assignment

For experiments, distinguish:

- unit sampled;
- unit assigned;
- unit measured;
- unit analyzed.

These can differ.

---

# Unit of Inference

Define explicitly what the final inference is intended to describe.

Examples:

- all students in a district;
- participating teachers only;
- patients meeting clinical criteria;
- formulation batches produced under defined conditions;
- studies meeting review eligibility criteria.

---

# Census vs Sample

Use a census when all eligible units in the defined population are included.

Do not call a convenience sample a census merely because all available units were included.

Use:

- `CENSUS`
- `SAMPLE`

---

# Probability Sampling

Probability sampling may be preferred when population-level estimation or representativeness is central.

Possible forms:

- simple random sampling;
- systematic sampling;
- stratified random sampling;
- cluster sampling;
- multistage sampling;
- probability proportional to size;
- two-stage sampling.

Selection probabilities should be known or reconstructable where possible.

---

# Simple Random Sampling

Use when:

- a usable frame exists;
- units are individually selectable;
- equal-probability selection is appropriate.

Operationally preserve the randomization mechanism.

---

# Systematic Sampling

Specify:

- ordered frame;
- sampling interval;
- random start.

Check for periodicity that could bias selection.

---

# Stratified Sampling

Use when representation or precision is improved by predefined strata.

Possible strata include:

- sex;
- age;
- region;
- school type;
- disease group;
- organization size.

Strata should be defined before selection.

Do not create strata solely after observing outcome values.

---

# Disproportionate Stratification

Disproportionate sampling may be justified to ensure adequate subgroup information.

If population estimates are required, weighting may later be necessary.

Do not ignore unequal selection probabilities.

---

# Cluster Sampling

Use cluster sampling when natural groupings are sampled, such as:

- schools;
- villages;
- clinics;
- hospitals;
- classes;
- organizations.

Account for:

- cluster size;
- intra-cluster correlation;
- number of clusters;
- design effect;
- unequal cluster sizes.

A large number of individuals from very few clusters may still provide weak cluster-level information.

---

# Multistage Sampling

Define each stage explicitly.

Example:

```text
Districts
  ↓
Schools
  ↓
Classes
  ↓
Students
```

Record selection method at every stage.

---

# Probability Proportional to Size

Use only when scientifically appropriate for unequal-size clusters.

Document the measure of size.

---

# Non-Probability Sampling

Non-probability strategies may be scientifically valid when:

- population estimation is not the goal;
- the population is hard to enumerate;
- qualitative depth is prioritized;
- purposive case selection is required;
- feasibility studies are being conducted.

Possible forms:

- convenience;
- purposive;
- quota;
- snowball;
- respondent-driven;
- consecutive;
- theoretical sampling;
- criterion sampling;
- maximum variation;
- homogeneous sampling;
- expert sampling.

Do not present non-probability sampling as statistically representative without justification.

---

# Convenience Sampling Guard

Convenience sampling may be acceptable for:

- pilot studies;
- exploratory research;
- early instrument development;
- feasibility work;
- some laboratory studies.

It should not be described as population-representative by default.

Use:

`CONVENIENCE_LIMITATION`

---

# Consecutive Sampling

In clinical or service settings, consecutive inclusion of all eligible units over a defined period may reduce discretionary selection compared with convenience recruitment.

Specify the recruitment window.

---

# Purposive Sampling

Use when specific information-rich cases are needed.

Possible logic includes:

- typical cases;
- extreme cases;
- maximum variation;
- critical cases;
- criterion-based cases;
- expert participants.

Sampling criteria should be explicit.

---

# Snowball Sampling

Use when population access depends on participant networks.

Recognize network dependence and selection bias.

Do not treat snowball samples as independent random samples.

---

# Respondent-Driven Sampling

If used, distinguish it from ordinary snowball sampling.

Its inferential assumptions require specialized handling.

Do not claim population estimates without satisfying those assumptions.

---

# Quota Sampling

Quota sampling may ensure category representation but does not automatically create probability sampling.

---

# Qualitative Sampling

Qualitative sampling follows information needs rather than statistical representativeness.

Possible strategies:

- purposive;
- maximum variation;
- homogeneous;
- criterion;
- theoretical;
- snowball;
- expert;
- typical case;
- deviant case.

The sample must fit the epistemic objective.

---

# Information Power

Qualitative sample adequacy may depend on:

- specificity of sample;
- strength of dialogue;
- study aim breadth;
- analytic strategy;
- theoretical background;
- case richness.

Do not apply arbitrary universal numerical thresholds.

---

# Saturation

Use saturation carefully.

Possible meanings include:

- code saturation;
- meaning saturation;
- theoretical saturation;
- thematic sufficiency.

Do not claim saturation merely because no new codes appeared in the last interview without documenting the analytic logic.

---

# Theoretical Sampling

Use theoretical sampling when data collection evolves in response to emerging theory, especially in grounded-theory designs.

Do not predefine a rigid statistically powered sample for this purpose.

---

# Mixed-Method Sampling

Mixed-method studies should specify sampling for each strand.

Possible relationships include:

- identical;
- nested;
- parallel;
- multilevel;
- sequential.

Record:

```yaml
mixed_sampling:
  quantitative_sample:
  qualitative_sample:
  relationship:
  integration_purpose:
```

---

# Experimental Sampling

For experiments distinguish:

- sampling from a population;
- random assignment to conditions.

Random assignment does not automatically create a representative sample.

---

# Laboratory Sampling

Laboratory studies may sample:

- biological specimens;
- batches;
- isolates;
- formulations;
- cell lines;
- devices;
- materials.

The sample-size logic must follow the experimental unit.

---

# Biological Replication

Biological replicates represent independent biological units.

Examples:

- independent patients;
- independent animals;
- independent cultures;
- independent biological specimens.

---

# Technical Replication

Technical replicates repeat measurement on the same underlying experimental unit.

They assess measurement precision.

They are not independent biological sample units.

---

# Batch Replication

For formulation or manufacturing research, independently prepared batches may be the relevant experimental units.

Do not count multiple measurements from one batch as independent batch replication.

---

# Pseudoreplication Guard

Use:

`PSEUDOREPLICATION_RISK`

when:

- repeated wells;
- repeated readings;
- subsamples;
- multiple time points;

are incorrectly counted as independent sampling units.

---

# Review Sampling

For systematic reviews, the sample is the eligible evidence corpus.

Sampling logic includes:

- databases;
- search coverage;
- eligibility criteria;
- date range;
- language restrictions;
- publication type;
- study design;
- duplicate populations.

Do not use arbitrary article-count targets.

---

# Bibliometric Corpus Sampling

Define:

- database;
- search string;
- field restrictions;
- document type;
- date range;
- language;
- indexing scope.

The corpus should represent the intended literature domain.

---

# Secondary Data Sampling

For secondary datasets clarify:

- original sampling design;
- inclusion process;
- coverage;
- weighting;
- attrition;
- missingness;
- exclusions.

Do not treat a large database as a random sample merely because it is large.

---

# Registry Sampling

Assess:

- registry eligibility;
- catchment;
- completeness;
- duplicate entries;
- reporting delay;
- linkage quality.

---

# Administrative Data Sampling

Administrative data reflect service or system processes.

They may systematically exclude people who do not interact with the system.

---

# Sample Size Principle

Sample size should be justified according to the inferential task.

Possible drivers include:

- estimation precision;
- hypothesis-testing power;
- event availability;
- cluster structure;
- prediction model stability;
- diagnostic accuracy;
- reliability estimation;
- validation precision;
- qualitative information power;
- laboratory replication;
- feasibility.

Do not use one universal sample-size rule.

---

# Precision-Based Sample Size

Use when the primary goal is estimation.

Possible targets:

- confidence interval width;
- margin of error;
- precision around prevalence;
- precision around mean;
- precision around diagnostic accuracy.

Specify the desired precision and confidence level.

---

# Power-Based Sample Size

Use when the primary aim is hypothesis testing.

Required inputs may include:

- effect size;
- alpha;
- desired power;
- group allocation;
- variance;
- outcome type;
- correlation structure;
- repeated measurement;
- clustering.

Do not invent effect sizes.

---

# Effect Size Source Hierarchy

Prefer effect-size assumptions from:

1. high-quality prior studies in comparable populations;
2. meta-analysis;
3. pilot data;
4. minimally important difference;
5. scientifically meaningful target effect.

Avoid arbitrary "small/medium/large" defaults unless justified.

---

# Minimal Clinically or Practically Important Difference

When relevant, sample size may be based on a minimally important difference rather than expected observed effect.

State clearly which value is used.

---

# Alpha and Power

Do not treat conventional alpha and power values as universal laws.

Use domain norms and scientific consequences.

Document choices.

---

# Two-Sided vs One-Sided Testing

One-sided assumptions require strong scientific justification.

Do not choose one-sided tests merely to reduce sample size.

---

# Unequal Allocation

If groups are intentionally unequal, include allocation ratio in sample-size planning.

---

# Finite Population

When the source population is small relative to the intended sample, finite-population considerations may be relevant.

Do not apply finite population correction automatically.

---

# Design Effect

Clustered sampling or complex sampling may require inflation for design effect.

Conceptually:

```text
Effective information
≠
Raw number of observations
```

Do not ignore intracluster similarity.

---

# Intracluster Correlation

ICC affects information contributed by clustered observations.

High ICC means additional individuals within the same cluster add less independent information.

---

# Number of Clusters

For cluster-level inference, the number of clusters can be more important than total individuals.

Do not compensate for very few clusters merely by enrolling many individuals per cluster.

---

# Repeated Measures

Repeated measurements within the same unit are correlated.

Sample-size planning should distinguish:

- number of units;
- number of repeated measurements.

Do not multiply these counts as if all observations were independent.

---

# Longitudinal Attrition

Inflate recruitment for expected attrition when justified.

Record:

```yaml
attrition:
  expected_rate:
  evidence_source:
  planned_recruitment_inflation:
  retention_strategy:
```

Do not use arbitrary attrition percentages without context.

---

# Nonresponse

For surveys consider:

- expected contact rate;
- eligibility rate;
- response rate;
- completion rate.

Recruitment target may exceed final required analyzed sample.

---

# Screening Yield

Clinical and rare-population studies may require screening many units to enroll the needed sample.

Track:

```text
screened → eligible → consented → enrolled
```

---

# Event-Based Sampling

For outcomes that depend on event counts, information may be constrained more by number of events than total sample size.

Examples:

- survival models;
- rare disease outcomes;
- diagnostic positives;
- prediction models.

Do not use total N alone.

---

# Prediction Model Sample Size

Prediction-model sample size should consider:

- outcome prevalence or event fraction;
- number and complexity of candidate predictors;
- anticipated model performance;
- shrinkage;
- calibration precision;
- validation strategy.

Do not rely solely on simplistic rules such as a fixed number of events per predictor.

Detailed statistical planning belongs downstream.

---

# Diagnostic Accuracy Sample Size

May depend on desired precision for:

- sensitivity;
- specificity;
- prevalence of target condition;
- confidence interval width.

Ensure sufficient positive and negative cases.

---

# Reliability Study Sample Size

Reliability studies may depend on:

- reliability coefficient;
- desired precision;
- number of raters;
- number of repetitions.

---

# Instrument Validation Sample Size

Instrument validation may require distinct samples or phases for:

- content validation;
- pilot;
- structural validity;
- reliability;
- criterion validity;
- cross-validation.

Do not use one sample-size heuristic for all phases.

---

# SEM Sample Size Guard

Do not justify SEM sample size only through generic minimum-N rules.

Consider:

- model complexity;
- number of latent variables;
- indicator quality;
- estimator;
- effect sizes;
- missing data;
- distribution;
- identification;
- power for target parameters.

---

# PLS-SEM Sample Size Guard

Do not use the "10-times rule" as the sole scientific justification.

Use stronger methods where possible, such as:

- power analysis for target paths;
- inverse square-root or gamma-exponential approaches when scientifically appropriate;
- simulation;
- prediction-oriented requirements.

The final method-specific calculation belongs downstream.

---

# Machine Learning Sample Size Guard

Do not assume large predictor count plus small N can be solved simply by choosing machine learning.

Consider:

- effective sample size;
- outcome prevalence;
- feature dimensionality;
- validation;
- leakage risk;
- model complexity.

---

# Genetic Study Sampling

Consider:

- allele frequency;
- genotype frequency;
- expected effect;
- outcome prevalence;
- ancestry / population structure;
- multiple testing;
- missing genotype rate;
- quality control.

Do not ignore rare genotype scarcity.

---

# Pharmacokinetic Sampling

Distinguish:

- number of participants;
- number of samples per participant;
- sampling time points.

Rich sampling and sparse sampling solve different design problems.

---

# Rare Population Sampling

When the target population is rare or difficult to access, possible strategies include:

- multicenter recruitment;
- registry-based identification;
- prolonged recruitment;
- case-control design;
- adaptive recruitment.

Feasibility does not remove the need to state selection limitations.

---

# Hard-to-Reach Population

Possible approaches include:

- community-based recruitment;
- network recruitment;
- respondent-driven sampling;
- trusted intermediaries.

Ethical and privacy safeguards are especially important.

---

# Vulnerable Populations

Sampling must avoid coercion or undue influence.

Do not select vulnerable populations merely because access is easy.

---

# Inclusion and Exclusion Criteria

Sampling eligibility should align with:

- RQ;
- target population;
- safety;
- measurement validity;
- study design.

Avoid exclusions that unnecessarily reduce generalizability.

---

# Over-Restriction Guard

Use:

`OVER_RESTRICTIVE_ELIGIBILITY`

when criteria make the sample scientifically narrower than the intended target population without justification.

---

# Under-Restriction Guard

Use:

`UNDER_RESTRICTIVE_ELIGIBILITY`

when heterogeneity threatens validity or safety.

---

# Recruitment Source

Specify the operational source:

- clinic;
- school;
- community;
- database;
- professional network;
- registry;
- laboratory collection;
- online panel.

Recruitment source affects selection bias.

---

# Recruitment Window

Define the time period during which sampling occurs.

This matters when the population changes over time.

---

# Seasonal Sampling

If the phenomenon varies seasonally, ensure sampling periods are appropriate.

---

# Geographic Sampling

Define geographic coverage.

Do not infer national representativeness from one city without explicit justification.

---

# Multi-Site Sampling

Specify:

- site selection;
- site eligibility;
- site contribution;
- site-level clustering;
- balancing strategy.

---

# Site Selection Bias

Conveniently selected sites may produce systematic differences.

Flag:

`SITE_SELECTION_BIAS_RISK`

---

# Sample Representativeness

Representativeness is specific to the inference target.

Assess:

- demographic;
- geographic;
- clinical;
- organizational;
- temporal;
- behavioral;
- disease severity;
- socioeconomic;
- institutional.

Do not claim "representative" without a defined target population.

---

# Generalizability vs Transferability

Quantitative population inference and qualitative transferability are not identical.

Use domain-appropriate language.

---

# Weighting Awareness

Complex probability samples may require weights based on:

- selection probability;
- nonresponse;
- post-stratification;
- calibration.

Weight calculation belongs downstream, but sampling design must preserve required information.

---

# Oversampling

Oversampling may be useful for:

- rare subgroups;
- minority groups;
- high-risk groups;
- small strata.

Document the rationale.

---

# Subgroup Analysis

Do not oversample or create subgroup targets without a substantive scientific reason.

Subgroup sample adequacy should be planned before data collection when subgroup inference is important.

---

# Matching

Matching may occur in:

- case-control studies;
- observational comparisons;
- validation studies.

Specify:

- matching variables;
- ratio;
- exact vs approximate matching;
- risk of overmatching.

Matching is not a substitute for all confounding control.

---

# Pairing

Paired designs may involve:

- matched individuals;
- before-after measurements;
- twins;
- paired specimens.

Sampling strategy must preserve pair identity.

---

# Replacement

If selected units cannot participate, define whether replacement is permitted.

Random replacement should preserve the sampling mechanism.

Do not substitute convenient units silently.

---

# Duplicate Enrollment

Prevent repeated inclusion of the same unit when independence is required.

---

# Sampling Log

Maintain when relevant:

```yaml
sampling_log:
  frame_id:
  selection_status:
  eligibility_status:
  contact_status:
  consent_status:
  enrollment_status:
  exclusion_reason:
  replacement_status:
```

---

# Recruitment Flow

When useful:

```text
Frame
 ↓
Selected
 ↓
Contacted
 ↓
Eligible
 ↓
Consented
 ↓
Enrolled
 ↓
Completed
 ↓
Analyzed
```

---

# Sampling Bias Architecture

Potential sampling-stage biases include:

- coverage bias;
- selection bias;
- volunteer bias;
- nonresponse bias;
- referral bias;
- survivor bias;
- spectrum bias;
- site-selection bias;
- healthy-worker effect;
- Berkson-type selection;
- attrition bias.

Identify threats relevant to the design.

---

# Nonresponse Bias

Low response rate does not automatically prove bias.

High response rate does not automatically eliminate bias.

Assess whether responders differ systematically from nonresponders.

---

# Volunteer Bias

Participants who volunteer may differ from the target population.

This is especially relevant for:

- online surveys;
- lifestyle studies;
- sensitive topics;
- intervention studies.

---

# Referral Bias

Clinic-based recruitment may overrepresent more severe or complex cases.

---

# Spectrum Bias

Diagnostic studies require an appropriate spectrum of disease and non-disease states.

Avoid case-control extremes when the target use population is broader unless justified.

---

# Attrition Bias

Longitudinal studies should compare dropout patterns and preserve retention procedures.

Sampling strategy should anticipate attrition before enrollment.

---

# Sampling Feasibility

Assess:

- population size;
- recruitment rate;
- accessibility;
- consent burden;
- follow-up burden;
- site cooperation;
- laboratory throughput;
- intervention capacity;
- budget;
- timeline.

Use:

- `SAMPLING_FEASIBLE`
- `SAMPLING_FEASIBLE_WITH_ADAPTATION`
- `SAMPLING_FEASIBILITY_UNCERTAIN`
- `SAMPLING_NOT_FEASIBLE`

---

# Feasibility Adaptation

Possible adaptations include:

- additional sites;
- longer recruitment;
- fewer secondary objectives;
- revised recruitment channels;
- staged study;
- pilot phase.

If adaptation changes the target inference, route back to `methodology-architect`.

---

# Ethics in Sampling

Consider:

- equitable participant selection;
- burden distribution;
- vulnerable groups;
- coercion;
- privacy;
- exclusion fairness;
- community sensitivity.

---

# Sampling and Consent

Sampling selection may occur before consent, but data collection requiring consent should follow applicable ethical requirements.

Do not assume access to contact lists permits unrestricted research use.

---

# Privacy

Sampling frames may contain identifiers.

Use minimum necessary access.

---

# Sampling and Instrument Burden

Long or invasive measurement can reduce participation and increase nonresponse.

Coordinate with `instrument-design`.

---

# Sampling and Protocol

`protocol-builder` operationalizes:

- recruitment;
- screening;
- enrollment;
- replacement;
- retention;
- tracking.

Sampling strategy defines the scientific selection logic.

---

# Sampling and Analysis

Sampling architecture should preserve information required for downstream analysis, such as:

- strata;
- cluster IDs;
- weights;
- pairing;
- repeated measures;
- site;
- selection probability.

Do not discard design variables.

---

# Sample Size Calculation Record

When a numerical calculation is eventually performed, preserve:

```yaml
sample_size:
  objective:
  method:
  assumptions:
  effect_or_precision_target:
  alpha:
  power:
  variance:
  event_rate:
  allocation_ratio:
  design_effect:
  attrition:
  finite_population:
  software_or_formula:
  base_required_n:
  recruitment_target:
  sensitivity_analysis:
```

Only include relevant fields.

---

# Sensitivity Analysis for Sample Size

When assumptions are uncertain, compare plausible scenarios.

Do not present a single exact sample size as unquestionable if inputs are uncertain.

---

# Recruitment Target vs Analyzed Sample

Distinguish:

- required analyzed sample;
- enrollment target;
- screening target.

---

# Qualitative Sample Record

Recommended:

```yaml
qualitative_sampling:
  strategy:
  inclusion_logic:
  variation_dimensions:
  initial_target:
  adequacy_rule:
  iterative_sampling:
  saturation_or_information_power:
  stop_rule:
```

---

# Laboratory Replication Record

Recommended:

```yaml
laboratory_sampling:
  experimental_unit:
  biological_replicates:
  batch_replicates:
  technical_replicates:
  repeated_measurements:
  control_units:
  independence_assumption:
```

---

# Sampling Strategy Output

Recommended internal structure:

```yaml
sampling_strategy:
  status:
  target_population:
  source_population:
  accessible_population:
  sampling_frame:
  sampling_unit:
  unit_of_observation:
  unit_of_analysis:
  unit_of_assignment:
  unit_of_inference:
  sampling_method:
  strata:
  clusters:
  sites:
  eligibility:
  recruitment_source:
  recruitment_window:
  sample_size_basis:
  sample_size_inputs:
  design_effect:
  attrition:
  nonresponse:
  replacement:
  representativeness:
  bias_risks:
  feasibility:
  ethics:
  downstream_analysis_requirements:
```

Unknown fields remain unknown.

---

# Minimal Output

For a simple request provide:

## Target Population
[...]

## Sampling Method
[...]

## Sampling Unit
[...]

## Sample-Size Basis
[...]

## Major Bias Risk
[...]

## Recruitment Target
[...]

## Next Step
[...]

---

# Comprehensive Output

When full sampling architecture is requested:

## A. Target Population
[...]

## B. Source Population
[...]

## C. Accessible Population
[...]

## D. Sampling Frame
[...]

## E. Sampling Unit
[...]

## F. Unit Structure
[...]

## G. Sampling Method
[...]

## H. Stratification / Clustering
[...]

## I. Eligibility
[...]

## J. Recruitment Source
[...]

## K. Sample-Size Rationale
[...]

## L. Attrition / Nonresponse
[...]

## M. Representativeness
[...]

## N. Bias Risks
[...]

## O. Feasibility
[...]

## P. Ethics
[...]

## Q. Protocol Handoff
[...]

## R. Analysis Handoff
[...]

---

# Relationship with Methodology Architect

`methodology-architect` defines what population, units, comparison, and inference the study requires.

`sampling-strategy` determines how units are selected and how sample adequacy is justified.

Use:

```text
methodology-architect
      ↓
sampling-strategy
```

---

# Relationship with Protocol Builder

`sampling-strategy` defines scientific selection logic.

`protocol-builder` operationalizes:

- screening;
- recruitment;
- enrollment;
- retention;
- replacement.

---

# Relationship with Instrument Design

Measurement burden, respondent eligibility, specimen availability, and administration mode can affect sampling feasibility.

Coordinate when needed.

---

# Relationship with Analysis Planner

Provide `analysis-planner` with:

- sampling design;
- strata;
- clusters;
- weights;
- repeated measures;
- pairing;
- site;
- attrition;
- event counts;
- selection probabilities when relevant.

---

# Relationship with Research Question Builder

The RQ determines the inference target.

Sampling must not redefine the RQ silently.

---

# Relationship with Problem-Solving Approach

The problem-solving approach determines the type of evidence required.

Sampling determines how suitable units are obtained to generate that evidence.

---

# Design-Specific Guardrails

## Descriptive population studies

Prefer probability-based selection when population prevalence or distribution is the primary inference.

## Causal experiments

Representative sampling and random assignment solve different problems.

## Prediction studies

Sampling should represent the population and outcome spectrum in which prediction will be used.

## Diagnostic studies

Ensure adequate disease and non-disease spectrum.

## Qualitative studies

Prioritize information richness and relevance over statistical representativeness.

## Laboratory studies

Preserve true experimental-unit independence.

## Systematic reviews

Coverage comes from search and eligibility architecture, not target article counts.

---

# Software Independence

Do not let G*Power, SmartPLS, SPSS, Jamovi, R, Python, or any calculator determine the sampling strategy by itself.

Software may calculate after scientific assumptions are defined.

---

# G*Power Guard

G*Power can implement some power calculations.

It does not determine:

- target population;
- design;
- effect-size justification;
- clustering;
- attrition;
- sampling frame;
- qualitative adequacy.

---

# SEM / PLS-SEM Guard

Do not start with:

> What is the minimum sample for SEM?

Start with:

> What parameters and inferences must the study estimate, with what design and measurement quality?

---

# Large-Sample Myth

Large N does not automatically fix:

- selection bias;
- poor measurement;
- confounding;
- invalid design;
- unrepresentative sampling;
- pseudoreplication.

---

# Small-Sample Myth

Small N is not automatically invalid.

Adequacy depends on:

- design;
- effect;
- precision;
- measurement;
- unit structure;
- evidence goal.

---

# Publication Strategy Independence

Do not inflate or reduce sample size merely to imitate target-journal articles.

Target-journal norms can inform expectations but cannot replace scientific justification.

APC status has no role in sampling.

---

# Avoid These Behaviors

Do not:

- use convenience sampling while claiming national representativeness;
- call all available participants a census when the target population is broader;
- calculate sample size before defining the unit of analysis;
- count technical replicates as independent units;
- use the 10-times rule as the sole PLS-SEM sample-size justification;
- use arbitrary qualitative sample thresholds;
- ignore clustering;
- ignore attrition;
- ignore nonresponse;
- ignore outcome event rates;
- invent effect sizes;
- oversample subgroups without documenting unequal probabilities;
- replace nonresponders with convenient participants silently;
- treat random assignment as proof of representative sampling;
- treat very large administrative datasets as unbiased samples;
- claim saturation without analytic evidence;
- change target population after recruitment to make the sample appear appropriate.

---

# Stop Conditions

Do not classify sampling as ready when:

- target population is undefined;
- source population is incompatible with the intended inference;
- unit of analysis is unclear;
- sampling frame is materially incomplete and no mitigation is planned;
- probability claims are made from non-probability selection without justification;
- sample-size assumptions are invented;
- cluster structure is ignored;
- technical replicates are counted as independent;
- attrition threatens longitudinal validity without mitigation;
- qualitative adequacy has no stopping logic;
- recruitment is ethically problematic;
- feasibility adaptations materially change the inference.

Use:

- `RETURN_TO_METHODOLOGY_ARCHITECT`
- `RETURN_TO_PROTOCOL_BUILDER`
- `RETURN_TO_INSTRUMENT_DESIGN`
- `SAMPLING_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`sampling-strategy` succeeds when the approved study architecture has been translated into a scientifically defensible plan that explicitly defines the target population, source and accessible populations, sampling frame, sampling unit, unit of observation, unit of analysis, unit of assignment and inference where relevant, selection mechanism, stratification or clustering, eligibility, recruitment source, sample-size basis, attrition and nonresponse assumptions, representativeness limits, bias risks, feasibility, and ethical safeguards, while preserving true experimental independence and providing the design information required by `protocol-builder`, `instrument-design`, and downstream `analysis-planner` without allowing convenience, arbitrary rules, software defaults, or publication strategy to redefine the intended inference.
