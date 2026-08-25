---
name: implication-builder
description: Translate defensibly interpreted and scientifically discussed research findings into bounded, evidence-proportionate theoretical, scientific, practical, clinical, educational, organizational, engineering, policy, implementation, methodological, measurement, and future-research implications. Use when result interpretation and scientific discussion are sufficiently established and the researcher needs to determine what the study legitimately changes, informs, recommends, or leaves unresolved without converting statistical significance into recommendation, overstating causality, ignoring uncertainty, feasibility, harms, or boundary conditions, or generating generic implications disconnected from the evidence.
---

# Implication Builder

## Purpose

`implication-builder` converts scientifically discussed findings into defensible implications.

Its central question is:

> Given what the study actually supports, what should change in theory, scientific understanding, research design, practice, policy, implementation, or future research — and what should not yet change?

This skill operates after:

- `result-interpreter`;
- `scientific-discussion`.

It does not replace scientific interpretation or scientific discussion.

---

# Core Principle

Use:

> Implication strength must never exceed evidence strength.

Preferred reasoning:

```text
Supported Finding
      ↓
Scientific Contribution
      ↓
Evidence Strength
      ↓
Uncertainty
      ↓
Boundary Conditions
      ↓
Feasibility / Risk / Context
      ↓
Implication Type
      ↓
Calibrated Recommendation
```

Do not reverse this sequence.

---

# Position in the Framework

Preferred architecture:

```text
result-interpreter
      ↓
scientific-discussion
      ↓
implication-builder
      ↓
manuscript-architect
```

When the implication reveals a coherent next research trajectory:

```text
implication-builder
      ↓
research-roadmap
```

---

# Required Upstream Context

Use established information from:

- `scientific-discussion`;
- `result-interpreter`;
- `novelty-auditor`;
- `gap-validator`;
- `theoretical-framework`;
- `conceptual-framework`;
- `methodology-architect`;
- `analysis-planner`;
- `phenomenon-evidence-builder` when implementation or policy context matters.

Useful context includes:

- main findings;
- effect magnitude or qualitative pattern;
- uncertainty;
- robustness;
- hypothesis status;
- theory relationship;
- mechanism status;
- scientific contribution;
- what is novel;
- what is not novel;
- limitations;
- generalizability;
- transferability;
- boundary conditions;
- contradictory evidence;
- unresolved questions;
- harms or trade-offs;
- feasibility constraints;
- population;
- setting.

Do not ask the researcher to repeat information already established.

---

# Readiness Gate

Classify:

- `READY_FOR_IMPLICATION_BUILDING`
- `SCIENTIFIC_DISCUSSION_INCOMPLETE`
- `RESULT_INTERPRETATION_INCOMPLETE`
- `CONTRIBUTION_UNCLEAR`
- `BOUNDARY_CONDITIONS_UNCLEAR`
- `EVIDENCE_STRENGTH_UNCLEAR`
- `FEASIBILITY_CONTEXT_MISSING`
- `IMPLICATIONS_ALREADY_ESTABLISHED`
- `IMPLICATIONS_REQUIRE_REASSESSMENT`

Do not generate strong recommendations from unstable evidence.

---

# Implication Is Not Recommendation

An implication may be:

- conceptual;
- theoretical;
- scientific;
- mechanistic;
- methodological;
- measurement;
- practical;
- clinical;
- educational;
- organizational;
- engineering;
- policy;
- implementation;
- equity;
- safety;
- economic;
- future research.

Not every implication requires an action recommendation.

---

# Implication Taxonomy

Classify:

- `THEORETICAL`
- `SCIENTIFIC`
- `MECHANISTIC`
- `METHODOLOGICAL`
- `MEASUREMENT`
- `PRACTICAL`
- `CLINICAL`
- `EDUCATIONAL`
- `ORGANIZATIONAL`
- `ENGINEERING`
- `POLICY`
- `IMPLEMENTATION`
- `EQUITY`
- `SAFETY`
- `ECONOMIC`
- `FUTURE_RESEARCH`

Multiple types may apply.

---

# Evidence-to-Implication Rule

Use:

```text
HIGH-CONFIDENCE FINDING
      ↓
stronger bounded implication

MODERATE-CONFIDENCE FINDING
      ↓
provisional implication

LOW-CONFIDENCE / EXPLORATORY FINDING
      ↓
hypothesis-generating implication
```

---

# Implication Strength

Classify:

- `STRONG`
- `MODERATE`
- `TENTATIVE`
- `EXPLORATORY`
- `NOT_SUPPORTED`

---

# Recommendation Strength

Classify separately:

- `ACTIONABLE_NOW`
- `CONSIDER_WITH_CONDITIONS`
- `PILOT_BEFORE_ADOPTION`
- `FURTHER_VALIDATION_REQUIRED`
- `RESEARCH_ONLY`
- `NOT_RECOMMENDED`

---

# Claim-to-Action Distance

The farther an implication moves from the observed result, the more evidence is required.

```text
Observed Result
      ↓
Scientific Meaning
      ↓
Generalized Meaning
      ↓
Practical Consequence
      ↓
Recommendation
      ↓
Policy / System Change
```

Each step requires additional justification.

---

# Action Escalation Guard

Do not escalate:

```text
association
→ intervention recommendation
→ policy mandate
```

without supporting causal and implementation evidence.

---

# Statistical Significance Guard

Do not write:

> Because p < 0.05, the intervention should be implemented.

Statistical significance is not an implementation criterion.

---

# Non-Significance Guard

Do not write:

> The intervention should be abandoned because p > 0.05.

Consider magnitude, uncertainty, design, and feasibility.

---

# Effect Magnitude Requirement

Practical implications should consider effect magnitude.

A statistically detectable but trivial effect may have little practical meaning.

---

# Uncertainty Requirement

Implications must reflect uncertainty.

Wide intervals imply weaker confidence in downstream action.

---

# Robustness Requirement

Recommendations should be stronger when findings remain stable across reasonable sensitivity analyses.

---

# Boundary Condition Requirement

Implications should specify where they apply.

Possible boundaries:

- population;
- setting;
- age;
- disease severity;
- institutional context;
- implementation fidelity;
- dose range;
- resource conditions;
- time horizon.

---

# Generalizability Guard

Do not make universal recommendations from one narrow setting without evidence.

---

# Transferability

For qualitative research, implications may be transferable where contextual conditions are sufficiently similar.

---

# Transportability

For causal or predictive studies, transportability requires population and setting compatibility.

---

# Theoretical Implications

Theoretical implications explain how findings affect theory.

Possible outcomes:

- support;
- refinement;
- extension;
- boundary;
- contradiction;
- integration;
- replacement need.

---

# Theory Support

Prefer:

> The findings strengthen support for the proposed relationship under the present conditions.

Avoid:

> The theory is proven.

---

# Theory Refinement

A study may imply refinement when it identifies:

- moderator;
- mediator;
- nonlinear relationship;
- temporal sequence;
- context boundary;
- missing construct;
- different mechanism.

---

# Theory Extension

Extension may occur when a theory is supported in:

- a scientifically meaningful new population;
- a new level of analysis;
- a new domain;
- a new temporal setting.

Context alone is not enough unless it changes explanatory scope.

---

# Theory Boundary

If a relationship holds only under certain conditions, define the boundary explicitly.

---

# Theory Contradiction

Contradiction may imply:

- theory revision;
- scope restriction;
- alternative mechanism;
- measurement reconsideration.

---

# Theoretical Implication Template

> The findings suggest that [theory/model] may require refinement to account for [new relationship, moderator, mechanism, boundary], particularly under [conditions].

---

# Scientific Implications

Scientific implications describe what changes in current knowledge.

Examples:

- uncertainty reduced;
- mechanism clarified;
- contradiction identified;
- boundary discovered;
- evidence strengthened;
- previously assumed relation weakened.

---

# Mechanistic Implications

Mechanistic implications require care.

Classify mechanism evidence as:

- `DIRECTLY_TESTED`
- `INDIRECTLY_SUPPORTED`
- `PLAUSIBLE`
- `SPECULATIVE`
- `UNSUPPORTED`

Do not recommend mechanism-targeted intervention when the mechanism is speculative.

---

# Methodological Implications

Methodological implications may include:

- stronger design;
- improved sampling;
- better measurement;
- alternative analysis;
- longitudinal follow-up;
- external validation;
- replication strategy.

---

# Methodology Recommendation Guard

Do not recommend a new method merely because it is more sophisticated.

Methodological implication should address a demonstrated weakness or uncertainty.

---

# Measurement Implications

Measurement findings may imply:

- instrument revision;
- item retention or removal;
- new validity testing;
- cultural adaptation;
- calibration;
- measurement invariance testing.

---

# Reliability Guard

High reliability alone does not justify adopting an instrument.

---

# Practical Implications

Practical implications ask:

> What can practitioners reasonably do differently?

Consider:

- effect magnitude;
- feasibility;
- burden;
- cost;
- acceptability;
- risk;
- context;
- implementation readiness.

---

# Practical Recommendation Template

> In settings comparable to the present study, practitioners may consider [action] when [conditions], although broader adoption should await [validation/implementation evidence].

---

# Clinical Implications

Clinical implications require attention to:

- patient benefit;
- harm;
- absolute risk;
- treatment burden;
- clinical thresholds;
- external validity;
- guideline context;
- implementation evidence.

---

# Clinical Recommendation Guard

Do not convert observational association into treatment recommendation.

---

# Clinical Utility

Predictive or diagnostic performance does not automatically imply clinical utility.

Clinical utility may require:

- decision-curve analysis;
- impact study;
- prospective validation;
- workflow integration.

---

# Pharmacogenetic Implications

Potential implications include:

- candidate genotype for validation;
- possible risk stratification;
- dose-response hypothesis;
- future clinical algorithm development.

Do not recommend routine genetic testing from one association study unless clinical validity and utility are established.

---

# Pharmacokinetic Implications

Potential implications may include:

- dose optimization hypothesis;
- population-specific monitoring;
- formulation modification;
- follow-up PK/PD study.

Do not infer dosing guideline changes without adequate evidence.

---

# Formulation Implications

Formulation findings may inform:

- optimization;
- stability testing;
- concentration selection;
- release profile;
- next-stage biological testing.

Do not infer clinical effectiveness from physicochemical data alone.

---

# Antimicrobial Implications

Disk or well diffusion findings may imply:

- MIC/MBC confirmation;
- diffusion limitation assessment;
- solvent-control interpretation;
- formulation optimization.

Do not recommend therapeutic use based only on inhibition zones.

---

# Educational Implications

Consider:

- pedagogical relevance;
- learning gains;
- implementation burden;
- teacher capacity;
- infrastructure;
- sustainability;
- equity.

---

# Educational Recommendation Guard

Do not recommend system-wide curricular change from one small classroom study without replication or implementation evidence.

---

# Organizational Implications

Possible implications include:

- leadership practice;
- learning systems;
- HR development;
- process redesign;
- resource allocation.

Consider organizational context and implementation feasibility.

---

# Workplace Learning Implications

Implications may concern:

- informal learning;
- learning culture;
- professional development;
- support;
- digital learning;
- organizational learning.

Do not reduce complex workplace learning to one significant predictor.

---

# Engineering Implications

Engineering implications may address:

- design tolerance;
- process optimization;
- safety margin;
- reliability;
- material selection;
- efficiency.

Recommendations should respect the tested operating range.

---

# Policy Implications

Policy implications require stronger evidence than descriptive findings alone.

Consider:

- population impact;
- causal evidence;
- feasibility;
- cost;
- equity;
- acceptability;
- implementation;
- unintended consequences.

---

# Policy Recommendation Strength

Classify:

- `POLICY_RELEVANT`
- `POLICY_PILOT_JUSTIFIED`
- `POLICY_CONSIDERATION`
- `POLICY_CHANGE_PREMATURE`
- `NO_POLICY_IMPLICATION`

---

# Policy Evidence Ladder

```text
Descriptive evidence
      ↓
Associational evidence
      ↓
Causal evidence
      ↓
Replication
      ↓
Implementation evidence
      ↓
Economic / equity evidence
      ↓
Policy readiness
```

---

# Regulation Implications

Regulatory implications require:

- legal relevance;
- safety;
- effectiveness;
- standard compliance;
- evidence maturity.

Do not infer regulatory recommendation from novelty alone.

---

# Implementation Implications

Implementation implications address:

- adoption;
- fidelity;
- feasibility;
- acceptability;
- reach;
- sustainability;
- scalability;
- adaptation.

---

# Implementation Readiness

Classify:

- `READY_FOR_IMPLEMENTATION`
- `READY_FOR_PILOT`
- `REQUIRES_ADAPTATION`
- `REQUIRES_VALIDATION`
- `NOT_READY`

---

# Feasibility

Assess:

- cost;
- personnel;
- infrastructure;
- time;
- training;
- workflow;
- technology.

---

# Acceptability

Consider stakeholders:

- patients;
- clinicians;
- teachers;
- students;
- managers;
- policymakers;
- communities.

---

# Adoption

Evidence of efficacy does not guarantee adoption.

---

# Fidelity

Implementation may fail if fidelity is low.

---

# Adaptation

Adaptation may be necessary across contexts.

Document what may change without undermining the intervention mechanism.

---

# Sustainability

Long-term continuation requires:

- resources;
- ownership;
- monitoring;
- institutional support.

---

# Scalability

A successful pilot does not prove scalability.

---

# Equity Implications

Assess whether implications differ across:

- socioeconomic groups;
- geography;
- sex/gender;
- disability;
- underserved populations;
- digital access;
- service access.

---

# Equity Guard

Do not recommend an intervention that may widen inequity without acknowledging the risk.

---

# Safety Implications

Assess:

- adverse effects;
- unintended consequences;
- risk exposure;
- monitoring needs.

---

# Benefit-Harm Balance

Recommendations should consider both benefit and harm.

---

# Economic Implications

Consider:

- cost;
- resource use;
- opportunity cost;
- cost-effectiveness;
- affordability.

Do not claim cost-effectiveness without economic evidence.

---

# Stakeholder Implications

Identify who is affected.

Possible stakeholders:

- patients;
- caregivers;
- clinicians;
- researchers;
- teachers;
- students;
- managers;
- institutions;
- policymakers;
- industry;
- communities.

---

# Stakeholder Matrix

| Stakeholder | Supported Implication | Required Condition | Risk | Actionability |
|---|---|---|---|---|

---

# Short-Term vs Long-Term Implications

Classify:

- immediate;
- short-term;
- medium-term;
- long-term.

Do not mix readiness levels.

---

# Immediate Implication

May involve:

- interpretation;
- monitoring;
- pilot;
- replication.

---

# Long-Term Implication

May involve:

- guideline change;
- policy;
- system redesign;
- broad implementation.

Requires stronger evidence.

---

# Future Research Implications

Future research should address unresolved scientific uncertainty.

Possible needs:

- replication;
- external validation;
- causal testing;
- longitudinal follow-up;
- mechanism testing;
- dose-response;
- implementation;
- economic evaluation;
- subgroup confirmation;
- measurement improvement.

---

# Generic Future Research Guard

Avoid:

> Future studies should use larger samples.

Prefer:

> A larger multi-site sample is needed to estimate the observed interaction with adequate precision and test whether the effect generalizes across institutional contexts.

---

# Research Gap Continuity

Future research should map back to:

- unresolved gap;
- partial answer;
- newly discovered boundary;
- contradiction;
- new mechanism hypothesis.

---

# New Gap Guard

Do not invent a new research gap solely to extend the discussion.

---

# Research Roadmap Handoff

When future research forms a coherent sequence, pass to `research-roadmap`.

Use:

```yaml
roadmap_handoff:
  current_evidence:
  unresolved_question:
  next_validation_step:
  next_mechanism_step:
  next_translation_step:
  long_term_goal:
```

---

# Replication Implication

Specify:

- what to replicate;
- in whom;
- under which design;
- with which outcome.

---

# External Validation Implication

Predictive or diagnostic models often need external validation before adoption.

---

# Prospective Validation

Retrospective performance does not guarantee prospective utility.

---

# Mechanism Testing Implication

If mechanism evidence is indirect, recommend direct testing.

---

# Mediation Follow-Up

A cross-sectional mediation result may justify longitudinal or experimental mediation testing.

