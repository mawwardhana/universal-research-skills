# Changelog

All notable changes to Universal Research Skills will be documented in this file.

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
