---
name: reviewer-simulator
description: Simulate rigorous, journal-aware, evidence-grounded peer review of a scientifically stable manuscript after journal matching or when the researcher explicitly requests adversarial pre-submission review. Use to generate independent reviewer reports, editorial synthesis, major/minor concerns, claim-evidence challenges, methodological and statistical critiques, reporting-guideline checks, novelty and contribution challenges, journal-fit concerns, reproducibility questions, ethics and transparency checks, likely author-response tasks, and revision priorities without inventing evidence, citations, journal policies, acceptance probabilities, reviewer identities, or scientific defects that are not supported by the manuscript and verified context. The simulator must preserve the distinction between actual peer review and simulated review, must not substitute for manuscript audit, and must route genuine scientific problems back to the appropriate upstream skill before publication-oriented revision.
---

# Reviewer Simulator

## Purpose

`reviewer-simulator` performs an adversarial pre-submission review of a scientifically stable manuscript.

Its central question is:

> If independent expert reviewers and an editor critically evaluated this manuscript for the selected or intended journal, what scientifically defensible concerns, revision requests, strengths, and publication risks would they most plausibly identify?

The goal is not to predict actual reviewer comments.

The goal is to expose vulnerabilities before submission.

---

# Core Principle

Use:

> Simulate criticism to strengthen the manuscript, not to manufacture rejection.

The simulator must be:

- evidence-grounded;
- manuscript-specific;
- method-aware;
- journal-aware when a target journal is known;
- transparent about uncertainty;
- explicit about simulated status;
- independent from author preference;
- adversarial without becoming arbitrary.

---

# Position in the Framework

Preferred architecture:

```text
manuscript-writer
      ↓
manuscript-auditor
      ↓
journal-matcher
      ↓
reviewer-simulator
      ↓
reviewer-response
```

`reviewer-simulator` is downstream of scientific audit and normally downstream of journal matching.

It does not replace either.

---

# Simulation Boundary

Reviewer simulation may critique:

- research question;
- theoretical framing;
- conceptual framing;
- study design;
- sampling;
- methods;
- measurement;
- analysis;
- reporting;
- results;
- interpretation;
- discussion;
- limitations;
- implications;
- novelty;
- references;
- ethics;
- transparency;
- journal fit;
- presentation.

Reviewer simulation must not:

- invent data;
- invent missing methods;
- invent citations;
- invent journal rules;
- invent reviewer identities;
- invent acceptance probability;
- invent editorial decisions as facts;
- pretend to know confidential peer-review criteria;
- rewrite the scientific record merely to satisfy a simulated reviewer.

---

# Simulated vs Actual Review

Always preserve:

```text
SIMULATED REVIEW
≠
ACTUAL JOURNAL PEER REVIEW
```

Use explicit wording such as:

> The following is a simulated pre-submission peer review based on the manuscript, verified journal context, and standard scientific-review principles. It does not represent comments from the actual journal, editor, or reviewers.

---

# Entry Modes

Classify the request as one or more of:

- `FULL_MANUSCRIPT_SIMULATION`
- `JOURNAL_AWARE_SIMULATION`
- `GENERAL_PEER_REVIEW_SIMULATION`
- `METHODS_REVIEW`
- `STATISTICAL_REVIEW`
- `RESULTS_REVIEW`
- `DISCUSSION_REVIEW`
- `NOVELTY_REVIEW`
- `REPORTING_GUIDELINE_REVIEW`
- `REFERENCE_REVIEW`
- `ETHICS_TRANSPARENCY_REVIEW`
- `EDITORIAL_SCREENING_SIMULATION`
- `DESK_REJECTION_RISK_SIMULATION`
- `SECTION_SPECIFIC_SIMULATION`
- `MULTI_REVIEWER_SIMULATION`
- `EDITOR_DECISION_SIMULATION`
- `REVISION_READINESS_REVIEW`
- `POST_REVISION_RE_REVIEW`

---

# Readiness Gate

Before full reviewer simulation, determine whether the current manuscript version:

- has passed `manuscript-auditor`;
- has unresolved submission-blocking issues;
- has materially changed since the last audit;
- has a selected journal;
- has sufficient manuscript content for the requested review.

Possible statuses:

- `SIMULATION_READY`
- `SIMULATION_READY_WITH_MINOR_OPEN_ISSUES`
- `SCIENTIFIC_AUDIT_REQUIRED`
- `JOURNAL_MATCHING_RECOMMENDED`
- `MANUSCRIPT_VERSION_CHANGED`
- `MANUSCRIPT_INCOMPLETE`
- `SECTION_ONLY_REVIEW_POSSIBLE`
- `INSUFFICIENT_CONTEXT`

---

# Version-Aware Audit Gate

If the manuscript has not yet passed scientific audit, or if material scientific revisions have occurred since the last audit:

```text
manuscript-auditor
      ↓
reviewer-simulator
```

If the same manuscript version has already passed scientific audit with no unresolved submission-blocking issues:

```text
reviewer-simulator
```

may run directly.

Do not repeat a completed audit unnecessarily when the manuscript has not materially changed.

---

# Journal-Aware Gate

If a target journal is known and verified:

```text
journal-matcher
      ↓
reviewer-simulator
```

may use:

- aims and scope;
- article type;
- audience;
- reporting requirements;
- word limits;
- formatting expectations;
- recent relevant content;
- explicit author instructions.

Do not infer undocumented editorial preferences.

---

# Journal Unknown

If no target journal is selected:

- simulate general disciplinary peer review;
- state that journal-specific fit and editorial expectations are not being assessed;
- optionally recommend `journal-matcher` afterward.

---

# Required Upstream Context

Use available information from:

- `manuscript-auditor`;
- `journal-matcher`;
- `manuscript-architect`;
- `manuscript-writer`;
- `research-question-builder`;
- `hypothesis-builder`;
- `theoretical-framework`;
- `conceptual-framework`;
- `methodology-architect`;
- `protocol-builder`;
- `sampling-strategy`;
- `instrument-design`;
- `analysis-planner`;
- `statistical-method-selector`;
- `qualitative-analysis`;
- `mixed-method-analysis`;
- `meta-analysis`;
- `result-interpreter`;
- `scientific-discussion`;
- `implication-builder`;
- `sota-builder`;
- `gap-validator`;
- `novelty-auditor`;
- `source-verification`;
- `reference-integrity-guard`;
- `research-intake`.

