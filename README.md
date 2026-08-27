# Universal Research Skills

A universal, evidence-driven research workflow for moving from a broad research idea or previous study to a defensible research question, methodology, governance, research execution, monitoring, analysis, manuscript, journal strategy, peer-review simulation, reviewer response, and long-term research roadmap.

Universal Research Skills is designed to support researchers across disciplines without forcing one method, software package, publication model, or disciplinary tradition onto every study.

The framework currently contains **56 modular research skills** that can be entered from different research stages and connected through explicit scientific routing.

---

## Core Principles

The framework is built around several non-negotiable principles:

1. **Science before publication strategy.**
2. **Evidence before claims.**
3. **Research questions before methods and software.**
4. **Validated gaps before novelty claims.**
5. **Audited novelty before strong contribution claims.**
6. **Interpretation before discussion.**
7. **Scientific correction before rebuttal writing.**
8. **Research progression before publication counting.**
9. **Governance before convenience.**
10. **Registration and preregistration must never be confused with ethics approval or scientific validity.**
11. **Data quality must be audited before analytical conclusions are trusted.**
12. **Reproducibility claims require an actually reconstructable research record.**
13. **Uncertainty must remain visible when evidence is incomplete.**
14. **A scientifically valid outcome may be that a gap, novelty claim, hypothesis, roadmap stage, proposed interpretation, dataset, analysis plan, or research activity should be rejected, revised, blocked, or reframed.**
15. **Approved scientific plans must not be silently rewritten during execution.**
16. **Prospective deviation risk must be distinguished from an actual protocol deviation.**
17. **Data-collection activity must not be confused with data validity or analysis readiness.**
18. **Scientific progress must be demonstrated by evidence-state advancement, not by calendar activity, expenditure, meetings, or publication counting.**

---

## Evidence Architecture

Universal Research Skills distinguishes two complementary evidence streams.

### Scholarly Evidence — Scopus-first

Scholarly evidence supports:

- theory;
- mechanisms;
- associations;
- effects;
- methods;
- State of the Art;
- research-gap validation;
- novelty assessment;
- methodology justification;
- scientific interpretation;
- and manuscript claims.

The preferred scholarly workflow is:

```text
scopus-literature-search
        ↓
source-verification
        ↓
reference-integrity-guard
        ↓
citation-chaining
        ↓
literature-screening
        ↓
evidence-synthesis
```

The framework is **Scopus-first**, not Scopus-only. When direct Scopus access is unavailable, appropriate fallback sources may include OpenAlex, Crossref, PubMed, Semantic Scholar, and publisher metadata.

The framework must never claim that a direct Scopus search was performed when it was not.

---

### Phenomenon Evidence — Authority-first

Real-world phenomenon evidence supports:

- magnitude;
- burden;
- prevalence;
- trends;
- distribution;
- policy context;
- regulatory context;
- institutional conditions;
- service conditions;
- population conditions;
- and other factual background claims.

Preferred sources include:

- official statistics;
- government datasets;
- international organizations;
- national agencies;
- surveillance systems;
- registries;
- regulations;
- policy documents;
- institutional reports;
- and original authoritative sources behind credible secondary reporting.

Use:

```text
phenomenon-evidence-builder
```

Phenomenon evidence can establish that a real-world problem is important, but it does **not** by itself prove a scholarly research gap or scientific novelty.

---

## Governance, Data Integrity, and Reproducibility Architecture

Research governance is a **cross-cutting layer**, not a single linear stage.

The five dedicated governance skills are:

```text
ethics-regulatory-gate
registration-preregistration-builder
research-data-governance
data-quality-auditor
reproducibility-auditor
```

A typical governance path may look like this:

```text
SCIENTIFIC QUESTION / STUDY DESIGN
        │
        ├── ethics-regulatory-gate
        │
        ├── registration-preregistration-builder
        │
        └── research-data-governance
                      ↓
                DATA CREATED /
                RECEIVED / LINKED
                      ↓
              data-quality-auditor
                      ↓
                  ANALYSIS
                      ↓
              INTERPRETATION
                      ↓
          reproducibility-auditor
              when warranted
                      ↓
          MANUSCRIPT / REVIEW /
              ARCHIVAL RECORD
```

This layer is conditional rather than mandatory.

It preserves the following distinctions:

```text
ETHICS APPROVAL ≠ SCIENTIFIC VALIDITY
PREREGISTRATION ≠ ETHICS APPROVAL
REGISTRATION ≠ SCIENTIFIC VALIDITY
PUBLIC DATA ≠ UNRESTRICTED USE
DEIDENTIFIED ≠ AUTOMATICALLY ANONYMOUS
CONSENT ≠ UNLIMITED FUTURE USE
DATA GOVERNANCE ≠ DATA QUALITY
DATA QUALITY ≠ DESIRED RESULT
REPRODUCIBILITY ≠ PUBLIC DATA RELEASE
REPRODUCIBILITY ≠ REPLICATION
REGISTERED ≠ IMMUTABLE
DEVIATION ≠ AUTOMATIC MISCONDUCT
EXPLORATORY ≠ CONFIRMATORY
```

Reviewer or editor requests may reactivate these gates when a revision changes participant scope, data use, specimens, linkage, outcomes, confirmatory analysis, dataset structure, privacy exposure, or analytical provenance.

---

## Research Execution and Monitoring Architecture

Once a study is sufficiently designed, governed, and ready to move from planning into implementation, Universal Research Skills uses a dedicated execution layer.

The five execution and monitoring skills are:

```text
research-execution-manager
protocol-adherence-monitor
data-collection-monitor
deviation-risk-monitor
research-progress-auditor
```

Their core relationship is:

```text
APPROVED / GOVERNABLE RESEARCH PLAN
              │
              ▼
   research-execution-manager
              │
      ┌───────┼────────┐
      │       │        │
      ▼       ▼        ▼
protocol-   data-    deviation-
adherence- collection risk-
monitor     monitor   monitor
      │       │        │
      └───────┼────────┘
              ▼
   research-progress-auditor
              │
              ▼
      NEXT DECISION GATE
 PROCEED / REPLAN / AMEND
    PAUSE / STOP / ESCALATE
```

This layer preserves several critical distinctions:

```text
PLANNED EXECUTION ≠ ACTUAL EXECUTION
ACTIVITY ≠ SCIENTIFIC PROGRESS
PROSPECTIVE RISK ≠ ACTUAL DEVIATION
COLLECTED DATA ≠ VALID DATA
DELAYED DATA ≠ MISSING DATA
PROTOCOL VARIATION ≠ MATERIAL VIOLATION
PAUSE ≠ FAILURE
REPLAN ≠ CONCEALMENT
MILESTONE REPORTED COMPLETE ≠ MILESTONE VERIFIED COMPLETE
```

`research-execution-manager` translates an approved and governable study into a traceable implementation architecture.

`protocol-adherence-monitor` evaluates whether actual implementation remains consistent with the current applicable protocol and distinguishes permitted variation, deviation, material violation, amendment, emergency action, and execution drift.

`data-collection-monitor` monitors whether the intended evidence stream is actually being generated or received with sufficient completeness, timing, provenance, continuity, and traceability.

`deviation-risk-monitor` identifies prospective threats before they become actual deviations and supports preventive action, contingency planning, escalation, replanning, pause, or stop decisions.

`research-progress-auditor` evaluates whether the study has genuinely advanced its scientific evidence state rather than merely remaining administratively active.

These skills do not replace the cross-cutting governance layer. Execution problems may reactivate `ethics-regulatory-gate`, `registration-preregistration-builder`, `research-data-governance`, `data-quality-auditor`, `analysis-planner`, or `reproducibility-auditor` whenever scientifically or institutionally required.

---

## End-to-End Research Architecture

A typical full workflow may look like this:

```text
Research Intake / Research Resume
        ↓
Idea Discovery / Previous Research Audit
        ↓
Research Landscape
        ↓
Trend Detection / Emerging Topic Discovery
        ↓
Scholarly Literature Discovery
        ↓
Source Verification
        ↓
Reference Integrity
        ↓
Citation Chaining
        ↓
Literature Screening
        ↓
Evidence Synthesis
        ↓
State of the Art
        ↓
Gap Discovery
        ↓
Gap Validation
        ↓
Novelty Builder
        ↓
Novelty Auditor
        ↓
Research Question
        ↓
Theory / Hypothesis / Conceptual Framework
        ↓
Problem-Solving Approach
        ↓
Methodology Architect
        ↓
Ethics / Regulatory Gate
        ↓
Registration / Preregistration when appropriate
        ↓
Protocol / Sampling / Instrument
        ↓
Analysis Planning when prospectively required
        ↓
Research Data Governance
        ↓
Research Execution Manager
        ↓
Protocol Adherence / Data Collection /
Prospective Deviation-Risk Monitoring
        ↓
Research Progress Audit
        ↓
Data Quality Audit
        ↓
Analysis Planning recheck when needed
        ↓
Statistical / Qualitative / Mixed-Method / Meta-Analysis
        ↓
Result Interpreter
        ↓
Scientific Discussion
        ↓
Implication Builder
        ↓
Research Roadmap
        ↓
Manuscript Architect
        ↓
Manuscript Writer
        ↓
Manuscript Auditor
        ↓
Journal Matcher
        ↓
Reviewer Simulator
        ↓
Reviewer Response
        ↓
Reproducibility Audit when reconstruction, rerun,
archival verification, or major reanalysis requires it
```

This is a **routing map**, not a rigid mandatory pipeline.

A study should use only the skills scientifically, ethically, institutionally, and methodologically required for its current stage and research purpose.

---

## Conditional Research Logic

Research logic is deliberately non-linear.

A finalized research question may require theory, hypotheses, both, or neither.

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
                  problem-solving-approach
                              ↓
                    methodology-architect
```

Examples:

- A theory-driven confirmatory study may use theory before hypothesis construction.
- A mechanistically grounded quantitative study may use hypotheses without a formal named theory.
- Exploratory qualitative studies may not require hypotheses.
- Descriptive, validation, or methodological studies may not require formal theory.
- A conceptual framework should be used only when it adds real study-specific clarity.

---

## Continuation of Previous Research

Researchers do not need to restart from zero when they already have articles, theses, dissertations, reports, datasets, proposals, or previous projects.

The continuation pathway is:

```text
research-resume
      ↓
prior-research-auditor
      ↓
research-trajectory-mapper
      ↓
continuation-opportunity-finder
      ↓
current literature revalidation
      ↓
gap-validator
      ↓
novelty-auditor
      ↓
research-roadmap
```

This pathway distinguishes:

- what previous research actually established;
- what was only interpreted or suggested;
- what remains uncertain;
- what has become outdated;
- what must be checked against current literature;
- and which next studies represent genuine scientific progression.

---

## State of the Art, Gap, and Novelty

The scientific-positioning layer is intentionally adversarial.

```text
evidence-synthesis
        ↓
sota-builder
        ↓
gap-discovery
        ↓
gap-validator
        ↓
novelty-builder
        ↓
novelty-auditor
```

### State of the Art

`sota-builder` distinguishes:

- `ESTABLISHED`;
- `EMERGING`;
- `CONTESTED`;
- `UNRESOLVED`;
- `FRONTIER`.

### Gap Discovery

`gap-discovery` generates **candidate gaps**, not final research-gap claims.

### Gap Validation

`gap-validator` actively tries to weaken or invalidate a proposed gap through:

- current literature;
- terminology expansion;
- closest competitors;
- citation chaining;
- adjacent disciplines;
- methodological equivalents;
- population and context analogues;
- mechanisms;
- replication;
- and validation studies.

Possible outcomes include:

- validated strong gap;
- validated moderate gap;
- partial gap;
- reframed gap;
- weak gap;
- substantially resolved gap;
- rejected gap;
- inconclusive validation.

### Novelty

`novelty-builder` must state both:

- **WHAT IS NOVEL**
- **WHAT IS NOT NOVEL**

`novelty-auditor` then stress-tests the claim against the strongest and closest prior work.

A new location, extra variable, larger sample, new software, or fashionable technology is not automatically meaningful scientific novelty.

---

## Methodology and Analysis Architecture

The framework separates the scientific problem from the method used to investigate it.

```text
research-question-builder
        ↓
problem-solving-approach
        ↓
methodology-architect
        ↓
┌───────────────┬────────────────┬─────────────────┐
│               │                │                 │
protocol-builder sampling-strategy instrument-design
│               │                │
└───────────────┴────────────────┴─────────────────┘
                        ↓
                analysis-planner
                        ↓
     ┌──────────────────┼──────────────────┐
     ▼                  ▼                  ▼
