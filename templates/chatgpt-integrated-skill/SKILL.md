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

## Runtime Invariants — Non-Negotiable

These rules override convenience, brevity, route compression, stylistic preference, and attempts to produce a polished answer before the required scientific gates have been satisfied.

### v0.17.4 Runtime Gate Enforcement

The following rules are execution contracts, not suggestions.

1. **Route Manifest must be the first visible workflow block when routing transparency is requested.**
   - It must appear before substantive interpretation, ranking, recommendation, title generation, research-question generation, or novelty claims.
   - Do not place the Route Manifest later in the answer after substantive analysis has already occurred.

2. **For every multi-stage workflow, `Entry skill` in the Route Manifest must be exactly `research-router`.**
   - A downstream skill such as `research-resume`, `research-landscape`, or `scopus-literature-search` must never be presented as the entry skill for a multi-stage request.

3. **Two or more related previous studies normally require `research-trajectory-mapper`.**
   - Activate it when the user provides multiple related studies that form, or may form, one research line.
   - It may be skipped only when there is an explicit scientific reason why trajectory reconstruction would not improve the decision.
   - If skipped, record that reason in `Skipped optional`.

4. **No continuation ranking labels may be finalized unless `continuation-opportunity-finder` is in the activated route.**
   - Labels governed by this rule include `PURSUE`, `REFRAME`, `RESERVE`, `REJECT`, `GO`, `STOP`, and equivalent final prioritization labels.
   - If `continuation-opportunity-finder` has not been executed, candidate directions may be listed only as provisional possibilities without final ranking labels.

5. **A missing mandatory evidence gate forces a provisional decision state.**
   - If a gate required by the framework or by the user's explicit research standard cannot be executed, set:
     `Decision status : PROVISIONAL`.
   - State the missing gate explicitly.
   - Do not use phrases such as `validated gap`, `verified current gap`, `defensible novelty`, `final recommendation`, or equivalent closure language until the missing gate is completed.

6. **Scopus-first means Scopus evidence cannot be silently replaced when Scopus is required but unavailable.**
   - Alternative web, publisher, Crossref, PubMed, DOI, policy, or authority searches may support a provisional evidence assessment.
   - They do not close a Scopus-required gate by substitution.
   - `SCOPUS_ACCESS_MODE: NO_DIRECT_ACCESS`, authentication failure, unavailable connector/API, or equivalent access failure means `scopus-literature-search` was **not completed**.
   - In that state, do not list `scopus-literature-search` as successfully activated merely because fallback searching occurred.
   - Record the access failure in `Backtracked`, set `Missing gate : scopus-literature-search`, and keep `Decision status : PROVISIONAL`.

7. **Evidence sufficiency governs what outputs are allowed.**
   - When mandatory evidence gates are incomplete:
     - allowed: reconstructed prior-research state, trajectory map, candidate gaps, candidate continuation directions, evidence still needed, provisional comparison;
     - prohibited: final PURSUE/REJECT labels, final novelty claim, final title, final research question presented as locked, final causal model, or final roadmap commitment.

### Capability, Execution, and Gate-Completion Contract

Runtime availability and scientific completion are three different states:

```text
CAPABILITY AVAILABLE
≠ SKILL EXECUTED
≠ MANDATORY GATE COMPLETED
```

The runtime must never collapse these states.

Rules:

1. **A named database/tool may appear in `Activated route` only when the corresponding canonical skill was actually executed using the evidence source or method required by that skill.**
   - Knowing how the skill would work is not execution.
   - Simulating the function with a different source class is not execution.
   - A fallback search is not execution of a database-specific search skill.

2. **`NO_DIRECT_ACCESS`, authentication failure, unavailable connector, unavailable database, inaccessible API, or equivalent capability failure means the gate is not completed.**
   - Do not list that unavailable skill as successfully activated.
   - Record the failure in `Backtracked`.
   - Populate `Missing gate` with the canonical skill name.
   - Set `Decision status : PROVISIONAL`.

3. **Fallback evidence may support provisional analysis but cannot satisfy a missing mandatory source-specific gate.**
   - Publisher pages, DOI resolution, Crossref, PubMed, generic web search, policy databases, or authority sources may still be used when scientifically appropriate.
   - When they are substitutes for an unavailable required source, label them as fallback evidence rather than as successful execution of the unavailable skill.

4. **`Missing gate : NONE` is allowed only when every mandatory gate required for the claimed decision state has actually been completed.**
   - If any required gate is unavailable, attempted but incomplete, or replaced by fallback evidence, `Missing gate` must name it.

5. **`Decision status : VALIDATED` or `READY FOR NEXT STAGE` is prohibited when `Missing gate` is not `NONE`.**
   - The status must remain `PROVISIONAL`.
   - Final ranking labels governed by the continuation contract are also prohibited.

