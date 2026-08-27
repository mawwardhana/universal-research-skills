---
name: research-progress-auditor
description: Audit whether an active research study or research stage is making scientifically meaningful progress against its approved objectives, milestones, dependencies, governance conditions, protocol requirements, data-collection expectations, risk profile, and evidence-of-completion criteria. Use after research-execution-manager has established implementation and while work is ongoing, delayed, paused, recovering, or approaching a decision gate. This skill distinguishes scientific progress from calendar activity, expenditure, meeting frequency, publication counting, and administrative completion; verifies milestone evidence; detects blocked dependencies, unresolved deviations, collection shortfalls, governance constraints, accumulating risk, capability gaps, and false “on track” reporting; and produces an evidence-based decision to proceed, proceed with conditions, replan, amend, pause, stop, or escalate without allowing deadlines, funding narratives, publication pressure, reviewer expectations, or desired results to redefine what meaningful research progress actually is.
---

# Research Progress Auditor

## Purpose

`research-progress-auditor` determines whether a study or research stage is making **scientifically meaningful, evidence-supported progress** toward its approved research objective.

Its central question is:

> Given the approved scientific plan, current execution evidence, milestone requirements, active risks, protocol status, data-collection status, governance conditions, and unresolved scientific dependencies, is the research genuinely progressing, merely active, delayed but recoverable, structurally blocked, or no longer defensible to continue as planned?

The core audit chain is:

```text
APPROVED RESEARCH OBJECTIVE
        ↓
SCIENTIFIC MILESTONES
        ↓
CURRENT EXECUTION EVIDENCE
        ↓
DEPENDENCY + GOVERNANCE + PROTOCOL + DATA STATUS
        ↓
RISK + DEVIATION + COLLECTION STATUS
        ↓
PROGRESS ASSESSMENT
        ↓
ON TRACK / CONDITIONAL / DELAYED / BLOCKED / AT RISK
        ↓
PROCEED / REPLAN / AMEND / PAUSE / STOP / ESCALATE
        ↓
TRACEABLE NEXT DECISION GATE
```

This skill does not measure progress by busyness.

It audits whether the evidence state has advanced.

---

# 1. Core Principles

Preserve these distinctions:

```text
ACTIVITY ≠ PROGRESS
PROGRESS ≠ CALENDAR ELAPSED
PROGRESS ≠ MONEY SPENT
PROGRESS ≠ MEETINGS HELD
PROGRESS ≠ PUBLICATIONS COUNTED
MILESTONE ≠ DEADLINE
DELAY ≠ FAILURE
PAUSE ≠ FAILURE
REPLAN ≠ SCIENTIFIC WEAKNESS
BLOCKED ≠ DELAYED
ON TRACK ≠ LOW RISK
COMPLETED ≠ VERIFIED
OUTPUT ≠ OUTCOME
ADMINISTRATIVE COMPLETION ≠ SCIENTIFIC COMPLETION
```

---

# 2. Activation Gate

Use this skill when:

- a study is actively being implemented;
- a progress report is due;
- the team asks whether the study is “on track”;
- a milestone has allegedly been completed;
- recruitment or collection is delayed;
- execution is paused;
- a major deviation has occurred;
- risks are accumulating;
- resources are constrained;
- funding continuation depends on progress evidence;
- a project must be replanned;
- a decision gate is approaching;
- a future phase depends on current-stage completion;
- or the researcher needs a defensible basis for continuation, pause, or termination.

---

# 3. Upstream Context

Use, when available:

- research question;
- objectives;
- hypotheses;
- methodology;
- protocol;
- research roadmap;
- execution plan;
- scientific milestones;
- decision gates;
- ethics and regulatory status;
- registration/preregistration;
- sampling plan;
- instrument plan;
- data-governance plan;
- data-collection dashboard;
- protocol adherence findings;
- deviation risk register;
- data-quality status;
- analysis plan;
- budget and resource constraints;
- and prior progress reports.

---

# 4. Progress Unit

A progress unit is a scientifically meaningful stage whose completion changes the evidence state.

Examples:

- protocol finalized;
- permission obtained;
- site activated;
- recruitment threshold reached;
- intervention delivered;
- primary outcome collected;
- assay validated;
- data source received;
- dataset locked;
- primary analysis completed;
- reproducibility audit passed.

---

# 5. Progress Unit Record

```yaml
progress_unit:
  unit_id:
  title:
  scientific_purpose:
  planned_milestone:
  evidence_required:
  evidence_available:
  verification_status:
  dependency_status:
  protocol_status:
  governance_status:
  risk_status:
  completion_status:
  consequence:
```

---

# 6. Progress Status

Use:

- `NOT_STARTED`
- `ON_TRACK`
- `ON_TRACK_WITH_CONDITIONS`
- `ON_TRACK_WITH_HIGH_RISK`
- `DELAYED_RECOVERABLE`
- `DELAYED_WITH_SCIENTIFIC_IMPACT`
- `AT_RISK`
- `BLOCKED`
- `PAUSED`
- `REQUIRES_REPLAN`
- `REQUIRES_AMENDMENT`
- `TERMINATED`
- `COMPLETED_UNVERIFIED`
- `COMPLETED_VERIFIED`
- `STATUS_UNCERTAIN`

---

# 7. Progress Is Evidence-State Change

Scientific progress means the study has moved from one defensible evidence state to another.

---

# 8. Activity Without Progress

Examples:

- repeated meetings without decision;
- repeated recruitment attempts without enrolled participants;
- repeated assays that fail QC;
- repeated data requests without access;
- manuscript drafting before results are valid.

---

# 9. Administrative Progress

Examples:

- purchasing completed;
- travel booked;
- invoices paid;
- contracts processed.

Important operationally, but not sufficient as scientific progress.

---

# 10. Scientific Milestone

A scientific milestone should have:

- purpose;
- evidence;
- verification;
- dependency;
- consequence.

---

# 11. Milestone Verification

Use:

```yaml
milestone_verification:
  milestone_id:
  required_evidence:
  observed_evidence:
  verified:
  verifier_role:
  date:
  unresolved_issue:
```

---

# 12. No Evidence, No Verified Completion

Do not mark a milestone complete merely because a status report says it is complete.

---

# 13. Completion Status

Use:

- `NOT_STARTED`
- `IN_PROGRESS`
- `COMPLETED_UNVERIFIED`
- `COMPLETED_VERIFIED`
- `PARTIALLY_COMPLETED`
- `FAILED`
- `SUPERSEDED`

---

# 14. Planned vs Actual

For each milestone compare:

```text
PLANNED
vs
ACTUAL
```

without treating difference as automatic failure.

---

# 15. Variance Types

Use:

- `NO_VARIANCE`
- `TIME_VARIANCE`
- `SCOPE_VARIANCE`
- `METHOD_VARIANCE`
- `RESOURCE_VARIANCE`
- `DATA_VARIANCE`
- `GOVERNANCE_VARIANCE`
- `QUALITY_VARIANCE`
- `UNKNOWN`

---

# 16. Delay Classification

Use:

- `MINOR_DELAY`
- `MODERATE_DELAY`
- `MAJOR_DELAY`
- `CRITICAL_DELAY`
- `UNKNOWN`

---

# 17. Delay Consequence

Ask whether delay affects:

- recruitment window;
- intervention timing;
- seasonality;
- participant availability;
- specimen integrity;
- funding;
- data access;
- analysis validity;
- reporting;
- or downstream stages.

---

# 18. Recoverable Delay

A delay is recoverable when the scientific objective remains defensible without hidden compromise.

---

# 19. Scientifically Material Delay

A delay becomes scientifically material when it changes design assumptions, timing, exposure, follow-up, sample representativeness, or outcome interpretation.

---

# 20. Blocked Status

A study is blocked when a hard dependency prevents defensible continuation.

---

# 21. Delay vs Blocked

```text
DELAYED
work can continue or recover

BLOCKED
a hard dependency prevents valid continuation
```

---

# 22. Pause Status

Pause may be appropriate when:

- safety review is needed;
- ethics approval lapses;
- protocol amendment is pending;
- major equipment failure occurs;
- data-integrity concern exists;
- collection validity is uncertain;
- or critical risk is unresolved.

