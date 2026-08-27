---
name: deviation-risk-monitor
description: Identify, assess, document, prioritize, and escalate prospective risks that may cause future divergence from an approved research protocol, execution plan, registration commitment, data-governance requirement, collection plan, or scientific milestone before the deviation actually occurs. Use during active research execution when there are warning signs such as recruitment delay, staff turnover, supply disruption, equipment instability, repeated near-misses, unresolved training gaps, data-access uncertainty, emerging site variation, instrument drift, participant burden, protocol infeasibility, missingness trends, external dependency failure, or approaching deadlines that may pressure the team into scientifically unjustified shortcuts. This skill estimates deviation likelihood and consequence without fabricating certainty, distinguishes risk from actual deviation, and routes observed deviations to protocol-adherence-monitor, active collection threats to data-collection-monitor, governance threats to ethics-regulatory-gate or research-data-governance, prospective commitment threats to registration-preregistration-builder, and milestone consequences to research-progress-auditor.
---

# Deviation Risk Monitor

## Purpose

`deviation-risk-monitor` identifies and manages **prospective deviation risk** before a protocol or execution failure actually occurs.

Its central question is:

> What conditions are making a future deviation more likely, how serious would the consequence be if that deviation occurred, what evidence supports the risk estimate, and what preventive action should happen before the study drifts from the approved scientific plan?

The core logic is:

```text
APPROVED PLAN
    ↓
ACTIVE EXECUTION
    ↓
EARLY WARNING SIGNALS
    ↓
DEVIATION RISK IDENTIFICATION
    ↓
LIKELIHOOD + CONSEQUENCE + DETECTABILITY
    ↓
PRIORITIZATION
    ↓
PREVENTIVE ACTION
    ↓
MONITOR / ESCALATE / REPLAN / PAUSE
    ↓
ACTUAL DEVIATION?
    ├── NO  → continue monitoring
    └── YES → protocol-adherence-monitor
```

This skill is not a prediction engine.

It is a scientific early-warning and prevention layer.

---

# 1. Core Principles

Preserve these distinctions:

```text
RISK ≠ DEVIATION
WARNING ≠ FAILURE
LIKELIHOOD ≠ CERTAINTY
FREQUENCY ≠ CONSEQUENCE
URGENT ≠ IMPORTANT
DEADLINE PRESSURE ≠ SCIENTIFIC JUSTIFICATION
PREVENTION ≠ RETROACTIVE CORRECTION
RISK SCORE ≠ SCIENTIFIC TRUTH
NO ALERT ≠ NO RISK
HIGH RISK ≠ AUTOMATIC STOP
LOW RISK ≠ SAFE FOREVER
```

---

# 2. Activation Gate

Use this skill when:

- execution is active;
- future protocol divergence is plausible;
- repeated near-misses occur;
- recruitment is falling behind;
- staff capacity is unstable;
- training gaps persist;
- supply or equipment failure is emerging;
- participant burden may increase dropout;
- missingness is rising;
- site variation is increasing;
- external data access is uncertain;
- regulatory or ethics deadlines approach;
- amendments are likely;
- publication or administrative pressure may create shortcuts;
- or a research manager wants an evidence-based early-warning view.

---

# 3. Upstream Context

Use, when available:

- approved protocol;
- protocol version;
- execution plan;
- sampling strategy;
- instrument plan;
- registration/preregistration;
- ethics and regulatory status;
- data-governance plan;
- collection plan;
- current collection dashboard;
- open protocol deviations;
- site performance;
- resource status;
- milestone plan;
- risk history;
- staff training records;
- external dependency records;
- and prior CAPA.

---

# 4. Risk Is Prospective

A risk describes a future possibility.

If the event has already occurred, route to:

`protocol-adherence-monitor`

or another appropriate skill.

---

# 5. Risk Unit

A risk unit should represent one specific prospective failure mode.

Examples:

