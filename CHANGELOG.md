# Changelog

All notable changes to Universal Research Skills will be documented in this file.

## [0.12.0] - Journal Matching & Publication Strategy Layer

### Added

- `journal-matcher` skill for identifying, verifying, comparing, ranking, and justifying scientifically appropriate publication targets for scientifically stable manuscripts.
- Scientific-fit-first journal matching based on research problem, study design, methods, contribution, article type, audience, novelty, evidence strength, and translational level.
- Current-status verification for journal scope, indexing, Scopus coverage, quartile context, publication model, APC requirements, other fees, article types, and editorial requirements.
- Explicit safeguards against prestige-driven matching, quartile-only selection, APC-first filtering, citation padding, unsupported indexing claims, historical-indexing confusion, and publication-pressure-driven scientific distortion.
- Version-aware scientific-audit gate ensuring that journal matching normally follows `manuscript-auditor` without unnecessarily repeating audit for an unchanged manuscript version.
- Submission sequencing with ambitious, balanced, conservative, and backup journal targets.
- Risk screening for discontinued, hijacked, predatory, unverifiable, misleading, or scientifically incompatible journals.
- Rejection-recovery routing so genuine scientific criticism returns to the appropriate upstream research skill rather than being treated merely as a journal-selection problem.

### Journal Matching Architecture

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

The new layer establishes `journal-matcher` as the bridge between a scientifically defensible manuscript and publication strategy.

### Core Principle

The governing principle is:

> **Scientific fit first. Publication strategy second.**

Preferred logic:

```text
Scientifically Stable Manuscript
      ↓
Scientific Identity Extraction
      ↓
Journal Discovery
      ↓
Current Status Verification
      ↓
Scope & Article-Type Matching
      ↓
Audience & Method Compatibility
      ↓
Indexing & Publication Model Verification
      ↓
Risk Screening
      ↓
Constraint-Aware Ranking
      ↓
Target Journal Shortlist
      ↓
Submission Strategy
```

Journal prestige, quartile, APC status, or publication speed must not override scientific compatibility.

### Scientific Identity Extraction

Before matching journals, the manuscript is characterized using elements such as:

- research problem;
- research question;
- discipline and subdiscipline;
- study design;
- population or material;
- intervention or exposure;
- comparator;
- primary and secondary outcomes;
- analytical approach;
- evidence strength;
- causal status;
- novelty type;
- contribution type;
- article type;
- reporting guideline;
- geographic context;
- intended audience;
- translational level.

This prevents journal selection from being based only on title keywords.

### Journal-Matching Entry Modes

Supported entry modes include:

- `JOURNAL_DISCOVERY`
- `JOURNAL_SHORTLIST`
- `JOURNAL_COMPARISON`
- `JOURNAL_VERIFICATION`
- `SCOPUS_VERIFICATION`
- `INDEXING_VERIFICATION`
- `APC_SCREENING`
- `NO_MANDATORY_APC_SEARCH`
- `OPEN_ACCESS_MODEL_CHECK`
- `ARTICLE_TYPE_MATCHING`
- `SCOPE_MATCHING`
- `PUBLISHER_VERIFICATION`
- `DISCONTINUATION_CHECK`
- `PREDATORY_RISK_SCREENING`
- `SUBMISSION_SEQUENCE_PLANNING`
- `JOURNAL_REPLACEMENT`
- `REJECTION_RECOVERY`
- `TARGET_JOURNAL_REASSESSMENT`

### Scientific Readiness Gate

Before confident journal ranking, the manuscript may be classified as:

- `MATCHING_READY`
- `MATCHING_READY_WITH_MINOR_UNRESOLVED_ISSUES`
- `SCIENTIFIC_AUDIT_REQUIRED`
- `METHOD_REASSESSMENT_REQUIRED`
- `RESULT_REINTERPRETATION_REQUIRED`
- `NOVELTY_REASSESSMENT_REQUIRED`
- `REFERENCE_VERIFICATION_REQUIRED`
- `MANUSCRIPT_ARCHITECTURE_UNSTABLE`
- `ARTICLE_TYPE_UNCLEAR`
- `MATCHING_SCOPE_REQUIRES_CLARIFICATION`

Journal matching must not be used to bypass unresolved scientific weaknesses.

### Version-Aware Audit Gate

Journal matching normally follows scientific audit.

If the current manuscript version has not yet passed scientific audit, or if material scientific revisions have occurred since the previous audit:

```text
manuscript-auditor
      ↓
journal-matcher
```

If the same manuscript version has already passed scientific audit with no unresolved submission-blocking issues and no material scientific changes:

```text
journal-matcher
```

can run directly.

This prevents both unsafe audit bypass and unnecessary repeated auditing.

### Journal Discovery Strategy

Preferred discovery sequence:

```text
Scientific Identity
      ↓
Field / Subfield Journals
      ↓
Closest-Comparator Journals
      ↓
Method-Compatible Journals
      ↓
Audience-Compatible Journals
      ↓
Cross-Disciplinary Candidates
      ↓
Current Status Verification
```

Recent journal content may be used as evidence of current editorial interest, but publication of a competitor study in a journal does not automatically make that journal the best target.

### Scientific Contribution Matching

Journal ambition and fit may be calibrated using contribution types including:

- theoretical;
- mechanistic;
- empirical;
- clinical;
- pharmaceutical;
- pharmacogenetic;
- pharmacokinetic;
- formulation;
- analytical-method;
- diagnostic;
- prognostic;
- prediction-model;
- validation;
- implementation;
- educational;
- social-science;
- engineering;
- materials;
- public-health;
- systematic-review;
- meta-analysis;
- qualitative;
- mixed-method;
- methodological;
- replication;
- context extension.

### Novelty Calibration

`journal-matcher` uses the output of `novelty-auditor`.

Possible novelty profiles include:

- high conceptual novelty;
- mechanistic novelty;
- methodological novelty;
- validation novelty;
- context-specific extension;
- replication with value;
- incremental advancement;
- negative or null contribution;
- contradictory evidence;
- emerging-topic contribution.

Novelty must not be exaggerated simply to target a higher-tier journal.

### Article-Type Compatibility

Journal matching verifies whether a candidate accepts the actual manuscript type, such as:

- Original Article
- Research Article
- Full-Length Article
- Short Communication
- Brief Report
- Technical Note
- Methods Article
- Validation Study
- Clinical Study
- Pharmacogenomics Study
- Formulation Study
- Experimental Study
- Systematic Review
- Meta-Analysis
- Narrative Review
- Scoping Review
- Qualitative Research
- Mixed-Methods Research
- Case Report
- Protocol
- Data Note
- Registered Report

The study must not be reshaped scientifically merely to fit a preferred article category.

### Scope Fit

Scope fit may be classified as:

- `EXCELLENT`
- `STRONG`
- `MODERATE`
- `WEAK`
- `OUT_OF_SCOPE`

Assessment considers:

- scientific problem;
- design;
- method;
- population or material;
- contribution;
- translational level;
- audience;
- article type.

Journal-title similarity alone is insufficient evidence of fit.

### Audience Fit

Audience fit may be classified as:

- `DIRECT_CORE_AUDIENCE`
- `STRONG_ADJACENT_AUDIENCE`
- `INTERDISCIPLINARY_AUDIENCE`
- `LIMITED_AUDIENCE_FIT`
- `AUDIENCE_MISMATCH`

This helps distinguish a scientifically appropriate specialized journal from a superficially broader but poorly aligned journal.

### Method Compatibility

The layer checks whether journals routinely publish studies using the relevant methods, for example:

- randomized trials;
- observational designs;
- pharmacogenetics;
- pharmacokinetic modeling;
- formulation experiments;
- diagnostic validation;
- prediction models;
- qualitative analysis;
- mixed methods;
- SEM;
- PLS-SEM;
- meta-analysis;
- educational interventions.

Topical scope alone does not guarantee methodological fit.

### Scopus-First Journal Verification

When Scopus indexing is required:

> **Scopus-first applies to journal discovery and indexing verification.**

However:

- publisher reputation does not prove Scopus status;
- an old Scopus badge does not prove current active coverage;
- publication of older indexed articles does not prove current coverage;
- Scopus inclusion does not automatically imply scientific fit or quality.

### Scopus Status Architecture

Possible classifications include:

- `ACTIVE_SCOPUS`
- `SCOPUS_DISCONTINUED`
- `SCOPUS_COVERAGE_ENDED`
- `SCOPUS_STATUS_UNCLEAR`
- `NOT_SCOPUS_VERIFIED`
- `OTHER_INDEXING_ONLY`

The framework explicitly distinguishes:

```text
historically indexed
≠
currently indexed
```

### Quartile Safeguard

Quartile claims must be interpreted with:

- year;
- database or metric source;
- subject category.

The system must not simply state that a journal is Q1, Q2, Q3, or Q4 without appropriate context when current verification is possible.

### Metric Safeguards

The layer distinguishes:

- CiteScore;
- SJR;
- SNIP;
- Journal Impact Factor.

Metrics must not be conflated.

They are secondary journal descriptors rather than primary scientific-fit criteria.

### Publication Model Classification

Journals may be classified as:

- `SUBSCRIPTION`
- `HYBRID`
- `FULL_OPEN_ACCESS`
- `DIAMOND_OPEN_ACCESS`
- `UNKNOWN`

### APC Principle

APC is treated as a publication constraint rather than scientific evidence.

Correct sequence:

```text
Scientific Fit
      ↓
Journal Legitimacy
      ↓
Indexing / Scope Verification
      ↓
Publication Model / APC Constraint
```

Incorrect sequence:

```text
No APC
      ↓
therefore scientifically suitable
```

### No-Mandatory-APC Strategy

When publication without mandatory APC is preferred, the layer can prioritize:

1. subscription journals with no mandatory publication charge;
2. hybrid journals where standard subscription publication does not require OA payment;
3. diamond open-access journals;
4. journals with verified waiver mechanisms;
5. full-OA journals when acceptable.

Hybrid journals should not simply be described as “free.”

Preferred wording is:

> No mandatory APC for the standard subscription route, subject to current publisher policy.

### APC Verification Status

Possible statuses include:

- `NO_MANDATORY_APC_VERIFIED`
- `OPTIONAL_OA_APC`
- `MANDATORY_APC`
- `WAIVER_AVAILABLE`
- `APC_STATUS_UNCLEAR`
- `OTHER_FEES_PRESENT`

### Hidden Publication Costs

Journal verification may also check:

- submission fees;
- page charges;
- color charges;
- excess-length charges;
- mandatory language-editing fees;
- society-membership requirements.

### Predatory-Risk Screening

A journal must not be labeled predatory merely because it:

- charges APC;
- is new;
- has a low metric;
- is published outside North America or Europe.

Risk assessment instead considers evidence such as:

- false indexing claims;
- unverifiable editorial board;
- misleading metrics;
- fake impact factors;
- copied journal names;
- unclear publisher identity;
- hidden fees;
- implausible peer-review promises;
- suspicious website inconsistencies;
- aggressive solicitation;
- fake archiving claims.

Possible classifications:

- `LOW_RISK`
- `SOME_CONCERNS`
- `HIGH_RISK`
- `UNVERIFIED`

### Hijacked Journal Safeguard

The layer verifies journal identity using:

- title;
- ISSN;
- eISSN;
- publisher;
- authentic journal homepage.

Similar or copied journal names must be disambiguated before recommendation.

### Current Metadata Principle

Journal metadata are treated as time-sensitive.

Current verification may be required for:

- indexing;
- quartile;
- CiteScore;
- SJR;
- Impact Factor;
- publisher;
- APC;
- open-access model;
- author instructions;
- word limits;
- article types;
- editorial policies;
- discontinued status.

Old journal lists, spreadsheets, blog posts, screenshots, or cached rankings must not automatically be treated as current.

### Verification Source Preference

Preferred journal-verification sources include:

1. official journal website;
2. official publisher website;
3. official Scopus source information;
4. Clarivate when relevant;
5. DOAJ when relevant;
6. official scholarly-society pages;
7. recognized indexing databases.

Secondary aggregators should be used cautiously.

### Journal Ranking Dimensions

Candidate journals may be evaluated across:

1. scientific scope fit;
2. audience fit;
3. article-type fit;
4. method fit;
5. novelty fit;
6. evidence-strength fit;
7. indexing status;
8. journal legitimacy;
9. publication model;
10. APC and fee compatibility;
11. reporting compatibility;
12. practical constraints;
13. strategic sequencing.

### Default Priority Architecture

Unless the researcher specifies otherwise:

```text
Scientific Scope Fit
      >
Audience Fit
      >
Article-Type Fit
      >
Method Fit
      >
Indexing / Legitimacy
      >
Evidence-Strength Fit
      >
Practical Constraints
      >
APC Preference
      >
Prestige Metrics
```

### Prestige Safeguard

Journal ranking must not be driven primarily by:

- Impact Factor;
- CiteScore;
- SJR;
- quartile;
- publisher prestige.

A highly specialized journal may be a better scientific target than a broader journal with a higher metric.

### Journal Recommendation Classes

Possible recommendations include:

- `EXCELLENT_MATCH`
- `STRONG_MATCH`
- `CONDITIONAL_MATCH`
- `BACKUP_MATCH`
- `WEAK_MATCH`
- `DO_NOT_RECOMMEND`

### Evidence Confidence

Recommendation confidence may be recorded as:

- `HIGH_CONFIDENCE`
- `MODERATE_CONFIDENCE`
- `LOW_CONFIDENCE`
- `REQUIRES_CURRENT_VERIFICATION`

### Submission Sequencing

A shortlist may be organized as:

- `TARGET_A` — ambitious but scientifically defensible;
- `TARGET_B` — strong balanced fit;
- `TARGET_C` — conservative strong fit;
- `BACKUP_1`;
- `BACKUP_2`.

`TARGET_A` must not simply mean the highest-metric journal.

### Journal Fit Matrix

The layer supports structured comparison such as:

```text
Journal
→ Scope
→ Audience
→ Article Type
→ Method
→ Indexing
→ APC Model
→ Risk
→ Overall Fit
```

### Desk-Rejection Risk

Desk-rejection risk may be qualitatively classified as:

- `LOW`
- `MODERATE`
- `HIGH`
- `UNCERTAIN`

based on:

- scope mismatch;
- audience mismatch;
- unsupported article type;
- narrow contribution;
- format incompatibility;
- novelty mismatch.

Numerical rejection probabilities must not be invented.

### Publication-Speed Safeguard

Publication speed may be considered, but:

```text
faster
≠
scientifically better
```

Acceptance rates and editorial timelines must not be invented when reliable data are unavailable.

### Target-Journal Citation Safeguard

Articles published in target journals may be examined to understand:

- scientific conversation;
- recent topics;
- common methods;
- audience;
- editorial positioning.

However:

> Target-journal references must never be added merely to increase perceived acceptance probability.

Citation padding remains prohibited.

### Scientific Record Preservation

Journal matching may adapt:

- title wording;
- abstract format;
- section organization;
- word count;
- figure and table allocation;
- supplementary strategy;
- cover-letter emphasis;
- submission metadata.

Journal matching must not alter:

- research question;
- study design;
- methods actually performed;
- primary outcome;
- numerical results;
- interpretation;
- validated gap;
- audited novelty;
- causal status;
- scientific conclusion.

### Simultaneous Submission Safeguard

The framework does not recommend simultaneous submission to multiple journals when prohibited.

Default principle:

> One active submission at a time unless explicitly permitted by the journal.

### Rejection Recovery

Journal rejection can be classified as:

- `SCOPE_REJECTION`
- `NOVELTY_REJECTION`
- `METHOD_REJECTION`
- `REPORTING_REJECTION`
- `PRIORITY_REJECTION`
- `FORMAT_REJECTION`
- `EDITORIAL_CAPACITY_REJECTION`
- `REVIEWER_SCIENTIFIC_REJECTION`
- `UNKNOWN`

### Rejection Routing

A rejection should not automatically trigger immediate submission to another journal.

Examples:

```text
Scope rejection
      ↓
journal-matcher
```

```text
Novelty challenge
      ↓
novelty-auditor
```

```text
Methodological challenge
      ↓
methodology-architect
or
manuscript-auditor
```

```text
Interpretation challenge
      ↓
result-interpreter
```

```text
Writing / architecture problem
      ↓
manuscript-architect
or
manuscript-writer
```

This prevents journal hopping from concealing genuine scientific weaknesses.

### `research-router` Integration

`Stage 11 — Journal Selection` was expanded.

The router now checks scientific-audit status before journal matching.

If the manuscript is not yet audited or has undergone material scientific revision:

```text
manuscript-auditor
      ↓
journal-matcher
```

If the same manuscript version has already passed audit:

```text
journal-matcher
```

The previous routing dependence on separate `no-apc-journal-finder` and `target-journal-intelligence` stages is removed from the core Stage 11 pathway because these functions are now integrated into `journal-matcher`.

Stage 11 now explicitly covers:

- scientific scope;
- audience;
- article type;
- method fit;
- indexing;
- Scopus status;
- discontinued coverage;
- quartile context;
- publication model;
- APC;
- waiver and fee verification;
- recent journal content;
- legitimacy;
- submission sequencing.

### `research-intake` Integration

`G4. Journal Selection` is now version-aware.

If the manuscript has not passed scientific audit or has undergone material scientific revision:

```text
manuscript-auditor
      ↓
journal-matcher
```

If the same manuscript version has already passed scientific audit:

```text
journal-matcher
```

The Existing Manuscript Routing Summary was also updated to use an audit-status gate before journal selection.

### Journal Matching vs Manuscript Audit

`manuscript-auditor` asks:

> Is the manuscript scientifically defensible and sufficiently complete?

`journal-matcher` asks:

> Where does this scientifically stable manuscript fit best?

Journal matching cannot substitute for scientific audit.

### Journal Matching vs Reviewer Simulation

After a target journal has been selected:

```text
journal-matcher
      ↓
reviewer-simulator
```

`reviewer-simulator` may then use the selected journal's audience, scope, and expectations to stress-test the manuscript.

### Journal Matching vs Manuscript Writing

`journal-matcher` determines publication fit and required presentation-level adaptation.

`manuscript-writer` performs controlled writing or adaptation.

Journal selection must not rewrite the scientific record.

### Journal Matching vs Novelty Audit

`novelty-auditor` determines what is genuinely novel.

`journal-matcher` uses that audited novelty to calibrate journal ambition.

### Framework Progression

