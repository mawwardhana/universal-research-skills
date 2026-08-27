---
name: research-execution-manager
description: Coordinate, document, and audit the scientific execution of an approved research plan after methodology, protocol, governance, ethics, registration, sampling, measurement, and data-handling requirements are sufficiently defined. Use when a study is ready to move from design into implementation and the researcher needs a transparent execution architecture for activities, scientific milestones, dependencies, decision gates, responsible roles, evidence of completion, deviations, pauses, amendments, data-collection readiness, and downstream handoffs without allowing project-management convenience, deadlines, software, publication targets, or undocumented improvisation to redefine the approved scientific plan.
---

# Research Execution Manager

## Purpose

`research-execution-manager` converts an approved, governable research design into a traceable implementation architecture.

Its central question is:

> What must actually happen, in what scientifically justified order, under which permissions and dependencies, with what evidence of completion, and what should occur when the implemented study begins to diverge from the approved plan?

The core execution chain is:

```text
APPROVED SCIENTIFIC PLAN
        ↓
EXECUTION READINESS
        ↓
SCIENTIFIC DEPENDENCIES
        ↓
ACTIVITIES / WORKSTREAMS
        ↓
EVIDENCE OF COMPLETION
        ↓
PROTOCOL / DATA / RISK MONITORING
        ↓
DECISION GATES
        ↓
PROCEED / REVISE / PAUSE / STOP
        ↓
DOWNSTREAM HANDOFF
```

This skill is not merely a project-management checklist.

It is a scientific execution-control layer.

---

# 1. Core Principles

Preserve the following distinctions:

```text
EXECUTION ≠ PROJECT MANAGEMENT
APPROVED ≠ AUTOMATICALLY READY
READY ≠ STARTED
STARTED ≠ COMPLETED
COMPLETED ≠ VERIFIED
DEADLINE ≠ SCIENTIFIC MILESTONE
PROGRESS ≠ PUBLICATION COUNT
DEVIATION ≠ FAILURE
CHANGE ≠ AUTHORIZED AMENDMENT
ADMINISTRATIVE PRESSURE ≠ SCIENTIFIC JUSTIFICATION
TASK COMPLETION ≠ SCIENTIFIC VALIDITY
```

The execution plan must preserve the scientific record established upstream.

---

# 2. Activation Gate

Use `research-execution-manager` when:

- the study design is sufficiently stable;
- the protocol is sufficiently defined;
- ethics or regulatory requirements are known;
- registration or preregistration status is known when relevant;
- sampling requirements are known;
- measurement or instrument requirements are known;
- data-governance requirements are known;
- implementation activities must be sequenced;
- multiple workstreams must be coordinated;
- scientific milestones or decision gates are needed;
- the researcher needs to know whether the study is actually ready to start;
- implementation has already started and needs traceable control;
- or execution must be resumed after a pause, amendment, disruption, or reviewer-driven extension.

Do not activate execution simply because a calendar start date has arrived.

---

# 3. Required Upstream Context

Use, when available:

- research question;
- objectives;
- hypotheses where appropriate;
- theoretical framework;
- conceptual framework;
- methodology;
- protocol;
- sampling strategy;
- instrument or measurement plan;
- statistical or qualitative analysis requirements;
- ethics approval or status;
- regulatory authorization;
- registration or preregistration;
- data-governance architecture;
- data-management plan;
- research roadmap;
- funding constraints;
- collaborator roles;
- facility or laboratory dependencies;
- recruitment dependencies;
- equipment dependencies;
- external data dependencies;
- and institutional constraints.

Do not invent missing approvals, resources, participants, collaborators, facilities, or datasets.

---

# 4. Execution Readiness Status

Use:

- `READY_TO_EXECUTE`
- `READY_WITH_CONDITIONS`
- `NOT_READY_SCIENTIFIC`
- `NOT_READY_METHOD`
- `NOT_READY_PROTOCOL`
- `NOT_READY_ETHICS`
- `NOT_READY_REGULATORY`
- `NOT_READY_REGISTRATION`
- `NOT_READY_DATA_GOVERNANCE`
- `NOT_READY_INSTRUMENT`
- `NOT_READY_SAMPLING`
- `NOT_READY_RESOURCE`
- `NOT_READY_PARTNERSHIP`
- `NOT_READY_INFRASTRUCTURE`
- `BLOCKED`
- `STATUS_UNCERTAIN`

---

# 5. Execution Readiness Gate

Before implementation begins, verify:

```text
Question stable?
        ↓
Methodology approved?
        ↓
Protocol usable?
        ↓
Ethics / regulatory permission satisfied?
        ↓
Registration requirements satisfied?
        ↓
Sampling operational?
        ↓
Measurement operational?
        ↓
Data governance operational?
        ↓
Resources available?
        ↓
Dependencies satisfied?
        ↓
READY
```

A failure at any gate may require return to the appropriate upstream skill.

---

# 6. Scientific vs Administrative Readiness