- visit-window nonadherence;
- recruitment shortfall;
- specimen transport failure;
- consent expiry;
- instrument downtime;
- dataset access delay;
- staff turnover;
- uncontrolled protocol drift;
- repeated missing primary outcomes;
- unauthorized source substitution.

---

# 6. Risk Record

```yaml
deviation_risk:
  risk_id:
  title:
  affected_workstream:
  future_failure_mode:
  evidence:
  likelihood:
  consequence:
  detectability:
  time_horizon:
  risk_owner:
  preventive_action:
  contingency:
  monitoring_trigger:
  escalation_route:
  status:
```

---

# 7. Risk Categories

Use:

- `SCIENTIFIC_RISK`
- `PROTOCOL_RISK`
- `ETHICS_RISK`
- `REGULATORY_RISK`
- `SAFETY_RISK`
- `RECRUITMENT_RISK`
- `PARTICIPANT_RETENTION_RISK`
- `MEASUREMENT_RISK`
- `INSTRUMENT_RISK`
- `SPECIMEN_RISK`
- `DATA_ACCESS_RISK`
- `DATA_GOVERNANCE_RISK`
- `DATA_QUALITY_RISK`
- `MISSINGNESS_RISK`
- `SITE_RISK`
- `STAFF_RISK`
- `TRAINING_RISK`
- `SUPPLY_RISK`
- `INFRASTRUCTURE_RISK`
- `PARTNERSHIP_RISK`
- `COMPUTATIONAL_RISK`
- `TIMELINE_RISK`
- `ARCHIVAL_RISK`

---

# 8. Evidence for Risk

Use observed signals such as:

- trend;
- near-miss;
- repeated delay;
- unresolved dependency;
- known equipment instability;
- staff shortage;
- high dropout;
- expiring permission;
- repeated ambiguity;
- delayed data source;
- rising missingness;
- repeated substitutions.

---

# 9. No Risk Fabrication

Do not create a high-risk label from intuition alone when evidence is absent.

---

# 10. Evidence Sufficiency

Use:

- `STRONG`
- `MODERATE`
- `LIMITED`
- `WEAK`
- `UNKNOWN`

---

# 11. Likelihood

Use:

- `RARE`
- `UNLIKELY`
- `POSSIBLE`
- `LIKELY`
- `VERY_LIKELY`
- `UNKNOWN`

---

# 12. Consequence

Use:

- `NEGLIGIBLE`
- `MINOR`
- `MODERATE`
- `MAJOR`
- `CRITICAL`
- `UNKNOWN`

---

# 13. Detectability

Use:

- `HIGH`
- `MODERATE`
- `LOW`
- `UNKNOWN`

Low detectability may increase monitoring priority.

---

# 14. Time Horizon

Use:

- `IMMEDIATE`
- `NEAR_TERM`
- `MID_TERM`
- `LONG_TERM`
- `UNKNOWN`

---

# 15. Risk Priority

Do not reduce priority to a single numeric score unless the scoring logic is explicit.

---

# 16. Qualitative Priority

Use:

- `LOW`
- `MODERATE`
- `HIGH`
- `CRITICAL`
- `UNRESOLVED`

---

# 17. Risk Matrix

A simple qualitative matrix may be used:

| Likelihood | Minor | Moderate | Major | Critical |
|---|---:|---:|---:|---:|
| Rare | Low | Low | Moderate | High |
| Unlikely | Low | Moderate | Moderate | High |
| Possible | Moderate | Moderate | High | Critical |
| Likely | Moderate | High | High | Critical |
| Very likely | High | High | Critical | Critical |

This matrix is a prioritization aid, not scientific truth.

---

# 18. Risk Velocity

Ask how quickly the risk could become an actual deviation.

---

# 19. Velocity Status

Use:

- `SLOW`
- `MODERATE`
- `FAST`
- `IMMEDIATE`
- `UNKNOWN`

---

# 20. Risk Owner

