---
name: data-collection-monitor
description: Monitor, document, and audit active research data collection for completeness, timeliness, source continuity, measurement fidelity, participant or sample flow, instrument use, missingness emergence, linkage integrity, collection-site variation, and collection-readiness for downstream analysis. Use after research-execution-manager has activated implementation and while primary, secondary, laboratory, clinical, survey, qualitative, observational, sensor, registry, archival, or multi-site data are being collected or received. This skill detects collection problems without silently cleaning data, distinguishes expected missingness from operational failure, routes protocol departures to protocol-adherence-monitor, prospective execution threats to deviation-risk-monitor, data-validity issues to data-quality-auditor, provenance issues to research-data-governance, permission issues to ethics-regulatory-gate, and milestone implications to research-progress-auditor while preserving a traceable record of what was planned, what was collected, what was not collected, why, and what scientific consequence follows.
---

# Data Collection Monitor

## Purpose

`data-collection-monitor` determines whether active research data collection is producing the planned evidence stream with sufficient completeness, timing, provenance, fidelity, and traceability to support the intended scientific analysis.

Its central question is:

> Is the study collecting the right data, from the right units, at the right times, through the right procedures, with traceable provenance and acceptable completeness, and what must happen when collection begins to fail, drift, or diverge from plan?

The core monitoring chain is:

```text
PLANNED DATA COLLECTION
        ↓
ACTIVE COLLECTION / RECEIPT
        ↓
SOURCE / PARTICIPANT / SAMPLE FLOW
        ↓
COMPLETENESS + TIMELINESS + FIDELITY
        ↓
MISSINGNESS / DELAY / LOSS / ANOMALY DETECTION
        ↓
SCIENTIFIC CONSEQUENCE ASSESSMENT
        ↓
CORRECT / RECOVER / ESCALATE / AMEND / PAUSE / STOP
        ↓
TRACEABLE HANDOFF TO DATA QUALITY / ANALYSIS
```

This skill does not perform cosmetic data cleaning.

It monitors whether the intended evidence is actually being generated or received.

---

# 1. Core Principles

Preserve these distinctions:

```text
DATA COLLECTION ≠ DATA CLEANING
COLLECTED ≠ VALID
AVAILABLE ≠ COMPLETE
COMPLETE ≠ REPRESENTATIVE
MISSING ≠ ERROR
DELAYED ≠ LOST
LOST ≠ RANDOM
SOURCE RECORD ≠ ANALYSIS DATASET
PLANNED VARIABLE ≠ ACTUALLY COLLECTED VARIABLE
COLLECTION PROGRESS ≠ SCIENTIFIC SUCCESS
HIGH RESPONSE ≠ LOW BIAS
NO WARNING ≠ NO COLLECTION PROBLEM
```

---

# 2. Activation Gate

Use `data-collection-monitor` when:

- recruitment or sampling is active;
- observations are being recorded;
- surveys are open;
- laboratory data are being generated;
- specimens are being processed;
- clinical measurements are being taken;
- qualitative interviews or observations are ongoing;
- secondary data are being received or extracted;
- sensor or device data are streaming;
- registry or administrative data are being linked;
- multiple sites are submitting data;
- or the researcher needs to know whether collection is on track and scientifically usable.

---

# 3. Upstream Requirements

Use, when available:

- research question;
- methodology;
- protocol;
- sampling strategy;
- instrument design;
- data collection schedule;
- variable dictionary;
- case report form;
- interview guide;
- observation protocol;
- laboratory SOP;
- specimen plan;
- source-data definition;
- data-governance plan;
- ethics and regulatory status;
- registration or preregistration;
- execution plan;
- and analysis requirements.

---

# 4. Collection Monitoring Context

```yaml
collection_context:
  study_id:
  protocol_version:
  collection_start:
  current_date:
  collection_end_planned:
  active_sites:
  active_sources:
  target_sample:
  current_sample:
  ethics_status:
  registration_status:
  data_governance_status:
```

---

# 5. Collection Unit

A collection unit may be:

- participant;
- patient;
- household;
- class;
- organization;
- site;
- specimen;
- batch;
- interview;
- observation session;
- document;
- record;
- sensor device;
- image;
- sequence;
- survey response;
- timepoint;
- experimental run.

---

# 6. Collection Unit Record

```yaml
collection_unit:
  unit_id:
  unit_type:
  site:
  source:
  planned_timepoint:
  actual_timepoint:
  protocol_version:
  eligibility_status:
  consent_status:
  data_expected:
  data_received:
  completeness_status:
  provenance_status:
  protocol_adherence_status:
  quality_flag:
  notes:
```

---

# 7. Collection Status

Use:

- `NOT_STARTED`
- `ACTIVE`
- `ON_TRACK`
- `ON_TRACK_WITH_RISK`
- `DELAYED`
- `PARTIALLY_COMPLETE`
- `COMPLETE_PENDING_REVIEW`
- `COMPLETE`
- `PAUSED`
- `BLOCKED`
- `TERMINATED`
- `STATUS_UNCERTAIN`

---

# 8. Collection Readiness

Before collection begins, verify:

- source access;
- participant or sample eligibility process;
- consent process;
- instrument availability;
- protocol version;
- data-entry mechanism;
- identifiers;
- storage;
- permissions;
- training;
- linkage logic;
- missingness coding;
- and escalation routes.

---

# 9. Readiness Status

Use:

- `READY_TO_COLLECT`
- `READY_WITH_CONDITIONS`
- `NOT_READY_PROTOCOL`
- `NOT_READY_INSTRUMENT`
- `NOT_READY_ETHICS`
- `NOT_READY_DATA_GOVERNANCE`
- `NOT_READY_SITE`
- `NOT_READY_STAFF`
- `NOT_READY_SOURCE`
- `BLOCKED`

---

# 10. Planned Data Elements

Monitor what the study planned to collect.

Use:

```yaml
planned_data_element:
  variable:
  role:
  source:
  instrument:
  timepoint:
  unit:
  required:
  allowed_missing:
  derivation:
  collection_rule:
```

---

# 11. Required vs Optional Data

Distinguish:

- scientifically required;
- operationally useful;
- optional;
- derived;
- exploratory.

---

# 12. Primary Outcome Priority

Primary outcomes require explicit monitoring for:

- completeness;
- timing;
- instrument fidelity;
- source evidence;
- missingness;
- protocol adherence.

---

# 13. Secondary Outcome Monitoring

Maintain hierarchy and planned timepoints.

---

# 14. Predictor Monitoring

Check whether key predictors are consistently collected.

---

# 15. Covariate Monitoring

Do not silently add or drop covariates because collection is difficult.

---

# 16. Exposure Monitoring

Track timing, dose, duration, intensity, and source where relevant.

---

# 17. Intervention Data

Track what was actually delivered.

---

# 18. Qualitative Data Elements

Monitor:

- recording;
- transcript;
- field notes;
- metadata;
- consent;
- interviewer;
- context;
- duration.

---

# 19. Source Data Definition

Define what counts as the authoritative source record.

---

# 20. Source Continuity

Monitor whether the same type and quality of source remains available over time.

---

# 21. Source Change

A source change may require:

- protocol review;
- governance review;
- comparability assessment;
- amendment;
- analysis adjustment.

---

# 22. Source Provenance

Route provenance issues to:

`research-data-governance`

---

# 23. Source-to-Dataset Traceability

Each material collected value should be traceable to its origin where required.

---

# 24. Identifier Integrity

Monitor participant, specimen, site, visit, and record identifiers.

---

# 25. Duplicate Identifier

Flag duplicate IDs immediately.

Do not merge automatically.

---

# 26. Missing Identifier

Treat as a traceability risk.

---

# 27. Linkage Integrity

For linked datasets, monitor:

- linkage keys;
- matching rules;
- unmatched records;
- one-to-many links;
- ambiguous links;
- linkage version.

---

# 28. Linkage Failure

Route unresolved linkage validity to:

`research-data-governance`

and potentially:

`data-quality-auditor`

---

# 29. Timeliness

Monitor planned vs actual collection time.

---