Do not ask the researcher to repeat information already contained in available materials.

---

# Manuscript Review Passport

Before simulation, extract:

```yaml
review_passport:
  manuscript_version:
  working_title:
  article_type:
  target_journal:
  journal_verification_status:
  discipline:
  subdiscipline:
  research_question:
  hypothesis:
  study_design:
  sample:
  setting:
  methods:
  measures:
  analysis:
  primary_outcome:
  secondary_outcomes:
  main_findings:
  null_findings:
  contradictory_findings:
  causal_status:
  novelty_type:
  contribution_type:
  reporting_guideline:
  ethics_status:
  data_availability:
  code_availability:
  conflict_of_interest:
  funding:
  manuscript_audit_status:
  unresolved_audit_items:
```

---

# Reviewer Persona Architecture

When multi-reviewer simulation is useful, construct differentiated reviewer roles.

Possible personas:

- `REVIEWER_1_DOMAIN_EXPERT`
- `REVIEWER_2_METHODS_EXPERT`
- `REVIEWER_3_STATISTICAL_EXPERT`
- `REVIEWER_4_CLINICAL_OR_APPLIED_EXPERT`
- `REVIEWER_5_THEORY_OR_CONCEPTUAL_EXPERT`
- `REVIEWER_6_REPORTING_REPRODUCIBILITY_EXPERT`
- `EDITORIAL_REVIEWER`

Do not assign real names.

---

# Persona Guard

Reviewer personas represent analytical perspectives, not stereotypes.

Do not simulate hostility merely for realism.

---

# Multi-Reviewer Independence

Each reviewer should independently assess the manuscript before editorial synthesis.

Preferred logic:

```text
Reviewer 1
      ↓
Independent Report

Reviewer 2
      ↓
Independent Report

Reviewer 3
      ↓
Independent Report

        ↓
Editorial Synthesis
```

Do not make all reviewers repeat the same concerns.

---

# Reviewer Count

Use as few reviewers as necessary.

Typical:

- 1 reviewer for focused section review;
- 2 reviewers for standard manuscript simulation;
- 3 reviewers for complex or interdisciplinary manuscripts;
- 4+ only when clearly useful.

---

# Reviewer Expertise Matching

Match reviewer lenses to the manuscript.

Examples:

### Pharmacogenetics

- clinical pharmacology;
- genetics/pharmacogenomics;
- biostatistics.

### Formulation

- pharmaceutics;
- materials/characterization;
- microbiology when antimicrobial activity is central.

### Education

- domain pedagogy;
- measurement/methodology;
- statistics or qualitative methods.

### PLS-SEM

- substantive-domain expert;
- measurement-model expert;
- structural-model/methods expert.

---

# Editorial Simulation

An editor-style synthesis may evaluate:

- journal scope;
- article type;
- novelty;
- priority;
- methodological credibility;
- reporting completeness;
- reviewer disagreement;
- revision burden.

---

# Editorial Decision Labels

Use simulated labels only:

- `SIMULATED_ACCEPTABLE_WITH_MINOR_REVISION`
- `SIMULATED_MAJOR_REVISION`
- `SIMULATED_RECONSIDER_AFTER_MAJOR_REVISION`
- `SIMULATED_REJECT_AND_RESUBMIT`
- `SIMULATED_DESK_REJECTION_RISK`
- `SIMULATED_OUT_OF_SCOPE`
- `SIMULATED_NOT_READY_FOR_DECISION`

Never present these as actual journal decisions.

---

# No Acceptance Prediction

Do not say:

> This manuscript has an 80% chance of acceptance.

unless a valid predictive model and evidence exist, which will usually not be the case.

---

# Desk-Rejection Simulation

Desk-rejection risk may be based on:

- scope mismatch;
- article-type mismatch;
- weak priority;
- obvious reporting incompleteness;
- severe methodological flaw;
- unsupported novelty claim;
- manuscript presentation that prevents evaluation.

---

# Desk-Rejection Risk Classes

Use:

- `LOW`
- `MODERATE`
- `HIGH`
- `UNCERTAIN`

Explain the basis.

---

# Review Dimensions

Assess as relevant:

1. title;
2. abstract;
3. introduction;
4. research question;
5. theory;
6. conceptual framework;
7. methods;
8. sampling;
9. instruments;
10. analysis;
11. results;
12. discussion;
13. limitations;
14. implications;
15. conclusion;
16. novelty;
17. references;
18. tables;
19. figures;
20. supplementary materials;
21. ethics;
22. transparency;
23. reproducibility;
24. reporting guideline;
25. journal fit.

---

# Scientific Question Review

Check:

- clarity;
- answerability;
- alignment with design;
- alignment with outcomes;
- scope;
- causal wording;
- consistency across manuscript sections.

---

# Question Drift Guard

Detect:

```text
Introduction Question A
      ↓
Methods Question B
      ↓
Results Question C
      ↓
Discussion Claim D
```

Flag drift explicitly.

---

# Hypothesis Review

When hypotheses exist, check:

- a priori status;
- theoretical or mechanistic basis;
- directionality;
- testability;
- consistency with analysis;
- outcome mapping;
- post-hoc reframing.

---

# HARKing Risk

Flag when hypotheses appear to have been written after results without transparent labeling.

Use:

- `LOW_RISK`
- `POSSIBLE`
- `LIKELY`
- `UNDETERMINED`

---

# Theory Review

Check whether theory:

- is actually needed;
- is correctly represented;
- matches constructs;
- explains expected relationships;
- has boundary conditions;
- is used consistently;
- is not merely decorative.

---

# Conceptual Framework Review

Check:

- concept definitions;
- arrows;
- causal semantics;
- mediator/moderator roles;
- confounders;
- temporal ordering;
- multilevel structure;
- redundancy.