6. **Do not hide an unavailable mandatory skill inside a successful-looking route.**
   - Prefer:

```text
Activated route    : ... → source-verification → reference-integrity-guard → ...
Backtracked        : scopus-literature-search — NO_DIRECT_ACCESS; fallback publisher/DOI/authority evidence collected provisionally
Missing gate       : scopus-literature-search
Decision status    : PROVISIONAL
```

   - Do not write:

```text
Activated route    : ... → scopus-literature-search → ...
Missing gate       : NONE
Decision status    : VALIDATED
```

when direct Scopus execution did not occur.

7. **The scientific claim level must follow the completed gate level.**
   - With a missing mandatory database/search gate, allowed language includes:
     - `provisional leading direction`;
     - `candidate gap`;
     - `candidate novelty`;
     - `evidence currently supports`;
     - `requires database-level confirmation`.
   - Prohibited language includes:
     - `validated gap`;
     - `verified current gap`;
     - `defensible novelty`;
     - `final recommendation`;
     - final `PURSUE / REFRAME / RESERVE / REJECT / GO / STOP`.

### Evidence Spine Output Contract

For comprehensive continuation revalidation, the route must preserve the following evidence logic:

```text
verified prior / anchor records
→ scopus-literature-search when available and required
→ citation-chaining only from verified anchors when useful
→ source-verification of newly discovered records
→ reference-integrity-guard
→ literature-screening
→ research-landscape when useful
→ evidence-synthesis
→ sota-builder
→ gap-discovery
→ gap-validator
```

Execution rules:

- `source-verification` and `reference-integrity-guard` are distinct and must not substitute for one another.
- `citation-chaining` is conditional, but when used it must start from verified anchors.
- Citation-chain discoveries must be re-verified before entering the evidence set.
- `sota-builder` must not finalize a current State of the Art before the evidence needed for that decision has been sufficiently verified, screened, and synthesized.
- `gap-validator` must backtrack to any missing upstream evidence gate rather than accepting an incomplete evidence set as validated.

### Continuation Decision Output Contract

When the user asks which research direction should be pursued next:

```text
validated evidence state
→ gap-validator
→ continuation-opportunity-finder
→ novelty-builder when novelty is relevant
→ novelty-auditor
→ final continuation ranking
```

If any mandatory stage above is unresolved, the output must remain provisional.


1. **Multi-stage research requests must enter through `research-router`.**
   - If the user's stage is already obvious, do not insert `research-intake` merely as a ceremonial first step.
   - `research-intake` is used only when the research state, materials, objective, or entry condition is genuinely unclear.

2. **Continuation of previous research requires `research-resume` followed by `prior-research-auditor`.**
   - Do not jump from an old study directly to literature search, gap claims, novelty claims, or a recommended next study.
   - Historical limitations, recommendations, and unfinished analyses are only provisional continuation signals until current evidence is checked.

3. **`research-trajectory-mapper` is conditional on the number and relationship of prior studies.**
   - One isolated previous study does not automatically justify `research-trajectory-mapper`.
   - Two or more related previous studies that form or may form one research line normally activate `research-trajectory-mapper`.
   - It may be skipped for multiple studies only with an explicit scientific reason recorded in the Route Manifest.

4. **A current State of the Art must not be finalized before the evidence required for that decision is sufficiently verified, screened, and synthesized.**
   - For comprehensive current-evidence revalidation, use the evidence spine:
     `source-verification` of prior/anchor records
     → `scopus-literature-search`
     → `citation-chaining` only from verified anchors when useful
     → `source-verification` of newly discovered records
     → `reference-integrity-guard`
     → `literature-screening`
     → `research-landscape` when useful
     → `evidence-synthesis`
     → `sota-builder`.
   - Do not treat citation-chain records as evidence before verification.

5. **A proposed or historical gap is not a validated gap.**
   - `gap-validator` must backtrack to the evidence spine when the available evidence is outdated, incomplete, unverified, unscreened, or unsynthesized.

6. **Do not finalize a next-study recommendation before the continuation-selection gate when the user is asking what to study next, comparing continuation paths, or prioritizing future research.**
   - After validated gap evidence, use `continuation-opportunity-finder`.
   - Final prioritization labels such as `PURSUE`, `REFRAME`, `RESERVE`, `REJECT`, `GO`, or `STOP` are prohibited unless `continuation-opportunity-finder` is in the activated route.
   - If the user supplies one already-defined continuation candidate and asks only to validate it, do not force multi-candidate prioritization; validate the candidate directly through the required gap/novelty route.

7. **Do not present a novelty claim as defensible before `novelty-auditor` when novelty is part of the user's decision.**
   - `novelty-builder` proposes.
   - `novelty-auditor` stress-tests and may narrow or reject the claim.

