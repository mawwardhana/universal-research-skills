---
name: research-roadmap
description: Build a coherent, evidence-grounded, multi-stage research roadmap from prior research, current State-of-the-Art, validated gaps, audited novelty, scientific implications, continuation opportunities, researcher capabilities, feasibility constraints, and long-term program goals. Use when a researcher needs to connect completed studies with defensible next studies, sequence multiple future projects, define milestones and decision gates, align methods and outputs across time, or convert a fragmented publication history into a cumulative research program without treating publication count, funding calls, journal prestige, software availability, or fashionable topics as substitutes for scientific progression.
---

# Research Roadmap

## Purpose

`research-roadmap` converts scientifically defensible research opportunities into a coherent program of future studies.

Its central question is:

> Given what has already been established, what remains unresolved, what can realistically be studied next, and what sequence of studies would produce the strongest cumulative scientific progression over time?

A research roadmap is not merely:

- a list of future topics;
- a sequence of publications;
- a grant schedule;
- a timeline of activities;
- a list of methods;
- a list of technologies;
- a list of journal targets;
- a collection of loosely connected projects;
- or a decorative long-term plan.

A defensible roadmap must explain:

- why each stage exists;
- what uncertainty each stage addresses;
- what evidence must be generated;
- what depends on earlier stages;
- what can proceed in parallel;
- what would invalidate or redirect later stages;
- what capabilities must be developed;
- and how the program cumulatively advances scientific knowledge.

---

# Core Principle

The roadmap must be driven by scientific dependency rather than calendar convenience.

Use:

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

Do not use:

```text
Year 1 → Study A
Year 2 → Study B
Year 3 → Study C
```

unless the scientific reason for that sequence is explicit.

---

# When to Use

Use `research-roadmap` when the researcher:

- wants to continue previous research;
- has multiple previous studies that need to be connected;
- wants to identify a coherent long-term research program;
- needs a 3-year, 5-year, or longer research trajectory;
- is preparing a grant roadmap;
- is developing a laboratory or research-group agenda;
- wants to convert validated gaps into staged studies;
- has several continuation opportunities and needs to sequence them;
- needs milestone and dependency logic;
- needs to distinguish near-term, mid-term, and long-term research;
- wants to connect discovery, validation, implementation, and translation;
- needs to coordinate multiple methods or disciplines across stages;
- needs to define evidence gates before later claims can be made;
- or needs to explain why one study should precede another.

Do not use this skill merely because a funder asks for a timeline.

A timeline can be created only after the scientific roadmap exists.

---

# Required Upstream Context

The roadmap should use the strongest available upstream evidence.

Preferred inputs include:

- `research-resume`;
- `prior-research-auditor`;
- `research-trajectory-mapper`;
- `continuation-opportunity-finder`;
- `research-landscape`;
- `sota-builder`;
- `gap-validator`;
- `novelty-auditor`;
- `research-question-builder`;
- `implication-builder`;
- verified literature;
- verified phenomenon evidence;
- completed datasets;
- completed manuscripts or publications;
- validated methods;
- known researcher or team capabilities;
- resource constraints;
- institutional priorities;
- and explicit long-term research goals.

Do not assume all inputs are required.

Use only the inputs needed to construct a scientifically defensible program.

---

# Minimum Readiness Gate

Before constructing a confident roadmap, determine whether the following are sufficiently clear:

1. What prior research has actually established?
2. Which findings remain uncertain?
3. Which gaps are validated rather than merely asserted?
4. Which proposed contributions survived novelty auditing?
5. Which continuation opportunities are feasible?
6. Which major dependencies exist?
7. Which research capabilities already exist?
8. Which critical capabilities are missing?
9. Which outputs are scientifically necessary?
10. Which later stages depend on earlier evidence?

If several of these are unknown, produce a provisional roadmap rather than a definitive roadmap.

---

# Roadmap Readiness Status

Use one of:

- `ROADMAP_READY`
- `ROADMAP_PARTIALLY_READY`
- `ROADMAP_REQUIRES_REVALIDATION`
- `ROADMAP_REQUIRES_PRIOR_RESEARCH_AUDIT`
- `ROADMAP_REQUIRES_GAP_VALIDATION`
- `ROADMAP_REQUIRES_NOVELTY_AUDIT`
- `ROADMAP_REQUIRES_FEASIBILITY_CLARIFICATION`
- `ROADMAP_NOT_YET_DEFENSIBLE`

Do not force a roadmap when upstream evidence is inadequate.

---

# Scientific Program Logic

The roadmap should show how knowledge accumulates.

A common progression may be:

```text
Discovery
   ↓
Characterization
   ↓
Association / Comparison
   ↓
Mechanistic Explanation
   ↓
Validation
   ↓
Prediction
   ↓
Intervention
   ↓
Implementation
   ↓
Translation
```

But this is not universal.

Other legitimate progressions include:

```text
Exploration
   ↓
Concept Development
   ↓
Instrument Development
   ↓
Validation
   ↓
Application
```

or:

```text
Method Development
   ↓
Benchmarking
   ↓
External Validation
   ↓
Robustness Testing
   ↓
Deployment
```

or:

```text
Formulation Development
   ↓
Physicochemical Characterization
   ↓
In-vitro Evaluation
   ↓
Stability
   ↓
Preclinical Evaluation
   ↓
Clinical Translation
```

or:

```text
Phenomenon Mapping
   ↓
Contextual Explanation
   ↓
Intervention Co-design
   ↓
Feasibility
   ↓
Effectiveness
   ↓
Implementation
```

Use the progression justified by the scientific problem.

---

# Do Not Force a Universal Maturity Ladder

Not every research program must reach:

- intervention;
- commercialization;
- clinical use;
- policy implementation;
- technology transfer;
- or large-scale deployment.

A basic-science program may legitimately end at mechanistic clarification.

A qualitative program may legitimately mature through explanatory depth and transferability rather than intervention.

A methodological program may mature through validation and reproducibility rather than product deployment.

A systematic-review program may mature through evidence synthesis, uncertainty resolution, and agenda setting.

---

# Roadmap Unit

The fundamental unit of a roadmap is a `ROADMAP_STAGE`.

Each stage must have a scientific purpose.

Use:

