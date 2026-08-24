---
name: instrument-design
description: Design, select, adapt, validate, and document measurement instruments and data-collection tools that operationalize the constructs, outcomes, exposures, phenomena, experiences, laboratory properties, or performance indicators required by an approved methodology. Use when the study design and measurement requirements are sufficiently clear and the researcher needs to determine whether to reuse, adapt, translate, develop, pilot, validate, calibrate, or quality-control questionnaires, scales, interview guides, observation tools, case report forms, laboratory assays, devices, rubrics, extraction forms, or other measurement systems without letting convenience or software dictate what is measured.
---

# Instrument Design

## Purpose

`instrument-design` determines how the concepts, constructs, outcomes, exposures, experiences, properties, behaviors, events, or performance indicators required by the study will be measured, elicited, observed, recorded, or extracted validly and reproducibly.

Its central question is:

> What measurement or data-collection instrument can capture the intended scientific concept with sufficient validity, reliability, precision, interpretability, feasibility, and contextual appropriateness?

This skill operates after the research question and methodology are sufficiently stable.

It may support:

- selecting an existing instrument;
- adapting an existing instrument;
- translating an instrument;
- developing a new instrument;
- designing interview or observation guides;
- designing case report forms;
- specifying laboratory assays;
- specifying measurement devices;
- designing extraction forms;
- planning pilot testing;
- planning validation;
- documenting measurement quality.

It does not select the final statistical analysis.

It does not invent constructs.

It does not automatically prefer a familiar questionnaire.

It does not treat software output as measurement validity.

---

# Core Principle

Use:

> Construct before item. Outcome before instrument. Measurement purpose before software.

Do not begin with:

- a questionnaire already available;
- a scale used in prior theses;
- a device simply because the laboratory owns it;
- SmartPLS indicators;
- SPSS variables;
- Jamovi columns;
- a convenient survey platform.

Begin with:

> What exactly must be measured or elicited to answer the research question?

---

# Position in the Framework

Preferred flow:

```text
Research Question
      ↓
conceptual / theoretical logic
when required
      ↓
problem-solving-approach
      ↓
methodology-architect
      ↓
instrument-design
      │
      ├───────────────┐
      ▼               ▼
protocol-builder  sampling-strategy
      │               │
      └───────┬───────┘
              ↓
        DESIGN READY
              ↓
        analysis-planner
```

Instrument development may interact iteratively with protocol and sampling.

---

# Required Upstream Context

Use established information from:

- `research-question-builder`;
- `theoretical-framework`;
- `hypothesis-builder`;
- `conceptual-framework`;
- `problem-solving-approach`;
- `methodology-architect`;
- `sampling-strategy` when available;
- `protocol-builder` when available.

Do not ask the researcher to repeat information already established.

Minimum useful context normally includes:

- primary RQ;
- construct / outcome / phenomenon;
- role of each measurement;
- population or specimen;
- timing;
- setting;
- language and culture;
- required level of precision;
- existing instruments if known;
- feasibility constraints.

---

# Instrument Readiness Gate

Classify:

- `READY_FOR_INSTRUMENT_DESIGN`
- `CONSTRUCT_DEFINITION_INCOMPLETE`
- `OUTCOME_DEFINITION_INCOMPLETE`
- `MEASUREMENT_ROLE_UNCLEAR`
- `EXISTING_INSTRUMENT_REVIEW_REQUIRED`
- `INSTRUMENT_ALREADY_AVAILABLE`
- `INSTRUMENT_REQUIRES_ADAPTATION`
- `NEW_INSTRUMENT_REQUIRED`
- `INSTRUMENT_REQUIRES_VALIDATION`
- `INSTRUMENT_REQUIRES_REASSESSMENT`

Do not develop items before defining the measurement target.

---

# Measurement Target

First classify what is being measured.

Possible targets include:

- latent construct;
- observed variable;
- clinical outcome;
- behavioral outcome;
- educational outcome;
- biological marker;
- pharmacological parameter;
- laboratory property;
- formulation property;
- performance indicator;
- experience;
- perception;
- attitude;
- knowledge;
- skill;
- process;
- implementation outcome;
- policy characteristic;
- event;
- document property.

---

# Measurement Role

Classify each measurement as:

- `PRIMARY_OUTCOME`
- `SECONDARY_OUTCOME`
- `EXPOSURE`
- `INTERVENTION_FIDELITY`
- `PREDICTOR`
- `MEDIATOR`
- `MODERATOR`
- `CONFOUNDER`
- `COVARIATE`
- `PROCESS_MEASURE`
- `SAFETY_MEASURE`
- `CONTEXT_MEASURE`
- `QUALITATIVE_PHENOMENON`
- `LABORATORY_PROPERTY`
- `VALIDATION_TARGET`
- `REFERENCE_STANDARD`

The role affects required measurement quality.

---

# Conceptual Definition

