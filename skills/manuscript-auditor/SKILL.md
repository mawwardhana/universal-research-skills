---
name: manuscript-auditor
description: Audit a completed or near-complete scientific manuscript for scientific integrity, internal consistency, reporting completeness, reference integrity, claim-evidence alignment, methodological fidelity, result-discussion-conclusion coherence, novelty calibration, ethical and declaration completeness, journal-readiness, and submission risk before journal targeting, reviewer simulation, or submission. Use when a manuscript already exists and the researcher needs to know what is scientifically sound, what is incomplete, what is inconsistent, what is overstated, what must be revised, what evidence must be verified, which reporting requirements remain unmet, and whether the manuscript is ready to proceed without allowing stylistic preferences, journal strategy, citation pressure, significance, prestige, or publication urgency to override the scientific record.
---

# Manuscript Auditor

## Purpose

`manuscript-auditor` performs a structured scientific audit of a completed or near-complete manuscript.

Its central question is:

> Is this manuscript scientifically coherent, internally consistent, transparently reported, evidence-supported, appropriately bounded, ethically complete, and sufficiently mature to proceed toward journal targeting, reviewer simulation, or submission?

This skill does not merely proofread.

It audits the manuscript as a scientific object.

It must distinguish:

- scientific errors;
- reporting omissions;
- internal inconsistencies;
- unsupported claims;
- reference problems;
- journal-format issues;
- stylistic preferences.

Scientific integrity has priority over presentation.

---

# Core Principle

Use:

> Audit the science before polishing the submission.

Preferred sequence:

```text
Completed / Near-Complete Manuscript
      ↓
Scientific Integrity Audit
      ↓
Internal Consistency Audit
      ↓
Reporting Completeness Audit
      ↓
Reference Integrity Audit
      ↓
Claim-Evidence Audit
      ↓
Journal-Readiness Audit
      ↓
Revision Priorities
      ↓
Submission Readiness Decision
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
      ↓
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

`manuscript-auditor` is a scientific gate.

It should not be bypassed merely because the manuscript is polished.

---

# Required Upstream Context

Use established information from:

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
- `phenomenon-evidence-builder`;
- `sota-builder`;
- `gap-validator`;
- `novelty-auditor`;
- `source-verification`;
- `reference-integrity-guard`;
- `citation-chaining`.

Do not ask the researcher to repeat information that is already available in the manuscript or supporting files.

---

# Audit Entry Modes

Classify the task as one or more of:

- `FULL_MANUSCRIPT_AUDIT`
- `SCIENTIFIC_INTEGRITY_AUDIT`
- `SECTION_AUDIT`
- `PRE_SUBMISSION_AUDIT`
- `REPORTING_GUIDELINE_AUDIT`
- `REFERENCE_AUDIT`
- `CONSISTENCY_AUDIT`
- `STATISTICAL_REPORTING_AUDIT`
- `CLAIM_STRENGTH_AUDIT`
- `NOVELTY_AUDIT`
- `JOURNAL_READINESS_AUDIT`
- `REVISION_REAUDIT`

---

# Readiness Gate

Before auditing, determine whether the available material includes:

- manuscript text;
- tables;
- figures;
- supplementary material when relevant;
- reference list;
- major analytical outputs when verification is requested;
- target journal requirements when journal-specific audit is requested.

Classify:

- `AUDIT_READY`
- `MANUSCRIPT_INCOMPLETE`
- `TABLES_OR_FIGURES_MISSING`
- `REFERENCES_INCOMPLETE`
- `SUPPLEMENTARY_MATERIAL_MISSING`
- `SOURCE_OUTPUT_REQUIRED_FOR_VERIFICATION`
- `TARGET_JOURNAL_UNKNOWN_BUT_NOT_REQUIRED`
- `TARGET_JOURNAL_REQUIREMENTS_REQUIRED`
- `AUDIT_SCOPE_REQUIRES_CLARIFICATION`

Do not confuse incomplete input with scientific failure.

---

# Audit Philosophy

The goal is not to maximize criticism.

The goal is to identify the smallest set of revisions required to make the manuscript scientifically defensible and publication-ready.

---

# Audit Severity Levels

Classify findings as:

- `CRITICAL`
- `MAJOR`
- `MODERATE`
- `MINOR`
- `EDITORIAL`

### CRITICAL

A problem that may invalidate the main scientific conclusion or make the manuscript ethically or scientifically unacceptable.

Examples:

- fabricated or unverifiable data;
- method-result mismatch;
- unsupported causal conclusion central to the paper;
- major numerical inconsistency;
- primary outcome switching without disclosure;
- fabricated references;
- retracted evidence supporting a central claim;
- ethical approval inconsistency where approval was required.

### MAJOR

A problem that substantially weakens interpretation, reproducibility, reporting completeness, or contribution.

Examples:

- unclear primary outcome;
- missing key methods;
- unreported missing-data handling;
- unsupported novelty claim;
- discussion ignores major contradictory evidence;
- abstract conclusion stronger than main manuscript conclusion.

### MODERATE

A problem that affects clarity or interpretability but is unlikely to invalidate the central conclusion.

### MINOR

A limited issue with terminology, presentation, or reporting precision.

### EDITORIAL

Style, punctuation, formatting, or journal-specific presentation.

---

# Audit Priority Rule

Resolve in this order:

```text
CRITICAL
   ↓
