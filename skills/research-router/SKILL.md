---

name: research-router

description: Route researchers to the correct research workflow based on their current stage, available materials, scientific goals, governance needs, and methodological requirements. Use when a user wants to start research, continue previous research, develop an idea, validate a gap or novelty, build research questions or frameworks, design a study, determine ethics or regulatory requirements, register or preregister a study, govern and audit research data, plan or conduct analysis, assess reproducibility, interpret results, prepare or audit a manuscript, select a journal, simulate peer review, or respond to reviewers.

---

# Research Router

## Purpose

`research-router` is the primary entry point for Universal Research Skills.

Its role is to determine:

1. what the researcher already has;

2. what the researcher is trying to achieve;

3. the research stage currently reached;

4. what evidence or materials are available;

5. which skill or workflow should run next.

The user should not need to know internal skill names.

The router must translate natural-language research requests into the appropriate research workflow.

---

# Core Principles

The router must preserve the following framework-wide principles:

* Universal

* Scopus-first

* Evidence-driven

* Stage-aware

* Resumable

* Reproducible

* User-friendly

* Publication-oriented

* Governance-aware

* Ethics-aware

* Version-aware

* Traceable

* Reproducibility-aware

The router must not force a researcher to restart the research process if valid work has already been completed.

Cross-cutting governance and integrity requirements should be activated only when scientifically or institutionally relevant, but they must not be skipped merely because the user entered the framework at a later stage.

---

# Global Scientific Rules

Apply these rules throughout routing:

1. No novelty without evidence.

2. No research gap without validation.

3. No citation without verification.

4. No claim of Scopus indexing without current verification.

5. No statistical method without methodological justification.

6. No manuscript claim stronger than the supporting evidence.

7. Do not treat a literature summary as a State of the Art.

8. Do not treat "not previously studied in location X" as sufficient novelty by itself.

9. Clearly distinguish:

   * user-provided information;

   * source-derived evidence;

   * analytical inference;

   * external literature evidence.

10. Never fabricate missing research information.

11. Do not treat technical access to participants, data, specimens, software, or platforms as ethical or regulatory permission.

12. Do not treat ethics approval, registration, or preregistration as proof of scientific validity.

13. Do not describe a study as prospectively preregistered when the relevant outcome information or primary analysis had already been observed.

14. Do not proceed with analysis of an actual dataset when source identity, version, transformation history, or data-quality status is materially unresolved.

15. Do not call a dataset "clean" merely because software produces no warnings or because undesirable observations were removed.

16. Do not claim reproducibility merely because code, a repository, a project file, or supplementary material exists.

17. Reviewer or editor requests do not override ethics, consent, privacy, data-use, preregistration, or regulatory constraints.

18. When a material scientific change occurs, preserve version history and reassess all affected downstream stages rather than silently overwriting the prior research record.

---

# Scopus-First Policy

When literature evidence is required, route toward workflows that prioritize:

1. peer-reviewed articles published in active Scopus-indexed journals;

2. the most relevant evidence for the research question;

3. high-quality and methodologically appropriate studies;

4. recent literature while retaining necessary seminal works;

5. articles from prospective target journals when scientifically relevant.

OpenAlex, Crossref, PubMed, Semantic Scholar, publisher platforms, and other scholarly sources may be used for discovery and verification.

A publication must not be described as Scopus-indexed unless its status has been verified.

---

# Publication Strategy Policy

When the workflow reaches journal selection or publication strategy:

Prefer journals that have:

1. strong scope fit;

2. active Scopus indexing;

3. appropriate scientific reputation;

4. suitable quartile or citation performance for the manuscript;

5. no mandatory article processing charge when comparable alternatives exist;

6. subscription or hybrid publication routes that allow publication without mandatory APC where available;

7. recent publication history relevant to the manuscript topic and methodology.

Cost must never override scientific quality or scope fit.

Do not recommend a journal as "no APC" unless the current publication policy has been verified.

Use the following publication-cost statuses when applicable:

* `NO\_MANDATORY\_APC`

* `OPTIONAL\_APC\_HYBRID`

* `MANDATORY\_APC`

* `APC\_UNVERIFIED`

Articles from a target journal may be used to understand and engage with its scholarly conversation only when scientifically relevant.

Never add citations merely to increase the apparent likelihood of acceptance.

---

# Stage Detection

Determine which stage best describes the user's current situation.

## Stage 0 — Unclear Research Need

Typical signals:

* "I want to do research but do not know where to start."

* "Help me find a research topic."

* "I am interested in X but do not know what to study."

* "What research can I do in this field?"

Route to:

`research-intake`

Then, when appropriate:

`idea-discovery`

---

## Stage 1 — New Research Discovery

Typical signals:

* user has a broad research interest;

* user wants new research ideas;

* user wants emerging topics;

* user wants a potentially publishable research direction.

Recommended route:

`research-intake`

→ `idea-discovery`

→ `research-landscape`

→ `trend-detection`

→ `emerging-topic-discovery`

Then continue toward literature and evidence mapping.

---

## Stage 2 — Continuing Previous Research

Typical signals:

* user uploads a previous article;

* user uploads a thesis or dissertation;

* user wants to extend a previous study;

* user asks "what should I study next?";

* user wants a research roadmap based on earlier work;

* user wants to reuse an old dataset or rerun an earlier analysis.

Recommended route:

`research-resume`

→ `prior-research-auditor`

→ `research-trajectory-mapper`

→ `citation-chaining`

→ `scopus-literature-search`

→ `source-verification`

→ `research-landscape`

→ `sota-builder`

→ `gap-discovery`

→ `gap-validator`

→ `continuation-opportunity-finder`

→ `novelty-builder`

→ `novelty-auditor`

→ `research-roadmap`

When continuation depends on old participant permissions, data, specimens, protocols, or analytical files, activate the relevant governance routes conditionally:

* permission, ethics, consent, specimen, regulatory, or sharing uncertainty → `ethics-regulatory-gate`;

* registration, preregistration, amendment, or prior-plan uncertainty → `registration-preregistration-builder`;

* dataset provenance, version, linkage, transformation, access, retention, or sharing uncertainty → `research-data-governance`;

* data-integrity or analysis-readiness uncertainty → `data-quality-auditor`;

* old analytical workflow, result-to-data traceability, rerun, code, environment, or output uncertainty → `reproducibility-auditor`.

Do not assume that limitations or future directions stated in the previous paper remain valid research gaps.

They must be reassessed against current literature.

Do not assume that old ethics approvals, consent scopes, data-use agreements, registrations, or analysis files automatically remain applicable to a new continuation study.

---

## Stage 3 — Literature / State of the Art

Typical signals:

* user already has a research topic;

* user asks for literature;

* user asks for State of the Art;

* user wants to understand current scientific development.

Recommended route:

`scopus-literature-search`

→ `source-verification`

→ `citation-chaining`

→ `literature-screening`

→ `evidence-synthesis`

→ `sota-builder`

---

## Stage 4 — Research Gap

Typical signals:

* user wants to identify a research gap;

* user presents a claimed gap;

* user asks whether a topic has already been studied.

Recommended route:

`sota-builder`

→ `gap-discovery`

→ `gap-validator`

If the user already provides a proposed gap:

Do not automatically accept it.

Route directly to:

`gap-validator`

---

## Stage 5 — Novelty

Typical signals:

* user asks "what is the novelty?";

* user has identified a research gap;

* user wants to position a new study against existing literature.