Before operationalization, define:

```yaml
measurement_concept:
  name:
  conceptual_definition:
  theoretical_basis:
  domain:
  boundaries:
  exclusions:
  expected_dimensions:
  role_in_study:
```

Do not allow the instrument to redefine the construct silently.

---

# Operational Definition

Translate the concept into observable evidence.

Record:

```yaml
operational_definition:
  concept:
  observable_indicator:
  measurement_method:
  unit:
  scale:
  timing:
  interpretation:
```

---

# Construct-to-Indicator Mapping

For latent constructs, map:

```text
Construct
   ↓
Dimensions
   ↓
Indicators / Items
   ↓
Response Format
   ↓
Scoring
```

Do not add indicators merely to satisfy software requirements.

---

# Existing Instrument First

Before developing a new instrument, search for suitable existing instruments.

Assess:

- conceptual fit;
- population fit;
- language;
- cultural context;
- validity evidence;
- reliability evidence;
- licensing;
- accessibility;
- burden;
- scoring;
- current usage.

Use:

- `EXISTING_INSTRUMENT_SUITABLE`
- `EXISTING_INSTRUMENT_REQUIRES_ADAPTATION`
- `EXISTING_INSTRUMENT_INADEQUATE`
- `NO_SUITABLE_EXISTING_INSTRUMENT_FOUND`

Do not create a new instrument merely for novelty.

---

# Instrument Search Logic

When scholarly evidence is needed for instrument selection, use Scopus-first or discipline-appropriate scholarly search.

Possible evidence includes:

- original development paper;
- validation studies;
- cross-cultural validation;
- measurement-invariance studies;
- systematic reviews of instruments;
- reliability studies;
- responsiveness studies.

Do not rely only on secondary citations when original measurement papers are recoverable.

---

# Instrument Provenance

For every existing instrument record:

```yaml
instrument_provenance:
  instrument_name:
  original_author:
  original_year:
  original_population:
  construct:
  language:
  licensing:
  source:
  adaptation_history:
```

Do not fabricate instrument ownership or licensing status.

---

# Permission and Licensing

Some instruments require permission or licensing.

Classify:

- `OPEN_USE`
- `PERMISSION_REQUIRED`
- `LICENSE_REQUIRED`
- `STATUS_UNCLEAR`

Do not assume academic use is automatically free.

---

# New Instrument Decision

Develop a new instrument only when:

- no suitable instrument exists;
- existing instruments do not cover the construct;
- the context introduces meaningful measurement differences;
- the phenomenon is genuinely new;
- available tools are methodologically inadequate.

Document why adaptation is insufficient.

---

# Instrument Type

Possible instrument forms include:

- questionnaire;
- scale;
- checklist;
- rubric;
- test;
- interview guide;
- focus-group guide;
- observation guide;
- case report form;
- extraction form;
- laboratory assay;
- device;
- sensor;
- imaging protocol;
- scoring algorithm;
- coding frame;
- performance task.

---

# Questionnaire Design

Questionnaires may measure:

- attitudes;
- beliefs;
- experiences;
- symptoms;
- behaviors;
- knowledge;
- satisfaction;
- implementation outcomes;
- service use;
- self-reported outcomes.

Questionnaire design requires conceptual clarity before item writing.

---

# Item Generation

Possible item sources:

- theory;
- literature;
- existing instruments;
- qualitative interviews;
- focus groups;
- expert input;
- patient / participant input;
- clinical practice;
- policy definitions.

Use multiple sources where appropriate.

---

# Item Writing Principles

Items should usually be:

- conceptually specific;
- understandable;
- unambiguous;
- focused on one idea;
- appropriate to respondent literacy;
- appropriate to recall period;
- neutral where possible;
- free from unnecessary jargon.

Avoid:

- double-barreled items;
- leading items;
- vague quantifiers;
- unnecessary negatives;
- hidden assumptions;
- culturally inappropriate wording.

---

# Double-Barreled Item Guard

Example of problematic item:

> The service was fast and friendly.

Speed and friendliness are different constructs.

Split them if both matter.

---

# Leading Question Guard

Avoid wording that suggests the desired answer.

---

# Double Negative Guard

Avoid unnecessary cognitive complexity.

---

# Recall Period

Specify recall period when relevant.

Examples:

- today;
- past 7 days;
- past month;
- current semester;
- last clinical episode.

Do not mix recall periods silently across items.

---

# Response Format

Possible formats include:

- binary;
- categorical;
- ordinal;
- Likert-type;
- numeric;
- visual analog;
- frequency;
- intensity;
- open-ended;
- ranking;
- forced choice.

Response format must match the construct and respondent capability.

---

# Likert-Type Items

Distinguish:

- individual Likert-type item;
- multi-item Likert scale.

Do not call every ordinal response a validated scale.

---

# Response Anchors

Anchors should be:

- mutually interpretable;
- ordered where intended;
- balanced when scientifically appropriate;
- consistent.

Avoid vague anchors unless justified.

---

# Neutral Option

A neutral midpoint may or may not be appropriate.

Do not remove it solely to force decisions.

---

# "Not Applicable" Option

Use when respondents may legitimately lack relevant experience.

Do not force inaccurate responses.

---

# Knowledge Tests

For knowledge instruments define:

- content domain;
- blueprint;
- cognitive level;
- scoring;
- item difficulty;
- distractor quality;
- guessing considerations.

---

# Educational Rubrics

Rubrics should define:

- criterion;
- performance level;
- observable evidence;
- scoring rule.

Avoid vague descriptors such as "good" without operational meaning.

---

# Performance Assessment

For skills or competency, direct performance assessment may be superior to self-report.

Examples:

- OSCE;
- teaching demonstration;
- laboratory procedure;
- practical task;
- simulation.

---

# Self-Report Guard

Self-report measures perceived or reported behavior.

It does not necessarily measure actual behavior or competence.

---

# Proxy Reporting

When proxy respondents are used, document:

- reason;
- relationship;
- proxy validity;
- potential disagreement.

---

# Interview Guide Design

For qualitative interviews define:

- research purpose;
- topic domains;
- opening questions;
- core questions;
- prompts;
- probes;
- closing questions.

Questions should support depth rather than force predetermined categories.

---

# Interview Question Guard

Avoid overloading interviews with:

- yes/no questions;
- leading questions;
- jargon;
- multiple concepts in one question.

---

# Semi-Structured Interviews

Use a core guide plus flexible probing.

Preserve comparability without suppressing emergent meaning.

---

# Focus Group Guide

Design for group interaction.

Include:

- opening;
- transition;
- key questions;
- probes;
- closing synthesis.

Avoid questions that require disclosure unsafe for a group setting.

---

# Observation Instrument

Observation tools may be:

- structured;
- semi-structured;
- open field notes.

Define:

- event;
- behavior;
- unit;
- frequency;
- duration;
- context;
- observer role.

---

# Structured Observation

Use explicit categories and decision rules.

Train observers.

---

# Qualitative Observation

Preserve context and reflexivity.

Do not force all observations into predetermined categories when discovery is the goal.

---

# Case Report Form

CRFs should capture only data required for:

- eligibility;
- exposure / intervention;
- outcomes;
- safety;
- confounding;
- protocol adherence.

Do not collect unnecessary identifiers.

---

# Extraction Form

For reviews or secondary data, extraction forms should define:

- source;
- variable;
- definition;
- unit;
- coding;
- missing handling;
- provenance.

---

# Laboratory Instrument Design

Laboratory measurement requires specification of:

- analyte or property;
- method principle;
- equipment;
- calibration;
- standard;
- detection limit;
- quantification limit where relevant;
- precision;
- accuracy;
- controls;
- repeat rules.

---

# Assay Selection

Choose assays based on:

- biological relevance;
- analytical validity;
- sample type;
- sensitivity;
- specificity;
- precision;
- equipment;
- cost;
- reproducibility.

---

# Analytical Validation

Depending on the assay, possible characteristics include:

- accuracy;
- precision;
- specificity;
- selectivity;
- linearity;
- range;
- detection limit;
- quantification limit;
- robustness;
- recovery;
- stability.

Do not require every characteristic for every method without context.

---

# Device-Based Measurement

For devices define:

- manufacturer;
- model;
- firmware when relevant;
- calibration;
- measurement range;
- resolution;
- precision;
- placement;
- operator;
- repeat rules.

---

# Sensor Measurement

Sensor-derived data require:

- sampling frequency;
- synchronization;
- wear or exposure time;
- missing-data handling;
- calibration;
- preprocessing provenance.

---

# Imaging Measurement

Define:

- modality;
- acquisition protocol;
- segmentation or reading;
- assessor;
- blinding;
- scoring;
- inter-rater needs;
- image quality criteria.

---

# Biomarker Measurement

Define:

- biomarker;
- specimen;
- assay;
- timing;
- biological variability;
- pre-analytical conditions;
- reference or calibration.

---

# Pharmacokinetic Measurement

Define:

- analyte;
- matrix;
- sampling time;
- assay;
- quantification range;
- actual sample time;
- handling;
- storage.

---

# Genetic / Genomic Measurement

Define:

- gene / variant;
- platform;
- specimen;
- extraction;
- genotype calling;
- QC;
- missing call threshold;
- duplicate or concordance checks;
- reference genome build where relevant.

---

# Formulation Measurement

Possible critical quality attributes include:

- pH;
- viscosity;
- spreadability;
- adhesion;
- particle size;
- drug content;
- moisture;
- ash;
- swelling;
- release;
- stability;
- antimicrobial activity.

Measurement method must be linked to the scientific question.

---

# Microbiological Measurement

