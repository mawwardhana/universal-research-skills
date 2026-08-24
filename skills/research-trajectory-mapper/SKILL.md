---

name: research-trajectory-mapper
description: Map and evaluate the evolution of a researcher's previous studies across time to identify recurring themes, scientific progression, methodological patterns, research niches, discontinuities, unresolved questions, and opportunities for building a coherent future research program. Use when multiple related studies, publications, theses, projects, grants, or research outputs are available and the researcher wants to understand or develop a long-term research trajectory.
---

# Research Trajectory Mapper

## Purpose

`research-trajectory-mapper` reconstructs the evolution of a researcher's work across multiple studies.

Its role is to determine whether prior research forms:

* a coherent research trajectory;
* an emerging research niche;
* several partially connected themes;
* a repetitive line with limited scientific progression;
* a fragmented portfolio;
* or a mature research program.

The skill must not merely list publications chronologically.

It must identify the scientific progression connecting them.

---

# Core Question

The central question is:

> How has this research evolved, what scientific capabilities and unresolved questions have accumulated, and what future direction would create the strongest coherent research program?

---

# Activation Conditions

Use this skill when:

* multiple related articles are provided;
* a researcher has several studies in one general field;
* a thesis or dissertation has generated subsequent studies;
* the user asks for a multi-year research roadmap;
* the researcher wants to define a research niche;
* several projects need to be integrated into one program;
* a grant agenda or publication trajectory is being planned;
* the user asks whether previous studies are sufficiently connected.

Do not use this skill for a single isolated previous study unless the user is explicitly asking to position it within a broader historical trajectory.

For one previous study, first use:

`prior-research-auditor`

---

# Required Upstream Context

Prefer inputs already processed by:

`research-resume`
→ `prior-research-auditor`

Each previous study should ideally have enough information to identify:

* study identity;
* research problem;
* objective;
* theory or conceptual framework;
* design;
* population/context;
* methods;
* analysis;
* major findings;
* limitations;
* continuation signals;
* research maturity.

Do not invent missing information merely to make the trajectory appear coherent.

---

# Provenance Rule

Maintain distinction among:

* `SOURCE_EXPLICIT`
* `SOURCE_INFERRED`
* `USER_PROVIDED`
* `ANALYTICAL_INFERENCE`
* `EXTERNAL_EVIDENCE`

Research trajectory conclusions are often analytical inferences.

Label them accordingly.

---

# 1. Build the Research Timeline

Arrange previous studies chronologically where possible.

Recommended representation:

```text
Study 1
Year
Problem
Method
Main Finding
Contribution
        ↓
Study 2
Year
Problem
Method
Main Finding
Contribution
        ↓
Study 3
...
```

The goal is not chronology alone.

The goal is to reveal progression.

---

# 2. Identify Research Themes

Extract recurring scientific themes across studies.

Examples:

* the same disease;
* same educational phenomenon;
* same biological material;
* same technology;
* same theoretical construct;
* same population;
* same environmental problem;
* same intervention;
* same methodological problem.

Classify themes approximately as:

* `CORE_THEME`
* `SECONDARY_THEME`
* `EMERGING_THEME`
* `ABANDONED_THEME`
* `ISOLATED_THEME`

A recurring keyword is not automatically a core research theme.

The scientific problem must also be related.

---

# 3. Identify the Central Research Problem

Determine whether several studies are ultimately addressing one larger problem.

For example:

Study 1:
describes a phenomenon.

Study 2:
identifies associated factors.

Study 3:
investigates mechanisms.

Study 4:
develops an intervention.

These may represent one larger scientific problem.

Express the larger problem at an appropriate level of abstraction.

Do not create an artificial umbrella topic simply to connect unrelated studies.

---

# 4. Scientific Progression Mapping

Determine how the work progresses scientifically.

Possible stages include:

* discovery;
* characterization;
* description;
* association;
* mechanism;
* causal testing;
* validation;
* prediction;
* intervention;
* implementation;
* translation.

