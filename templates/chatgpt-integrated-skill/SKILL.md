---
name: universal-research-skills
description: Orchestrate the 56 canonical Universal Research Skills as one integrated, evidence-driven research workflow in ChatGPT. Use when a researcher needs end-to-end or multi-stage support for idea discovery, continuation of prior research, literature and evidence work, State of the Art, gap and novelty validation, research questions, theory, conceptual frameworks, methodology, ethics and governance, execution and monitoring, data quality, analysis, interpretation, manuscripts, journal selection, peer review, reproducibility, or research roadmapping. Route through research-router and load only the canonical skill references needed for the shortest scientifically defensible path.
---

# Universal Research Skills

## Purpose

Use this file as the single ChatGPT entry point for the Universal Research Skills framework.

This distribution preserves the framework as one integrated workflow while keeping the 56 canonical research skills as separate reference resources.

This entry point is **not a 57th research skill**. Its role is orchestration only.

The release build must place the canonical skill resources at:

```text
references/<skill-name>.md
```

Each reference file must be generated from the corresponding canonical repository file:

```text
skills/<skill-name>/SKILL.md
```

without changing its content.

---

## Mandatory Router-First Protocol

For a substantive research request that can involve more than one research stage:

1. Read `references/research-router.md`.
2. Determine the user's actual entry state, available materials, scientific goal, unresolved decisions, and whether the request is single-stage or multi-stage.
3. Follow the router's shortest scientifically defensible path.
4. When the router selects a skill, read `references/<selected-skill>.md` before applying that skill.
5. When a selected skill hands off to another skill, read the next canonical reference before continuing.
6. Preserve outputs, uncertainties, gates, unresolved issues, conditional activation rules, and backtracking requirements across handoffs.
7. Re-enter an earlier evidence, governance, methodology, or quality stage when a downstream skill finds that its upstream requirements are insufficient.
8. Stop when the user's current request has been answered or the next defensible action has been established.

Do not load all 56 resources merely for completeness.

If the user explicitly requests one narrow function and the correct skill is unambiguous, consult that canonical skill directly. Use the router whenever stage, sequence, or handoff is uncertain.

If the user asks to see the internal route, the displayed route must begin with `research-router` whenever router-first behavior was used. Do not hide the router and present a downstream skill as the apparent entry point.

---

## Canonical Resource Rule

Treat every file under `references/` as a canonical workflow resource.

Do not:

- reconstruct a canonical skill from memory when its reference is available;
- merge distinct scientific decision functions into a generic workflow;
- invent a new internal skill name;
- silently omit a required handoff;
- claim a stage is complete when evidence of completion is absent;
- alter scientific meaning because of publication, deadline, funding, or desired-result pressure.

If a canonical resource is unavailable, state which resource is missing. Do not pretend it was consulted.

---

## Integrated Research State

When multiple skills are used, maintain a compact working state containing only relevant fields:

```yaml
research_state:
  entry_mode:
  current_stage:
  available_materials:
  research_problem:
  research_question:
  phenomenon_evidence_status:
  scholarly_evidence_status:
  gap_status:
  novelty_status:
  theory_status:
  hypothesis_status:
  conceptual_framework_status:
  methodology_status:
  ethics_regulatory_status:
  registration_status:
  data_governance_status:
  execution_status:
  protocol_adherence_status:
  data_collection_status:
  deviation_risk_status:
  progress_status:
  data_quality_status:
  analysis_status:
  interpretation_status:
  manuscript_status:
  publication_status:
  reproducibility_status:
  unresolved_issues:
  next_route:
```

Populate only supported and relevant fields. Never fabricate status.

---

## Core Scientific Distinctions

Preserve these distinctions across all skill handoffs:

```text
phenomenon evidence ≠ scholarly evidence
candidate gap ≠ validated gap
novelty claim ≠ audited novelty
research question ≠ method
theory useful ≠ theory mandatory
preregistration ≠ ethics approval
data governance ≠ data quality
data collection ≠ data validity
risk ≠ actual deviation
activity ≠ scientific progress
reported completion ≠ verified completion
reviewer request ≠ scientifically justified change
publication strategy ≠ evidence selection
```

---

## Evidence Priorities

Use two complementary evidence priorities:

```text
SCHOLARLY EVIDENCE
Scopus-first, not Scopus-only

PHENOMENON / REAL-WORLD EVIDENCE
Authority-first
```