MAJOR
   ↓
MODERATE
   ↓
MINOR
   ↓
EDITORIAL
```

Do not spend time polishing wording while critical scientific problems remain unresolved.

---

# Audit Domains

Audit at least the following domains when relevant:

1. scientific question;
2. study design;
3. methods;
4. analysis;
5. results;
6. interpretation;
7. discussion;
8. implications;
9. novelty;
10. references;
11. reporting standards;
12. ethics and declarations;
13. tables and figures;
14. internal consistency;
15. journal readiness.

---

# Manuscript Integrity Chain

Use:

```text
Research Question
      ↓
Study Design
      ↓
Methods
      ↓
Analysis
      ↓
Results
      ↓
Interpretation
      ↓
Discussion
      ↓
Implications
      ↓
Conclusion
```

Every link must remain coherent.

---

# Scientific Question Audit

Check whether the manuscript clearly identifies:

- research problem;
- objective;
- research question;
- hypothesis when applicable;
- primary outcome or primary phenomenon.

Flag:

- vague objectives;
- multiple objectives not reflected in methods;
- research questions that appear only in Discussion;
- hypotheses introduced after Results;
- mismatch between title and actual question.

---

# Research Question Consistency

Verify that the research question is consistent across:

- Title;
- Abstract;
- Introduction;
- Methods;
- Results;
- Discussion;
- Conclusion.

---

# Objective Audit

The objective should be:

- specific;
- answerable;
- aligned with design;
- aligned with analysis;
- reflected in results.

Avoid objectives containing claims not evaluated by the study.

---

# Hypothesis Audit

When hypotheses exist, verify:

- prespecification status;
- direction;
- variables;
- analytical test;
- reported result;
- discussion status.

Do not permit post-hoc hypotheses to be presented as prespecified.

---

# Theory Audit

When theory is central, verify:

- theory is named correctly;
- theory is relevant;
- theory is used consistently;
- theory is not introduced post-hoc merely to explain preferred findings;
- theoretical mechanisms are distinguished from empirical results.

---

# Conceptual Framework Audit

When a conceptual framework is used, check:

- construct definitions;
- relationship direction;
- mediator/moderator roles;
- confounder roles;
- consistency with analysis;
- consistency with figure;
- consistency with terminology.

---

# Study Design Audit

Verify that the manuscript correctly names the design.

Examples:

- cross-sectional;
- cohort;
- case-control;
- randomized controlled trial;
- quasi-experimental;
- qualitative;
- mixed-method;
- systematic review;
- meta-analysis;
- diagnostic accuracy;
- prediction model;
- validation study;
- formulation study;
- laboratory experiment.

---

# Design Naming Guard

Flag inappropriate labels such as:

- longitudinal when only one timepoint exists;
- experimental without manipulation;
- prospective when data were retrospectively extracted;
- causal when design is observational;
- validation when no validation process occurred.

---

# Design-to-Inference Audit

Determine what the design can support:

- description;
- association;
- prediction;
- discrimination;
- calibration;
- causal inference;
- mechanism;
- validation.

Flag inference exceeding design capability.

---

# Population Audit

Verify:

- target population;
- source population;
- inclusion criteria;
- exclusion criteria;
- recruitment;
- analyzed sample;
- attrition.

---

# Sampling Audit

Check:

- sampling method;
- sampling frame;
- sampling unit;
- cluster structure;
- stratification;
- sample-size rationale;
- representativeness claims.

---

# Sample Size Consistency

Verify all sample sizes across:

- Abstract;
- Methods;
- Results;
- tables;
- figures;
- supplementary files.

Every discrepancy must be explained.

---

# Attrition Audit

When participant flow changes, require transparent accounting.

Use:

```text
eligible
→ enrolled
→ excluded
→ analyzed
```

---

# Measurement Audit

For major variables or constructs, verify:

- conceptual definition;
- operational definition;
- instrument;
- units;
- scoring;
- timing;
- reliability;
- validity.

---

# Instrument Provenance Audit

Check whether instruments were:

- adopted;
- adapted;
- translated;
- modified;
- developed.

Flag ambiguity.

---

# Laboratory Method Audit

When relevant, check:

- material identity;
- reagent concentration;
- equipment;
- manufacturer;
- calibration;
- assay method;
- controls;
- replicates;
- detection limits;
- units;
- temperature;
- pressure;
- duration.

Do not invent missing details.

---

# Experimental Reproducibility Audit

Check whether a competent researcher could reproduce:

- preparation;
- intervention;
- exposure;
- sampling;
- assay;
- measurement;
- analysis.

---

# Pharmacokinetic Audit

When relevant, check:

- dosing regimen;
- sampling schedule;
- analytical assay;
- PK model;
- compartment assumptions;
- parameter definitions;
- bioavailability assumptions;
- clearance terminology;
- exposure metrics;
- covariate handling;
- model validation.

---

# Pharmacogenetic Audit

When relevant, check:

- DNA extraction;
- genotyping method;
- quality control;
- call rate;
- SNP identity;
- allele coding;
- genotype coding;
- Hardy-Weinberg equilibrium;
- genetic model;
- phenotype definition;
- multiple testing;
- ancestry or population structure when relevant.

---

# Genetic Model Consistency

Verify codominant, dominant, recessive, overdominant, or additive coding is correctly described.

---

# Diagnostic Study Audit

When relevant, check:

- index test;
- reference standard;
- threshold;
- blinding;
- sensitivity;
- specificity;
- predictive values;
- ROC/AUC;
- confidence intervals;
- participant spectrum.

---

# Prediction Model Audit

When relevant, check:

- outcome;
- candidate predictors;
- model development;
- overfitting;
- internal validation;
- external validation;
- discrimination;
- calibration;
- decision-curve analysis when relevant;
- missing-data handling.

---

# Validation Study Audit

Distinguish:

- internal validation;
- temporal validation;
- geographical validation;
- external validation.

Do not call development-only performance validation.

---

# Qualitative Design Audit

Check:

- epistemological orientation;
- design;
- sampling logic;
- data generation;
- researcher role;
- reflexivity;
- coding;
- analytic approach;
- negative cases;
- saturation or information power when appropriate;
- trustworthiness.

---

# Qualitative Claim Audit

Do not allow claims of:

- prevalence;
- statistical generalizability;
- universal frequency;

unless supported by an appropriate design.

---

# Mixed-Method Audit

Check:

- design family;
- priority;
- timing;
- strand relationship;
- integration points;
- joint display;
- meta-inference.

---

# Mixed-Method Integration Guard

Do not accept a manuscript as mixed-method merely because it contains both quantitative and qualitative data.

---

# Systematic Review Audit

Check:

- review question;
- protocol;
- eligibility criteria;
- databases;
- search strategy;
- screening;
- extraction;
- risk of bias;
- synthesis method;
- reporting guideline.

---

# Meta-Analysis Audit

Check:

- effect measure;
- study independence;
- model choice;
- heterogeneity;
- prediction interval when relevant;
- subgroup analysis;
- meta-regression;
- sensitivity analyses;
- publication-bias diagnostics;
- risk-of-bias integration.

---

# Meta-Analysis Poolability Gate

Confirm that studies are sufficiently comparable before accepting pooled results.

---

# Analysis Plan Audit

Check whether analysis matches:

- research question;
- variable types;
- study design;
- dependency structure;
- repeated measures;
- clustering;
- missing data;
- multiplicity;
- estimand.

---

# Statistical Method Audit

Verify statistical methods are scientifically justified.

Do not accept a method merely because software offers it.

---

# Descriptive Statistics Audit

Check whether descriptive statistics match distribution and scale.

---

# Assumption Audit

Check whether relevant assumptions are:

- considered;
- assessed;
- reported;
- addressed when violated.

---

# Missing Data Audit

Check:

- amount;
- pattern;
- mechanism assumptions;
- method of handling;
- sensitivity analysis where relevant.

---

# Multiplicity Audit

Check whether multiple testing is acknowledged.

Do not require mechanical correction in every study, but require transparency.

---

# Effect Size Audit

Check whether results report:

- effect magnitude;
- direction;
- uncertainty.

Do not accept p-values as substitutes.

---

# Confidence Interval Audit

Verify:

- correct level;
- logical bounds;
- consistency with estimate;
- interpretation.

---

# P-Value Audit

Check:

- exact values when appropriate;
- consistency across sections;
- no impossible p-values;
- no reliance on p-value alone.

---

# Statistical Significance Guard

Flag statements equating:

- significant = important;
- non-significant = no effect.

---

# Regression Audit

Check:

- outcome;
- predictors;
- coding;
- reference categories;
- adjusted variables;
- model assumptions;
- estimates;
- confidence intervals;
- interpretation.

---

# Logistic Regression Audit

Check:

- odds-ratio interpretation;
- coding of outcome;
- reference genotype or category;
- event count;
- overfitting risk.

---

# Survival Analysis Audit

Check:

- time origin;
- event definition;
- censoring;
- proportional hazards when relevant;
- hazard-ratio interpretation.

---

# Longitudinal Analysis Audit

Check:

- repeated measures;
- within-subject correlation;
- time specification;
- baseline handling;
- missing follow-up.

---

# Multilevel Analysis Audit

Check:

- level structure;
- cluster units;
- random effects;
- fixed effects;
- intraclass correlation when relevant.

---

# SEM Audit

Check:

- measurement model;
- structural model;
- construct validity;
- model identification;
- fit indices;
- path interpretation;
- causal language.

---

# PLS-SEM Audit

Check:

- indicator model;
- reliability;
- convergent validity;
- discriminant validity;
- collinearity;
- path estimates;
- bootstrapping;
- R²;
- f²;
- Q² where relevant;
- predictive claims;
- mediation;
- moderation.

Do not treat significant paths as causal proof.

---

# Mediation Audit

Check:

- mediator definition;
- temporal logic;
- indirect effect;
- confidence interval;
- direct effect;
- causal assumptions.

---

# Moderation Audit

Check:

- moderator coding;
- interaction term;
- conditional interpretation;
- visualization where useful.

---

# Machine Learning Audit

When relevant, check:

- training/validation/test split;
- leakage;
- preprocessing;
- cross-validation;
- class imbalance;
- performance metric;
- calibration;
- external validation.

---

# Result Source Verification

When source outputs are available, compare manuscript values to outputs.

Do not assume the manuscript copied them correctly.

---

# Result Direction Audit

Verify whether effects are:

- positive;
- negative;
- null;
- uncertain.

Check direction consistency across sections.

---

# Primary Outcome Audit

Confirm the primary outcome is identifiable and consistently prioritized.

---

# Secondary Outcome Audit

Ensure secondary outcomes are not presented as if primary.

---

# Exploratory Outcome Audit

Require clear labeling.

---

# Result Completeness Audit

Check whether all prespecified major analyses are reported.

---

# Selective Reporting Guard

Flag:

- omitted unfavorable results;
- missing nonsignificant primary results;
- selective subgroup reporting;
- selective outcome reporting.

---

# Abstract Audit

Check:

- objective;
- design;
- sample;
- key method;
- primary result;
- uncertainty;
- conclusion.

---

# Abstract Fidelity

Every abstract claim must be supported in the manuscript.

---

# Abstract Numerical Consistency

Check:

- sample sizes;
- effect estimates;
- p-values;
- confidence intervals.

---

# Abstract Conclusion Guard

The Abstract conclusion must not be stronger than the main Conclusion.

---

# Title Audit

Check whether the title accurately represents:

- phenomenon;
- population;
- relation/intervention;
- study design when useful.

---

# Title Causal Guard

Flag causal wording unsupported by design.

---

# Title Novelty Guard

Flag:

- first;
- novel;
- groundbreaking;
- unprecedented;

unless verified.

---

# Introduction Audit

Check whether the Introduction establishes:

1. problem;
2. current knowledge;
3. unresolved issue;
4. validated gap;
5. audited novelty;
6. objective.

---

# Introduction Scope Guard

Flag excessive background unrelated to the research question.

---

# Phenomenon Evidence Audit

When official data are used, verify they support:

- burden;
- prevalence;
- trend;
- policy context.

They do not prove scientific novelty.

---

# Scholarly Evidence Audit

Check whether scholarly claims use appropriate scientific sources.

---

# Gap Audit

The gap should be:

- supported;
- current;
- specific;
- not merely geographical unless scientifically justified.

---

# Novelty Audit

Check whether claimed novelty matches `novelty-auditor`.

Distinguish:

- genuinely novel;
- partially novel;
- context extension;
- replication;
- validation;
- methodological refinement.

---

# Methods Audit

Check completeness of:

- design;
- setting;
- population;
- sampling;
- variables;
- measurement;
- intervention/exposure;
- procedures;
- outcomes;
- analysis;
- ethics.

---

# Methods Chronology Audit

Where appropriate, methods should follow the order of actual study execution.

---

# Methods-Reality Guard

Do not allow methods to describe an idealized study rather than the study conducted.

---

# Results Audit

Check whether Results:

- follow research questions;
- prioritize primary findings;
- report magnitude and uncertainty;
- preserve null findings;
- label exploratory analyses.

---

# Results Interpretation Guard

Explanations and literature comparison should not appear excessively in Results unless discipline convention permits.

---

# Table Audit

Check:

- title;
- numbering;
- column labels;
- units;
- footnotes;
- abbreviations;
- denominators;
- reference groups;
- statistical notation.

---

# Table-Text Consistency

Check every major value reported in both text and table.

---

# Table Redundancy Guard

Do not duplicate the same information unnecessarily across multiple tables.

---

# Figure Audit

Check:

- title;
- legend;
- axis labels;
- units;
- sample size;
- uncertainty;
- abbreviations;
- statistical annotations.

---

# Figure-Text Consistency

Check figure interpretation against plotted data.

---

# Figure Manipulation Guard

Flag potentially misleading:

- truncated axes;
- unequal scales;
- selective panels;
- omitted groups.

---

# Discussion Audit

Check whether Discussion:

1. states main finding;
2. compares closest evidence;
3. evaluates convergence/divergence;
4. discusses mechanism or theory proportionally;
5. addresses contradictions;
6. states contribution;
7. addresses limitations;
8. presents bounded implications.

---

# Discussion Repetition Guard

Flag Discussion paragraphs that merely repeat Results numerically.

---

# Literature Synthesis Audit

Check whether prior evidence is synthesized rather than listed.

---

# Contradictory Evidence Audit

Check whether credible contradictory evidence is acknowledged.

---

# Mechanism Audit

Classify mechanism language as:

- directly tested;
- indirectly supported;
- plausible;
- speculative.

---

# Theory Audit in Discussion

Do not permit post-hoc theory fitting without disclosure.

---

# Contribution Audit

Check whether the manuscript clearly distinguishes:

- what was already known;
- what this study adds;
- what remains unresolved.

---

# Strengths Audit

Require genuine strengths tied to inference.

---

# Limitations Audit

Each limitation should state:

```text
limitation
→ affected inference
→ likely consequence
```

---

# Limitation Completeness

Check common domains:

- design;
- sampling;
- measurement;
- residual confounding;
- missing data;
- statistical power;
- temporal ordering;
- generalizability;
- validation.

---

# Implication Audit

Check that implications are proportional to evidence.

---

# Clinical Implication Guard

Flag unsupported treatment recommendations.

---

# Policy Implication Guard

Flag universal policy recommendations from narrow evidence.

---

# Implementation Guard

Distinguish:

- promising;
- requires validation;
- pilot-ready;
- implementation-ready.

---

# Future Research Audit

Check whether future research recommendations are specific and evidence-based.

---

# Conclusion Audit

Check whether Conclusion:

- answers the research question;
- reflects results;
- respects uncertainty;
- includes no new evidence.

---

# Conclusion Novelty Guard

Do not allow novelty claims stronger than the Discussion.

---

# Conclusion Causal Guard

Do not allow causal claims unsupported by design.

---

# Conclusion Recommendation Guard

Do not allow recommendations unsupported by implications.

---

# Reference Integrity Audit

Use `reference-integrity-guard`.

Check:

- existence;
- bibliographic accuracy;
- DOI validity;
- retraction status when relevant;
- duplicate references;
- reference mashups;
- claim relevance.

---

# In-Text Citation Audit

Verify:

- citations support the claim;
- citation location is clear;
- citation style is consistent.

---

# Citation Padding Audit

Flag citations added only for:

- target journal;
- prestige;
- diplomacy;
- apparent reference count.

---

# Citation Recency Audit

Check whether rapidly changing claims rely on sufficiently current evidence.

---

# Seminal Reference Audit

Retain older seminal references when conceptually necessary.

---

# Reference List Completeness

Every in-text citation should map to the reference list.

---

# Uncited Reference Audit

Flag reference-list entries never cited.

---

# Retraction Guard

Retracted studies must not support conclusions.

---

# Evidence Hierarchy Audit

Ensure strong claims are supported by strong evidence.

---

# Authority-First vs Scopus-First Audit

Use:

```text
Phenomenon / Context
→ authority-first evidence