Specify:

- endpoint;
- assay type;
- organism;
- inoculum;
- medium;
- incubation;
- control;
- unit;
- measurement rule.

Distinguish total inhibition diameter from net inhibition zone if subtraction is applied.

---

# Reference Standard

When a reference standard exists, define:

- standard;
- rationale;
- traceability;
- limitations.

---

# Gold Standard Guard

Do not call a comparator a "gold standard" unless that status is scientifically established.

Prefer:

`REFERENCE_STANDARD`

when appropriate.

---

# Content Validity

Content validity asks whether the instrument adequately represents the construct domain.

Possible evidence includes:

- expert review;
- target-user review;
- content validity index;
- qualitative feedback.

Do not rely solely on statistical factor analysis for content validity.

---

# Expert Panel

Define:

- expertise criteria;
- number;
- independence;
- rating task;
- disagreement handling.

Do not select experts merely by availability.

---

# Face Validity

Face validity concerns apparent relevance and clarity.

It is not sufficient evidence of construct validity.

---

# Cognitive Interviewing

Use cognitive interviews to examine:

- interpretation;
- comprehension;
- recall;
- response process;
- wording.

Especially useful during questionnaire adaptation or new item development.

---

# Pilot Testing

Pilot testing may assess:

- clarity;
- burden;
- timing;
- missing responses;
- administration;
- technical problems;
- ceiling / floor patterns.

A pilot is not automatically a full validation study.

---

# Reliability

Reliability concerns consistency.

Possible forms include:

- internal consistency;
- test-retest;
- inter-rater;
- intra-rater;
- parallel forms.

Select the form appropriate to the measurement process.

---

# Internal Consistency

Internal consistency is relevant for multi-item scales intended to measure a coherent construct.

Do not maximize alpha by adding redundant items.

---

# Cronbach Alpha Guard

Cronbach's alpha is not proof of validity.

High alpha may reflect redundancy.

Do not use alpha as the only reliability evidence.

---

# Omega

McDonald's omega or other reliability coefficients may be preferable in some measurement models.

Final statistical choice belongs downstream.

---

# Test-Retest Reliability

Specify:

- interval;
- expected construct stability;
- conditions.

Too short may inflate memory effects.

Too long may permit true change.

---

# Inter-Rater Reliability

Use when scoring depends on raters.

Define:

- rater training;
- scoring rules;
- independent rating;
- disagreement process.

---

# Measurement Error

Distinguish:

- random error;
- systematic error.

Reliability primarily concerns random consistency.

Validity concerns whether intended meaning is captured.

---

# Construct Validity

Construct validity may include evidence from:

- structural validity;
- convergent evidence;
- discriminant evidence;
- known-groups evidence;
- hypothesis testing;
- relationships with external variables.

---

# Convergent Validity

Assess whether measures expected to relate actually relate.

Do not define validity only by one threshold.

---

# Discriminant Validity

Assess whether conceptually distinct constructs are sufficiently distinguishable.

Do not rely blindly on one metric.

---

# Criterion Validity

Use when a defensible external criterion exists.

Possible forms:

- concurrent;
- predictive.

---

# Structural Validity

Evaluate whether the internal structure matches the intended dimensional model.

Possible tools include:

- exploratory factor analysis;
- confirmatory factor analysis;
- item-response models.

Method selection belongs downstream.

---

# Measurement Invariance

When comparing groups or time points, determine whether the instrument functions comparably.

Possible levels may include:

- configural;
- metric;
- scalar;
- strict;

depending on framework.

Do not compare latent means without considering invariance when relevant.

---

# Cross-Cultural Validity

Adaptation across languages or cultures should preserve conceptual meaning, not just literal wording.

---

# Translation

Possible process:

```text
Permission
  ↓
Forward Translation
  ↓
Reconciliation
  ↓
Back Translation
  ↓
Expert Review
  ↓
Cognitive Testing
  ↓
Pilot
  ↓
Validation
```

Exact process may vary.

Do not treat back-translation alone as proof of equivalence.

---

# Translation Team

Prefer translators with complementary expertise:

- language;
- subject matter;
- measurement;
- cultural context.

---

# Semantic Equivalence

Assess whether words convey comparable meaning.

---

# Idiomatic Equivalence

Adapt idioms rather than translating literally.

---

# Experiential Equivalence

Ensure situations or examples are relevant to the target culture.

---

# Conceptual Equivalence

The underlying construct must remain meaningful in the target context.

---

# Adaptation Documentation

Record every adapted element:

```yaml
adaptation:
  original_item:
  adapted_item:
  rationale:
  reviewer:
  evidence:
```

---

# Scoring

Define:

- item coding;
- reverse coding;
- subscales;
- total score;
- missing-item rule;
- transformation;
- interpretation.

Do not invent scoring systems for established instruments.

---

# Reverse-Coded Items

Use carefully.

