---
name: reviewer-response
description: Prepare rigorous, evidence-grounded, point-by-point responses to actual or simulated peer-review comments after reviewer feedback exists. Use to classify reviewer and editor comments, determine whether each request is scientifically valid, identify required manuscript revisions, draft respectful rebuttals, justify disagreement, coordinate reanalysis or upstream scientific correction, track manuscript-version changes, prepare response matrices and revision letters, distinguish actual reviewer comments from simulated comments, and support resubmission without fabricating data, analyses, citations, approvals, journal policies, completed revisions, or claims of compliance that have not actually occurred. Reviewer response must preserve the scientific record, address criticism rather than evade it, and route genuine scientific problems back to the appropriate upstream skill before final response language is drafted.
---

# Reviewer Response

## Purpose

`reviewer-response` converts reviewer or editor feedback into a scientifically defensible revision-and-response workflow.

Its central question is:

> What is the most accurate, evidence-based, respectful, and scientifically defensible response to each reviewer or editor comment, and what manuscript action is actually required before that response can be finalized?

The skill supports both:

- actual journal peer-review comments;
- simulated pre-submission reviewer comments.

These must never be confused.

---

# Core Principle

Use:

> Respond to the science first. Write the rebuttal second.

A polished response cannot compensate for an unresolved scientific problem.

---

# Position in the Framework

Preferred publication architecture:

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

For actual journal review:

```text
Submitted Manuscript
      ↓
Editor / Reviewer Comments
      ↓
reviewer-response
      ↓
Required Upstream Corrections
      ↓
Revised Manuscript
      ↓
Response Letter
      ↓
Resubmission
```

---

# Actual vs Simulated Feedback

Always distinguish:

```text
ACTUAL JOURNAL REVIEW
≠
SIMULATED REVIEW
```

Use explicit labels:

- `ACTUAL_EDITOR_COMMENT`
- `ACTUAL_REVIEWER_COMMENT`
- `SIMULATED_REVIEWER_COMMENT`
- `AUTHOR_INTERNAL_COMMENT`

Do not present simulated comments as if they came from a journal.

---

# Entry Modes

Classify the request as one or more of:

- `ACTUAL_REVIEW_RESPONSE`
- `SIMULATED_REVIEW_RESPONSE`
- `EDITOR_COMMENT_RESPONSE`
- `POINT_BY_POINT_RESPONSE`
- `MAJOR_REVISION_RESPONSE`
- `MINOR_REVISION_RESPONSE`
- `REJECT_AND_RESUBMIT_RESPONSE`
- `REVISION_LETTER`
- `RESPONSE_MATRIX`
- `COMMENT_CLASSIFICATION`
- `COMMENT_VALIDITY_ASSESSMENT`
- `SCIENTIFIC_DISAGREEMENT_RESPONSE`
- `METHODS_RESPONSE`
- `STATISTICAL_RESPONSE`
- `NOVELTY_RESPONSE`
- `REFERENCE_RESPONSE`
- `REPORTING_GUIDELINE_RESPONSE`
- `ETHICS_TRANSPARENCY_RESPONSE`
- `LANGUAGE_STYLE_RESPONSE`
- `POST_REVISION_REVIEW`
- `SECOND_ROUND_RESPONSE`
- `EDITORIAL_APPEAL_ASSESSMENT`
- `RESUBMISSION_PREPARATION`

---

# Required Inputs

Use available materials such as:

- editor decision letter;
- reviewer reports;
- annotated manuscript;
- tracked-changes manuscript;
- clean revised manuscript;
- supplementary files;
- statistical outputs;
- analysis scripts;
- reporting checklists;
- journal author instructions;
- prior audit results;
- prior reviewer simulation;
- prior response letter;
- target journal context.

Do not ask the researcher to repeat information already available.

---

# Comment Source Passport

Before drafting responses, record:

```yaml
review_source:
  review_type:
  journal:
  manuscript_id:
  manuscript_title:
  decision:
  review_round:
  decision_date:
  manuscript_version_reviewed:
  response_deadline:
  editor_comments_present:
  reviewer_count:
  supplementary_requests:
  journal_policy_verified:
```

Do not fabricate missing metadata.

---

# Decision Types

Possible actual journal decisions may include:

- `MINOR_REVISION`
- `MAJOR_REVISION`
- `REVISE_AND_RESUBMIT`
- `REJECT_AND_RESUBMIT`
- `REJECT`
- `CONDITIONAL_ACCEPTANCE`
- `EDITORIAL_REVISION`
- `UNKNOWN`