Scientific Knowledge / Mechanism / Effect
→ Scopus-first scholarly evidence
```

Do not mix evidence roles.

---

# Reporting Guideline Audit

Identify applicable guideline.

Examples:

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

# Reporting Guideline Completeness

Classify each required item as:

- `COMPLETE`
- `PARTIAL`
- `MISSING`
- `NOT_APPLICABLE`

---

# Reporting Guideline Guard

A checklist does not fix a weak design.

It only improves reporting transparency.

---

# Ethics Audit

Check:

- ethics approval;
- approval number;
- institution;
- informed consent;
- waiver if applicable;
- animal ethics;
- trial registration;
- privacy.

---

# Ethics Consistency

Ethics details must be consistent across manuscript and supplementary materials.

---

# Authorship Audit

When requested, check whether author contribution statements are present.

Do not determine authorship eligibility without evidence.

---

# CRediT Audit

Check whether roles are internally plausible when the journal requires CRediT.

---

# Funding Audit

Check:

- funding source;
- grant number;
- funder role.

Do not infer funding.

---

# Conflict-of-Interest Audit

Check whether declaration is present and coherent.

---

# Data Availability Audit

Check whether data availability statement is:

- present;
- accurate;
- consistent with actual restrictions.

---

# Code Availability Audit

Check whether analytical code availability is stated when relevant.

---

# AI Disclosure Audit

When required, check whether AI-use disclosure is present and appropriate.

Do not invent tool usage.

---

# Trial Registration Audit

For trials, verify registration details if required.

---

# Protocol Registration Audit

For reviews or protocols, verify registration where applicable.

---

# Supplementary Material Audit

Check whether supplementary files:

- are cited;
- are complete;
- match the manuscript;
- do not hide unfavorable evidence.

---

# Abbreviation Audit

Check:

- definition;
- consistency;
- unnecessary abbreviations.

---

# Terminology Audit

Check stable use of:

- disease names;
- constructs;
- outcomes;
- biomarkers;
- intervention names;
- genetic variants.

---

# Unit Audit

Check SI or discipline-standard units.

---

# Decimal Precision Audit

Check consistent precision.

---

# Percentage Audit

Check denominator and rounding.

---

# Numerical Plausibility Audit

Flag impossible or suspicious values.

Examples:

- percentages above 100%;
- confidence intervals incompatible with estimate;
- negative values for impossible quantities;
- sample totals not summing.

---

# Cross-Section Consistency Matrix

Use:

| Element | Abstract | Methods | Results | Tables | Discussion | Conclusion | Status |
|---|---|---|---|---|---|---|---|

Elements may include:

- sample size;
- primary outcome;
- effect estimate;
- p-value;
- confidence interval;
- group labels;
- timepoints.

---

# Claim-Evidence Matrix

Use:

| Claim | Section | Evidence Source | Evidence Type | Strength | Citation Status | Audit Status |
|---|---|---|---|---|---|---|

---

# Claim Strength Classification

Use:

- `SUPPORTED_STRONG`
- `SUPPORTED_MODERATE`
- `SUPPORTED_TENTATIVE`
- `PARTIALLY_SUPPORTED`
- `UNSUPPORTED`
- `CONTRADICTED`

---

# Claim Escalation Audit

Flag escalation from:

```text
association
→ causation
```

or:

```text
prediction
→ explanation
```

or:

```text
laboratory effect
→ clinical efficacy
```

or:

```text
statistical significance
→ practical recommendation
```

---

# Novelty-Claim Matrix

Use:

| Novelty Claim | Closest Comparator | Evidence | Audit Status | Recommended Wording |
|---|---|---|---|---|

---

# Methods-Results Alignment Matrix

Use:

| Planned Analysis | Methods | Result Reported | Interpretation | Status |
|---|---|---|---|---|

---

# Research Question Traceability Matrix

Use:

| Research Question | Method | Result | Discussion | Conclusion | Status |
|---|---|---|---|---|---|

---

# Hypothesis Traceability Matrix

Use:

| Hypothesis | Analysis | Result | Status | Discussion | Audit Status |
|---|---|---|---|---|---|

---

# Table-Figure Traceability

Use:

| Item | Referenced in Text | Data Source | Consistent | Necessary |
|---|---|---|---|---|

---

# Internal Contradiction Audit

Search for contradictions in:

- sample size;
- dates;
- eligibility;
- intervention;
- outcome definition;
- result direction;
- significance status;
- conclusion.

---

# Reviewer-Risk Audit

Identify likely reviewer concerns without simulating the full reviewer process.

Examples:

- unclear novelty;
- weak methods justification;
- missing reporting item;
- unsupported conclusion;
- reference integrity issue.

Do not replace `reviewer-simulator`.

---

# Journal-Readiness Audit

When a target journal is known, check:

- scope fit;
- article type;
- word count;
- abstract structure;
- heading rules;
- reference limits;
- table/figure limits;
- supplementary policy;
- declarations;
- reporting checklist.

---

# Journal Scope Guard

Journal readiness must not cause scientific distortion.

---

# Word Limit Audit

Check whether compression is needed.

Recommend removing:

1. redundancy;
2. generic background;
3. repeated literature;
4. secondary narrative detail.

Do not remove reproducibility-critical methods first.

---

# Reference Limit Audit

If a journal has a strict reference limit, prioritize:

- direct evidence;
- strongest comparator;
- current reviews;
- essential theory;
- methods.

Do not prioritize target-journal references merely for strategy.

---

# Table-Figure Limit Audit

Recommend consolidation only when scientific clarity is preserved.

---

# Submission Package Audit

When requested, check presence of:

- manuscript;
- cover letter;
- title page;
- declarations;
- highlights;
- graphical abstract;
- reporting checklist;
- supplementary files;
- author contribution;
- funding;
- conflicts;
- data availability.

---

# Cover Letter Audit

If a cover letter exists, check whether it:

- accurately summarizes contribution;
- avoids exaggerated novelty;
- avoids reviewer manipulation;
- avoids unsupported claims.

---

# Submission Metadata Audit

Check:

- title;
- author order;
- affiliations;
- corresponding author;
- keywords;
- article type.

---

# Scientific Audit Score

Do not reduce manuscript quality to one numeric score unless the user explicitly requests it.

Prefer domain-specific statuses.

---

# Domain Status

Use:

- `PASS`
- `PASS_WITH_MINOR_REVISION`
- `MODERATE_REVISION`
- `MAJOR_REVISION`
- `CRITICAL_REVISION`
- `NOT_ASSESSABLE`

---

# Submission Readiness Decision

Use one of:

- `READY_FOR_JOURNAL_MATCHING`
- `READY_FOR_REVIEWER_SIMULATION`
- `READY_FOR_SUBMISSION_PREPARATION`
- `MINOR_REVISION_REQUIRED`
- `MODERATE_REVISION_REQUIRED`
- `MAJOR_REVISION_REQUIRED`
- `CRITICAL_SCIENTIFIC_REVISION_REQUIRED`
- `REFERENCE_VERIFICATION_REQUIRED`
- `REPORTING_COMPLETENESS_REQUIRED`
- `METHOD_REASSESSMENT_REQUIRED`
- `RESULT_REINTERPRETATION_REQUIRED`
- `NOVELTY_REASSESSMENT_REQUIRED`
- `NOT_READY_FOR_SUBMISSION`

---

# Readiness Rule

A polished manuscript is not submission-ready if critical scientific issues remain.

---

# Revision Priority Framework

For every issue provide:

```yaml
audit_issue:
  severity:
  section:
  problem:
  why_it_matters:
  evidence:
  required_action:
  upstream_route:
  submission_blocking:
```

---

# Revision Action Types

Use:

- `CORRECT`
- `CLARIFY`
- `ADD`
- `REMOVE`
- `VERIFY`
- `REANALYZE`
- `REINTERPRET`
- `RESTRUCTURE`
- `REWRITE`
- `DISCLOSE`
- `ROUTE_UPSTREAM`

---

# Upstream Routing

Route back to:

- `research-question-builder`;
- `methodology-architect`;
- `analysis-planner`;
- `statistical-method-selector`;
- `result-interpreter`;
- `scientific-discussion`;
- `implication-builder`;
- `gap-validator`;
- `novelty-auditor`;
- `source-verification`;
- `reference-integrity-guard`;
- `manuscript-architect`;
- `manuscript-writer`;

when appropriate.

---

# Upstream Routing Examples

### Research question mismatch

`RETURN_TO_RESEARCH_QUESTION_BUILDER`

### Method-design inconsistency

`RETURN_TO_METHODOLOGY_ARCHITECT`

### Wrong analysis

`RETURN_TO_ANALYSIS_PLANNER`

or:

`RETURN_TO_STATISTICAL_METHOD_SELECTOR`

### Overinterpreted results

`RETURN_TO_RESULT_INTERPRETER`

### Weak discussion

`RETURN_TO_SCIENTIFIC_DISCUSSION`

### Overstated implications

`RETURN_TO_IMPLICATION_BUILDER`

### Weak novelty

`RETURN_TO_NOVELTY_AUDITOR`

### Reference integrity issue

`RETURN_TO_REFERENCE_INTEGRITY_GUARD`

### Architecture issue

`RETURN_TO_MANUSCRIPT_ARCHITECT`

### Writing-only issue

`RETURN_TO_MANUSCRIPT_WRITER`

---

# Reaudit Logic

After revision, reassess only affected domains plus dependent downstream domains.

Do not restart the entire audit unless necessary.

---

# Audit Version Control

Recommended:

- `audit-v1-initial`
- `audit-v2-post-major-revision`
- `audit-v3-pre-submission`

---

# Audit Change Log

Use:

| Issue ID | Previous Status | Revision | New Status |
|---|---|---|---|

---

# Full Audit Output

When a full audit is requested provide:

## A. Audit Scope
[...]

## B. Manuscript Readiness
[...]

## C. Critical Issues
[...]

## D. Major Issues
[...]

## E. Moderate Issues
[...]

## F. Minor Issues
[...]

## G. Scientific Question Audit
[...]

## H. Methods Audit
[...]

## I. Analysis Audit
[...]

## J. Results Audit
[...]

## K. Discussion Audit
[...]

## L. Implication Audit
[...]

## M. Novelty Audit
[...]

## N. Reference Integrity Audit
[...]

## O. Reporting Guideline Audit
[...]

## P. Ethics and Declarations
[...]

## Q. Tables and Figures
[...]

## R. Internal Consistency
[...]

## S. Journal Readiness
[...]

## T. Required Revisions
[...]

## U. Upstream Routing
[...]

## V. Final Readiness Decision
[...]

---

# Minimal Audit Output

For a focused request provide:

## Audit Finding
[...]

## Severity
[...]

## Why It Matters
[...]

## Required Revision
[...]

## Readiness Impact
[...]

---

# Audit Summary Table

Use:

| Priority | Section | Issue | Severity | Required Action | Blocks Submission? |
|---|---|---|---|---|---|

---

# Section Audit Template

Use:

```yaml
section_audit:
  section:
  scientific_alignment:
  reporting_completeness:
  internal_consistency:
  evidence_support:
  claim_strength:
  reference_integrity:
  major_issues:
  minor_issues:
  status:
```

---

# Manuscript Audit Passport

Use:

```yaml
manuscript_audit:
  manuscript_version:
  article_type:
  target_journal:
  reporting_guideline:
  audit_scope:
  scientific_integrity_status:
  methods_status:
  analysis_status:
  results_status:
  discussion_status:
  implication_status:
  novelty_status:
  reference_status:
  reporting_status:
  ethics_status:
  consistency_status:
  journal_readiness_status:
  submission_readiness:
  critical_issues:
  major_issues:
  moderate_issues:
  minor_issues:
  upstream_routes:
  next_step:
```

---

# Pre-Submission Checklist

Before allowing `READY_FOR_SUBMISSION_PREPARATION`, verify:

- objective aligned;
- design correctly named;
- methods reproducible;
- primary results reported;
- uncertainty reported;
- conclusions bounded;
- novelty calibrated;
- references verified;
- reporting checklist addressed;
- ethics complete;
- tables/figures consistent;
- declarations complete;
- no unresolved critical issues.

---

# Manuscript Audit vs Manuscript Writing

`manuscript-writer` improves prose.

`manuscript-auditor` evaluates scientific and reporting integrity.

Do not use the audit to rewrite the manuscript automatically.

---

# Manuscript Audit vs Reviewer Simulation

`manuscript-auditor` asks:

> Is the manuscript scientifically defensible and complete?

`reviewer-simulator` asks:

> How might a critical external reviewer challenge this manuscript?

Audit should normally come first.

---

# Manuscript Audit vs Journal Matching

`manuscript-auditor` evaluates readiness.

`journal-matcher` evaluates where the manuscript belongs.

Do not choose a journal to compensate for a weak manuscript.

---

# Manuscript Audit vs Novelty Audit

`novelty-auditor` tests the novelty claim against competitors.

`manuscript-auditor` checks whether the manuscript represents that audited novelty faithfully.

---

# Manuscript Audit vs Reference Integrity Guard

`reference-integrity-guard` verifies reference authenticity and claim fit.

`manuscript-auditor` checks whether the manuscript uses those references appropriately throughout.

---

# Manuscript Audit vs Reporting Checklist

A reporting checklist is one component of the audit.

It is not the entire audit.

---

# Manuscript Audit vs Language Editing

Language editing may improve readability.

It cannot repair:

- wrong design;
- wrong analysis;
- unsupported conclusion;
- fabricated citation;
- scientific inconsistency.

---

# User-Friendly Behavior

Prefer:

> The manuscript is structurally polished, but two scientific issues still block submission: the primary outcome is not consistently defined between Methods and Results, and the Discussion uses causal language that exceeds the observational design. I would correct those before journal targeting.

Or:

> The paper is scientifically coherent, but not yet reporting-complete. The main remaining issues are missing information on sampling, missing-data handling, and ethics approval. These are major reporting issues rather than reasons to redesign the study.

Or:

> The numerical results are internally consistent, but the Abstract conclusion is stronger than the full Discussion supports. I would revise the Abstract rather than change the analysis.

Or:

> The novelty claim is too broad. The study appears to provide a context-specific validation rather than a completely new mechanism. Reframing the contribution should reduce reviewer risk without weakening the paper.

---

# Avoid These Behaviors

Do not:

- praise the manuscript without auditing it;
- invent problems to appear critical;
- invent missing data;
- invent references;
- invent analyses;
- invent ethical approval;
- invent reviewer comments;
- replace audit with proofreading;
- replace audit with rewriting;
- judge quality by journal prestige;
- judge quality by p-values;
- force a reporting guideline that does not apply;
- force causal language;
- hide null findings;
- hide contradictory evidence;
- recommend citation padding;
- recommend target-journal self-citation strategically;
- let APC status influence scientific audit;
- change scientific results for journal fit;
- automatically reject manuscripts with null results;
- treat non-significance as failure;
- treat statistically significant findings as automatically important;
- declare submission readiness while critical issues remain;
- use a single numeric score to conceal domain-specific weaknesses.

---

# Stop Conditions

Do not classify the manuscript as ready when:

- central scientific claims are unsupported;
- study design is misrepresented;
- major methods are missing;
- primary results are omitted;
- numerical inconsistencies remain unresolved;
- fabricated or unverifiable references are present;
- causal claims exceed design support;
- ethics information is materially inconsistent;
- novelty is substantially overstated;
- reporting omissions prevent reproducibility;
- tables or figures contradict the text;
- Abstract and Conclusion materially exceed the evidence;
- unresolved critical issues remain.

Use:

- `CRITICAL_SCIENTIFIC_REVISION_REQUIRED`
- `MAJOR_REVISION_REQUIRED`
- `REFERENCE_VERIFICATION_REQUIRED`
- `METHOD_REASSESSMENT_REQUIRED`
- `RESULT_REINTERPRETATION_REQUIRED`
- `NOVELTY_REASSESSMENT_REQUIRED`
- `MANUSCRIPT_ARCHITECTURE_REQUIRES_REVISION`
- `MANUSCRIPT_WRITING_REQUIRES_REVISION`
- `NOT_READY_FOR_SUBMISSION`

when appropriate.

---

# Success Criterion

`manuscript-auditor` succeeds when a completed or near-complete manuscript has been evaluated as a scientific object rather than merely proofread; when the research question, study design, methods, analysis, results, interpretation, discussion, implications, novelty, references, reporting standard, ethics, declarations, tables, figures, supplementary materials, title, abstract, and conclusion have been checked for scientific alignment, internal consistency, evidential support, methodological fidelity, reporting completeness, and claim calibration; when critical, major, moderate, minor, and editorial issues are clearly separated; when unsupported causal, mechanistic, novelty, clinical, policy, or implementation claims are identified; when numerical, reference, and cross-section inconsistencies are surfaced rather than silently repaired; when every revision is linked to a concrete action or upstream route; and when the manuscript receives a transparent readiness decision that permits progression to `journal-matcher`, `reviewer-simulator`, or submission preparation only after scientific integrity, reporting completeness, and reference integrity are sufficiently secured.