---

# Introduction Review

Evaluate whether the introduction establishes:

```text
Phenomenon / Context
      ↓
Scientific Knowledge
      ↓
State of the Art
      ↓
Validated Gap
      ↓
Audited Novelty
      ↓
Research Question / Objective
```

when appropriate.

---

# Phenomenon Evidence Review

Check whether real-world claims rely on suitable authority-first evidence.

Examples:

- official statistics;
- government data;
- regulatory documents;
- institutional reports;
- authoritative international organizations.

---

# Scholarly Evidence Review

Check whether scientific claims rely on suitable scholarly evidence.

Prefer verified primary literature, systematic reviews, meta-analyses, and current State of the Art as appropriate.

---

# Background Evidence Role Guard

Do not allow:

```text
official statistic
→ causal mechanism
```

or:

```text
journal article
→ legal/regulatory status
```

without appropriate evidence.

---

# Methods Review

Check:

- design naming;
- setting;
- participants/materials;
- eligibility;
- sampling;
- interventions/exposures;
- measurements;
- outcomes;
- procedures;
- reproducibility;
- analysis plan;
- ethics;
- deviations from protocol.

---

# Design Fidelity

Ask:

> Does the manuscript claim a design that matches what was actually done?

---

# Causal Design Guard

Flag causal language unsupported by design.

Examples:

```text
cross-sectional association
≠
causal effect
```

```text
prediction
≠
causal explanation
```

---

# Sampling Review

Check:

- sampling frame;
- recruitment;
- inclusion/exclusion;
- representativeness;
- sample-size justification;
- attrition;
- missingness;
- clustering;
- selection bias.

---

# Sample Size Review

Do not reduce adequacy to an arbitrary threshold.

Consider:

- design;
- estimand;
- number of parameters;
- event count;
- expected effect;
- precision;
- power;
- model complexity;
- validation design.

---

# Instrument Review

Check:

- construct definition;
- measurement validity;
- reliability;
- adaptation;
- translation;
- calibration;
- scoring;
- observer training;
- blinding when relevant.

---

# Measurement Model Review

For latent-variable studies, assess:

- indicator quality;
- construct validity;
- discriminant validity;
- reliability;
- model specification;
- formative vs reflective logic.

---

# Statistical Review

Check as appropriate:

- estimand;
- outcome type;
- predictor structure;
- dependency structure;
- repeated measures;
- clustering;
- confounding;
- missing data;
- multiplicity;
- model assumptions;
- effect estimates;
- uncertainty;
- sensitivity analyses;
- model diagnostics.

---

# Statistical Significance Guard

Flag:

```text
p < 0.05
      ↓
important
```

when importance is not otherwise justified.

---

# Non-Significance Guard

Flag:

```text
p ≥ 0.05
      ↓
no effect
```

when uncertainty remains.

---

# Effect Size Review

Check whether the manuscript reports and interprets:

- magnitude;
- direction;
- uncertainty;
- clinical/practical meaning;
- confidence intervals.

---

# Multiple Testing Review

Check whether multiple comparisons, outcomes, subgroups, or models create inflated false-positive risk.

---

# Missing Data Review

Ask:

- how much is missing;
- why;
- how handled;
- whether assumptions are plausible;
- whether sensitivity analyses are needed.

---

# Regression Review

Check:

- outcome family;
- link function;
- reference categories;
- collinearity;
- nonlinearity;
- interactions;
- confounding;
- diagnostics;
- overfitting.

---

# Logistic Regression Review

Check:

- event counts;
- coding;
- reference group;
- odds-ratio interpretation;
- calibration;
- discrimination when predictive;
- separation;
- model stability.

---

# Survival Analysis Review

Check:

- time origin;
- censoring;
- proportional hazards;
- competing risks;
- time-varying effects;
- event counts.

---

# Longitudinal Review

Check:

- within-subject dependence;
- time coding;
- missing follow-up;
- repeated measures;
- random effects or correlation structure;
- temporal interpretation.

---

# Multilevel Review

Check:

- level definitions;
- cluster counts;
- nesting;
- random effects;
- ICC;
- cross-level effects;
- level-specific interpretation.

---

# Mediation Review

Check:

- temporal ordering;
- causal assumptions;
- direct/indirect effects;
- confidence intervals;
- confounding;
- cross-sectional limitations.

---

# Moderation Review

Check:

- interaction term;
- centering if relevant;
- conditional effects;
- probing;
- interpretation;
- visualization.

---

# SEM Review

Check:

- theory/model basis;
- identification;
- measurement model;
- structural model;
- fit;
- modification indices;
- post-hoc changes;
- indirect effects.

---

# PLS-SEM Review

Check as relevant:

- construct type;
- indicator specification;
- outer loadings/weights;
- reliability;
- convergent validity;
- discriminant validity;
- VIF;
- path estimates;
- bootstrap inference;
- R²;
- f²;
- Q²/predictive assessment;
- mediation;
- moderation;
- model purpose;
- causal claims.

---

# Machine Learning Review

Check:

- prediction target;
- data leakage;
- train/test separation;
- cross-validation;
- hyperparameter tuning;
- class imbalance;
- calibration;
- discrimination;
- external validation;
- interpretability;
- overfitting.

---

# Diagnostic Study Review

Check:

- reference standard;
- index test;
- blinding;
- spectrum;
- threshold selection;
- sensitivity;
- specificity;
- predictive values;
- ROC analysis;
- confidence intervals;
- STARD alignment.

---

# Prediction Model Review

Check:

- model development;
- predictor selection;
- overfitting;
- internal validation;
- calibration;
- discrimination;
- external validation;
- TRIPOD alignment.

---

# Pharmacokinetic Review

Check:

- sampling schedule;
- assay;
- PK model;
- parameter estimation;
- covariates;
- exposure metrics;
- variability;
- model diagnostics;
- dosing interpretation.

---

# Pharmacogenetic Review

Check:

- SNP selection rationale;
- genotyping quality;
- allele/genotype coding;
- Hardy-Weinberg equilibrium;
- inheritance models;
- multiple testing;
- population structure;
- haplotypes when relevant;
- clinical covariates;
- interaction;
- outcome definition;
- replication/validation.

---

# Formulation Review

Check:

- formulation rationale;
- excipient concentrations;
- process parameters;
- physicochemical characterization;
- replicates;
- stability;
- biological testing;
- controls;
- analytical methods;
- statistical comparison.

---

# Antimicrobial Review

Check:

- organism identification;
- strain;
- inoculum;
- controls;
- diffusion-method limitations;
- MIC/MBC when relevant;
- replicate structure;
- interpretation of zone diameter;
- solvent effects.

---

# Experimental Review

Check:

- randomization;
- controls;
- replication;
- blinding;
- batch effects;
- technical vs biological replicates;
- intervention fidelity;
- measurement reliability.

---

# Qualitative Review

Check:

- research paradigm;
- sampling logic;
- data source;
- saturation/information power;
- reflexivity;
- coding process;
- analytic method;
- negative cases;
- trustworthiness;
- audit trail;
- quotations;
- COREQ/SRQR alignment when relevant.

---

# Mixed-Methods Review

Check:

- rationale for mixing;
- design type;
- timing;
- priority;
- integration;
- joint displays;
- meta-inferences;
- contradiction management.

---

# Systematic Review Review

Check:

- protocol;
- eligibility criteria;
- databases;
- search strategy;
- screening;
- duplicate processes;
- risk of bias;
- synthesis;
- certainty assessment;
- PRISMA alignment.

---

# Meta-Analysis Review

Check:

- effect-size definition;
- model choice;
- heterogeneity;
- dependency;
- subgroup/meta-regression;
- publication bias;
- sensitivity analysis;
- study quality;
- certainty;
- interpretation.

---

# Results Review

Check:

- complete reporting;
- outcome hierarchy;
- primary vs secondary;
- exploratory analyses;
- numerical consistency;
- tables/figures;
- effect estimates;
- uncertainty;
- missingness;
- adverse events when relevant.

---

# Result Integrity

Compare across:

- abstract;
- main text;
- tables;
- figures;
- supplementary materials.

---

# Numerical Consistency Review

Check:

- n;
- percentages;
- denominators;
- totals;
- effect estimates;
- p-values;
- confidence intervals;
- rounding;
- units.

---

# Outcome Switching Review

Look for unexplained differences between:

- protocol/objective;
- methods;
- results;
- abstract;
- conclusion.

---

# Selective Reporting Review

Flag when unfavorable, null, or contradictory findings appear omitted or minimized.

---

# Null Result Review

Ensure null results are interpreted using:

- estimate;
- uncertainty;
- power/precision;
- confidence interval;
- clinical relevance.

---

# Contradictory Result Review

Check whether contradictory evidence is:

- acknowledged;
- explained cautiously;
- compared with literature;
- not hidden.

---

# Discussion Review

Assess whether the discussion:

- answers the research question;
- interprets rather than repeats results;
- compares with evidence;
- explains mechanisms cautiously;
- considers alternatives;
- addresses contradictions;
- respects design limits;
- states contribution;
- acknowledges limitations.

---

# Literature Comparison Review

Check whether the manuscript distinguishes:

- agreement;
- partial agreement;
- contradiction;
- context-specific difference;
- methodological difference;
- unresolved evidence.

---

# Mechanism Review

Flag unsupported mechanistic language.

Use:

- `SUPPORTED`
- `PLAUSIBLE`
- `SPECULATIVE`
- `UNSUPPORTED`

---

# Alternative Explanation Review

Ask:

> What plausible alternative explanation could account for the observed result?

---

# Confounding Review

Check whether alternative explanations from measured or unmeasured confounders are adequately addressed.

---

# Limitation Review

Check whether limitations are:

- specific;
- proportional;
- linked to inference;
- not generic disclaimers;
- not hidden.

---

# Strengths Review

Reviewers should also identify genuine strengths.

Do not write only criticism.

Potential strengths:

- rigorous design;
- rare dataset;
- underrepresented population;
- strong validation;
- transparent methods;
- robust sensitivity analyses;
- mechanistic contribution;
- reproducibility.

---

# Implication Review

Check whether implications are proportional to evidence.

Possible domains:

- theoretical;
- scientific;
- mechanistic;
- clinical;
- pharmaceutical;
- educational;
- organizational;
- policy;
- implementation;
- future research.

---

# Implication Escalation Guard

Flag:

```text
single observational study
→ policy recommendation
```

when unsupported.

---

# Clinical Claim Guard

Do not allow:

```text
statistical association
→ clinical recommendation
```

without adequate evidence.

---

# Policy Claim Guard

Policy recommendations require suitable evidence and context.

---

# Conclusion Review

Check whether conclusion:

- answers the stated question;
- matches results;
- preserves uncertainty;
- respects causal limits;
- does not introduce new evidence;
- does not overstate novelty.

---

# Novelty Review

Use output of `novelty-auditor`.

Challenge claims such as:

- first;
- novel;
- unique;
- unprecedented;
- groundbreaking.

Require verification.

---

# Contribution Review

Ask:

> What does this manuscript add that the closest competitor studies do not?

---

# Replication Value

Do not treat replication as inherently weak.

Assess whether it adds:

- population validation;
- external validity;
- methodological robustness;
- contradiction;
- boundary-condition evidence.

---

# State-of-the-Art Review

Check whether the manuscript is positioned against current evidence rather than obsolete literature.

---

# Reference Review

Assess:

- relevance;
- verification;
- completeness;
- recency;
- primary-source use;
- overcitation;
- citation padding;
- incorrect attribution;
- retractions.

---

# Reference Integrity Handoff

When citation integrity problems exist:

```text
reference-integrity-guard
```

should be invoked.

---

# Target-Journal Citation Guard

Do not recommend adding citations merely because they were published in the target journal.

---

# Self-Citation Guard

Do not recommend unnecessary self-citation.

---

# Retraction Guard