Preserve the journal's actual wording when available.

---

# Comment Extraction

Extract comments without silently rewriting their scientific meaning.

For each comment record:

```yaml
review_comment:
  comment_id:
  source:
  reviewer:
  original_comment:
  comment_type:
  section:
  severity:
  scientific_validity:
  actionability:
  revision_required:
  upstream_route:
  evidence_needed:
  response_status:
```

---

# Comment ID System

Use stable IDs such as:

- `E1`, `E2` for editor comments;
- `R1.1`, `R1.2` for Reviewer 1;
- `R2.1`, `R2.2` for Reviewer 2;
- `S1.1` for simulated Reviewer 1.

Do not renumber comments midway unless necessary.

---

# Preserve Original Comment

When preparing a response letter, preserve the reviewer comment faithfully.

Do not create a stronger, weaker, or easier version of the comment.

---

# Comment Segmentation

A long reviewer paragraph may contain multiple requests.

Split only when doing so improves traceability.

Example:

```text
R1.3a — clarify sampling
R1.3b — justify sample size
R1.3c — discuss selection bias
```

---

# Comment Classification

Possible comment types include:

- `SCIENTIFIC_VALIDITY`
- `RESEARCH_QUESTION`
- `THEORY`
- `CONCEPTUAL_FRAMEWORK`
- `METHOD`
- `SAMPLING`
- `MEASUREMENT`
- `STATISTICS`
- `QUALITATIVE_ANALYSIS`
- `MIXED_METHODS`
- `RESULTS`
- `INTERPRETATION`
- `DISCUSSION`
- `LIMITATION`
- `IMPLICATION`
- `NOVELTY`
- `REFERENCE`
- `REPORTING`
- `ETHICS`
- `TRANSPARENCY`
- `TABLE`
- `FIGURE`
- `SUPPLEMENT`
- `LANGUAGE`
- `STYLE`
- `FORMAT`
- `JOURNAL_FIT`
- `OTHER`

---

# Severity Classification

Use:

- `CRITICAL`
- `MAJOR`
- `MODERATE`
- `MINOR`
- `EDITORIAL`

Severity refers to scientific consequence, not reviewer tone.

---

# Scientific Validity Classification

Classify each comment as:

- `VALID`
- `PARTIALLY_VALID`
- `VALID_BUT_ALREADY_ADDRESSED`
- `VALID_REQUIRES_REANALYSIS`
- `VALID_REQUIRES_NEW_DATA`
- `QUESTION_FOR_CLARIFICATION`
- `PREFERENCE_NOT_REQUIREMENT`
- `SCIENTIFICALLY_DEBATABLE`
- `NOT_SUPPORTED`
- `CONFLICTS_WITH_DATA`
- `CONFLICTS_WITH_DESIGN`
- `CONFLICTS_WITH_JOURNAL_POLICY`
- `REQUIRES_VERIFICATION`

---

# Reviewer Authority Guard

A reviewer request is not automatically scientifically correct merely because a reviewer made it.

Assess the request against:

- study design;
- data;
- methods;
- current evidence;
- reporting standards;
- journal policy;
- scientific logic.

---

# Respectful Disagreement

The author may disagree.

Use:

> We appreciate the reviewer’s concern. We respectfully disagree with the requested interpretation because...

Then provide evidence.

Do not use adversarial language.

---

# Do Not Agree Falsely

Never write:

> We agree and have revised accordingly.

unless the manuscript was actually revised accordingly.

---

# Response Before Revision Guard

Do not finalize a response before required revisions are completed or verified.

Preferred sequence:

```text
Reviewer Comment
      ↓
Scientific Assessment
      ↓
Required Revision
      ↓
Revision Completed
      ↓
Revision Verified
      ↓
Response Drafted
```

---

# Response Status

Use:

- `NOT_STARTED`
- `ASSESSING`
- `UPSTREAM_CORRECTION_REQUIRED`
- `REVISION_IN_PROGRESS`
- `REVISION_COMPLETED`
- `RESPONSE_DRAFTED`
- `VERIFIED`
- `READY_FOR_RESUBMISSION`

---

# Revision Action Types

Possible actions include:

- `TEXT_CLARIFICATION`
- `TEXT_CORRECTION`
- `METHOD_CLARIFICATION`
- `REANALYSIS`
- `ADDITIONAL_ANALYSIS`
- `TABLE_REVISION`
- `FIGURE_REVISION`
- `SUPPLEMENT_REVISION`
- `REFERENCE_UPDATE`
- `LIMITATION_EXPANSION`
- `CONCLUSION_NARROWING`
- `NOVELTY_RECALIBRATION`
- `THEORY_REFRAMING`
- `NO_MANUSCRIPT_CHANGE_JUSTIFIED`
- `NEW_DATA_REQUIRED`
- `NOT_FEASIBLE_POST_HOC`

---

# Upstream Routing

When a reviewer reveals a genuine scientific problem, route appropriately.

### Research Question

`research-question-builder`

### Theory

`theoretical-framework`

### Conceptual Framework

`conceptual-framework`

### Methodology

`methodology-architect`

### Protocol

`protocol-builder`

### Sampling

`sampling-strategy`

### Instrument

`instrument-design`

### Analysis

`analysis-planner`

or:

`statistical-method-selector`

### Qualitative Analysis

`qualitative-analysis`

### Mixed Methods

`mixed-method-analysis`

### Meta-Analysis

`meta-analysis`

### Result Interpretation

`result-interpreter`

### Discussion

`scientific-discussion`

### Implications

`implication-builder`

### Novelty

`novelty-auditor`

### References

`reference-integrity-guard`

### Manuscript Architecture

`manuscript-architect`

### Manuscript Writing

`manuscript-writer`

### Journal Fit

`journal-matcher`

---

# No Cosmetic Repair of Scientific Problems

Do not route:

```text
methodological flaw
      ↓
manuscript-writer
```

unless the problem is genuinely only reporting.

---

# Comment Resolution Logic

For every reviewer comment determine:

```text
Is the comment scientifically valid?
      ↓
YES / PARTIAL / NO / UNCERTAIN
      ↓
Does manuscript change follow?
      ↓
YES / NO
      ↓
What evidence justifies the response?
      ↓
What exact revision was made?
```

---

# Accepting a Comment

A strong acceptance response contains:

1. acknowledgement;
2. scientific action;
3. exact manuscript change;
4. location;
5. concise explanation.

Example:

> Thank you for this important comment. We agree that the original wording overstated causal interpretation. We revised the Discussion and Conclusion to describe the association rather than a causal effect. The changes appear in the Discussion, paragraph 4, and Conclusion, paragraph 1.

---

# Partial Agreement

When partly agreeing:

> We agree that clarification is needed; however, we do not agree that the analysis should be replaced because...

Then explain the retained method.

---

# Scientific Disagreement

A defensible disagreement should include:

- respectful acknowledgement;
- explicit point of disagreement;
- scientific rationale;
- supporting evidence;
- manuscript clarification if useful.

---

# No Defensive Tone

Avoid:

- “The reviewer misunderstood.”
- “The reviewer is wrong.”
- “Obviously...”
- “As clearly stated...”
- “We already explained this.”

Prefer:

> We appreciate that the original text may not have made this sufficiently clear.

---

# Reviewer Misunderstanding as Signal

If a reviewer misunderstands something that is technically present, consider whether the manuscript needs clearer wording.

---

# Citation Verification

Any citation introduced in a response must be verified.

Use:

- `source-verification`;
- `reference-integrity-guard`;

when needed.

---

# Target-Journal Citation Guard

Do not add citations merely because they are from the target journal.

---

# Self-Citation Guard

Do not add self-citations unless scientifically relevant.

---

# Retraction Guard

Do not use retracted literature to defend a response.

---

# Statistical Reviewer Response

For statistical comments, determine whether the issue concerns:

- data coding;
- model choice;
- assumptions;
- diagnostics;
- effect size;
- uncertainty;
- multiplicity;
- missing data;
- sensitivity analysis;
- model fit;
- calibration;
- prediction;
- power;
- sample size.

---

# Reanalysis Guard

Do not say:

> We reanalyzed the data.

unless reanalysis was actually performed.

---

# Statistical Result Update

If reanalysis changes results:

- update abstract;
- methods;
- results;
- tables;
- figures;
- discussion;
- conclusion;
- supplement

as necessary.

---

# Cascading Change Guard

A revised estimate may require multiple downstream manuscript changes.

Do not update only the response letter.

---

# P-Value Guard

Do not respond to reviewer pressure by significance chasing.

Avoid:

- arbitrary subgrouping;
- unplanned exclusion;
- repeated model searching;
- outcome switching.

---

# Multiple-Testing Response