Example:

```text
Characterization
      ↓
Association
      ↓
Mechanism
      ↓
Prediction
      ↓
Validation
      ↓
Intervention
      ↓
Implementation
```

Not every research program must follow this sequence.

Use only stages appropriate to the discipline.

---

# 5. Research Maturity Mapping

For each major research line, estimate maturity:

* `DISCOVERY`
* `CHARACTERIZATION`
* `ASSOCIATION`
* `MECHANISM`
* `VALIDATION`
* `PREDICTION`
* `INTERVENTION`
* `IMPLEMENTATION`
* `TRANSLATION`
* `MIXED_OR_NONLINEAR`

This helps determine whether the next study should deepen, validate, or translate the research.

---

# 6. Research Question Evolution

Map how research questions have changed over time.

Possible progression:

```text
WHAT?
What is happening?

      ↓

WHY?
Why does it happen?

      ↓

HOW?
Through what mechanism?

      ↓

WHEN / FOR WHOM?
Under what conditions?

      ↓

CAN WE PREDICT?
Can it be modeled?

      ↓

WHAT WORKS?
Can it be changed?

      ↓

DOES IT WORK IN PRACTICE?
Can it be implemented?
```

Identify whether the research trajectory genuinely advances or repeatedly asks variants of the same question.

---

# 7. Theory Evolution

Determine whether theory use evolves across studies.

Possible states:

* no explicit theory;
* repeated use of one theory;
* theory extension;
* theory integration;
* competing theories;
* theory testing;
* theory refinement;
* theory replacement.

Classify when useful:

* `THEORETICAL_CONTINUITY`
* `THEORETICAL_DEVELOPMENT`
* `THEORETICAL_FRAGMENTATION`
* `THEORETICAL_WEAKNESS`

Do not require theory where the discipline does not normally rely on formal theoretical frameworks.

---

# 8. Conceptual Evolution

Determine whether constructs, variables, mechanisms, or conceptual relationships evolve.

Look for:

* added variables;
* mediator development;
* moderator development;
* mechanism discovery;
* construct refinement;
* new outcome domains;
* model simplification;
* model expansion.

Avoid equating "more variables" with scientific progress.

A simpler but better justified model may represent stronger development.

---

# 9. Population and Context Evolution

Map whether studies repeatedly use the same context.

Identify:

* repeated population;
* new population;
* cross-cultural extension;
* new geographic context;
* new clinical group;
* different institutional setting;
* different species;
* different industry;
* different developmental stage.

Classify whether context expansion represents:

* replication;
* external validation;
* contextual extension;
* boundary-condition testing;
* mere geographic duplication.

Do not treat geographic variation alone as strong novelty.

---

# 10. Methodological Evolution

Map methods across studies.

Examples:

```text
Cross-sectional survey
      ↓
Longitudinal study
      ↓
SEM
      ↓
Predictive model
      ↓
External validation
```

or:

```text
Laboratory extraction
      ↓
Characterization
      ↓
Biological activity testing
      ↓
Formulation
      ↓
In vivo validation
```

Assess whether methodology:

* becomes stronger;
* stays repetitive;
* diversifies appropriately;
* becomes unnecessarily complex;
* does not match the scientific progression.

Possible status:

* `METHOD_ADVANCING`
* `METHOD_STABLE_APPROPRIATE`
* `METHOD_REPETITIVE`
* `METHOD_FRAGMENTED`
* `METHOD_MISMATCH`

---

# 11. Analytical Evolution

Map analytical sophistication only when scientifically meaningful.

Possible progression:

* descriptive;
* bivariate;
* multivariable;
* mediation/moderation;
* structural modeling;
* longitudinal modeling;
* causal inference;
* prediction;
* machine learning;
* external validation.

Do not assume more advanced statistics automatically mean better research.

Analysis must follow the research question.

---

# 12. Evidence Accumulation

