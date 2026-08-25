---

name: research-router

description: Route researchers to the correct research workflow based on their current stage, available materials, goals, and methodological needs. Use when a user wants to start research, continue previous research, develop an idea, validate a gap or novelty, design a study, analyze data, interpret results, prepare a manuscript, select a journal, or respond to reviewers.

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

The router must not force a researcher to restart the research process if valid work has already been completed.

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

* user wants a research roadmap based on earlier work.

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

→ `research-program-builder`

→ `research-roadmap`

Do not assume that limitations or future directions stated in the previous paper remain valid research gaps.

They must be reassessed against current literature.

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

* user asks how to solve the research problem scientifically.

Recommended route:

`problem-solving-approach`

→ `methodology-architect`

Then, as required:

`protocol-builder`

`sampling-strategy`

`instrument-design`

Methodology must follow the research problem and scientific question.

Do not begin by selecting statistical software.

---

## Stage 8 — Data Analysis Planning

Typical signals:

* user has a study design;

* user has collected or will collect data;

* user asks which analysis to use;

* user asks which statistical test is appropriate;

* user asks how qualitative data should be analyzed;

* user asks how quantitative and qualitative findings should be integrated;

* user asks whether evidence from multiple studies should be pooled.

First route to:

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

* user provides tables or figures;

* user asks what findings mean.

Recommended route:

`result-interpreter`

Then:

`scientific-discussion`

→ `implication-builder`

Interpretation must remain proportional to the design and evidence.

Association must not be described as causation unless the design supports causal inference.

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

* evidence-proportional interpretation.

---

## Stage 11 — Journal Selection

Typical signals:

* user asks where to publish;

* user requests Scopus journals;

* user prefers no-APC publication;

* user wants Q1/Q2/Q3/Q4 options.

Recommended route:

`journal-matcher`

→ `no-apc-journal-finder`

→ `target-journal-intelligence`

Selection should consider:

* scope fit;

* Scopus status;

* journal quality;

* publication model;

* mandatory vs optional APC;

* recent relevant articles;

* methodological fit;

* readership;

* manuscript positioning.

Do not select journals based only on quartile.

---

## Stage 12 — Manuscript Audit

Typical signals:

* user uploads a completed manuscript;

* user asks whether it is ready for submission;

* user wants reviewer-style criticism.

Recommended route:

`manuscript-auditor`

→ `reviewer-simulator`

Audit dimensions may include:

* methodological rigor;

* evidence strength;

* novelty strength;

* journal fit;

* reporting compliance;

* reference integrity;

* statistical reporting;

* internal consistency;

* reviewer vulnerability;

* submission readiness.

---

## Stage 13 — Reviewer Response

Typical signals:

* reviewer comments are provided;

* manuscript has received major or minor revision;

* user asks for a response-to-reviewers document.

Route to:

`reviewer-response`

The reviewer response must distinguish:

* changes accepted;

* changes partially accepted;

* changes respectfully disputed;

* manuscript locations where revisions were made;

* evidence supporting any disagreement.

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

→ research program development

→ research roadmap

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

# Research Passport Awareness

When available, use:

`.research/research-passport.yaml`

to understand the current research state.

The router should identify:

* completed stages;

* current stage;

* unresolved issues;

* evidence status;

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

* `REVIEWER\_RESPONSE`

---

# Stop Conditions

Do not proceed to a downstream stage if:

* a claimed research gap is unsupported;

* novelty depends on an unverified gap;

* critical sources cannot be verified;

* research questions and methodology are materially inconsistent;

* the requested statistical method is incompatible with the design;

* a publication claim depends on unverified Scopus or APC status.

Explain the issue and route the user to the stage needed to resolve it.

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

`research-router` succeeds when the researcher can enter the framework from any reasonable research stage and receive the shortest scientifically defensible path toward the next research objective, while correctly distinguishing phenomenon evidence from scholarly evidence, conditionally routing research questions, theory, hypotheses, conceptual frameworks, and methodology, and avoiding unnecessary repetition or premature method selection.
