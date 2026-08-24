---
name: protocol-builder
description: Convert an approved methodology architecture into a reproducible, auditable, implementation-ready research protocol. Use when the study design is sufficiently stable and the researcher needs to specify participant or unit flow, recruitment, consent, allocation, intervention or exposure procedures, measurement schedule, laboratory or field procedures, quality control, safety, data capture, deviation handling, monitoring, documentation, and protocol versioning without changing the scientific design silently.
---

# Protocol Builder

## Purpose

`protocol-builder` translates an approved methodology architecture into a reproducible operational protocol.

Its central question is:

> What exactly must happen, in what order, by whom, to whom or to what, under which conditions, with which controls, measurements, safeguards, records, and decision rules so that the study can be implemented consistently and reproduced by another competent research team?

This skill operationalizes methodology.

It does not redesign the study silently.

It does not choose statistical analysis.

It does not replace:

- `methodology-architect`;
- `sampling-strategy`;
- `instrument-design`;
- `analysis-planner`.

---

# Core Principle

Use:

> Design first. Protocol second. Procedures must implement the approved design without changing its scientific meaning.

The protocol should make the methodology executable.

Do not allow implementation convenience to redefine:

- research question;
- primary outcome;
- comparator;
- intervention;
- population;
- experimental unit;
- timing;
- sampling logic;
- measurement logic.

If an operational constraint changes the scientific design, route back to:

`methodology-architect`

---

# Position in the Framework

Preferred workflow:

```text
Research Question
      ↓
problem-solving-approach
      ↓
methodology-architect
      ↓
protocol-builder
      │
      ├───────────────┬────────────────┐
      ▼               ▼                ▼
sampling-strategy  instrument-design  quality safeguards
      │               │                │
      └───────────────┴────────────────┘
                      ↓
                DESIGN READY
                      ↓
                analysis-planner
```

The exact ordering may vary.

For some studies, sampling and instrument decisions must be refined in parallel with protocol development.

---

# Required Upstream Context

Use available information from:

- `methodology-architect`;
- `problem-solving-approach`;
- `research-question-builder`;
- `hypothesis-builder`;
- `theoretical-framework`;
- `conceptual-framework`;
- `sampling-strategy` when already available;
- `instrument-design` when already available.

Do not ask the researcher to repeat information already established.

Minimum useful context normally includes:

- approved study design;
- setting;
- population or unit;
- exposure / intervention / comparator;
- primary outcome or phenomenon;
- timing;
- measurement requirements;
- sampling requirements;
- bias safeguards;
- ethics needs;
- feasibility constraints.

---

# Protocol Readiness Gate

Classify:

- `READY_FOR_PROTOCOL_BUILDING`
- `METHODOLOGY_NOT_STABLE`
- `SAMPLING_DEPENDENCY_UNRESOLVED`
- `INSTRUMENT_DEPENDENCY_UNRESOLVED`
- `ETHICS_DEPENDENCY_UNRESOLVED`
- `PROTOCOL_ALREADY_AVAILABLE`
- `PROTOCOL_REQUIRES_REVISION`

Do not build detailed procedures if the methodology is still fundamentally unstable.

---

# Protocol Scope

A complete protocol may need to specify:

- study title;
- version;
- date;
- objectives;
- design summary;
- setting;
- eligibility;
- recruitment;
- consent;
- allocation;
- intervention;
- comparator;
- exposure ascertainment;
- measurement schedule;
- specimen collection;
- laboratory procedures;
- qualitative procedures;
- data capture;
- quality control;
- safety;
- monitoring;
- deviations;
- adverse events;
- data management;
- documentation;
- retention;
- closeout.

Not every study requires every section.

Use only scientifically relevant components.

---

# Protocol Identity

Recommended metadata:

```yaml
protocol:
  study_title:
  protocol_id:
  version:
  version_date:
  status:
  principal_investigator:
  study_site:
  document_owner:
  approval_status:
  registration_status:
```

Do not fabricate missing identifiers.

---

# Version Control

Every operational protocol should have explicit version control.

Use:

- version number;
- effective date;
- amendment date;
- amendment reason;
- approved by;
- replaced version.

Example:

```text
v1.0 — Initial approved protocol
v1.1 — Administrative clarification
v2.0 — Scientific amendment
```