---

# Moderation Follow-Up

An interaction may justify confirmatory subgroup study if prespecified and plausible.

---

# Null Finding Follow-Up

Future research may need:

- improved precision;
- equivalence design;
- alternative measurement;
- stronger intervention.

---

# Contradiction Follow-Up

Conflicting results may justify:

- replication;
- harmonized measures;
- individual-participant data;
- context comparison.

---

# Qualitative Future Research

May focus on:

- deviant cases;
- underexplored contexts;
- mechanism refinement;
- transferability;
- longitudinal qualitative work.

---

# Mixed-Method Future Research

May strengthen integration through:

- sequential design;
- joint displays;
- embedded process evaluation;
- explanatory follow-up.

---

# Meta-Analysis Future Research

May identify needs for:

- standardized outcomes;
- longer follow-up;
- better reporting;
- low-bias trials;
- individual participant data.

---

# Strength-to-Implication Mapping

| Evidence Strength | Recommended Language |
|---|---|
| High | supports, justifies, can inform |
| Moderate | suggests, may inform, warrants consideration |
| Low | raises possibility, warrants testing |
| Very low | hypothesis-generating only |

---

# Language Calibration

Strong:

- supports;
- justifies;
- can inform.

Moderate:

- suggests;
- may inform;
- warrants consideration.

Tentative:

- may indicate;
- could motivate;
- warrants further study.

---

# Avoid Absolute Language

Avoid:

- proves;
- guarantees;
- should always;
- must be implemented universally.

unless evidence truly supports such language.

---

# Recommendation Specificity

A recommendation should specify:

- actor;
- action;
- population;
- setting;
- condition;
- evidence strength.

---

# Recommendation Template

> [Actor] may consider [action] for [population/context] when [condition], because [supported finding]. The recommendation is [strength] and should be revisited after [required evidence].

---

# Conditional Recommendation

Use:

> If [condition] is present, [action] may be reasonable.

This is often preferable to universal recommendation.

---

# No-Action Implication

Sometimes the correct implication is:

> Current practice should not change yet.

This is scientifically valid.

---

# De-Implementation

Evidence may imply reducing or discontinuing ineffective practices.

Requires strong evidence and attention to harm.

---

# Uncertainty Communication

Implications should state what remains uncertain.

---

# Decision Threshold

When possible, identify what evidence would change the recommendation.

---

# Practical Importance vs Statistical Importance

A large practical effect with uncertainty may warrant further testing.

A tiny precise effect may warrant little action.

---

# Population Impact

A small individual effect may matter at population scale.

Do not dismiss automatically.

---

# Baseline Risk

Absolute benefit may depend on baseline risk.

---

# Resource-Limited Context

Recommendations may differ when resources are constrained.

---

# Digital Intervention Implications

Consider:

- infrastructure;
- device access;
- literacy;
- privacy;
- maintenance;
- training.

---

# AI Implications

AI-related implications should address:

- validation;
- bias;
- explainability;
- data governance;
- drift;
- human oversight.

Do not recommend deployment from development-set accuracy alone.

---

# Prediction Model Implementation

Before deployment consider:

- calibration;
- external validation;
- workflow;
- decision impact;
- monitoring.

---

# Diagnostic Implementation

Clinical adoption may require:

- threshold selection;
- clinical utility;
- availability;
- cost;
- false-positive consequences;
- false-negative consequences.

---

# SEM Implications

A structural path may imply theoretical relevance, not necessarily intervention relevance.

---

# PLS-SEM Implications

Do not recommend managerial or policy action solely from path significance.

Consider magnitude, predictive relevance, design, and context.

---

# Qualitative Implications

Qualitative implications may be highly actionable when they reveal:

- barriers;
- facilitators;
- process failures;
- stakeholder priorities;
- contextual mechanisms.

Actionability does not require numerical effect sizes.

---

# Mixed-Method Implications

Integrated implications should derive from meta-inference.

Do not privilege the quantitative strand automatically.

---

# Discordant Mixed-Method Implications

Discordance may imply:

- measurement revision;
- implementation adaptation;
- stakeholder engagement;
- further investigation.

---