If reviewer requests additional tests:

- assess scientific necessity;
- assess multiplicity;
- label exploratory analyses transparently.

---

# Sample Size Response

Do not justify sample size using unsupported rules of thumb.

Use design-appropriate reasoning.

---

# Power Analysis Guard

Do not perform post-hoc observed-power calculations merely to defend a non-significant result.

---

# Missing Data Response

If reviewer raises missingness:

- report extent;
- explain handling;
- assess assumptions;
- add sensitivity analysis when justified.

---

# Method-Specific Response

Adapt reviewer-response logic to the study.

## Regression

Check:

- model family;
- reference coding;
- collinearity;
- confounding;
- nonlinearity;
- interactions;
- diagnostics;
- overfitting.

## Logistic Regression

Check:

- event count;
- separation;
- coding;
- OR interpretation;
- calibration;
- discrimination;
- stability.

## Survival Analysis

Check:

- time origin;
- censoring;
- proportional hazards;
- competing risks;
- time-varying effects.

## Longitudinal Analysis

Check:

- within-subject dependence;
- time coding;
- missing follow-up;
- repeated measures;
- random effects.

## Mediation

Do not defend causal mediation when temporal ordering and confounding assumptions are not met.

## Moderation

Check interaction terms, conditional effects, probing, and visualization.

## SEM

Check measurement model, identification, fit, structural paths, and post-hoc modifications.

## PLS-SEM

Check:

- reflective/formative specification;
- outer loadings/weights;
- reliability;
- AVE;
- HTMT;
- VIF;
- path inference;
- R²;
- f²;
- Q²;
- mediation;
- moderation;
- prediction.

## Qualitative Research

Potential concerns include:

- sampling;
- saturation/information power;
- reflexivity;
- coding;
- trustworthiness;
- quotations;
- analytic transparency.

Do not fabricate saturation if it was not established.

## Mixed Methods

Potential concerns include:

- rationale;
- timing;
- priority;
- integration;
- joint displays;
- meta-inference.

## Systematic Review

Potential concerns include:

- protocol;
- search strategy;
- databases;
- eligibility;
- duplicate screening;
- risk of bias;
- synthesis;
- certainty;
- PRISMA.

## Meta-Analysis

Potential concerns include:

- effect measure;
- model;
- heterogeneity;
- dependent effects;
- publication bias;
- subgroup analysis;
- meta-regression;
- sensitivity analysis.

## Pharmacogenetics

Potential concerns include:

- SNP rationale;
- genotyping QC;
- Hardy-Weinberg equilibrium;
- genetic models;
- multiple testing;
- haplotypes;
- population stratification;
- clinical covariates;
- replication.

## Pharmaceutical Formulation

Potential concerns include:

- formulation rationale;
- extraction/process conditions;
- characterization;
- controls;
- physicochemical tests;
- antimicrobial testing;
- replicates;
- stability;
- statistical analysis.

## Pharmacokinetics

Potential concerns include:

- sampling schedule;
- assay;
- PK model;
- parameter estimation;
- exposure metrics;
- covariates;
- diagnostics;
- variability.

---

# Novelty Reviewer Response

If reviewer challenges novelty:

```text
Reviewer Novelty Challenge
      ↓
novelty-auditor
      ↓
Recalibrated Claim
      ↓
Response
```

Do not defend “first ever” without verification.

---

# Novelty Downgrade

A response may legitimately say:

> We agree that the original novelty statement was too strong. We have revised the claim from “the first study” to “one of the first studies in...”.

---

# Closest Competitor Response

When reviewer identifies a close competitor:

- verify the study;
- compare methods;
- compare population;
- compare outcome;
- compare contribution;
- revise novelty if needed.

---

# Discussion Reviewer Response

Possible response actions include:

- add contradictory literature;
- narrow mechanistic interpretation;
- distinguish association from causation;
- discuss boundary conditions;
- add alternative explanations;
- refine limitations.

---

# Limitation Response

Do not use limitations as a dumping ground.

A reviewer-raised limitation should be linked to its effect on interpretation.

---

# Implication Response

If reviewer challenges implications:

- classify implication type;
- assess evidence strength;
- narrow if needed.

---

# Clinical Recommendation Guard

Do not defend clinical recommendations from evidence that does not support them.

---

# Policy Recommendation Guard

Do not defend policy claims beyond the evidence.

---

# Title and Abstract Response

If reviewer requests a title or abstract change, ensure the revised wording still accurately represents:

- design;
- population;
- exposure/intervention;
- outcome;
- causal status;
- main findings.

Any substantive result change must propagate to the abstract.

---

# Table Response

When revising tables:

- preserve denominators;
- correct units;
- define abbreviations;
- update footnotes;
- update statistical notation;
- avoid duplication.

---

# Figure Response

When revising figures:

- preserve data integrity;
- use correct axes;
- include uncertainty where relevant;
- avoid misleading scaling.

---

# Supplement Response

Do not hide essential methods in supplementary material.

---

# Reporting Guideline Response

Use relevant guidance such as:

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

Do not claim compliance unless actually checked.

---

# Ethics Comment Response

Do not fabricate:

- ethics approval;
- consent;
- registration;
- waiver;
- animal approval.

If absent, state the actual status.

---

# Transparency Response

Potential requests include:

- data availability;
- code availability;
- conflicts;
- funding;
- author contributions;
- AI-use disclosure.

---

# Data Availability

Do not promise open data if restrictions prevent it.

---

# Code Availability

Do not claim code availability unless code actually exists and is accessible as stated.

---

# AI Disclosure

If a reviewer or journal asks about AI use:

- follow current journal policy;
- describe actual use;
- do not invent a disclosure statement.

---

# Language and Style Comments

Language edits may be addressed by `manuscript-writer`.

But verify that wording changes do not alter scientific meaning.

---

# Reviewer Tone vs Scientific Content

Ignore hostility; answer the scientific point.

---

# Duplicate Reviewer Comments

If multiple reviewers raise the same issue:

- address each comment;
- avoid inconsistent responses;
- cross-reference when useful.

---

# Conflicting Reviewer Requests

When reviewers conflict:

```text
Reviewer 1 asks A
Reviewer 2 asks not-A
      ↓
Identify Scientific Basis
      ↓
Choose Defensible Resolution
      ↓
Explain to Both Reviewers
```

---

# Editor Priority

If editor instruction resolves reviewer conflict, prioritize the editor's explicit decision while preserving scientific validity.

---

# Impossible Reviewer Request

If a request cannot be fulfilled because data were not collected:

do not fabricate data.

Possible response:

> We agree that this information would strengthen the analysis. However, the requested variable was not collected in the original study and cannot be reconstructed reliably. We have therefore added this as a limitation and narrowed the corresponding interpretation.

---

# New Experiment Request

Determine whether new experiments are:

- necessary for current claims;
- desirable but not essential;
- outside study scope.

---

# Future Work Boundary

Do not promise future work as if it resolves a current validity problem.

---

# No Fabricated Compliance

Never write:

- “We have added...”
- “We performed...”
- “We corrected...”
- “We verified...”

unless the action actually occurred.

---

# Revision Evidence Record

For every completed revision record:

```yaml
revision_record:
  comment_id:
  manuscript_version_before:
  manuscript_version_after:
  action:
  section:
  paragraph:
  line_range:
  old_text:
  new_text:
  analysis_changed:
  results_changed:
  tables_changed:
  figures_changed:
  references_changed:
  verified:
```

---

# Line Number Guard

Only cite manuscript line numbers after final pagination or line numbering is stable.

---

# Page/Line Location

Response wording may use:

- page;
- line;
- section;
- paragraph;
- table;
- figure.

Use whatever the journal manuscript format supports.

---

# Track Changes

If the journal requests tracked changes:

- retain a marked manuscript;
- preserve a clean manuscript when useful.

---

# Response Letter Architecture

Recommended structure:

```text
Cover Note to Editor
      ↓
Editor Comments
      ↓
Reviewer 1
      ↓
Reviewer 2
      ↓
Reviewer 3
      ↓
Closing Note
```

---

# Cover Note

A concise cover note may include:

- thanks;
- decision acknowledged;
- major revision themes;
- confirmation that point-by-point responses follow.

Do not oversell.

---

# Point-by-Point Template

Use:

```markdown
### Reviewer 1 — Comment 1

**Comment**

[Reviewer comment]

**Response**

[Scientific response]

**Change in manuscript**

[Exact change and location]
```

---

# Response Without Manuscript Change

When no change is justified:

```markdown
**Response**

We appreciate this comment. After reviewing the issue, we respectfully retained the original analysis because...

**Change in manuscript**

No change was made to the analysis. We added a clarification in the Methods to make the rationale explicit.
```

---

# Response with Reanalysis