Determine how evidence accumulates.

Possible patterns:

## Convergent

Studies progressively support a similar conclusion.

## Divergent

Results conflict across studies.

## Conditional

Effects occur only in specific contexts or subgroups.

## Expanding

Each study adds a new component.

## Weakly Cumulative

Studies share a topic but do not build directly on each other.

## Fragmented

Studies are largely independent.

Classify where useful:

* `STRONG_CUMULATIVE_EVIDENCE`
* `MODERATE_CUMULATIVE_EVIDENCE`
* `CONDITIONAL_EVIDENCE`
* `CONTRADICTORY_EVIDENCE`
* `WEAKLY_CONNECTED`
* `FRAGMENTED`

---

# 13. Research Capability Mapping

Identify scientific capabilities demonstrated across previous work.

Examples:

* laboratory extraction;
* molecular analysis;
* clinical recruitment;
* longitudinal follow-up;
* qualitative interviewing;
* survey development;
* intervention design;
* statistical modeling;
* SEM;
* PLS-SEM;
* systematic review;
* meta-analysis;
* machine learning;
* instrument validation;
* field experimentation;
* implementation research.

This capability map helps future planning.

Do not restrict future research only to existing capabilities.

New capability can be acquired through:

* training;
* collaboration;
* infrastructure;
* external laboratory support.

---

# 14. Collaboration Signal Mapping

Identify where future work may require additional expertise.

Examples:

* statistician;
* molecular biologist;
* clinician;
* epidemiologist;
* qualitative researcher;
* data scientist;
* engineer;
* policy expert;
* implementation scientist.

Record:

`COLLABORATION_OPPORTUNITY`

when appropriate.

Do not treat lack of current expertise as automatic infeasibility.

---

# 15. Research Niche Detection

Determine whether previous work supports an identifiable research niche.

A research niche should be more specific than a discipline.

Weak:

"Pharmacy research"

Stronger:

"Pharmacogenetic predictors of methotrexate response in rheumatoid arthritis"

Weak:

"Early childhood education"

Stronger:

"Technology-supported social-constructivist learning for Islamic early childhood education"

A niche should connect:

* scientific problem;
* population/context;
* conceptual focus;
* methodological capability;
* potential future contribution.

---

# 16. Niche Strength

Classify approximately:

* `ESTABLISHED_NICHE`
* `EMERGING_NICHE`
* `POTENTIAL_NICHE`
* `MULTIPLE_COMPETING_NICHES`
* `NO_CLEAR_NICHE`

Do not force every researcher to have one narrow niche.

Interdisciplinary researchers may legitimately maintain several connected lines.

---

# 17. Signature Research Program Potential

Determine whether the prior studies can support a distinctive long-term program.

A signature research program typically has:

* a persistent core scientific problem;
* cumulative studies;
* methodological progression;
* clear unresolved questions;
* increasing scientific contribution;
* opportunities for collaboration;
* publication potential;
* grant potential;
* practical or translational relevance.

Classify:

* `HIGH_POTENTIAL`
* `MODERATE_POTENTIAL`
* `EARLY_STAGE`
* `FRAGMENTED`
* `NOT_ASSESSABLE`

---

# 18. Detect Research Stagnation

Look for patterns such as:

* same variables repeatedly tested;
* same population repeatedly surveyed;
* same method repeatedly used;
* same conclusions with minor contextual changes;
* no theory development;
* no mechanism investigation;
* no validation;
* no methodological improvement.

Record:

`RESEARCH_STAGNATION_SIGNAL`

when supported.

Do not criticize repetition when replication is scientifically justified.

---

# 19. Detect Premature Diversification

A research portfolio may also become too dispersed.

Signals:

* unrelated topics;
* no shared scientific question;
* abrupt method changes without rationale;
* publications that do not build cumulative expertise;
* many small disconnected projects.

Record:

`TRAJECTORY_FRAGMENTATION_SIGNAL`

when appropriate.