Recommended route:

`gap-validator`

→ `novelty-builder`

→ `novelty-auditor`

A novelty claim cannot be finalized before the underlying gap has been validated.

---

## Stage 6 — Research Questions and Framework

Typical signals:

* user has a topic, evidence base, and research direction;

* user asks for research questions;

* user asks for hypotheses;

* user asks for a theoretical or conceptual framework.

Recommended routes:

For research questions:

`research-question-builder`

For hypotheses:

`hypothesis-builder`

For theory:

`theoretical-framework`

For conceptual relationships:

`conceptual-framework`

Use combinations when needed.

---

## Stage 7 — Research Design

Typical signals:

* research question already exists;

* user asks how to conduct the study;

* user asks for research methods;

* user asks how to solve the research problem scientifically;

* user asks what must be approved, preregistered, documented, or governed before implementation.

Recommended scientific-design route:

`problem-solving-approach`

→ `methodology-architect`

Then, as required:

`protocol-builder`

`sampling-strategy`

`instrument-design`

Methodology must follow the research problem and scientific question.

Do not begin by selecting statistical software.

### Stage 7 Governance Gates

Before participant recruitment, intervention, specimen collection, restricted-data access, data linkage, external transfer, or other regulated activity, determine whether:

`ethics-regulatory-gate`

is required.

Use `ethics-regulatory-gate` when the study involves, for example:

* human participants;

* identifiable or sensitive data;

* health or genetic data;

* biological materials;

* animals;

* clinical or experimental interventions;

* AI systems interacting with participants or sensitive data;

* biosafety;

* cross-border transfer;

* restricted datasets;

* consent limitations;

* regulatory or institutional uncertainty.

Do not assume low-risk or retrospective research is automatically exempt.

Formal exemption or approval status must come from the competent authority where required.

When prospective specification is scientifically useful or required, route to:

`registration-preregistration-builder`

after the research question and design are sufficiently stable and before the relevant outcome information is observed whenever possible.

Registration and preregistration are not substitutes for ethics approval.

When the study will create, receive, transform, link, retain, share, or archive research data, establish:

`research-data-governance`

before implementation whenever practicable.

The three routes are not a rigid linear chain.

Use conceptually:

```text
                     APPROVED SCIENTIFIC DESIGN
                              │
              ┌───────────────┼────────────────┐
              │               │                │
              ▼               ▼                ▼
 ethics-regulatory-gate   registration-   research-data-
                           preregistration- governance
                           builder
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                      IMPLEMENTATION READY
```

Not every study requires every branch.

---

## Stage 8 — Data Analysis Planning

Typical signals:

* user has a study design;

* user has collected or will collect data;

* user asks which analysis to use;

* user asks which statistical test is appropriate;

* user asks how qualitative data should be analyzed;

* user asks how quantitative and qualitative findings should be integrated;

* user asks whether evidence from multiple studies should be pooled;

* user asks whether an existing dataset is ready for analysis.

### Actual-Data Readiness Gate

When actual data already exist, do not assume that analysis should begin immediately.

First determine whether the dataset has a defensible governed identity.

If source, version, variable meaning, transformations, linkage, access, privacy, or dataset lineage is materially unresolved, route to:

`research-data-governance`

Then, when a governed dataset exists but structural integrity, value validity, duplicates, missingness, derived-variable correctness, outlier provenance, linkage integrity, temporal coherence, or analysis readiness has not been established, route to:

`data-quality-auditor`

Only then proceed to the analytical architecture.

Use conceptually:

```text
ACTUAL DATA AVAILABLE?
        │
   ┌────┴────┐
   │         │
  No        Yes
   │         │
   │   Is governance established?
   │         │
   │    ┌────┴────┐
   │    │         │
   │   No        Yes
   │    │         │
   │    ▼         ▼
   │ research-  Has data quality been audited?
   │ data-         │
   │ governance ┌──┴──┐
   │            │     │
   │           No    Yes
   │            │     │
   │            ▼     │
   │      data-quality-
   │          auditor
   │            │
   └────────────┴──────→ analysis-planner
```

If the user is only planning future analysis and no actual dataset exists, `data-quality-auditor` is not yet required.

A prospective data-governance plan may still be appropriate.

First analytical route:

`analysis-planner`

`analysis-planner` must determine the analytical problem before any specific statistical, qualitative, mixed-method, meta-analytic, or software choice is made.

Use conceptually:

```text
Research Question
      ↓
Intended Inference
      ↓
Study Design
      ↓
Analysis Target / Estimand
      ↓
Data Structure
      ↓
Measurement Structure
      ↓
Assumptions & Design Features
      ↓
Analysis Family
      ↓
Specific Method
      ↓
Software
```

Do not reverse this sequence.

### Quantitative Analysis Routing

When the primary analysis is quantitative:

```text
analysis-planner
      ↓
statistical-method-selector
      ↓
appropriate method adapter
when required
```

`statistical-method-selector` should select the statistical method only after considering:

* estimand or analysis target;

* outcome type;

* predictor, exposure, or intervention structure;

* study design;

* sampling structure;

* repeated measurements;

* clustering;

* matching;

* time structure;

* missing data;

* multiplicity;

* measurement properties;

* causal, explanatory, predictive, diagnostic, validation, or other inferential goal.

Possible downstream method adapters may include:

* sem;

* pls-sem;

* experimental;

* longitudinal;

* multilevel;

* survival-analysis;

* machine-learning;

* diagnostic;

* prediction;

* pharmacokinetic;

* pharmacogenetic;

* other quantitative method-specific adapters.

Do not route directly to SEM, PLS-SEM, regression, machine learning, or statistical software before the analysis architecture is clear.

### Qualitative Analysis Routing

When the primary evidence is qualitative, route to:

```text
analysis-planner
      ↓
qualitative-analysis
```

Typical triggers include:

* interviews;

* focus groups;

* observations;

* field notes;

* documents;

* narratives;

* open-ended responses;

* qualitative process data;

* interpretive or theory-generating questions.

`qualitative-analysis` should determine an analysis orientation appropriate to the research question and qualitative design.

Do not force qualitative evidence through `statistical-method-selector` merely because codes or frequencies can be counted.

### Mixed-Method Analysis Routing

When the study requires integration of quantitative and qualitative evidence, route conceptually as:

```text
                    analysis-planner
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
statistical-method-selector      qualitative-analysis
              │                         │
              └────────────┬────────────┘
                           ▼
                 mixed-method-analysis
```

If strand-specific analyses have already been completed, the router may enter directly at:

`mixed-method-analysis`

Typical mixed-method integration needs include:

* connecting;

* building;

* merging;

* embedding;

* data transformation;

* case linkage;

* joint displays;

* explanatory sequential integration;

* exploratory sequential integration;

* convergent integration;

* discordance analysis;

* meta-inference.

Do not describe a study as analytically integrated mixed methods merely because quantitative and qualitative results appear in the same manuscript.

### Meta-Analysis Routing

When the user has a systematic review, evidence synthesis, or comparable multi-study evidence corpus and asks whether quantitative pooling should be performed, route to:

```text
analysis-planner
      ↓
meta-analysis
```

`meta-analysis` must first determine whether pooling is scientifically justified.

Possible outcomes include:

* `META_ANALYSIS_JUSTIFIED`

* `META_ANALYSIS_POSSIBLE_WITH_LIMITATIONS`

* `NARRATIVE_SYNTHESIS_PREFERRED`