statistical-       qualitative-      mixed-method-
method-selector       analysis          analysis
                        │
                        └──────────┐
                                   ▼
                              meta-analysis
                              when justified
```

The framework explicitly rejects:

- method-first study design;
- software-first model construction;
- p-value chasing;
- arbitrary normality-test decision trees;
- sample-size folklore;
- significance-driven interpretation;
- decorative mediators or moderators;
- and unnecessary analytical complexity.

Software such as SmartPLS, AMOS, SPSS, Jamovi, R, Python, or other tools may implement an analysis, but software must not define the scientific question.

---

## Research Data Governance

`research-data-governance` defines how research data are created, received, named, transformed, protected, versioned, linked, stored, shared, archived, and handed downstream.

It preserves source-data identity, raw-data provenance, transformation history, variable meaning, dataset versions, access permissions, privacy constraints, derived variables, missingness conventions, linkage logic, analysis-ready datasets, retention, archiving, and downstream reconstructability.

A “clean” dataset must never erase the path from source data to inference.

---

## Data Quality Audit

`data-quality-auditor` evaluates governed research data for structural integrity, identifier integrity, coding, numeric ranges, units, temporal coherence, cross-variable consistency, duplicate records, linkage integrity, missingness, derived-variable correctness, scoring, laboratory or instrument plausibility, outlier provenance, and fitness for the intended analysis.

It distinguishes:

```text
CONFIRMED ERROR
LEGITIMATE UNUSUAL OBSERVATION
UNRESOLVED ANOMALY
```

It must not delete, recode, impute, or transform data merely because software prefers a cleaner result.

---

## Ethics and Regulatory Gate

`ethics-regulatory-gate` evaluates whether a proposed, ongoing, revised, reused, shared, or published research activity may proceed.

Depending on the study, it may consider human participants, consent, privacy, identifiability, sensitive data, biological materials, animals, biosafety, AI-assisted research, cross-border transfer, institutional requirements, contractual restrictions, regulatory requirements, and publication ethics.

Possible outcomes include:

```text
PROCEED
PROCEED_WITH_CONDITIONS
REVISE_BEFORE_PROCEEDING
FORMAL_APPROVAL_REQUIRED
AMENDMENT_REQUIRED
INSTITUTIONAL_REVIEW_REQUIRED
REGULATORY_REVIEW_REQUIRED
DATA_USE_AUTHORIZATION_REQUIRED
BLOCKED_PENDING_RESOLUTION
```

The skill does not replace an ethics committee, regulator, legal office, data protection officer, animal ethics committee, biosafety committee, or other competent authority.

---

## Registration and Preregistration

`registration-preregistration-builder` creates and maintains a transparent prospective record of what the researcher intended to do, what was actually done, what changed, when it changed, why it changed, and which analyses remain confirmatory, exploratory, amended, or post-hoc.

It supports, where appropriate, study registration, clinical trial registration, protocol registration, systematic review registration, meta-analysis registration, preregistration, analysis-plan preregistration, secondary-data preregistration, replication preregistration, registered reports, amendment tracking, deviation tracking, and planned-vs-implemented comparison.

It protects against retrospective preregistration, hidden outcome switching, HARKing, undisclosed analytic flexibility, hidden subgroup switching, hidden exclusion changes, and fabricated registration identifiers.

> **Exploration is scientifically legitimate. Mislabeling exploration as prespecified confirmation is the problem.**

---

## Reproducibility Audit

`reproducibility-auditor` evaluates whether a research workflow can be reconstructed from the scientific record.

It distinguishes computational reproducibility, analytical reproducibility, methodological replicability, and conceptual replication.

It may inspect source data, governed transformations, analysis-ready data, code or procedures, software environments, versions, parameters, outputs, reported results, and result-to-data traceability.

The skill must never claim a rerun occurred unless execution or direct verification actually occurred.

Restricted or sensitive data can still support reproducible research through appropriately authorized controlled-access procedures.

---

## Results, Discussion, and Implications

The post-analysis workflow is:

```text
result-interpreter
        ↓
scientific-discussion
        ↓