Excessive reverse wording can create method effects and confusion.

---

# Missing Item Scoring

Follow validated scoring instructions where available.

Do not improvise prorating rules.

---

# Cutoffs

Cutoff scores require empirical or clinical justification.

Do not create arbitrary "low / medium / high" categories from continuous scores.

---

# Categorization Guard

Avoid unnecessary categorization of continuous measures.

Categorization may lose information.

---

# Floor and Ceiling Effects

Check whether many respondents cluster at minimum or maximum.

This may limit responsiveness or discrimination.

---

# Responsiveness

Responsiveness concerns ability to detect meaningful change.

Important for intervention or longitudinal measurement.

---

# Minimal Important Change

When available, define meaningful change separately from statistical significance.

---

# Interpretability

Users should know what scores mean.

Possible aids:

- normative values;
- clinical thresholds;
- percentile ranks;
- minimally important difference;
- category descriptions.

Do not invent interpretation rules.

---

# Measurement Burden

Assess:

- completion time;
- cognitive burden;
- emotional burden;
- physical burden;
- specimen burden;
- repeated measurement burden.

Burden can affect missingness and retention.

---

# Mode of Administration

Possible modes:

- paper;
- online;
- interviewer-administered;
- telephone;
- device-based;
- self-administered;
- laboratory;
- observation.

Mode may affect responses.

---

# Mode Equivalence

If multiple administration modes are used, consider whether results are comparable.

---

# Order Effects

Question order can influence response.

Randomization or structured ordering may be needed.

---

# Survey Logic

For electronic instruments define:

- branching;
- skip logic;
- required fields;
- validation;
- duplicate prevention;
- save / resume.

---

# Data Type

For each variable define intended type:

- binary;
- nominal;
- ordinal;
- integer;
- continuous;
- date/time;
- text;
- image;
- sequence;
- categorical code.

Do not let software infer important variable meaning blindly.

---

# Unit

Always record measurement unit when relevant.

Examples:

- mg/L;
- mm;
- seconds;
- kg;
- score points;
- CFU/mL;
- percentage.

---

# Measurement Range

Define plausible and valid range.

Use data validation where possible.

---

# Detection Limit

For laboratory methods, distinguish:

- below detection;
- below quantification;
- true zero.

Do not code all three identically.

---

# Precision

Define required measurement resolution.

Do not report more decimal places than the method supports.

---

# Calibration

Specify calibration needs for:

- scales;
- balances;
- pH meters;
- spectrometers;
- viscometers;
- pipettes;
- sensors;
- imaging devices.

---

# Standardization

Standardize measurement conditions when they affect results.

Examples:

- temperature;
- fasting;
- posture;
- time of day;
- incubation time;
- sample preparation;
- observer distance.

---

# Rater Training

For subjective measurement define:

- training;
- examples;
- calibration;
- competency threshold;
- refresher training.

---

# Inter-Rater Drift

Repeated measurement over time may cause rater drift.

Monitor and recalibrate where necessary.

---

# Instrument Versioning

Record:

- version;
- date;
- language;
- adaptation status;
- scoring version.

Do not mix instrument versions silently.

---

# Form Version Control

For CRFs, survey forms, or interview guides use explicit versions.

---

# Measurement Timing

Measurement timing must align with:

- exposure;
- intervention;
- mechanism;
- expected response;
- follow-up;
- learning cycle;
- clinical process;
- stability period.

---

# Baseline Measurement

Baseline should occur before intervention or relevant exposure when required.

---

# Repeated Measurement

Specify whether the same instrument is repeated.

Consider:

- practice effects;
- recall;
- burden;
- responsiveness;
- interval.

---

# Instrument-Blinding

When possible, assessors may be blinded to:

- intervention;
- group;
- exposure;
- prior result.

---

# Common Method Bias Awareness

When predictor and outcome are measured from the same person, same instrument, and same time, common method effects may arise.

Potential design safeguards include:

- temporal separation;
- different sources;
- different methods;
- procedural separation;
- neutral wording.

Do not assume statistical post-hoc tests fully solve design-stage bias.

---

# Social Desirability Bias

Sensitive self-report may require:

- privacy;
- neutral wording;
- anonymous response;
- indirect questioning.

---

# Recall Bias

Reduce with:

- appropriate recall period;
- records;
- event anchors;
- contemporaneous collection.

---

# Interviewer Bias

Use training and standardized core procedures.

---

# Observer Bias

Use explicit criteria, training, and blinding where possible.

---

# Misclassification

For categorical measures assess:

- sensitivity;
- specificity;
- threshold;
- adjudication;
- repeat testing.

---

# Outcome Adjudication

For complex outcomes, define:

- adjudication criteria;
- adjudicators;
- blinding;
- disagreement resolution.

---

# Measurement Bias Architecture

For each important measurement record:

```yaml
measurement_bias:
  source:
  direction:
  affected_variable:
  prevention:
  residual_risk:
```