# Meta-Analysis Implications

A pooled estimate may inform practice only when:

- studies are sufficiently comparable;
- risk of bias is acceptable;
- heterogeneity is understood;
- prediction intervals are considered.

---

# Prediction Interval Guard

If the prediction interval includes harm or no effect, universal recommendation may be premature.

---

# Certainty of Evidence

If a formal certainty framework exists, use it.

Do not invent GRADE ratings without proper assessment.

---

# Guideline Implications

Guideline change generally requires:

- body of evidence;
- certainty assessment;
- benefit-harm;
- values;
- resources;
- equity;
- feasibility.

One study rarely suffices.

---

# Target Journal Guard

Journal scope does not determine implication strength.

---

# APC Independence

APC status must not influence implication construction.

---

# Phenomenon Evidence

Official statistics may help quantify why implications matter.

They do not strengthen causal evidence by themselves.

---

# Policy Data

Use authoritative phenomenon evidence for:

- population burden;
- service coverage;
- regulatory context;
- implementation scale.

---

# Implication Matrix

| Finding | Implication Type | Evidence Strength | Boundary | Actionability | Recommendation |
|---|---|---|---|---|---|

---

# Recommendation Matrix

| Actor | Action | Population | Condition | Strength | Evidence Needed |
|---|---|---|---|---|---|

---

# Future Research Matrix

| Unresolved Question | Why It Matters | Next Design | Required Evidence |
|---|---|---|---|

---

# Risk Matrix

| Proposed Action | Benefit | Risk | Uncertainty | Mitigation |
|---|---|---|---|---|

---

# Implementation Matrix

| Intervention | Feasibility | Acceptability | Fidelity Need | Scalability | Readiness |
|---|---|---|---|---|---|

---

# Implication Passport

Recommended internal representation:

```yaml
implication:
  status:
  source_finding:
  evidence_strength:
  uncertainty:
  contribution:
  implication_type:
  stakeholder:
  action:
  population:
  setting:
  boundary_conditions:
  feasibility:
  acceptability:
  safety:
  equity:
  economic_context:
  implementation_readiness:
  recommendation_strength:
  unsupported_actions:
  future_evidence_needed:
  roadmap_handoff:
```

Unknown fields remain unknown.

---

# Implication Workflow

Use:

```text
1. Import supported findings
2. Import contribution and limitations
3. Classify evidence strength
4. Identify implication type
5. Identify stakeholder
6. Define boundary conditions
7. Assess feasibility
8. Assess harms and trade-offs
9. Calibrate recommendation strength
10. Identify unsupported actions
11. Define future evidence needed
12. Generate roadmap handoff when useful
```

---

# Minimal Output

For a simple request provide:

## Supported Finding
[...]

## Main Implication
[...]

## Who It Applies To
[...]

## Boundary Conditions
[...]

## Recommendation Strength
[...]

## What Should Not Yet Be Done
[...]

## Evidence Still Needed
[...]

---

# Comprehensive Output

When full implication analysis is requested:

## A. Supported Findings
[...]

## B. Scientific Contribution
[...]

## C. Theoretical Implications
[...]

## D. Scientific Implications
[...]

## E. Mechanistic Implications
[...]

## F. Methodological Implications
[...]

## G. Measurement Implications
[...]

## H. Practical Implications
[...]

## I. Clinical Implications
[...]

## J. Educational Implications
[...]

## K. Organizational Implications
[...]

## L. Engineering Implications
[...]

## M. Policy Implications
[...]

## N. Implementation Implications
[...]

## O. Equity Implications
[...]

## P. Safety Implications
[...]

## Q. Economic Implications
[...]

## R. Stakeholders
[...]

## S. Boundary Conditions
[...]

## T. Recommendation Strength
[...]

## U. Unsupported Recommendations
[...]

## V. Future Research
[...]

## W. Research Roadmap Handoff
[...]

---

# Relationship with Scientific Discussion

`scientific-discussion` establishes scientific meaning and contribution.

`implication-builder` determines what those conclusions legitimately imply.

Use:

```text
scientific-discussion
      ↓
implication-builder
```

Do not re-open rejected interpretations.

---

# Relationship with Result Interpreter