---

# 23. Pause Is Not Failure

A scientifically justified pause protects integrity.

---

# 24. Replan Status

Replanning is required when original execution assumptions no longer hold.

---

# 25. Replan Record

```yaml
replan:
  trigger:
  evidence:
  affected_milestones:
  proposed_change:
  scientific_consequence:
  governance_consequence:
  registration_consequence:
  new_dependencies:
  approval_needed:
```

---

# 26. Amendment Requirement

If the scientific plan itself changes materially, route to appropriate amendment processes.

---

# 27. Amendment Route

Potentially route to:

- `protocol-builder`
- `ethics-regulatory-gate`
- `registration-preregistration-builder`
- `research-data-governance`
- `analysis-planner`

---

# 28. Progress Dependency

Each milestone may depend on:

- scientific evidence;
- protocol completion;
- permission;
- registration;
- recruitment;
- measurement;
- data access;
- data quality;
- analysis;
- resource;
- partnership;
- infrastructure.

---

# 29. Dependency Status

Use:

- `SATISFIED`
- `PARTIALLY_SATISFIED`
- `UNSATISFIED`
- `BLOCKED`
- `UNKNOWN`

---

# 30. Hard Dependency

An unsatisfied hard dependency prevents defensible progress.

---

# 31. Soft Dependency

A soft dependency may reduce efficiency or increase risk without making continuation invalid.

---

# 32. Governance Dependency

If permission or authorization is unresolved, progress cannot be rated fully on track.

---

# 33. Ethics Status

Integrate:

- approval;
- amendment;
- expiry;
- consent;
- privacy;
- participant protection.

---

# 34. Registration Status

Integrate prospective commitment status and amendment needs.

---

# 35. Protocol Status

Use evidence from:

`protocol-adherence-monitor`

---

# 36. Collection Status

Use evidence from:

`data-collection-monitor`

---

# 37. Deviation Risk Status

Use evidence from:

`deviation-risk-monitor`

---

# 38. Data Governance Status

Use evidence from:

`research-data-governance`

---

# 39. Data Quality Status

Use evidence from:

`data-quality-auditor`

---

# 40. Reproducibility Status

Use when relevant from:

`reproducibility-auditor`

---

# 41. Progress Evidence Hierarchy

Prefer:

1. verified source evidence;
2. audit trail;
3. controlled logs;
4. documented decision;
5. validated dashboard;
6. self-report.

---

# 42. Self-Report Guard

Self-reported “percent complete” should not substitute for milestone evidence.

---

# 43. Percent Complete Guard

Avoid arbitrary progress percentages when scientific work is nonlinear.

---

# 44. Binary Milestone Guard

Some milestones are not meaningfully binary.

Use partial status where scientifically appropriate.

---

# 45. Progress Trend

Use:

- `IMPROVING`
- `STABLE`
- `WORSENING`
- `VOLATILE`
- `UNKNOWN`

---

# 46. Progress Velocity

Use cautiously:

- `ACCELERATING`
- `STEADY`
- `SLOWING`
- `STALLED`
- `UNKNOWN`

---

# 47. Progress Forecast

Forecasts may estimate likely future milestone completion.

Label assumptions explicitly.

---

# 48. Forecast Is Not Commitment

Do not represent projection as guaranteed completion.

---

# 49. Progress Forecast Record

```yaml
progress_forecast:
  milestone:
  current_status:
  projected_completion:
  assumptions:
  uncertainty:
  main_risks:
  confidence:
```

---

# 50. Forecast Confidence

Use:

- `HIGH`
- `MODERATE`
- `LOW`
- `UNKNOWN`

---

# 51. Recruitment Progress

Track:

- screened;
- eligible;
- consented;
- enrolled;
- retained;
- completed.

---

# 52. Recruitment Progress Guard

High screening volume is not equivalent to enrollment progress.

---

# 53. Recruitment Feasibility

Repeated shortfall may require sampling or execution review.

---

# 54. Collection Progress

Track evidence actually collected, not forms opened.

---