Assign responsibility by role, not merely by name.

---

# 21. Ownership Is Not Blame

Risk ownership means responsibility for monitoring and action.

---

# 22. Preventive Action

Preventive action reduces likelihood or consequence before deviation occurs.

---

# 23. Corrective Action

Corrective action belongs to an observed problem.

Do not confuse it with prevention.

---

# 24. Preventive Action Record

```yaml
preventive_action:
  action_id:
  risk_id:
  action:
  responsible_role:
  start_date:
  due_date:
  evidence_required:
  status:
  effectiveness_review:
```

---

# 25. Contingency Plan

A contingency specifies what to do if prevention fails.

---

# 26. Contingency Record

```yaml
contingency:
  risk_id:
  trigger:
  fallback_action:
  scientific_constraints:
  governance_constraints:
  approval_needed:
  downstream_route:
```

---

# 27. Trigger Threshold

A trigger should be evidence-based.

Examples:

- recruitment below threshold;
- dropout above expected range;
- repeated equipment failure;
- repeated missed timepoints;
- unresolved consent renewal;
- source-data latency exceeding operational tolerance.

---

# 28. No Arbitrary Threshold

Do not invent thresholds merely because software expects one.

---

# 29. Near-Miss

A near-miss is a condition that almost produced a deviation but did not.

---

# 30. Near-Miss Record

```yaml
near_miss:
  event_id:
  date:
  affected_process:
  what_almost_happened:
  why_it_did_not_happen:
  evidence:
  residual_risk:
  preventive_action:
```

---

# 31. Repeated Near-Miss

Repeated near-misses indicate systemic vulnerability.

---

# 32. Risk Trend

Monitor whether risk is:

- increasing;
- stable;
- decreasing;
- volatile;
- unknown.

---

# 33. Risk Trend Status

Use:

- `IMPROVING`
- `STABLE`
- `WORSENING`
- `VOLATILE`
- `UNKNOWN`

---

# 34. Risk Escalation

Escalate when:

- likelihood rises;
- consequence rises;
- detectability falls;
- preventive action fails;
- risk becomes imminent;
- multiple related risks cluster.

---

# 35. Risk Clustering

Several moderate risks may combine into a major threat.

---

# 36. Dependency Risk

A risk may originate in an upstream dependency.

---

# 37. External Dependency Risk

Examples:

- ethics committee delay;
- hospital data release;
- sequencing vendor delay;
- supplier shortage;
- collaborator withdrawal;
- permit delay.

---

# 38. Internal Dependency Risk

Examples:

- staff capacity;
- instrument availability;
- protocol ambiguity;
- data-entry backlog;
- training gaps.

---

# 39. Scientific Dependency Risk

A future downstream stage may fail because an upstream scientific condition is unresolved.

---

# 40. Recruitment Risk

Monitor:

- screening rate;
- eligibility rate;
- consent rate;
- enrollment rate;
- site activation;
- retention.

---

# 41. Recruitment Forecast

Forecasting may be used, but label assumptions explicitly.

---

# 42. Recruitment Forecast Guard

Do not treat extrapolation as certainty.

---

# 43. Retention Risk

Signals:

- increasing missed visits;
- participant burden;
- transport problems;
- intervention intolerance;
- contact failure.

---

# 44. Missingness Risk

Rising missingness may precede analysis limitations.

---

# 45. Missingness Risk Route

Coordinate with:

`data-collection-monitor`

and later:

`data-quality-auditor`

---

# 46. Primary Outcome Risk

Loss of the primary outcome deserves higher scientific attention than loss of minor administrative variables.

---

# 47. Instrument Risk

Signals:

- calibration instability;
- downtime;
- firmware changes;
- incompatible replacement;
- maintenance backlog.

---

# 48. Measurement Drift Risk

Potential gradual change in measurement behavior should be monitored.

---

# 49. Specimen Risk

Signals:

- transport delays;
- freezer instability;
- labeling problems;
- low volume;
- repeated contamination.

---

# 50. Laboratory Risk

Signals:

- control failure;
- reagent shortage;
- batch instability;
- instrument failure;
- operator inconsistency.

---

# 51. Data Access Risk

Signals:

- expiring agreement;
- delayed approval;
- unstable API;
- changing source schema;
- restricted account access.

---

# 52. Data Governance Risk

Signals:

- unclear access;
- unclear provenance;
- uncontrolled copies;
- inconsistent identifiers;
- unauthorized sharing.

---

# 53. Ethics Risk

Signals:

- approval expiration;
- consent mismatch;
- new participant burden;
- changed data use;
- new site;
- new population.

---

# 54. Ethics Risk Route

Route to:

`ethics-regulatory-gate`

---

# 55. Registration Risk

Signals:

- outcome change likely;
- analytic plan likely to change;
- recruitment plan likely to change;
- intervention timing likely to change.

---

# 56. Registration Risk Route

Route to:

`registration-preregistration-builder`

before silent drift occurs.

---

# 57. Protocol Risk

Signals:

- ambiguous instructions;
- repeated staff questions;
- repeated workaround;
- impractical step;
- incompatible site workflow.

---

# 58. Protocol Risk Route

Potential future divergence stays here.

Actual departure routes to:

`protocol-adherence-monitor`

---

# 59. Site Risk

Compare site-specific warning signs.

---

# 60. Site Risk Is Contextual

Do not label a site high-risk solely because its population differs.

---

# 61. Staff Risk

Signals:

- turnover;
- absence;
- overload;
- incomplete training;
- role ambiguity.

---

# 62. Training Risk

Repeated procedural uncertainty may indicate inadequate training.

---

# 63. Handover Risk

Staff transition can threaten continuity.

---

# 64. Supply Risk

Signals:

- low stock;
- unstable supplier;
- import delay;
- lot change;
- substitution pressure.

---

# 65. Substitution Risk

A potential substitute may not be scientifically equivalent.

---

# 66. Infrastructure Risk

Examples:

- power instability;
- storage failure;
- network failure;
- lab closure;
- site access disruption.

---

# 67. Computational Risk

Examples:

- software incompatibility;
- environment loss;
- expired license;
- insufficient compute;
- version mismatch.

---

# 68. Timeline Risk

Timeline pressure can create scientific shortcuts.

---

# 69. Deadline Risk

Approaching reporting deadlines should not justify invalid execution.

---

# 70. Publication Pressure Risk

Do not let submission targets create premature collection closure.

---

# 71. Reviewer Pressure Risk

Reviewer requests may create new execution work, but should not retroactively rewrite original protocol adherence.

---

# 72. Budget Risk

Budget shortage may threaten execution.

---

# 73. Budget Guard

Financial constraint may require replan, not silent scientific compromise.

---

# 74. Multi-Site Risk

Watch for divergence in:

- protocol;
- instrument;
- staff;
- timing;
- data submission;
- quality;
- governance.

---

# 75. Harmonization Risk

If site procedures are drifting apart, risk increases.

---

# 76. Central Monitoring Signal

Cross-site patterns may be visible centrally before locally.

---

# 77. Qualitative Research Risk

Potential risks include:

- recruitment narrowing;
- premature saturation claims;
- recording failure;
- reflexive documentation gaps;
- consent mismatch.

---

# 78. Mixed-Method Risk

One strand may fail to reach integration readiness.

---

# 79. Secondary Data Risk

Potential:

- source update;
- schema change;
- access withdrawal;
- coding changes;
- incomplete extraction.

---

# 80. Survey Risk

Potential:

- low response;
- duplicate response;
- instrument change;
- mode shift;
- sampling-frame erosion.

---

# 81. Sensor Risk

Potential:

- battery failure;
- clock drift;
- data loss;
- firmware change;
- device reassignment.