```text
Evidence Discovery & Verification
      ↓
Scientific Positioning
      ↓
Research Logic & Framework
      ↓
Methodology & Study Design
      ↓
Analysis Planning & Method Selection
      ↓
Results Interpretation
      ↓
Scientific Discussion
      ↓
Implication Building
      ↓
Manuscript Architecture
      ↓
Manuscript Writing
      ↓
Manuscript Audit & Publication Readiness
      ↓
Journal Matching & Publication Strategy
      ↓
Reviewer Simulation
      ↓
Reviewer Response
```

This release establishes an evidence-based, verification-aware publication-targeting layer that separates **scientific journal fit** from **prestige, metrics, APC pressure, and publication convenience**, while ensuring that journal selection remains downstream of scientific audit and upstream of adversarial reviewer simulation.

---

## [0.11.0] - Manuscript Audit & Publication Readiness Layer

### Added

- `manuscript-auditor` skill for auditing completed or near-complete scientific manuscripts as scientific objects rather than merely proofreading them.
- Structured audit of scientific integrity, internal consistency, reporting completeness, reference integrity, claim-evidence alignment, methodological fidelity, result-discussion-conclusion coherence, novelty calibration, ethics, declarations, tables, figures, supplementary materials, and publication readiness.
- Explicit audit entry modes for full-manuscript audit, scientific-integrity audit, section audit, pre-submission audit, reporting-guideline audit, reference audit, consistency audit, statistical-reporting audit, claim-strength audit, novelty audit, journal-readiness audit, and revision re-audit.
- Severity classification separating `CRITICAL`, `MAJOR`, `MODERATE`, `MINOR`, and `EDITORIAL` issues.
- Transparent submission-readiness decisions and upstream routing when scientific problems require correction before publication-oriented work continues.
- Version-aware audit logic preventing unnecessary repetition of a completed scientific audit when the same manuscript version has not materially changed.

### Manuscript Audit Architecture

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

`manuscript-auditor` now functions as a scientific gate between manuscript writing and downstream publication strategy.

### Core Audit Principle

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

The governing principle is:

> **Audit the science before polishing the submission.**

### Audit Severity Architecture

Audit findings are classified as:

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

Scientific and methodological problems must be resolved before stylistic or formatting refinement is prioritized.

### Scientific Integrity Audit

The new layer checks alignment across:

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

It detects:

- research-question drift;
- hypothesis inconsistency;
- design misclassification;
- unsupported causal inference;
- method-result mismatch;
- outcome switching;
- selective reporting;
- contradictory numerical reporting;
- unsupported mechanistic claims;
- exaggerated novelty;
- implication escalation;
- conclusion overreach.

### Study Design Safeguards

The audit verifies whether the manuscript correctly identifies and respects the inferential limits of designs including:

- cross-sectional studies;
- cohort studies;
- case-control studies;
- randomized controlled trials;
- quasi-experimental studies;
- laboratory experiments;
- qualitative studies;
- mixed-method studies;
- systematic reviews;
- meta-analyses;
- diagnostic studies;
- prediction-model studies;
- validation studies.

The audit prevents labels such as `causal`, `experimental`, `prospective`, `longitudinal`, or `validation` from being used when the actual design does not support them.

### Methodological Fidelity

The audit checks whether Methods accurately describe what was actually done rather than retrospectively idealizing the study.

Domains include:

- population;
- sampling;
- inclusion and exclusion criteria;
- variables;
- measurement;
- intervention or exposure;
- procedures;
- analytical methods;
- ethics;
- reproducibility.

### Domain-Specific Audit Support

The new layer includes audit logic for:

- quantitative research;
- qualitative research;
- mixed methods;
- laboratory and formulation research;
- pharmacokinetics;
- pharmacogenetics;
- diagnostic accuracy;
- prediction models;
- validation studies;
- longitudinal analysis;
- multilevel analysis;
- survival analysis;
- SEM;
- PLS-SEM;
- mediation;
- moderation;
- machine learning;
- systematic reviews;
- meta-analysis.

### Statistical Reporting Safeguards

The audit checks:

- effect magnitude;
- direction;
- uncertainty;
- confidence intervals;
- p-values;
- assumptions;
- missing-data handling;
- multiplicity;
- model specification;
- reference categories;
- clustering;
- repeated measures;
- sensitivity analyses.

It explicitly prevents:

```text
significant
→ important
```

and:

```text
non-significant
→ no effect
```

from being treated as valid scientific conclusions without appropriate support.

### Result Integrity

The audit checks consistency of:

- sample size;
- outcome definitions;
- group labels;
- effect estimates;
- p-values;
- confidence intervals;
- result direction;
- primary and secondary outcome status;
- exploratory analyses.

When source outputs are available, manuscript values should be verified against them rather than assumed to have been copied correctly.

### Abstract Integrity

The audit verifies that the Abstract accurately represents:

- objective;
- design;
- sample;
- methods;
- primary results;
- uncertainty;
- conclusion.

The Abstract conclusion must not be stronger than the full manuscript conclusion.

### Introduction Audit

The Introduction is checked for coherent progression from:

```text
Problem
      ↓
Current Knowledge
      ↓
Unresolved Issue
      ↓
Validated Gap
      ↓
Audited Novelty
      ↓
Research Objective
```

Authority-first phenomenon evidence remains distinct from Scopus-first scholarly evidence.

### Novelty Calibration

The audit checks whether manuscript novelty claims remain consistent with the output of `novelty-auditor`.

It distinguishes:

- genuine novelty;
- partial novelty;
- contextual extension;
- replication;
- validation;
- methodological refinement.

Unverified claims such as “first,” “novel,” “unprecedented,” or “groundbreaking” are not accepted automatically.

### Discussion Audit

The Discussion is audited for:

- accurate statement of the main findings;
- comparison with closest evidence;
- convergence and divergence;
- theory and mechanism proportionality;
- contradictory evidence;
- validated contribution;
- limitations;
- bounded implications.

The audit prevents the Discussion from degenerating into result repetition, literature listing, post-hoc theory fitting, or significance-driven storytelling.

### Limitation Architecture

Limitations should be expressed conceptually as:

```text
limitation
      ↓
affected inference
      ↓
likely consequence
```

Generic limitation lists without inferential consequences are discouraged.

### Implication Safeguards

The audit checks whether theoretical, scientific, clinical, educational, organizational, engineering, policy, implementation, safety, economic, and future-research implications remain proportional to the evidence.

It prevents escalation such as:

```text
association
→ treatment recommendation
```

or:

```text
single-context finding
→ universal policy recommendation
```

### Conclusion Safeguards

The Conclusion must:

- answer the research question;
- reflect the actual results;
- preserve uncertainty;
- introduce no new evidence;
- avoid unsupported novelty claims;
- avoid unsupported causal claims;
- avoid recommendations stronger than the validated implications.

### Reference Integrity Audit

The new layer integrates with `reference-integrity-guard` and checks:

- reference existence;
- bibliographic accuracy;
- DOI validity;
- retraction status;
- duplicate references;
- reference mashups;
- claim relevance;
- in-text/reference-list correspondence;
- uncited references;
- citation padding.

Target-journal citation padding and prestige-driven citation strategy remain prohibited.

### Evidence Role Safeguard

The established distinction remains:

```text
Phenomenon / Context
      ↓
Authority-first evidence

Scientific Knowledge / Mechanism / Effect
      ↓
Scopus-first scholarly evidence
```

The manuscript audit checks whether these evidence roles remain appropriately separated.

### Reporting Guideline Audit

Applicable reporting guidelines may include:

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

Each required item may be classified as:

```text
COMPLETE
PARTIAL
MISSING
NOT_APPLICABLE
```

A reporting checklist improves transparency but does not repair a weak study design.

### Ethics and Declaration Audit

The audit checks, when applicable:

- ethics approval;
- approval number;
- informed consent;
- consent waiver;
- trial registration;
- protocol registration;
- privacy;
- funding;
- conflicts of interest;
- CRediT roles;
- data availability;
- code availability;
- AI-use disclosure.

Missing information must remain explicit rather than being invented.

### Table and Figure Audit

Tables and figures are checked for:

- titles;
- numbering;
- labels;
- units;
- denominators;
- reference categories;
- uncertainty;
- abbreviations;
- statistical notation;
- consistency with manuscript text.

Potentially misleading graphical practices such as truncated axes, inconsistent scales, selective panels, or omitted groups are flagged.

### Internal Consistency Matrices

The audit supports structured traceability including:

```text
Research Question
→ Method
→ Result
→ Discussion
→ Conclusion
```

and:

```text
Planned Analysis
→ Methods
→ Reported Result
→ Interpretation
```

as well as cross-section consistency checks for sample sizes, effect estimates, confidence intervals, p-values, group definitions, and timepoints.

### Claim-Evidence Audit

Claims may be classified as:

- `SUPPORTED_STRONG`
- `SUPPORTED_MODERATE`
- `SUPPORTED_TENTATIVE`
- `PARTIALLY_SUPPORTED`
- `UNSUPPORTED`
- `CONTRADICTED`

The audit detects claim escalation such as:

```text
association
→ causation
```

```text
prediction
→ explanation
```

```text
laboratory effect
→ clinical efficacy
```

```text
statistical significance
→ practical recommendation
```

### Submission Readiness Decisions

Possible outcomes include:

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

A polished manuscript is not considered submission-ready while critical scientific issues remain unresolved.

### Upstream Revision Routing

When necessary, the audit can route back to:

```text
research-question-builder
methodology-architect
analysis-planner
statistical-method-selector
result-interpreter
scientific-discussion
implication-builder
gap-validator
novelty-auditor
source-verification
reference-integrity-guard
manuscript-architect
manuscript-writer
```