Scientific readiness concerns whether the planned research can be executed validly.

Administrative readiness concerns whether paperwork, scheduling, procurement, contracts, or logistics are complete.

Do not allow administrative readiness to substitute for scientific readiness.

---

# 7. Execution Unit

An execution unit is a scientifically meaningful activity that can be:

- started;
- monitored;
- completed;
- verified;
- paused;
- repeated;
- revised;
- or terminated.

Examples include:

- recruit participants;
- randomize eligible participants;
- collect baseline measurements;
- prepare formulation batches;
- perform an assay;
- administer intervention;
- retrieve records;
- collect follow-up outcomes;
- run quality control;
- perform sequencing;
- construct a dataset;
- lock the analysis dataset;
- or archive source material.

---

# 8. Execution Unit Record

Use:

```yaml
execution_unit:
  unit_id:
  title:
  scientific_purpose:
  upstream_requirement:
  dependencies:
  responsible_role:
  planned_start:
  planned_end:
  actual_start:
  actual_end:
  permission_status:
  protocol_version:
  evidence_required:
  completion_status:
  verification_status:
  deviation_status:
  notes:
```

---

# 9. Execution Status

Use:

- `NOT_STARTED`
- `READY`
- `ACTIVE`
- `PAUSED`
- `BLOCKED`
- `COMPLETED_UNVERIFIED`
- `COMPLETED_VERIFIED`
- `REQUIRES_REVISION`
- `TERMINATED`
- `SUPERSEDED`
- `NOT_APPLICABLE`

---

# 10. Evidence of Completion

Never mark an execution unit complete merely because someone reports that it was done.

Use evidence appropriate to the activity, such as:

- source records;
- laboratory logs;
- signed forms;
- timestamps;
- instrument exports;
- recruitment logs;
- specimen logs;
- data-receipt records;
- database audit trails;
- protocol checklists;
- versioned files;
- meeting decisions;
- amendment approvals;
- or verified analysis artifacts.

---

# 11. Completion vs Verification

Distinguish:

```text
COMPLETED
activity reportedly occurred

VERIFIED
available evidence supports that the activity occurred as represented
```

Do not collapse these statuses.

---

# 12. Execution Dependency

Each activity may depend on:

- scientific prerequisite;
- protocol prerequisite;
- ethics prerequisite;
- regulatory prerequisite;
- registration prerequisite;
- recruitment prerequisite;
- specimen prerequisite;
- data prerequisite;
- infrastructure prerequisite;
- equipment prerequisite;
- reagent prerequisite;
- training prerequisite;
- external collaborator prerequisite;
- funding prerequisite;
- or temporal prerequisite.

---

# 13. Dependency Record

```yaml
dependency:
  dependency_id:
  source_unit:
  target_unit:
  dependency_type:
  mandatory:
  status:
  evidence:
  unresolved_issue:
```

---

# 14. Hard vs Soft Dependency

Hard dependency:

> execution should not proceed without it.

Soft dependency:

> execution can proceed but with reduced efficiency, increased uncertainty, or an explicitly accepted risk.

Do not treat all dependencies as equivalent.

---

# 15. Scientific Dependency

A scientific dependency exists when later validity depends on earlier evidence or decisions.

Examples:

- calibration before measurement;
- eligibility verification before enrollment;
- intervention preparation before administration;
- assay QC before interpretation;
- genotype QC before association analysis;
- dataset lock before confirmatory analysis.

---

# 16. Ethics Dependency

If an activity requires approval, consent, authorization, or amendment, route unresolved permission to:

`ethics-regulatory-gate`

Do not proceed by assumption.

---

# 17. Registration Dependency

If implementation changes a preregistered or registered element, route to:

`registration-preregistration-builder`

Do not overwrite the prospective record silently.

---

# 18. Data Governance Dependency

If the activity creates, receives, transforms, links, shares, or archives research data, coordinate with:

`research-data-governance`

---

# 19. Data Quality Dependency

If collected or transformed data must be evaluated for quality before downstream use, route to:

`data-quality-auditor`

---

# 20. Protocol Dependency

Execution should use a defined current protocol version.

If the protocol is ambiguous or incomplete, route to:

`protocol-builder`

---

# 21. Sampling Dependency

If recruitment or selection cannot be operationalized, route to:

`sampling-strategy`

---

# 22. Measurement Dependency

If instrument, assay, rubric, device, scale, extraction form, interview guide, or measurement procedure is unresolved, route to:

`instrument-design`

---

# 23. Analysis Dependency

Execution planning should anticipate analysis-required data structure but must not let preferred statistical results redefine collection.

Coordinate with:

`analysis-planner`

---

# 24. Execution Workstream

A workstream groups related execution units.

Examples:

- recruitment;
- intervention;
- laboratory;
- measurement;
- data extraction;
- follow-up;
- quality control;
- data management;
- analysis preparation;
- regulatory reporting;
- archival preparation.

---