```yaml
roadmap_stage:
  stage_id:
  stage_name:
  scientific_purpose:
  upstream_evidence:
  unresolved_question:
  proposed_study:
  knowledge_function:
  expected_contribution:
  required_capabilities:
  dependencies:
  decision_gate:
  success_condition:
  failure_condition:
  downstream_options:
  indicative_timing:
  outputs:
  confidence:
```

---

# Stage ID

Use stable identifiers such as:

- `RM-S1`
- `RM-S2`
- `RM-S3`

or, for branching programs:

- `RM-A1`
- `RM-A2`
- `RM-B1`
- `RM-B2`

Do not encode year into the scientific identity of the stage unless required.

The same stage may shift in calendar time without changing its scientific role.

---

# Stage Name

Use a scientific function rather than a vague project title.

Prefer:

- Biomarker Discovery
- Mechanistic Validation
- External Cohort Validation
- Instrument Validation
- Formulation Optimization
- Comparative Effectiveness
- Implementation Feasibility
- Cross-context Replication

Avoid:

- Research Year 1
- Advanced Study
- Further Research
- Follow-up Study
- Publication 2
- Phase Next

unless a formal phase name has a defined scientific meaning.

---

# Scientific Purpose

Every stage must state what uncertainty it resolves.

Example:

```text
Scientific purpose:
Determine whether the candidate biomarker identified in the discovery cohort remains associated with treatment response after adjustment for clinically relevant covariates.
```

Not:

```text
Scientific purpose:
Publish a Scopus Q1 article.
```

Publication is an output, not the scientific purpose.

---

# Knowledge Function

Classify the primary knowledge function of each stage.

Possible values include:

- `DISCOVERY`
- `DESCRIPTION`
- `MAPPING`
- `CHARACTERIZATION`
- `ASSOCIATION`
- `COMPARISON`
- `EXPLANATION`
- `MECHANISM`
- `PREDICTION`
- `VALIDATION`
- `REPLICATION`
- `INTERVENTION`
- `IMPLEMENTATION`
- `TRANSLATION`
- `METHOD_DEVELOPMENT`
- `MEASUREMENT_DEVELOPMENT`
- `SYNTHESIS`
- `THEORY_DEVELOPMENT`
- `THEORY_TESTING`
- `CONTEXTUALIZATION`
- `FEASIBILITY`
- `OPTIMIZATION`
- `SAFETY`
- `POLICY_EVALUATION`

A stage may have secondary functions, but identify one primary function.

---

# Evidence Dependency

Every stage must identify which prior evidence justifies it.

Use:

```yaml
evidence_dependency:
  established_findings:
  unresolved_findings:
  validated_gap:
  audited_novelty:
  prior_stage_output:
  phenomenon_context:
  theoretical_or_mechanistic_basis:
```

If a stage cannot be justified by upstream evidence, it may be speculative.

Label speculative stages explicitly.

---

# Dependency Types

Dependencies may be:

- scientific;
- methodological;
- measurement;
- data;
- infrastructure;
- regulatory;
- ethical;
- capability;
- recruitment;
- computational;
- translational;
- financial;
- partnership;
- or temporal.

Distinguish hard dependencies from soft dependencies.

Use:

```yaml
dependency:
  type:
  source_stage:
  target_stage:
  strength: HARD | SOFT
  rationale:
  consequence_if_unmet:
```

---

# Hard Dependency

A hard dependency means the later stage should not proceed without the earlier result.

Example:

```text
External validation cannot proceed until the prediction model has been fully specified and internally validated.
```

---

# Soft Dependency

A soft dependency improves the later stage but is not absolutely required.

Example:

```text
A qualitative stakeholder study may improve implementation design but is not required to complete laboratory validation.
```

---

# Parallel Workstreams

Do not force all stages into one chain.

Some research programs require parallel workstreams.

Example:

```text
              ┌─ Biomarker Validation ─┐
Discovery ────┤                        ├─ Integrated Prediction Model
              └─ Clinical Data Model ──┘
```

Another example:

```text
                    ┌─ Quantitative Effect Study
Problem Definition ─┤
                    └─ Qualitative Context Study
                              ↓
                       Mixed-Method Integration
```

Represent parallelism explicitly.

---

# Branching Logic

A roadmap may branch depending on findings.

Use:

```text
Stage 1
  ↓
Decision Gate
  ├─ if supported → Stage 2A
  ├─ if partially supported → Stage 2B
  └─ if unsupported → Reframe or stop
```

Do not write a roadmap as though every planned result will be positive.

---

# Decision Gates

Every major transition should have a `DECISION_GATE`.

Use:

```yaml
decision_gate:
  gate_id:
  after_stage:
  decision_question:
  required_evidence:
  proceed_if:
  revise_if:
  stop_if:
  alternative_route:
```

A decision gate protects the roadmap from confirmation bias.

---

# Examples of Decision Gates

Examples include:

```text
Does the candidate association replicate in an independent sample?
```

```text
Does the instrument meet prespecified reliability and validity requirements?
```

```text
Does the formulation remain stable under the intended storage conditions?
```

```text
Does the prediction model retain acceptable calibration and discrimination in external validation?
```

```text
Is the intervention feasible and acceptable enough to justify an effectiveness trial?
```

---

# Stop Rules

A roadmap must permit scientifically valid termination.

Possible stop conditions include:

- candidate mechanism unsupported;
- effect not replicated;
- measurement system invalid;
- unacceptable safety profile;
- feasibility inadequate;
- resource requirements unrealistic;
- validated gap substantially resolved by new literature;
- novelty no longer defensible;
- stronger competing explanation emerges;
- new regulation blocks progression;
- or translational value becomes negligible.

Stopping a line of research can be a successful scientific outcome.

---

# Revalidation Gates

Long-term roadmaps become stale.

Before major later stages, revalidate:

- current literature;
- State of the Art;
- research gap;
- novelty;
- technology landscape;
- regulatory environment;
- feasibility;
- available methods;
- and competing studies.

Use:

```text
ROADMAP STAGE
     ↓
CURRENT-EVIDENCE RECHECK
     ↓
PROCEED / MODIFY / REFRAME / STOP
```

---

# Literature Currency

A roadmap is not a permanent claim about the future.

Before initiating a later stage:

- update literature search;
- verify newly discovered sources;
- screen relevant evidence;
- update synthesis;
- reassess closest competitors;
- and re-audit novelty when appropriate.

Route to:

- `scopus-literature-search`;
- `source-verification`;
- `reference-integrity-guard`;
- `citation-chaining`;
- `literature-screening`;
- `evidence-synthesis`;
- `sota-builder`;
- `gap-validator`;
- `novelty-auditor`.

---

# Phenomenon Evidence

Real-world changes may alter roadmap priorities.

Examples include:

- disease burden;
- regulatory change;
- population shifts;
- policy changes;
- new surveillance data;
- new educational indicators;
- new environmental exposure patterns;
- technology adoption;
- service delivery changes;
- or market and implementation conditions.

Use `phenomenon-evidence-builder` to verify such context.

Do not use phenomenon evidence as a substitute for scholarly gap validation.

---

# Gap-to-Roadmap Mapping

Each major stage should map to a validated unresolved condition.

Use:

```yaml
gap_to_stage:
  gap_id:
  gap_status:
  roadmap_stage:
  why_this_stage_addresses_the_gap:
  residual_gap_after_stage:
```

A roadmap can address only part of a gap.

State the residual uncertainty explicitly.

---

# Novelty-to-Roadmap Mapping

Do not assume every stage is independently novel.

Some stages may be necessary validation or replication.

Use:

```yaml
novelty_to_stage:
  stage_id:
  novelty_role:
  what_is_novel:
  what_is_not_novel:
  closest_competitor:
  audit_status:
```

Possible novelty roles:

- `PRIMARY_NOVELTY_STAGE`
- `SECONDARY_NOVELTY_STAGE`
- `VALIDATION_STAGE`
- `REPLICATION_STAGE`
- `METHOD_SUPPORT_STAGE`
- `TRANSLATIONAL_STAGE`
- `NON_NOVEL_BUT_NECESSARY_STAGE`

A scientifically necessary non-novel stage is acceptable.

---

# Prior Research Integration

When previous studies exist, reconstruct:

```text
Previous Study 1
       ↓
Established Finding A
       ↓
Unresolved Limitation A
       ↓
Previous Study 2
       ↓
Established Finding B
       ↓
Current Opportunity
```

Use:

- `research-resume`;
- `prior-research-auditor`;
- `research-trajectory-mapper`;
- `continuation-opportunity-finder`.

Do not treat every previous publication as equally important.

---

# Research Trajectory Coherence

Assess whether the roadmap:

- deepens an existing scientific question;
- broadens it intentionally;
- tests a mechanism;
- validates a prior finding;
- translates evidence;
- develops required methods;
- resolves contradictions;
- or opens a defensible new branch.

If the roadmap shifts topic substantially, label the transition.

Do not fabricate continuity merely to make a career history look coherent.

---

# Continuation Opportunity Ranking

Candidate next studies may be compared by:

- scientific value;
- gap strength;
- novelty defensibility;
- feasibility;
- dependency position;
- capability fit;
- translational potential;
- time sensitivity;
- risk;
- evidence maturity;
- and strategic leverage.

Do not rank by:

- journal quartile;
- citation potential;
- fashionable terminology;
- grant attractiveness alone;
- or ease of publication.

---

# Research Program Portfolio

A mature roadmap may contain several workstreams.

Use:

```yaml
research_program:
  program_name:
  central_scientific_problem:
  long_term_goal:
  workstreams:
    - workstream_id:
      theme:
      purpose:
      stages:
  integration_points:
  major_decision_gates:
  final_expected_knowledge_state:
```

---

# Workstream Types

Possible workstreams include:

- discovery;
- mechanism;
- methods;
- measurement;
- experimental;
- clinical;
- population;
- qualitative;
- implementation;
- policy;
- computational;
- translational;
- formulation;
- validation;
- education;
- engineering;
- or evidence synthesis.

Do not create workstreams merely for organizational symmetry.

---

# Milestones

A milestone should represent a scientifically meaningful state change.

Prefer:

- validated instrument;
- replicated association;
- externally validated model;
- stable formulation;
- verified mechanism;
- completed feasibility threshold;
- reproducible protocol;
- resolved contradiction;
- completed evidence synthesis.

Avoid treating these as scientific milestones:

- manuscript submitted;
- journal accepted;
- conference attended;
- software purchased;
- grant application filed.

These may be administrative milestones, but distinguish them clearly.

---

# Scientific Milestone Schema

Use:

```yaml
milestone:
  milestone_id:
  stage_id:
  milestone_type:
  evidence_required:
  completion_rule:
  downstream_unlocks:
  scientific_significance:
```

---

# Administrative Milestones

Administrative milestones may include:

- ethics approval;
- data-use agreement;
- contract execution;
- participant recruitment launch;
- equipment acquisition;
- database lock;
- manuscript submission;
- grant submission.

They are important but should not be confused with scientific knowledge milestones.

---

# Capability Roadmap

A research roadmap may require capability development.

Possible capability domains include:

- laboratory methods;
- analytical chemistry;
- molecular biology;
- sequencing;
- bioinformatics;
- statistical modeling;
- qualitative interviewing;
- mixed-method integration;
- clinical recruitment;
- data engineering;
- software development;
- regulatory science;
- implementation science;
- systematic review;
- meta-analysis;
- or advanced instrumentation.

Use:

```yaml
capability_requirement:
  capability:
  current_status:
  required_stage:
  gap:
  development_action:
  collaborator_option:
  validation_requirement:
```

---

# Collaboration Logic

Do not add collaborators merely to make a roadmap look multidisciplinary.

Add collaboration when a stage requires expertise not defensibly available within the current team.

For each collaboration, state:

- expertise needed;
- scientific role;
- stage requiring it;
- dependency;
- and whether the collaboration is essential or optional.

---

# Infrastructure Logic

Identify infrastructure only when scientifically relevant.

Examples:

- laboratory equipment;
- specialized assay platform;
- clinical site;
- biobank;
- computing infrastructure;
- secure data environment;
- field access;
- validated software pipeline;
- pilot manufacturing capability.

Do not allow existing equipment to determine the scientific question.

---

# Feasibility Layer

Assess feasibility at each stage.

Use:

```yaml
stage_feasibility:
  participants_or_samples:
  data_access:
  recruitment:
  equipment:
  expertise:
  ethics:
  regulation:
  time:
  budget:
  collaboration:
  overall_status:
```

Possible values:

- `FEASIBLE`
- `FEASIBLE_WITH_CONDITIONS`
- `UNCERTAIN`
- `CURRENTLY_INFEASIBLE`

---

# Risk Layer

Research roadmaps should represent scientific and operational risk.