This prevents downstream publication preparation from silently repairing scientific problems at the wrong stage.

### Audit Version Awareness

Scientific audit should normally precede reviewer simulation.

However, audit repetition is not required when the **same manuscript version** has already passed audit and no material scientific change has occurred.

Conceptually:

```text
Reviewer Simulation Request
        ↓
Audit Status Check
        │
        ├── not audited / materially revised
        │        ↓
        │ manuscript-auditor
        │        ↓
        │ reviewer-simulator
        │
        └── same version already passed audit
                 ↓
          reviewer-simulator
```

This prevents both unsafe audit bypass and unnecessary repeated auditing.

### `research-intake` Integration

Existing-manuscript routing was expanded to recognize manuscript audit as a version-aware scientific gate.

Scientific audit:

```text
scientific audit needed
      ↓
manuscript-auditor
```

Submission preparation:

```text
manuscript-auditor
      ↓
journal-matcher
```

Reviewer simulation now checks audit status before routing.

### `research-router` Integration

Existing Stage 12 routing was verified as already recognizing:

```text
## Stage 12 — Manuscript Audit
```

with:

```text
manuscript-auditor
      ↓
reviewer-simulator
```

No unnecessary router rewrite was introduced.

### Manuscript Audit vs Reviewer Simulation

```text
manuscript-auditor
```

asks:

> Is the manuscript scientifically defensible and sufficiently complete?

while:

```text
reviewer-simulator
```

asks:

> How might a critical external reviewer challenge this manuscript?

Scientific audit should normally precede adversarial reviewer simulation.

### Manuscript Audit vs Journal Matching

`manuscript-auditor` evaluates scientific and reporting readiness.

`journal-matcher` evaluates where the scientifically stable manuscript belongs.

Journal selection must not compensate for scientific weakness.

### Manuscript Audit vs Manuscript Writing

`manuscript-writer` produces or revises prose.

`manuscript-auditor` evaluates scientific integrity and publication readiness.

Audit findings should route writing-only problems back to `manuscript-writer` rather than silently rewriting the manuscript.

### Framework Progression

```text
Evidence Discovery & Verification
      ↓
Scientific Positioning
      ↓
Research Logic & Framework
      ↓
Methodology & Study Design
      ↓
Analysis Planning & Method Selection
      ↓
Results Interpretation
      ↓
Scientific Discussion
      ↓
Implication Building
      ↓
Manuscript Architecture
      ↓
Manuscript Writing
      ↓
Manuscript Audit & Publication Readiness
      ↓
Journal Matching
      ↓
Reviewer Simulation
      ↓
Reviewer Response
```

This release establishes a formal scientific quality gate between manuscript writing and publication strategy, ensuring that journal targeting, reviewer simulation, and submission preparation occur only after the manuscript's scientific integrity, reporting completeness, internal consistency, reference integrity, and claim boundaries have been adequately secured.

---

## [0.10.0] - Manuscript Development Layer

### Added

- `manuscript-architect` skill for converting scientifically stable research into a complete manuscript blueprint before prose drafting begins, including article-type selection, reporting-guideline alignment, scientific narrative structure, claim hierarchy, section objectives, evidence placement, citation roles, table and figure strategy, supplementary-material planning, word-budget allocation, journal-aware constraints, and manuscript-writer handoff.
- `manuscript-writer` skill for translating an approved manuscript architecture into clear, coherent, publication-ready scientific prose while preserving the research question, methods, numerical results, uncertainty, novelty boundaries, causal status, limitations, and approved implications.
- Explicit manuscript-writing modes covering new manuscript drafting, section writing, continuation of incomplete manuscripts, controlled rewriting, compression, expansion, scientific translation, coherence improvement, abstract writing, title writing, and journal adaptation.
- Manuscript readiness gates preventing prose generation when scientific architecture, results, interpretation, references, or reporting requirements remain materially unresolved.

### Manuscript Development Architecture

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
```

### Architecture-before-Writing Safeguard

The manuscript workflow now explicitly separates:

```text
manuscript-architect
      ↓
determines WHAT must be communicated,
WHERE it belongs,
WHY it belongs there,
and in WHAT order
      ↓
manuscript-writer
      ↓
determines HOW the approved science
is expressed as manuscript prose
```

Full scientific writing must not silently redesign the manuscript architecture.

### Scientific Fidelity Safeguards

- Prevents manuscript writing from silently changing research questions, hypotheses, methods, outcomes, group definitions, analyses, numerical results, or interpretation.
- Prevents exploratory findings from being rewritten as confirmatory findings.
- Prevents associational findings from being escalated into unsupported causal claims.
- Preserves null, contradictory, negative, and context-specific findings.
- Requires primary outcomes and prespecified hypotheses to retain their scientific priority.
- Prevents polished prose from concealing unresolved scientific inconsistencies.
- Prevents journal preferences, word limits, editorial strategy, or publication pressure from redefining the scientific record.

### Reference Integrity Safeguards

- Prohibits fabricated authors, article titles, journals, years, DOIs, PMIDs, URLs, or other bibliographic details.
- Requires references to remain claim-relevant.
- Allows explicit `[CITATION NEEDED]` placeholders when supporting evidence has not yet been verified.
- Prevents target-journal citation padding.
- Keeps APC status independent from scientific evidence selection.
- Preserves the existing source-verification and reference-integrity architecture.

### Manuscript Section Architecture

The new layer supports scientifically distinct writing logic for:

- Title
- Abstract
- Keywords
- Introduction
- Methods
- Results
- Discussion
- Conclusion
- Declarations
- Tables
- Figures
- Supplementary Materials

The default empirical logic remains:

```text
Introduction
→ Why was the study needed?

Methods
→ How was the question answered?

Results
→ What was observed?

Discussion
→ What does it mean?

Conclusion
→ What is the bounded take-home message?
```

Alternative article structures remain available when IMRAD is not scientifically appropriate.

### Introduction Safeguards

- Preserves the sequence from phenomenon and current knowledge to validated gap, audited novelty, and research objective.
- Distinguishes authority-first phenomenon evidence from Scopus-first scholarly evidence.
- Prevents literature accumulation from replacing scientific argument.
- Prevents unverified claims that a study is the “first” or entirely unprecedented.

### Methods Safeguards

- Requires Methods to describe what was actually done rather than retrospectively idealizing the study.
- Preserves study-design naming, sampling logic, measurement architecture, intervention or exposure definitions, analytical methods, and ethics information.
- Keeps statistical methodology conceptually prior to software reporting.
- Supports discipline-specific structures for quantitative, qualitative, mixed-method, laboratory, pharmacokinetic, pharmacogenetic, systematic-review, and meta-analytic studies.

### Results Safeguards

- Organizes Results according to research questions, prespecified outcomes, and analysis logic rather than software-output order.
- Gives primary results explicit priority.
- Emphasizes estimates, magnitude, direction, and uncertainty rather than significance alone.
- Requires transparent reporting of null and inconclusive primary findings.
- Clearly labels exploratory and post-hoc analyses.

### Discussion Safeguards

- Uses the scientific position already established by `scientific-discussion`.
- Prioritizes comparison with the closest relevant evidence.
- Preserves contradictory evidence.
- Calibrates theoretical and mechanistic interpretation to evidence strength.
- Prevents discussion sections from degenerating into literature lists or significance-driven storytelling.

### Implication and Conclusion Safeguards

- Uses implications already bounded by `implication-builder`.
- Prevents statistical associations from becoming treatment recommendations.
- Prevents narrow studies from becoming universal policy recommendations.
- Prevents new data, mechanisms, references, or claims from appearing for the first time in the Conclusion.
- Requires the Abstract conclusion to remain no stronger than the full manuscript conclusion.

### Journal-Aware but Science-Preserving Writing

Journal requirements may influence:

- word limits;
- abstract format;
- headings;
- reference style;
- table and figure limits;
- supplementary-material placement;
- declaration format.

They must not influence:

- scientific results;
- novelty;
- causal interpretation;
- effect magnitude;
- conclusion strength.

The governing hierarchy remains:

```text
Scientific Integrity
      >
Reporting Completeness
      >
Journal Requirements
      >
Stylistic Preference
```

### Existing Manuscript Routing

`research-intake` was expanded so an existing manuscript is no longer routed automatically to scientific audit.

Routing now follows the actual goal:

```text
Existing Manuscript
        │
        ├── structure unclear
        │        ↓
        │ manuscript-architect
        │        ↓
        │ manuscript-writer
        │
        ├── structure stable, writing needed
        │        ↓
        │ manuscript-writer
        │
        ├── scientific audit needed
        │        ↓
        │ manuscript-auditor
        │
        ├── journal selection needed
        │        ↓
        │ journal-matcher
        │
        ├── submission preparation
        │        ↓
        │ manuscript-auditor
        │        ↓
        │ journal-matcher
        │
        └── reviewer simulation
                 ↓
          reviewer-simulator
```

### Integration

Existing `research-router` Stage 10 routing was verified as already consistent with:

```text
manuscript-architect
      ↓
manuscript-writer
```

No unnecessary routing changes were introduced there.

### Framework Progression

```text
Evidence Discovery & Verification
      ↓
Scientific Positioning
      ↓
Research Logic & Framework
      ↓
Methodology & Study Design
      ↓
Analysis Planning & Method Selection
      ↓
Results Interpretation
      ↓