# 30. Timing Status

Use:

- `ON_TIME`
- `EARLY`
- `LATE_WITHIN_WINDOW`
- `LATE_OUTSIDE_WINDOW`
- `MISSED`
- `UNKNOWN`

---

# 31. Timing Window

Use protocol-defined windows.

Do not invent tolerance after the fact.

---

# 32. Visit Window Deviation

Route protocol-relevant timing departures to:

`protocol-adherence-monitor`

---

# 33. Collection Completeness

Completeness should be assessed at multiple levels:

- unit;
- variable;
- visit;
- site;
- timepoint;
- study.

---

# 34. Unit Completeness

```yaml
unit_completeness:
  unit_id:
  expected_fields:
  received_fields:
  missing_fields:
  completion_rate:
  critical_missing:
  status:
```

---

# 35. Variable Completeness

Monitor whether missingness clusters by variable.

---

# 36. Site Completeness

Monitor whether one site systematically under-collects.

---

# 37. Timepoint Completeness

Monitor whether later follow-up declines.

---

# 38. Missingness Is Not Automatically Error

Missing data may arise from:

- nonresponse;
- dropout;
- unavailable source;
- inapplicability;
- technical failure;
- skipped item;
- protocol rule;
- participant refusal;
- lost specimen;
- administrative delay;
- extraction failure.

---

# 39. Missingness Reason

Record when known:

```yaml
missingness_event:
  unit_id:
  variable:
  timepoint:
  missing_reason:
  evidence:
  recoverable:
  protocol_consequence:
  analysis_consequence:
```

---

# 40. Missingness Status

Use:

- `EXPECTED`
- `EXPLAINED`
- `UNEXPLAINED`
- `POTENTIALLY_SYSTEMATIC`
- `RECOVERABLE`
- `IRRECOVERABLE`
- `UNKNOWN`

---

# 41. Recovery Attempt

Recovery must be scientifically and ethically permissible.

---

# 42. No Fabricated Recovery

Do not impute or invent missing source data during collection monitoring.

---

# 43. Late Data Receipt

Distinguish delayed receipt from true missingness.

---

# 44. Participant Flow Monitoring

Where relevant:

```text
SCREENED
↓
ELIGIBLE
↓
CONSENTED
↓
ENROLLED
↓
ALLOCATED
↓
FOLLOWED
↓
OUTCOME AVAILABLE
```

---

# 45. Participant Flow Record

```yaml
participant_flow:
  screened:
  eligible:
  consented:
  enrolled:
  allocated:
  completed:
  withdrawn:
  lost_to_followup:
  excluded_after_enrollment:
```

---

# 46. Recruitment Rate

Do not interpret rate without denominator and time window.

---

# 47. Recruitment Shortfall

Potential routes:

- `research-execution-manager`
- `sampling-strategy`
- `deviation-risk-monitor`
- `research-progress-auditor`

---

# 48. Recruitment Overrun

Do not exceed approved limits without appropriate review.

---

# 49. Attrition Monitoring

Track who leaves, when, and why if known.

---

# 50. Attrition Is Not Automatically Random

Carry forward to analysis planning.

---

# 51. Loss to Follow-Up

Track attempts and known reasons.

---

# 52. Withdrawal

Respect participant rights.

Do not infer motive.

---

# 53. Specimen Flow Monitoring

```text
COLLECTED
↓
LABELED
↓
TRANSPORTED
↓
RECEIVED
↓
PROCESSED
↓
STORED
↓
ASSAYED
↓
ARCHIVED / DISPOSED
```

---

# 54. Specimen Integrity

Monitor:

- label;
- volume;
- temperature;
- transport time;
- storage;
- freeze-thaw;
- contamination;
- chain of custody.

---

# 55. Specimen Loss

Document exact stage of loss.

---

# 56. Laboratory Collection Monitoring

Track:

- batch;
- run;
- operator;
- instrument;
- reagent lot;
- control status;
- raw output;
- rerun.

---

# 57. Laboratory Failure

Do not hide failed runs.

---

# 58. Rerun Trigger

Reruns require documented rationale.

---