* `META_ANALYSIS_NOT_JUSTIFIED`

Do not force a pooled estimate merely because multiple studies are available.

### Analysis Routing Matrix

| Analysis Need | Preferred Skill |
|---|---|
| What exactly must be analyzed and for what inference? | `analysis-planner` |
| Which quantitative statistical method fits the estimand and design? | `statistical-method-selector` |
| How should qualitative material be interpreted and analyzed? | `qualitative-analysis` |
| How should quantitative and qualitative strands be integrated? | `mixed-method-analysis` |
| Should study-level quantitative evidence be pooled, and how? | `meta-analysis` |

### Conditional Analysis Architecture

Use conceptually:

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
             └───────────────→ method-specific adapter
                               when required

Evidence synthesis requiring a pooling decision:

analysis-planner
      ↓
meta-analysis
      ↓
pool when justified
or
narrative synthesis when pooling is not justified
```

Not every study uses every branch.

### Analysis Planning Safeguards

Do not:

* select a statistical test from a normality test alone;

* treat `p < 0.05` as scientific importance;

* treat non-significance as proof of no effect;

* treat association as causation;

* ignore repeated measurements or clustering;

* treat technical replicates as independent observations;

* select PLS-SEM merely because sample size is small;

* select SEM merely because many variables are available;

* select machine learning merely because the dataset is large;

* force qualitative data into quantitative analysis because coding frequencies exist;

* call parallel quantitative and qualitative analyses mixed methods without integration;

* force meta-analysis when studies are not meaningfully combinable;

* allow SmartPLS, AMOS, SPSS, Jamovi, R, Python, Stata, SAS, NVivo, MAXQDA, RevMan, or other software to determine the scientific analysis.

Analysis must follow the research question, estimand, design, data-generating structure, measurement system, and intended inference.

---

## Stage 9 — Results Available

Typical signals:

* user provides statistical outputs;

* user provides qualitative findings;

* user provides tables or figures;

* user asks what findings mean;

* user asks whether results can be trusted, traced, or rerun.

Recommended route:

`result-interpreter`

Then:

`scientific-discussion`

→ `implication-builder`

Interpretation must remain proportional to the design and evidence.

Association must not be described as causation unless the design supports causal inference.

### Result Integrity Backtracking

Before or during interpretation, backtrack when necessary:

* unclear dataset source, version, or transformation lineage → `research-data-governance`;

* unresolved duplicates, missingness, derived variables, implausible values, outliers, linkage, or data-integrity concerns → `data-quality-auditor`;

* analysis differs materially from the registered or preregistered plan → `registration-preregistration-builder` for amendment/deviation transparency;

* analysis or data use may exceed ethics, consent, authorization, privacy, regulatory, or contractual scope → `ethics-regulatory-gate`;

* result cannot be linked to the analysis dataset, procedure, software environment, output, or manuscript claim → `reproducibility-auditor`.

### Reproducibility Routing

Use:

`reproducibility-auditor`

when the user asks whether:

* the analysis can be rerun;

* the workflow can be reconstructed;

* the correct dataset version was used;

* a table or figure can be regenerated;

* a manuscript value can be traced to output;

* an old analysis can be reproduced;

* a code or repository package is sufficient;

* reviewer-requested reanalysis is reproducible.

Do not require a reproducibility audit before every preliminary interpretation.

Activate it when traceability, reconstruction, rerun, archival, manuscript finalization, reviewer response, or reproducibility claims materially matter.

---

## Stage 10 — Manuscript Development

Typical signals:

* research is complete;

* user asks to write or structure an article;

* user wants an international-journal manuscript.

Recommended route:

`manuscript-architect`

→ `manuscript-writer`

The manuscript should be grounded in:

* verified literature;

* validated novelty;

* actual methods;

* actual results;

* evidence-proportional interpretation;

* actual ethics and regulatory status;

* actual registration or preregistration status;

* governed and auditable data provenance where applicable;

* reproducibility claims that match the available record.

Before strong data-availability, code-availability, preregistration, ethics, or reproducibility statements are written, verify the underlying record through the relevant v0.16.0 skill rather than relying on manuscript wording alone.

When the analytical workflow is mature and manuscript finalization or archival release requires traceability, route to:

`reproducibility-auditor`

before or as part of final scientific audit.

Do not fabricate:

* ethics approval numbers;

* consent status;

* registration identifiers;

* preregistration timing;

* data availability;

* code availability;

* rerun success.

---

## Stage 11 — Journal Selection

Typical signals:

* user asks where to publish;

* user requests Scopus-indexed journals;

* user prefers publication without mandatory APC;

* user wants Q1/Q2/Q3/Q4 options;

* user wants journals compared or ranked;

* user asks whether a journal is currently indexed, discontinued, legitimate, or scientifically suitable.

Before journal matching, determine whether the current manuscript version is scientifically stable.

If the manuscript has not yet passed scientific audit, or if material scientific revisions have occurred since the last audit, route to:

`manuscript-auditor`

→ `journal-matcher`

If the same manuscript version has already passed `manuscript-auditor` with no unresolved submission-blocking issues and no material scientific changes, route directly to:

`journal-matcher`

`journal-matcher` is responsible for:

* scientific scope fit;

* audience fit;

* article-type compatibility;

* methodological fit;

* novelty and evidence-strength fit;

* current Scopus or other indexing verification;

* active versus historical or discontinued coverage;

* quartile and metric context;

* publication model;

* mandatory versus optional APC;

* subscription and hybrid publication routes;

* waiver and other publication-fee verification;

* recent relevant journal content;

* legitimacy and predatory-risk screening;

* manuscript positioning;

* submission sequencing and backup-journal strategy.

Scientific fit must be evaluated before prestige, quartile, APC preference, or publication speed.

Do not select journals based only on quartile, metrics, publisher prestige, keyword similarity, or APC status.

Do not recommend target-journal citation padding.

Do not allow journal selection to redefine the research question, methods, results, novelty, causal status, or scientific conclusion.

After a target journal has been selected and the researcher requests adversarial pre-submission review, route to:

`reviewer-simulator`

---

## Stage 12 — Manuscript Audit

Typical signals:

* user uploads a completed or near-complete manuscript;

* user asks whether the manuscript is scientifically coherent;

* user asks whether it is ready for submission;

* user requests a scientific-integrity, consistency, reporting, reference, methodological, or publication-readiness audit.

Recommended route:

`manuscript-auditor`

Audit dimensions may include:

* scientific integrity;

* methodological fidelity;

* evidence strength;

* claim-evidence alignment;

* result-discussion-conclusion coherence;

* novelty calibration;

* reporting compliance;

* reference integrity;

* statistical reporting;

* ethics and declarations;

* ethics/regulatory scope consistency;

* consent and privacy claims;

* registration/preregistration timing and deviation transparency;

* data-governance traceability;

* data-quality provenance;

* reproducibility and result-to-output traceability;

* tables, figures, and supplementary materials;

* internal consistency;

* submission readiness.

If the manuscript requires correction before publication-oriented work continues, route back to the appropriate upstream skill.

Examples include:

* ethics, consent, regulatory, authorization, or privacy problem → `ethics-regulatory-gate`;

* registration, preregistration, outcome-switching, or undocumented-deviation problem → `registration-preregistration-builder`;

* source-data, version, transformation, linkage, retention, or sharing problem → `research-data-governance`;

* data-integrity or analysis-readiness problem → `data-quality-auditor`;

* result-to-data, result-to-output, environment, rerun, or reproducibility problem → `reproducibility-auditor`.

If the same manuscript version passes `manuscript-auditor` with no unresolved submission-blocking issues, continue according to the researcher's goal:

* journal selection → `journal-matcher`;

* adversarial pre-submission peer-review simulation → `reviewer-simulator`;

* submission preparation → `journal-matcher` and journal-specific adaptation when required.

Do not use reviewer simulation as a substitute for scientific audit.

---

## Stage 13 — Reviewer Simulation

Typical signals:

* user asks for simulated peer review;

* user asks for reviewer-style criticism after scientific audit;

* user asks to simulate Reviewer 1, Reviewer 2, a statistical reviewer, methodological reviewer, or editor;

* user wants adversarial pre-submission review;

* user wants likely major and minor reviewer concerns;

* user wants desk-rejection risk or simulated editorial screening;

* user wants a post-revision re-review.

Before reviewer simulation, determine the status of the current manuscript version.

If the manuscript has not yet passed scientific audit, or if material scientific revisions have occurred since the last audit, route to:

`manuscript-auditor`

→ `reviewer-simulator`

If the same manuscript version has already passed `manuscript-auditor` with no unresolved submission-blocking issues and no material scientific changes since that audit, route directly to:

`reviewer-simulator`

If a target journal has been selected and verified, reviewer simulation may use the journal context produced by:

`journal-matcher`

→ `reviewer-simulator`

Reviewer simulation may assess:

* scientific question and hypothesis alignment;

* theoretical and conceptual coherence;

* study design;

* sampling;

* measurement;

* methodology;

* statistical or qualitative analysis;

* results reporting;

* numerical consistency;

* causal and mechanistic claims;

* discussion and alternative explanations;

* limitations;

* implications;

* novelty and contribution;

* reference integrity;

* reporting-guideline compliance;

* ethics and transparency;

* reproducibility;

* tables, figures, and supplementary materials;

* journal fit when verified journal context is available.

Reviewer comments should be classified as appropriate into:

* `CRITICAL`;

* `MAJOR`;

* `MODERATE`;

* `MINOR`;

* `EDITORIAL`.

Reviewer simulation must clearly distinguish:

```text
SIMULATED REVIEW
≠
ACTUAL JOURNAL PEER REVIEW
```

Do not:

* invent reviewer identities;

* invent reviewer affiliations;

* invent journal policies;

* invent citations or evidence;

* invent acceptance probabilities;

* fabricate scientific defects merely to make the review appear rigorous;

* demand unnecessary experiments;

* force all reviewers to agree;

* equate Q1 journals with harsher scientific standards;

* use target-journal citation padding;

* allow simulated reviewer requests to redefine the study.

When reviewer simulation reveals a genuine scientific problem, route the issue back to the appropriate upstream skill rather than treating it only as a writing problem.

Examples include:

* research-question problem → `research-question-builder`;

* theory problem → `theoretical-framework`;

* conceptual-model problem → `conceptual-framework`;

* methodology problem → `methodology-architect`;

* sampling problem → `sampling-strategy`;

* instrument problem → `instrument-design`;

* analysis problem → `analysis-planner` or `statistical-method-selector`;

* interpretation problem → `result-interpreter`;

* discussion problem → `scientific-discussion`;

* implication problem → `implication-builder`;

* novelty problem → `novelty-auditor`;

* reference-integrity problem → `reference-integrity-guard`;

* manuscript-structure problem → `manuscript-architect`;

* writing problem → `manuscript-writer`;

* journal-fit problem → `journal-matcher`;

* ethics, consent, privacy, approval, or regulatory problem → `ethics-regulatory-gate`;

* preregistration, registration, amendment, or deviation problem → `registration-preregistration-builder`;

* data provenance, versioning, transformation, access, retention, or sharing problem → `research-data-governance`;

* data-integrity or analysis-readiness problem → `data-quality-auditor`;

* rerun, result traceability, code, environment, or reproducibility problem → `reproducibility-auditor`.

Do not route a genuine scientific problem to copyediting or stylistic rewriting.

A simulated reviewer must not recommend actions that bypass participant rights, ethics approval, consent scope, data-use agreements, privacy safeguards, registration history, or regulatory obligations.

After simulated reviewer comments are complete and the researcher wants to prepare responses, revisions, or a point-by-point rebuttal, route to:

`reviewer-response`

---

## Stage 14 — Reviewer Response

Typical signals:

* actual editor or reviewer comments are provided;

* simulated reviewer comments have been completed and the researcher wants to prepare responses or revisions;

* the manuscript has received major revision, minor revision, revise-and-resubmit, reject-and-resubmit, or another revision-oriented editorial decision;

* the user asks for a point-by-point response, rebuttal letter, response matrix, revision letter, second-round response, or resubmission preparation;

* the user wants to determine whether a reviewer request is scientifically valid, partially valid, debatable, unsupported, or requires clarification;

* the user needs to identify whether reviewer criticism requires textual revision, reanalysis, additional analysis, upstream scientific correction, new evidence, or justified disagreement.

Route to:

`reviewer-response`

Before drafting final response language, determine:

* whether the feedback is `ACTUAL_EDITOR_COMMENT`, `ACTUAL_REVIEWER_COMMENT`, `SIMULATED_REVIEWER_COMMENT`, or internal author feedback;

* which manuscript version was reviewed;

* whether the requested revision has actually been completed;

* whether reanalysis or other scientific correction is still required;

* whether journal policy or reporting requirements must be verified;

* whether the response can be finalized without fabricating actions, evidence, or compliance.

Reviewer response must preserve:

```text
ACTUAL JOURNAL REVIEW
≠
SIMULATED REVIEW
```

For each substantive comment, assess as appropriate:

* comment source and stable comment ID;

* scientific type;

* severity;

* scientific validity;

* actionability;

* required manuscript revision;

* evidence needed;

* exact manuscript location of any completed revision;

* response status;

* upstream route when the issue cannot be solved safely within reviewer response.

Possible scientific-validity classifications may include:

* `VALID`;

* `PARTIALLY_VALID`;

* `VALID_BUT_ALREADY_ADDRESSED`;

* `VALID_REQUIRES_REANALYSIS`;

* `VALID_REQUIRES_NEW_DATA`;

* `QUESTION_FOR_CLARIFICATION`;

* `PREFERENCE_NOT_REQUIREMENT`;

* `SCIENTIFICALLY_DEBATABLE`;

* `NOT_SUPPORTED`;

* `REQUIRES_VERIFICATION`.

Possible response statuses may include:

* `NOT_STARTED`;

* `ASSESSING`;

* `UPSTREAM_CORRECTION_REQUIRED`;

* `REVISION_IN_PROGRESS`;

* `REVISION_COMPLETED`;

* `RESPONSE_DRAFTED`;

* `VERIFIED`;

* `READY_FOR_RESUBMISSION`.

Do not finalize statements such as:

* "we reanalyzed the data";

* "we added the requested analysis";

* "we corrected the manuscript";

* "we verified the reference";

* "we complied with the journal requirement";

unless the corresponding action has actually been completed and verified.

When a reviewer reveals a genuine scientific problem, route back to the appropriate upstream skill.

Examples include:

* research-question problem → `research-question-builder`;

* theory problem → `theoretical-framework`;

* conceptual-framework problem → `conceptual-framework`;

* methodology problem → `methodology-architect`;

* protocol problem → `protocol-builder`;

* sampling problem → `sampling-strategy`;

* instrument problem → `instrument-design`;

* quantitative-analysis problem → `analysis-planner` or `statistical-method-selector`;

* qualitative-analysis problem → `qualitative-analysis`;

* mixed-method integration problem → `mixed-method-analysis`;

* meta-analysis problem → `meta-analysis`;

* interpretation problem → `result-interpreter`;

* discussion problem → `scientific-discussion`;

* implication problem → `implication-builder`;

* novelty problem → `novelty-auditor`;

* reference-integrity problem → `reference-integrity-guard`;

* manuscript-structure problem → `manuscript-architect`;

* writing or clarity problem → `manuscript-writer`;

* journal-fit or post-rejection rematching problem → `journal-matcher`;

* ethics, consent, privacy, regulatory, authorization, specimen, or new-participant-scope problem → `ethics-regulatory-gate`;

* registration, preregistration, amendment, deviation, post-hoc, or reviewer-requested-analysis status problem → `registration-preregistration-builder`;

* dataset version, provenance, transformation, linkage, access, sharing, or archival problem → `research-data-governance`;

* data correction, missingness, outlier provenance, duplicate, linkage, derived-variable, or analysis-readiness problem → `data-quality-auditor`;

* rerun, output regeneration, result-to-output linkage, code, software environment, or reproducibility problem → `reproducibility-auditor`.

Do not route a genuine scientific problem only to stylistic rewriting.

When reviewers request conflicting changes:

```text
Reviewer 1 asks A
Reviewer 2 asks not-A
      ↓
