---
name: protocol-adherence-monitor
description: Monitor, classify, document, and escalate adherence to an approved research protocol during implementation without confusing protocol fidelity with rigid procedural conformity. Use after research-execution-manager has established the execution architecture and while recruitment, intervention, measurement, laboratory work, fieldwork, data extraction, follow-up, or other implementation is active. This skill distinguishes expected variation, minor operational divergence, protocol deviation, material protocol violation, approved amendment, emergency action, and execution drift; preserves protocol-version history; assesses scientific, ethical, regulatory, safety, data-quality, and interpretive consequences; and routes issues to the appropriate governance, registration, execution, data, analysis, or reproducibility skill without silently rewriting the approved plan or fabricating compliance.
---

# Protocol Adherence Monitor

## Purpose

`protocol-adherence-monitor` determines whether the study is being implemented consistently with the current approved protocol and whether observed departures require documentation, correction, amendment, escalation, pause, or termination.

Its central question is:

> Is the research being implemented as authorized and scientifically intended, what departures from the current protocol have actually occurred, what do they mean, and what action is required before the study can defensibly continue?

The core monitoring chain is:

```text
CURRENT APPROVED PROTOCOL
        ↓
EXPECTED IMPLEMENTATION
        ↓
OBSERVED IMPLEMENTATION
        ↓
COMPARE
        ↓
NO MATERIAL ISSUE
   OR
VARIATION / DEVIATION / VIOLATION / DRIFT
        ↓
CONSEQUENCE ASSESSMENT
        ↓
CORRECT / PREVENT / AMEND / ESCALATE / PAUSE / STOP
        ↓
VERSIONED RECORD
        ↓
DOWNSTREAM SCIENTIFIC INTERPRETATION
```

This skill is not a compliance ritual.

It is a scientific fidelity and traceability layer.

---

# 1. Core Principles

Preserve these distinctions:

```text
ADHERENCE ≠ MECHANICAL UNIFORMITY
VARIATION ≠ DEVIATION
DEVIATION ≠ VIOLATION
DEVIATION ≠ MISCONDUCT
AMENDMENT ≠ RETROACTIVE ERASURE
EMERGENCY ACTION ≠ AUTOMATIC NONCOMPLIANCE
PROTOCOL VERSION ≠ TIMELESS INSTRUCTION
PLANNED FLEXIBILITY ≠ PROTOCOL DRIFT
DRIFT ≠ SINGLE EVENT
FREQUENCY ≠ SEVERITY
COMPLIANCE ≠ SCIENTIFIC VALIDITY
SCIENTIFIC VALIDITY ≠ ETHICS PERMISSION
```

---

# 2. Activation Gate

Use this skill when:

- research implementation is active;
- protocol adherence must be monitored;
- an execution step may have diverged from protocol;
- repeated small departures are emerging;
- staff interpret protocol differently;
- protocol version changed during execution;
- reviewer or auditor asks whether procedures were followed;
- a participant, specimen, intervention, measurement, data extraction, or follow-up event occurred outside the planned process;
- unexpected conditions required urgent action;
- or the scientific consequence of a departure is uncertain.

---

# 3. Upstream Requirements

Use, when available:

- current approved protocol;
- protocol version history;
- ethics approval or authorization;
- regulatory authorization;
- registration or preregistration;
- execution plan;
- sampling plan;
- instrument or measurement plan;
- intervention manual;
- SOPs;
- case report forms;
- data dictionary;
- deviation policy;
- monitoring plan;
- and prior deviation records.

---

# 4. Required Current-State Context

Record:

```yaml
protocol_context:
  study_id:
  protocol_version:
  version_effective_date:
  approval_status:
  ethics_status:
  regulatory_status:
  registration_status:
  active_sites:
  active_workstreams:
  monitor_date:
```

---

# 5. Adherence Question

For each monitored activity:

```text
What should have happened?
What actually happened?
Which version governed the activity?
Was the difference allowed?
If not, why did it occur?
What scientific or governance consequence follows?
```

---