Use only after reanalysis is actually completed:

```markdown
**Response**

We agree that the original analysis did not adequately address [issue]. We therefore performed [analysis].

**Result of reanalysis**

[Verified result]

**Change in manuscript**

[Sections/tables/figures updated]
```

---

# Response with Narrowed Claim

Use:

```markdown
**Response**

We agree that the original wording was too strong. We revised the claim to reflect the study design and uncertainty.

**Change in manuscript**

[Old claim → revised claim]
```

---

# Response with Disagreement

Use:

```markdown
**Response**

We appreciate the reviewer’s concern. We respectfully disagree with the proposed change because [scientific rationale]. To reduce ambiguity, we clarified [specific issue] in the manuscript.

**Change in manuscript**

[Location]
```

---

# Response Length

Responses should be long enough to resolve the issue but not performatively verbose.

---

# Reviewer Burden

Make it easy for reviewers to verify changes.

---

# Response Matrix

Use:

| ID | Comment | Validity | Action | Manuscript Change | Location | Status |
|---|---|---|---|---|---|---|

---

# Revision Priority Matrix

Use:

| Priority | Comment ID | Severity | Scientific Impact | Action | Upstream Skill |
|---|---|---|---|---|---|

---

# Critical Path

Address in this order:

```text
Scientific Validity
      ↓
Methods / Analysis
      ↓
Results
      ↓
Interpretation
      ↓
Novelty / Discussion
      ↓
Reporting
      ↓
Presentation
```

---

# Major Revision Workflow

```text
Extract Comments
      ↓
Classify
      ↓
Identify Scientific Blockers
      ↓
Route Upstream
      ↓
Complete Revisions
      ↓
Verify Cascading Consistency
      ↓
Draft Responses
      ↓
Audit Response Letter
      ↓
Resubmit
```

---

# Minor Revision Workflow

Even minor revision may contain scientifically important items.

Do not assume all comments are cosmetic.

---

# Second-Round Review

Compare round 2 comments with:

- round 1 comment;
- round 1 response;
- revised manuscript.

---

# Reopened Comment

A reviewer may reopen a previously addressed issue.

Determine whether:

- original response was incomplete;
- manuscript revision was insufficient;
- reviewer disagrees scientifically;
- new concern emerged.

---

# Response Consistency Across Rounds

Do not contradict a previous response without explaining why.

---

# Version Control

Record:

```yaml
revision_round:
  round:
  manuscript_version:
  response_version:
  decision:
  editor_letter_date:
  response_deadline:
  changes_since_previous_round:
```

---

# Manuscript Version Guard

Never respond using the wrong manuscript version.

---

# Response Letter Version Guard

Ensure response letter matches the exact revised manuscript being submitted.

---

# Clean vs Tracked Version

If both exist:

- verify content is identical except markup;
- do not let tracked and clean versions diverge.

---

# Cascading Consistency Check

After substantive revision verify:

- abstract;
- methods;
- results;
- discussion;
- conclusion;
- tables;
- figures;
- supplements;
- references;
- reporting checklists.

---

# Editor Comment Priority

Editor comments may supersede reviewer suggestions when explicitly stated.

---

# Decision Letter Parsing

Separate:

- editorial requirements;
- reviewer scientific comments;
- administrative instructions.

---

# Administrative Instructions

Examples:

- word count;
- file naming;
- forms;
- declarations;
- graphical abstract;
- highlights;
- cover letter.

These should not redefine scientific results.

---

# Journal Policy Verification

Current journal instructions should be verified when the response depends on them.

---

# Deadline Handling

If response deadline matters, record it.

Do not fabricate deadline extensions.

---

# Extension Request Drafting

If requested, draft a professional extension request.

Do not claim circumstances not provided by the user.

---

# Appeal Assessment

Before recommending appeal, assess:

- factual error in decision;
- reviewer misunderstanding;
- procedural concern;
- conflict with stated journal policy;
- strong scientific basis.

---

# Appeal Guard

Do not appeal merely because rejection is disappointing.

---

# Appeal Tone

Appeals should be concise, evidence-based, and non-confrontational.

---

# Rejection After Review

If rejected:

```text
Rejection Reason
      ↓
Scientific Problem?
      ├─ YES → upstream correction
      └─ NO  → journal-matcher
```

---

# Journal Hopping Guard

Do not immediately move to another journal if reviewer comments reveal genuine scientific problems.

---

# Resubmission Strategy

After rejection and valid correction:

`journal-matcher`

may identify the next target.

---

# Transfer Offer

If publisher offers journal transfer:

- evaluate scientific fit;
- do not accept solely for convenience.

---

# Response to Simulated Review

For simulated comments:

- clearly label them simulated;
- use them as internal revision tasks;
- do not create a fake journal response letter unless requested as practice.

---

# Practice Rebuttal

If the user wants practice:

state:

> Simulated response exercise — not an actual journal correspondence.

---

# Actual Reviewer Comments Supersede Simulated Ones

Once actual review exists, prioritize actual comments.

Simulated concerns may still be used as internal quality checks.

---

# Mixed Review Packet

If both actual and simulated comments are used:

```yaml
comment_source:
  actual:
  simulated:
  internal:
```

Keep them separate.

---

# Response Risk Flags

Flag:

- `UNRESOLVED_SCIENTIFIC_ISSUE`
- `UNVERIFIED_REFERENCE`
- `UNVERIFIED_JOURNAL_POLICY`
- `REANALYSIS_NOT_COMPLETED`
- `MANUSCRIPT_CHANGE_NOT_VERIFIED`
- `CASCADING_RESULT_CHANGE`
- `POTENTIAL_CONTRADICTION`
- `NEW_DATA_REQUIRED`
- `ETHICS_ISSUE`
- `RESPONSE_OVERCLAIM`

---

# Ready-for-Resubmission Gate

Do not mark ready until:

- all editor comments addressed;
- all reviewer comments addressed;
- critical/major scientific issues resolved or transparently justified;
- revisions verified;
- response letter matches manuscript;
- references verified;
- tables/figures synchronized;
- reporting checklist updated if required;
- journal administrative requirements checked.

---

# Readiness Status

Use:

- `NOT_READY`
- `SCIENTIFIC_CORRECTION_REQUIRED`
- `REVISION_IN_PROGRESS`
- `RESPONSE_REVIEW_REQUIRED`
- `READY_WITH_MINOR_ADMIN_TASKS`
- `READY_FOR_RESUBMISSION`

---

# Response Audit

Before finalizing each response ask:

- Did we answer the actual comment?
- Is the science correct?
- Did we perform the claimed revision?
- Is the location accurate?
- Did the revision introduce contradictions?
- Does the response overstate agreement?
- Does the response rely on unverified evidence?

---

# Reviewer Response Passport

Use:

```yaml
reviewer_response:
  journal:
  manuscript_id:
  manuscript_title:
  review_round:
  decision:
  manuscript_version_reviewed:
  revised_manuscript_version:
  reviewer_count:
  editor_comment_count:
  reviewer_comment_count:
  critical_count:
  major_count:
  moderate_count:
  minor_count:
  editorial_count:
  unresolved_count:
  reanalysis_count:
  new_reference_count:
  disagreement_count:
  readiness_status:
```

---

# Full Output

When a comprehensive response workflow is requested provide:

## A. Decision Summary
[...]

## B. Comment Inventory
[...]

## C. Scientific Validity Assessment
[...]

## D. Revision Priority Matrix
[...]

## E. Required Upstream Corrections
[...]

## F. Editor Response
[...]

## G. Reviewer 1 Responses
[...]

## H. Reviewer 2 Responses
[...]

## I. Reviewer 3 Responses
[...]

## J. Cascading Manuscript Changes
[...]

## K. Reference / Evidence Verification
[...]

## L. Reanalysis Summary
[...]

## M. Remaining Risks
[...]

## N. Resubmission Readiness
[...]

---

# Compact Output

For a small number of comments provide:

## Comment
[...]

## Assessment
[...]

## Required Action
[...]

## Suggested Response
[...]

## Manuscript Change
[...]

---

# User-Friendly Behavior

Prefer:

> Reviewer 1’s request is scientifically valid and requires reanalysis before we draft the final rebuttal. I would not write “we have reanalyzed the data” yet because that analysis has not been completed.

Or:

> I would partially agree with this comment. The reviewer is correct that the causal wording is too strong, but replacing the regression model is not justified by the study design. The safest response is to narrow the interpretation and clarify the model rationale.

Or:

> These two reviewers are asking for conflicting changes. We should not satisfy both mechanically. We need to resolve the scientific question first, then explain the chosen approach respectfully to each reviewer.

Or:

> The manuscript already contains the requested information, but the reviewer’s confusion indicates that the wording is not sufficiently visible. A clarification is preferable to simply telling the reviewer that it is already there.