Distinguish administrative edits from scientific amendments.

---

# Amendment Guard

If a change affects:

- primary RQ;
- outcome;
- population;
- intervention;
- comparator;
- sample structure;
- timing;
- eligibility;
- measurement validity;
- bias risk;

classify:

`SCIENTIFIC_PROTOCOL_AMENDMENT`

and route back to `methodology-architect` when necessary.

Do not hide substantive design changes inside operational revisions.

---

# Protocol Summary

Start with a concise implementation summary:

```yaml
protocol_summary:
  design:
  setting:
  population_or_unit:
  intervention_or_exposure:
  comparator:
  primary_target:
  duration:
  major_procedures:
  major_safeguards:
```

---

# Participant / Unit Flow

Define the operational flow.

For human participants:

```text
Potentially Eligible
      ↓
Screened
      ↓
Eligible
      ↓
Approached
      ↓
Consented
      ↓
Enrolled
      ↓
Assigned / Classified
      ↓
Measured / Treated / Observed
      ↓
Followed
      ↓
Completed / Withdrawn
      ↓
Analyzed
```

For non-human studies adapt terminology.

---

# Screening

Define:

- who screens;
- where;
- against which criteria;
- source documents;
- documentation;
- handling of ineligible cases;
- re-screening rules if applicable.

Do not allow undocumented eligibility exceptions.

---

# Eligibility Verification

Eligibility should be operationalized into verifiable criteria.

For each criterion:

```yaml
eligibility_check:
  criterion:
  evidence_required:
  responsible_role:
  decision_rule:
  documentation:
```

---

# Recruitment

Specify:

- recruitment source;
- recruitment channel;
- recruitment message;
- recruiter;
- recruitment window;
- repeated contact limits;
- screening transition;
- coercion safeguards.

Recruitment procedures must match the source population.

---

# Consent

When human participants are involved, define:

- consent type;
- person obtaining consent;
- timing;
- information provided;
- documentation;
- language;
- comprehension safeguards;
- withdrawal rights;
- assent / parental permission when relevant.

Do not invent jurisdiction-specific legal wording.

---

# Consent Capacity

If capacity may be limited, define procedures for:

- capacity assessment;
- legally authorized representative;
- assent;
- re-consent if capacity changes.

Detailed legal requirements require jurisdiction-specific verification.

---

# Enrollment

Define the exact point at which a participant or unit becomes enrolled.

Do not conflate:

- screened;
- eligible;
- consented;
- enrolled;
- analyzed.

---

# Allocation

For interventional studies specify:

- allocation unit;
- allocation sequence;
- generation method;
- concealment;
- implementation;
- assignment responsibility.

If randomization is not used, state the assignment mechanism explicitly.

---

# Randomization Procedure

Operationalize:

- sequence generation;
- blocking if used;
- stratification if used;
- allocation ratio;
- seed / reproducibility if computational;
- secure storage;
- access control.

Do not reveal allocation prematurely.

---

# Cluster Randomization

If clusters are randomized, specify:

- cluster definition;
- cluster recruitment;
- participant recruitment timing;
- contamination safeguards;
- cluster-level allocation.

---

# Blinding / Masking Procedure

Specify who is blinded:

- participant;
- provider;
- assessor;
- laboratory analyst;
- data manager;
- statistician.

Also specify:

- what information is concealed;
- when unblinding is permitted;
- who can authorize unblinding;
- how it is documented.

---

# Intervention Protocol

For each intervention define:

```yaml
intervention:
  name:
  rationale:
  components:
  dose_or_intensity:
  route_or_mode:
  duration:
  frequency:
  delivery_agent:
  setting:
  materials:
  adherence_monitoring:
  allowed_modifications:
  prohibited_modifications:
  stopping_rules:
```

---

# Comparator Protocol

Define comparator procedures with equal operational clarity.

Possible comparator types:

- placebo;
- standard care;
- no intervention;
- alternative intervention;
- baseline;
- reference formulation;
- reference assay;
- unexposed group.

Do not under-specify the comparator.

---

# Intervention Fidelity

Define how fidelity will be protected.

Possible dimensions:

- dose delivered;
- dose received;
- adherence;
- protocol consistency;
- provider competence;
- session completion;
- material preparation;
- intervention exposure.