Phenomenon evidence may establish magnitude, trend, context, policy, or real-world relevance.

It does not by itself prove a scientific gap or novelty.

Publication economics, journal quartile, target-journal fit, and APC preference must not distort evidence selection.

---

## Scientific Positioning

When the task requires research positioning, preserve the adversarial sequence when applicable:

```text
evidence-synthesis
→ sota-builder
→ gap-discovery
→ gap-validator
→ novelty-builder
→ novelty-auditor
```

A valid result can be rejection, narrowing, reframing, or conditional acceptance of a proposed gap or novelty claim.

---

## Conditional Research Logic

Do not force theory, hypotheses, or conceptual frameworks into every study.

Route according to the research question, design, and inferential purpose.

Use conditional branches rather than a single default chain:

```text
research-question-builder
      │
      ├── theory needed
      │      ↓
      │ theoretical-framework
      │      ↓
      │ hypothesis-builder when hypothesis testing is appropriate
      │
      ├── hypothesis appropriate without a formal theory-building step
      │      ↓
      │ hypothesis-builder
      │
      └── neither theory nor hypothesis required
             ↓
        proceed without forcing them

conceptual-framework
→ use when scientifically useful or required by the design
```

Exploratory, qualitative, descriptive, methodological, validation, review, and other legitimate designs may follow shorter or non-hypothesis paths.

---

## Methodology Before Software

Preserve:

```text
research question
→ evidence need
→ problem-solving approach
→ methodology
→ protocol / sampling / instrument
→ analysis architecture
→ method
→ software
```

Do not let software availability define the scientific question.

---

## Governance and Execution

Governance is cross-cutting and may reactivate at multiple stages.

Use the relevant canonical resources for:

```text
ethics-regulatory-gate
registration-preregistration-builder
research-data-governance
data-quality-auditor
reproducibility-auditor
```

For active research execution, preserve:

```text
research-execution-manager
          │
   ┌──────┼──────┐
   ▼      ▼      ▼
protocol- data-  deviation-
adherence collection risk
monitor   monitor monitor
   └──────┼──────┘
          ▼
research-progress-auditor
          ↓
next decision gate
```

A defensible decision may be proceed, proceed with conditions, replan, amend, pause, stop, or escalate.

---

## Analysis and Interpretation

Distinguish **analysis planning** from **interpretation of actual results**.

When the user is planning analysis and no results yet exist:

```text
analysis-planner
      ↓
statistical-method-selector
or
qualitative-analysis
or
mixed-method-analysis
or
meta-analysis
      ↓
analysis plan / method decision
      ↓
STOP unless another planning stage is requested
```

When analysis outputs or study results actually exist:

```text
appropriate analysis skill(s)
      ↓
result-interpreter
      ↓
scientific-discussion when requested or needed
      ↓
implication-builder when requested or needed
```

Do not invoke `result-interpreter`, `scientific-discussion`, or `implication-builder` merely because an analysis method has been selected.

Preserve uncertainty, effect magnitude, contradictions, study-design boundaries, and causal limits.

---

## Manuscript and Publication

Use manuscript resources according to the user's actual publication state.

A common manuscript-development route is:

```text
manuscript-architect
      ↓
manuscript-writer
      ↓
manuscript-auditor
      ↓
branch according to the user's goal
      ├── journal selection / positioning → journal-matcher
      ├── pre-submission stress test      → reviewer-simulator
      ├── actual reviewer/editor comments → reviewer-response
      └── no further publication task     → STOP
```

`reviewer-response` requires actual reviewer/editor comments or an explicitly identified simulated-review output. Do not activate it merely because a manuscript exists.

Do not rewrite the scientific record to fit a journal.

Keep simulated peer review distinct from actual peer review.

---

## Continuation and Roadmapping

For continuation of previous research, use a **current-evidence-first validation route** rather than selecting the next study from historical limitations alone.

```text
research-router
      ↓
research-resume
      ↓
prior-research-auditor
      ↓
research-trajectory-mapper
ONLY when multiple related studies exist
or the user explicitly requests trajectory / program / roadmap positioning
      ↓
CURRENT EVIDENCE REFRESH
source-verification of prior / anchor records
      ↓
scopus-literature-search
      ↓
citation-chaining when verified anchors exist
      ↓
source-verification of newly discovered records
      ↓
reference-integrity-guard
      ↓
literature-screening
      ↓
research-landscape when mapping is useful
      ↓
evidence-synthesis
      ↓
sota-builder
      ↓
gap-discovery
      ↓
gap-validator
      ↓
continuation-opportunity-finder
      ↓
novelty-builder
      ↓
novelty-auditor
      ↓
research-question-builder and/or research-roadmap
according to the user's goal
```