---

# Instrument Validity Matrix

When useful:

| Instrument | Target | Validity Evidence | Reliability | Population Fit | Adaptation Need | Status |
|---|---|---|---|---|---|---|

---

# Item-Construct Matrix

When useful:

| Construct | Dimension | Item / Indicator | Evidence Source | Response Format |
|---|---|---|---|---|

---

# Outcome Measurement Matrix

| Outcome | Operational Definition | Instrument / Assay | Timing | Assessor | Unit |
|---|---|---|---|---|---|

---

# Qualitative Guide Matrix

| Topic Domain | Core Question | Probe | RQ Link |
|---|---|---|---|

---

# Measurement Validation Roadmap

Possible phased plan:

```text
Conceptual Definition
      ↓
Existing Instrument Review
      ↓
Adapt / Develop
      ↓
Content Evaluation
      ↓
Cognitive Testing
      ↓
Pilot
      ↓
Reliability
      ↓
Structural / Construct Validity
      ↓
External / Cross-Group Validation
```

Not every instrument requires every phase.

---

# Instrument Development Phases

Use:

- `DEFINITION`
- `ITEM_GENERATION`
- `CONTENT_VALIDATION`
- `RESPONSE_PROCESS_TESTING`
- `PILOT`
- `STRUCTURAL_VALIDATION`
- `RELIABILITY`
- `CRITERION_VALIDATION`
- `RESPONSIVENESS`
- `INVARIANCE`
- `EXTERNAL_VALIDATION`

---

# Instrument Status

Classify:

- `READY_FOR_USE`
- `READY_WITH_PERMISSION`
- `READY_WITH_ADAPTATION`
- `READY_AFTER_PILOT`
- `READY_AFTER_VALIDATION`
- `DEVELOPMENT_REQUIRED`
- `INSTRUMENT_NOT_SUITABLE`
- `MEASUREMENT_PLAN_INCOMPLETE`

---

# Existing Instrument Adoption

When adopting without modification, verify:

- population;
- language;
- scoring;
- validity evidence;
- administration mode;
- license.

Do not assume prior validation in another population guarantees validity here.

---

# Instrument Adaptation

Adaptation may involve:

- wording;
- language;
- examples;
- response format;
- cultural context;
- mode.

Every substantive change may require new validation evidence.

---

# Instrument Modification Guard

Deleting, adding, or rewording items can alter:

- dimensionality;
- reliability;
- validity;
- comparability.

Do not call a heavily modified instrument "the same validated scale."

---

# Short Forms

Short forms may reduce burden.

Use only if validity evidence supports the intended use.

---

# Composite Scores

Composite scores require conceptual and empirical justification.

Do not average unrelated items merely because software allows it.

---

# Formative Measurement

For formative constructs, indicators may define rather than reflect the construct.

Do not apply reflective measurement logic automatically.

---

# Reflective Measurement

For reflective constructs, indicators are manifestations of an underlying construct.

Measurement assumptions should align with theory.

---

# Formative vs Reflective Guard

Do not classify measurement direction based only on SEM software conventions.

---

# Single-Item Measures

Single-item measures may be appropriate for simple, concrete concepts.

They are usually weaker for complex multidimensional constructs.

---

# Proxy Variables

A proxy may be used when direct measurement is unavailable.

Document:

- why;
- validity;
- limitations.

---

# Derived Variables

If variables are calculated from multiple inputs, document:

- formula;
- source variables;
- timing;
- unit;
- assumptions.

---

# Algorithmic Scores

For risk scores or algorithms preserve:

- original formula;
- coefficient version;
- input definitions;
- cutoff;
- missing handling.

Do not recalculate differently without labeling adaptation.

---

# Reference Data

If normative or reference values are used, verify population relevance.

---

# Cultural Adaptation

Cultural adaptation may be necessary even within the same language.

---

# Literacy Adaptation

For low-literacy populations consider:

- interviewer administration;
- plain language;
- pictorial support;
- audio.

Do not change conceptual meaning merely to simplify wording.

---

# Accessibility

Consider:

- vision;
- hearing;
- motor limitations;
- cognitive impairment;
- language barriers.

Accessibility changes should preserve measurement intent.

---

# Children

For pediatric or education contexts, adapt:

- language;
- response format;
- developmental level;
- proxy use;
- assent.

---

# Older Adults

Consider:

- vision;
- hearing;
- fatigue;
- cognitive burden;
- medication effects;
- digital literacy.

---

# Sensitive Topics

Use privacy-preserving collection.

Avoid unnecessary identifiers.

---

# Genetic Data

Genetic measurement requires:

- sample identity;
- assay QC;
- variant definition;
- secure data;
- population context.

---

# Electronic Data Capture

For electronic forms specify:

- platform;
- field validation;
- version;
- access control;
- export format;
- audit trail;
- backup.