implication-builder
```

`result-interpreter` asks what the results actually support.

`scientific-discussion` positions those findings against:

- current evidence;
- State of the Art;
- theory;
- mechanisms;
- contradictions;
- alternative explanations;
- context;
- boundary conditions;
- and limitations.

`implication-builder` translates defensible findings into proportionate:

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
- and future-research implications.

Statistical significance alone must never be converted automatically into scientific or practical importance.

---

## Research Roadmap

`research-roadmap` transforms previous research, current evidence, validated uncertainty, audited opportunity, scientific implications, feasibility, and researcher capabilities into a coherent long-term program.

The roadmap is driven by scientific dependency:

```text
Existing Evidence
        ↓
Current State of the Art
        ↓
Validated Uncertainty
        ↓
Audited Scientific Opportunity
        ↓
Feasible Next Study
        ↓
Evidence Generated
        ↓
Decision Gate
        ↓
Next Defensible Study
```

It supports:

- sequential stages;
- parallel workstreams;
- branching pathways;
- decision gates;
- replication;
- validation;
- negative findings;
- revalidation points;
- capability development;
- feasibility constraints;
- risk;
- and stop rules.

A research roadmap is not a publication-count plan.

---

## Manuscript and Publication Architecture

The manuscript workflow is:

```text
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

### Manuscript Architect

Builds the scientific manuscript structure before prose drafting.

### Manuscript Writer

Writes or revises prose without changing the scientific record.

### Manuscript Auditor

Checks scientific coherence, reporting completeness, reference integrity, methods, results, interpretation, novelty, ethics, declarations, and claim calibration.

### Journal Matcher

Identifies scientifically appropriate journals using:

- scope fit;
- article-type compatibility;
- audience relevance;
- method compatibility;
- evidence strength;
- current indexing status;
- publication model;
- editorial requirements;
- and practical constraints.

Journal prestige, quartile, citation potential, or target-journal citation strategy must not override scientific fit.

A preference for journals without mandatory APC may be respected as a publication constraint, but APC status must never distort evidence selection or scientific interpretation.

---

## Reviewer Simulation

`reviewer-simulator` performs rigorous, evidence-grounded pre-submission peer-review simulation.

It supports multiple independent reviewer perspectives followed by editorial synthesis.

The purpose is:

> Simulate criticism to strengthen the manuscript, not to manufacture rejection.

The simulator must not fabricate:

- reviewer identities;
- journal policies;
- citations;
- scientific defects;
- acceptance probabilities;
- or claims that a revision has already occurred.

Actual journal peer review and simulated peer review must remain explicitly distinct.

---

## Reviewer Response

`reviewer-response` converts actual or simulated reviewer and editor comments into a transparent, traceable scientific revision-and-response workflow.

Its central principle is:

> Respond to the science first. Write the rebuttal second.

Reviewer requests may be:

- accepted;
- partially accepted;
- respectfully disputed;
- routed to reanalysis;
- routed to source verification;
- routed to methodology review;
- routed to ethics/regulatory review;
- routed to registration/deviation review;
- routed to data governance or data-quality review;
- routed to reproducibility review;
- or routed to another upstream scientific skill.

A response letter must never claim that:

- an analysis was rerun;
- data were added;
- citations were verified;
- ethics approval exists;
- registration exists;
- a manuscript section was revised;
- reproducibility was demonstrated;
- or a reviewer concern was resolved

unless that action actually occurred and was verified.

---

## Skill Catalog

### Research Entry and Routing

- `research-router`
- `research-intake`
- `research-resume`

### Previous Research and Continuation

- `prior-research-auditor`
- `research-trajectory-mapper`
- `continuation-opportunity-finder`
- `research-roadmap`

### Idea, Landscape, and Emerging Directions

- `idea-discovery`
- `research-landscape`
- `trend-detection`
- `emerging-topic-discovery`

### Scholarly Evidence

- `scopus-literature-search`
- `source-verification`
- `reference-integrity-guard`
- `citation-chaining`
- `literature-screening`
- `evidence-synthesis`

### Real-World Phenomenon Evidence

- `phenomenon-evidence-builder`

### State of the Art, Gap, and Novelty

- `sota-builder`
- `gap-discovery`
- `gap-validator`
- `novelty-builder`
- `novelty-auditor`

### Research Logic and Frameworks

- `research-question-builder`
- `theoretical-framework`
- `hypothesis-builder`
- `conceptual-framework`
- `problem-solving-approach`

### Methodology

- `methodology-architect`
- `protocol-builder`
- `sampling-strategy`
- `instrument-design`