# 55. Primary Outcome Progress

Primary outcome acquisition is often more scientifically important than total row count.

---

# 56. Follow-Up Progress

Track completed follow-up relative to eligible follow-up.

---

# 57. Attrition Impact

Rising attrition may downgrade progress status even when enrollment target is met.

---

# 58. Laboratory Progress

Track:

- valid runs;
- QC-passed batches;
- usable outputs;
- failed runs;
- reruns.

---

# 59. Laboratory Progress Guard

Raw number of runs does not equal valid scientific progress.

---

# 60. Assay Validation Progress

Validation must be evidence-based.

---

# 61. Specimen Progress

Track collected, processed, stored, assayed, failed, lost.

---

# 62. Survey Progress

Track invitations, eligible responses, complete responses, duplicates, missingness.

---

# 63. Qualitative Progress

Progress may include:

- recruitment;
- interviews;
- transcript readiness;
- analytic sufficiency;
- information power.

Do not force qualitative work into simplistic completion percentages.

---

# 64. Mixed-Method Progress

Each strand may have its own progress status.

Integration readiness must be assessed separately.

---

# 65. Secondary-Data Progress

Track request, receipt, validation, schema understanding, linkage, readiness.

---

# 66. Systematic Review Progress

Track search, screening, full text, extraction, appraisal, synthesis.

---

# 67. Meta-Analysis Progress

Track effect extraction, harmonization, model readiness, sensitivity planning.

---

# 68. Computational Progress

Track environment readiness, scripts, validated outputs, reproducibility.

---

# 69. Manuscript Progress Guard

Manuscript drafting is not a substitute for unresolved scientific work.

---

# 70. Publication Progress Guard

Accepted papers are outputs, not necessarily evidence that the current research stage is scientifically complete.

---

# 71. Research Roadmap Relationship

`research-roadmap` defines long-term cumulative progression.

`research-progress-auditor` audits the current study or stage against defensible milestones.

---

# 72. Stage Progress

A roadmap stage should not advance until required scientific gates are satisfied.

---

# 73. Stage Gate

Use:

```yaml
stage_gate:
  stage:
  required_evidence:
  current_evidence:
  unresolved_dependencies:
  decision:
  rationale:
```

---

# 74. Stage Decision

Use:

- `PROCEED`
- `PROCEED_WITH_CONDITIONS`
- `REVISE`
- `REPEAT`
- `REPLAN`
- `PAUSE`
- `STOP`
- `TERMINATE_STAGE`
- `AWAIT_EVIDENCE`

---

# 75. Proceed

Use only when scientific and governance prerequisites are sufficiently satisfied.

---

# 76. Proceed With Conditions

Use when continuation is defensible but unresolved issues require monitoring.

---

# 77. Revise

Use when current work can be corrected without changing the fundamental study.

---

# 78. Repeat

Use when a failed procedure can be scientifically repeated.

---

# 79. Replan

Use when sequencing, resources, scope, or dependencies require redesign.

---

# 80. Pause

Use when temporary suspension protects scientific integrity.

---

# 81. Stop

Use when continuation is no longer defensible.

---

# 82. Terminate Stage

A stage may terminate without terminating the entire research program.

---

# 83. Await Evidence

Do not force a decision before required evidence exists.

---

# 84. Progress Risk Integration

Progress should reflect active risk, not just completed tasks.

---

# 85. High-Risk On Track

A study can be on schedule but scientifically fragile.

Use:

`ON_TRACK_WITH_HIGH_RISK`

---

# 86. Low Activity but Healthy Progress

A study may have low visible activity while waiting for a scientifically required dependency.

---

# 87. Progress Dashboard

```yaml
progress_dashboard:
  overall_status:
  verified_milestones:
  unverified_milestones:
  delayed_milestones:
  blocked_milestones:
  active_high_risks:
  open_major_deviations:
  collection_status:
  governance_status:
  next_decision_gate:
  next_scientific_milestone:
```

---

# 88. Red-Amber-Green Guard

Color coding may summarize.

It must not hide the evidence basis.

---

# 89. “Green” Status Guard