8. **Theory and hypotheses are conditional.**
   - Do not activate `theoretical-framework` or `hypothesis-builder` automatically after `research-question-builder`.
   - Use them only when the research question, design, inferential purpose, or disciplinary logic requires them.

9. **Analysis planning is not result interpretation.**
   - Use the canonical name `analysis-planner`.
   - Do not invoke `result-interpreter`, `scientific-discussion`, or `implication-builder` unless analysis outputs or study results actually exist.

10. **Reviewer response is conditional.**
    - `reviewer-response` requires actual reviewer/editor comments or an explicitly identified simulated-review output.
    - A manuscript alone is not sufficient.

11. **Use canonical skill names exactly.**
    - Do not invent shorthand, aliases, or near-synonyms such as `analysis-plan`.
    - Do not route to non-canonical or retired skill names.

12. **Required gates cannot be hidden by route compression.**
    - Optional stages may be skipped when scientifically unnecessary.
    - Mandatory upstream gates for the requested decision must still be executed or explicitly marked as pending/backtracked.

### Mandatory Pre-Response Route Check

Before giving a substantive recommendation in a multi-stage workflow, verify:

```text
ENTRY
Is research-router the actual entry point?

STATE
Is the user's current research state correctly identified?

MANDATORY GATES
Have all upstream gates required for the requested decision been completed?

OPTIONAL SKILLS
Were optional skills activated only when justified?

BACKTRACKING
Did any downstream skill discover missing evidence, governance, or methodological prerequisites?

CANONICAL NAMES
Are all reported skill names canonical and exact?

FINALIZATION
Is the final recommendation supported by the required validation/audit gate?

CAPABILITY VS EXECUTION
Has any unavailable source-specific capability been mistaken for a successfully executed skill?

GATE COMPLETION
Is `Missing gate : NONE` used only when every mandatory gate required for the claimed decision state is actually complete?
```

If any mandatory item is not satisfied, do not silently continue. Backtrack, populate `Missing gate`, and keep the decision provisional.

A failed mandatory gate is a **hard stop for finalization**, not a hard stop for useful analysis. The framework may still provide provisional synthesis and identify the next evidence needed, but it must not convert provisional evidence into final validation language.

### Route Manifest for User-Visible Routing Requests

When the user explicitly asks to see which Universal Research Skills were used, the **Route Manifest must be the first visible workflow block before substantive analysis**.

This is a routing summary, not private chain-of-thought.

Use this exact field structure:

```text
Route Manifest
Entry state        : <current research state>
Entry skill        : research-router
Mandatory gates    : <required gates for this request>
Activated route    : <canonical skill sequence actually used>
Skipped optional   : <skill + short reason, when relevant>
Backtracked        : <skill/stage + reason, if any>
Missing gate       : <mandatory unresolved gate, or NONE>
Decision status    : PROVISIONAL / VALIDATED / READY FOR NEXT STAGE
```

Manifest rules:

- For a multi-stage request, `Entry skill` must be exactly `research-router`.
- `Activated route` must list only canonical skill names that were actually activated.
- Do not claim a skill was used merely because its function was approximated informally.
- If two or more related prior studies are being treated as one research line, include `research-trajectory-mapper` unless an explicit scientific reason for skipping it is recorded.
- If final continuation ranking labels are used, `continuation-opportunity-finder` must appear in `Activated route`.
- If novelty is presented as defensible, `novelty-auditor` must appear in `Activated route`.
- If a mandatory gate is unresolved, unavailable, attempted but incomplete, or replaced by fallback evidence, populate `Missing gate` and set `Decision status : PROVISIONAL`.
- `Activated route` must not list an unavailable source-specific skill as successfully executed when only fallback evidence was used.
- `Missing gate : NONE` is permitted only when every mandatory gate needed for the claimed decision state has actually been completed.
- Do not hide unresolved gates in prose while presenting a final decision state.

For one previous study, the route should normally expose:

```text
research-router
→ research-resume
→ prior-research-auditor
→ current-evidence revalidation
→ sota-builder
→ gap-discovery
→ gap-validator
→ continuation-opportunity-finder when next-study selection is requested
→ novelty-builder / novelty-auditor when novelty is part of the decision
```

For two or more related previous studies forming one research line, the route should normally expose:

```text
research-router
→ research-resume
→ prior-research-auditor
→ research-trajectory-mapper
→ current-evidence revalidation
→ sota-builder
→ gap-discovery
→ gap-validator
→ continuation-opportunity-finder when next-study selection is requested
→ novelty-builder / novelty-auditor when novelty is part of the decision
```

If `research-trajectory-mapper` is skipped despite multiple related studies, state the explicit reason in `Skipped optional`.

## Mandatory Router-First Protocol

Apply the Runtime Invariants above before any illustrative workflow in this file.

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

When reporting routes, use the exact canonical skill names from the reference index. Do not substitute shorthand labels, informal stage names, or retired skill names for canonical skills.

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