Retracted evidence must not support conclusions.

---

# Reporting Guideline Review

Check applicable standards such as:

- CONSORT;
- STROBE;
- PRISMA;
- STARD;
- TRIPOD;
- CARE;
- COREQ;
- SRQR;
- ARRIVE;
- CHEERS;
- SPIRIT;
- RECORD;
- SAGER.

---

# Reporting Status

Use:

- `COMPLETE`
- `PARTIAL`
- `MISSING`
- `NOT_APPLICABLE`

---

# Reporting vs Science

A complete checklist does not repair a scientifically weak study.

---

# Ethics Review

Check as applicable:

- ethics approval;
- informed consent;
- waiver;
- trial registration;
- protocol registration;
- privacy;
- vulnerable populations;
- animal ethics;
- data governance.

---

# Declaration Review

Check:

- funding;
- conflicts of interest;
- author contributions;
- data availability;
- code availability;
- AI-use disclosure;
- acknowledgments.

---

# AI Disclosure Review

When AI tools were used, check whether disclosure is required by the journal or institution.

Do not invent a policy.

---

# Reproducibility Review

Ask whether another researcher could understand and reproduce:

- sampling;
- intervention;
- measurement;
- analysis;
- code logic;
- data-processing steps.

---

# Data Availability Review

Classify:

- `OPEN`
- `CONTROLLED`
- `AVAILABLE_ON_REQUEST`
- `RESTRICTED`
- `NOT_AVAILABLE`
- `NOT_STATED`

---

# Code Availability Review

Classify:

- `OPEN`
- `AVAILABLE_ON_REQUEST`
- `NOT_AVAILABLE`
- `NOT_APPLICABLE`
- `NOT_STATED`

---

# Table Review

Check:

- title;
- self-containment;
- denominator;
- units;
- abbreviations;
- statistical notation;
- footnotes;
- reference groups;
- duplication with text.

---

# Figure Review

Check:

- scientific necessity;
- labels;
- axes;
- units;
- legends;
- uncertainty;
- sample sizes;
- accessibility;
- duplication.

---

# Supplementary Material Review

Check whether important methods or results are inappropriately hidden in supplements.

---

# Abstract Review

Check:

- objective;
- design;
- sample;
- methods;
- primary result;
- numerical estimates;
- uncertainty;
- conclusion;
- consistency with main text.

---

# Title Review

Check whether title accurately represents:

- design;
- population;
- exposure/intervention;
- outcome;
- causal status.

---

# Keywords Review

Check discoverability without keyword stuffing.

---

# Journal-Fit Review

When target journal is known, evaluate:

- scope;
- readership;
- article type;
- methodological fit;
- novelty fit;
- reporting expectations.

---

# Journal Prestige Guard

Do not simulate harsher review merely because a journal has a high metric.

---

# Reviewer Severity Architecture

Classify comments as:

- `CRITICAL`
- `MAJOR`
- `MODERATE`
- `MINOR`
- `EDITORIAL`

---

# Critical Issue

A critical issue threatens:

- scientific validity;
- ethical acceptability;
- core inference;
- data integrity;
- reproducibility;
- fundamental journal suitability.

---

# Major Issue

A major issue materially affects:

- interpretation;
- method credibility;
- reporting completeness;
- novelty;
- contribution;
- reproducibility.

---

# Moderate Issue

A moderate issue requires meaningful improvement but does not invalidate the core study.

---

# Minor Issue

A minor issue improves clarity, completeness, or precision.

---

# Editorial Issue

Editorial issues concern:

- grammar;
- formatting;
- style;
- numbering;
- presentation.

Do not inflate editorial issues into scientific criticism.

---

# Comment Structure

Each substantive comment should contain:

```yaml
review_comment:
  reviewer:
  section:
  severity:
  issue:
  evidence_from_manuscript:
  why_it_matters:
  requested_action:
  acceptable_resolution:
  upstream_skill_if_needed:
  confidence:
```

---

# Evidence-from-Manuscript Requirement

Every major or critical simulated concern should point to actual manuscript evidence or an explicit missing element.

Do not invent defects.

---

# Confidence Classification

Use:

- `HIGH_CONFIDENCE`
- `MODERATE_CONFIDENCE`
- `LOW_CONFIDENCE`
- `REQUIRES_VERIFICATION`

---

# Reviewer Comment Quality Guard

Avoid vague comments such as:

> The methods are weak.

Prefer:

> The manuscript describes a cross-sectional design but uses causal language in the Discussion. Please revise causal wording and clarify whether temporal ordering can be established.

---

# Reviewer Request Guard

A reviewer request should be:

- scientifically justified;
- proportionate;
- feasible when possible;
- linked to the manuscript.

---

# Impossible Reviewer Request

If a simulated reviewer requests data that cannot be collected retrospectively, distinguish:

- required scientific correction;
- desirable future work;
- impossible post-hoc request.

---

# New Experiment Request

Do not automatically recommend new experiments.

Ask whether the manuscript's claims actually require them.

---

# Scope Creep Guard

Do not let simulated reviewers expand the paper into a different study.

---

# Reviewer Contradiction

Different reviewers may disagree.

Record disagreement rather than forcing false consensus.

---

# Editorial Synthesis

After independent reports, summarize:

- shared concerns;
- reviewer-specific concerns;
- conflicts;
- strengths;
- revision burden;
- decision risk.

---

# Reviewer Agreement Matrix

Use:

| Issue | Reviewer 1 | Reviewer 2 | Reviewer 3 | Consensus |
|---|---|---|---|---|

---

# Revision Priority Matrix

Use:

| Priority | Issue | Severity | Scientific Impact | Effort | Upstream Route |
|---|---|---|---|---|---|

---

# Simulated Decision Logic

Do not derive decision from comment count alone.

Consider:

- severity;
- validity;
- fixability;
- novelty;
- journal fit;
- reporting completeness.

---

# Simulated Minor Revision

Appropriate when:

- no critical issue;
- no unresolved major scientific flaw;
- changes mainly clarify/report.

---

# Simulated Major Revision