---

# Paper-to-Digital Conversion

If paper forms are digitized, define:

- data entry;
- verification;
- source retention;
- correction.

---

# Barcode / QR Use

May improve specimen or form identification.

Do not encode unnecessary personal identifiers.

---

# Data Dictionary

Every final instrument set should support a data dictionary.

Recommended fields:

```yaml
variable:
  name:
  label:
  concept:
  role:
  type:
  unit:
  coding:
  missing_code:
  source:
  timing:
  instrument_version:
```

---

# Naming Convention

Variable names should be:

- stable;
- unique;
- machine-readable;
- human-interpretable.

Avoid ambiguous names such as `Q1` when durable semantic names are feasible.

---

# Missing Codes

Define missing categories when relevant:

- not answered;
- not applicable;
- not measured;
- below detection;
- unknown.

Do not collapse different missing reasons into zero.

---

# Instrument Documentation

Preserve:

- instrument;
- version;
- instructions;
- scoring;
- permission;
- validation evidence;
- adaptation notes;
- administration protocol;
- data dictionary.

---

# Quality Control

Instrument-level QC may include:

- calibration;
- pilot;
- training;
- duplicate measurement;
- logic checks;
- range checks;
- inter-rater checks;
- assay controls;
- version control.

---

# Protocol Handoff

Provide `protocol-builder` with:

- instrument name;
- administration conditions;
- responsible role;
- timing;
- instructions;
- scoring;
- calibration;
- repeat rules;
- storage;
- quality checks.

---

# Sampling Handoff

Provide `sampling-strategy` with information about:

- respondent burden;
- specimen needs;
- subgroup validation;
- rater needs;
- repeated measurement;
- pilot sample;
- validation sample.

---

# Analysis Handoff

Provide `analysis-planner` with:

- variable roles;
- measurement scales;
- score construction;
- latent structure;
- repeated measures;
- reliability context;
- validation status;
- missing codes;
- limits of detection;
- clustering by rater or device.

Do not choose analysis here.

---

# Instrument Research Passport

Recommended internal structure:

```yaml
instrument_design:
  status:
  construct_or_outcome:
  measurement_role:
  conceptual_definition:
  operational_definition:
  instrument_type:
  existing_instrument:
  provenance:
  licensing:
  language:
  cultural_context:
  adaptation_need:
  development_need:
  content_validity:
  cognitive_testing:
  pilot:
  reliability:
  structural_validity:
  criterion_validity:
  responsiveness:
  invariance:
  administration_mode:
  timing:
  scoring:
  missing_rules:
  burden:
  quality_control:
  protocol_handoff:
  sampling_handoff:
  analysis_handoff:
```

Unknown fields remain unknown.

---

# Minimal Output

For a simple request provide:

## Measurement Target
[...]

## Recommended Instrument
[...]

## Use / Adapt / Develop
[...]

## Required Validation
[...]

## Administration
[...]

## Scoring
[...]

## Next Step
[...]

---

# Comprehensive Output

When full instrument architecture is requested:

## A. Measurement Target
[...]

## B. Conceptual Definition
[...]

## C. Operational Definition
[...]

## D. Measurement Role
[...]

## E. Existing Instrument Review
[...]

## F. Instrument Decision
[...]

## G. Item / Indicator Structure
[...]

## H. Response Format
[...]

## I. Administration
[...]

## J. Translation / Adaptation
[...]

## K. Content Validity
[...]

## L. Cognitive Testing
[...]

## M. Pilot
[...]

## N. Reliability
[...]

## O. Construct / Criterion Validity
[...]

## P. Responsiveness / Invariance
[...]

## Q. Scoring
[...]

## R. Measurement Bias
[...]

## S. Burden
[...]

## T. Quality Control
[...]

## U. Data Dictionary
[...]

## V. Protocol Handoff
[...]

## W. Sampling Handoff
[...]

## X. Analysis Handoff
[...]

---

# Relationship with Methodology Architect

`methodology-architect` defines what must be measured.

`instrument-design` determines how valid measurement will be achieved.

Use:

```text
methodology-architect
      ↓
instrument-design
```

---

# Relationship with Conceptual Framework

`conceptual-framework` defines constructs, variables, mechanisms, and relationships.

`instrument-design` operationalizes those constructs without redefining them.

---

# Relationship with Theoretical Framework

Theory may define the domain or dimensions of a construct.

Instrument design should preserve theoretical meaning.

---

# Relationship with Hypothesis Builder

Hypotheses may determine which variables require precise, reliable, temporally appropriate measurement.

---

# Relationship with Protocol Builder

`instrument-design` specifies the tool.

`protocol-builder` specifies how it is administered operationally.

---

# Relationship with Sampling Strategy

Sampling affects:

- population fit;
- validation;
- subgroup testing;
- measurement burden;
- rater or specimen availability.

Instrument design may require pilot or validation samples.