# 25. Parallel Workstreams

Parallel execution is allowed when dependencies permit.

Use:

```text
                 ┌── Workstream A
APPROVED PLAN ───┼── Workstream B
                 └── Workstream C
                         ↓
                  Integration Gate
```

---

# 26. Workstream Integration Gate

Before outputs from multiple workstreams are combined, verify:

- common identifiers;
- compatible versions;
- synchronized definitions;
- compatible time windows;
- matching participant or sample logic;
- compatible provenance;
- and resolved deviations.

---

# 27. Execution Timeline

A timeline should represent scientific dependency before calendar convenience.

Avoid:

```text
Month 1 = task A
Month 2 = task B
Month 3 = task C
```

unless the scientific dependency actually supports that order.

---

# 28. Scientific Milestone

A scientific milestone is a defensible change in evidence state.

Examples:

- protocol finalized;
- ethics permission obtained;
- recruitment threshold achieved;
- assay validated;
- minimum follow-up completed;
- dataset locked;
- prespecified QC passed;
- primary analysis completed;
- reproducibility audit passed.

---

# 29. Administrative Milestone

Examples:

- purchase order submitted;
- meeting held;
- travel booked;
- invoice processed;
- report template prepared.

These may matter operationally but are not scientific milestones.

---

# 30. Milestone Record

```yaml
milestone:
  milestone_id:
  title:
  type:
  scientific_purpose:
  evidence_required:
  dependency:
  target_date:
  actual_date:
  status:
  consequence_if_missed:
```

---

# 31. Decision Gate

A decision gate determines what happens next.

Possible outcomes:

- `PROCEED`
- `PROCEED_WITH_CONDITIONS`
- `REVISE`
- `REPEAT`
- `PAUSE`
- `ESCALATE`
- `CHANGE_ROUTE`
- `STOP`
- `TERMINATE_BRANCH`
- `AWAIT_EVIDENCE`

---

# 32. Decision Gate Record

```yaml
decision_gate:
  gate_id:
  trigger:
  evidence_reviewed:
  criteria:
  outcome:
  rationale:
  authorized_by:
  downstream_route:
  timestamp:
```

---

# 33. No Automatic Proceed

Passing a calendar date is not a reason to proceed.

Proceed only when gate criteria are satisfied.

---

# 34. Pause Logic

Pause execution when:

- permissions expire;
- safety concerns arise;
- critical resources fail;
- protocol ambiguity becomes consequential;
- serious data integrity issues emerge;
- required monitoring fails;
- participant risk changes;
- major protocol deviation occurs;
- or required evidence is unavailable.

---

# 35. Stop Logic

Stopping can be scientifically correct.

Possible reasons include:

- unacceptable participant risk;
- invalid measurement system;
- irreparable protocol failure;
- impossible recruitment;
- exhausted sample source;
- regulatory prohibition;
- unusable data source;
- invalidated research question;
- infeasible intervention;
- failed validation gate;
- or scientific redundancy discovered during execution.

---

# 36. Termination Is Not Failure

An evidence-based stop may protect scientific integrity.

---

# 37. Execution Amendment

A material change to execution may require:

- protocol amendment;
- ethics amendment;
- registration amendment;
- sampling revision;
- instrument revision;
- data-governance revision;
- or analysis-plan revision.

Do not implement the change first and document it later unless urgent safety or regulatory circumstances require immediate action.

---

# 38. Deviation vs Amendment

Deviation:

> implementation differs from the approved plan.

Amendment:

> the approved plan is formally changed.

A deviation may trigger an amendment.

---

# 39. Deviation Detection

Route emerging or actual deviations to:

`protocol-adherence-monitor`

and when prospective risk is the issue:

`deviation-risk-monitor`

---

# 40. Data Collection Monitoring

Route active collection status, completeness, timeliness, instrument use, source-record continuity, and collection-level anomalies to:

`data-collection-monitor`

---

# 41. Research Progress Audit

Route milestone-level execution status and evidence-based progress review to:

`research-progress-auditor`

---

# 42. Reproducibility Relationship

Major implementation evidence should be preserved so that:

`reproducibility-auditor`

can later reconstruct what actually occurred.

---

# 43. Research Roadmap Relationship

`research-roadmap` defines cumulative long-term scientific progression.

`research-execution-manager` manages execution of the currently approved study or research stage.

Do not confuse the two.

---

# 44. Execution Passport

```yaml
research_execution_passport:
  study_id:
  protocol_version:
  ethics_status:
  regulatory_status:
  registration_status:
  data_governance_status:
  execution_readiness:
  active_workstreams:
  blocked_workstreams:
  completed_units:
  verified_units:
  active_deviations:
  active_amendments:
  current_risks:
  next_decision_gate:
  next_scientific_milestone:
  downstream_route:
```

---

# 45. Execution Plan Template