Possible risk categories:

- conceptual;
- evidence;
- measurement;
- recruitment;
- technical;
- methodological;
- statistical;
- regulatory;
- ethical;
- computational;
- implementation;
- translation;
- partnership;
- budget;
- timeline.

Use:

```yaml
roadmap_risk:
  risk_id:
  stage_id:
  category:
  description:
  probability:
  impact:
  mitigation:
  trigger:
  contingency_route:
```

---

# Scientific Risk Versus Project Risk

Distinguish:

```text
Scientific risk:
The proposed mechanism may be wrong.
```

from:

```text
Project risk:
Recruitment may be slower than expected.
```

Both matter, but they require different responses.

---

# Negative Findings

A roadmap must remain useful if results are negative.

For each high-risk stage, ask:

> If the expected result is not observed, what scientifically meaningful path remains?

Possible outcomes:

- reject mechanism;
- refine theory;
- identify boundary condition;
- validate null effect;
- change population;
- improve measurement;
- redirect to alternative mechanism;
- or terminate the branch.

Do not assume positive findings.

---

# Replication

Replication may be an essential roadmap stage.

Do not downgrade replication merely because it appears less novel.

Replication is particularly important when:

- evidence comes from one population;
- sample size was small;
- effect estimates are unstable;
- methods changed;
- findings conflict;
- external validity is uncertain;
- or later translational stages depend on the finding.

---

# Validation

Validation must be separated from discovery.

Possible validation stages include:

- internal validation;
- temporal validation;
- geographic validation;
- external cohort validation;
- analytical validation;
- clinical validation;
- construct validation;
- criterion validation;
- cross-cultural validation;
- technological validation.

Do not claim validation from reuse of the same evidence used for discovery unless scientifically justified.

---

# Mechanistic Progression

A mechanism-oriented roadmap may use:

```text
Observed Association
        ↓
Candidate Mechanism
        ↓
Mechanistic Test
        ↓
Independent Replication
        ↓
Boundary Conditions
        ↓
Intervention Target
```

Do not infer mechanism from association alone.

---

# Prediction Progression

A prediction-oriented roadmap may use:

```text
Predictor Discovery
       ↓
Model Development
       ↓
Internal Validation
       ↓
External Validation
       ↓
Calibration / Updating
       ↓
Clinical or Operational Utility
       ↓
Implementation Evaluation
```

Do not move to deployment before appropriate validation.

---

# Diagnostic Progression

A diagnostic roadmap may use:

```text
Candidate Marker
      ↓
Analytical Validity
      ↓
Diagnostic Accuracy
      ↓
External Validation
      ↓
Clinical Utility
      ↓
Implementation
```

Do not equate association with diagnostic utility.

---

# Pharmacogenetic / Precision-Medicine Progression

A pharmacogenetic roadmap may include:

```text
Variant / Biomarker Association
        ↓
Replication
        ↓
Mechanistic Interpretation
        ↓
Multivariable Prediction
        ↓
External Validation
        ↓
Clinical Decision Model
        ↓
Prospective Utility Study
        ↓
Implementation
```

Do not assume genotype association automatically supports clinical decision use.

---

# Pharmacokinetic / PBPK Progression

A PBPK-oriented roadmap may include:

```text
Physiological Data Assembly
        ↓
Model Development
        ↓
Verification
        ↓
Population Calibration
        ↓
External Evaluation
        ↓
Sensitivity / Uncertainty Analysis
        ↓
Dose Scenario Simulation
        ↓
Prospective Clinical Validation
```

Do not treat simulation alone as clinical validation.

---

# Formulation / Pharmaceutical Development Progression

A formulation roadmap may include:

```text
Material Characterization
        ↓
Formulation Design
        ↓
Optimization
        ↓
Physicochemical Evaluation
        ↓
Stability
        ↓
Biological Activity
        ↓
Safety
        ↓
Preclinical Evaluation
        ↓
Clinical Translation
```

Do not force later stages when the formulation fails basic quality criteria.

---

# Education Research Progression

An education roadmap may include:

```text
Problem Mapping
      ↓
Needs Analysis
      ↓
Conceptual Model
      ↓
Instrument Development
      ↓
Intervention Design
      ↓
Pilot Feasibility
      ↓
Effectiveness Evaluation
      ↓
Implementation
```

Qualitative explanatory work may occur before, during, or after quantitative stages when scientifically justified.

---

# Social-Science Progression

A social-science roadmap may include:

```text
Phenomenon Exploration
       ↓
Conceptual Clarification
       ↓
Theory Development / Selection
       ↓
Measurement
       ↓
Association / Explanation
       ↓
Cross-context Validation
       ↓
Intervention or Policy Evaluation
```

Do not force quantitative progression if interpretive depth is the scientific objective.

---

# Engineering Progression

An engineering roadmap may include:

```text
Problem Definition
      ↓
Design Requirements
      ↓
Prototype
      ↓
Bench Validation
      ↓
Optimization
      ↓
Robustness
      ↓
Field Testing
      ↓
Scale-up
```

Do not equate prototype novelty with demonstrated performance.

---

# Evidence-Synthesis Progression

An evidence-synthesis roadmap may include:

```text
Landscape Mapping
      ↓
Systematic Review
      ↓
Meta-analysis when appropriate
      ↓
Contradiction Analysis
      ↓
Evidence-Gap Mapping
      ↓
Priority Research Questions
```

Do not force meta-analysis when studies are not scientifically poolable.

---

# Temporal Horizon

After scientific sequencing is clear, assign indicative horizons.

Possible categories:

- `NEAR_TERM`
- `MID_TERM`
- `LONG_TERM`

or actual years when requested.

Do not assign time before determining dependencies.

---

# Year Mapping

When a user requires annual planning, use:

```yaml
year_plan:
  year:
  active_stages:
  scientific_milestones:
  enabling_activities:
  decision_gates:
  expected_outputs:
  dependencies:
```

A single stage may span multiple years.

Several stages may occur in one year.

---

# Calendar Uncertainty

Do not present timing as precise when it depends on:

- recruitment;
- ethics;
- funding;
- sample availability;
- laboratory optimization;
- validation outcomes;
- regulatory review;
- or partner readiness.

Use ranges or conditional timing.

---

# Research Outputs

Outputs may include:

- datasets;
- validated instruments;
- validated models;
- protocols;
- software;
- assays;
- mechanisms;
- theoretical contributions;
- evidence syntheses;
- policy recommendations;
- implementation frameworks;
- prototypes;
- formulations;
- publications;
- patents;
- clinical decision tools;
- or educational resources.

Distinguish knowledge output from dissemination output.

---

# Publication Outputs

Publications may be mapped to stages, but publication must not determine the scientific design.

Use:

```yaml
publication_output:
  stage_id:
  scientific_story:
  article_type:
  likely_audience:
  timing:
```

Do not prematurely select a journal if the manuscript does not yet exist.

Route later to `journal-matcher`.

---

# Journal Independence

Do not redesign a roadmap because:

- a journal prefers a particular method;
- a quartile is more prestigious;
- a journal has no APC;
- a special issue is open;
- a publisher is fashionable;
- or a journal is likely to accept the paper.

Scientific progression comes first.

Publication strategy comes later.

---

# Funding Independence

A funding call may influence feasibility and timing, but it must not create a false scientific gap.

If a grant theme is relevant, map it after scientific justification.

Use:

```text
Scientific Need
      ↓
Roadmap Stage
      ↓
Funding Fit
```

not:

```text
Funding Call
      ↓
Invented Research Gap
```

---

# Institutional Strategy

Institutional priorities may help choose among multiple scientifically valid options.

They must not override evidence quality.

Possible strategy factors:

- research center focus;
- available infrastructure;
- national priority;
- translational mission;
- local population access;
- educational mission;
- interdisciplinary strength.

Label strategy factors separately from scientific justification.

---

# SDG / Policy Alignment

SDG, national priority, or policy alignment may be reported when relevant.

Do not use policy alignment as proof of novelty.

Use:

```yaml
policy_alignment:
  stage_id:
  framework:
  relevance:
  evidence:
  role: CONTEXTUAL | IMPLEMENTATION | STRATEGIC
```

---

# Roadmap Coherence Test

For each stage ask:

1. Does this stage answer a real unresolved question?
2. Is the unresolved question supported by current evidence?
3. Is the stage dependent on previous evidence?
4. Is the proposed contribution proportionate?
5. Is the stage feasible?
6. Is the next stage unlocked by this result?
7. Is there a decision gate?
8. What happens if the result is negative?
9. Is this stage scientifically necessary?
10. Is it being included only because it sounds advanced?

Remove decorative stages.

---

# Redundancy Test

Two stages may be redundant when they:

- answer essentially the same question;
- use equivalent designs without new inferential value;
- repeat the same population without justification;
- add a variable without scientific rationale;
- repeat validation unnecessarily;
- or split one coherent study merely to increase publication count.

Merge redundant stages where appropriate.

---

# Artificial Complexity Guard

Do not add:

- mediators;
- moderators;
- omics layers;
- AI;
- machine learning;
- SEM;
- PLS-SEM;
- imaging;
- sequencing;
- blockchain;
- digital twins;
- or other technologies

merely to make a roadmap appear advanced.

Add complexity only when it resolves a defined scientific uncertainty.

---

# Software Independence

Do not allow:

- SmartPLS;
- AMOS;
- SPSS;
- Jamovi;
- R;
- Python;
- MATLAB;
- NVivo;
- Atlas.ti;
- or any other software

to define the scientific roadmap.

Software is an implementation choice after the scientific requirement is clear.

---

# Method Independence

Do not decide that later stages must use:

- RCT;
- cohort;
- cross-sectional survey;
- qualitative interviews;
- PLS-SEM;
- meta-analysis;
- machine learning;
- laboratory experiment;
- or another method

until the research question and intended inference justify that design.

Route specific design decisions to `methodology-architect`.

---

# Research Question Handoff

When a roadmap stage is mature enough to become a concrete study, route to:

`research-question-builder`

The roadmap stage should provide:

- unresolved question;
- intended contribution;
- boundaries;
- dependency context;
- evidence need;
- feasibility;
- and expected knowledge function.

---

# Problem-Solving Handoff

After the research question is finalized, route to:

`problem-solving-approach`

Then:

`methodology-architect`

The roadmap must not pre-empt detailed methodological design.

---

# Theory Handoff

If a stage requires explicit theoretical grounding, route to:

`theoretical-framework`

Do not force theory into every roadmap stage.

---

# Hypothesis Handoff

If hypothesis testing is scientifically appropriate, route to:

`hypothesis-builder`

Do not generate hypotheses merely because a roadmap stage is quantitative.

---

# Conceptual Framework Handoff

When useful or required, route to:

`conceptual-framework`

The conceptual framework should represent the study-specific structure, not the entire long-term roadmap.

---

# Implication Handoff

Use `implication-builder` upstream when results have already been interpreted and discussed.

Implications may generate:

- translation opportunities;
- implementation stages;
- validation needs;
- policy questions;
- future research priorities.

Do not treat every implication as a mandatory roadmap stage.

---

# Manuscript Handoff

When a stage has completed evidence and is ready for publication development, route to:

- `manuscript-architect`;
- `manuscript-writer`;
- `manuscript-auditor`;
- `journal-matcher`;
- `reviewer-simulator`;
- `reviewer-response`.

Publication workflows are downstream from the science.

---

# Roadmap Table

A compact roadmap table may use:

| Stage | Scientific Question | Knowledge Function | Evidence Needed | Dependency | Decision Gate | Expected Contribution |
|---|---|---|---|---|---|---|

Add timing only when requested.

---

# Detailed Roadmap Table

For complex programs use:

| Stage | Purpose | Prior Evidence | Validated Gap | Novelty Role | Design Direction | Capability Need | Milestone | Gate | Next Route |
|---|---|---|---|---|---|---|---|---|---|

---

# Workstream Table

| Workstream | Central Question | Current Maturity | Next Stage | Long-Term Aim | Major Dependency |
|---|---|---|---|---|---|

---

# Risk Table

| Risk | Stage | Type | Probability | Impact | Mitigation | Alternative Route |
|---|---|---|---|---|---|---|

---

# Capability Table

| Capability | Current Status | Required Stage | Gap | Development Plan | Essential? |
|---|---|---|---|---|---|

---

# Decision-Gate Table

| Gate | Trigger | Evidence Required | Proceed | Revise | Stop |
|---|---|---|---|---|---|

---

# Research Roadmap Passport

For reusable downstream routing, create:

```yaml
research_roadmap_passport:
  roadmap_status:
  central_scientific_problem:
  current_evidence_state:
  prior_research_basis:
  validated_gaps:
  audited_novelty:
  long_term_goal:
  workstreams:
  stages:
  dependencies:
  decision_gates:
  revalidation_points:
  capabilities:
  risks:
  feasibility:
  expected_outputs:
  publication_outputs:
  near_term_priority:
  next_skill:
```

---

# Confidence

Assign confidence to major roadmap decisions.

Possible values:

- `HIGH`
- `MODERATE`
- `LOW`
- `PROVISIONAL`

Confidence should reflect:

- evidence quality;
- gap validation;
- novelty audit;
- feasibility clarity;
- dependency certainty;
- and literature currency.

Do not use confidence as a decorative label.

---

# Roadmap Status by Stage

Each stage may be:

- `READY_TO_FORMULATE_RQ`
- `REQUIRES_CURRENT_LITERATURE_UPDATE`
- `REQUIRES_GAP_VALIDATION`
- `REQUIRES_NOVELTY_AUDIT`
- `REQUIRES_FEASIBILITY_CHECK`
- `DEPENDENT_ON_PRIOR_STAGE`
- `PARALLEL_STAGE`
- `OPTIONAL_BRANCH`
- `SPECULATIVE_LONG_TERM`
- `STOPPED`
- `COMPLETED`

---

# Handling New Evidence

When new evidence appears:

1. identify which stage or dependency it affects;
2. verify the source;
3. determine whether it changes the State of the Art;
4. reassess the gap;
5. re-audit novelty if needed;
6. revise the roadmap only where scientifically necessary.

Do not rebuild the entire roadmap automatically.

---

# Handling a Published Competitor Study

If a competitor publishes a similar study:

- compare populations;
- compare methods;
- compare outcomes;
- compare mechanisms;
- compare timing;
- compare evidence strength;
- determine whether the gap is narrowed or closed;
- determine whether replication remains valuable;
- and update novelty claims.

Route to:

- `gap-validator`;
- `novelty-auditor`.

Do not assume the roadmap is invalid merely because a related paper appears.

---

# Handling a Failed Stage

If a stage fails scientifically:

- preserve the finding;
- determine why it failed;
- assess whether the hypothesis, mechanism, instrument, design, or feasibility assumption was wrong;
- update downstream dependencies;
- cancel stages that are no longer justified;
- create alternative routes only when evidence supports them.

A failed stage should not be hidden.

---

# Handling a Feasibility Failure

If a stage is scientifically strong but operationally infeasible:

- reduce scope only if scientific integrity is preserved;
- seek collaboration;
- modify timing;
- use an alternative population;
- use an alternative validated method;
- create a pilot stage;
- or defer the stage.

Do not silently replace the scientific question with an easier one.

---

# Handling Multiple Candidate Roadmaps

When several program architectures are plausible, compare them.

Use:

```yaml
roadmap_candidate:
  candidate_id:
  central_logic:
  strengths:
  weaknesses:
  scientific_risk:
  feasibility:
  dependency_complexity:
  expected_information_gain:
  translational_potential:
  confidence:
```

Do not choose automatically by simplicity.

Choose the roadmap that best balances scientific value and feasibility.

---

# Information Gain

A strong next stage should substantially reduce important uncertainty.

Ask:

> If this study succeeds, how much will our scientific understanding change?

and:

> If this study fails, will we still learn something important?

Prefer stages with meaningful information gain.

---

# Boundary Conditions

State where the roadmap is intended to apply.

Examples:

- population;
- disease;
- setting;
- age group;
- geography;
- technology maturity;
- formulation type;
- regulatory context;
- educational level;
- institutional context.

Do not imply universal applicability.

---

# Causal Boundary

Do not build later causal stages on non-causal evidence without an explicit bridge.

Example:

```text
Cross-sectional association
      ↓
Longitudinal confirmation
      ↓
Mechanistic investigation
      ↓
Intervention
```

Do not jump directly from association to intervention unless independently justified.

---

# Measurement Boundary

Do not build advanced models on invalid measurement.

If measurement is uncertain, create or route to a measurement-development stage.

Use:

`instrument-design`

---

# Reproducibility Boundary

Before later translational or implementation stages, ensure key findings are reproducible enough for the intended claim.

Reproducibility may require:

- independent sample;
- independent laboratory;
- temporal replication;
- external validation;
- alternative method;
- robustness analysis.

---

# Ethics Boundary

Later stages must not be planned as though ethics approval is guaranteed.

Identify ethical dependencies when relevant.

Do not invent approval status.

---

# Regulatory Boundary

Regulatory requirements may affect:

- clinical research;
- medical devices;
- diagnostics;
- pharmaceuticals;
- genetic testing;
- data privacy;
- human subjects;
- animal studies;
- environmental interventions.

Verify current requirements before operational planning.

Do not fabricate regulatory claims.

---

# Translation Readiness

Before translational stages, assess whether the evidence has reached sufficient maturity.

Possible statuses:

- `TRANSLATION_NOT_YET_JUSTIFIED`
- `PRELIMINARY_TRANSLATION`
- `VALIDATION_REQUIRED`
- `UTILITY_EVALUATION_READY`
- `IMPLEMENTATION_READY`

Do not equate promising results with implementation readiness.

---

# Implementation Readiness

Implementation research may require:

- demonstrated effectiveness;
- acceptable safety;
- stakeholder acceptability;
- feasibility;
- organizational readiness;
- cost considerations;
- contextual adaptation.

Do not place implementation merely because it sounds like an advanced final stage.

---

# Commercialization

Commercialization is optional and domain-dependent.

If relevant, separate:

```text
Scientific Validation
      ↓
Technical Validation
      ↓
Regulatory / Market Assessment
      ↓
Commercialization
```

Do not label commercialization as a scientific outcome.

---

# Intellectual Property

IP may be relevant for:

- inventions;
- formulations;
- devices;
- algorithms;
- assays;
- software;
- processes.

Do not let IP strategy distort evidence interpretation.

When needed, treat IP as a parallel translational consideration.

---

# Roadmap Narrative

A roadmap narrative should explain:

1. the starting evidence state;
2. the central unresolved problem;
3. why the first next stage is scientifically necessary;
4. what evidence that stage must produce;
5. what later stages depend on it;
6. where branching may occur;
7. how the program matures;
8. what the long-term knowledge state should become.