Use fidelity logs when appropriate.

---

# Co-Interventions

Define:

- allowed co-interventions;
- prohibited co-interventions;
- required documentation;
- rescue treatment;
- contamination risk.

---

# Exposure Ascertainment

For observational studies define:

- exposure source;
- time window;
- operational definition;
- repeated ascertainment;
- misclassification safeguards;
- data provenance.

---

# Outcome Ascertainment

For each major outcome define:

```yaml
outcome_procedure:
  outcome:
  operational_definition:
  assessor:
  instrument_or_assay:
  timing:
  source:
  adjudication:
  quality_control:
```

---

# Measurement Schedule

Create a schedule when timing matters.

Example:

| Time Point | Eligibility | Exposure / Intervention | Primary Outcome | Secondary Outcome | Safety | Other |
|---|---|---|---|---|---|---|

Do not add time points without scientific purpose.

---

# Visit Schedule

For longitudinal or clinical studies define:

- baseline;
- intervention visits;
- follow-up visits;
- allowable windows;
- missed-visit handling;
- unscheduled visits;
- final visit.

---

# Measurement Window

Specify acceptable time windows around scheduled assessments.

Do not silently treat measurements taken far outside the intended window as equivalent.

Use:

`PROTOCOL_WINDOW_DEVIATION`

when necessary.

---

# Participant Instructions

Standardize instructions that could affect measurement.

Examples:

- fasting;
- medication withholding where ethically appropriate;
- activity restriction;
- device preparation;
- questionnaire conditions;
- specimen collection instructions.

---

# Laboratory Sample Collection

Define:

- specimen type;
- collection container;
- collection volume;
- timing;
- labeling;
- transport;
- temperature;
- processing time;
- storage;
- chain of custody.

---

# Laboratory Sample Labeling

Use unique identifiers.

Avoid unnecessary direct identifiers on research specimens.

Recommended fields may include:

- study ID;
- visit;
- specimen type;
- date;
- aliquot number.

---

# Sample Processing

Define:

- centrifugation;
- separation;
- aliquoting;
- dilution;
- extraction;
- stabilization;
- freezing;
- thaw limits;
- disposal.

Only include procedures relevant to the actual study.

---

# Storage Conditions

Specify:

- temperature;
- container;
- duration;
- location;
- access;
- monitoring;
- backup storage if needed.

---

# Chain of Custody

For sensitive specimens or regulated materials define:

```text
Collection
   ↓
Transfer
   ↓
Receipt
   ↓
Processing
   ↓
Storage
   ↓
Analysis
   ↓
Retention / Disposal
```

Each transfer should be traceable when required.

---

# Assay Procedure

Define:

- assay principle;
- equipment;
- reagents;
- calibration;
- controls;
- sample preparation;
- run order;
- acceptance criteria;
- repeat criteria;
- result recording.

Do not embed unverified manufacturer instructions as universal rules.

---

# Calibration

Specify:

- equipment;
- calibration method;
- frequency;
- acceptable range;
- documentation;
- corrective action.

---

# Positive and Negative Controls

For laboratory assays define:

- positive control;
- negative control;
- blank;
- solvent control;
- reference standard;

as relevant.

---

# Microbiological Protocol

When relevant specify:

- organism;
- strain;
- culture conditions;
- inoculum preparation;
- inoculum target;
- medium;
- incubation;
- test method;
- controls;
- endpoint;
- replicate structure;
- contamination safeguards.

Distinguish screening diffusion assays from quantitative susceptibility methods.

---

# Formulation Protocol

For formulation research specify:

- raw materials;
- supplier / grade;
- formulation code;
- batch number;
- quantities;
- processing sequence;
- temperature;
- mixing;
- pH adjustment;
- homogenization;
- packaging;
- curing / resting;
- storage;
- quality checks.

Do not allow undocumented batch changes.

---

# Batch Record

Each formulation or material batch should record:

```yaml
batch_record:
  batch_id:
  date:
  operator:
  raw_material_lots:
  quantities:
  process_conditions:
  deviations:
  yield:
  release_status:
```

---

# Stability Protocol

Define:

- storage condition;
- packaging;
- time points;
- critical quality attributes;
- acceptance criteria;
- sample handling;
- analytical method;
- failure rule.