# 6. Protocol Source Hierarchy

Prefer:

1. current approved protocol;
2. approved amendment;
3. current SOP;
4. approved study manual;
5. registration/preregistration record;
6. documented operational clarification.

Do not allow informal memory to override the controlled version.

---

# 7. Current Protocol Version

Every adherence assessment should identify the version in force at the time of the event.

---

# 8. Version Effective Period

Use:

```yaml
protocol_version_record:
  version:
  approved_date:
  effective_from:
  effective_to:
  superseded_by:
  approval_reference:
  notes:
```

---

# 9. No Retroactive Versioning

Do not apply a later amendment backward to make earlier departures appear compliant.

---

# 10. Expected Implementation

Translate protocol text into observable execution expectations.

---

# 11. Observable Protocol Element

Examples:

- eligibility check;
- consent timing;
- randomization;
- dose;
- visit window;
- specimen handling;
- assay condition;
- interview procedure;
- instrument version;
- data extraction rule;
- follow-up timing;
- exclusion rule;
- primary outcome timing.

---

# 12. Adherence Unit

Use:

```yaml
adherence_unit:
  unit_id:
  protocol_section:
  protocol_requirement:
  expected_action:
  observed_action:
  protocol_version:
  status:
  consequence:
  evidence:
  route:
```

---

# 13. Adherence Status

Use:

- `ADHERENT`
- `ADHERENT_WITH_ALLOWED_VARIATION`
- `POTENTIAL_DEVIATION`
- `CONFIRMED_DEVIATION`
- `MATERIAL_VIOLATION`
- `APPROVED_AMENDMENT_APPLIED`
- `EMERGENCY_DEPARTURE`
- `DRIFT_SUSPECTED`
- `DRIFT_CONFIRMED`
- `NOT_ASSESSABLE`
- `NOT_APPLICABLE`

---

# 14. Allowed Variation

Allowed variation is explicitly permitted by the protocol, SOP, predefined tolerance, or approved flexible design.

---

# 15. Operational Variation

A minor operational difference may be scientifically immaterial.

Document when relevant, but do not automatically classify it as protocol deviation.

---

# 16. Protocol Deviation

A protocol deviation is an unplanned departure from the approved protocol.

---

# 17. Material Protocol Violation

Use this category only when the departure materially affects:

- participant rights;
- safety;
- eligibility;
- intervention integrity;
- outcome validity;
- data integrity;
- interpretability;
- or regulatory compliance.

---

# 18. Emergency Departure

Urgent action taken to protect safety may be scientifically and ethically appropriate even when it departs from ordinary protocol.

---

# 19. Protocol Drift

Protocol drift is gradual, repeated, or normalized departure from the intended procedure.

---

# 20. Drift Signal

Signals include:

- repeated timing slippage;
- informal shortening of procedures;
- undocumented substitutions;
- inconsistent staff interpretation;
- progressive instrument changes;
- repeated waiver of eligibility checks;
- increasingly flexible exclusion decisions;
- or recurring “minor” deviations.

---

# 21. Single Event vs Pattern

Do not infer drift from one event.

Do not ignore repeated small departures merely because each is individually minor.

---

# 22. Event Record

```yaml
protocol_event:
  event_id:
  date_time:
  site:
  participant_or_sample_id:
  workstream:
  protocol_version:
  expected:
  observed:
  immediate_action:
  evidence:
  preliminary_classification:
```

---

# 23. Evidence Standard

Use direct records when possible:

- source documentation;
- instrument logs;
- specimen logs;
- timestamps;
- case report forms;
- consent forms;
- staff logs;
- laboratory records;
- audit trails;
- meeting decisions;
- approved amendments.

---

# 24. No Fabricated Compliance

Never mark adherence when evidence is unavailable.

---

# 25. Not Assessable

Use `NOT_ASSESSABLE` when the record cannot support a conclusion.

---

# 26. Consequence Dimensions

Assess:

- scientific;
- ethical;
- safety;
- regulatory;
- recruitment;
- measurement;
- intervention;
- data quality;
- analysis;
- interpretation;
- reproducibility;
- reporting.