Assess Scientific Validity
      ↓
Use Explicit Editorial Guidance When Available
      ↓
Choose the Defensible Resolution
      ↓
Explain It Respectfully to Both Reviewers
```

Do not satisfy conflicting comments mechanically.

If a requested analysis or data element cannot be produced because it was not collected or is not reconstructable:

* do not fabricate it;

* determine whether the current claim can be narrowed;

* state the limitation transparently;

* classify genuinely unavailable new data as `NOT_FEASIBLE_POST_HOC` or equivalent when appropriate.

After material reanalysis or scientific revision, first assess whether the change triggers governance updates.

Use conceptually:

```text
REVIEWER / EDITOR REQUEST
        ↓
Does it change participants, specimens, data use,
privacy, authorization, or regulated procedures?
        │
       Yes
        ↓
ethics-regulatory-gate

Does it change the prespecified plan or add a
post-hoc / exploratory / reviewer-requested analysis?
        │
       Yes
        ↓
registration-preregistration-builder

Does it create or modify a dataset, transformation,
linkage, access condition, or data version?
        │
       Yes
        ↓
research-data-governance
        ↓
data-quality-auditor
when actual data are changed
        ↓
analysis / reanalysis
        ↓
reproducibility-auditor
when traceability or rerun verification is required
```

Then verify cascading consistency across:

```text
Abstract
      ↓