---

# Pharmacokinetic Sampling Protocol

Define:

- dose time;
- sample times;
- allowable windows;
- specimen;
- processing;
- storage;
- assay;
- actual collection time recording.

Actual sample time matters.

---

# Genetic / Genomic Protocol

When relevant define:

- specimen;
- extraction;
- DNA / RNA quality;
- genotyping platform;
- variant call criteria;
- quality control;
- contamination control;
- sample identity;
- storage;
- re-run rules.

---

# Qualitative Interview Protocol

Define:

- interviewer;
- interview mode;
- location;
- duration;
- topic guide;
- recording;
- field notes;
- probing principles;
- confidentiality;
- transcription;
- reflexive notes.

Do not over-standardize qualitative interviews to the point that relevant participant meaning is suppressed.

---

# Focus Group Protocol

Specify:

- group size logic;
- moderator;
- co-moderator;
- composition;
- setting;
- recording;
- group confidentiality limitations;
- discussion guide;
- field notes.

---

# Observation Protocol

Define:

- observation setting;
- observer role;
- observation period;
- structured vs open observation;
- field-note format;
- participant awareness;
- recording rules.

---

# Document Analysis Protocol

Define:

- document source;
- inclusion rule;
- document version;
- extraction fields;
- provenance;
- authenticity checks;
- handling of duplicates.

---

# Survey Administration Protocol

Define:

- administration mode;
- invitation;
- consent;
- authentication if needed;
- item order;
- mandatory vs optional items;
- save / resume rules;
- duplicate-response control;
- reminders;
- closure.

---

# Online Data Collection

Specify:

- platform;
- access;
- authentication;
- privacy;
- browser/device considerations;
- duplicate prevention;
- timestamp;
- export;
- backup.

Do not assume online platforms are automatically compliant with local privacy rules.

---

# Device-Based Measurement

Define:

- device;
- model;
- firmware when relevant;
- calibration;
- placement;
- wear time;
- synchronization;
- missing-data rules;
- charging;
- data transfer.

---

# Imaging Protocol

When relevant specify:

- modality;
- acquisition parameters;
- operator;
- positioning;
- calibration;
- image labeling;
- quality review;
- storage;
- blinded reading.

---

# Intervention Training

If staff deliver an intervention, define:

- training content;
- competency assessment;
- retraining;
- certification;
- supervision.

---

# Assessor Training

Define:

- instrument training;
- scoring practice;
- competency threshold;
- inter-rater calibration;
- refresher schedule.

---

# Standard Operating Procedures

Use SOPs for procedures requiring high consistency.

Each SOP should ideally include:

- purpose;
- scope;
- responsibilities;
- materials;
- steps;
- acceptance criteria;
- deviations;
- documentation.

---

# Roles and Responsibilities

Define operational roles.

Examples:

- principal investigator;
- coordinator;
- recruiter;
- assessor;
- intervention provider;
- laboratory analyst;
- data manager;
- safety monitor.

Avoid role ambiguity.

---

# Responsibility Matrix

When useful:

| Procedure | Responsible | Backup | Documentation |
|---|---|---|---|

---

# Data Capture

Specify:

- source document;
- case report form;
- electronic form;
- spreadsheet;
- database;
- device export;
- laboratory system.

Do not create parallel undocumented data sources.

---

# Source Data

Define which record is the authoritative source.

Examples:

- medical record;
- laboratory instrument;
- interview audio;
- paper CRF;
- electronic CRF;
- device log.

---

# Case Report Form

A CRF should capture only information necessary for:

- eligibility;
- exposure / intervention;
- outcomes;
- safety;
- confounding;
- protocol compliance.

Avoid unnecessary personal data.

---

# Data Entry

Define:

- single entry;
- double entry;
- direct electronic capture;
- validation rules;
- date format;
- missing code;
- correction rules.

---

# Data Validation

Possible checks:

- range;
- consistency;
- date sequence;
- duplicate ID;
- impossible values;
- required fields;
- visit windows;
- logical dependencies.

---

# Audit Trail

Changes to important research data should preserve:

- old value;
- new value;
- reason;
- user;
- date/time.

---

# Data Correction

Do not overwrite data silently.

Use correction procedures appropriate to the data system.

---

# Missing Data Prevention