---

# 27. Scientific Consequence

Ask whether the departure changes:

- exposure;
- timing;
- eligibility;
- measurement;
- comparison;
- causal contrast;
- precision;
- bias;
- missingness;
- generalizability.

---

# 28. Ethical Consequence

Ask whether the departure affects:

- consent;
- privacy;
- participant burden;
- risk;
- rights;
- withdrawal;
- vulnerable populations.

---

# 29. Regulatory Consequence

Ask whether formal reporting, notification, or amendment is required.

Route uncertain authority questions to:

`ethics-regulatory-gate`

---

# 30. Registration Consequence

If a prespecified element changes, route to:

`registration-preregistration-builder`

---

# 31. Data Governance Consequence

If the departure alters data access, linkage, transformation, identifiers, sharing, or retention, route to:

`research-data-governance`

---

# 32. Data Quality Consequence

If the departure may affect dataset validity, route to:

`data-quality-auditor`

---

# 33. Analysis Consequence

If the departure changes analysis assumptions, route to:

`analysis-planner`

---

# 34. Interpretation Consequence

Material deviations must be carried forward to:

`result-interpreter`

---

# 35. Reproducibility Consequence

Preserve evidence so:

`reproducibility-auditor`

can reconstruct what actually happened.

---

# 36. Severity Dimensions

Assess:

- magnitude;
- duration;
- recurrence;
- participant impact;
- safety impact;
- scientific impact;
- reversibility;
- detectability;
- scope;
- governance consequence.

---

# 37. Severity Status

Use:

- `NEGLIGIBLE`
- `MINOR`
- `MODERATE`
- `MAJOR`
- `CRITICAL`
- `UNKNOWN`

---

# 38. Recurrence Status

Use:

- `ISOLATED`
- `REPEATED`
- `SYSTEMATIC`
- `UNKNOWN`

---

# 39. Detectability

Was the problem:

- immediately visible;
- detected by monitoring;
- discovered during data review;
- discovered during analysis;
- discovered during audit;
- discovered during manuscript preparation;
- discovered during peer review?

---

# 40. Timing Matters

Late discovery does not erase the departure.

---

# 41. Corrective Action

Corrective action addresses the current deviation.

---

# 42. Preventive Action

Preventive action reduces recurrence.

---

# 43. CAPA

Where appropriate:

```yaml
capa:
  event_id:
  root_cause_status:
  corrective_action:
  preventive_action:
  responsible_role:
  due_date:
  completion_evidence:
  effectiveness_review:
```

---

# 44. Root Cause Status

Use:

- `CONFIRMED`
- `LIKELY`
- `POSSIBLE`
- `UNKNOWN`

---

# 45. No Root-Cause Guessing

Do not turn speculation into a confirmed root cause.

---

# 46. Immediate Correction

Examples:

- repeat measurement;
- relabel specimen;
- obtain missing documentation;
- retrain staff;
- restore approved instrument;
- correct timing;
- pause enrollment.

---

# 47. Irreversible Deviation

Some deviations cannot be corrected.

They must remain visible in analysis and interpretation.

---

# 48. Participant-Level Deviation

Examples:

- visit outside window;
- missed dose;
- consent timing issue;
- ineligible enrollment;
- missed assessment.

---

# 49. Site-Level Deviation

Examples:

- local protocol interpretation;
- training failure;
- storage condition failure;
- repeated timing drift.

---

# 50. Study-Level Deviation

Examples:

- protocol-wide instrument change;
- recruitment strategy change;
- outcome timing change;
- analysis population change.

---

# 51. Specimen-Level Deviation

Track:

- collection;
- labeling;
- transport;
- processing;
- storage;
- assay.

---

# 52. Laboratory Deviation

Examples:

- incorrect temperature;
- wrong reagent;
- missed control;
- instrument calibration lapse;
- assay run outside SOP.

---

# 53. Intervention Deviation

Track:

- dose;
- duration;
- timing;
- delivery;
- contamination;
- co-intervention;
- adherence.

---

# 54. Measurement Deviation

Track:

- instrument;
- operator;
- timing;
- scoring;
- calibration;
- administration mode.

---

# 55. Survey Deviation

Examples:

- duplicate responses;
- altered item wording;
- unintended survey branching;
- response-window extension.

---

# 56. Qualitative Protocol Adherence

Do not force emergent qualitative inquiry into rigid procedural conformity.

Monitor adherence to the intended methodological logic rather than mechanical sameness.

---

# 57. Qualitative Flexible Element

Examples:

- probing;
- interview sequence;
- emergent sampling;
- evolving coding focus.

These may be legitimate if the design allows them.

---

# 58. Mixed-Method Adherence

Monitor strand timing, integration points, priority, and sequence.

---

# 59. Secondary-Data Adherence

Track extraction rules, inclusion dates, coding, linkage, exclusions, and version.

---

# 60. Meta-Analysis Adherence

Track protocol eligibility, search updates, screening rules, effect selection, model changes, and sensitivity analyses.

---

# 61. Adaptive Design

Prespecified adaptive rules are not deviations when followed as planned.

---

# 62. Adaptive Rule Evidence

Document trigger and decision evidence.

---

# 63. Protocol Flexibility Zone

Where appropriate, define an allowed range:

```yaml
flexibility_zone:
  element:
  lower_bound:
  upper_bound:
  rationale:
  approved_source:
```

---

# 64. Visit Window

A visit outside the permitted window may be deviation.

Within-window variation is not.

---

# 65. Dose Window

Preserve planned tolerances.

---

# 66. Timing Window

Timing tolerance should be protocol-based, not invented during monitoring.

---

# 67. Instrument Substitution

If a new instrument is used, assess equivalence before declaring adherence.

---

# 68. Staff Substitution

Staff changes may be permissible if competency requirements are satisfied.

---

# 69. Site Adaptation

Local adaptation may require amendment if it changes scientific meaning.

---

# 70. Contextual Necessity

Context can justify adaptation, but not silent protocol rewriting.

---

# 71. COVID/Emergency-Type Disruption

Major external disruption should be documented as contextual execution evidence.

---

# 72. Supply Disruption

Substitutions require equivalence assessment.

---

# 73. Equipment Failure

Document whether affected observations remain usable.

---

# 74. Data Source Failure

If a planned source becomes unavailable, route to execution and methodology review before substitution.

---

# 75. Recruitment Deviation

Examples:

- altered inclusion interpretation;
- altered recruitment channel;
- enrollment beyond approved maximum;
- missing eligibility documentation.

---

# 76. Eligibility Deviation

Classify impact on analysis population and validity.

---

# 77. Consent Deviation

Route immediately when rights or permission may be affected.

---

# 78. Privacy Deviation

Route to governance and ethics.

---

# 79. Safety Deviation

Safety may require immediate escalation independent of scientific severity.

---

# 80. Randomization Deviation

Track allocation sequence breach, predictable allocation, or incorrect assignment.

---

# 81. Blinding Deviation

Track who became unblinded, when, why, and consequence.

---

# 82. Contamination

Track unintended treatment exposure across groups.

---

# 83. Follow-Up Deviation

Track missing visits, delayed visits, altered modality, shortened follow-up.

---

# 84. Outcome Assessment Deviation

Primary-outcome departures require explicit consequence assessment.

---

# 85. Assay Deviation

Assess whether rerun is permitted and scientifically justified.

---

# 86. Rerun Governance

Do not rerun merely because the result is undesirable.

---

# 87. Repeat Measurement

Record why repetition occurred.

---

# 88. Missing Protocol Step

Determine whether omission is recoverable.

---

# 89. Extra Protocol Step

Additional procedures may require permission or registration amendment.

---

# 90. Unplanned Analysis

Route to:

`registration-preregistration-builder`

and label exploratory or post-hoc appropriately.

---

# 91. Execution Manager Relationship

`research-execution-manager` coordinates the study.