### Research Governance, Data Integrity, and Reproducibility

- `ethics-regulatory-gate`
- `registration-preregistration-builder`
- `research-data-governance`
- `data-quality-auditor`
- `reproducibility-auditor`

### Research Execution and Monitoring

- `research-execution-manager`
- `protocol-adherence-monitor`
- `data-collection-monitor`
- `deviation-risk-monitor`
- `research-progress-auditor`

### Analysis

- `analysis-planner`
- `statistical-method-selector`
- `qualitative-analysis`
- `mixed-method-analysis`
- `meta-analysis`

### Interpretation and Scientific Meaning

- `result-interpreter`
- `scientific-discussion`
- `implication-builder`

### Manuscript and Publication

- `manuscript-architect`
- `manuscript-writer`
- `manuscript-auditor`
- `journal-matcher`
- `reviewer-simulator`
- `reviewer-response`

**Total: 56 skills.**

---

## Routing Philosophy

The framework is designed to support entry from any reasonable research stage.

Examples:

### Starting with only a broad idea

```text
research-intake
      ↓
idea-discovery
      ↓
research-landscape
      ↓
current evidence workflow
```

### Starting with previous research

```text
research-resume
      ↓
prior-research-auditor
      ↓
research-trajectory-mapper
      ↓
continuation-opportunity-finder
```

### Starting with a proposed research gap

```text
gap-validator
      ↓
novelty-builder
      ↓
novelty-auditor
```

### Starting with a study design before data collection

```text
methodology-architect
      ↓
ethics-regulatory-gate
      ↓
registration-preregistration-builder
      when appropriate
      ↓
research-data-governance
```

### Starting with an approved study ready for implementation

```text
research-execution-manager
      ↓
protocol-adherence-monitor /
data-collection-monitor /
deviation-risk-monitor
      as required
      ↓
research-progress-auditor
      ↓
next defensible decision gate
```

### Starting with an active study that is drifting, delayed, or at risk

```text
research-progress-auditor
      ↓
identify whether the issue is:
actual deviation / collection problem /
prospective risk / governance constraint
      ↓
appropriate execution or governance skill
      ↓
verified corrective, preventive,
replan, amendment, pause, or stop decision
```

### Starting with an existing dataset

```text
research-data-governance
      ↓
data-quality-auditor
      ↓
analysis-planner
      ↓
appropriate analysis skill
      ↓
result-interpreter
```

### Starting with a completed analysis

```text
result-interpreter
      ↓
scientific-discussion
      ↓
reproducibility-auditor
      when reconstruction or verification is needed
```

### Starting with a manuscript

```text
manuscript-auditor
      ↓
scientific correction if required
      ↓
journal-matcher
```

### Starting with reviewer comments

```text
reviewer-response
      ↓
appropriate upstream scientific or governance skill
      ↓
verified revision
      ↓
response finalization
```

The shortest scientifically defensible route should be preferred.

---

## Research Integrity Safeguards

Universal Research Skills is designed to prevent:

- fabricated citations;
- fabricated DOI metadata;
- fabricated Scopus status;
- fabricated analyses;
- fabricated reviewer actions;
- fabricated ethics approvals;
- fabricated registration identifiers;
- fabricated reproducibility claims;
- citation padding;
- reference mashups;
- selective evidence inclusion;
- suppression of contradictory evidence;
- post-hoc novelty inflation;
- HARKing;
- outcome switching without disclosure;
- significance chasing;
- result-driven data cleaning;
- unsupported causal escalation;
- method-driven questions;
- software-driven models;
- journal-driven scientific distortion;
- permission-by-assumption;
- retrospective preregistration presented as prospective;
- silent protocol deviation;
- silent protocol rewriting during execution;
- normalization of repeated near-misses;
- fabricated milestone completion;
- fabricated collection completeness;
- deadline-driven scientific shortcuts;
- publication-driven risk downgrading;
- reviewer-driven execution claims that did not actually occur;
- undocumented data transformation;
- and premature claims of readiness.

When the available evidence is insufficient, the framework should say so.

---

## Scopus and Publication Policy

### Scopus-first

For scholarly evidence discovery, prioritize Scopus-indexed literature when available and scientifically relevant.

Scopus status does not replace:

- source verification;
- evidence quality;
- relevance;
- study design appraisal;
- or claim-to-source fit.