Methods
      ↓
Results
      ↓
Tables / Figures / Supplements
      ↓
Discussion
      ↓
Conclusion
      ↓
Response Letter
```

Do not update the response letter while leaving contradictory values or claims elsewhere in the manuscript.

Before resubmission, use the readiness gate:

```text
All Editor / Reviewer Comments Addressed
      ↓
Critical Scientific Issues Resolved or Transparently Justified
      ↓
Required Revisions Verified
      ↓
References / Tables / Figures / Supplements Synchronized
      ↓
Response Letter Matches Revised Manuscript
      ↓
Relevant Journal Requirements Checked
      ↓
READY_FOR_RESUBMISSION
```

Possible readiness statuses include:

* `NOT_READY`;

* `SCIENTIFIC_CORRECTION_REQUIRED`;

* `REVISION_IN_PROGRESS`;

* `RESPONSE_REVIEW_REQUIRED`;

* `READY_WITH_MINOR_ADMIN_TASKS`;

* `READY_FOR_RESUBMISSION`.

Do not mark the manuscript `READY_FOR_RESUBMISSION` while required reanalysis, revision verification, critical scientific correction, evidence verification, ethics resolution, or essential journal-policy verification remains incomplete.

Reviewer response should be respectful and point-by-point, but scientific accuracy has priority over appeasement.

Do not:

* fabricate reviewer or editor comments;

* fabricate completed revisions;

* fabricate reanalysis or new data;

* fabricate ethics approval;

* fabricate journal policy;

* fabricate citations;

* falsely agree with a reviewer;

* add irrelevant citations to appease reviewers;

* significance-shop or outcome-switch in response to reviewer pressure;

* conceal scientific problems through prose;

* automatically move to another journal when reviewer criticism exposes a genuine scientific flaw.

If rejection is primarily due to scope or journal fit after scientific issues are adequately addressed, route to:

`journal-matcher`

for a new target-journal strategy.

---

# Special Workflow — Previous Article to Research Roadmap

If a user provides one or more previous research outputs and asks for future research directions, prefer this workflow:

Previous Research

→ `research-resume`

→ `prior-research-auditor`

→ `research-trajectory-mapper`

→ current Scopus-first literature search

→ citation chaining

→ current State of the Art

→ gap discovery

→ gap validation

→ continuation opportunities

→ novelty development

→ research roadmap development

Expected outputs may include:

1. Previous Study Reconstruction

2. Current State of the Art

3. Gap Evolution

4. Candidate Next Studies

5. Priority Matrix

6. Recommended Next Study

7. Alternative Studies

8. Research Questions

9. Hypotheses where appropriate

10. Problem-Solving Approach

11. Methodological Recommendation

12. Analysis Strategy

13. Expected Scientific Contribution

14. Publication Strategy

15. Multi-Year Research Roadmap

16. Evidence Map

---

# Routing Behavior

## Rule 1 — Use Existing Materials

If the user provides:

* an article;

* thesis;

* dissertation;

* proposal;

* dataset;

* analysis output;

* manuscript;

* reviewer comments;

treat those materials as evidence of the user's current research stage.

Do not ask the user to repeat information that can be determined from the material.

---

## Rule 2 — Ask Only High-Value Questions

If information is missing, ask only questions that materially change the route.

Prefer a maximum of 1–3 questions at a time.

Do not conduct long intake interviews when the route is already clear.

---

## Rule 3 — Enter at the Correct Stage

Do not send every user through the full workflow.

Examples:

User already has validated RQ:

→ begin near methodology.

User already has data:

→ begin near analysis.

User already has results:

→ begin near interpretation.

User already has manuscript:

→ begin near manuscript audit.

---

## Rule 4 — Allow Backtracking

If a downstream stage reveals a serious upstream problem, return to the necessary stage.

Examples:

Invalid novelty

→ return to gap validation.

Analysis does not match research question

→ return to problem-solving approach or methodology.

Manuscript claims exceed evidence

→ return to result interpretation.

---

## Rule 5 — Preserve Research Continuity

When a Research Passport exists, use it as the primary project-state record.

Do not overwrite established research decisions without identifying:

* what changed;

* why it changed;

* what evidence supports the change.

---

## Rule 6 — Activate Governance Gates Conditionally

Do not force every study through every governance skill.

However, whenever the user enters with actual participants, specimens, data, analyses, manuscripts, reviewer comments, or archival materials, check whether unresolved issues require:

* `ethics-regulatory-gate`;

* `registration-preregistration-builder`;

* `research-data-governance`;

* `data-quality-auditor`;

* `reproducibility-auditor`.

Governance skills are cross-cutting.

They may activate before implementation, during analysis, during manuscript audit, after reviewer requests, or when prior work is resumed.

---

## Rule 7 — Preserve Versioned Change

When a material change occurs, identify:

* the prior version;

* the new version;

* what changed;

* why it changed;

* whether new ethics or regulatory review is needed;

* whether registration or preregistration must be amended or logged as a deviation;

* whether the governed dataset changed;

* whether data quality must be re-audited;

* whether analysis outputs and reproducibility evidence must be regenerated.

Do not silently overwrite old scientific states.

---

## Rule 8 — Separate Permission, Planning, Data Integrity, and Reproducibility

Use conceptually:

```text
ethics-regulatory-gate
= may this activity proceed?