This skill provides protocol-fidelity evidence back to it.

---

# 92. Data Collection Monitor Relationship

`data-collection-monitor` monitors ongoing collection performance.

Protocol deviations detected there should route here.

---

# 93. Deviation Risk Monitor Relationship

`deviation-risk-monitor` estimates future deviation risk.

This skill evaluates actual protocol departures.

---

# 94. Research Progress Auditor Relationship

Progress status should not be considered healthy if material protocol nonadherence is unresolved.

---

# 95. Deviation Risk vs Actual Deviation

```text
DEVIATION RISK
future possibility

PROTOCOL DEVIATION
observed departure
```

---

# 96. Protocol Adherence vs Data Quality

Protocol adherence asks whether procedures were followed.

Data quality asks whether resulting data are valid and fit for use.

Both may diverge.

---

# 97. Adherent but Poor Quality

Possible when the protocol itself is insufficient or the process fails despite adherence.

---

# 98. Nonadherent but Usable Data

Possible in limited cases.

Do not automatically discard data solely because a deviation occurred.

---

# 99. Data Exclusion Decision

Exclusion should be justified scientifically and analytically, not automatically by protocol labels.

---

# 100. Deviation Analysis Population

Preserve transparent inclusion/exclusion logic.

---

# 101. Per-Protocol Analysis

Do not confuse a per-protocol analysis with a universal definition of protocol compliance.

---

# 102. Intention-to-Treat

Protocol deviations do not automatically remove participants from ITT.

---

# 103. Qualitative Inclusion

A procedural departure may alter context without invalidating the material.

---

# 104. Deviation Consequence Matrix

| Severity | Recurrence | Typical Response |
|---|---|---|
| minor | isolated | document |
| minor | repeated | corrective/preventive review |
| moderate | isolated | assess and correct |
| moderate | repeated | amendment/escalation review |
| major | any | immediate escalation |
| critical | any | pause/stop and competent review |

---

# 105. Monitoring Frequency

Frequency should reflect:

- risk;
- complexity;
- participant vulnerability;
- novelty;
- multi-site variation;
- prior deviations;
- intervention risk;
- data sensitivity.

---

# 106. High-Risk Element

High-risk protocol elements may require more frequent monitoring.

---

# 107. Monitoring Trigger

Triggers include:

- first participant;
- first batch;
- first site;
- first data transfer;
- new staff;
- amendment;
- repeated deviation;
- safety signal;
- site activation.

---

# 108. Triggered Review

Use event-based monitoring when continuous review is unnecessary.

---

# 109. Central Monitoring

May detect cross-site patterns.

---

# 110. Site Monitoring

May detect local implementation problems.

---

# 111. Remote Monitoring

Can be appropriate if evidence quality is sufficient.

---

# 112. Source Data Verification

Use selectively and proportionately.

Do not confuse complete source verification with complete protocol adherence.

---

# 113. Monitoring Note

```yaml
monitoring_note:
  date:
  scope:
  protocol_version:
  evidence_reviewed:
  findings:
  deviations:
  unresolved_questions:
  actions:
  next_review:
```

---

# 114. Deviation Register

```yaml
deviation_register:
  deviation_id:
  date:
  site:
  protocol_version:
  requirement:
  observed_departure:
  classification:
  severity:
  recurrence:
  impact:
  immediate_action:
  capa:
  amendment_needed:
  reporting_needed:
  status:
```

---

# 115. Deviation Status

Use:

- `OPEN`
- `UNDER_REVIEW`
- `ACTION_REQUIRED`
- `CAPA_ACTIVE`
- `AMENDMENT_PENDING`
- `REPORTED`
- `RESOLVED`
- `CLOSED_WITH_RESIDUAL_IMPACT`

---

# 116. Closed With Residual Impact

A deviation may be operationally closed while still affecting interpretation.

---

# 117. Amendment Trigger

Consider amendment when:

- repeated departures indicate protocol infeasibility;
- procedure permanently changes;
- outcome timing changes;
- intervention changes;
- population changes;
- instrument changes materially;
- data source changes;
- analytic commitments change.