A green dashboard cannot override unresolved critical scientific problems.

---

# 90. Progress Narrative

A defensible progress summary should explain:

- what advanced;
- what did not;
- why;
- what evidence proves it;
- what risks remain;
- what happens next.

---

# 91. Evidence-Based Progress Narrative

Avoid promotional language unsupported by evidence.

---

# 92. Funding Report

Funding reports should distinguish:

- scientific progress;
- expenditure;
- outputs;
- administrative milestones;
- unresolved barriers.

---

# 93. Funding Pressure Guard

Do not overstate progress to protect funding.

---

# 94. Sponsor Milestone

Sponsor milestones may be administrative, scientific, or both.

Classify explicitly.

---

# 95. Regulatory Milestone

A regulatory submission may be required but does not itself prove scientific progress.

---

# 96. Ethics Milestone

Approval allows work to proceed; it is not research evidence.

---

# 97. Registration Milestone

Registration documents intent; it does not prove implementation success.

---

# 98. Data Receipt Milestone

Receiving a dataset is not the same as validating it.

---

# 99. Data Lock Milestone

Data lock should depend on collection closure and reconciliation.

---

# 100. Analysis Milestone

Analysis is only scientifically meaningful if the input data and method are defensible.

---

# 101. Result Milestone

Statistical significance is not a milestone criterion unless scientifically prespecified and justified.

---

# 102. Negative Finding

A null or negative result can represent successful scientific progress.

---

# 103. Unexpected Finding

Unexpected evidence may require re-evaluation without invalidating progress.

---

# 104. Failed Hypothesis

A rejected hypothesis is not a failed project.

---

# 105. Failed Assay

A failed assay may be an execution failure that requires correction.

Distinguish scientific result from operational failure.

---

# 106. Feasibility Finding

Discovering infeasibility can be scientifically informative.

---

# 107. Stop Rule Success

Stopping according to a valid stop rule can be successful execution.

---

# 108. Progress and Quality

More data are not meaningful progress if quality deteriorates.

---

# 109. Progress and Protocol

More participants are not progress if protocol adherence fails materially.

---

# 110. Progress and Ethics

Fast recruitment is not progress if participant protections are compromised.

---

# 111. Progress and Reproducibility

Fast analysis is not progress if the record cannot be reconstructed.

---

# 112. Progress and Novelty

Progress does not mean increasingly novel claims.

---

# 113. Progress and Publication

Publication is downstream communication, not the definition of research progression.

---

# 114. Progress and Roadmap

A roadmap should advance because evidence justifies it.

---

# 115. Milestone Dependency Map

```text
MILESTONE A
    ↓
MILESTONE B
    ↓
MILESTONE C
```

Use branching when appropriate.

---

# 116. Parallel Milestones

Parallel work is legitimate when dependencies permit.

---

# 117. Integration Gate

Parallel workstreams may require an integration milestone.

---

# 118. Critical Path

Identify scientifically critical dependencies, not merely the shortest calendar path.

---

# 119. Critical Path Guard

Do not accelerate critical scientific steps merely because they delay the schedule.

---

# 120. Bottleneck

A bottleneck is the condition limiting progress.

---

# 121. Bottleneck Categories

Use:

- `SCIENTIFIC`
- `METHOD`
- `PROTOCOL`
- `ETHICS`
- `REGULATORY`
- `RECRUITMENT`
- `INSTRUMENT`
- `DATA_ACCESS`
- `DATA_QUALITY`
- `RESOURCE`
- `STAFF`
- `SUPPLY`
- `PARTNERSHIP`
- `INFRASTRUCTURE`
- `COMPUTATIONAL`
- `UNKNOWN`

---

# 122. Bottleneck Record

```yaml
bottleneck:
  type:
  evidence:
  affected_milestones:
  severity:
  recoverability:
  owner:
  action:
  escalation:
```

---

# 123. Recoverability

Use:

- `FULLY_RECOVERABLE`
- `PARTIALLY_RECOVERABLE`
- `UNLIKELY_RECOVERABLE`
- `IRRECOVERABLE`
- `UNKNOWN`

---

# 124. Capability Gap