`result-interpreter` defines supported claims.

Implications may use only those supported claims.

---

# Relationship with Novelty Auditor

Novelty determines what the study adds.

Implications should not exceed the audited contribution.

---

# Relationship with Gap Validator

A study may reduce a validated gap only partially.

Implications should reflect residual uncertainty.

---

# Relationship with Theoretical Framework

Theory implications may include:

- support;
- refinement;
- boundary;
- challenge.

---

# Relationship with Conceptual Framework

Conceptual implications may include:

- new relationship;
- revised pathway;
- removed construct;
- contextual boundary.

---

# Relationship with Methodology Architect

Methodological implications should route future design changes back to `methodology-architect`.

---

# Relationship with Research Roadmap

When multiple follow-up studies are required, route to `research-roadmap`.

---

# Relationship with Manuscript Architect

After implications are stable, the manuscript can integrate them into:

- Discussion;
- Conclusion;
- Recommendations;
- Future Research.

---

# User-Friendly Behavior

Prefer:

> The study supports a practical implication, but not immediate system-wide implementation. Because the effect was moderate and observed in one institution, the most defensible next step is a controlled pilot in comparable settings followed by external validation.

Or:

> The genetic association is potentially useful for risk stratification, but it is not yet sufficient to recommend routine genotyping. Replication in an independent population and evaluation of predictive utility are still required.

Or:

> The qualitative findings indicate that implementation barriers are not merely individual but organizational. The implication is therefore not simply to train staff, but to address workload, access to resources, and supervisory support.

Or:

> The meta-analysis supports an average benefit, but the prediction interval suggests that some settings may experience little effect. This argues for conditional rather than universal implementation.

---

# Avoid These Behaviors

Do not:

- equate significance with recommendation;
- recommend intervention from association alone;
- recommend policy from one narrow study;
- recommend clinical implementation without utility evidence;
- recommend genetic testing from one association study;
- recommend deployment from development-set prediction accuracy;
- recommend universal adoption from one context;
- ignore harms;
- ignore cost;
- ignore equity;
- ignore implementation feasibility;
- overstate novelty;
- invent practical implications unrelated to findings;
- generate generic future research;
- claim guideline change from one study;
- use target-journal preferences to inflate implications;
- let APC status influence implication strength;
- convert laboratory findings directly into clinical recommendations;
- convert PLS-SEM paths directly into managerial mandates;
- claim causal intervention from cross-sectional mediation;
- ignore contradictory evidence;
- ignore uncertainty.

---

# Stop Conditions

Do not classify implications as ready when:

- scientific discussion is incomplete;
- evidence strength is unclear;
- contribution is unclear;
- boundary conditions are unknown;
- recommendation exceeds causal evidence;
- feasibility is unknown for action-oriented recommendations;
- harms are ignored;
- equity is ignored where relevant;
- implementation readiness is assumed;
- clinical utility is untested;
- policy readiness is unsupported;
- future-research recommendations are generic;
- implication language exceeds certainty.

Use:

- `RETURN_TO_SCIENTIFIC_DISCUSSION`
- `RETURN_TO_RESULT_INTERPRETER`
- `RETURN_TO_NOVELTY_AUDITOR`
- `RETURN_TO_GAP_VALIDATOR`
- `RETURN_TO_METHODOLOGY_ARCHITECT`
- `IMPLICATIONS_REQUIRE_REVISION`

when appropriate.

---

# Success Criterion

`implication-builder` succeeds when defensibly interpreted and scientifically discussed findings have been translated into evidence-proportionate implications that clearly distinguish theoretical, scientific, mechanistic, methodological, measurement, practical, clinical, educational, organizational, engineering, policy, implementation, equity, safety, economic, and future-research consequences; explicitly identify stakeholders, actionability, feasibility, boundary conditions, uncertainty, harms, trade-offs, and implementation readiness; calibrate recommendation strength to evidence strength; specify what should not yet be recommended; identify the additional evidence required before stronger action; and, when appropriate, generate a coherent handoff to `research-roadmap` or manuscript development without allowing statistical significance, publication strategy, contextual novelty, software output, unsupported causality, or generic recommendation language to inflate what the study can legitimately change.