---

# 118. Amendment Route

Route to:

- `protocol-builder`
- `ethics-regulatory-gate`
- `registration-preregistration-builder`

as appropriate.

---

# 119. Amendment Before Implementation

Prefer formal amendment before planned change takes effect.

---

# 120. Emergency Exception

Urgent participant-protection action may precede amendment.

---

# 121. Deviations After Amendment

Assess using the version in force at the event date.

---

# 122. Historical Integrity

Never delete old deviation records after amendment.

---

# 123. Recurrence Detection

Aggregate deviations by:

- protocol element;
- site;
- staff role;
- participant type;
- time;
- equipment;
- intervention batch;
- data source.

---

# 124. Pattern Detection

A cluster may reveal systemic process failure.

---

# 125. Trend Interpretation

Do not infer root cause from counts alone.

---

# 126. Drift Score

If used, it should be transparent and not replace case-level review.

---

# 127. Staff Training Signal

Repeated deviations may indicate training need.

---

# 128. Protocol Ambiguity Signal

Divergent staff interpretations may indicate protocol wording failure.

---

# 129. Unrealistic Protocol Signal

Repeated justified departures may indicate an impractical design.

---

# 130. Governance Signal

Repeated permission-related issues may indicate governance misalignment.

---

# 131. Resource Signal

Recurring substitutions may indicate procurement or infrastructure weakness.

---

# 132. Data Signal

Repeated collection deviations may forecast data-quality problems.

---

# 133. Analysis Signal

Systematic deviation may require modified analysis or sensitivity analysis.

---

# 134. Reporting Signal

Material deviations should be transparently reported.

---

# 135. Manuscript Methods

Report what actually occurred.

---

# 136. Manuscript Limitations

Include material deviations that constrain interpretation.

---

# 137. Reviewer Response

Do not claim “protocol was followed” if monitoring shows material departures.

---

# 138. Reproducibility Record

Preserve:

- protocol version;
- event date;
- deviation;
- action;
- amendment;
- resulting data consequence.

---

# 139. Deviation and Missing Data

Some deviations produce missingness.

Do not assume missingness mechanism without analysis.

---

# 140. Deviation and Bias

Assess possible:

- selection bias;
- information bias;
- performance bias;
- detection bias;
- attrition bias;
- confounding changes.

---

# 141. Causal Study

Protocol fidelity may affect treatment contrast.

---

# 142. Prediction Study

Protocol inconsistency may affect predictor measurement or outcome definition.

---

# 143. Diagnostic Study

Protocol deviation may alter reference-standard integrity.

---

# 144. Validation Study

Protocol drift may make validation noncomparable.

---

# 145. Laboratory Study

Procedural drift may introduce batch effects.

---

# 146. Formulation Study

Processing deviations may change material properties.

---

# 147. Pharmacokinetic Study

Sampling-time deviations can materially affect PK estimates.

---

# 148. Pharmacogenetic Study

Genotyping QC deviations can affect genotype calls and downstream association.

---

# 149. Qualitative Study

Protocol fidelity should preserve epistemic and ethical commitments rather than enforce artificial rigidity.

---

# 150. Mixed Methods

Protocol deviation in one strand may change integration validity.

---

# 151. Systematic Review

Eligibility and synthesis deviations must preserve prospective transparency.

---

# 152. Meta-Analysis

Model changes should remain traceable.

---

# 153. Multi-Site Study

Compare adherence across sites without assuming identical context.

---

# 154. Site Effect

Site-specific deviations may create heterogeneity.

---

# 155. Site Suspension Trigger

Repeated major deviations may justify suspension pending review.

---

# 156. Participant Protection Trigger

Any credible rights or safety concern routes immediately to competent review.

---

# 157. Protocol Fidelity Dashboard

```yaml
protocol_fidelity_dashboard:
  current_version:
  adherence_status:
  open_deviations:
  major_deviations:
  repeated_deviations:
  drift_status:
  amendment_status:
  participant_protection_alerts:
  data_quality_alerts:
  next_monitoring_date:
```