Protocol-level prevention may include:

- required checks;
- visit reminders;
- redundant contact;
- immediate form review;
- real-time validation;
- specimen completeness checks.

---

# Data Security

Define:

- storage location;
- access roles;
- password / authentication;
- encryption where available;
- backup;
- export controls;
- transfer rules.

---

# Identifier Management

Separate identifiers from research data when possible.

Use:

- study ID;
- linkage key;
- restricted master list.

---

# Confidentiality

Define:

- who can see identifiers;
- who can see analysis data;
- where files are stored;
- how outputs are de-identified.

---

# Data Retention

Specify:

- retention duration if known;
- storage;
- access;
- destruction;
- archival responsibilities.

Do not invent regulatory retention periods.

---

# Quality Assurance

Protocol-level QA may include:

- training;
- SOP compliance;
- monitoring;
- calibration;
- source verification;
- data checks;
- laboratory QC;
- deviation review.

---

# Quality Control

QC occurs during execution.

Possible QC includes:

- duplicate measurements;
- internal controls;
- repeat assays;
- inter-rater checks;
- batch acceptance;
- form review;
- automated validation.

---

# Quality Assurance vs Quality Control

Distinguish:

- QA = system-level assurance that processes are appropriate;
- QC = operational checks that outputs meet criteria.

---

# Monitoring Plan

Define monitoring when needed:

- frequency;
- scope;
- responsible role;
- source documents;
- deviations;
- consent;
- safety;
- data quality.

---

# Risk-Based Monitoring

Monitoring intensity may depend on:

- participant risk;
- intervention complexity;
- data criticality;
- site experience;
- protocol complexity.

---

# Protocol Deviations

Define:

- deviation;
- violation where terminology is used;
- detection;
- documentation;
- classification;
- corrective action;
- preventive action;
- reporting.

---

# Deviation Classification

Use:

- `MINOR_DEVIATION`
- `MAJOR_DEVIATION`
- `SAFETY_RELEVANT_DEVIATION`
- `DATA_INTEGRITY_RELEVANT_DEVIATION`
- `SCIENTIFIC_DESIGN_DEVIATION`

---

# Deviation Decision Rule

A deviation affecting scientific validity may require:

`METHODOLOGY_REASSESSMENT`

Do not solve major design deviations only through analysis.

---

# Corrective and Preventive Action

For recurring problems define:

```text
Problem
  ↓
Root Cause
  ↓
Corrective Action
  ↓
Preventive Action
  ↓
Verification
```

---

# Adverse Events

For human interventional studies define:

- event definition;
- detection;
- severity;
- seriousness;
- relatedness;
- expectedness;
- action;
- reporting;
- follow-up.

Do not invent regulatory reporting deadlines.

---

# Stopping Rules

When relevant specify rules for:

- participant stopping;
- intervention stopping;
- batch rejection;
- laboratory run rejection;
- study suspension;
- early termination.

---

# Rescue Procedure

If participants can deteriorate or require rescue treatment, define:

- trigger;
- response;
- responsible role;
- documentation.

---

# Emergency Unblinding

When relevant specify:

- who can request;
- who can authorize;
- what criteria apply;
- documentation;
- downstream consequences.

---

# Protocol Noncompliance

Define how repeated noncompliance is handled.

Do not remove data automatically unless predefined criteria justify exclusion.

---

# Withdrawal

For participant withdrawal specify:

- voluntary withdrawal;
- investigator withdrawal;
- safety withdrawal;
- lost to follow-up;
- consent withdrawal;
- data-use implications where ethically and legally applicable.

---

# Lost to Follow-Up

Define:

- contact attempts;
- channels;
- timing;
- escalation;
- final classification.

---

# Study Completion

Define the operational definition of completion.

For example:

- final visit completed;
- all required samples collected;
- minimum follow-up reached;
- study endpoint observed.

---

# Early Termination

Document:

- reason;
- date;
- procedures completed;
- safety follow-up;
- data status.

---

# Closeout

Study closeout may include:

- final data check;
- unresolved queries;
- specimen inventory;
- equipment return;
- document archive;
- access closure;
- deviation reconciliation.

---

# Protocol for Secondary Data

For secondary-data studies define:

- dataset;
- version;
- access date;
- extraction query;
- inclusion window;
- linkage;
- transformation;
- variable mapping;
- provenance;
- reproducibility.

---

# Query Reproducibility

For database extraction preserve:

- query text;
- parameters;
- database version;
- extraction date;
- filters;
- code where applicable.

---

# Protocol for Systematic Reviews

Define operationally:

- databases;
- search dates;
- search strings;
- deduplication;
- screening sequence;
- reviewers;
- conflict resolution;
- extraction;
- risk-of-bias assessment;
- synthesis preparation.

This should align with evidence-layer skills rather than duplicate their scientific roles.

---

# Screening Protocol

For reviews define:

- title / abstract screening;
- full-text screening;
- number of reviewers;
- conflict resolution;
- exclusion reasons.

---

# Extraction Protocol

Define:

- extraction fields;
- reviewer process;
- duplicate extraction if needed;
- discrepancy resolution;
- source verification.

---

# Bibliometric Protocol

Define:

- database;
- search query;
- export date;
- metadata fields;
- deduplication;
- cleaning;
- normalization;
- network construction;
- parameter recording.

---

# Computational Protocol

For computational studies specify:

- software;
- version;
- packages;
- environment;
- hardware when relevant;
- seeds;
- input data;
- preprocessing;
- model configuration;
- output storage.

Software is relevant here because methodology has already been established.

---

# Reproducible Computing

Preserve:

- code;
- environment;
- package versions;
- random seeds;
- configuration;
- file paths;
- data dictionary.

---

# Simulation Protocol

Define:

- data-generating process;
- parameter values;
- number of simulations;
- random seeds;
- scenarios;
- performance metrics.

---

# Pilot Protocol

If a pilot is required, define what uncertainty it is intended to resolve.

Pilot objectives may include:

- recruitment feasibility;
- timing;
- intervention delivery;
- instrument usability;
- laboratory workflow;
- adherence;
- data completeness.

Do not use a pilot to make unsupported definitive effectiveness claims.

---

# Run-In Period

When relevant define:

- purpose;
- duration;
- criteria;
- impact on eligibility;
- data use.

---

# Training Pilot

A protocol may include internal dry runs before participant enrollment.

Document whether pilot data are part of the study.

---

# Pre-Study Checklist

Before launch confirm:

- approvals;
- protocol version;
- staff training;
- instruments;
- database;
- supplies;
- calibration;
- randomization;
- emergency procedures;
- contact information;
- document templates.

---

# Site Initiation

For multi-site studies define:

- site qualification;
- training;
- approvals;
- equipment;
- startup documentation;
- activation criteria.

---

# Multi-Site Consistency

Standardize:

- eligibility;
- intervention;
- measurement;
- laboratory handling;
- data capture;
- deviation reporting.

---

# Site-Specific Adaptation

Allow local adaptation only when it does not alter core scientific meaning.

Classify changes as:

- administrative;
- operational;
- scientific.

---

# Protocol Timeline

Build when useful:

```text
Preparation
   ↓
Recruitment
   ↓
Enrollment
   ↓
Intervention / Observation
   ↓
Follow-up
   ↓
Data Lock
   ↓
Analysis
   ↓
Closeout
```

---

# Milestone Table

| Milestone | Trigger | Responsible | Output |
|---|---|---|---|

---

# Decision Rules

Predefine operational decision rules when possible.

Examples:

- eligibility;
- assay acceptance;
- repeat measurement;
- participant discontinuation;
- batch rejection;
- missing visit;
- protocol deviation severity.

---

# Acceptance Criteria

For procedures requiring acceptance criteria define:

```yaml
acceptance_rule:
  procedure:
  criterion:
  threshold:
  action_if_failed:
```

Do not invent thresholds without scientific or regulatory basis.

---

# Escalation Rules

Specify when an issue must be escalated to:

- principal investigator;
- safety lead;
- laboratory lead;
- ethics committee;
- sponsor;
- data manager.

Only include roles relevant to the study.

---

# Documentation Architecture

Recommended protocol documents may include:

- protocol;
- SOPs;
- screening log;
- enrollment log;
- consent log;
- randomization log;
- intervention log;
- visit forms;
- specimen log;
- deviation log;
- adverse-event log;
- calibration log;
- training log;
- data query log.

Do not create unnecessary bureaucracy.