Repeated bottlenecks may indicate capability deficiency.

---

# 125. Capability Gap Examples

- assay expertise;
- data management;
- recruitment infrastructure;
- statistical expertise;
- regulatory support;
- computing capacity;
- qualitative expertise;
- instrumentation.

---

# 126. Capability Development

Capability-building may become a legitimate milestone.

---

# 127. Capability Guard

Do not label ordinary inconvenience as a strategic capability gap.

---

# 128. External Dependency

Track external actors and their effect on milestones.

---

# 129. External Delay

Separate from internal scientific failure.

---

# 130. Partner Failure

May require route change.

---

# 131. Supplier Failure

Substitution may require equivalence assessment.

---

# 132. Site Failure

Site suspension may alter study feasibility.

---

# 133. Resource Utilization

Resource use may inform feasibility.

It does not define scientific progress.

---

# 134. Budget Burn Guard

High budget consumption with low evidence advancement is a warning.

---

# 135. Time Burn Guard

Elapsed time without evidence-state change is a warning.

---

# 136. Effort Burn Guard

High labor effort does not automatically equal progress.

---

# 137. Progress Variance Review

For each major variance ask:

```text
What changed?
Why?
Was it preventable?
What scientific consequence follows?
What action is required?
```

---

# 138. Progress Audit Record

```yaml
progress_audit:
  audit_date:
  study_stage:
  protocol_version:
  overall_status:
  verified_milestones:
  delayed_milestones:
  blocked_dependencies:
  major_deviations:
  critical_risks:
  collection_status:
  governance_status:
  decision:
  rationale:
  next_gate:
```

---

# 139. Audit Frequency

Frequency should reflect:

- study risk;
- complexity;
- funding cycle;
- milestone density;
- participant vulnerability;
- active deviations;
- data velocity.

---

# 140. Event-Triggered Audit

Trigger when:

- major deviation;
- serious collection shortfall;
- ethics issue;
- critical risk;
- major staff change;
- site closure;
- instrument failure;
- amendment;
- unexpected feasibility problem.

---

# 141. Routine Audit

May be monthly, quarterly, stage-based, or milestone-based depending on context.

---

# 142. No Arbitrary Cadence

Do not impose monthly audits simply because that is common.

---

# 143. Progress Evidence Confidence

Use:

- `HIGH`
- `MODERATE`
- `LOW`
- `UNKNOWN`

---

# 144. Uncertainty

Preserve uncertainty when milestone evidence is incomplete.

---

# 145. Conflicting Progress Evidence

Do not resolve conflicting records by convenience.

---

# 146. Site Progress

For multi-site studies assess:

- activation;
- recruitment;
- adherence;
- collection;
- risk;
- submission;
- closure.

---

# 147. Site Comparison Guard

Do not rank sites without accounting for context and denominator.

---

# 148. Central Progress

May aggregate across sites.

---

# 149. Local Progress

May differ meaningfully.

---

# 150. Multi-Site Stage Gate

Do not advance a study-wide stage if critical sites remain unresolved unless the design permits it.

---

# 151. Qualitative Progress

Progress may reflect increasing informational sufficiency rather than numerical target attainment.

---

# 152. Mixed-Method Progress

One strand may be complete while integration is not.

---

# 153. Longitudinal Progress

Follow-up maturity matters.

---

# 154. Intervention Progress

Delivery completion should be distinguished from outcome availability.

---

# 155. Laboratory Progress

Batch completion should be distinguished from valid analyzable output.

---

# 156. Secondary-Data Progress

Access and receipt should be distinguished from harmonization and usability.

---

# 157. AI-Assisted Progress Monitoring

AI may assist with:

- summarizing logs;
- identifying delayed milestones;
- comparing versions;
- detecting inconsistent status reports;
- mapping dependencies.

AI must not fabricate milestone completion or decision authority.

---

# 158. AI Verification

Material AI-generated progress claims require verification.

---

# 159. Automated Dashboard

Automation may surface:

- recruitment;
- collection;
- risk;
- deviation;
- missingness;
- milestone status.

---

# 160. Automation Guard

Dashboard automation does not replace scientific audit.