For a **single isolated previous study**, do not automatically activate `research-trajectory-mapper`. Route directly from `prior-research-auditor` into the current-evidence refresh unless broader trajectory positioning is explicitly needed.

A continuation idea inferred from an old study before current-evidence validation is only a **provisional continuation opportunity**. Do not present it as a validated research gap, defensible novelty claim, or recommended next study until the required current-evidence, gap-validation, and novelty-audit stages have been completed.

Research progression should follow scientific dependency rather than publication counting.

---

## Canonical Reference Index

### Entry, discovery, and continuation

- `references/research-router.md`
- `references/research-intake.md`
- `references/research-resume.md`
- `references/idea-discovery.md`
- `references/research-landscape.md`
- `references/trend-detection.md`
- `references/emerging-topic-discovery.md`
- `references/prior-research-auditor.md`
- `references/research-trajectory-mapper.md`
- `references/continuation-opportunity-finder.md`
- `references/research-roadmap.md`

### Evidence and scientific positioning

- `references/scopus-literature-search.md`
- `references/source-verification.md`
- `references/reference-integrity-guard.md`
- `references/citation-chaining.md`
- `references/literature-screening.md`
- `references/evidence-synthesis.md`
- `references/phenomenon-evidence-builder.md`
- `references/sota-builder.md`
- `references/gap-discovery.md`
- `references/gap-validator.md`
- `references/novelty-builder.md`
- `references/novelty-auditor.md`

### Research logic and methodology

- `references/research-question-builder.md`
- `references/theoretical-framework.md`
- `references/hypothesis-builder.md`
- `references/conceptual-framework.md`
- `references/problem-solving-approach.md`
- `references/methodology-architect.md`
- `references/sampling-strategy.md`
- `references/instrument-design.md`
- `references/protocol-builder.md`

### Governance, data integrity, and execution

- `references/ethics-regulatory-gate.md`
- `references/registration-preregistration-builder.md`
- `references/research-data-governance.md`
- `references/data-quality-auditor.md`
- `references/reproducibility-auditor.md`
- `references/research-execution-manager.md`
- `references/protocol-adherence-monitor.md`
- `references/data-collection-monitor.md`
- `references/deviation-risk-monitor.md`
- `references/research-progress-auditor.md`

### Analysis and interpretation

- `references/analysis-planner.md`
- `references/statistical-method-selector.md`
- `references/qualitative-analysis.md`
- `references/mixed-method-analysis.md`
- `references/meta-analysis.md`
- `references/result-interpreter.md`
- `references/scientific-discussion.md`
- `references/implication-builder.md`

### Manuscript, journal, and peer review

- `references/manuscript-architect.md`
- `references/manuscript-writer.md`
- `references/manuscript-auditor.md`
- `references/journal-matcher.md`
- `references/reviewer-simulator.md`
- `references/reviewer-response.md`

---

## Current-Evidence Rule

When a claim depends on current information, verify it with current authoritative sources when tools are available.

Examples include:

- current literature;
- Scopus coverage;
- journal indexing;
- APC or publication model;
- author instructions;
- regulations and policies;
- official statistics;
- corrections, expressions of concern, or retractions.

Do not present stale information as current.

---

## Stable-Baseline Rule

Universal Research Skills v0.17.x contains 56 canonical research skills.

Do not create a 57th skill merely because a task is specialized.

Use this order:

```text
existing canonical skill
→ composition through research-router
→ method/domain-specific handling inside an existing skill
→ explicitly identify a genuine uncovered need
```

Framework expansion requires a separately reviewed repository change and release.

---

## Success Criterion

The integrated ChatGPT distribution succeeds when the user can enter from any reasonable research state without manually choosing among 56 skills; when `research-router` selects the shortest scientifically defensible route; when each selected function is executed from its canonical reference; when handoffs and backtracking remain coherent; when completed work is not unnecessarily repeated; when evidence roles, governance gates, execution monitoring, data-quality boundaries, analysis logic, interpretation limits, manuscript integrity, publication strategy, peer-review handling, reproducibility, and research roadmapping remain scientifically consistent; and when the final response provides the next defensible research action without fabricating evidence, status, permission, completion, or certainty.