Do not merely restate the table.

---

# Short Narrative Template

```text
The roadmap begins from [established evidence]. The immediate unresolved issue is [validated uncertainty]. Therefore, the first stage will address [question] because [scientific rationale]. If [decision criterion] is met, the program will proceed to [next stage]; otherwise, it will [alternative route]. Subsequent stages progressively address [validation/mechanism/translation/etc.], with revalidation of the literature and novelty before major transitions. The long-term objective is to establish [defensible final knowledge state].
```

---

# Long-Term Goal

A long-term goal should describe the intended knowledge or capability state.

Prefer:

```text
Establish and externally validate a clinically interpretable model for identifying patients at high risk of treatment failure.
```

Avoid:

```text
Publish five Scopus papers.
```

---

# Research Program Maturity

Possible maturity levels:

- `FOUNDATIONAL`
- `EMERGING`
- `DEVELOPING`
- `VALIDATING`
- `TRANSLATIONAL`
- `IMPLEMENTING`
- `MATURE`

Use these only when meaningful.

Do not automatically assume that later calendar years represent higher maturity.

---

# Roadmap Audit

Before finalizing, audit:

- scientific coherence;
- evidence traceability;
- dependency correctness;
- stage necessity;
- gap validity;
- novelty proportionality;
- feasibility;
- negative-result handling;
- decision gates;
- literature revalidation;
- capability needs;
- ethical constraints;
- regulatory constraints;
- publication independence;
- and strategic distortion.

---

# Publication-Pressure Guard

Reject roadmap logic such as:

- one publication per year regardless of science;
- splitting one study into multiple weak projects;
- adding variables solely for novelty;
- choosing topics because they are easier to publish;
- changing endpoints to fit journals;
- adding fashionable methods without scientific need;
- or keeping a research line alive only because it already has publications.

---

# Prestige Guard

Do not prioritize a roadmap stage because:

- it may reach a Q1 journal;
- it may attract many citations;
- it may be popular on social media;
- it uses a fashionable technology;
- or it resembles work from a prestigious institution.

Scientific value must remain primary.

---

# APC Guard

APC preference may influence journal selection later.

It must not influence:

- evidence inclusion;
- gap identification;
- novelty;
- study design;
- roadmap sequencing;
- or scientific priority.

---

# Contradictory Evidence

Contradictory evidence may generate valuable roadmap stages.

Possible routes:

```text
Contradiction
    ↓
Methodological Reconciliation
```

or:

```text
Contradiction
    ↓
Boundary-Condition Study
```

or:

```text
Contradiction
    ↓
Replication
```

Do not suppress contradictory findings to preserve roadmap continuity.

---

# Null Evidence

Null or non-significant findings may justify:

- replication;
- precision improvement;
- alternative mechanism testing;
- boundary analysis;
- measurement review;
- or stopping the line.

Do not interpret null results automatically as failure.

---

# Uncertainty Preservation

Use explicit labels when uncertainty remains.

Examples:

- `UNCERTAIN_DEPENDENCY`
- `PROVISIONAL_STAGE`
- `UNVERIFIED_LONG_TERM_BRANCH`
- `FEASIBILITY_UNKNOWN`
- `NOVELTY_REVALIDATION_REQUIRED`

Do not hide uncertainty behind confident prose.

---

# User-Facing Behavior

Do not expose unnecessary internal routing language unless useful.

Instead of:

```text
I am routing to gap-validator.
```

Prefer:

```text
Before treating this as the next major research stage, the proposed gap still needs to be checked against the latest evidence.
```

Instead of:

```text
Stage status is ROADMAP_REQUIRES_NOVELTY_AUDIT.
```

Prefer:

```text
The scientific direction is plausible, but the claimed contribution should still be compared with the closest current studies before we lock it into the roadmap.
```

---

# Beginner-Friendly Behavior

For users who only know their broad research history:

1. reconstruct previous work;
2. identify the strongest established finding;
3. identify the most important unresolved issue;
4. check current literature;
5. propose a small number of continuation options;
6. then build the roadmap.

Do not require users to understand roadmap terminology first.

---

# Advanced-Researcher Behavior

For experienced users, support:

- multi-workstream research programs;
- decision-tree roadmaps;
- research portfolio balancing;
- dependency graphs;
- translational maturity;
- validation ladders;
- capability planning;
- grant sequencing;
- team-level programs;
- cross-disciplinary integration;
- and research-center strategy.

Still preserve scientific evidence as the primary driver.

---

# Output Modes

The user may request:

- concise roadmap;
- detailed roadmap;
- annual roadmap;
- 3-year roadmap;
- 5-year roadmap;
- doctoral roadmap;
- laboratory roadmap;
- research-group roadmap;
- grant roadmap;
- publication-support roadmap;
- translational roadmap;
- visual roadmap;
- table;
- narrative;
- or staged workflow.

Adapt format without changing scientific logic.

---

# Minimal Output

When a concise answer is appropriate, provide:

```text
Current evidence
↓
Priority unresolved question
↓
Next study
↓
Decision gate
↓
Second-stage study
↓
Long-term direction
```

---

# Full Output

When comprehensive output is requested, provide:

1. starting evidence state;
2. central scientific problem;
3. validated gaps;
4. audited novelty;
5. research-program goal;
6. workstreams;
7. stage-by-stage roadmap;
8. dependencies;
9. decision gates;
10. capability requirements;
11. feasibility;
12. risk and contingency;
13. revalidation points;
14. expected outputs;
15. indicative timeline;
16. next immediate research action.

---

# Roadmap Quality Classification

Use one of:

- `SCIENTIFICALLY_COHERENT`
- `COHERENT_WITH_REVALIDATION_NEEDED`
- `PARTIALLY_COHERENT`
- `FRAGMENTED`
- `PUBLICATION_DRIVEN`
- `METHOD_DRIVEN`
- `TECHNOLOGY_DRIVEN`
- `INSUFFICIENT_EVIDENCE`

Explain the classification briefly.

---

# Relationship with Research Resume

Use `research-resume` to recover the state of an existing research program.

Then use `research-roadmap` to decide where the program should go next.

Do not use roadmap construction to rewrite history.

---

# Relationship with Prior Research Auditor

Use `prior-research-auditor` to determine what earlier studies actually established and where their limitations lie.

The roadmap must use audited prior evidence rather than author memory alone.

---

# Relationship with Research Trajectory Mapper