---

# Relationship with Analysis Planner

`analysis-planner` must respect:

- measurement scale;
- dimensionality;
- validation status;
- score construction;
- reliability;
- repeated measurement;
- censoring or detection limits.

---

# Relationship with Research Router

Route here when the user asks to:

- create a questionnaire;
- select a validated scale;
- adapt a scale;
- translate an instrument;
- develop an interview guide;
- develop an observation rubric;
- build a CRF;
- design data extraction;
- specify laboratory measurement;
- validate an instrument;
- assess reliability;
- operationalize constructs.

---

# Software Independence

Do not let:

- SmartPLS;
- SPSS;
- Jamovi;
- AMOS;
- Mplus;
- R;
- Python;

determine what the instrument measures.

Software operates on data after measurement decisions are made.

---

# SEM Guard

SEM requires a defensible measurement model.

Do not create items merely to satisfy a minimum indicator count.

---

# PLS-SEM Guard

Do not select formative or reflective measurement solely because SmartPLS asks for a model type.

The direction must follow construct logic.

---

# Cronbach Alpha Guard

Do not retain poor or redundant items solely to increase alpha.

---

# Factor Analysis Guard

Factor analysis does not replace conceptual definition or content validity.

---

# Existing Scale Guard

Do not copy items from copyrighted or licensed scales without checking permitted use.

---

# Translation Guard

Do not present machine translation alone as validated cross-cultural adaptation.

---

# Questionnaire Length Guard

Longer is not automatically more rigorous.

Minimize burden while preserving construct coverage.

---

# Item Deletion Guard

Do not delete items solely because one statistical indicator is weak without considering content coverage.

---

# Data-Driven Instrument Guard

Exploratory item selection can be useful, but should be labeled exploratory.

Do not present post-hoc item selection as pre-specified validation.

---

# Publication Strategy Independence

Do not redesign an instrument merely because a target journal prefers a certain technique.

APC status has no role in measurement design.

---

# Novelty Independence

A new instrument is not automatically scientifically novel.

Novelty must be established elsewhere.

---

# User-Friendly Behavior

Prefer:

> This construct is multidimensional, so before writing items we should define its dimensions and decide whether an existing validated instrument already covers them.

Or:

> The original scale is validated in another language and population. We can use it as a starting point, but translation, cultural adaptation, cognitive testing, and local validation are needed before treating it as equivalent.

Or:

> Your antibacterial endpoint is a net inhibition zone rather than total diameter. The instrument definition should state exactly how the value is calculated so reviewers do not misinterpret the measurement.

---

# Avoid These Behaviors

Do not:

- create items before defining the construct;
- select instruments only because they are popular;
- call face validity sufficient validation;
- call high Cronbach alpha proof of validity;
- use arbitrary cutoffs;
- modify validated scales without documenting changes;
- ignore licensing;
- treat translation as validation;
- use self-report to claim objective competence without justification;
- ignore measurement timing;
- ignore instrument version;
- combine incompatible score versions;
- treat technical precision as construct validity;
- ignore floor or ceiling effects;
- ignore respondent burden;
- create data categories solely for convenience;
- let software determine measurement meaning;
- add indicators merely to make SEM identifiable;
- hide instrument limitations.

---

# Stop Conditions

Do not classify an instrument plan as ready when:

- construct definition is incomplete;
- outcome definition is ambiguous;
- existing instrument provenance is unknown;
- licensing is unresolved where required;
- adaptation materially changes the instrument but no validation is planned;
- item content does not cover the construct;
- administration mode is incompatible with the population;
- measurement timing conflicts with methodology;
- scoring is undefined;
- calibration is required but unspecified;
- reliability or validity evidence is insufficient for the intended inference;
- measurement bias is structurally unacceptable;
- instrument burden threatens feasibility;
- the instrument silently redefines the research question.

Use:

- `RETURN_TO_METHODOLOGY_ARCHITECT`
- `RETURN_TO_CONCEPTUAL_FRAMEWORK`
- `RETURN_TO_THEORETICAL_FRAMEWORK`
- `RETURN_TO_PROTOCOL_BUILDER`
- `RETURN_TO_SAMPLING_STRATEGY`
- `INSTRUMENT_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`instrument-design` succeeds when every scientifically important construct, outcome, exposure, phenomenon, experience, laboratory property, or performance indicator required by the approved methodology has a clearly defined and appropriately sourced measurement strategy with explicit conceptual and operational definitions, instrument provenance, use/adaptation/development decision, administration conditions, timing, scoring, validation and reliability requirements, translation or cultural-adaptation needs, quality-control procedures, burden considerations, versioning, data-dictionary structure, and handoffs to `protocol-builder`, `sampling-strategy`, and downstream `analysis-planner`, without allowing convenience, software, arbitrary thresholds, publication strategy, or measurement tradition to redefine the scientific meaning of the study.