Scientific Discussion
      ↓
Implication Building
      ↓
Manuscript Architecture
      ↓
Manuscript Writing
      ↓
Manuscript Audit & Publication Readiness
```

This release establishes a science-preserving bridge from completed research interpretation to structured manuscript development while ensuring that publication-oriented writing cannot silently redefine the underlying scientific record.

---


## [0.9.0] - Results Interpretation & Scientific Discussion Layer

### Added

- `result-interpreter` skill for translating completed analytical outputs into scientifically defensible findings while preserving effect magnitude, uncertainty, robustness, study-design boundaries, causal limits, hypothesis status, theory relationships, contradictions, and unsupported-claim safeguards.
- `scientific-discussion` skill for positioning interpreted findings against verified scholarly evidence, current State of the Art, closest competitor studies, theory, mechanisms, competing explanations, contradictory evidence, context, boundary conditions, limitations, and the study's validated scientific contribution.
- `implication-builder` skill for translating scientifically discussed findings into evidence-proportionate theoretical, scientific, mechanistic, methodological, measurement, practical, clinical, educational, organizational, engineering, policy, implementation, equity, safety, economic, and future-research implications.

### Interpretation Safeguards

- Separates statistical significance from scientific importance.
- Prevents non-significant findings from being automatically interpreted as evidence of no effect.
- Requires magnitude, uncertainty, robustness, practical meaning, and study-design boundaries to be considered before conclusions are formed.
- Prevents unsupported causal escalation from association to mechanism, intervention, recommendation, or policy.
- Distinguishes confirmatory, exploratory, post-hoc, and incidental findings.
- Preserves contradictory, unexpected, negative, and context-specific findings rather than forcing a preferred narrative.
- Prevents software labels, fit indices, path significance, or familiar reporting conventions from determining scientific conclusions.

### Scientific Discussion Safeguards

- Requires discussion to begin from defensibly interpreted findings rather than raw analytical output.
- Uses verified scholarly evidence and State-of-the-Art positioning rather than citation accumulation.
- Prioritizes closest direct comparators, high-quality evidence, relevant syntheses, seminal explanatory work, and credible contradictory evidence.
- Distinguishes convergence, extension, refinement, contradiction, mixed evidence, and absence of close comparators.
- Requires theory and mechanism claims to be calibrated as directly tested, indirectly supported, plausible, speculative, or unsupported.
- Prevents post-hoc theory fitting, target-journal citation padding, and prestige-based evidence selection.
- Maintains Scopus-first scholarly evidence principles while preserving source-verification and reference-integrity safeguards.

### Implication Safeguards

- Enforces the principle that implication strength must never exceed evidence strength.
- Separates scientific implications from practical recommendations, clinical adoption, policy change, and implementation readiness.
- Requires explicit consideration of feasibility, boundary conditions, harms, equity, costs, implementation context, and uncertainty before action recommendations are made.
- Prevents laboratory findings from being translated directly into clinical recommendations.
- Prevents observational associations from being translated directly into intervention or policy mandates.
- Prevents predictive performance from being treated automatically as clinical utility.
- Allows `Current practice should not change yet` to remain a scientifically valid implication.
- Converts unresolved uncertainty into specific future-research requirements rather than generic calls for larger studies.

### Results-to-Implications Architecture

```text
Completed Analysis
      ↓
result-interpreter
      ↓
Scientifically Defensible Finding
      ↓
scientific-discussion
      ↓
Evidence-Positioned Scientific Meaning
      ↓
implication-builder
      ↓
Bounded Scientific / Practical / Policy / Future-Research Implications
```

The complete downstream logic is:

```text
Research Question
      ↓
Methodology & Study Design
      ↓
Analysis Planning & Method Selection
      ↓
Results Interpretation
      ↓
Scientific Discussion
      ↓
Implication Building
      ↓
Manuscript Development
```

### Integration

Existing routing compatibility was verified for:

- `research-router`, which already routes results through:

```text
result-interpreter
      ↓
scientific-discussion
      ↓
implication-builder
```

- `research-intake`, which already routes existing analytical results to:

```text
research_entry_mode: RESULT_INTERPRETATION
      ↓
result-interpreter
```

No unnecessary routing changes were introduced.

---


## [0.8.0] - Analysis Planning & Method Selection Layer

### Added

- `analysis-planner` skill for translating a design-ready study into a complete analysis architecture before any specific statistical, qualitative, mixed-method, meta-analytic, or software choice is made.
- `statistical-method-selector` skill for selecting scientifically appropriate quantitative statistical methods from the estimand, study design, outcome type, dependency structure, measurement architecture, and intended inference rather than from software menus, normality tests, p-value chasing, or sample-size folklore.
- `qualitative-analysis` skill for planning and conducting context-sensitive qualitative analysis across thematic, framework, content, grounded-theory, phenomenological, narrative, discourse, case-based, and other design-consistent approaches while preserving reflexivity, negative cases, audit trails, and trustworthiness.
- `mixed-method-analysis` skill for explicitly integrating quantitative and qualitative evidence through connecting, building, merging, embedding, case linkage, data transformation, joint displays, discordance analysis, and meta-inference rather than treating mixed methods as two parallel analyses.
- `meta-analysis` skill for determining whether quantitative evidence pooling is scientifically justified and, when appropriate, specifying effect measures, dependency handling, heterogeneity models, prediction intervals, subgroup and meta-regression analyses, sensitivity analyses, risk-of-bias integration, and small-study-effect diagnostics.
- Explicit separation between analysis architecture, statistical-method selection, qualitative interpretation, mixed-method integration, and quantitative evidence pooling.
- Estimand-before-estimator, design-before-model, and method-before-software safeguards across the analysis workflow.
- Safeguards against automatic parametric/nonparametric selection from normality tests, significance-driven analysis, inappropriate independence assumptions, software-driven SEM or PLS-SEM selection, forced qualitative quantification, and unjustified meta-analytic pooling.
- Conditional analysis routing supporting quantitative, qualitative, mixed-method, and evidence-synthesis pathways without requiring every study to use every analytical skill.

### Updated

- `research-router` Stage 8 — Data Analysis Planning now explicitly routes through `analysis-planner`, `statistical-method-selector`, `qualitative-analysis`, `mixed-method-analysis`, and `meta-analysis`.
- Quantitative analysis routing now separates analysis planning from specific statistical-method selection and downstream method-specific adapters.
- Qualitative studies now route directly from `analysis-planner` to `qualitative-analysis` rather than through generic analysis labels.
- Mixed-method studies now route through strand-specific quantitative and qualitative analysis before `mixed-method-analysis`, while allowing direct integration when strand analyses already exist.
- Evidence-synthesis workflows now route to `meta-analysis` for an explicit poolability decision, including `NARRATIVE_SYNTHESIS_PREFERRED` when statistical pooling would be scientifically misleading.
- `research-intake` compatibility with the v0.8.0 architecture verified: existing data enter `DATA_ANALYSIS` and route first to `analysis-planner`.

### Analysis Architecture

```text
                         analysis-planner
                               │
             ┌─────────────────┼──────────────────┐
             │                 │                  │
             ▼                 ▼                  ▼
        quantitative       qualitative       mixed-method
             │                 │                  │
             ▼                 ▼          ┌───────┴────────┐
statistical-method-selector  qualitative-  ▼                ▼
             │              analysis   statistical-   qualitative-
             │                         method-selector  analysis
             │                              │                │
             │                              └───────┬────────┘
             │                                      ▼
             │                              mixed-method-analysis
             │
             └──────────────→ method-specific adapter
                              when required

Evidence synthesis requiring a pooling decision:

analysis-planner
      ↓
meta-analysis
      ↓
pool when scientifically justified
or
narrative synthesis when pooling is not justified
```

---

## [0.7.0] - Methodology & Study Design Layer

### Added

- `problem-solving-approach` skill for translating finalized research questions into scientifically justified evidence-generating strategies before detailed methodology is selected.
- `methodology-architect` skill for converting an approved problem-solving approach into the smallest scientifically adequate, ethically defensible, feasible, and reproducible study architecture.
- `protocol-builder` skill for translating approved methodology into version-controlled, auditable, implementation-ready research procedures without silently changing the scientific design.
- `sampling-strategy` skill for connecting target and source populations, sampling frames, unit structures, selection mechanisms, sample-size rationale, clustering, stratification, attrition, representativeness, and feasibility to the intended inference.
- `instrument-design` skill for selecting, adapting, translating, developing, validating, documenting, and quality-controlling questionnaires, scales, interview guides, observation tools, case report forms, laboratory assays, devices, rubrics, extraction forms, and other measurement systems.
- Explicit separation between scientific problem-solving strategy and detailed methodology.
- Method-before-software safeguards preventing statistical packages, SEM, PLS-SEM, machine learning, or familiar analytical tools from defining the research design.
- Design-function classification covering descriptive, estimative, comparative, associational, causal, mechanistic, predictive, diagnostic, prognostic, validation, measurement-development, intervention, implementation, qualitative, mixed-method, evidence-synthesis, formulation, optimization, stability, safety, and performance-oriented research.
- Design-family support for observational, experimental, quasi-experimental, qualitative, mixed-method, systematic-review, scoping-review, meta-analytic, bibliometric, laboratory, pharmaceutical, biomedical, educational, organizational, policy, computational, and implementation research.
- Explicit distinction among unit of observation, unit of analysis, unit of assignment, sampling unit, experimental unit, and unit of inference.
- Pseudoreplication safeguards distinguishing biological, technical, batch, and repeated-measure replication.
- Counterfactual, comparator, temporal-order, randomization, allocation-concealment, blinding, clustering, contamination, fidelity, and bias-control architecture where scientifically relevant.
- Sampling architecture covering probability and non-probability strategies, qualitative information power, complex sampling, cluster and multistage sampling, recruitment, nonresponse, attrition, event-based requirements, and design-effect awareness.
- Sample-size safeguards preventing arbitrary minimum-N rules, unsupported effect sizes, misuse of the PLS-SEM 10-times rule, and confusion between precision, power, event counts, qualitative adequacy, and experimental replication.
- Measurement architecture requiring conceptual definition before operationalization, construct-to-indicator mapping, existing-instrument review before new development, provenance, licensing, adaptation, translation, pilot testing, reliability, validity, responsiveness, invariance, scoring, calibration, measurement-bias control, and versioning.
- Protocol architecture covering screening, eligibility, recruitment, consent, enrollment, allocation, intervention or exposure procedures, comparators, measurement schedules, specimen and laboratory workflows, data capture, quality control, safety, monitoring, deviations, documentation, roles, version control, and closeout.
- Domain-specific methodological safeguards for pharmaceutical formulation, microbiology, pharmacokinetics, pharmacogenetics/pharmacogenomics, diagnostics, prediction models, education, organizational research, policy evaluation, implementation research, and laboratory science.
- Explicit handoffs from study design to `protocol-builder`, `sampling-strategy`, `instrument-design`, and downstream `analysis-planner`.

### Architecture

The Methodology & Study Design Layer follows:

```text
Validated Gap
      ↓