---

# Avoid These Behaviors

Do not:

- fabricate reviewer comments;
- fabricate editor decisions;
- fabricate completed revisions;
- fabricate reanalysis;
- fabricate new data;
- fabricate ethics approval;
- fabricate journal policy;
- fabricate citations;
- claim full compliance without checking;
- agree falsely;
- use aggressive rebuttal language;
- significance-shop;
- outcome-switch;
- add irrelevant citations to appease reviewers;
- perform citation padding;
- hide scientific problems through prose;
- ignore contradictory reviewer requests;
- promise impossible new data;
- overstate novelty;
- overstate causality;
- misrepresent simulated comments as actual;
- resubmit before critical scientific issues are resolved.

---

# Stop Conditions

Do not produce a final response letter when:

- reviewer comments are unavailable;
- manuscript version is unclear;
- required reanalysis is incomplete;
- claimed revisions cannot be verified;
- critical scientific issues remain unresolved;
- journal policy is essential but unverified;
- ethics concerns are unresolved.

Use:

- `COMMENTS_REQUIRED`
- `MANUSCRIPT_VERSION_REQUIRED`
- `REANALYSIS_REQUIRED`
- `REVISION_VERIFICATION_REQUIRED`
- `SCIENTIFIC_CORRECTION_REQUIRED`
- `JOURNAL_POLICY_VERIFICATION_REQUIRED`
- `ETHICS_RESOLUTION_REQUIRED`

when appropriate.

---

# Relationship with Reviewer Simulator

`reviewer-simulator` generates adversarial simulated comments.

`reviewer-response` determines how to revise and respond.

```text
reviewer-simulator
      ↓
reviewer-response
```

---

# Relationship with Manuscript Auditor

If reviewer feedback exposes broad manuscript-integrity problems:

`manuscript-auditor`

may be rerun after material revision.

Do not rerun unnecessarily.

---

# Relationship with Journal Matcher

If rejection is primarily due to scope or journal fit:

`journal-matcher`

should guide the next target.

---

# Relationship with Manuscript Writer

`manuscript-writer` may implement approved textual revisions.

It must not invent scientific corrections.

---

# Relationship with Result Interpreter

Use `result-interpreter` when reviewer comments challenge:

- meaning;
- uncertainty;
- effect magnitude;
- causal status;
- null findings.

---

# Relationship with Scientific Discussion

Use `scientific-discussion` when comments challenge:

- literature comparison;
- mechanisms;
- contradictions;
- alternative explanations;
- limitations.

---

# Relationship with Novelty Auditor

Use `novelty-auditor` when reviewers challenge:

- originality;
- priority;
- closest competitors;
- “first” claims.

---

# Relationship with Reference Integrity Guard

Use `reference-integrity-guard` before adding or defending references.

---

# Relationship with Methodology Architect

Use `methodology-architect` when reviewers expose design or method problems.

---

# Relationship with Analysis Planner

Use `analysis-planner` for scientifically justified additional analyses.

---

# Relationship with Statistical Method Selector

Use `statistical-method-selector` when reviewer criticism concerns method choice.

---

# Success Criterion

`reviewer-response` succeeds when actual or simulated reviewer and editor comments are converted into a transparent, traceable, scientifically defensible revision-and-response workflow; when actual and simulated review sources are never confused; when every comment is preserved faithfully, classified by scientific type, severity, validity, actionability, and required revision; when valid criticism leads to verified manuscript correction before response language claims that the correction has occurred; when scientifically debatable or unsupported requests may be respectfully challenged with evidence rather than accepted mechanically; when conflicting reviewer requests are reconciled according to scientific validity and explicit editorial guidance rather than appeasement; when reanalysis, new citations, new data, ethics approvals, journal policies, reporting compliance, or manuscript changes are never fabricated; when cascading changes caused by revised analyses are propagated consistently through abstract, methods, results, tables, figures, discussion, conclusion, supplements, references, and reporting checklists; when genuine scientific problems are routed back to the appropriate upstream skill instead of being hidden through prose; when response letters remain respectful, concise, point-by-point, and easy for reviewers to verify; when journal rejection leads either to genuine scientific correction or scientifically appropriate rematching rather than automatic journal hopping; when response and manuscript versions remain synchronized across review rounds; and when the manuscript is marked `READY_FOR_RESUBMISSION` only after scientific issues, revisions, evidence integrity, response consistency, and relevant journal requirements have been adequately resolved.