# 59. Rerun Bias Guard

Do not selectively rerun unfavorable values.

---

# 60. Instrument Fidelity

Monitor:

- instrument version;
- calibration;
- operating range;
- firmware;
- administration mode;
- scoring rule.

---

# 61. Instrument Change

Assess comparability before combining data.

---

# 62. Calibration Failure

Potentially route to:

`protocol-adherence-monitor`

and:

`data-quality-auditor`

---

# 63. Survey Collection Monitoring

Monitor:

- invitations;
- responses;
- response window;
- duplicates;
- partial responses;
- device or mode;
- branching;
- item nonresponse.

---

# 64. Survey Response Rate

Report numerator and denominator definition.

---

# 65. Duplicate Response

Do not delete automatically.

---

# 66. Qualitative Collection Monitoring

Monitor:

- interview completion;
- recording success;
- transcript completeness;
- field-note continuity;
- contextual metadata;
- sampling progression.

---

# 67. Saturation / Information Power

Do not convert a qualitative stopping rationale into a mechanical number without methodological justification.

---

# 68. Interview Failure

Track failed recording, interruption, or unusable transcript.

---

# 69. Observation Data

Monitor date, context, observer, duration, and protocol.

---

# 70. Secondary Data Receipt

Track:

- request date;
- receipt date;
- source;
- version;
- coverage period;
- schema;
- permission;
- exclusions;
- update date.

---

# 71. Secondary Data Version

Do not combine versions silently.

---

# 72. Registry Data

Track extraction criteria and registry update cycle.

---

# 73. Administrative Data

Monitor coding and administrative process changes.

---

# 74. API Data Collection

Track:

- endpoint;
- query;
- date;
- parameters;
- pagination;
- response status;
- version.

---

# 75. Web Data Collection

Track access date, source, extraction method, and terms where relevant.

---

# 76. Sensor Data Collection

Monitor:

- uptime;
- sampling interval;
- clock synchronization;
- firmware;
- battery;
- signal loss;
- device assignment.

---

# 77. Imaging Data Collection

Monitor:

- acquisition protocol;
- device;
- sequence;
- operator;
- reconstruction;
- image completeness.

---

# 78. Sequencing Data Collection

Monitor:

- sample identity;
- library;
- run;
- platform;
- read yield;
- base quality;
- batch;
- failed samples.

---

# 79. Pharmacokinetic Collection

Monitor exact sampling times.

Timing deviations may materially affect PK inference.

---

# 80. Pharmacogenetic Collection

Monitor DNA identity, extraction quality, genotype call completeness, and assay batch.

---

# 81. Formulation Study Collection

Monitor batch-level physical and microbiological measurements.

---

# 82. Education Study Collection

Monitor class, assessment timing, instrument version, attendance, and intervention exposure.

---

# 83. Organizational Study Collection

Monitor access changes, participation changes, and organizational disruptions.

---

# 84. Field Research Collection

Monitor environmental conditions, location, access, and contextual events.

---

# 85. Multi-Site Collection

Monitor by site:

- activation;
- enrollment;
- completeness;
- timing;
- deviations;
- data submission;
- QC.

---

# 86. Site Comparison

Do not assume differences are errors.

Investigate context.

---

# 87. Site Outlier

A site-level outlier may indicate:

- population difference;
- procedure difference;
- coding difference;
- measurement difference;
- or genuine contextual heterogeneity.

---

# 88. Multi-Site Harmonization

Track common definitions and procedures.

---

# 89. Collection Drift

Collection drift may include:

- increasing missingness;
- shortened assessments;
- altered timing;
- changing instrument use;
- source substitution;
- staff workarounds.

---

# 90. Drift Route

Route procedural drift to:

`protocol-adherence-monitor`

---

# 91. Prospective Risk

Route likely future collection failure to:

`deviation-risk-monitor`

---

# 92. Progress Implication

Route milestone or timeline consequence to:

`research-progress-auditor`

---

# 93. Collection Quality vs Data Quality

Collection monitoring asks whether the evidence stream is being generated as intended.

`data-quality-auditor` asks whether the resulting dataset is scientifically fit for analysis.