---

# Essential Documents

Essential-document requirements vary by study type and jurisdiction.

Do not invent formal regulatory lists unless verified.

---

# Protocol Operational Schema

Recommended internal representation:

```yaml
protocol_execution:
  protocol_id:
  version:
  status:
  study_design:
  setting:
  population:
  screening:
  consent:
  enrollment:
  allocation:
  intervention_or_exposure:
  comparator:
  measurement_schedule:
  specimen_procedures:
  laboratory_procedures:
  qualitative_procedures:
  data_capture:
  quality_control:
  safety:
  deviations:
  monitoring:
  closeout:
  roles:
  documents:
```

---

# Procedure Record

For each major procedure:

```yaml
procedure:
  name:
  purpose:
  trigger:
  responsible_role:
  materials:
  prerequisites:
  steps:
  timing:
  acceptance_criteria:
  documentation:
  deviation_handling:
```

---

# Operational Sequence

When useful create:

| Step | Procedure | Responsible | Timing | Input | Output | Record |
|---|---|---|---|---|---|---|

---

# Reproducibility Check

Ask:

> Could another competent team reproduce the procedure from this protocol without guessing critical steps?

If no, classify:

`PROTOCOL_NOT_REPRODUCIBLE`

---

# Ambiguity Check

Flag vague language such as:

- "appropriate amount";
- "as needed";
- "standard method";
- "regularly";
- "sufficient time";

unless the phrase is defined elsewhere.

---

# Over-Specification Guard

Do not specify arbitrary detail that has no scientific, safety, quality, or reproducibility value.

A protocol should be precise, not bloated.

---

# Researcher Convenience Guard

Do not allow statements such as:

> We will measure whenever participants are available.

if timing is scientifically important.

---

# Protocol Drift

Detect:

`PROTOCOL_DRIFT`

when actual procedures gradually diverge from the approved protocol.

Use monitoring and retraining when necessary.

---

# Instrument Dependency

If the protocol requires a measurement tool that has not yet been selected or validated, route to:

`instrument-design`

Do not invent the instrument.

---

# Sampling Dependency

If participant or unit selection procedures are unresolved, route to:

`sampling-strategy`

Do not improvise recruitment rules.

---

# Analysis Dependency

Do not redesign procedures solely to match a preferred analysis method.

However, ensure data structure required by the approved design will be captured.

---

# Analysis Handoff

Provide downstream analysis planning with:

- actual design;
- allocation;
- clustering;
- repeated measures;
- timing;
- outcome structure;
- missingness process;
- protocol deviations;
- adherence;
- censoring;
- exclusions.

---

# Protocol-to-Analysis Integrity

Do not allow analysis labels that contradict execution.

Example:

A study cannot be analyzed as a randomized trial if assignment was not randomized.

---

# Protocol Deviations and Analysis

Deviations may affect:

- intention-to-treat;
- per-protocol;
- as-treated;
- sensitivity analyses.

Detailed analysis decisions belong downstream.

---

# Data Lock

Define when data become ready for final analysis.

Possible prerequisites:

- queries resolved;
- coding finalized;
- data validation complete;
- deviations classified;
- outcome adjudication complete.

---

# Blinded Data Review

When appropriate, a blinded review may identify:

- data issues;
- coding problems;
- missingness;
- protocol inconsistencies;

without examining treatment effects.

---

# Protocol Reporting Alignment

Where relevant, align protocol structure with applicable reporting or protocol standards.

Do not claim compliance with a named guideline unless requirements are actually met.

---

# Domain Adaptation

Adapt protocol content to domain.

Examples:

- clinical;
- pharmaceutical;
- laboratory;
- biomedical;
- education;
- qualitative;
- organizational;
- engineering;
- policy;
- computational;
- evidence synthesis.

The core protocol principles remain:

- reproducibility;
- traceability;
- consistency;
- design fidelity;
- quality;
- safety.

---

# User-Friendly Behavior

Prefer:

> The methodology is already stable. The next task is to turn it into an executable sequence: screening, consent, enrollment, intervention, measurement, follow-up, data capture, quality control, and deviation handling.

Or:

> Because your formulation study varies chitosan concentration, each batch needs a unique code, fixed processing conditions, raw-material lot records, defined storage, and predefined physicochemical testing time points.