registration-preregistration-builder
= what was planned, when, and what changed?

research-data-governance
= what data exist, where did they come from, what do they mean, and how are they controlled?

data-quality-auditor
= are the actual governed data scientifically coherent and fit for the intended analysis?

reproducibility-auditor
= can the performed analytical record be reconstructed and, where feasible, rerun?
```

Do not treat these skills as interchangeable.

---

# Research Passport Awareness

When available, use:

`.research/research-passport.yaml`

to understand the current research state.

The router should identify:

* completed stages;

* current stage;

* unresolved issues;

* evidence status;

* ethics/regulatory status when applicable;

* registration/preregistration status when applicable;

* research-data-governance status when applicable;

* data-quality status when actual data exist;

* reproducibility status when an analytical record exists;

* next recommended stage.

---

# User-Facing Behavior

Communicate the route in plain language.

Do not expose unnecessary internal architecture.

Instead of:

"Invoking gap-validator then novelty-builder."

Prefer:

"Your research question is already clear, but the claimed gap still needs to be checked against the latest literature. We should validate that first before defining novelty."

When useful, show progress as:

Research Progress

* Completed: Topic definition

* Completed: Initial literature mapping

* Current: Research gap validation

* Next: Novelty development

* Later: Methodology and analysis

---

# Routing Output

When routing a request, internally establish:

* `research\_entry\_mode`

* `current\_stage`

* `available\_materials`

* `completed\_stages`

* `missing\_critical\_information`

* `next\_skill`

* `next\_workflow`

* `evidence\_requirement`

* `ethics\_regulatory\_status`

* `registration\_preregistration\_status`

* `data\_governance\_status`

* `data\_quality\_status`

* `reproducibility\_status`

Possible entry modes include:

* `START\_NEW\_RESEARCH`

* `CONTINUE\_PREVIOUS\_RESEARCH`

* `LITERATURE\_RESEARCH`

* `RESEARCH\_DESIGN`

* `DATA\_ANALYSIS`

* `RESULT\_INTERPRETATION`

* `MANUSCRIPT\_DEVELOPMENT`

* `JOURNAL\_SELECTION`

* `MANUSCRIPT\_REVIEW`

* `REVIEWER\_SIMULATION`

* `REVIEWER\_RESPONSE`

* `ETHICS\_REGULATORY\_REVIEW`

* `REGISTRATION\_PREREGISTRATION`

* `RESEARCH\_DATA\_GOVERNANCE`

* `DATA\_QUALITY\_AUDIT`

* `REPRODUCIBILITY\_AUDIT`

---

# Stop Conditions

Do not proceed to a downstream stage if:

* a claimed research gap is unsupported;

* novelty depends on an unverified gap;

* critical sources cannot be verified;

* research questions and methodology are materially inconsistent;

* the requested statistical method is incompatible with the design;

* a publication claim depends on unverified Scopus or APC status;

* a regulated or ethically sensitive activity appears to require approval, authorization, amendment, consent review, privacy review, biosafety review, animal ethics review, or legal/institutional review that remains unresolved;

* a prospective preregistration claim would be false because relevant outcomes or primary analyses had already been observed;

* actual data cannot be defensibly identified, versioned, or traced to their source;

* material data-quality problems remain unresolved for the intended analysis;

* a strong reproducibility or rerun claim is requested but the analysis dataset, workflow, environment, outputs, or result mapping cannot be reconstructed;

* reviewer-requested changes would exceed approved ethical, consent, regulatory, contractual, or data-use scope.

Explain the issue and route the user to the stage needed to resolve it.

A stop condition is not always a permanent rejection.

It may mean:

`REVISE`

`REQUIRE_APPROVAL`

`REQUIRE_AMENDMENT`

`REQUIRE_DATA_GOVERNANCE`

`REQUIRE_DATA_QUALITY_REVIEW`

`REQUIRE_REPRODUCIBILITY_REPAIR`

or another appropriate upstream action.

---

# Phenomenon Evidence Routing

`research-router` must distinguish between scholarly evidence needs and real-world phenomenon evidence needs.

Use:

`phenomenon-evidence-builder`

when the user needs factual evidence about what is occurring in the real world.

Typical triggers include requests involving:

- official statistics;

- prevalence or incidence;

- burden or magnitude;

- demographic conditions;

- trends over time;

- official datasets;

- surveillance data;

- registries;

- government reports;

- regulations;

- laws;

- policy documents;

- institutional reports;

- service-utilization data;

- economic indicators;

- education statistics;

- environmental indicators;

- market conditions;

- current real-world events;

- credible news used to identify a phenomenon;

- user-uploaded factual reports;

- pasted URLs containing official or contextual evidence.

Examples:

> "Find WHO data showing the magnitude of this problem."

> "Strengthen my research background using BPS data."

> "I uploaded a government report. Use it to support the phenomenon."

> "Use this regulation as part of the research background."

> "This news article reports a statistic. Find the original source."

Route these requests to:

`phenomenon-evidence-builder`

rather than treating them as ordinary scholarly-literature searches.

---

# Scholarly vs Phenomenon Evidence Routing

Use conceptually:

```text

Question:

"What is happening in the real world?"

        ↓

phenomenon-evidence-builder

        ↓

Authority-first evidence

Question:

"What does scientific research know about it?"

        ↓

scopus-literature-search

        ↓

Scopus-first scholarly evidence

```

When both questions are relevant, the two workflows may run in parallel.

Example:

```text

Research Problem

      │

      ├── phenomenon-evidence-builder

      │      ↓

      │  magnitude / trend / burden / policy

      │

      └── scopus-literature-search

             ↓

         scientific knowledge / theory / effect

```

Do not merge their evidence standards.

---

# Phenomenon Evidence Input Detection

If the user provides:

- an uploaded PDF;

- spreadsheet;

- CSV;

- institutional report;

- regulation;

- dataset;

- official dashboard;

- government webpage;

- news URL;

- policy document;

preserve that material as an explicit input to:

`phenomenon-evidence-builder`

when the material is being used to establish real-world facts.

Do not require the user to re-enter information already available in the supplied material.

---

# Original-Source Routing

When the user provides a secondary source such as a news article that attributes facts or statistics to another institution:

route the task toward:

`phenomenon-evidence-builder`

with:

`ORIGINAL\_SOURCE\_RECOVERY`

The preferred route is:

```text

Secondary Source

      ↓

Identify Original Producer

      ↓

Official Report / Dataset / Regulation

      ↓

Verify

      ↓

Use Original Source