---

# 94. Collection Complete but Poor Quality

Possible.

---

# 95. Collection Incomplete but Scientifically Usable

Possible.

Do not decide without analysis context.

---

# 96. Threshold Guard

Do not invent arbitrary completeness thresholds.

---

# 97. Critical Variable Missingness

Missingness in a critical variable may matter more than overall completion rate.

---

# 98. Primary Outcome Missingness

Must be explicit.

---

# 99. Differential Missingness

Monitor whether missingness differs by:

- group;
- site;
- time;
- exposure;
- outcome status;
- demographic category;
- device;
- operator.

---

# 100. Missingness Mechanism

Do not declare MCAR, MAR, or MNAR from operational monitoring alone.

Route analytical assessment to:

`analysis-planner`

---

# 101. Data Latency

Latency is time between real-world event and data availability.

---

# 102. Latency Risk

Long latency may delay monitoring or analysis.

---

# 103. Real-Time Data

Real-time availability does not imply validity.

---

# 104. Data Lock Readiness

Collection completion is one prerequisite for data lock.

---

# 105. Data Lock Gate

Before lock, verify:

- required collection ended;
- late data window closed;
- unresolved source discrepancies known;
- missingness documented;
- protocol deviations documented;
- data-quality audit planned or complete.

---

# 106. No Premature Lock

Do not lock simply to begin analysis sooner.

---

# 107. Reopening Collection

If reopened, preserve:

- reason;
- date;
- affected units;
- protocol version;
- registration impact;
- ethics impact.

---

# 108. Data Correction During Collection

Corrections should be traceable.

---

# 109. Source Correction

Preserve original value when required by governance.

---

# 110. Derived Variable

Do not silently compute derived variables as if they were collected source data.

---

# 111. Coding During Collection

Version coding rules.

---

# 112. Category Changes

Do not silently merge or redefine categories.

---

# 113. Unit Changes

Track measurement units.

---

# 114. Time Zone

Relevant for time-sensitive collection.

---

# 115. Date Format

Prevent ambiguous date parsing.

---

# 116. BLQ / LLOQ

Laboratory studies should preserve below-limit status rather than invent replacement values.

---

# 117. Detection Limit

Record method-specific limits where relevant.

---

# 118. Qualitative Redaction

Preserve raw record and governed redacted version distinctly.

---

# 119. Deidentification

Do not assume deidentification means anonymization.

---

# 120. Consent Scope

Collection must remain within authorized scope.

---

# 121. New Data Element

If a new variable is proposed during collection, assess:

- scientific need;
- consent;
- ethics;
- registration;
- burden;
- governance;
- analysis impact.

---

# 122. New Data Element Route

Potentially route to:

- `ethics-regulatory-gate`
- `registration-preregistration-builder`
- `research-data-governance`
- `protocol-builder`

---

# 123. Extra Collection Burden

Do not add participant burden casually.

---

# 124. Participant Refusal

Respect refusal and document without coercion.

---

# 125. Safety Signal

Safety concerns override ordinary collection scheduling.

---

# 126. Collection Pause

Pause when:

- permission lapses;
- source integrity fails;
- instrument failure invalidates measurement;
- participant risk changes;
- protocol ambiguity is material;
- major identifier failure occurs;
- data leakage occurs;
- specimen integrity fails systematically.

---

# 127. Collection Stop

Stop may be justified when recovery is not scientifically or ethically defensible.

---

# 128. Pause Status

Use:

- `PAUSE_RECOMMENDED`
- `PAUSE_REQUIRED`
- `NO_PAUSE`
- `COMPETENT_REVIEW_REQUIRED`

---

# 129. Recovery Status

Use:

- `RECOVERABLE`
- `PARTIALLY_RECOVERABLE`
- `IRRECOVERABLE`
- `UNKNOWN`

---

# 130. Collection Problem Record

```yaml
collection_issue:
  issue_id:
  date:
  site:
  source:
  affected_units:
  problem_type:
  severity:
  recurrence:
  evidence:
  recovery_status:
  protocol_implication:
  governance_implication:
  data_quality_implication:
  analysis_implication:
  action:
  status:
```