Appropriate when:

- core study remains viable;
- substantial clarification/reanalysis/reframing is needed.

---

# Simulated Reject and Resubmit

Appropriate when:

- major reconstruction is needed;
- journal may reconsider a fundamentally revised manuscript.

---

# Simulated Rejection

Use cautiously when:

- fatal scientific flaw;
- irreparable design mismatch;
- out of scope;
- unsupported core claim that cannot be fixed.

---

# Upstream Routing

When simulation reveals genuine scientific problems, route appropriately.

Examples:

### Research question problem

`research-question-builder`

### Theory problem

`theoretical-framework`

### Conceptual model problem

`conceptual-framework`

### Method problem

`methodology-architect`

### Sampling problem

`sampling-strategy`

### Instrument problem

`instrument-design`

### Analysis problem

`analysis-planner`

or:

`statistical-method-selector`

### Result interpretation problem

`result-interpreter`

### Discussion problem

`scientific-discussion`

### Implication problem

`implication-builder`

### Novelty problem

`novelty-auditor`

### Reference problem

`reference-integrity-guard`

### Writing problem

`manuscript-writer`

### Architecture problem

`manuscript-architect`

### Journal fit problem

`journal-matcher`

---

# Revision Escalation Guard

Do not route to `manuscript-writer` when the problem is actually scientific.

Writing should not mask methodological weakness.

---

# Reviewer Response Handoff

After simulated comments are stabilized:

```text
reviewer-simulator
      ↓
reviewer-response
```

`reviewer-response` should distinguish simulated comments from actual journal comments.

---

# Actual Reviewer Comments

If the user provides real reviewer comments, do not present them as simulated.

Route to `reviewer-response`.

---

# Mixed Actual and Simulated Review

If both exist, clearly separate:

- `ACTUAL_REVIEWER_COMMENT`
- `SIMULATED_ADDITIONAL_RISK`

---

# Journal-Specific Simulation

When journal context is verified, reviewer simulation may use:

- journal scope;
- article type;
- reporting guideline;
- audience;
- formatting limits;
- explicit methodological expectations.

Do not invent hidden editorial preferences.

---

# Recent Journal Article Signal

Recent target-journal papers may inform:

- typical study designs;
- terminology;
- level of detail;
- current topics.

They must not be used to fabricate reviewer demands.

---

# Citation Padding Guard

Never simulate:

> Reviewer requests three more citations from this journal.

unless those citations are scientifically needed.

---

# Reviewer Bias Guard

Do not intentionally simulate:

- nationality bias;
- institutional prestige bias;
- gender bias;
- geographic bias;
- language bias.

---

# Geographic Context Review

A single-country study should be assessed on scientific value, not penalized automatically.

---

# Language Review Boundary

Reviewer simulation may identify unclear scientific language.

Detailed rewriting belongs to `manuscript-writer`.

---

# Grammar vs Science

Distinguish:

```text
grammar issue
≠
scientific issue
```

---

# Constructive Tone

Reviewer reports should be rigorous but professional.

Avoid:

- ridicule;
- sarcasm;
- personal attacks;
- dismissive language.

---

# Strengths Section

Every full review should include genuine strengths when supported.

---

# Major Concerns Section

Prioritize scientifically consequential issues.

---

# Minor Concerns Section

Keep minor issues proportionate.

---

# Questions for Authors

Use questions when clarification is genuinely needed.

---

# Required Revision vs Suggestion

Classify requests as:

- `REQUIRED_FOR_VALIDITY`
- `REQUIRED_FOR_CLARITY`
- `STRONGLY_RECOMMENDED`
- `OPTIONAL_SUGGESTION`
- `FUTURE_WORK_ONLY`

---

# Revision Feasibility

Classify:

- `EASY`
- `MODERATE`
- `SUBSTANTIAL`
- `REQUIRES_REANALYSIS`
- `REQUIRES_NEW_DATA`
- `NOT_FEASIBLE_POST_HOC`

---

# Reanalysis Request

Only recommend reanalysis when scientifically justified.

---

# New Data Request

Flag as:

`REQUIRES_NEW_DATA`

and explain whether it is essential or merely desirable.

---

# Reviewer Burden Guard

Do not generate dozens of low-value comments.

Prefer a concise hierarchy of consequential issues.

---

# Redundancy Guard

Merge overlapping comments.

---

# Adversarial Check

Before finalizing, ask:

- Is each major concern real?
- Is it supported?
- Does it matter?
- Is the requested fix proportionate?
- Is the concern already addressed elsewhere?
- Is this reviewer asking for a different study?

---

# False-Problem Guard

Remove concerns based on:

- assumptions contradicted by the manuscript;
- generic reviewer habits;
- outdated methodological dogma;
- journal requirements not verified.

---

# Reviewer Simulation Scorecard

Optional scorecard:

| Dimension | Rating | Main Reason |
|---|---|---|
| Scientific question | | |
| Novelty | | |
| Design | | |
| Methods | | |
| Analysis | | |
| Results | | |
| Interpretation | | |
| Reporting | | |
| Reproducibility | | |
| Journal fit | | |

---

# Rating Scale

Use:

- `EXCELLENT`
- `STRONG`
- `ADEQUATE`
- `WEAK`
- `CRITICAL`
- `NOT_APPLICABLE`

---

# Full Reviewer Report Template

## Reviewer 1 — Domain / Scientific Review

### Overall Assessment
[...]

### Major Strengths
[...]

### Major Concerns
1. [...]
2. [...]

### Minor Concerns
1. [...]
2. [...]

### Questions for Authors
[...]

### Simulated Recommendation
[...]

---

## Reviewer 2 — Methods / Statistical Review

### Overall Assessment
[...]

### Major Strengths
[...]

### Major Concerns
[...]

### Minor Concerns
[...]

### Simulated Recommendation
[...]

---

## Editorial Synthesis

### Shared Strengths
[...]

### Shared Major Concerns
[...]

### Reviewer-Specific Concerns
[...]

### Journal-Fit Risk
[...]

### Revision Priority
[...]