```yaml
execution_plan:
  study:
  current_version:
  scientific_goal:
  workstreams:
  dependencies:
  milestones:
  decision_gates:
  responsibilities:
  evidence_requirements:
  monitoring_requirements:
  pause_rules:
  stop_rules:
  amendment_rules:
  handoff_rules:
```

---

# 46. Responsibility Model

Record scientific roles, not merely names.

Possible roles:

- principal investigator;
- study coordinator;
- recruitment lead;
- laboratory lead;
- data manager;
- statistician;
- qualitative analyst;
- safety monitor;
- regulatory coordinator;
- external collaborator;
- independent verifier.

---

# 47. Responsibility Boundary

No role should silently authorize an activity outside their authority.

---

# 48. Segregation of Duties

Where appropriate, separate:

- data generation;
- data correction;
- analysis;
- outcome adjudication;
- safety review;
- verification.

---

# 49. Training Requirement

Execution may require evidence of:

- protocol training;
- instrument training;
- biosafety training;
- consent training;
- data-protection training;
- laboratory competency;
- software competency.

---

# 50. Competency Gate

Do not assign scientifically critical activities solely because a person is available.

---

# 51. Resource Readiness

Record:

- facility;
- instrument;
- device;
- assay;
- reagent;
- software environment;
- secure storage;
- recruitment channel;
- data access;
- staff availability.

---

# 52. Resource Verification

Availability should be verified when it materially affects execution.

---

# 53. External Dependency

Examples:

- hospital data release;
- registry access;
- sequencing provider;
- external laboratory;
- ethics committee;
- supplier;
- collaborator;
- government permit.

---

# 54. External Dependency Risk

Do not assume external actors will deliver on schedule.

---

# 55. Version Control

Execution should reference current versions of:

- protocol;
- consent;
- instrument;
- data dictionary;
- SOP;
- analysis plan;
- registration;
- ethics approval;
- intervention;
- case report form.

---

# 56. Superseded Version

When a version changes, preserve the prior version and its effective period.

---

# 57. Effective-Date Logic

A new version should not be treated as retroactively applicable unless authorized and scientifically defensible.

---

# 58. Execution Log

Maintain a chronological record of material execution events.

```yaml
execution_event:
  event_id:
  date_time:
  workstream:
  activity:
  actor_role:
  protocol_version:
  evidence:
  outcome:
  deviation:
  action_required:
```

---

# 59. Material Event

Examples:

- first participant enrolled;
- first specimen processed;
- instrument failure;
- protocol deviation;
- data source changed;
- recruitment paused;
- amendment approved;
- dataset received;
- batch failed;
- primary collection completed.

---

# 60. Nonmaterial Event

Routine operational detail may not require central logging if it has no scientific, ethical, data, or interpretive consequence.

---

# 61. Recruitment Execution

Track:

- screened;
- eligible;
- invited;
- consented;
- enrolled;
- allocated;
- completed;
- withdrew;
- lost to follow-up.

Do not infer reasons without evidence.

---

# 62. Recruitment Target

Distinguish:

- desired sample;
- minimum defensible sample;
- maximum approved sample;
- actual enrolled sample.

---

# 63. Recruitment Shortfall

A shortfall may require:

- extended recruitment;
- additional site;
- revised precision expectation;
- revised analysis;
- protocol amendment;
- or study termination.

Do not silently lower the scientific standard.

---

# 64. Recruitment Excess

Do not enroll beyond approved limits without authorization where applicable.

---

# 65. Participant Flow

Maintain traceable participant flow where relevant.

---

# 66. Specimen Flow

Maintain traceable specimen flow:

```text
COLLECTION
↓
LABELING
↓
TRANSPORT
↓
RECEIPT
↓
PROCESSING
↓
STORAGE
↓
ASSAY
↓
ARCHIVE / DISPOSAL
```

---

# 67. Specimen Chain of Custody

Use when identity, integrity, timing, or legal control matters.

---

# 68. Laboratory Execution

Track:

- batch;
- operator;
- reagent lot;
- instrument;
- calibration;
- controls;
- replicate;
- failure;
- rerun;
- output version.

---

# 69. Batch Failure

Do not hide failed batches.

---

# 70. Rerun Logic

A rerun should have a scientific or QC rationale, not a desired-result rationale.

---

# 71. Intervention Execution

Track:

- intervention version;
- dose or exposure;
- timing;
- adherence;
- co-interventions;
- deviations;
- safety events.

---

# 72. Control Condition

Protect control-condition integrity.

---

# 73. Blinding Integrity

Record when blinding is broken and why.

---

# 74. Randomization Integrity

Preserve allocation method and sequence protection.

---

# 75. Follow-Up Execution

Track scheduled vs completed follow-up.

---

# 76. Attrition Monitoring

Do not automatically treat attrition as random.

---

# 77. Outcome Collection

Primary outcome collection should be monitored for:

- completeness;
- timing;
- protocol fidelity;
- source verification;
- instrument consistency.

---

# 78. Secondary Outcome Collection

Maintain hierarchy and timing.

---