---

# 131. Collection Issue Types

Use:

- `MISSING_DATA`
- `DELAYED_DATA`
- `LOST_SOURCE`
- `IDENTIFIER_PROBLEM`
- `LINKAGE_PROBLEM`
- `INSTRUMENT_FAILURE`
- `SPECIMEN_FAILURE`
- `TIMING_DEVIATION`
- `PROTOCOL_DEVIATION`
- `SITE_VARIATION`
- `STAFF_VARIATION`
- `SOURCE_CHANGE`
- `ACCESS_FAILURE`
- `PERMISSION_FAILURE`
- `DATA_TRANSFER_FAILURE`
- `UNKNOWN`

---

# 132. Severity

Use:

- `MINOR`
- `MODERATE`
- `MAJOR`
- `CRITICAL`
- `UNKNOWN`

---

# 133. Recurrence

Use:

- `ISOLATED`
- `REPEATED`
- `SYSTEMATIC`
- `UNKNOWN`

---

# 134. Monitoring Frequency

Set frequency based on:

- study risk;
- data velocity;
- intervention risk;
- sample vulnerability;
- site count;
- collection complexity;
- prior problems;
- source fragility.

---

# 135. High-Velocity Data

May require automated or frequent monitoring.

---

# 136. Low-Velocity Data

May be reviewed at milestones.

---

# 137. Triggered Monitoring

Triggers include:

- first participant;
- first specimen;
- first site;
- first data transfer;
- instrument change;
- new staff;
- amendment;
- repeated missingness;
- safety event;
- unexpected dropout.

---

# 138. Monitoring Dashboard

```yaml
collection_dashboard:
  overall_status:
  active_units:
  completed_units:
  primary_outcome_completion:
  critical_missingness:
  delayed_units:
  lost_units:
  site_alerts:
  instrument_alerts:
  protocol_alerts:
  governance_alerts:
  next_review:
```

---

# 139. Collection Performance Metrics

Use only with explicit denominator and interpretation.

Examples:

- recruitment rate;
- visit completion rate;
- specimen completion rate;
- survey completion rate;
- data latency;
- source discrepancy rate.

---

# 140. Metric Guard

Metrics summarize operations.

They do not prove scientific validity.

---

# 141. Green Dashboard Guard

An “all green” dashboard cannot override known scientific problems.

---

# 142. Manual Review

Automated flags should allow human review.

---

# 143. AI-Assisted Monitoring

AI may help flag:

- missingness patterns;
- site differences;
- timing anomalies;
- duplicate text;
- inconsistent metadata.

AI should not automatically delete, impute, exclude, or classify scientifically material observations.

---

# 144. AI Verification

Material AI-generated alerts require verification.

---

# 145. No Result-Driven Collection Change

Do not alter collection because interim results are unfavorable unless a prespecified adaptive rule or justified amendment permits it.

---

# 146. No Convenience-Driven Collection Change

Do not shorten procedures merely to increase completion.

---

# 147. No Silent Instrument Change

Document instrument substitutions.

---

# 148. No Silent Source Change

Document data-source substitutions.

---

# 149. No Silent Timepoint Change

Document schedule changes.

---

# 150. No Silent Eligibility Change

Route to protocol review.

---

# 151. No Silent Outcome Change

Route to registration and protocol review.

---

# 152. No Selective Collection

Do not preferentially collect easier or more favorable observations.

---

# 153. No Selective Follow-Up

Do not follow only participants likely to produce favorable outcomes.

---

# 154. No Silent Exclusion

Do not remove problematic records during collection monitoring.

---

# 155. No Fabricated Completeness

Do not call a record complete if required data are missing.

---

# 156. No Fabricated Source

Do not infer an unavailable source value.

---

# 157. No Fabricated Consent

Permission status must be verified.

---

# 158. No Fabricated Timestamp

Timing should come from actual records when relevant.

---

# 159. No Fabricated Specimen Status

Do not call a specimen processed, stored, or assayed without evidence.

---

# 160. No Fabricated Response