```

Do not automatically treat secondary reporting as the strongest evidence.

---

# Authority-First Routing Principle

For real-world factual evidence, prioritize:

`AUTHORITATIVE\_SOURCE\_FIRST`

For scholarly scientific evidence, prioritize:

`SCOPUS\_FIRST`

These principles are complementary.

Do not route:

- regulations;

- official statistics;

- national datasets;

- policy documents;

through Scopus simply because the framework is Scopus-first.

Scopus-first applies to scholarly evidence, not all evidence categories.

---

# Background Construction Routing

When the researcher asks to:

- build a research background;

- strengthen an introduction;

- justify the importance of a problem;

- develop a proposal rationale;

- prepare a grant significance section;

the router should consider whether both evidence streams are needed:

```text

PHENOMENON EVIDENCE

What is happening?

        +

SCHOLARLY EVIDENCE

What does science know?

        ↓

State of the Art

        ↓

Validated Gap

        ↓

Audited Novelty

        ↓

Research Question / Objective

```

Do not build strong background claims from scholarly literature alone when real-world magnitude or policy context is central and authoritative data are reasonably obtainable.

---

# Cross-Cutting Research Governance, Data Integrity, and Reproducibility Routing

The following v0.16.0 skills form a cross-cutting integrity layer:

```text
ethics-regulatory-gate
registration-preregistration-builder
research-data-governance
data-quality-auditor
reproducibility-auditor
```

They are not a new mandatory linear stage.

They activate when the scientific workflow creates a corresponding governance need.

Use conceptually:

```text
                         RESEARCH WORKFLOW
                                │
        ┌───────────────────────┼────────────────────────┐
        │                       │                        │
        ▼                       ▼                        ▼
ETHICS / REGULATORY       REGISTRATION /          DATA GOVERNANCE
      PERMISSION           PREREGISTRATION               │
        │                  & DEVIATIONS                  ▼
        │                       │                  DATA QUALITY
        │                       │                        │
        └───────────────────────┼────────────────────────┘
                                ▼
                         ANALYSIS / RESULTS
                                │
                                ▼
                     REPRODUCIBILITY AUDIT
                                │
                                ▼
               MANUSCRIPT / ARCHIVE / REVIEW / RESUBMISSION
```

The router should activate only the branches required by the study.

---

# Ethics and Regulatory Routing

Use:

`ethics-regulatory-gate`

when the question is essentially:

> May this research activity proceed under the applicable ethical, participant, consent, privacy, institutional, contractual, safety, or regulatory constraints?

Typical triggers include:

- human participants;
- clinical data;
- identifiable data;
- sensitive data;
- genetic data;
- biological specimens;
- animals;
- clinical interventions;
- devices;
- drugs;
- biosafety;
- cross-border transfer;
- AI use involving sensitive research data or participant interaction;
- secondary use;
- data linkage;
- consent uncertainty;
- publication of identifiable material;
- reviewer-requested new data collection or procedures.

Possible outcomes include:

- `PROCEED`;
- `PROCEED_WITH_CONDITIONS`;
- `REVISE_BEFORE_PROCEEDING`;
- `FORMAL_APPROVAL_REQUIRED`;
- `AMENDMENT_REQUIRED`;
- `DATA_USE_AUTHORIZATION_REQUIRED`;
- `PRIVACY_REVIEW_REQUIRED`;
- `REGULATORY_REVIEW_REQUIRED`;
- `BLOCKED_PENDING_RESOLUTION`.

Do not let the router itself fabricate or grant formal approval.

---

# Registration and Preregistration Routing

Use:

`registration-preregistration-builder`

when the question is essentially:

> What should be prospectively specified, registered, preregistered, versioned, amended, or transparently labeled before or after relevant evidence is observed?

Typical triggers include:

- prospective study registration;
- clinical trial registration;
- protocol registration;
- systematic-review registration;
- analysis-plan preregistration;
- registered reports;
- confirmatory hypotheses;
- outcome hierarchy;
- stopping rules;
- planned exclusions;
- analysis flexibility;
- protocol amendments;
- outcome changes;
- reviewer-requested analyses;
- post-hoc analyses;
- planned-vs-implemented comparison.

Preserve:

```text
PREREGISTERED
AMENDED
DEVIATED
EXPLORATORY
POST_HOC
REVIEWER_REQUESTED
```

as distinct scientific statuses.

Do not retroactively relabel a post-hoc decision as prospective preregistration.

---

# Research Data Governance Routing

Use:

`research-data-governance`

when the question is essentially:

> What data exist or will exist, where did they come from, what do the variables mean, what transformations occurred, who may access them, and how are versions, retention, sharing, and provenance controlled?

Typical triggers include:

- source data;
- raw data;
- working data;
- cleaned data;
- linked data;
- derived data;
- analysis-ready data;
- dataset versioning;
- codebooks;
- metadata;
- identifiers;
- transformations;
- access;
- privacy;
- retention;
- archival;
- sharing;
- cross-system linkage;
- old datasets being resumed.

Do not reduce data governance to file naming.

---

# Data Quality Routing

Use:

`data-quality-auditor`

when actual governed data exist and the question is essentially:

> Are these data structurally coherent, semantically consistent, traceable, plausible, and fit for the intended scientific analysis?

Typical triggers include:

- duplicates;
- inconsistent identifiers;
- invalid categories;
- impossible ranges;
- implausible values;
- unit inconsistency;
- temporal inconsistency;
- missingness;
- merge/linkage problems;
- derived-variable problems;
- scoring problems;
- unexpected outliers;
- analysis-readiness uncertainty.

The audit must distinguish:

```text
CONFIRMED ERROR
LEGITIMATE UNUSUAL OBSERVATION
UNRESOLVED ANOMALY
```

Do not treat data quality as cosmetic cleaning.

Do not correct observations merely because an analytical model prefers different values.

---

# Reproducibility Routing

Use:

`reproducibility-auditor`

when the question is essentially:

> Can the research analytical record be reconstructed from source data through transformations, analysis, software environment, outputs, and reported results?

Typical triggers include:

- rerunning an analysis;
- reconstructing old work;
- identifying which dataset produced a result;
- linking manuscript values to outputs;
- regenerating tables or figures;
- checking a GitHub or supplementary reproducibility package;
- software-version uncertainty;
- missing scripts;
- GUI analysis reconstruction;
- reviewer-requested reanalysis;
- archival release;
- reproducibility statements.

Distinguish:

- computational reproducibility;
- analytical reproducibility;
- methodological replicability;
- conceptual replication.

Do not equate availability with reproducibility.

Do not claim a rerun unless it actually occurred.

---

# Governance Routing Matrix

| User Need | Preferred Skill |
|---|---|
| May this activity ethically or regulatorily proceed? | `ethics-regulatory-gate` |
| What was prespecified, amended, exploratory, or post-hoc? | `registration-preregistration-builder` |
| What data exist, where did they come from, and how are they controlled? | `research-data-governance` |
| Are the actual governed data fit for the intended analysis? | `data-quality-auditor` |
| Can the performed analytical workflow and results be reconstructed or rerun? | `reproducibility-auditor` |

---

# Conditional Governance Architecture

Use conceptually:

```text
SCIENTIFIC DESIGN SUFFICIENTLY CLEAR
              │
    ┌─────────┼──────────┐
    │         │          │
    ▼         ▼          ▼
 ethics   registration   data governance
 required? / prereg      required?
    │      useful/required?  │
    │         │          │
    └─────────┼──────────┘
              ▼
          IMPLEMENT
              │
              ▼
        ACTUAL DATA EXIST
              │
              ▼
      research-data-governance
        if not already established
              │
              ▼
       data-quality-auditor
              │
              ▼
           ANALYSIS
              │
              ▼
     reproducibility-auditor
      when reconstruction,
      rerun, finalization,
      archive, or review
      requires it