---

# 161. No Progress Inflation

Do not describe partial work as completed work.

---

# 162. No Output Inflation

Do not count drafts, posters, meetings, or presentations as equivalent to evidence advancement.

---

# 163. No Publication Inflation

Do not treat publication count as a proxy for research validity.

---

# 164. No Deadline-Driven Status

Do not call a milestone complete because a report is due.

---

# 165. No Funding-Driven Status

Do not exaggerate progress for financial continuation.

---

# 166. No Reviewer-Driven Status

Do not claim new work is complete until it actually is.

---

# 167. No Result-Driven Status

Do not call progress better because results are favorable.

---

# 168. No Significance-Driven Progress

A small p-value is not a progress metric.

---

# 169. No Software-Driven Progress

Software completion messages are not scientific milestones.

---

# 170. No Hidden Delay

Material delay should remain visible.

---

# 171. No Hidden Blocker

Hard dependencies should be explicit.

---

# 172. No Hidden Pause

A paused study should not be represented as actively progressing.

---

# 173. No Hidden Termination

A terminated branch should remain visible in the research record.

---

# 174. No Silent Replan

Replanning should be documented.

---

# 175. No Silent Scope Change

A change in scientific scope may require upstream review.

---

# 176. No Silent Milestone Redefinition

Do not redefine a milestone after failure simply to preserve a green status.

---

# 177. No Retroactive Success Criterion

Success criteria should not be rewritten because the original target was missed unless formally revised and history preserved.

---

# 178. Scientific Progress Narrative Template

```text
What was planned?
What evidence was achieved?
What remains unresolved?
What changed?
What risks remain?
What is the next defensible gate?
```

---

# 179. Progress Report Structure

A defensible report may include:

1. Objective
2. Current Stage
3. Verified Milestones
4. Unverified Milestones
5. Delays
6. Blockers
7. Deviations
8. Risks
9. Collection Status
10. Governance Status
11. Data Quality Status
12. Decision
13. Next Gate

---

# 180. Executive Summary Guard

Do not compress uncertainty out of the summary.

---

# 181. Relationship with Research Execution Manager

`research-execution-manager` coordinates implementation.

`research-progress-auditor` independently evaluates whether implementation has produced defensible scientific progress.

---

# 182. Relationship with Protocol Adherence Monitor

Material nonadherence may downgrade progress status.

---

# 183. Relationship with Data Collection Monitor

Collection completeness, timing, attrition, and source continuity inform progress.

---

# 184. Relationship with Deviation Risk Monitor

High or worsening risk can downgrade an otherwise on-schedule study.

---

# 185. Relationship with Ethics Regulatory Gate

Unresolved permission issues may block progress.

---

# 186. Relationship with Registration Preregistration Builder

Prospective-plan changes may require amendment before progress can continue defensibly.

---

# 187. Relationship with Research Data Governance

Data lifecycle failures may block progress toward analysis readiness.

---

# 188. Relationship with Data Quality Auditor

Poor data quality may invalidate apparent collection progress.

---

# 189. Relationship with Reproducibility Auditor

A study may be scientifically incomplete if critical reconstruction evidence is missing.

---

# 190. Relationship with Analysis Planner

Analysis readiness is a milestone only when data and design conditions support it.

---

# 191. Relationship with Result Interpreter

Progress into interpretation requires valid results.

---

# 192. Relationship with Scientific Discussion

Scientific discussion should not begin as a substitute for unresolved evidence generation.

---

# 193. Relationship with Manuscript Architect

Manuscript development should reflect actual research maturity.

---

# 194. Relationship with Manuscript Writer

Writing should not overstate study completion.

---

# 195. Relationship with Manuscript Auditor

Audit should compare manuscript claims with verified milestone status.

---

# 196. Relationship with Reviewer Response

Reviewer-requested actions become new auditable progress units.

---

# 197. Relationship with Research Roadmap

Current-stage progress determines whether long-term roadmap advancement is justified.

---

# 198. Relationship with Research Resume

When resuming prior work, reconstruct verified progress before assigning the next task.

---

# 199. Relationship with Prior Research Auditor