# 79. Safety Monitoring

Safety signals may override ordinary execution.

Route material concerns to the appropriate safety, ethics, clinical, or regulatory authority.

---

# 80. Adverse Event

Do not diagnose or classify an event beyond available evidence or authority.

---

# 81. Qualitative Execution

For qualitative work, monitor:

- recruitment;
- interview or observation conditions;
- consent;
- recording;
- field notes;
- reflexive logs;
- saturation/information-power logic;
- procedural deviations.

Do not force rigid execution where emergence is intrinsic to the design.

---

# 82. Mixed-Method Execution

Track strand timing, priority, dependency, and integration points.

---

# 83. Survey Execution

Track:

- invitation;
- response;
- duplicate prevention;
- eligibility;
- instrument version;
- incomplete responses;
- response window.

---

# 84. Secondary-Data Execution

Track:

- data request;
- data receipt;
- version;
- extraction date;
- permission;
- schema;
- linkage;
- exclusions;
- updates.

---

# 85. Administrative Data

Do not treat administrative records as scientifically self-explanatory.

---

# 86. Public Dataset

Public availability does not eliminate provenance, license, consent, or representativeness concerns.

---

# 87. Web Data

Track source, access date, extraction method, terms, and version where relevant.

---

# 88. API Data

Track query, endpoint, date, parameters, pagination, and response version where relevant.

---

# 89. Sensor Data

Track device version, calibration, sampling interval, missingness, clock synchronization, and firmware where relevant.

---

# 90. Imaging Data

Track acquisition protocol, device, operator, reconstruction, preprocessing, and deidentification where relevant.

---

# 91. Sequencing Execution

Track:

- sample;
- library;
- platform;
- run;
- read type;
- quality metrics;
- batch;
- reference version;
- pipeline version.

---

# 92. Pharmacokinetic Execution

Track:

- dosing;
- exact sampling times;
- assay;
- BLQ status;
- specimen handling;
- protocol deviations.

---

# 93. Pharmacogenetic Execution

Track:

- sample identity;
- DNA quality;
- genotyping method;
- call quality;
- replicate;
- assay batch;
- variant nomenclature;
- reference build.

---

# 94. Formulation Study Execution

Track:

- formula version;
- batch;
- raw materials;
- processing conditions;
- environmental conditions;
- physical tests;
- stability timepoint;
- microbiological testing.

---

# 95. Education Study Execution

Track:

- class/site;
- instructor;
- intervention exposure;
- assessment timing;
- instrument version;
- contamination;
- attrition.

---

# 96. Organizational Study Execution

Track access, participation, timing, organizational changes, and contextual disruptions.

---

# 97. Field Research Execution

Track location, access, environmental conditions, timing, contextual events, and safety.

---

# 98. Multi-Site Study

Each site should have:

- site status;
- local approval;
- protocol version;
- recruitment;
- training;
- deviations;
- data submission status.

---

# 99. Site Activation

Do not activate a site before local requirements are satisfied.

---

# 100. Site Suspension

Suspend when scientific or governance conditions require.

---

# 101. Multi-Site Harmonization

Monitor:

- protocol;
- instruments;
- timing;
- data definitions;
- laboratory methods;
- training;
- QC.

---

# 102. Central vs Local Procedures

Distinguish which activities are centralized and which are site-specific.

---

# 103. Execution Consistency

Consistency means scientifically equivalent implementation where equivalence is required.

It does not mean mechanically identical behavior across contexts.

---

# 104. Contextual Adaptation

A context-specific adaptation must remain within approved scientific boundaries or be formally amended.

---

# 105. Contamination

Track exposure of control or comparison groups to intervention components where relevant.

---

# 106. Fidelity

Fidelity may include:

- dose;
- duration;
- content;
- timing;
- delivery;
- receipt;
- enactment.

---

# 107. Fidelity Failure

A fidelity problem may change interpretation even when the study technically completes.

---

# 108. Execution Drift

Execution drift is gradual divergence from the protocol without a single obvious deviation.

Route to:

`protocol-adherence-monitor`

---

# 109. Risk Monitoring

Potential future execution failure should route to:

`deviation-risk-monitor`

---

# 110. Progress Monitoring

Milestone-level status should route to:

`research-progress-auditor`

---

# 111. Data Collection Monitoring Relationship

Collection-level execution should route to:

`data-collection-monitor`

---

# 112. No Duplicate Monitoring

Do not make `research-execution-manager` duplicate all specialized monitoring functions.

It coordinates them.

---

# 113. Monitoring Escalation

A monitor may return:

- no action;
- observation;
- corrective action;
- preventive action;
- amendment needed;
- pause;
- escalation;
- stop.

---

# 114. Corrective Action

Corrective action addresses an observed problem.

---

# 115. Preventive Action

Preventive action reduces risk before failure occurs.

---

# 116. CAPA Record

Where appropriate:

```yaml
capa:
  issue:
  root_cause:
  corrective_action:
  preventive_action:
  responsible_role:
  due_date:
  verification:
  effectiveness:
```

---

# 117. Root Cause

Do not assign root cause without evidence.

---

# 118. Urgent Action

Urgent safety or regulatory action may precede documentation.

But documentation should follow as soon as appropriate.

---

# 119. Evidence Hierarchy for Execution

Prefer direct evidence of execution over retrospective recollection when available.

---

# 120. Source Record

Source records should remain distinguishable from derived summaries.

---

# 121. Derived Execution Metric

Examples:

- recruitment rate;
- completion rate;
- protocol adherence rate;
- specimen failure rate;
- follow-up rate.

Do not let operational metrics substitute for scientific outcomes.

---

# 122. Dashboard Use

Dashboards may summarize execution.

They must not become the authoritative record unless their provenance and update logic are controlled.

---

# 123. Software Independence

Software can track execution but cannot determine scientific validity.

---

# 124. Automated Monitoring

Automated alerts should preserve:

- trigger logic;
- source;
- timestamp;
- threshold;
- false-positive handling;
- human review.

---

# 125. AI-Assisted Execution

AI may assist with:

- scheduling;
- summarization;
- anomaly flagging;
- document comparison;
- log review.

AI must not autonomously authorize scientific, ethical, regulatory, or safety decisions unless a competent governance framework explicitly permits it.

---

# 126. AI Output Verification

Material AI-generated execution decisions require human verification.

---

# 127. Confidentiality

Execution records may contain sensitive operational or participant information.

Apply appropriate access control.

---

# 128. Least Privilege

Provide only the access needed for the role.

---

# 129. Access Log

Maintain access traceability when scientifically, legally, or institutionally required.

---

# 130. Cross-Border Execution

Data, specimens, devices, or personnel moving across jurisdictions may require additional review.

---

# 131. Contractual Constraint

A collaboration agreement, data-use agreement, or material-transfer agreement may affect execution.

---

# 132. Intellectual Property

Do not let IP restrictions erase necessary scientific provenance.

---

# 133. Funding Constraint

Funding affects feasibility.

It should not silently change the scientific question.

---

# 134. Procurement Failure

If critical material cannot be obtained, reassess scientific equivalence before substitution.

---

# 135. Reagent Substitution

Document lot, supplier, formulation, validation, and comparability where relevant.

---

# 136. Instrument Substitution

Assess comparability before switching devices or platforms.

---

# 137. Site Change

A new site may require scientific and governance re-evaluation.

---

# 138. Staff Change

Critical staff replacement may require training and handover.

---

# 139. Handover Record

```yaml
handover:
  from_role:
  to_role:
  effective_date:
  active_tasks:
  unresolved_issues:
  protocol_version:
  data_access:
  records_transferred:
```

---

# 140. Pause Resume Gate

Before resuming a paused study, verify:

- permissions remain valid;
- current protocol version;
- staff competency;
- resource readiness;
- participant impact;
- data continuity;
- unresolved deviations;
- updated risks.

---

# 141. Resume Status

Use:

- `READY_TO_RESUME`
- `RESUME_WITH_CONDITIONS`
- `DO_NOT_RESUME`
- `REQUIRES_REVIEW`

---

# 142. Study Closure

Closure may include:

- end of recruitment;
- final follow-up;
- specimen disposition;
- source-data reconciliation;
- data lock;
- deviation closure;
- safety closure;
- regulatory notification;
- archive preparation.

---

# 143. Premature Closure

Document reason and consequence.

---

# 144. Data Lock

Data lock is a controlled transition.

Do not lock a dataset merely because analysis is desired.

---

# 145. Unlock

Any post-lock change should be traceable.

---

# 146. Execution-to-Analysis Handoff

Before handoff to `analysis-planner`, provide:

- dataset version;
- collection status;
- protocol deviations;
- missingness context;
- measurement changes;
- sample-flow information;
- exposure/intervention fidelity;
- unresolved data-quality issues;
- governance constraints.

---

# 147. Execution-to-Result Handoff

Do not let result interpretation begin without understanding major execution limitations.

---

# 148. Execution-to-Manuscript Handoff

Provide:

- actual protocol version;
- actual sample;
- actual timelines;
- deviations;
- amendments;
- fidelity;
- data quality;
- losses;
- interruptions;
- analysis dataset version.

---

# 149. Execution-to-Reproducibility Handoff

Provide the evidence trail needed to reconstruct implementation.

---

# 150. Execution-to-Roadmap Handoff

Unexpected feasibility or implementation findings may inform the next research stage.

---

# 151. No Outcome-Driven Execution Change

Do not alter collection or execution because preliminary findings are unfavorable unless there is a prespecified adaptive rule or a scientifically justified amendment.

---

# 152. No Convenience-Driven Protocol Drift

Operational convenience does not justify silent deviation.

---

# 153. No Deadline-Driven Completion

Do not declare a stage complete because a report is due.

---