---

# 82. Sequencing Risk

Potential:

- low DNA quality;
- library failure;
- batch imbalance;
- read quality problems;
- reference-version mismatch.

---

# 83. Pharmacokinetic Risk

Potential:

- missed sampling windows;
- incorrect dose timing;
- BLQ prevalence;
- specimen handling failure.

---

# 84. Pharmacogenetic Risk

Potential:

- DNA failure;
- genotyping call failure;
- sample mismatch;
- batch effects.

---

# 85. Formulation Risk

Potential:

- raw material variation;
- process instability;
- storage instability;
- microbial contamination.

---

# 86. Education Study Risk

Potential:

- contamination across classes;
- attendance decline;
- intervention drift;
- assessment timing failure.

---

# 87. Organizational Study Risk

Potential:

- organizational restructuring;
- access withdrawal;
- policy change;
- participant turnover.

---

# 88. Field Research Risk

Potential:

- access disruption;
- environmental hazard;
- political instability;
- transport failure;
- safety constraints.

---

# 89. Early Warning Signal

Use:

```yaml
warning_signal:
  signal_id:
  risk_id:
  date:
  observation:
  source:
  strength:
  trend:
  action:
```

---

# 90. Warning Signal Strength

Use:

- `WEAK`
- `MODERATE`
- `STRONG`
- `CRITICAL`

---

# 91. Signal Validation

Do not escalate solely from an unverified alert when verification is feasible.

---

# 92. Automated Alert

Automation may detect:

- rising missingness;
- repeated lateness;
- site variation;
- recruitment decline;
- equipment failures.

---

# 93. Automation Guard

Automated alerts do not authorize scientific action by themselves.

---

# 94. AI-Assisted Risk Monitoring

AI may assist with:

- trend summarization;
- anomaly flagging;
- dependency mapping;
- document comparison;
- pattern detection.

AI must not fabricate risk evidence or authority.

---

# 95. AI Risk Verification

Material AI-derived risk claims require human review.

---

# 96. Risk Register

```yaml
risk_register:
  risk_id:
  category:
  failure_mode:
  evidence:
  likelihood:
  consequence:
  detectability:
  velocity:
  priority:
  owner:
  preventive_action:
  contingency:
  status:
```

---

# 97. Risk Status

Use:

- `OPEN`
- `MONITORED`
- `MITIGATION_ACTIVE`
- `ESCALATED`
- `CONTROLLED`
- `MATERIALIZED`
- `CLOSED`
- `UNKNOWN`

---

# 98. Materialized Risk

Once risk becomes an actual event, preserve its history and route appropriately.

---

# 99. No Risk Deletion

Do not delete a risk merely because it did not materialize.

Historical risk records may explain preventive actions.

---

# 100. Risk Closure

Close when:

- threat no longer exists;
- study stage passes;
- mitigation is verified;
- dependency resolves;
- or risk materializes and transfers to event management.

---

# 101. Residual Risk

After mitigation, reassess remaining risk.

---

# 102. Residual Risk Status

Use:

- `ACCEPTABLE`
- `ACCEPTABLE_WITH_MONITORING`
- `UNACCEPTABLE`
- `UNKNOWN`

---

# 103. Risk Acceptance

Risk acceptance should be explicit and within role authority.

---

# 104. Risk Transfer

Some risks may transfer to:

- vendor;
- site;
- data provider;
- regulator;
- collaborator.

Scientific responsibility does not disappear merely because an external actor owns the task.

---

# 105. Risk Avoidance

Sometimes the defensible action is to remove the risky activity.

---

# 106. Risk Reduction

Reduce likelihood or consequence.

---

# 107. Risk Contingency

Prepare response if the risk materializes.

---

# 108. Risk Monitoring Interval

Choose based on:

- velocity;
- priority;
- volatility;
- detectability;
- participant risk;
- scientific consequence.

---

# 109. Critical Risk