Audited Novelty
      ↓
Research Question
      ↓
Theory / Hypothesis / Conceptual Framework
when scientifically required
      ↓
problem-solving-approach
      ↓
methodology-architect
      │
      ├───────────────┬────────────────┐
      ▼               ▼                ▼
protocol-builder  sampling-strategy  instrument-design
      │               │                │
      └───────────────┴────────────────┘
                      ↓
                 DESIGN READY
                      ↓
                analysis-planner
```

The downstream branches are conditional rather than mandatory in a rigid order. Sampling, protocol, and instrument decisions may be refined iteratively when the study design requires it.

### Functional Responsibilities

`problem-solving-approach`

- Determines what kind of evidence is required to answer the research question.
- Classifies the knowledge function and intended inference before detailed design.
- Compares scientifically defensible candidate approaches and prevents method-first or software-first decisions.

`methodology-architect`

- Converts the approved evidence-generating strategy into a complete study architecture.
- Defines the design function, study design, setting, population, unit structure, intervention or exposure, comparator, outcomes or phenomena, temporal logic, sampling requirements, measurement requirements, validity safeguards, feasibility, ethics, and downstream analysis requirements.

`protocol-builder`

- Operationalizes methodology into reproducible, auditable, version-controlled procedures.
- Preserves design fidelity while specifying implementation flow, quality control, safety, deviations, documentation, and closeout.

`sampling-strategy`

- Defines who, what, or which units should be selected, from where, by what mechanism, and in what quantity.
- Aligns population representation, experimental independence, sample-size logic, clustering, attrition, and feasibility with the intended inference.

`instrument-design`

- Determines how required constructs, outcomes, exposures, experiences, biological measures, laboratory properties, or performance indicators will be measured or elicited.
- Separates construct definition from item writing and supports reuse, adaptation, translation, development, validation, calibration, scoring, and measurement-quality documentation.

### Integration

Existing `research-router` and `research-intake` routing already recognizes the transition into `problem-solving-approach` and `methodology-architect`, so no additional routing patch was required for v0.7.0.

The new layer provides a design-ready handoff to the forthcoming analysis-planning layer.

### Scientific Integrity

The Methodology & Study Design Layer establishes these principles:

- the research question must precede detailed method selection;
- evidence needs must be explicit before choosing a design;
- methodology must not be determined by software availability;
- SEM and PLS-SEM are analytical modeling families, not research designs;
- machine learning is not a methodology by itself;
- causal questions require designs capable of supporting causal inference;
- cross-sectional association must not be presented automatically as causal effect;
- prediction, explanation, diagnosis, validation, and causal inference are distinct scientific tasks;
- mixed methods require explicit integration rather than parallel use of two methods for appearance;
- qualitative sampling follows information needs rather than statistical representativeness;
- probability sampling is not mandatory when population-level estimation is not the intended inference;
- random assignment and representative sampling solve different scientific problems;
- technical replicates do not automatically increase the number of independent experimental units;
- pseudoreplication must be detected before analysis;
- sample-size justification must follow the inferential task rather than arbitrary universal rules;
- the PLS-SEM 10-times rule must not be used as the sole scientific sample-size justification;
- existing validated instruments should be considered before creating new instruments;
- construct definition and content validity precede factor-analytic validation;
- translation alone does not establish cross-cultural validity;
- Cronbach's alpha alone does not establish validity;
- protocol convenience must not silently change the scientific design;
- protocol amendments affecting scientific meaning must be distinguished from administrative edits;
- target-journal preferences, quartile, APC status, and publication strategy must not determine methodology, sampling, protocol, or measurement design.

### Downstream Readiness

The framework can now hand off a complete study-design architecture to:

- `analysis-planner`;
- `statistical-method-selector`;
- quantitative, qualitative, mixed-method, SEM, PLS-SEM, experimental, review, and other method adapters;
- result-interpretation and manuscript-development workflows.

## [0.6.0] - Research Logic & Framework Layer

### Added

- `phenomenon-evidence-builder` skill for discovering, receiving, verifying, extracting, organizing, and contextualizing authoritative real-world evidence supporting the phenomenon behind a research problem.
- `research-question-builder` skill for translating validated gaps and audited novelty into focused, answerable, scientifically aligned research questions and objectives.
- `hypothesis-builder` skill for constructing testable hypotheses only when hypothesis testing is scientifically appropriate.
- `theoretical-framework` skill for identifying, comparing, selecting, adapting, or explicitly declining formal theory when explanatory grounding is required.
- `conceptual-framework` skill for translating finalized research logic into the smallest scientifically adequate study-specific structure of constructs, mechanisms, relationships, boundaries, and temporal logic.
- Authority-first phenomenon-evidence architecture for official statistics, international and national agency data, government datasets, registries, surveillance systems, regulations, policies, institutional reports, and other authoritative real-world sources.
- Explicit separation between phenomenon evidence and scholarly evidence.
- Original-source recovery logic for tracing secondary reporting back to authoritative reports, datasets, regulations, or official producers where possible.
- Phenomenon-evidence verification covering indicator definitions, units, populations, geography, reference periods, publication dates, provenance, data status, and conflicting official sources.
- Explicit distinction between observed, estimated, modeled, projected, target, provisional, final, and revised real-world data.
- Research-question classification covering knowledge function, orientation, maturity, feasibility, answerability, theory need, hypothesis appropriateness, and conceptual-framework need.
- Theory-prerequisite gate for hypothesis development.
- Conditional support for formal theory, middle-range theory, domain-specific theory, mechanistic models, biological pathways, pharmacological models, physical or engineering models, empirical explanatory models, and interpretive lenses.
- Competing-theory, boundary-condition, mechanism, adaptation, falsifiability, and confirmation-bias safeguards.
- Conceptual-framework support for constructs, variables, predictors, outcomes, mediators, moderators, confounders, contextual factors, temporal logic, multilevel structure, experimental pathways, prediction, validation, implementation, qualitative, mixed-method, and review-oriented designs.
- Explicit distinction between theoretical framework and conceptual framework.
- Conditional routing architecture connecting research questions, theory, hypotheses, conceptual frameworks, and methodology.
- Framework-wide safeguard that software does not determine the scientific model.

### Changed

- Updated `research-intake` to detect whether authoritative real-world phenomenon evidence is available, missing, useful, or required before downstream research development.
- Updated `research-router` to distinguish Authority-first phenomenon evidence from Scopus-first scholarly evidence.
- Updated `research-router` with explicit `Research Logic and Framework Routing`.
- Updated `research-router` so theory, hypotheses, and conceptual frameworks are routed conditionally rather than as a mandatory linear sequence.
- Updated downstream logic so theory-dependent hypotheses are grounded before hypothesis construction.
- Clarified that exploratory, qualitative, descriptive, methodological, validation, and other non-confirmatory studies may legitimately proceed without formal hypotheses.
- Clarified that some studies may legitimately proceed without a formal named theory when a defensible mechanism, model, pathway, or non-theoretical explanatory structure is more appropriate.
- Clarified that phenomenon evidence may establish real-world importance but does not by itself prove a scientific research gap, novelty, theory, mechanism, or causal effect.

### Architecture

The Research Logic & Framework Layer now supports two complementary evidence streams:

```text
              RESEARCH PROBLEM
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
PHENOMENON EVIDENCE     SCHOLARLY EVIDENCE
  Authority-first          Scopus-first
          │                     │
          └──────────┬──────────┘
                     ▼
              SCIENTIFIC PROBLEM
                     ↓
                State of Art
                     ↓
              Validated Gap
                     ↓
              Audited Novelty
                     ↓
              Research Question