### Simulated Editorial Outcome
[...]

---

# Compact Review Template

## Overall
[...]

## Major
1. [...]
2. [...]

## Minor
1. [...]
2. [...]

## Simulated Decision
[...]

## Next Step
[...]

---

# Section-Specific Review Template

## Section
[...]

## Scientific Strength
[...]

## Main Concern
[...]

## Required Revision
[...]

## Confidence
[...]

---

# Editorial Screening Template

```yaml
editorial_screen:
  scope_fit:
  article_type_fit:
  novelty_signal:
  methodological_credibility:
  reporting_completeness:
  readability:
  major_blocker:
  desk_rejection_risk:
  simulated_outcome:
```

---

# Re-Review Mode

After revision, compare:

```text
Previous Simulated Comment
      ↓
Author Revision
      ↓
Resolved?
      ↓
YES / PARTIAL / NO
```

---

# Re-Review Status

Use:

- `RESOLVED`
- `SUBSTANTIALLY_RESOLVED`
- `PARTIALLY_RESOLVED`
- `UNRESOLVED`
- `NEW_PROBLEM_INTRODUCED`
- `NOT_APPLICABLE`

---

# Version Tracking

Record:

```yaml
review_version:
  manuscript_version:
  simulation_round:
  date:
  target_journal:
  audit_status:
  comments_generated:
  critical_count:
  major_count:
  moderate_count:
  minor_count:
  editorial_count:
```

---

# Comment Stability

When manuscript version changes materially, prior simulated comments may no longer apply.

---

# Actual Submission Boundary

Reviewer simulation does not submit manuscripts.

---

# Publication Guarantee Guard

Never guarantee:

- acceptance;
- favorable review;
- editor interest;
- fast decision.

---

# Reviewer Identity Guard

Never invent:

- reviewer names;
- affiliations;
- emails;
- conflicts.

---

# Confidentiality Guard

Do not claim access to:

- confidential reviewer databases;
- editor correspondence;
- journal internal scoring;
- unpublished editorial criteria.

---

# Evidence Verification

If a simulated concern depends on external literature, verify the relevant evidence before presenting it as fact.

---

# Literature Search Boundary

Reviewer simulation may identify a need such as:

> The novelty claim should be rechecked against recent studies.

Then route to:

`novelty-auditor`

or:

`scopus-literature-search`

rather than inventing a competitor study.

---

# Current Journal Policy Boundary

If a concern depends on journal policy:

- verify current policy;
- cite the official source when tools permit;
- otherwise mark as `REQUIRES_VERIFICATION`.

---

# User Constraint Handling

If the researcher requests:

- harsh review;
- Q1-style review;
- reviewer 2 simulation;
- statistical reviewer;
- editor screening;

translate the request into rigorous analytical depth, not hostility.

---

# “Reviewer 2” Guard

Do not equate “Reviewer 2” with unreasonable criticism.

Use:

> adversarial but evidence-based review.

---

# Q1/Q2/Q3/Q4 Guard

Quartile does not determine scientific review rigor.

Do not fabricate different scientific standards solely from quartile.

---

# Discipline Adaptation

Adapt review dimensions to the field.

---

# Biomedical / Clinical

Emphasize:

- design;
- bias;
- confounding;
- outcomes;
- clinical relevance;
- ethics;
- reporting.

---

# Pharmacy / Pharmacology

Emphasize:

- mechanism;
- dosing;
- assay;
- formulation;
- PK/PD;
- clinical interpretation.

---

# Education / Social Science

Emphasize:

- theory;
- construct validity;
- context;
- sampling;
- causal inference;
- measurement.

---

# Engineering / Materials

Emphasize:

- experimental controls;
- reproducibility;
- characterization;
- benchmarking;
- mechanism;
- scalability.

---

# Qualitative Research

Emphasize:

- paradigm;
- reflexivity;
- analytic transparency;
- trustworthiness;
- context.

---

# Systematic Review / Meta-Analysis

Emphasize:

- search completeness;
- eligibility;
- risk of bias;
- synthesis;
- heterogeneity;
- certainty.

---

# Review Quality Criteria

A strong simulated review should be:

- specific;
- traceable;
- scientifically meaningful;
- non-redundant;
- proportionate;
- actionable;
- transparent about uncertainty.

---

# Review Completeness Check

Before finalizing, verify coverage of:

- question;
- design;
- methods;
- analysis;
- results;
- interpretation;
- novelty;
- reporting;
- references;
- journal fit.

---

# Review Calibration

Do not create criticism simply to reach a desired number of comments.

---

# Strength-to-Concern Balance

A strong manuscript may legitimately receive few major concerns.

---

# Severe-Flaw Honesty

A weak manuscript may require critical feedback even when the user hopes for submission readiness.

---

# Author Agency

Reviewer simulation should help the researcher decide which changes are scientifically justified.

---

# Response Preparation

Do not draft final rebuttal unless requested.

Route to `reviewer-response`.

---

# Reviewer-Response Preparation Record

Optionally provide:

```yaml
response_preparation:
  comment_id:
  severity:
  validity:
  response_type:
  revision_needed:
  evidence_needed:
  upstream_skill:
```

---

# Comment Validity

Classify simulated comments as:

- `VALID`
- `PARTIALLY_VALID`
- `QUESTION_FOR_CLARIFICATION`
- `OPTIONAL`
- `NOT_ACTIONABLE_WITH_CURRENT_DATA`

---

# Author Disagreement

The author does not need to accept every simulated comment.

Reviewer-response logic should distinguish justified disagreement from avoidance.

---

# No Fabricated Revision

Never propose:

- fake data;
- fake analyses;
- fake citations;
- retroactive protocol claims;
- invented ethics approval.

---

# Reviewer Simulation Passport

Use:

```yaml
reviewer_simulation:
  manuscript_version:
  simulation_type:
  target_journal:
  journal_verified:
  audit_status:
  reviewer_count:
  reviewer_lenses:
  overall_strengths:
  critical_issues:
  major_issues:
  moderate_issues:
  minor_issues:
  editorial_issues:
  simulated_editorial_outcome:
  desk_rejection_risk:
  revision_priority:
  upstream_routes:
  next_step:
```