Use `research-trajectory-mapper` to reconstruct how multiple prior studies connect.

Then use `research-roadmap` to design the future trajectory.

Trajectory mapping is retrospective.

Roadmapping is prospective.

---

# Relationship with Continuation Opportunity Finder

Use `continuation-opportunity-finder` to generate and prioritize plausible next studies.

Use `research-roadmap` to sequence the selected opportunities into a cumulative program.

---

# Relationship with Research Landscape

Use `research-landscape` to understand the structure of the field before long-term positioning.

A roadmap should not be built from an isolated local view when broader field structure matters.

---

# Relationship with Trend Detection

Use `trend-detection` when temporal shifts may affect roadmap relevance.

Do not equate a trend with a research priority automatically.

---

# Relationship with Emerging Topic Discovery

Use `emerging-topic-discovery` to identify genuinely developing areas.

Emerging topics may become roadmap branches only after evidence assessment.

---

# Relationship with State of the Art

Use `sota-builder` to establish what the field currently knows.

The roadmap begins from the current scientific frontier, not merely from the researcher's previous publication.

---

# Relationship with Gap Validator

Use `gap-validator` before using a claimed unresolved issue as a major roadmap foundation.

A weak or rejected gap should not anchor a long-term research program.

---

# Relationship with Novelty Auditor

Use `novelty-auditor` before assigning strong novelty claims to roadmap stages.

Later stages may require re-audit because novelty changes over time.

---

# Relationship with Implication Builder

Use `implication-builder` to identify legitimate consequences of completed findings.

Some implications may become future roadmap stages.

Others may remain recommendations rather than research questions.

---

# Relationship with Research Question Builder

Use `research-question-builder` to convert a roadmap stage into a precise study question.

The roadmap itself should not substitute for study-level research questions.

---

# Relationship with Problem-Solving Approach

Use `problem-solving-approach` after a research question is sufficiently clear.

It determines what kind of evidence must be generated.

---

# Relationship with Methodology Architect

Use `methodology-architect` to translate a selected roadmap stage into a defensible study design.

The roadmap specifies scientific progression.

Methodology specifies study architecture.

---

# Relationship with Analysis Planner

Use `analysis-planner` only after the study design and data-generating structure are sufficiently defined.

Do not preselect analysis methods merely to decorate future roadmap stages.

---

# Relationship with Manuscript Workflows

A research roadmap may anticipate scientific outputs, but manuscript construction occurs downstream.

Use:

- `manuscript-architect`;
- `manuscript-writer`;
- `manuscript-auditor`.

Do not design the research merely to fit a predetermined manuscript structure.

---

# Relationship with Journal Matcher

Use `journal-matcher` only when a sufficiently stable manuscript exists.

Do not choose journals as roadmap stages.

---

# Relationship with Reviewer Simulation

Reviewer simulation may reveal future research needs, but reviewer criticism must first be evaluated scientifically.

Do not add roadmap stages merely to appease a simulated reviewer.

---

# Relationship with Reviewer Response

Actual reviewer comments may reveal unresolved scientific issues.

When scientifically valid, route them upstream to the appropriate skill.

Only after the issue is understood should the roadmap be revised.

---

# Avoid These Behaviors

Do not:

- create a roadmap from publication targets alone;
- assume all future stages will succeed;
- hide negative or null results;
- force linear progression;
- force every project into one theme;
- fabricate continuity;
- inflate novelty;
- treat geographic difference alone as sufficient novelty;
- treat new software as scientific novelty;
- use journal prestige as a priority criterion;
- use APC status as a scientific criterion;
- add advanced methods for appearance;
- skip replication when later claims depend on it;
- skip validation before implementation;
- confuse association with mechanism;
- confuse prediction with causation;
- confuse simulation with clinical validation;
- confuse feasibility with effectiveness;
- confuse effectiveness with implementation;
- confuse policy relevance with evidence of causality;
- confuse publication with scientific milestone;
- or declare a roadmap definitive when major evidence is missing.

---

# Stop Conditions

Do not finalize a confident research roadmap when:

- previous research cannot be reconstructed sufficiently;
- key prior findings have not been audited;
- the State of the Art is materially outdated;
- the central gap is unvalidated;
- the novelty claim is materially uncertain;
- continuation options have not been compared where needed;
- critical feasibility constraints are unknown;
- later stages depend on assumed positive results;
- scientific dependencies are unclear;
- the roadmap is primarily publication-driven;
- the roadmap is primarily method-driven;
- the roadmap is primarily technology-driven;
- or the long-term direction depends on unsupported assumptions.

Instead use one or more of:

- `RETURN_TO_RESEARCH_RESUME`
- `RETURN_TO_PRIOR_RESEARCH_AUDITOR`
- `RETURN_TO_RESEARCH_TRAJECTORY_MAPPER`
- `RETURN_TO_CONTINUATION_OPPORTUNITY_FINDER`
- `RETURN_TO_SCOPUS_LITERATURE_SEARCH`
- `RETURN_TO_SOTA_BUILDER`
- `RETURN_TO_GAP_VALIDATOR`
- `RETURN_TO_NOVELTY_AUDITOR`
- `RETURN_TO_IMPLICATION_BUILDER`
- `ROADMAP_REQUIRES_FEASIBILITY_CLARIFICATION`
- `ROADMAP_REQUIRES_REVISION`
- `ROADMAP_PROVISIONAL`

when appropriate.

---

# Success Criterion

`research-roadmap` succeeds when previous research, current State-of-the-Art evidence, validated uncertainties, audited scientific opportunities, defensible implications, researcher capabilities, feasibility constraints, and long-term goals have been transformed into a coherent prospective research program whose stages each have a clear scientific purpose, evidence dependency, expected contribution, decision gate, success and failure logic, capability requirement, and downstream route; when parallel workstreams, branching pathways, replication, validation, negative findings, revalidation points, and stop rules are represented where scientifically necessary; when near-term, mid-term, and long-term priorities reflect knowledge dependency rather than calendar convenience; when publication targets, journal prestige, Scopus status, APC preferences, funding calls, fashionable technologies, software availability, or methodological familiarity do not redefine the scientific problem; when the roadmap can be updated as evidence changes rather than being treated as a fixed prediction of the future; and when the researcher can identify the single most defensible next study while also understanding how that study may contribute to a cumulative, evidence-grounded long-term research trajectory.