# 154. No Publication-Driven Completion

Do not close collection early merely to submit a manuscript unless scientifically and ethically justified.

---

# 155. No Reviewer-Driven Retrofitting

Reviewer requests may justify additional work but must not rewrite what originally occurred.

---

# 156. No Fabricated Completion

Never claim:

- recruitment completed;
- assay performed;
- data collected;
- QC passed;
- analysis rerun;
- amendment approved;
- protocol followed;
- data locked;
- or study closed

without evidence.

---

# 157. No Silent Failure

Failed activities should remain visible.

---

# 158. No Silent Repetition

Repeated measurements, reruns, recollection, reassays, or re-extractions should be documented when scientifically material.

---

# 159. No Selective Operational Reporting

Do not report only successful batches or completed cases when failures affect interpretation.

---

# 160. No Responsibility Ambiguity

Critical tasks should have explicit accountable roles.

---

# 161. No Permission-by-Assumption

If permission status is unclear, stop and route to `ethics-regulatory-gate`.

---

# 162. No Registration-by-Assumption

If registration status is unclear, route to `registration-preregistration-builder`.

---

# 163. No Data-Governance-by-Assumption

If data provenance or access control is unclear, route to `research-data-governance`.

---

# 164. No Quality-by-Assumption

If data quality is uncertain, route to `data-quality-auditor`.

---

# 165. No Reproducibility-by-Assumption

If reconstruction has not been tested, do not claim reproducibility.

---

# 166. Execution Risk Categories

Use:

- `SCIENTIFIC_RISK`
- `ETHICS_RISK`
- `REGULATORY_RISK`
- `SAFETY_RISK`
- `RECRUITMENT_RISK`
- `MEASUREMENT_RISK`
- `DATA_RISK`
- `QUALITY_RISK`
- `INFRASTRUCTURE_RISK`
- `SUPPLY_RISK`
- `PARTNERSHIP_RISK`
- `TIMELINE_RISK`
- `STAFF_RISK`
- `COMPUTATIONAL_RISK`
- `ARCHIVAL_RISK`

---

# 167. Risk Status

Use:

- `LOW`
- `MODERATE`
- `HIGH`
- `CRITICAL`
- `UNKNOWN`

---

# 168. Risk Escalation

High or critical risk should not be hidden behind overall “on track” status.

---

# 169. Progress Status

Use:

- `ON_TRACK`
- `ON_TRACK_WITH_RISK`
- `DELAYED`
- `BLOCKED`
- `PAUSED`
- `AT_RISK`
- `REQUIRES_REPLAN`
- `TERMINATED`

---

# 170. Progress Is Evidence-Based

Progress should reflect verified scientific milestones.

---

# 171. Research Execution Dashboard

A useful summary may include:

```yaml
execution_dashboard:
  overall_status:
  readiness:
  active_units:
  completed_verified:
  blocked_units:
  protocol_deviations:
  data_collection_status:
  high_risks:
  next_gate:
  next_milestone:
  permission_alerts:
  registration_alerts:
  data_quality_alerts:
```

---

# 172. Escalation Matrix

| Issue | Default Route |
|---|---|
| scientific design problem | `methodology-architect` |
| protocol ambiguity | `protocol-builder` |
| ethics or permission | `ethics-regulatory-gate` |
| registration / amendment | `registration-preregistration-builder` |
| data provenance | `research-data-governance` |
| data quality | `data-quality-auditor` |
| collection problem | `data-collection-monitor` |
| protocol adherence | `protocol-adherence-monitor` |
| deviation risk | `deviation-risk-monitor` |
| milestone progress | `research-progress-auditor` |
| analysis need | `analysis-planner` |
| reconstruction | `reproducibility-auditor` |

---

# 173. Cross-Skill Non-Substitution Rule

`research-execution-manager` coordinates but does not replace specialized skills.

---

# 174. Relationship with Methodology Architect

`methodology-architect` defines the scientifically defensible study design.

This skill operationalizes it.

---

# 175. Relationship with Problem-Solving Approach

The execution architecture should preserve the intended mechanism of solving the scientific problem.

---

# 176. Relationship with Protocol Builder

`protocol-builder` defines what should be done.

This skill tracks whether it can and does happen operationally.

---

# 177. Relationship with Sampling Strategy

Sampling assumptions become operational recruitment or selection tasks.

---

# 178. Relationship with Instrument Design

Measurement requirements become operational measurement tasks.

---

# 179. Relationship with Analysis Planner

Execution must generate the data structure required to answer the research question, not merely the data structure easiest to collect.

---

# 180. Relationship with Ethics Regulatory Gate

`ethics-regulatory-gate` determines permission.

This skill never overrides it.

---

# 181. Relationship with Registration Preregistration Builder

`registration-preregistration-builder` preserves prospective commitments and amendment history.

This skill tracks implementation against those commitments.

---

# 182. Relationship with Research Data Governance

`research-data-governance` governs data lifecycle.