```

Research logic then follows a conditional architecture:

```text
                research-question-builder
                          │
              ┌───────────┼────────────┐
              │           │            │
              ▼           ▼            ▼
       theory needed   hypothesis    neither
              │        appropriate      │
              ▼           │            │
 theoretical-framework    │            │
              │           │            │
              └──────┬────┘            │
                     ▼                 │
             hypothesis-builder        │
              when appropriate         │
                     │                 │
                     └────────┬────────┘
                              ▼
                    conceptual-framework
                    when useful/required
                              ↓
                    methodology-architect
```

`phenomenon-evidence-builder` remains cross-cutting and may run whenever authoritative real-world evidence is required.

### Functional Responsibilities

`phenomenon-evidence-builder`

- Establishes what is happening in the real world using appropriately authoritative and preferably original sources.

`research-question-builder`

- Translates validated scientific uncertainty and audited novelty into focused, answerable research questions and objectives.

`theoretical-framework`

- Establishes explanatory theory, mechanism, model, pathway, or other appropriate grounding when needed.

`hypothesis-builder`

- Constructs testable hypotheses only when scientifically appropriate and sufficiently grounded.

`conceptual-framework`

- Organizes the study-specific constructs, mechanisms, relationships, boundaries, levels, temporal logic, and hypotheses needed to guide methodology.

`research-intake`

- Detects whether phenomenon evidence and research-logic inputs are already available or still need to be established.

`research-router`

- Routes evidence, research questions, theory, hypotheses, conceptual frameworks, and methodology according to actual scientific need rather than a rigid sequence.

### Scientific Integrity

The Research Logic & Framework Layer establishes these principles:

- real-world importance does not automatically prove a scientific research gap;
- official statistics do not establish scientific novelty by themselves;
- regulations establish legal or policy context but do not prove causal effectiveness;
- policy targets must not be presented as observed outcomes;
- publication date must not be confused with data reference period;
- projections must not be presented as observed facts;
- conflicting official sources must not be silently reconciled;
- scholarly evidence and phenomenon evidence require different source-priority rules;
- Scopus-first applies to scholarly evidence, not every evidence category;
- Authority-first applies to real-world factual evidence;
- hypotheses are not mandatory for every research design;
- theory must not be selected post hoc merely to justify preferred hypotheses;
- formal named theory is not mandatory when another scientifically defensible explanatory structure is more appropriate;
- conceptual frameworks must be study-specific rather than decorative;
- mediators and moderators must not be added merely to increase model complexity;
- statistical software must not define the scientific research model;
- methodology must follow the research question rather than precede it;
- APC status, target-journal preference, and publication strategy must not distort research logic.

### Downstream Readiness

The framework can now hand off a scientifically coherent research logic to:

- `methodology-architect`;
- `protocol-builder`;
- `sampling-strategy`;
- `instrument-design`;
- `analysis-planner`;
- `statistical-method-selector`;
- qualitative, mixed-method, SEM, PLS-SEM, experimental, review, and other method adapters;
- manuscript-development and publication-support workflows.

## [0.5.0] - Scientific Positioning Layer

### Added

- `sota-builder` skill for constructing a defensible current State of the Art from verified and synthesized scholarly evidence.

- `gap-discovery` skill for transforming unresolved scientific conditions into explicit candidate research gaps.

- `gap-validator` skill for adversarially stress-testing candidate gaps against current literature, alternative terminology, adjacent disciplines, citation networks, methodological equivalents, and closest competitor studies.

- `novelty-builder` skill for constructing precise scientific contribution claims from validated gaps and closest existing research.

- `novelty-auditor` skill for stress-testing proposed novelty claims against the strongest verified competitors and current evidence.

- State-of-the-Art architecture distinguishing established knowledge, emerging evidence, contested knowledge, unresolved questions, and active scientific frontiers.

- Explicit research-gap taxonomy covering theoretical, conceptual, empirical, contradiction, mechanistic, methodological, measurement, analytical, validation, population, contextual, temporal, predictive, intervention, implementation, translational, and integration gaps.

- False-gap safeguards against geographic absence, arbitrary variable combinations, mediator/moderator shopping, method-as-gap reasoning, technology-as-gap reasoning, and trend-based gap claims.

- Explicit falsification conditions for candidate research gaps.

- Adversarial gap validation designed to search for evidence that could invalidate, weaken, resolve, or reframe a proposed gap.

- Closest-competitor identification and competitor comparison matrices.

- Gap outcomes including validated, partially validated, reframed, weak, substantially resolved, rejected, and inconclusive.

- Scientific-consequence and researchability assessment for validated gaps.

- Explicit novelty taxonomy covering theoretical, conceptual, mechanistic, empirical, methodological, measurement, analytical, validation, predictive, intervention, implementation, translational, contextual, integrative, and technological contributions.

- Novelty construction based on meaningful scientific advancement relative to the closest existing evidence.

- Mandatory distinction between `WHAT IS NOVEL` and `WHAT IS NOT NOVEL`.

- Novelty-boundary statements to reduce overclaiming.

- Novelty falsification and strongest-competitor stress testing.

- First-study claim safeguards.

- Terminology-reframing and adjacent-discipline novelty audits.

- Duplication, replication, validation, and incremental-contribution classification.

- Novelty threat analysis covering direct duplication, competitor overlap, geographic-only differences, method-only differences, variable-combination-only claims, technology hype, and rapid field change.

- Pre-submission novelty-refresh logic for fast-moving research fields.

- Reviewer-challenge simulation for novelty claims.

### Architecture

The Scientific Positioning Layer follows:

`evidence-synthesis`

→ `sota-builder`

→ `gap-discovery`

→ `gap-validator`

→ `novelty-builder`

→ `novelty-auditor`

### Functional Responsibilities

`evidence-synthesis`

- Determines what the verified evidence collectively shows.

`sota-builder`

- Establishes what is currently known, emerging, contested, unresolved, and scientifically frontier-level.

`gap-discovery`

- Converts selected unresolved conditions into candidate research gaps.

`gap-validator`

- Attempts to disprove, close, weaken, or reframe those gaps before they are accepted.

`novelty-builder`

- Defines the proposed scientific advancement relative to the validated gap and closest competitors.

`novelty-auditor`

- Attempts to disprove or narrow that novelty claim before downstream study design or publication positioning.

### Scientific Integrity

The Scientific Positioning Layer establishes these principles:

- unresolved does not automatically mean research gap;

- absence of literature does not automatically prove a gap;

- one failed search does not validate a gap;

- an author's limitation section does not establish a current gap;

- future-research recommendations must be revalidated against current literature;

- geographic absence alone is weak gap evidence;

- arbitrary variable combinations are not meaningful gaps;

- a different software package is not methodological novelty;

- a trendy technology does not automatically create a scientific gap;

- research gaps must survive active falsification attempts;

- close competitor studies must be disclosed rather than hidden;

- novelty must be defined relative to the strongest existing competitors;

- replication and validation should be described honestly rather than disguised as first discovery;

- incremental novelty can be valuable when scientifically meaningful;

- "first ever" claims require exceptionally strong evidence coverage;

- novelty is not a marketing statement;

- target-journal preferences must not distort gap or novelty claims;

- APC status and journal quartile do not determine scientific novelty.

### Scientific Positioning Pipeline

The framework now supports:

Verified Evidence

→ Evidence Synthesis

→ State of the Art

→ Candidate Gap Discovery

→ Adversarial Gap Validation

→ Proposed Novelty

→ Adversarial Novelty Audit

→ Defensible Scientific Position

### Downstream Readiness

The resulting validated gap and audited novelty can now support:

- research-question development;

- hypothesis development;

- theoretical-framework construction;

- conceptual-framework construction;

- continuation-study selection;

- research-program development;

- research-roadmap development;

- methodology design;

- manuscript positioning.

## [0.4.0] - Evidence & Reference Integrity Layer

### Added

- `citation-chaining` skill for expanding verified scholarly corpora through backward citations, forward citations, related-paper discovery, author lineage, theory lineage, method lineage, replication tracking, contradiction tracking, and closest-competitor discovery.

- `literature-screening` skill for creating transparent and purpose-specific eligible literature corpora using explicit inclusion and exclusion criteria.

- `evidence-synthesis` skill for integrating findings across verified and screened studies into defensible scientific conclusions.

- Backward and forward citation chaining for identifying foundational literature, replications, validations, extensions, critiques, contradictions, and subsequent scientific development.

- Citation genealogy and scientific-lineage mapping.

- False-gap protection through citation-network expansion and terminology-aware literature recovery.

- Screening modes for exploratory research, research landscapes, trends, emerging topics, State of the Art, gap validation, novelty validation, continuation research, systematic review, meta-analysis, methodology, and manuscript support.

- Transparent title, abstract, and full-text screening logic.

- Explicit screening exclusion reasons and duplicate-study controls.

- Shared-dataset awareness to prevent false independent replication.

- Contradictory and negative-result protection during literature screening.

- Evidence synthesis across convergent, contradictory, heterogeneous, mechanistic, contextual, methodological, and temporal patterns.

- Evidence-maturity assessment.

- Evidence-strength assessment.

- Consensus classification.

- Explicit distinction between evidence absence and evidence of no effect.

- Evidence maps linking synthesis claims to supporting and contradictory studies.

- Handoff from narrative synthesis to meta-analysis when quantitative pooling is scientifically appropriate.

### Completed Architecture

The Evidence & Reference Integrity Layer now follows:

`scopus-literature-search`

→ `source-verification`

→ `reference-integrity-guard`

→ `citation-chaining`

→ `literature-screening`

→ `evidence-synthesis`

### Functional Responsibilities

`scopus-literature-search`

- DISCOVER relevant scholarly literature.

`source-verification`

- VERIFY publication identity, metadata, DOI, scholarly status, Scopus status, correction, and retraction information.

`reference-integrity-guard`

- GUARD the relationship between scientific claims, citations, verified sources, and reference-list entries.

`citation-chaining`

- EXPAND the corpus through scientific relationships around verified anchor papers.

`literature-screening`

- SELECT scientifically relevant and eligible evidence.

`evidence-synthesis`

- SYNTHESIZE the included evidence into defensible cross-study scientific conclusions.

### Scientific Integrity

The completed Evidence & Reference Integrity Layer enforces:

- no fabricated references;

- no guessed DOI values;

- no metadata mashups;

- no unsupported Scopus claims;

- no citation padding;

- no target-journal citation manipulation;

- no exclusion of contradictory evidence merely because it conflicts with a preferred interpretation;

- no treatment of publication counts as evidence quality;

- no treatment of journal quartile as study quality;

- no APC-based evidence filtering;

- no confusion between discovered and verified literature;

- no confusion between eligible literature and strong evidence;

- no confusion between evidence absence and evidence of no effect;

- no synthesis from unverified or inadequately screened evidence.

### Evidence Pipeline

The framework now supports the complete evidence flow:

Research Question / Research Direction

→ Scholarly Discovery

→ Source Verification

→ Reference Integrity

→ Citation Expansion

→ Literature Screening

→ Evidence Synthesis

The resulting evidence architecture is ready to support:

- State-of-the-Art development;

- research-gap discovery;

- research-gap validation;

- novelty construction;

- novelty auditing;

- theoretical positioning;

- methodological design;

- scientific discussion;

- manuscript preparation.

## [0.4.0-alpha.1] - Evidence & Reference Integrity Foundation

### Added

- `scopus-literature-search` skill as the primary scholarly literature discovery layer.

- `source-verification` skill for validating scholarly publication identity, metadata, DOI integrity, peer-review status, journal legitimacy, Scopus status, corrections, and retractions.

- `reference-integrity-guard` skill for auditing the complete relationship between scientific claims, in-text citations, verified sources, and reference-list entries.

- Scopus-first literature discovery with fallback support for OpenAlex, Crossref, PubMed, Semantic Scholar, publisher platforms, and discipline-specific scholarly sources.

- Explicit separation between Scopus source-level status and document-level Scopus verification.

- Historical Scopus coverage awareness to prevent incorrect indexing claims for articles published outside a journal's Scopus coverage period.

- Search-query decomposition using concept blocks, synonyms, historical terminology, disciplinary terminology, and terminology drift.

- Dedicated search modes for exploratory research, research landscapes, State of the Art, gap validation, novelty validation, continuation studies, methodology, target-journal context, systematic review, meta-analysis, and manuscript support.

- Mandatory contradictory-evidence and competing-theory search principles to reduce confirmation bias.

- DOI normalization, bibliographic normalization, duplicate detection, and provenance preservation.

- Source-verification tiers covering publication identity, scholarly status, indexing status, and integrity checks.

- Retraction, correction, preprint, conference-paper, and duplicate-publication handling.

- Reference-mashup and citation-hallucination detection.

- Claim-to-source support auditing.

- Claim-strength auditing to prevent causal or universal claims that exceed the underlying evidence.

- In-text citation and reference-list consistency checks.

- Target-journal citation integrity safeguards.

- Citation-padding detection.

- Explicit prohibition of fabricated references, guessed DOI values, unsupported Scopus claims, and "vibe citation."

### Architecture

Evidence and Reference Integrity architecture — foundation:

`scopus-literature-search`

→ `source-verification`

→ `reference-integrity-guard`

Responsibilities are intentionally separated:

- `scopus-literature-search` discovers potentially relevant scholarly records.

- `source-verification` determines whether individual sources are real, traceable, bibliographically consistent, legitimate, and appropriately verified.

- `reference-integrity-guard` determines whether verified sources are used accurately and appropriately to support scientific claims.

### Scientific Integrity

The Evidence Layer establishes the following non-negotiable principles:

- discovered does not mean verified;

- Scopus source status does not automatically prove Scopus document status;

- DOI-like syntax does not prove DOI validity;

- a real source can still be cited incorrectly;

- a relevant title does not prove claim support;

- target-journal citations must remain scientifically relevant;

- APC status must not influence scientific evidence selection;

- journal prestige does not substitute for evidence quality;

- unverified references must not silently enter evidence-dependent scientific claims;

- retracted literature must not support scientific conclusions;

- references must never be assembled from mixed metadata belonging to different publications.

### Status

This is the first development checkpoint of the Evidence & Reference Integrity Layer.

Remaining components planned for v0.4.0:

- `citation-chaining`

- `literature-screening`

- `evidence-synthesis`

## [0.3.0] - Research Discovery Layer

### Added

- `idea-discovery` skill for transforming broad interests, real-world problems, scientific observations, available resources, and strategic priorities into focused candidate research directions.

- `research-landscape` skill for mapping the structure of a research field across themes, concepts, theories, methods, populations, contexts, evidence streams, and scientific maturity.

- `trend-detection` skill for distinguishing meaningful scientific change from simple publication-volume growth.

- `emerging-topic-discovery` skill for identifying genuinely emerging scientific topics, concepts, methods, technologies, interdisciplinary combinations, and early research frontiers.

- Explicit distinction between research ideas, trends, emerging topics, research gaps, and novelty.

- Research maturity mapping from discovery through validation, prediction, intervention, implementation, and translation.

- Preliminary research-direction comparison based on scientific importance, researchability, feasibility, program potential, and evidence needs.

- Multi-signal trend evaluation covering topic growth, methodological shifts, theory changes, population shifts, evidence maturity, technology adoption, interdisciplinary development, saturation, and durability.

- Emerging-topic assessment covering emergence strength, evidence maturity, saturation, durability, hype risk, terminology stability, and long-term research-program potential.

- Strong anti-trend-chasing rules to prevent fashionable technologies, publication growth, geographic absence, or advanced methods from being treated automatically as novelty.

- Explicit requirement that candidate directions and emerging topics proceed to Scopus-first evidence assessment before research-gap or novelty claims are finalized.

### Architecture

New-research discovery architecture:

`research-router`

→ `research-intake`

→ `idea-discovery`

→ `research-landscape`

→ `trend-detection`

→ `emerging-topic-discovery`

→ Scopus-first evidence investigation

The Research Discovery Layer produces candidate scientific directions and emerging-topic signals.

It does not independently declare:

- confirmed research gaps;

- final novelty;

- guaranteed publication potential;

- confirmed journal suitability.

Those decisions require downstream evidence verification and scientific synthesis.

### Scientific Integrity

The discovery layer reinforces these principles:

- trend does not equal research gap;

- emerging topic does not equal novelty;

- publication volume does not equal scientific importance;

- sparse literature does not automatically indicate opportunity;

- new location does not automatically indicate novelty;

- advanced methodology does not automatically indicate scientific contribution;

- fashionable technology does not replace a research problem.

## [0.2.0] - Research Continuation Layer

### Added

* `research-trajectory-mapper` skill for reconstructing the evolution of multiple previous studies across time.

* `continuation-opportunity-finder` skill for generating and prioritizing scientifically defensible next-study opportunities.

* Research trajectory assessment covering themes, research-question evolution, theory, methods, analysis, population, evidence accumulation, and research maturity.

* Research niche and signature research-program detection.

* Research stagnation and trajectory-fragmentation detection.

* Continuation pathway taxonomy covering replication, validation, mechanism, mediation, moderation, longitudinal research, experimentation, methodological advancement, prediction, intervention, implementation, translation, contextual extension, and integrative research.

* Candidate continuation comparison based on scientific importance, validated gap strength, novelty potential, methodological progression, feasibility, research-program coherence, and roadmap value.

* Explicit distinction between historical research opportunities and currently validated continuation opportunities.

* Risk–reward and trade-off assessment for alternative next studies.

* Research capability and collaboration-awareness for continuation planning.

### Changed

* Revised `research-resume` to focus specifically on research-state recovery and continuity rather than duplicating detailed scientific auditing.

* Clarified the division of responsibility between:

  * `research-resume`

  * `prior-research-auditor`

  * `research-trajectory-mapper`

  * `continuation-opportunity-finder`

### Architecture

Research continuation architecture:

`research-router`

→ `research-resume`

→ `prior-research-auditor`

→ `research-trajectory-mapper` when multiple studies exist

→ current literature revalidation

→ `continuation-opportunity-finder`

The continuation layer does not declare final research gaps or novelty before current evidence has been verified.

## [0.1.0] - Initial Architecture

### Added

- Initial plugin repository structure.

- Plugin manifest under `.codex-plugin/plugin.json`.

- `research-router` skill.

- `research-intake` skill.

- `research-resume` skill.

- `prior-research-auditor` skill.

- Scopus-first research principle.

- Evidence-driven gap and novelty policy.

- No-mandatory-APC publication preference.

- Target-journal citation integrity principle.

- Research continuity and previous-study continuation workflow.

### Architecture

Initial research entry architecture:

`research-router`

→ `research-intake` or `research-resume`

→ `prior-research-auditor`

This release establishes the foundation for future research discovery, evidence synthesis, research trajectory mapping, methodology, analysis, manuscript development, and publication-support skills.