Never reconstruct missing questionnaire responses from assumptions.

---

# 161. No Premature “Collection Complete”

Collection completes only when defined closure criteria are met.

---

# 162. Closure Criteria

May include:

- target reached or justified stop;
- final follow-up window closed;
- late data window closed;
- source reconciliation complete;
- unresolved collection issues documented;
- amendments closed;
- participant flow reconciled.

---

# 163. Collection Closure Status

Use:

- `OPEN`
- `CLOSING`
- `CLOSED_PENDING_RECONCILIATION`
- `CLOSED`
- `PREMATURELY_CLOSED`

---

# 164. Reconciliation

Compare:

- planned units;
- collected units;
- missing units;
- excluded units;
- duplicate units;
- withdrawn units;
- lost units.

---

# 165. Collection Reconciliation Record

```yaml
collection_reconciliation:
  planned:
  attempted:
  collected:
  complete:
  incomplete:
  missing:
  lost:
  excluded:
  unresolved:
```

---

# 166. Handoff to Data Quality Auditor

Provide:

- collection status;
- source provenance;
- identifier issues;
- missingness reasons;
- timing issues;
- site variation;
- instrument changes;
- protocol deviations;
- recovery attempts.

---

# 167. Handoff to Analysis Planner

Provide:

- achieved sample;
- actual timepoints;
- missingness profile;
- attrition;
- collection deviations;
- source changes;
- site variation;
- measurement changes.

---

# 168. Handoff to Result Interpreter

Carry material collection limitations forward.

---

# 169. Handoff to Reproducibility Auditor

Preserve collection provenance and execution history.

---

# 170. Handoff to Research Progress Auditor

Provide milestone-level collection status.

---

# 171. Relationship with Research Execution Manager

`research-execution-manager` coordinates the overall study.

`data-collection-monitor` evaluates the active evidence-generation stream.

---

# 172. Relationship with Protocol Adherence Monitor

Collection departures that violate or may violate protocol route to:

`protocol-adherence-monitor`

---

# 173. Relationship with Deviation Risk Monitor

Potential future collection failure routes to:

`deviation-risk-monitor`

---

# 174. Relationship with Research Progress Auditor

Collection delays or completion affect scientific progress status.

---

# 175. Relationship with Research Data Governance

`research-data-governance` controls provenance, access, versioning, storage, and transformations.

This skill monitors whether those governed data actually arrive or are generated.

---

# 176. Relationship with Data Quality Auditor

`data-quality-auditor` evaluates the resulting dataset after or during collection.

This skill detects collection-level issues before or as they enter the dataset.

---

# 177. Relationship with Ethics Regulatory Gate

Consent, privacy, access, or participant-protection problems route to:

`ethics-regulatory-gate`

---

# 178. Relationship with Registration Preregistration Builder

New outcomes, altered timepoints, or changed collection commitments route to:

`registration-preregistration-builder`

---

# 179. Relationship with Sampling Strategy

Recruitment or sample-source problems may require sampling review.

---

# 180. Relationship with Instrument Design

Measurement-system failure may require instrument revision.

---

# 181. Relationship with Protocol Builder

Systematic collection infeasibility may require protocol amendment.

---

# 182. Relationship with Analysis Planner

Actual collected data constrain valid analysis.

---

# 183. Relationship with Statistical Method Selector

Collection limitations may alter feasible statistical methods.

---

# 184. Relationship with Qualitative Analysis

Qualitative collection metadata should inform analytic interpretation.

---

# 185. Relationship with Mixed Method Analysis

Monitor whether both strands reach the planned integration point.

---

# 186. Relationship with Meta Analysis

For evidence synthesis, “collection” may include article retrieval, extraction, and effect-data acquisition.

---

# 187. Relationship with Manuscript Architect

Methods structure should reflect actual collection.

---

# 188. Relationship with Manuscript Writer

Do not report planned data as if collected.

---

# 189. Relationship with Manuscript Auditor

Audit should compare reported sample and variables with collection records.

---

# 190. Relationship with Reviewer Response

Reviewer-requested new collection should be clearly labeled as post-submission work.