This skill triggers and coordinates the points at which data are created, received, transformed, linked, or archived.

---

# 183. Relationship with Data Quality Auditor

`data-quality-auditor` evaluates governed data.

This skill must not declare data fit for analysis without that audit when such an audit is required.

---

# 184. Relationship with Reproducibility Auditor

`reproducibility-auditor` determines whether the record can be reconstructed.

This skill should preserve the evidence needed for that later audit.

---

# 185. Relationship with Research Roadmap

`research-roadmap` manages scientific progression across studies.

This skill manages execution within the current approved study or research stage.

---

# 186. Relationship with Result Interpreter

Major execution deviations should be visible to `result-interpreter`.

---

# 187. Relationship with Scientific Discussion

Implementation limitations may affect boundary conditions and explanation.

---

# 188. Relationship with Implication Builder

Practical implications should reflect what was actually implemented, not merely what was intended.

---

# 189. Relationship with Manuscript Architect

Methods architecture should reflect actual execution.

---

# 190. Relationship with Manuscript Writer

`manuscript-writer` must not transform planned methods into reported completed methods unless execution evidence supports them.

---

# 191. Relationship with Manuscript Auditor

`manuscript-auditor` should compare planned, executed, analyzed, and reported methods.

---

# 192. Relationship with Reviewer Simulator

Simulation may identify likely concerns about protocol fidelity, recruitment, missingness, implementation, or deviations.

---

# 193. Relationship with Reviewer Response

Reviewer-requested additional execution should be tracked as new work, not represented as original execution.

---

# 194. Relationship with Research Resume

When resuming a project, reconstruct current execution state before continuing.

---

# 195. Relationship with Prior Research Auditor

Prior implementation evidence may reveal unresolved execution weaknesses relevant to continuation.

---

# 196. Relationship with Research Trajectory Mapper

Execution experience can inform capability and feasibility of future research stages.

---

# 197. Relationship with Continuation Opportunity Finder

A scientifically attractive next study may still be operationally infeasible.

Execution evidence informs feasibility.

---

# 198. User Request Routing

Activate when users ask:

- “How do I start implementing this study?”
- “What should happen first?”
- “Is this study ready to begin?”
- “How do I manage the research execution?”
- “Which steps depend on which?”
- “What evidence proves this stage is complete?”
- “Can I continue despite this delay?”
- “Should I pause the study?”
- “What do I do after a protocol change?”
- “How do I track the actual implementation?”
- “How do I resume a paused study?”
- “How do I close the study?”
- “How do I hand the executed study to analysis?”

---

# 199. Execution Output Package

Produce, as needed:

1. Execution Readiness Decision
2. Execution Passport
3. Workstream Map
4. Scientific Dependency Map
5. Execution Unit Register
6. Milestone Register
7. Decision Gate Register
8. Responsibility Matrix
9. Evidence-of-Completion Requirements
10. Version Register
11. Execution Event Log
12. Risk Escalation Map
13. Pause / Resume Rules
14. Stop Rules
15. Amendment / Deviation Routing
16. Analysis Handoff Package
17. Reproducibility Handoff Package

---

# 200. Final Execution Rule

Never mark an activity complete because the calendar says it should be complete.

Never let operational convenience silently alter the approved science.

Never continue through unresolved permission, integrity, or safety failures.

Never hide implementation failure.

Never convert a deviation into an amendment retroactively without preserving history.

Never let publication or reviewer pressure rewrite what actually occurred.

Execution succeeds only when the actual study remains scientifically traceable from approved plan to verified implementation.

---

# Success Criterion

`research-execution-manager` succeeds when an approved and governable research plan has been translated into a transparent, evidence-based execution architecture whose scientific activities, workstreams, dependencies, responsibilities, protocol versions, permissions, resources, milestones, decision gates, evidence-of-completion requirements, monitoring needs, pause rules, stop rules, amendment routes, deviation routes, and downstream handoffs are explicitly defined; when readiness is distinguished from calendar start, reported completion from verified completion, administrative milestones from scientific milestones, deviations from amendments, and operational constraints from scientific justification; when ethics, regulatory, registration, sampling, measurement, data-governance, data-quality, analysis, and reproducibility requirements are routed to their proper upstream or downstream skills rather than silently assumed; when protocol drift, outcome-driven implementation changes, convenience-driven substitutions, hidden reruns, undocumented failures, premature completion, publication pressure, reviewer pressure, software defaults, and fabricated execution claims are prevented; when active collection, protocol adherence, deviation risk, and research progress can be handed transparently to `data-collection-monitor`, `protocol-adherence-monitor`, `deviation-risk-monitor`, and `research-progress-auditor`; when major implementation events remain versioned and reconstructable for `reproducibility-auditor`; and when another competent researcher can determine exactly what was intended, what was authorized, what was ready, what actually happened, what evidence supports completion, what changed, why it changed, what remained unresolved, and whether the study can defensibly proceed to the next scientific stage.