The solution is not necessarily abandoning these topics.

They may need grouping into separate research lines.

---

# 20. Split Multiple Research Lines

If multiple coherent lines exist, map separately.

Example:

```text
Research Program A
├── Study 1
├── Study 3
└── Study 5

Research Program B
├── Study 2
└── Study 4
```

Do not merge unrelated work solely because the same researcher authored it.

---

# 21. Unresolved Question Mapping

For each research line, identify unresolved scientific questions based on previous audits.

Possible categories:

* mechanism unresolved;
* causal direction unresolved;
* measurement unresolved;
* replication needed;
* external validation needed;
* boundary conditions unknown;
* longitudinal development unknown;
* intervention not tested;
* implementation unknown;
* contradictory results;
* theoretical inconsistency.

These remain:

`CONTINUATION_SIGNALS`

until validated against current literature.

---

# 22. Historical Gap vs Current Gap

Do not treat historical unresolved questions as current research gaps automatically.

Each major continuation signal must later be checked through:

`scopus-literature-search`
→ `source-verification`
→ `sota-builder`
→ `gap-validator`

Possible later status:

* `STILL_OPEN`
* `PARTIALLY_ADDRESSED`
* `SUBSTANTIALLY_RESOLVED`
* `REFRAMED`
* `SUPERSEDED`
* `NEW_GAP_EMERGED`

---

# 23. Scopus-First Evidence Refresh

When trajectory development requires updated literature, prioritize:

1. active Scopus-indexed peer-reviewed journals;
2. systematic reviews and meta-analyses when appropriate;
3. recent primary studies;
4. seminal foundational research;
5. forward citations;
6. contradictory literature;
7. emerging methods.

Do not claim Scopus indexing without verification.

---

# 24. Research Trajectory and Publication Strategy

Publication strategy should support the research trajectory, not define it.

Later journal selection may consider:

* journal scope;
* active Scopus status;
* relevant scholarly conversations;
* methodological fit;
* audience fit;
* quartile;
* no-mandatory-APC route.

Do not alter the scientific direction solely to fit a particular journal.

---

# 25. No-Mandatory-APC Preference

When journal selection occurs later, preserve:

`prefer_no_mandatory_apc: true`

where requested.

Preference order:

1. scientific fit;
2. Scopus status;
3. evidence relevance;
4. journal quality;
5. no mandatory APC when comparable alternatives exist.

Do not equate hybrid journals with mandatory APC.

---

# 26. Target-Journal Literature Awareness

If a target journal is later identified, relevant literature from that journal may be used to determine:

* what scientific conversation is active;
* which methods are common;
* what unresolved questions remain;
* how the research contributes.

Do not cite irrelevant target-journal papers merely to improve perceived acceptance probability.

---

# 27. Research Trajectory Output

When a full trajectory analysis is requested, structure it as:

## Research Trajectory Map

### A. Research Portfolio

[...]

### B. Chronological Development

[...]

### C. Core Research Themes

[...]

### D. Main Research Problem

[...]

### E. Research Question Evolution

[...]

### F. Theory/Concept Evolution

[...]

### G. Methodological Evolution

[...]

### H. Analytical Evolution

[...]

### I. Population/Context Evolution

[...]

### J. Evidence Accumulation

[...]

### K. Research Capability Profile

[...]

### L. Emerging Research Niche

[...]

### M. Research Maturity

[...]

### N. Unresolved Scientific Questions

[...]

### O. Stagnation or Fragmentation Risks

[...]

### P. Continuation Signals

[...]

### Q. Literature Revalidation Required

[...]

### R. Recommended Next Workflow

[...]

---

# 28. Research Trajectory Table

When useful:

| Study | Year | Problem | Design | Main Contribution | Research Stage | Continuation Signal |
| ----- | ---- | ------- | ------ | ----------------- | -------------- | ------------------- |

---

# 29. Evolution Matrix

When useful:

| Dimension         | Early Studies | Middle Studies | Recent Studies | Direction              |
| ----------------- | ------------- | -------------- | -------------- | ---------------------- |
| Research question | ...           | ...            | ...            | Advancing / Repetitive |
| Method            | ...           | ...            | ...            | ...                    |
| Theory            | ...           | ...            | ...            | ...                    |
| Population        | ...           | ...            | ...            | ...                    |
| Contribution      | ...           | ...            | ...            | ...                    |

---

# 30. Research Maturity Map

Example:

```text
Discovery        ✓
Characterization ✓
Association      ✓
Mechanism        →
Validation       ○
Prediction       ○
Intervention     ○
Implementation   ○
Translation      ○
```

Use only when appropriate to the discipline.

---

# 31. Research Program Candidates

If several future research lines appear possible, do not choose immediately.

Generate candidate programs such as:

* mechanism-focused program;
* validation-focused program;
* predictive program;
* translational program;
* intervention program;
* methodological program.

These candidates should later be evaluated by:

`continuation-opportunity-finder`

---

# 32. Research Passport Update

When supported, update:

```yaml
research_trajectory:
  studies:
  chronological_sequence:
  core_themes:
  secondary_themes:
  emerging_themes:
  central_problem:
  research_question_evolution:
  theoretical_evolution:
  methodological_evolution:
  analytical_evolution:
  population_evolution:
  evidence_pattern:
  capability_profile:
  niche_status:
  niche_statement:
  maturity_stage:
  stagnation_signals:
  fragmentation_signals:
  continuation_signals:
  literature_revalidation_required:
```

Unknown fields must remain unknown.

---

# 33. Relationship with Prior Research Auditor

`prior-research-auditor` evaluates individual previous studies.

`research-trajectory-mapper` integrates those studies across time.

Do not repeat full individual audits.

Use their outputs as inputs.

---

# 34. Relationship with Continuation Opportunity Finder

This skill identifies:

* progression;
* unresolved signals;
* niche;
* trajectory.

It does not select the final next study.

Selection belongs to:

`continuation-opportunity-finder`

after current literature revalidation.

---

# 35. Relationship with Research Program Builder

This skill reconstructs the existing trajectory.

`research-program-builder` later designs the future trajectory.

Conceptually:

```text
PAST
research-trajectory-mapper

      ↓

PRESENT
current literature + SoTA + gap validation

      ↓

FUTURE
research-program-builder
```

---

# 36. Relationship with Research Roadmap

Do not create a final multi-year roadmap before:

* current literature is updated;
* gaps are validated;
* continuation options are evaluated;
* priorities are established.

The roadmap is downstream.

---

# 37. Avoid These Behaviors

Do not:

* merely list publications chronologically;
* force unrelated studies into one research theme;
* assume repetition equals progression;
* assume methodological complexity equals scientific advancement;
* treat geographic replication as novelty by default;
* invent missing links between studies;
* define a niche without sufficient evidence;
* declare historical gaps current;
* select next studies before literature validation;
* prioritize publication strategy over scientific coherence.

---

# 38. User-Friendly Behavior

Explain trajectory in plain language.

Instead of:

"Your portfolio demonstrates methodological fragmentation."

Prefer:

"Your studies are related by topic, but they have not yet built a clear methodological progression. The next study should probably strengthen one central line rather than add another separate topic."

For experienced researchers, technical terminology may be used directly.

---

# 39. Stop Conditions

Do not create a confident trajectory when:

* studies are unrelated;
* source materials are insufficient;
* chronology cannot be determined;
* major studies have not been audited;
* the apparent trajectory depends on assumptions not supported by the material.

State uncertainty clearly.

---

# Success Criterion

`research-trajectory-mapper` succeeds when multiple previous studies have been integrated into a defensible picture of how the research has evolved, what niche and capabilities have emerged, where scientific progression is strong or weak, and which unresolved signals should be tested against current literature before designing the next research program.