---

# 158. Escalation Status

Use:

- `NO_ACTION`
- `DOCUMENT_ONLY`
- `CORRECTIVE_ACTION`
- `PREVENTIVE_ACTION`
- `CAPA_REQUIRED`
- `AMENDMENT_REQUIRED`
- `ETHICS_REVIEW_REQUIRED`
- `REGULATORY_REVIEW_REQUIRED`
- `PAUSE_REQUIRED`
- `STOP_REQUIRED`

---

# 159. Evidence Sufficiency

Use:

- `SUFFICIENT`
- `PARTIAL`
- `INSUFFICIENT`
- `CONFLICTING`

---

# 160. Conflicting Evidence

Preserve disagreement between records until resolved.

---

# 161. Monitor Independence

Where appropriate, monitoring should be sufficiently independent from the activity being evaluated.

---

# 162. Conflict of Interest

Document material monitoring conflicts.

---

# 163. No Punitive Classification

Deviation classification should protect research integrity, not punish staff.

---

# 164. Learning System

Deviation records can reveal design and process improvement opportunities.

---

# 165. No Normalization of Deviance

Repeated tolerated departures should not become de facto protocol without review.

---

# 166. No Compliance Theater

A complete checklist does not prove adherence if evidence contradicts it.

---

# 167. No Retroactive Cleaning of History

Do not rewrite logs after discovering nonadherence.

---

# 168. No Silent Reclassification

If a deviation is later reclassified, preserve prior status and rationale.

---

# 169. No Outcome-Driven Reclassification

Do not downgrade deviations because results appear favorable.

---

# 170. No Publication-Driven Reclassification

Do not hide departures to make the manuscript cleaner.

---

# 171. No Reviewer-Driven Rewriting

Reviewer requests may lead to clarification, not retroactive protocol compliance.

---

# 172. No Unverified “No Deviations”

Absence of recorded deviations is not proof that none occurred.

---

# 173. Negative Finding

A monitoring round may legitimately conclude:

`NO_MATERIAL_PROTOCOL_DEVIATION_IDENTIFIED`

This is not equivalent to proving perfect adherence.

---

# 174. User Request Routing

Activate when users ask:

- “Did we follow the protocol?”
- “Is this a protocol deviation?”
- “How serious is this deviation?”
- “Can this still be used?”
- “Do we need an amendment?”
- “Should this be reported?”
- “Why are sites doing the procedure differently?”
- “How do I monitor protocol fidelity?”
- “Is this drift?”
- “Can I continue despite this deviation?”
- “What should be documented?”
- “Does this affect the analysis?”

---

# 175. Output Package

Produce, as needed:

1. Protocol Version Check
2. Adherence Assessment
3. Deviation Classification
4. Severity Assessment
5. Recurrence Assessment
6. Scientific Consequence Assessment
7. Ethics / Regulatory Consequence Assessment
8. Data Consequence Assessment
9. CAPA Recommendation
10. Amendment Recommendation
11. Pause / Stop Recommendation
12. Deviation Register Entry
13. Protocol Fidelity Dashboard
14. Downstream Routing
15. Interpretation Handoff

---

# 176. Relationship with Research Execution Manager

`research-execution-manager` coordinates implementation.

`protocol-adherence-monitor` evaluates whether implementation remains consistent with the applicable protocol.

---

# 177. Relationship with Data Collection Monitor

`data-collection-monitor` evaluates active collection performance.

Protocol departures detected during collection route here.

---

# 178. Relationship with Deviation Risk Monitor

`deviation-risk-monitor` identifies prospective risk.

This skill evaluates observed adherence and actual deviations.

---

# 179. Relationship with Research Progress Auditor

Progress cannot be rated healthy solely from timeline completion when major adherence issues remain unresolved.

---

# 180. Relationship with Protocol Builder

`protocol-builder` defines or revises the controlled protocol.

This skill detects when revision may be required.

---