Or:

> Your qualitative design is not improved by a rigid script. The protocol should standardize consent, recording, topic domains, confidentiality, transcription, and reflexive documentation while preserving responsive probing.

---

# Minimal Output

For a simple request provide:

## Protocol Summary
[...]

## Operational Flow
[...]

## Critical Procedures
[...]

## Quality Safeguards
[...]

## Documentation
[...]

## Dependencies
[...]

---

# Comprehensive Output

When full protocol development is requested:

## A. Protocol Identification
[...]

## B. Objectives
[...]

## C. Design Summary
[...]

## D. Setting
[...]

## E. Eligibility
[...]

## F. Recruitment
[...]

## G. Consent
[...]

## H. Enrollment
[...]

## I. Allocation
[...]

## J. Intervention / Exposure
[...]

## K. Comparator
[...]

## L. Measurement Schedule
[...]

## M. Specimen / Laboratory Procedures
[...]

## N. Qualitative Procedures
[...]

## O. Data Capture
[...]

## P. Quality Control
[...]

## Q. Safety
[...]

## R. Monitoring
[...]

## S. Deviations
[...]

## T. Data Management
[...]

## U. Roles
[...]

## V. Documentation
[...]

## W. Closeout
[...]

## X. Version Control
[...]

---

# Relationship with Methodology Architect

`methodology-architect` defines the scientific design.

`protocol-builder` operationalizes that design.

Use:

```text
methodology-architect
      ↓
protocol-builder
```

Do not let the protocol silently redesign methodology.

---

# Relationship with Sampling Strategy

`sampling-strategy` defines how eligible units are selected and how many are needed.

`protocol-builder` defines how that sampling strategy is executed operationally.

---

# Relationship with Instrument Design

`instrument-design` determines valid measurement tools.

`protocol-builder` determines:

- when;
- by whom;
- under what conditions;
- how;

those instruments are administered.

---

# Relationship with Analysis Planner

`protocol-builder` provides the actual data-generating process.

`analysis-planner` must respect that process.

---

# Relationship with Research Router

`research-router` should route here when the user already has a sufficiently stable methodology and asks for:

- research protocol;
- SOP;
- procedural flow;
- implementation procedure;
- data collection procedure;
- laboratory procedure;
- study execution plan.

---

# Avoid These Behaviors

Do not:

- rewrite the RQ silently;
- change eligibility for convenience without scientific review;
- change the primary outcome during protocol drafting;
- invent regulatory requirements;
- invent safety thresholds;
- invent assay thresholds;
- confuse randomization with convenience assignment;
- confuse technical replicates with independent units;
- use vague procedural language when precision is important;
- over-specify irrelevant detail;
- create SOP bureaucracy without value;
- choose analysis software here;
- allow protocol drift;
- overwrite source data silently;
- omit version control;
- omit deviation handling where deviations can affect validity;
- call a draft protocol approved;
- claim reproducibility when critical steps remain implicit.

---

# Stop Conditions

Do not classify the protocol as ready when:

- methodology is not stable;
- eligibility cannot be operationalized;
- intervention / exposure is undefined;
- comparator procedures are undefined where required;
- measurement timing is unresolved;
- critical instruments are unavailable or invalid;
- sampling execution cannot be specified;
- major safety procedures are missing;
- data capture is undefined;
- quality-control rules are absent for critical procedures;
- major deviations have no handling logic;
- version control is absent;
- the protocol contains silent scientific design changes.

Use:

- `RETURN_TO_METHODOLOGY_ARCHITECT`
- `RETURN_TO_SAMPLING_STRATEGY`
- `RETURN_TO_INSTRUMENT_DESIGN`
- `PROTOCOL_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`protocol-builder` succeeds when an approved methodology has been translated into a version-controlled, reproducible, auditable, and implementation-ready operational protocol that specifies the exact flow of units or participants, screening, eligibility, recruitment, consent where applicable, allocation, intervention or exposure procedures, comparator procedures, measurement schedule, laboratory or qualitative procedures, data capture, quality control, safety, monitoring, deviation handling, documentation, roles, and closeout processes without silently changing the scientific design, and is ready to operate coherently with `sampling-strategy`, `instrument-design`, and downstream `analysis-planner`.