Critical risk may require immediate review.

---

# 110. Pause Recommendation

Recommend pause when continued execution could turn a foreseeable risk into serious scientific or governance failure.

---

# 111. Stop Recommendation

Stop recommendation is appropriate when risk cannot be reduced to defensible levels.

---

# 112. No Alarmism

High-risk labeling should be proportionate to evidence.

---

# 113. No False Reassurance

Low historical frequency does not guarantee safety.

---

# 114. No Deadline Compression

Do not accelerate scientifically critical steps solely to recover schedule.

---

# 115. No Silent Workaround

A workaround that changes scientific meaning may require amendment.

---

# 116. No Preventive Overreach

Do not add unnecessary procedures that create new burden without evidence of benefit.

---

# 117. No Outcome-Driven Mitigation

Do not change procedures because preliminary results are undesirable.

---

# 118. No Publication-Driven Mitigation

Do not redefine risk solely to preserve a submission date.

---

# 119. No Risk Score Theater

A numerical score without transparent evidence is not a scientific assessment.

---

# 120. No Normalization of Warning Signs

Repeated near-misses should not become “normal operations.”

---

# 121. No Silent Risk Reclassification

Preserve status history.

---

# 122. No Fabricated Mitigation

Do not claim preventive action completed without evidence.

---

# 123. Risk Escalation Matrix

| Risk Type | Default Route |
|---|---|
| actual protocol departure | `protocol-adherence-monitor` |
| active collection threat | `data-collection-monitor` |
| ethics or regulatory threat | `ethics-regulatory-gate` |
| registration commitment threat | `registration-preregistration-builder` |
| provenance or access threat | `research-data-governance` |
| data-validity threat | `data-quality-auditor` |
| execution coordination threat | `research-execution-manager` |
| milestone or timeline consequence | `research-progress-auditor` |
| analysis consequence | `analysis-planner` |
| reconstruction consequence | `reproducibility-auditor` |

---

# 124. Relationship with Research Execution Manager

`research-execution-manager` coordinates active implementation.

`deviation-risk-monitor` provides prospective warning and prevention.

---

# 125. Relationship with Protocol Adherence Monitor

`protocol-adherence-monitor` evaluates actual departures.

This skill evaluates the risk that departures may occur.

---

# 126. Relationship with Data Collection Monitor

`data-collection-monitor` observes the active evidence stream.

Its warning signs may generate future-deviation risks here.

---

# 127. Relationship with Research Progress Auditor

Risk can affect whether progress remains scientifically on track.

---

# 128. Relationship with Ethics Regulatory Gate

Potential permission failures route to:

`ethics-regulatory-gate`

---

# 129. Relationship with Registration Preregistration Builder

Potential prospective-plan changes route to:

`registration-preregistration-builder`

---

# 130. Relationship with Research Data Governance

Potential provenance, access, sharing, or linkage failures route to:

`research-data-governance`

---

# 131. Relationship with Data Quality Auditor

Potential validity consequences should be communicated to:

`data-quality-auditor`

---

# 132. Relationship with Sampling Strategy

Recruitment risk may require sampling review.

---

# 133. Relationship with Instrument Design

Measurement-system risk may require redesign.

---

# 134. Relationship with Protocol Builder

Protocol infeasibility may require formal revision.

---

# 135. Relationship with Analysis Planner

Foreseeable missingness or design disruption may affect feasible analysis.

---

# 136. Relationship with Reproducibility Auditor

Risk and mitigation history should remain reconstructable.

---

# 137. Relationship with Manuscript Auditor

Materialized risks and resulting deviations may become reporting issues.

---

# 138. Relationship with Reviewer Response

Reviewer-requested new work may create additional execution risk and should be assessed prospectively.

---

# 139. Relationship with Research Roadmap

Repeated execution risks may reveal long-term capability gaps.

---

# 140. Risk Dashboard