# 181. Relationship with Ethics Regulatory Gate

Permission-related departures route to:

`ethics-regulatory-gate`

---

# 182. Relationship with Registration Preregistration Builder

Changes to prospective commitments route to:

`registration-preregistration-builder`

---

# 183. Relationship with Research Data Governance

Data-handling departures route to:

`research-data-governance`

---

# 184. Relationship with Data Quality Auditor

Potential data-validity consequences route to:

`data-quality-auditor`

---

# 185. Relationship with Analysis Planner

Material deviations that affect estimands, populations, timing, or missingness route to:

`analysis-planner`

---

# 186. Relationship with Result Interpreter

`result-interpreter` should receive unresolved material deviations.

---

# 187. Relationship with Scientific Discussion

Protocol limitations may affect explanatory strength and generalizability.

---

# 188. Relationship with Manuscript Writer

Methods reporting must reflect actual implementation.

---

# 189. Relationship with Manuscript Auditor

`manuscript-auditor` should compare reported methods with protocol and deviation records.

---

# 190. Relationship with Reviewer Response

Reviewer concerns about protocol fidelity should be answered from verified records.

---

# 191. Relationship with Reproducibility Auditor

Deviation and version histories support reconstruction.

---

# 192. Relationship with Research Roadmap

Recurring protocol problems may reveal feasibility or capability needs for future studies.

---

# 193. Stop Conditions

Return or escalate when:

- protocol version cannot be determined;
- required evidence is unavailable;
- participant rights may be compromised;
- safety risk is unresolved;
- material regulatory uncertainty exists;
- deviation classification affects permission;
- a major amendment is needed;
- or implementation cannot proceed scientifically.

Possible statuses:

- `RETURN_TO_PROTOCOL_BUILDER`
- `RETURN_TO_ETHICS_REGULATORY_GATE`
- `RETURN_TO_REGISTRATION_PREREGISTRATION`
- `RETURN_TO_RESEARCH_EXECUTION_MANAGER`
- `PAUSE_EXECUTION`
- `STOP_EXECUTION`
- `PROTOCOL_ADHERENCE_REQUIRES_REVISION`

---

# 194. Final Adherence Rule

Never call a study adherent merely because no one documented a deviation.

Never call every operational difference a deviation.

Never call every deviation misconduct.

Never erase a deviation because an amendment was later approved.

Never downgrade a deviation because the data look favorable.

Never allow protocol monitoring to become a substitute for scientific judgment.

The correct objective is transparent correspondence between approved protocol and actual implementation.

---

# Success Criterion

`protocol-adherence-monitor` succeeds when current protocol versions, effective dates, operational requirements, expected implementation, observed implementation, evidence, allowed flexibility, protocol deviations, material violations, emergency departures, amendment status, recurrence, execution drift, scientific consequence, ethical or regulatory consequence, data-quality consequence, analytical consequence, corrective and preventive action, pause or stop requirements, and downstream routing are transparently distinguished and documented; when isolated deviations are separated from recurring systemic drift, operational variation from material nonadherence, approved amendments from retrospective rewriting, and emergency participant-protection actions from ordinary procedural breaches; when protocol fidelity is assessed using evidence rather than memory, checklists, publication pressure, reviewer expectations, or desired results; when unresolved permission issues route to `ethics-regulatory-gate`, prospective commitment changes to `registration-preregistration-builder`, data-handling issues to `research-data-governance`, data-validity issues to `data-quality-auditor`, active implementation coordination to `research-execution-manager`, prospective deviation risk to `deviation-risk-monitor`, collection problems to `data-collection-monitor`, milestone implications to `research-progress-auditor`, analytical implications to `analysis-planner`, and reconstruction needs to `reproducibility-auditor`; and when another competent researcher can determine which protocol governed each material event, what was expected, what actually occurred, what departures happened, how serious and recurrent they were, what corrective or preventive actions were taken, whether amendment or escalation was required, what residual impact remains, and how those facts should constrain later analysis, interpretation, reporting, and reproducibility claims.