### No-Mandatory-APC Preference

When journal selection begins, researchers may prefer journals without mandatory APC.

This preference belongs to **publication strategy**, not evidence selection.

A high-quality scientific source must not be excluded because its journal charges an APC.

---

## Repository Structure

```text
universal-research-skills/
├── .codex-plugin/
│   └── plugin.json
├── skills/
│   ├── <56 modular research skills>/
│   │   └── SKILL.md
├── providers/
├── methods/
├── domains/
├── schemas/
├── templates/
├── scripts/
├── tests/
├── docs/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── LICENSE
```

---

## Using the Framework

A user can begin with any of the following:

- a broad research interest;
- a practical problem;
- a research proposal;
- an article;
- a thesis or dissertation;
- a dataset;
- a literature corpus;
- a research gap;
- a research question;
- a methodology;
- a protocol;
- an ethics or regulatory question;
- a registration or preregistration need;
- a data-governance problem;
- an approved study ready for execution;
- an active data-collection process;
- a protocol-adherence question;
- a prospective deviation risk;
- a research-progress or milestone question;
- a data-quality problem;
- analytical outputs;
- a reproducibility question;
- a manuscript;
- a target journal;
- reviewer comments;
- or a long-term research program.

The framework should first determine what already exists and what is genuinely missing.

It should not force the user to repeat work that has already been completed and remains scientifically valid.

---

## Materials That Can Support the Workflow

Depending on the research stage, users may provide:

- published articles;
- manuscripts;
- theses;
- dissertations;
- proposals;
- protocols;
- ethics approvals;
- consent documents;
- registration records;
- preregistrations;
- reports;
- datasets;
- raw data;
- codebooks;
- transformation logs;
- execution plans;
- milestone registers;
- protocol-adherence records;
- deviation registers;
- near-miss records;
- risk registers;
- preventive-action or CAPA records;
- collection dashboards;
- participant or sample-flow records;
- site-monitoring records;
- collection-closure and reconciliation records;
- progress-audit records;
- analysis scripts;
- spreadsheets;
- statistical outputs;
- regulations;
- policies;
- institutional documents;
- official statistics;
- web links;
- journal author guidelines;
- reviewer comments;
- response letters;
- or research roadmaps.

Uploaded materials should be treated as evidence to be examined, not automatically as correct or current.

---

## Discipline-Agnostic Design

The framework is intended to support research across fields such as:

- health sciences;
- pharmacy;
- biomedical sciences;
- education;
- social sciences;
- management;
- engineering;
- computing;
- environmental research;
- laboratory research;
- qualitative inquiry;
- mixed methods;
- evidence synthesis;
- and other disciplines.

Domain-specific methods may differ, but the core scientific principles remain:

```text
Question
↓
Evidence Need
↓
Appropriate Design
↓
Ethical / Regulatory Feasibility
↓
Transparent Data Governance
↓
Traceable Research Execution
↓
Protocol / Collection / Risk Monitoring
↓
Evidence-Based Progress Audit
↓
Audited Data Quality
↓
Transparent Analysis
↓
Proportionate Interpretation
↓
Reconstructable Scientific Record
↓
Defensible Scientific Claim
```

---

## Contribution

Contributions are welcome.

Before adding or modifying a skill, contributors should preserve:

- evidence integrity;
- explicit routing;
- scientific scope;
- stop conditions where appropriate;
- uncertainty handling;
- cross-skill compatibility;
- governance compatibility;
- execution traceability;
- protocol-version integrity;
- explicit planned-versus-actual distinctions;
- data provenance;
- version traceability;
- and the separation between scientific reasoning and publication strategy.

See `CONTRIBUTING.md` for repository contribution guidance.

---

## Code of Conduct

Participation in this project is governed by `CODE_OF_CONDUCT.md`.

---

## License

See `LICENSE` for licensing terms.

---

## Project Goal

Universal Research Skills aims to make advanced research reasoning reusable, transparent, modular, and accessible without reducing research to templates, software menus, journal tactics, compliance rituals, or automatic claims of novelty.

The framework succeeds when it helps a researcher identify the **next scientifically defensible action** while preserving the integrity of the evidence, the research question, the methods, the participants and permissions, the approved plan, the actual implementation, the protocol and deviation history, the data, the analysis, the interpretation, and the scientific record.