Historical milestone evidence may reveal unfinished scientific work.

---

# 200. Relationship with Research Trajectory Mapper

Verified progress contributes to cumulative capability and trajectory evidence.

---

# 201. User Request Routing

Activate when users ask:

- “Is the study on track?”
- “Have we made enough progress?”
- “Can we move to the next stage?”
- “Should we continue or pause?”
- “What is blocking the study?”
- “Is this delay still acceptable?”
- “Which milestones are really complete?”
- “What should go in the progress report?”
- “Can we start analysis now?”
- “Can we close data collection?”
- “Should we extend the project?”
- “Do we need to replan?”
- “Is this stage scientifically complete?”

---

# 202. Output Package

Produce, as needed:

1. Overall Progress Status
2. Verified Milestone Register
3. Unverified Milestone Register
4. Delay Assessment
5. Blocker Register
6. Dependency Status
7. Governance Status
8. Protocol Status
9. Collection Status
10. Risk Status
11. Data Quality Status
12. Progress Trend
13. Forecast
14. Replan Recommendation
15. Amendment Recommendation
16. Pause / Stop Recommendation
17. Stage-Gate Decision
18. Next Defensible Milestone

---

# 203. Stop Conditions

Return, pause, or escalate when:

- critical milestone evidence is missing;
- permission is unresolved;
- primary outcome collection is failing;
- protocol nonadherence is major;
- data quality prevents inference;
- risk is critical;
- a hard dependency is blocked;
- the research question can no longer be answered;
- or continuation would produce activity without meaningful scientific progress.

Possible statuses:

- `CONTINUE`
- `CONTINUE_WITH_CONDITIONS`
- `REPLAN`
- `AMEND`
- `PAUSE`
- `STOP`
- `TERMINATE_STAGE`
- `AWAIT_EVIDENCE`
- `RETURN_TO_UPSTREAM_SKILL`

---

# 204. Final Progress Rule

Never call activity progress merely because time, money, or effort has been spent.

Never call a milestone complete without evidence.

Never hide delay, blockers, deviations, or risk to produce a favorable progress report.

Never let publication count, funding pressure, reviewer requests, software output, or desired results redefine scientific progress.

Never advance a research stage merely because the calendar says the next stage should begin.

The correct objective is evidence-supported advancement of the scientific state.

---

# Success Criterion

`research-progress-auditor` succeeds when the current study or research stage has been evaluated against its approved scientific objective, verified milestones, evidence-of-completion requirements, dependencies, protocol status, ethics and regulatory conditions, registration commitments, data-governance status, data-collection status, deviation history, prospective risk profile, data-quality status, resource constraints, capability constraints, and downstream decision gates; when scientific progress is distinguished from administrative activity, elapsed time, money spent, meetings held, output counting, publication counting, and manuscript activity; when completed milestones are separated from verified milestones, recoverable delays from scientifically material delays, delays from hard blocks, pauses from failures, replan from concealment, and negative or null scientific findings from operational failure; when apparent progress is downgraded where protocol nonadherence, collection shortfall, governance uncertainty, critical risk, data-quality failure, or missing evidence makes continuation scientifically fragile; when unresolved execution issues route to `research-execution-manager`, actual protocol departures to `protocol-adherence-monitor`, collection problems to `data-collection-monitor`, future threats to `deviation-risk-monitor`, permission issues to `ethics-regulatory-gate`, prospective commitment changes to `registration-preregistration-builder`, provenance issues to `research-data-governance`, data-validity issues to `data-quality-auditor`, analytical readiness issues to `analysis-planner`, and reconstruction needs to `reproducibility-auditor`; when progress inflation, deadline-driven status, funding-driven optimism, publication-driven milestones, reviewer-driven completion claims, significance-driven progress claims, arbitrary percentages, and software-driven status are prevented; and when another competent researcher can determine what was planned, what scientifically meaningful evidence has actually advanced, which milestones are verified, what is delayed or blocked, which risks and deviations remain active, whether the stage should proceed, proceed with conditions, replan, amend, pause, stop, or await evidence, and what the next defensible scientific milestone should be.