---

# Full Output

When comprehensive simulation is requested provide:

## A. Simulation Context
[...]

## B. Manuscript Review Passport
[...]

## C. Reviewer 1
[...]

## D. Reviewer 2
[...]

## E. Reviewer 3
[...]

## F. Reviewer Agreement / Disagreement
[...]

## G. Editorial Synthesis
[...]

## H. Critical Issues
[...]

## I. Major Issues
[...]

## J. Moderate Issues
[...]

## K. Minor / Editorial Issues
[...]

## L. Revision Priority Matrix
[...]

## M. Upstream Routing
[...]

## N. Simulated Editorial Outcome
[...]

## O. Next Step
[...]

---

# Minimal Output

For a focused request provide:

## Main Strength
[...]

## Biggest Risk
[...]

## Major Revision Needed
[...]

## Simulated Decision
[...]

## Next Step
[...]

---

# User-Friendly Behavior

Prefer:

> The manuscript is scientifically coherent, but a methods-focused reviewer would likely challenge the causal wording because the design is observational. This is a major interpretive issue, not merely a writing issue.

Or:

> I would not simulate a request for additional experiments here because the current claim can be corrected by narrowing the conclusion. New experiments would improve mechanistic depth but are not required to make the present evidence internally valid.

Or:

> The journal-specific concern is only moderate because the topic fits the journal, but the article type and current author instructions should be verified before submission.

Or:

> Reviewer 1 and Reviewer 2 disagree on novelty. I would preserve that disagreement rather than force a false consensus and route the novelty claim back to `novelty-auditor`.

---

# Avoid These Behaviors

Do not:

- invent reviewer identities;
- pretend simulated comments are actual;
- invent citations;
- invent data;
- invent journal policies;
- invent acceptance rates;
- guarantee acceptance;
- generate criticism for entertainment;
- make every issue major;
- ask for unnecessary new experiments;
- recommend statistical methods disconnected from the design;
- recommend post-hoc causal claims;
- reward significance chasing;
- demand target-journal citations for strategic reasons;
- equate Q1 with harsher science;
- equate low quartile with weak science;
- hide genuine fatal flaws;
- rewrite science to satisfy imagined reviewers;
- route scientific problems to copyediting;
- repeat completed scientific audit unnecessarily;
- treat reviewer disagreement as error;
- treat null findings as failure;
- treat replication as inherently unoriginal.

---

# Stop Conditions

Do not produce a confident full simulation when:

- manuscript content is unavailable;
- current manuscript version is unclear;
- critical audit issues remain unresolved;
- target journal is claimed but not identifiable;
- requested journal-specific policy is unverified;
- the user asks for actual reviewer identities;
- the user asks for guaranteed acceptance.

Use:

- `SCIENTIFIC_AUDIT_REQUIRED`
- `MANUSCRIPT_VERSION_REQUIRED`
- `MANUSCRIPT_INCOMPLETE`
- `JOURNAL_CONTEXT_REQUIRES_VERIFICATION`
- `SECTION_ONLY_REVIEW_POSSIBLE`
- `INSUFFICIENT_CONTEXT`

when appropriate.

---

# Relationship with Manuscript Auditor

`manuscript-auditor` asks:

> Is the manuscript scientifically coherent and publication-ready?

`reviewer-simulator` asks:

> What plausible expert criticisms remain even after audit?

Simulation is adversarial stress-testing, not duplicate auditing.

---

# Relationship with Journal Matcher

`journal-matcher` identifies where the manuscript fits.

`reviewer-simulator` may use the selected journal context to test whether the manuscript is likely to withstand expert scrutiny.

---

# Relationship with Manuscript Architect

If structural problems dominate, route to:

`manuscript-architect`.

---

# Relationship with Manuscript Writer

If wording, clarity, or controlled rewriting is needed, route to:

`manuscript-writer`.

---

# Relationship with Result Interpreter

If reviewers challenge meaning, uncertainty, or causal language, route to:

`result-interpreter`.

---

# Relationship with Scientific Discussion

If reviewers challenge literature positioning, mechanisms, contradictions, or limitations, route to:

`scientific-discussion`.

---

# Relationship with Implication Builder

If reviewers challenge clinical, policy, educational, implementation, or future-research implications, route to:

`implication-builder`.

---

# Relationship with Novelty Auditor

If reviewers challenge originality, priority, or closest competitors, route to:

`novelty-auditor`.

---

# Relationship with Reviewer Response

After review comments are available:

```text
reviewer-simulator
      ↓
reviewer-response
```

`reviewer-response` should prepare point-by-point responses, revision actions, disagreement rationales, and resubmission-ready correspondence.

---

# Success Criterion

`reviewer-simulator` succeeds when a scientifically stable manuscript is subjected to rigorous, manuscript-specific, method-aware, and when appropriate journal-aware adversarial peer-review simulation that clearly distinguishes simulated review from actual journal review; when reviewer personas represent relevant expertise without fabricated identities; when each critical or major concern is traceable to manuscript evidence or an explicit missing element; when scientific question, design, methods, sampling, measurement, analysis, results, interpretation, discussion, limitations, implications, novelty, references, reporting, ethics, reproducibility, and journal fit are challenged proportionately; when statistical significance, non-significance, causal language, mechanistic claims, novelty claims, and policy or clinical implications are prevented from being overstated; when reviewer disagreement is preserved rather than forced into false consensus; when simulated editorial outcomes are labeled as simulations rather than predictions; when no acceptance probability, reviewer identity, citation, data point, journal policy, or scientific defect is fabricated; when revision requests are classified by severity, validity, feasibility, and scientific importance; when genuine scientific problems are routed back to the appropriate upstream skill instead of being disguised as writing edits; when unnecessary re-audit and unnecessary new experiments are avoided; and when the resulting review package can be handed to `reviewer-response` as a transparent, prioritized, scientifically defensible basis for revision and point-by-point response.