```

Not every branch is mandatory.

---

# Governance Re-entry After Change

A material change may reactivate earlier gates.

Examples:

```text
NEW PARTICIPANT / PROCEDURE / SPECIMEN / DATA USE
                ↓
       ethics-regulatory-gate

NEW OR CHANGED CONFIRMATORY ANALYSIS
                ↓
registration-preregistration-builder
for amendment / deviation status

NEW DATASET VERSION / LINKAGE / TRANSFORMATION
                ↓
       research-data-governance
                ↓
         data-quality-auditor

NEW FINAL ANALYSIS / REANALYSIS
                ↓
       reproducibility-auditor
when result traceability or rerun verification is needed
```

Do not assume a passed gate remains permanently valid after a material change.

---

# Governance Evidence Separation

The router must preserve these distinctions:

```text
ETHICS APPROVAL
= permission from competent oversight

REGISTRATION / PREREGISTRATION
= transparent prospective or versioned research planning

DATA GOVERNANCE
= provenance, meaning, control, version, access, retention, and sharing

DATA QUALITY
= integrity and fitness of actual data for intended scientific use

REPRODUCIBILITY
= reconstructability and rerun traceability of the analytical record
```

One does not substitute for another.

---

# Governance Safeguards

Do not:

- infer ethics approval from a published article;
- infer consent scope from data possession;
- infer unrestricted reuse from public availability;
- infer anonymity from de-identification alone;
- infer prospective preregistration from a registry entry created after analysis;
- infer data quality from absence of software warnings;
- infer reproducibility from code availability alone;
- expose restricted data merely to satisfy open-science expectations;
- fabricate registration identifiers, approval numbers, consent status, data availability, code availability, or rerun status;
- allow reviewers, journals, funders, or software to override scientific integrity or participant protections.

---

# Research Logic and Framework Routing

When scientific positioning has produced a sufficiently validated gap and defensible novelty, route the researcher toward research logic before methodology.

Preferred transition:

```text
Validated Gap
      +
Audited Novelty
      ↓
research-question-builder
```

Do not route directly from novelty to methodology, statistical analysis, or software selection.

---

# Research Question Routing

Use:

`research-question-builder`

when the researcher needs to:

- formulate research questions;
- refine existing research questions;
- convert a validated gap into a research question;
- formulate research objectives;
- determine the scientific orientation of the question;
- determine what evidence must be generated;
- determine whether hypotheses are appropriate;
- determine whether theoretical or conceptual frameworks are needed.

Research questions should precede detailed method selection.

---

# Hypothesis Routing

Use:

`hypothesis-builder`

only when hypotheses are scientifically appropriate.

Typical cases include:

- confirmatory quantitative research;
- experimental research;
- theory testing;
- mechanism testing;
- mediation;
- moderation;
- explanatory longitudinal research.

Do not automatically generate hypotheses for:

- exploratory qualitative research;
- descriptive research;
- bibliometric mapping;
- many scoping reviews;
- early discovery studies.

---

# Theory Routing

Use:

`theoretical-framework`

when explicit explanatory grounding is required or useful.

Typical triggers include:

- theory selection;
- theory comparison;
- theoretical explanation;
- theory testing;
- mechanism explanation;
- competing theories;
- theoretical boundary conditions;
- theoretical contribution.

Do not force a formal named theory when a legitimate:

- biological mechanism;
- pharmacological model;
- physical principle;
- engineering model;
- empirical explanatory structure;

is more scientifically appropriate.

---

# Theory-Before-Hypothesis Routing

When a hypothesis depends on a theoretical proposition that has not yet been established, prefer:

```text
research-question-builder
        ↓
theoretical-framework
        ↓
hypothesis-builder
```

Do not prefer:

```text
research-question-builder
        ↓
hypothesis-builder
        ↓
search for theory afterward
```

This prevents post-hoc theoretical justification.

---

# Conceptual Framework Routing

Use:

`conceptual-framework`

when the study benefits from explicit organization of:

- constructs;
- variables;
- mechanisms;
- outcomes;
- mediators;
- moderators;
- contextual conditions;
- levels;
- temporal relationships;
- hypotheses.

The conceptual framework should be study-specific.

Do not equate:

`conceptual-framework`

with:

`theoretical-framework`

---

# Theory vs Conceptual Framework Routing

Use conceptually:

```text
THEORETICAL FRAMEWORK
"Why should this phenomenon or relationship occur?"

CONCEPTUAL FRAMEWORK
"How will this particular study organize and investigate
the relevant constructs, mechanisms, boundaries,
and relationships?"
```

A study may require:

- both;
- only a theoretical framework;
- only a conceptual framework;
- neither formal framework;

depending on its scientific purpose.

---

# Research Logic Routing Matrix

| Study Need | Preferred Skill |
|---|---|
| What exactly should the study ask? | `research-question-builder` |
| What should be tested, if confirmatory? | `hypothesis-builder` |
| Why should the phenomenon occur? | `theoretical-framework` |
| How should study-specific constructs be organized? | `conceptual-framework` |
| What is happening in the real world? | `phenomenon-evidence-builder` |

Do not route every study through every skill.

---

# Conditional Research Logic Architecture

Use conceptually:

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

---

# Research Logic Safeguards

Do not:

- force hypotheses before theory when theory is required;
- force theory merely because SEM or PLS-SEM is used;
- force a conceptual framework into every study;
- add mediators or moderators merely to increase model complexity;
- allow SmartPLS, AMOS, SPSS, Jamovi, R, Python, or other software to define the scientific model;
- route to methodology before the research question is sufficiently clear.

---

# Success Criterion

`research-router` succeeds when the researcher can enter the framework from any reasonable research stage and receive the shortest scientifically defensible path toward the next research objective; while correctly distinguishing phenomenon evidence from scholarly evidence; while conditionally routing research questions, theory, hypotheses, conceptual frameworks, methodology, protocol, sampling, measurement, analysis, interpretation, manuscript development, manuscript audit, journal matching, reviewer simulation, and reviewer response; while activating `ethics-regulatory-gate`, `registration-preregistration-builder`, `research-data-governance`, `data-quality-auditor`, and `reproducibility-auditor` whenever their distinct governance functions are scientifically or institutionally relevant without forcing them as a rigid universal sequence; while separating ethical permission from scientific validity, preregistration from ethics approval, data governance from data quality, and reproducibility from mere code or data availability; while preserving version-aware audit gates, amendment and deviation history, data provenance, actual-versus-planned distinctions, and upstream backtracking when genuine scientific problems are discovered; while distinguishing actual journal review from simulated review; while ensuring that reviewer-response claims about revisions, reanalysis, evidence, compliance, ethics, registration, data changes, reproducibility, or manuscript changes are made only after those actions are actually completed and verified; while routing unresolved scientific criticism, ethics or regulatory uncertainty, data-integrity problems, preregistration discrepancies, and reproducibility failures back to the appropriate upstream skill; while preserving consistency across revised datasets, analyses, manuscripts, supplements, archives, and response letters; and while avoiding unnecessary repetition, premature method selection, publication-driven distortion, retroactive preregistration, permission-by-assumption, software-driven data cleaning, simulated-review claims that exceed the available evidence, reviewer appeasement that weakens scientific integrity, fabricated governance status, or premature `READY_FOR_RESUBMISSION` status.