```yaml
risk_dashboard:
  overall_risk:
  critical_risks:
  high_risks:
  worsening_risks:
  imminent_risks:
  mitigation_active:
  unresolved_dependencies:
  next_review:
  escalation_needed:
```

---

# 141. Portfolio View

A study may have many risks.

Prioritize those that threaten:

- participant protection;
- primary outcome validity;
- protocol integrity;
- data provenance;
- study feasibility;
- reproducibility.

---

# 142. Risk Dependency Map

Use:

```text
RISK A
  ↓
RISK B
  ↓
RISK C
```

when one threat can trigger another.

---

# 143. Compound Risk

Multiple small risks may combine into a major failure.

---

# 144. Risk Interaction

Examples:

- staff shortage + equipment failure;
- recruitment delay + funding deadline;
- missingness + site drift;
- source delay + analysis deadline.

---

# 145. Scenario Analysis

Use scenarios to explore plausible consequences.

Do not represent scenarios as predictions.

---

# 146. Scenario Status

Use:

- `PLAUSIBLE`
- `LESS_PLAUSIBLE`
- `UNLIKELY`
- `UNKNOWN`

---

# 147. Best-Case Scenario

May help test resilience.

---

# 148. Worst-Case Scenario

Use proportionately, not theatrically.

---

# 149. Most Plausible Scenario

Should be evidence-based.

---

# 150. Contingency Readiness

Ask whether fallback routes are scientifically valid and authorized.

---

# 151. Contingency Equivalence

A fallback may require equivalence validation.

---

# 152. Substitution Guard

Do not assume replacement reagent, instrument, site, staff, or data source is equivalent.

---

# 153. Replanning Trigger

Replan when mitigation changes:

- sequence;
- resource;
- site;
- collection timing;
- protocol feasibility;
- or milestone dependency.

---

# 154. Replanning Route

Return to:

`research-execution-manager`

---

# 155. Amendment Trigger

If the intended scientific plan itself must change, route to:

- `protocol-builder`
- `ethics-regulatory-gate`
- `registration-preregistration-builder`

as appropriate.

---

# 156. Risk-to-Deviation Transition

```text
RISK IDENTIFIED
↓
WARNING SIGNAL
↓
MITIGATION
↓
DID DEVIATION OCCUR?
├── NO → monitor residual risk
└── YES → protocol-adherence-monitor
```

---

# 157. Transition Record

```yaml
risk_transition:
  risk_id:
  materialized:
  event_id:
  date:
  actual_deviation:
  route:
  residual_risk:
```

---

# 158. Risk Review Meeting

A meeting may review risks.

The meeting itself is not evidence that risks were resolved.

---

# 159. Risk Decision Record

```yaml
risk_decision:
  risk_id:
  evidence_reviewed:
  decision:
  rationale:
  responsible_role:
  date:
  followup:
```

---

# 160. Risk Communication

Communicate proportionately to those with relevant responsibility.

---

# 161. Confidential Risk Information

Sensitive risks may require restricted handling.

---

# 162. Participant Risk Priority

Participant protection overrides ordinary schedule recovery.

---

# 163. Data Risk Priority

Data integrity risks may require pause even when collection appears productive.

---

# 164. Scientific Validity Priority

A study that completes on time but cannot answer its research question is not scientifically successful.

---

# 165. Administrative vs Scientific Risk

Administrative risk may affect schedule or budget.

Scientific risk affects validity, interpretation, or research integrity.

---

# 166. Risk Tolerance

Do not assume universal tolerance.

It depends on consequence, context, authority, and scientific purpose.

---

# 167. Zero-Risk Fallacy

No research execution is completely risk-free.

---

# 168. Residual Uncertainty

Preserve uncertainty when evidence is incomplete.

---

# 169. Negative Risk Finding

A monitoring round may conclude:

`NO_MATERIAL_DEVIATION_RISK_IDENTIFIED`

This does not prove future absence of risk.