---

# 191. Relationship with Research Roadmap

Collection feasibility informs future-stage design.

---

# 192. Stop Conditions

Escalate or return when:

- permission is uncertain;
- critical identifiers fail;
- protocol deviation is material;
- primary outcome collection fails systematically;
- source provenance is unresolved;
- collection becomes scientifically nonrepresentative;
- safety is compromised;
- or the data stream cannot support the research question.

Possible statuses:

- `RETURN_TO_RESEARCH_EXECUTION_MANAGER`
- `RETURN_TO_PROTOCOL_ADHERENCE_MONITOR`
- `RETURN_TO_ETHICS_REGULATORY_GATE`
- `RETURN_TO_RESEARCH_DATA_GOVERNANCE`
- `RETURN_TO_SAMPLING_STRATEGY`
- `RETURN_TO_INSTRUMENT_DESIGN`
- `COLLECTION_REQUIRES_REVISION`
- `PAUSE_COLLECTION`
- `STOP_COLLECTION`

---

# 193. User Request Routing

Activate when users ask:

- “Is data collection on track?”
- “Why are so many values missing?”
- “Can we still use these data?”
- “Which site is falling behind?”
- “Did we collect the primary outcome?”
- “Should we extend recruitment?”
- “Do we need to recollect this?”
- “Is this missingness operational or scientific?”
- “Can we close data collection?”
- “What should be monitored during collection?”
- “How do we know the dataset is ready for analysis?”
- “What should be handed to the analyst?”

---

# 194. Output Package

Produce, as needed:

1. Collection Readiness Decision
2. Collection Context
3. Planned Data Element Register
4. Collection Unit Register
5. Participant / Sample Flow
6. Completeness Summary
7. Missingness Summary
8. Timing Summary
9. Source Provenance Summary
10. Site Monitoring Summary
11. Collection Issue Register
12. Recovery Plan
13. Collection Dashboard
14. Closure Decision
15. Reconciliation Record
16. Data Quality Handoff
17. Analysis Handoff
18. Reproducibility Handoff

---

# 195. Final Collection Rule

Never call data collection successful merely because many records exist.

Never call data complete merely because forms are submitted.

Never treat missingness as random without evidence.

Never hide failed collection attempts.

Never silently change sources, instruments, timepoints, eligibility rules, or outcome definitions.

Never delete inconvenient observations during collection monitoring.

Never let software convenience or desired results redefine what should be collected.

The goal is a transparent evidence stream whose provenance, completeness, timing, missingness, and limitations are scientifically visible.

---

# Success Criterion

`data-collection-monitor` succeeds when active research data collection has been monitored as a traceable scientific evidence-generation process whose planned variables, sources, participants or samples, sites, timepoints, instruments, identifiers, provenance, completeness, timeliness, missingness, attrition, specimen flow, source continuity, linkage, collection failures, recovery attempts, site variation, instrument changes, collection drift, protocol implications, governance implications, data-quality implications, analytical implications, closure criteria, and downstream handoffs are explicitly documented; when collected data are distinguished from valid data, delayed data from missing data, expected missingness from unexplained or potentially systematic missingness, operational completion from scientific completeness, and source records from derived analysis data; when protocol departures route to `protocol-adherence-monitor`, prospective execution threats to `deviation-risk-monitor`, milestone consequences to `research-progress-auditor`, provenance and access problems to `research-data-governance`, participant-permission problems to `ethics-regulatory-gate`, prospective commitment changes to `registration-preregistration-builder`, data-validity issues to `data-quality-auditor`, and analytical consequences to `analysis-planner`; when result-driven recollection, silent source substitution, silent instrument change, hidden exclusion, fabricated completeness, fabricated source values, arbitrary missingness rules, premature collection closure, publication pressure, reviewer pressure, and software-driven collection decisions are prevented; and when another competent researcher can determine exactly what data were planned, what was actually collected or received, from whom or what source, when and how collection occurred, what was missing or delayed, why problems arose where known, what recovery was attempted, what limitations remain, and whether the resulting evidence stream can defensibly proceed to data-quality auditing and analysis.