---

# 170. User Request Routing

Activate when users ask:

- “What could go wrong next?”
- “Is this becoming a protocol problem?”
- “Should we intervene before it becomes a deviation?”
- “Which risks are most important?”
- “Can we still finish on time without compromising the study?”
- “Should we pause?”
- “Do we need a contingency?”
- “What if recruitment keeps falling?”
- “What if the instrument fails?”
- “What if the data provider is late?”
- “How do we prevent protocol drift?”
- “Which warning signs should we monitor?”

---

# 171. Output Package

Produce, as needed:

1. Risk Register
2. Early Warning Register
3. Near-Miss Register
4. Likelihood Assessment
5. Consequence Assessment
6. Detectability Assessment
7. Risk Priority
8. Risk Trend
9. Preventive Action Plan
10. Contingency Plan
11. Risk Dashboard
12. Escalation Recommendation
13. Replanning Recommendation
14. Amendment Recommendation
15. Pause / Stop Recommendation
16. Residual Risk Assessment
17. Risk-to-Deviation Transition Record

---

# 172. Stop Conditions

Escalate when:

- participant safety risk is critical;
- permission expiry is imminent;
- primary outcome validity is at serious risk;
- data provenance is likely to fail;
- repeated near-misses indicate systemic breakdown;
- mitigation is ineffective;
- protocol infeasibility is structural;
- or continuation would likely create an irreparable scientific failure.

Possible statuses:

- `CONTINUE_MONITORING`
- `MITIGATION_REQUIRED`
- `ESCALATION_REQUIRED`
- `REPLAN_REQUIRED`
- `AMENDMENT_REQUIRED`
- `PAUSE_RECOMMENDED`
- `PAUSE_REQUIRED`
- `STOP_RECOMMENDED`
- `COMPETENT_REVIEW_REQUIRED`

---

# 173. Final Risk Rule

Never treat risk as certainty.

Never ignore repeated warning signs because no formal deviation has yet occurred.

Never use deadline pressure as a reason to accept scientifically unacceptable risk.

Never use a numeric risk score as a substitute for evidence.

Never hide risk to protect a progress report, manuscript timeline, funding narrative, or reviewer response.

The objective is to prevent foreseeable scientific divergence before it becomes an actual deviation.

---

# Success Criterion

`deviation-risk-monitor` succeeds when prospective threats to protocol adherence, execution fidelity, participant protection, registration commitments, data governance, data collection, measurement integrity, sample retention, site consistency, staff capacity, infrastructure, supply continuity, external dependencies, data access, data quality, computational continuity, milestone completion, and reproducibility are identified before they materialize; when risk is distinguished from actual deviation, likelihood from certainty, frequency from consequence, warning signal from failure, and prevention from correction; when each material risk has transparent evidence, category, likelihood, consequence, detectability, time horizon, trend, responsible role, preventive action, contingency, escalation route, and residual status; when repeated near-misses and worsening signals are not normalized; when actual departures route to `protocol-adherence-monitor`, collection threats to `data-collection-monitor`, execution coordination problems to `research-execution-manager`, ethics or regulatory threats to `ethics-regulatory-gate`, prospective commitment threats to `registration-preregistration-builder`, provenance or access threats to `research-data-governance`, data-validity threats to `data-quality-auditor`, milestone consequences to `research-progress-auditor`, analytical consequences to `analysis-planner`, and reconstruction consequences to `reproducibility-auditor`; when alarmism, false reassurance, arbitrary thresholds, deadline-driven shortcuts, publication-driven risk downgrading, reviewer-driven scientific compromise, silent workarounds, fabricated mitigation, and software-driven risk scoring are prevented; and when another competent researcher can determine what future failures were foreseeable, what evidence supported each concern, what prevention was attempted, which risks worsened or resolved, whether a risk materialized into an actual deviation, and whether the study could defensibly continue, replan, amend, pause, or stop.
