---
name: sota-builder
description: Build a defensible State of the Art from verified, screened, and synthesized scholarly evidence by distinguishing established knowledge, emerging evidence, contested findings, unresolved questions, methodological frontiers, theoretical developments, and current scientific boundaries. Use before research-gap discovery, gap validation, novelty construction, research-question refinement, continuation-study selection, methodology development, or competitive manuscript positioning.
---

# State of the Art Builder

## Purpose

`sota-builder` constructs the current scientific State of the Art from verified and synthesized evidence.

Its central question is:

> What does the best available evidence currently establish, where is the scientific frontier moving, what remains contested, and what is still unresolved?

The purpose is not to produce a chronological literature review.

The purpose is to establish the present position of the field so that later decisions about:

- research gaps;
- novelty;
- research questions;
- continuation studies;
- methodology;
- manuscript positioning;

are scientifically defensible.

---

# Core Principle

Use:

> State of the Art is the current structure and frontier of scientific knowledge, not a list of recent publications.

A strong State of the Art should distinguish:

1. what is established;
2. what is emerging;
3. what is contested;
4. what is unresolved.

These categories form the minimum architecture of the SoTA.

---

# Required Upstream Evidence

Prefer evidence processed through:

`scopus-literature-search`
→ `source-verification`
→ `reference-integrity-guard`
→ `citation-chaining`
→ `literature-screening`
→ `evidence-synthesis`

Do not construct a confident SoTA from:

- unverified references;
- search-engine snippets;
- isolated abstracts;
- one review article;
- one journal;
- only supportive literature.

---

# Activation Conditions

Use this skill when the researcher asks:

- "What is the State of the Art?"
- "What is currently known?"
- "Where is the scientific frontier?"
- "What has already been established?"
- "What remains unresolved?"
- "What is the current position of my research?"
- "How does my previous study compare with current science?"
- "I want to identify a defensible research gap."
- "Help me position this study for an international journal."

---

# 1. Define the SoTA Question

A State of the Art must answer a defined scientific problem.

Determine:

- research field;
- scientific phenomenon;
- population or context when relevant;
- major concepts;
- scientific purpose;
- time sensitivity.

Avoid producing a SoTA so broad that it becomes a general textbook overview.

---

# 2. Define the Evidence Boundary

State what evidence is represented.

Possible boundaries:

- global literature;
- specific discipline;
- specific population;
- intervention;
- technology;
- research design;
- publication period.

When the evidence corpus is incomplete, classify:

`PRELIMINARY_SOTA`

Do not present incomplete mapping as comprehensive.

---

# 3. Scopus-First Evidence Principle

Prioritize verified peer-reviewed evidence from active Scopus-indexed sources when appropriate.

However:

Scopus status does not replace:

- relevance;
- study quality;
- methodological rigor;
- evidence strength.

Authoritative non-Scopus sources may still be required for:

- regulations;
- standards;
- guidelines;
- official statistics;
- foundational books.

Clearly distinguish them.

---

# 4. Current Evidence Priority

SoTA must represent the present field.

Prioritize:

- recent high-quality primary research;
- recent systematic reviews;
- meta-analyses;
- recent validation studies;
- major methodological advances;
- current contradictory evidence.

Retain older studies when they remain:

- foundational;
- seminal;
- theoretically important;
- methodologically essential.

---

# 5. Field Velocity

Determine how rapidly the field changes.

Possible classifications:

- `FAST_MOVING`
- `MODERATELY_DYNAMIC`
- `SLOW_MOVING`
- `UNKNOWN`

Fast-moving fields require heavier weighting toward recent literature.

Do not apply a universal five-year rule.

---

# 6. Historical Foundation

Identify only the historical evidence needed to explain:

- origin of the concept;
- theory;
- major methodological foundation;
- important turning points.

Do not allow historical discussion to dominate the current SoTA.

---

# 7. Scientific Evolution

When useful, structure development as:

```text
Foundational Knowledge
        ↓
Major Scientific Development
        ↓
Current Dominant Approaches
        ↓
Current Best Evidence
        ↓
Scientific Frontier
```

This is an intellectual-development map, not a mandatory chronological narrative.

The purpose is to explain how the current scientific position emerged.

---

# 8. Evolution Record

Use when useful:

```yaml
scientific_evolution:
  foundational_knowledge:
  turning_points:
  dominant_current_approaches:
  current_best_evidence:
  frontier:
  superseded_approaches:
  unresolved_transitions:
```

Do not fabricate historical turning points.

---

# 9. Minimum SoTA Architecture

A defensible SoTA should distinguish at least:

```text
ESTABLISHED
EMERGING
CONTESTED
UNRESOLVED
FRONTIER
```

These categories are not interchangeable.

---

# 10. Established Knowledge

`ESTABLISHED` means the evidence is sufficiently mature and convergent that the proposition can be treated as a stable part of the current field within stated boundaries.

Possible signals:

- independent replication;
- convergent results;
- methodological maturity;
- consistent theoretical interpretation;
- external validation;
- stable definitions.

Publication volume alone is insufficient.

---

# 11. Established Knowledge Guard

Do not classify a proposition as established merely because:

- many papers repeat it;
- it is highly cited;
- a famous review states it;
- it appears in a prestigious journal;
- it is common practice.

Require evidence appropriate to the proposition.

---

# 12. Established Record

Use:

```yaml
established:
  proposition:
  supporting_evidence:
  independent_replication:
  population_scope:
  method_scope:
  boundary_conditions:
  contradictory_evidence:
  confidence:
  notes:
```

---

# 13. Emerging Evidence

`EMERGING` means scientifically meaningful evidence is accumulating but has not yet reached mature convergence.

Potential signals:

- recent independent studies;
- a new mechanism;
- preliminary validation;
- new methodology;
- early cross-population replication;
- rapidly developing conceptual integration.

Emerging does not mean established.

---

# 14. Emerging Evidence Guard

Do not classify something as emerging merely because it is:

- recent;
- technologically fashionable;
- highly visible online;
- frequently mentioned;
- published by influential authors.

Scientific novelty and temporal novelty are different.

---

# 15. Emerging Record

Use:

```yaml
emerging:
  proposition:
  first_signals:
  recent_evidence:
  replication_status:
  method_maturity:
  theoretical_status:
  major_uncertainty:
  frontier_potential:
```

---

# 16. Contested Evidence

`CONTESTED` means credible scientific evidence or interpretation remains in meaningful conflict.

Possible sources:

- contradictory results;
- competing theories;
- failed replications;
- measurement disagreement;
- methodological disagreement;
- population-specific reversals;
- causal interpretation disputes.

Contestation is a valid scientific state.

---

# 17. Contested Evidence Guard

Do not resolve contested evidence by:

- counting publications;
- preferring prestigious journals;
- preferring statistically significant results;
- ignoring inconvenient studies;
- selecting the newest paper automatically.

Explain why disagreement persists.

---

# 18. Contestation Record

Use:

```yaml
contested:
  proposition:
  supporting_stream:
  opposing_stream:
  key_methodological_differences:
  key_population_differences:
  theory_conflict:
  replication_conflict:
  current_status:
  unresolved_reason:
```

---

# 19. Unresolved Knowledge

`UNRESOLVED` means the current evidence does not yet support a sufficiently stable scientific answer.

Potential reasons:

- too few independent studies;
- contradictory findings;
- poor measurement;
- inadequate design;
- missing populations;
- insufficient follow-up;
- untested mechanism;
- lack of external validation.

Unresolved does not automatically mean research gap.

---

# 20. Unresolved Record

Use:

```yaml
unresolved:
  question:
  evidence_available:
  why_unresolved:
  methodological_limit:
  theoretical_limit:
  population_limit:
  replication_need:
  validation_need:
  next_evidence_needed:
```

---

# 21. Frontier

`FRONTIER` is the boundary where the current field is actively advancing.

Possible frontier forms:

- theoretical frontier;
- mechanistic frontier;
- methodological frontier;
- measurement frontier;
- computational frontier;
- translational frontier;
- population frontier;
- implementation frontier;
- interdisciplinary frontier.

Frontier is not synonymous with gap.

---

# 22. Frontier Record

Use:

```yaml
frontier:
  domain:
  current_boundary:
  recent_advances:
  closest_competitors:
  enabling_methods:
  unresolved_risks:
  evidence_maturity:
  opportunity:
```

---

# 23. Frontier Guard

Do not identify a frontier only because:

- a technology is new;
- software is new;
- a geographic context is underrepresented;
- a variable has not been combined before.

The frontier should represent a meaningful scientific boundary.

---

# 24. Evidence Maturity

Classify the maturity of each major knowledge domain.

Possible statuses:

- `NASCENT`
- `EMERGING`
- `DEVELOPING`
- `MATURE`
- `MATURE_BUT_CONTESTED`
- `FRAGMENTED`
- `INSUFFICIENT_TO_CLASSIFY`

---

# 25. Evidence Maturity Dimensions

Consider:

- independent studies;
- replication;
- design strength;
- methodological diversity;
- population diversity;
- theoretical integration;
- mechanism evidence;
- external validation;
- consistency;
- current relevance.

Do not use publication count alone.

---

# 26. Maturity Matrix

Use:

| Domain | Replication | Method Maturity | Population Breadth | Consistency | Maturity |
|---|---|---|---|---|---|

---

# 27. Evidence Convergence

Identify where multiple independent evidence streams converge.

Convergence may involve:

- different designs;
- different populations;
- different methods;
- different research groups;
- different settings.

Strong convergence should survive reasonable methodological variation.

---

# 28. Convergence Guard

Do not mistake repeated publications from one cohort or research group for independent convergence.

Route dependence questions to:

`reference-integrity-guard`

---

# 29. Evidence Divergence

Identify where evidence diverges.

Possible divergence types:

- population-dependent;
- measurement-dependent;
- method-dependent;
- context-dependent;
- temporal;
- theory-dependent;
- dose-dependent.

Divergence can define the scientific frontier.

---

# 30. Divergence Matrix

Use:

| Finding | Convergent Evidence | Divergent Evidence | Key Difference | Interpretation |
|---|---|---|---|---|

---

# 31. Contradictory Evidence Requirement

Every SoTA should actively look for credible evidence that challenges the dominant narrative.

Do not build SoTA only from supportive literature.

If contradictions appear missing, route to:

`citation-chaining`

and/or:

`scopus-literature-search`

---

# 32. Replication Status

Distinguish:

- direct replication;
- conceptual replication;
- external validation;
- failed replication;
- partial replication.

Do not label similar studies as replication without justification.

---

# 33. Replication Independence

Assess whether replications use:

- independent samples;
- independent datasets;
- independent research groups;
- different contexts.

Shared data should be labeled.

---

# 34. Theory Status

For theory-relevant fields, classify:

- dominant theory;
- competing theory;
- refined theory;
- partially supported theory;
- theory under challenge;
- theory not central.

Route formal theory construction to:

`theoretical-framework`

---

# 35. Theory Evolution

When useful:

```text
Original Theory
      ↓
Major Refinement
      ↓
Empirical Tests
      ↓
Competing Interpretation
      ↓
Current Theoretical Position
```

Do not select a theory merely because it is popular.

---

# 36. Theory Boundary Conditions

Identify conditions under which a theory appears to hold or weaken.

Examples:

- population;
- setting;
- developmental stage;
- dose;
- time;
- institutional context.

Boundary conditions can be more informative than a binary supported/not-supported judgment.

---

# 37. Mechanistic Status

Classify mechanisms as:

- `DIRECTLY_TESTED`
- `PARTIALLY_TESTED`
- `INDIRECTLY_SUPPORTED`
- `PLAUSIBLE`
- `SPECULATIVE`
- `NOT_EVALUATED`

Do not convert association into mechanism.

---

# 38. Mechanistic Frontier

A mechanistic frontier exists when:

- effects are repeatedly observed;
- causal pathway remains unclear;
- competing mechanisms remain;
- mediator evidence is incomplete;
- biological or theoretical pathway needs testing.

---

# 39. Methodological State

Characterize current dominant and emerging methods.

Possible categories:

- established standard;
- preferred current method;
- emerging method;
- contested method;
- method with known limitations;
- obsolete or superseded method.

Do not assume the newest method is superior.

---

# 40. Methodological Frontier

Potential methodological frontier signals:

- improved causal identification;
- better measurement;
- external validation;
- higher-resolution data;
- longitudinal design;
- multimethod integration;
- reproducibility improvement;
- computational advance with scientific gain.

---

# 41. Methodological Gap Guard

A method difference is not automatically a research gap.

Ask whether the method change enables a substantively new scientific answer.

Route candidate methodology opportunities to:

`gap-discovery`

---

# 42. Measurement State

Assess current measurement approaches:

- construct definition;
- validity;
- reliability;
- sensitivity;
- specificity;
- invariance;
- reproducibility;
- context adaptation.

---

# 43. Measurement Frontier

Potential frontier:

- new validated instrument;
- better biomarker;
- improved assay;
- digital measurement;
- objective measurement replacing weak proxy;
- cross-cultural validation.

Route instrument development to:

`instrument-design`

when needed.

---

# 44. Population State

Identify populations in which the knowledge is:

- well established;
- partially tested;
- underrepresented;
- contradictory;
- untested.

Do not call underrepresentation a strong gap without validating scientific importance.

---

# 45. Geographic State

Geography may influence:

- epidemiology;
- culture;
- health systems;
- education systems;
- regulation;
- environment.

Geographic novelty alone is usually weak.

---

# 46. Context State

Assess whether findings vary across:

- clinical;
- educational;
- workplace;
- laboratory;
- community;
- industrial;
- digital;
- policy contexts.

---

# 47. Temporal State

Current evidence may differ from historical evidence because of:

- technology change;
- policy change;
- treatment change;
- diagnostic change;
- population change;
- measurement change.

SoTA should explain material temporal shifts.

---

# 48. Translational State

For biomedical or applied research, distinguish:

```text
Mechanistic
      ↓
Preclinical
      ↓
Early Human
      ↓
Clinical
      ↓
Implementation
```

A frontier may occur at any transition.

---

# 49. Translational Guard

Do not infer:

- clinical efficacy from in-vitro evidence;
- population benefit from early human evidence;
- implementation effectiveness from efficacy alone.

---

# 50. Implementation State

For applied fields, identify whether evidence has progressed from:

- concept;
- efficacy;
- effectiveness;
- implementation;
- scale-up;
- sustainability.

---

# 51. Validation State

Identify whether findings or models have:

- internal validation;
- temporal validation;
- external validation;
- geographic validation;
- prospective validation.

Lack of validation may be scientifically important.

---

# 52. Prediction State

For prediction research, characterize:

- derivation;
- internal validation;
- external validation;
- calibration;
- discrimination;
- clinical utility.

Do not treat high derivation performance as established generalizability.

---

# 53. Diagnostic State

For diagnostic research, characterize:

- index test;
- reference standard;
- threshold;
- sensitivity;
- specificity;
- external validation;
- clinical utility.

---

# 54. Prognostic State

For prognosis, characterize:

- factor/model;
- time horizon;
- calibration;
- discrimination;
- external validation;
- clinical application.

---

# 55. Causal State

For causal questions, distinguish evidence from:

- randomized trials;
- quasi-experiments;
- longitudinal observational studies;
- cross-sectional studies;
- mechanistic studies.

Do not synthesize these as equivalent causal evidence.

---

# 56. Causal Frontier

Potential causal frontier exists where:

- association is robust;
- causal identification remains weak;
- confounding remains unresolved;
- temporality remains uncertain;
- mechanism is under-tested.

---

# 57. Pharmacogenetic State

Possible SoTA dimensions:

- gene/SNP;
- treatment;
- response;
- toxicity;
- population;
- allele frequency;
- genotype model;
- replication;
- validation.

---

# 58. Pharmacokinetic State

Possible SoTA dimensions:

- drug;
- population;
- dose;
- route;
- PK parameters;
- assay;
- model;
- covariates;
- external validation.

---

# 59. Pharmaceutical Formulation State

Possible dimensions:

- active ingredient;
- polymer/excipient;
- formulation;
- preparation method;
- physicochemical performance;
- stability;
- biological activity;
- translational stage.

---

# 60. Experimental State

Distinguish:

- in-vitro;
- ex-vivo;
- animal;
- human;
- computational.

Do not collapse evidence levels.

---

# 61. Qualitative State

For qualitative fields, SoTA may distinguish:

- dominant themes;
- context-specific themes;
- contested interpretations;
- missing perspectives;
- methodological evolution.

Do not force quantitative maturity criteria.

---

# 62. Mixed-Methods State

For mixed methods, evaluate:

- strand quality;
- integration;
- complementarity;
- contradiction;
- explanatory contribution.

Route formal integration to:

`mixed-method-analysis`

---

# 63. Systematic Review State

A systematic review may provide a high-level evidence snapshot.

Check:

- search cutoff;
- included designs;
- population;
- outcome;
- heterogeneity;
- later evidence.

Do not let an old review define the current SoTA without updating.

---

# 64. Meta-Analysis State

Meta-analysis may inform:

- pooled direction;
- magnitude;
- heterogeneity;
- subgroup patterns.

A pooled estimate does not by itself define the entire SoTA.

---

# 65. Review Update Guard

Forward-chain and update beyond the search date of influential reviews.

Route to:

`citation-chaining`

when needed.

---

# 66. Currentness Check

Before finalizing SoTA ask:

> Is there any realistic chance that important evidence has appeared after the current corpus cutoff?

If yes:

route to:

`scopus-literature-search`

and/or:

`citation-chaining`

---

# 67. Fast-Moving Field Rule

For `FAST_MOVING` fields:

- prioritize latest primary research;
- inspect preprint context when scientifically necessary;
- verify current review search dates;
- avoid relying on stale consensus.

Do not sacrifice verification for recency.

---

# 68. Slow-Moving Field Rule

For `SLOW_MOVING` fields:

- seminal sources may remain central;
- theoretical continuity may matter more;
- recency should not displace stable foundational evidence.

---

# 69. Evidence Cutoff

Record the latest literature date represented.

Use:

```yaml
sota_cutoff:
  latest_search_date:
  latest_included_publication:
  field_velocity:
  update_required:
```

---

# 70. Corpus Adequacy

Possible statuses:

- `ADEQUATE`
- `ADEQUATE_WITH_LIMITATIONS`
- `PRELIMINARY`
- `UPDATE_REQUIRED`
- `INSUFFICIENT`

Do not call a preliminary corpus comprehensive.

---

# 71. Evidence Breadth

Assess whether the corpus covers:

- primary studies;
- major reviews;
- contradictions;
- key methods;
- theory when relevant;
- independent replications;
- recent frontier.

---

# 72. Evidence Depth

Assess whether important claims have enough depth to understand:

- mechanism;
- method;
- population;
- boundary conditions;
- competing explanations.

Breadth without depth can produce shallow SoTA.

---

# 73. Discipline Boundary

State whether SoTA is:

- discipline-specific;
- multidisciplinary;
- interdisciplinary;
- transdisciplinary.

Do not mix adjacent disciplines without explaining equivalence.

---

# 74. Adjacent Discipline Guard

Adjacent evidence may challenge a claimed frontier.

Include it when scientifically equivalent enough.

Route difficult equivalence questions to:

`conceptual-framework`

or:

`methodology-architect`

---

# 75. Terminology Boundary

Map:

- current terms;
- synonyms;
- historical terms;
- neighboring constructs.

A false frontier can arise from terminology mismatch.

---

# 76. Terminology Drift

If a concept changed labels over time:

document the lineage.

Do not conclude that older evidence is absent merely because newer terminology was used.

---

# 77. Construct Boundary

Distinguish:

- identical construct;
- overlapping construct;
- nested construct;
- related construct;
- different construct.

Route formal construct organization to:

`conceptual-framework`

---

# 78. Scientific Boundary

For every major SoTA claim specify where it stops being supported.

Possible boundaries:

- population;
- geography;
- method;
- mechanism;
- outcome;
- context;
- time.

---

# 79. Boundary Condition Matrix

Use:

| Proposition | Supported Where | Weakens Where | Evidence |
|---|---|---|---|

---

# 80. Superseded Knowledge

Identify when older scientific positions have been materially replaced.

Possible reasons:

- invalidated theory;
- better measurement;
- stronger design;
- updated diagnostic criteria;
- corrected evidence.

Do not erase historical importance.

---

# 81. Supersession Guard

A newer paper does not automatically supersede an older paper.

Require substantive scientific replacement.

---

# 82. Scientific Turning Point

A turning point may be:

- landmark trial;
- theory shift;
- measurement breakthrough;
- method innovation;
- major contradiction;
- external validation.

Use sparingly.

---

# 83. Turning Point Record

Use:

```yaml
turning_point:
  source:
  prior_state:
  change_introduced:
  subsequent_support:
  current_relevance:
```

---

# 84. Dominant Approach

Identify current dominant approaches only when supported by the evidence corpus.

Dominance may reflect:

- repeated use;
- guideline adoption;
- methodological consensus;
- theoretical prevalence.

Dominance does not equal superiority.

---

# 85. Alternative Approach

Retain credible alternatives.

Alternative approaches may be:

- minority but stronger in some contexts;
- emerging;
- theoretically distinct;
- methodologically advantageous.

---

# 86. Best Available Evidence

"Best available" is question-specific.

Evaluate relevance plus evidence quality, not prestige.

---

# 87. Evidence Hierarchy Boundary

Do not apply one evidence hierarchy universally.

Examples:

- RCTs for intervention efficacy;
- qualitative evidence for lived experience;
- mechanistic experiments for biological pathways;
- longitudinal cohorts for prognosis.

---

# 88. Evidence Quality vs SoTA Status

A field can be:

- mature but methodologically weak;
- emerging but high quality;
- contested despite many studies;
- established in one population but unresolved in another.

Keep dimensions separate.

---

# 89. Confidence Without Formal Grading

If no formal certainty framework was applied, use qualitative language.

Examples:

- strong convergence;
- moderate convergence;
- limited evidence;
- substantial uncertainty.

Do not use GRADE-style certainty labels unless GRADE was actually applied.

---

# 90. Formal Certainty Boundary

If formal evidence certainty is needed:

route to the appropriate systematic-review or appraisal workflow.

Do not fabricate certainty grades.

---

# 91. Risk-of-Bias Boundary

SoTA may incorporate verified risk-of-bias assessments.

Do not invent them.

Risk of bias can influence interpretation but should remain traceable.

---

# 92. Publication Bias Awareness

The published field may overrepresent:

- positive findings;
- significant results;
- novel findings.

SoTA should acknowledge this possibility where material.

---

# 93. Citation Bias Awareness

Highly cited papers may dominate narratives disproportionately.

Do not let citation centrality define current truth.

---

# 94. Research Group Concentration

If much evidence comes from one research group:

label limited independence.

This may weaken the claim of establishment.

---

# 95. Dataset Concentration

If many papers use one dataset:

do not treat them as broad population replication.

---

# 96. Geographic Concentration

If evidence is concentrated geographically:

state the boundary.

Do not assume global generalizability.

---

# 97. Method Concentration

If one method dominates:

ask whether the apparent consensus is method-dependent.

---

# 98. Measurement Concentration

If one instrument dominates:

ask whether findings generalize across alternative measurements.

---

# 99. Contradiction Explanation

For contested evidence, evaluate:

- population;
- measurement;
- design;
- analysis;
- dose;
- time;
- context;
- sample independence.

Do not invent explanations.

---

# 100. Competing Explanation Matrix

Use:

| Explanation | Evidence For | Evidence Against | Current Status |
|---|---|---|---|

---

# 101. Scientific Consensus

Use "consensus" only when broad independent evidence supports it.

Possible status:

- `CONSENSUS_SUPPORTED`
- `GENERAL_CONVERGENCE_WITH_EXCEPTIONS`
- `NO_CLEAR_CONSENSUS`
- `CONTESTED`

---

# 102. Consensus Guard

Do not infer consensus from:

- one guideline;
- one meta-analysis;
- one research group;
- publication majority alone.

---

# 103. Scientific Uncertainty

Uncertainty may arise from:

- data scarcity;
- contradiction;
- imprecision;
- design limitations;
- population limits;
- theoretical ambiguity;
- measurement weakness.

Identify the source.

---

# 104. Uncertainty Record

Use:

```yaml
uncertainty:
  question:
  type:
  source:
  affected_claim:
  evidence_needed:
  priority:
```

---

# 105. Uncertainty Prioritization

Possible priority:

- `HIGH`
- `MODERATE`
- `LOW`

Priority depends on scientific importance, not publication attractiveness.

---

# 106. Unresolved Does Not Equal Gap

Preserve:

```text
UNRESOLVED KNOWLEDGE
      ≠
VALIDATED RESEARCH GAP
```

SoTA may generate candidate gaps.

Gap validity belongs to:

`gap-validator`

---

# 107. Candidate Gap Signal

Possible gap signals include:

- unresolved contradiction;
- missing replication;
- missing validation;
- mechanism uncertainty;
- population boundary;
- method limitation;
- theory inconsistency.

Route to:

`gap-discovery`

---

# 108. Gap Signal Record

Use:

```yaml
gap_signal:
  unresolved_area:
  evidence_basis:
  why_scientifically_important:
  possible_gap_type:
  known_threats:
  validation_required:
```

---

# 109. Gap Discovery Handoff

Preferred route:

```text
sota-builder
      ↓
gap-discovery
      ↓
gap-validator
```

Do not skip adversarial gap validation.

---

# 110. Gap Validation Input

Provide:

```yaml
gap_validation_input:
  established_knowledge:
  emerging_knowledge:
  contested_knowledge:
  unresolved_knowledge:
  frontier:
  closest_competitors:
  recent_evidence:
  terminology_variants:
  methodological_equivalents:
```

---

# 111. Novelty Boundary

SoTA defines what the field already contains.

It does not itself define what is novel.

Route novelty construction to:

`novelty-builder`

---

# 112. Novelty Threats

SoTA should identify:

- closest prior studies;
- existing method combinations;
- existing populations;
- existing mechanisms;
- prior priority claims.

This prevents inflated novelty.

---

# 113. Novelty Auditor Handoff

Preferred route:

```text
validated gap
      ↓
novelty-builder
      ↓
novelty-auditor
```

SoTA supplies the competitor evidence.

---

# 114. Research Question Handoff

A mature SoTA can inform:

`research-question-builder`

by clarifying:

- what is known;
- what is uncertain;
- what is answerable;
- what would add scientific value.

Do not formulate RQ before the gap and novelty are sufficiently clear when those are required.

---

# 115. Hypothesis Handoff

When confirmatory hypotheses are appropriate:

route to:

`hypothesis-builder`

after theory requirements are resolved.

Do not derive hypotheses from publication frequency alone.

---

# 116. Theoretical Framework Handoff

When SoTA reveals that explanation depends on theory:

route to:

`theoretical-framework`

before hypothesis construction when theory is required.

---

# 117. Conceptual Framework Handoff

When construct relationships need formal mapping:

route to:

`conceptual-framework`

---

# 118. Methodology Handoff

SoTA can reveal:

- common designs;
- persistent limitations;
- validation needs;
- underused stronger designs.

Route design decisions to:

`methodology-architect`

---

# 119. Sampling Handoff

Population evidence may inform:

`sampling-strategy`

Do not infer sampling method solely from prior practice.

---

# 120. Instrument Handoff

Measurement-frontier findings may route to:

`instrument-design`

---

# 121. Analysis Handoff

Analytical patterns may route to:

`analysis-planner`

or:

`statistical-method-selector`

Do not select analysis merely because it is fashionable.

---

# 122. Result Interpretation Handoff

When a new study is completed:

`result-interpreter`

may compare results against the SoTA.

Do not retroactively redefine SoTA to fit new results.

---

# 123. Scientific Discussion Handoff

SoTA provides the intellectual baseline for:

`scientific-discussion`

The discussion should explain how the new result:

- confirms;
- refines;
- contradicts;
- extends;
- challenges

the current state.

---

# 124. Implication Handoff

Route implication construction to:

`implication-builder`

SoTA should not overstate practical implications beyond evidence.

---

# 125. Manuscript Architecture Handoff

SoTA may inform:

`manuscript-architect`

for introduction and discussion positioning.

---

# 126. Manuscript Writer Handoff

`manuscript-writer` may translate SoTA into prose.

It must preserve category distinctions and uncertainty.

---

# 127. Manuscript Audit Handoff

`manuscript-auditor` may check whether claims of:

- established knowledge;
- gap;
- novelty;
- consensus;
- frontier

match the evidence.

---

# 128. Journal Matcher Boundary

`journal-matcher` may use scientific positioning.

Journal selection must not redefine the SoTA.

---

# 129. Reviewer Simulator Handoff

`reviewer-simulator` may challenge:

- stale SoTA;
- missing contradictions;
- unsupported consensus;
- weak gap;
- inflated novelty;
- selective literature.

---

# 130. Reviewer Response Handoff

If reviewers challenge the SoTA:

route to:

`reviewer-response`

Update evidence scientifically before drafting rebuttal language.

---

# 131. Previous Research Positioning

When the user supplies previous research:

compare it against the current SoTA.

Possible statuses:

- still current;
- partially superseded;
- independently replicated;
- contradicted;
- extended;
- frontier-adjacent;
- now routine.

---

# 132. Previous Research Record

Use:

```yaml
previous_research_position:
  previous_output:
  original_contribution:
  current_status:
  subsequent_replications:
  subsequent_extensions:
  contradictions:
  superseding_evidence:
  continuation_opportunity:
```

---

# 133. Research Resume Handoff

For continuing earlier work:

route to:

`research-resume`

with updated SoTA context.

---

# 134. Continuation Opportunity Handoff

When SoTA identifies scientifically meaningful next directions:

route to:

`continuation-opportunity-finder`

Do not recommend continuation merely because a variable was not tested before.

---

# 135. Research Trajectory Handoff

For multi-study progression:

route to:

`research-trajectory-mapper`

SoTA can show where prior work sits in the broader field.

---

# 136. Idea Discovery Handoff

If the user has no specific research question:

SoTA may support:

`idea-discovery`

after sufficient landscape discovery.

---

# 137. Research Landscape Relationship

`research-landscape` maps the broad domain.

`sota-builder` identifies the current scientific position and frontier.

Conceptually:

```text
research-landscape
      ↓
evidence synthesis
      ↓
sota-builder
```

---

# 138. Trend Detection Relationship

`trend-detection` identifies temporal activity patterns.

SoTA interprets whether those trends represent meaningful scientific progress.

---

# 139. Emerging Topic Relationship

`emerging-topic-discovery` identifies emerging areas.

SoTA determines how those areas relate to established, contested, unresolved, and frontier knowledge.

---

# 140. Scopus Literature Search Relationship

`scopus-literature-search` discovers scholarly evidence.

SoTA should not claim direct Scopus coverage unless the search actually occurred.

---

# 141. Source Verification Relationship

`source-verification` establishes source identity and metadata.

SoTA depends on verified evidence.

---

# 142. Reference Integrity Relationship

`reference-integrity-guard` ensures the sources are represented correctly.

A real paper can still be cited incorrectly.

---

# 143. Citation Chaining Relationship

`citation-chaining` expands historical and forward scientific lineage.

SoTA uses chained evidence to understand development and frontier.

---

# 144. Literature Screening Relationship

`literature-screening` determines purpose-specific eligibility.

SoTA should use the screened corpus rather than all discovered records indiscriminately.

---

# 145. Evidence Synthesis Relationship

Preferred immediate upstream:

```text
literature-screening
      ↓
evidence-synthesis
      ↓
sota-builder
```

Evidence synthesis identifies patterns.

SoTA classifies their current intellectual status.

---

# 146. SoTA Classification Record

Use:

```yaml
sota_classification:
  proposition:
  category:
  evidence_basis:
  independent_support:
  contradiction:
  boundary_conditions:
  currentness:
  confidence:
  notes:
```

---

# 147. Category Rules

Use:

- `ESTABLISHED`
- `EMERGING`
- `CONTESTED`
- `UNRESOLVED`
- `FRONTIER`

A proposition may occupy more than one category only when dimensions are clearly separated.

Example:

```text
Established association
+
Unresolved mechanism
```

---

# 148. Multidimensional Status

Possible:

```yaml
multidimensional_status:
  association:
  causality:
  mechanism:
  prediction:
  validation:
  implementation:
```

This prevents oversimplified labels.

---

# 149. Example Multidimensional Classification

```text
Association: ESTABLISHED
Mechanism: EMERGING
Causality: CONTESTED
External Validation: UNRESOLVED
Implementation: FRONTIER
```

This is often more informative than one overall label.

---

# 150. Scientific Frontier Map

Use:

```text
                 CURRENT KNOWLEDGE
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
     ESTABLISHED     CONTESTED     UNRESOLVED
          │             │             │
          └─────────────┼─────────────┘
                        ↓
                     FRONTIER
                        ↓
               Candidate Research Gaps
```

Do not equate every frontier node with a gap.

---

# 151. SoTA Evidence Map

Recommended:

| Scientific Proposition | Status | Evidence Basis | Contradiction | Boundary | Frontier Relevance |
|---|---|---|---|---|---|

---

# 152. Evolution Matrix

Recommended:

| Period | Dominant Knowledge | Key Development | Current Relevance |
|---|---|---|---|

---

# 153. Frontier Matrix

Recommended:

| Frontier | Why It Matters | Current Evidence | Main Uncertainty | Next Evidence Needed |
|---|---|---|---|---|

---

# 154. Contestation Matrix

Recommended:

| Question | Position A | Position B | Why They Differ | Current Assessment |
|---|---|---|---|---|

---

# 155. Unresolved Matrix

Recommended:

| Unresolved Question | Evidence Available | Why Unresolved | Candidate Next Step |
|---|---|---|---|

---

# 156. Established Matrix

Recommended:

| Proposition | Independent Support | Boundaries | Confidence |
|---|---|---|---|

---

# 157. Method Frontier Matrix

Recommended:

| Current Method | Limitation | Emerging Alternative | Scientific Gain |
|---|---|---|---|

---

# 158. Theory Frontier Matrix

Recommended:

| Theory | Support | Challenge | Boundary | Current Position |
|---|---|---|---|---|

---

# 159. Population Frontier Matrix

Recommended:

| Population | Evidence State | Missing Evidence | Scientific Relevance |
|---|---|---|---|

---

# 160. Translational Frontier Matrix

Recommended:

| Stage | Current Evidence | Barrier | Next Translational Step |
|---|---|---|---|

---

# 161. Full SoTA Output

For a comprehensive task provide:

## A. SoTA Question
[...]

## B. Evidence Boundary
[...]

## C. Field Velocity and Cutoff
[...]

## D. Historical Foundation
[...]

## E. Scientific Evolution
[...]

## F. Established Knowledge
[...]

## G. Emerging Evidence
[...]

## H. Contested Evidence
[...]

## I. Unresolved Knowledge
[...]

## J. Scientific Frontier
[...]

## K. Theory State
[...]

## L. Methodological State
[...]

## M. Measurement State
[...]

## N. Population and Context Boundaries
[...]

## O. Translational / Validation State
[...]

## P. Evidence Maturity
[...]

## Q. Closest Scientific Competitors
[...]

## R. Candidate Gap Signals
[...]

## S. Limitations of the SoTA
[...]

## T. Recommended Next Skill
[...]

---

# 162. Compact SoTA Output

For a smaller request use:

```text
Question:
Established:
Emerging:
Contested:
Unresolved:
Frontier:
Main boundary:
Next step:
```

---

# 163. SoTA Narrative Structure

A strong narrative can follow:

```text
What is established
      ↓
What changed recently
      ↓
Where findings diverge
      ↓
What remains unresolved
      ↓
Where the frontier now sits
```

---

# 164. Avoid Chronological Article Listing

Avoid:

> Study A found...
> Study B found...
> Study C found...

unless chronology itself explains scientific evolution.

Prefer integrated propositions.

---

# 165. Claim Traceability

Every major SoTA claim should trace to:

- included evidence;
- synthesis output;
- contradiction record;
- boundary conditions.

Do not create unsupported intellectual categories.

---

# 166. Current Best Evidence Claim

When using the phrase "current best evidence":

state the scientific basis.

Do not use it as rhetorical emphasis.

---

# 167. Established Claim Wording

Examples:

> Multiple independent studies across several populations consistently support...

Avoid:

> It is universally proven...

unless truly justified.

---

# 168. Emerging Claim Wording

Example:

> Recent studies suggest an emerging pattern, although independent validation remains limited.

---

# 169. Contested Claim Wording

Example:

> Evidence remains contested, with divergent findings that appear partly related to measurement and population differences.

---

# 170. Unresolved Claim Wording

Example:

> The available evidence is insufficient to determine whether the observed association reflects a causal mechanism.

---

# 171. Frontier Claim Wording

Example:

> The current frontier has shifted from establishing the association toward clarifying mechanism and external validation.

---

# 172. No Universal Frontier

A field may have several simultaneous frontiers.

Examples:

- mechanism;
- validation;
- implementation;
- method.

Do not force one frontier.

---

# 173. Frontier Prioritization

Possible priority dimensions:

- scientific importance;
- evidence deficit;
- feasibility;
- translational relevance;
- theoretical leverage;
- replication need.

Do not prioritize by publication attractiveness alone.

---

# 174. Frontier Priority Record

Use:

```yaml
frontier_priority:
  frontier:
  scientific_importance:
  evidence_need:
  feasibility:
  impact:
  dependency:
  priority:
```

---

# 175. SoTA and Feasibility

A scientifically important frontier may be infeasible for a specific researcher.

SoTA should describe the science.

Feasibility decisions belong downstream.

---

# 176. SoTA and Research Resources

Do not redefine SoTA because:

- sample access is limited;
- software is unavailable;
- funding is limited.

Those constraints affect project selection, not the state of knowledge.

---

# 177. SoTA and Journal Strategy

Do not reshape SoTA to fit journal scope.

Journal fit comes later.

---

# 178. SoTA and APC

Do not let APC preference affect evidence selection or SoTA conclusions.

---

# 179. SoTA and Prestige

Do not privilege evidence because of:

- journal prestige;
- author prestige;
- institution prestige.

Scientific relevance and evidence strength govern.

---

# 180. Citation Padding Guard

Do not add citations merely to:

- appear comprehensive;
- cite the target journal;
- satisfy assumed reviewer preferences;
- increase citation count.

---

# 181. Historical Citation Guard

Do not use secondary reviews to replace original seminal sources when original attribution matters.

Route to:

`citation-chaining`

and:

`source-verification`

---

# 182. Primary Evidence Guard

For central scientific claims, prioritize primary evidence when needed.

Reviews can contextualize but should not always substitute for primary studies.

---

# 183. Review Dependence Guard

Do not let one review determine:

- established status;
- frontier;
- gap;
- novelty.

Update beyond its search date.

---

# 184. Contradiction Suppression Guard

Do not remove credible contradictory evidence because it weakens the intended research rationale.

Contradiction may strengthen the rationale by identifying a more defensible unresolved problem.

---

# 185. Null Evidence Guard

Null findings belong in the SoTA when eligible.

Do not classify a field as established from significant results alone.

---

# 186. Negative Evidence Guard

Negative or failed evidence may:

- falsify claims;
- reveal boundary conditions;
- challenge mechanism;
- redefine frontier.

Treat it scientifically.

---

# 187. Replication Failure Guard

Failed replication should not be dismissed automatically.

Investigate differences before interpretation.

---

# 188. Mechanistic Overclaim Guard

Do not write mechanism as established when evidence only supports association.

---

# 189. Causal Overclaim Guard

Do not classify causality as established from predominantly observational cross-sectional evidence.

---

# 190. Prediction Overclaim Guard

Do not interpret predictive performance as causal explanation.

---

# 191. Generalization Guard

Do not state global generality from geographically or demographically narrow evidence.

---

# 192. Method Dominance Guard

A dominant method can create apparent consensus.

Ask whether alternative methods produce the same conclusion.

---

# 193. Construct Equivalence Guard

Do not merge related constructs merely to increase the evidence base.

---

# 194. Context Equivalence Guard

Do not assume evidence transfers across contexts without rationale.

---

# 195. Evidence Absence Guard

Absence in the screened corpus does not prove absence in the literature.

Before strong absence claims:

route to:

`scopus-literature-search`

and:

`citation-chaining`

---

# 196. Priority Claim Guard

Claims such as:

- "first";
- "never studied";
- "no previous study";

require adversarial validation.

Route to:

`novelty-auditor`

---

# 197. SoTA Update Trigger

Update SoTA when:

- a major new review appears;
- new external validation appears;
- a key replication fails;
- a new method changes the field;
- policy or technology materially changes context;
- a reviewer identifies important omitted evidence.

---

# 198. SoTA Versioning

Use:

```yaml
sota_version:
  version:
  evidence_cutoff:
  updated_from:
  major_changes:
  classification_changes:
  new_frontiers:
  retired_frontiers:
```

---

# 199. Classification Change

A proposition may move:

```text
EMERGING → ESTABLISHED
ESTABLISHED → CONTESTED
UNRESOLVED → EMERGING
FRONTIER → ESTABLISHED
```

Record why.

---

# 200. Retired Frontier

A former frontier may become:

- established;
- resolved;
- superseded;
- scientifically unproductive.

Do not preserve old frontier language indefinitely.

---

# 201. SoTA Reassessment After New Evidence

When new evidence is added:

1. verify;
2. screen;
3. synthesize;
4. reassess categories;
5. update frontier;
6. reassess candidate gaps.

---

# 202. SoTA Consistency Check

Ensure:

- established claims do not contradict unresolved claims unless dimensions differ;
- frontier follows from current evidence;
- gap signals arise from unresolved/frontier areas;
- terminology is consistent;
- evidence cutoff is clear.

---

# 203. Category Conflict

If the same proposition appears in conflicting categories:

resolve by specifying dimensions.

Example:

```text
Association: ESTABLISHED
Causality: UNRESOLVED
Mechanism: EMERGING
```

---

# 204. Intellectual Positioning

SoTA should answer:

> Where exactly does the proposed or previous research sit relative to the current field?

Possible positions:

- confirms established knowledge;
- extends established knowledge;
- tests an unresolved boundary;
- challenges contested knowledge;
- addresses a validation frontier;
- investigates an emerging mechanism.

---

# 205. Research Position Record

Use:

```yaml
research_position:
  study:
  relative_to_established:
  relative_to_emerging:
  relative_to_contested:
  relative_to_unresolved:
  relative_to_frontier:
  contribution_type:
  major_risk:
```

---

# 206. Competitive Positioning

Identify the nearest existing studies.

Compare:

- question;
- population;
- theory;
- mechanism;
- method;
- outcome;
- contribution.

Do not exaggerate differences.

---

# 207. Closest Competitor Matrix

Use:

| Competitor | Scientific Overlap | Key Difference | Frontier Relevance |
|---|---|---|---|

---

# 208. Research Continuation Position

For previous research:

ask:

- What was original then?
- What is established now?
- What has been replicated?
- What has been contradicted?
- What remains open?
- What is now the best continuation?

---

# 209. Continuation Guard

Do not recommend continuation solely because:

- another variable can be added;
- another location can be studied;
- new software can be used.

Continuation should advance the scientific frontier.

---

# 210. SoTA to Gap Logic

Preferred logic:

```text
ESTABLISHED
      +
EMERGING
      +
CONTESTED
      +
UNRESOLVED
      +
FRONTIER
      ↓
Candidate Gap
```

Then:

```text
Candidate Gap
      ↓
gap-validator
```

---

# 211. SoTA to Novelty Logic

Preferred:

```text
SoTA
      ↓
Validated Gap
      ↓
Novelty Builder
      ↓
Novelty Auditor
```

Do not jump directly from literature scarcity to novelty.

---

# 212. SoTA to Research Question Logic

Preferred:

```text
SoTA
      ↓
Validated Gap
      ↓
Audited Novelty
      ↓
research-question-builder
```

unless the workflow is exploratory and a different route is scientifically justified.

---

# 213. SoTA to Method Logic

Method selection should follow the scientific question.

Do not route directly from "popular current method" to methodology without a clear research objective.

---

# 214. User-Provided SoTA

If the user provides a SoTA draft:

audit:

- currentness;
- category accuracy;
- missing contradictions;
- gap inflation;
- novelty inflation;
- citation integrity.

Do not assume the user's classifications are correct.

---

# 215. Manuscript SoTA Audit

In an introduction or discussion, check whether:

- "known" claims are truly established;
- "unknown" claims are truly unresolved;
- "first" claims survive novelty audit;
- frontier language is current.

---

# 216. SoTA Evidence Passport

Use:

```yaml
sota:
  question:
  evidence_boundary:
  corpus_version:
  field_velocity:
  evidence_cutoff:
  established:
  emerging:
  contested:
  unresolved:
  frontier:
  theory_state:
  method_state:
  measurement_state:
  population_boundaries:
  context_boundaries:
  translational_state:
  evidence_maturity:
  closest_competitors:
  candidate_gap_signals:
  update_required:
  limitations:
  next_stage:
```

---

# 217. SoTA Status

Possible statuses:

- `NOT_STARTED`
- `EVIDENCE_NOT_READY`
- `PRELIMINARY_SOTA`
- `UPDATE_REQUIRED`
- `SOTA_IN_PROGRESS`
- `SOTA_READY`
- `READY_FOR_GAP_DISCOVERY`
- `READY_FOR_GAP_VALIDATION`
- `READY_FOR_NOVELTY_DEVELOPMENT`
- `READY_FOR_RESEARCH_POSITIONING`

---

# 218. Preliminary SoTA

Use `PRELIMINARY_SOTA` when:

- corpus is incomplete;
- latest search is unavailable;
- important contradictions remain unverified;
- only selected sources were provided.

Do not present it as final.

---

# 219. SoTA Readiness Gate

Before `SOTA_READY`, verify:

- evidence is sufficiently current;
- critical sources are verified;
- major contradictions are represented;
- established/emerging/contested/unresolved/frontier categories are defensible;
- boundaries are explicit;
- no major study-family distortion remains;
- no strong absence claim is unsupported.

---

# 220. Gap Discovery Readiness Gate

Before `READY_FOR_GAP_DISCOVERY`, ensure the SoTA identifies scientifically meaningful unresolved or frontier areas.

---

# 221. Gap Validation Readiness Gate

Before `READY_FOR_GAP_VALIDATION`, ensure:

- close competitors are known;
- recent literature is represented;
- terminology variants are mapped;
- method equivalents are recognized;
- contradiction is visible.

---

# 222. Novelty Readiness Gate

Before `READY_FOR_NOVELTY_DEVELOPMENT`, ensure:

- current frontier is clear;
- closest competitors are known;
- what is already established is explicit;
- candidate gap has been validated or appropriately reframed.

---

# 223. Research Positioning Readiness Gate

Before positioning a study:

ensure the study's claimed contribution is compared against:

- current established knowledge;
- current frontier;
- closest competitors;
- unresolved evidence.

---

# 224. SoTA Limitation Statement

Always disclose material limitations.

Examples:

- database limitation;
- date cutoff;
- language limitation;
- incomplete full text;
- preliminary corpus;
- discipline boundary;
- no formal certainty grading.

---

# 225. No Exhaustiveness Claim

Avoid:

> This SoTA includes all relevant literature.

Prefer:

> This SoTA represents the verified and screened evidence available within the defined search scope and cutoff.

---

# 226. Researcher-Friendly Summary

A concise SoTA summary should answer:

1. What do we know?
2. What is changing?
3. Where do studies disagree?
4. What remains unknown?
5. Where is the frontier?
6. What should be validated next?

---

# 227. Example Researcher-Facing Output

> The association is now well supported across several independent cohorts, so repeating the same association study would add little. The current frontier has shifted toward mechanism and external validation, while evidence in older adults remains limited. The strongest candidate gap is therefore not the association itself but whether the proposed mechanism replicates in that population.

---

# 228. Avoid These Behaviors

Do not:

- produce a chronological paper list instead of SoTA;
- classify recent as automatically emerging;
- classify highly cited as automatically established;
- hide contradictory evidence;
- treat one review as complete evidence;
- use journal prestige as scientific weight;
- use Scopus indexing as evidence quality;
- use APC status to influence evidence;
- add target-journal citations strategically;
- call literature scarcity a validated gap;
- call new geography strong novelty by itself;
- call new software a frontier without scientific gain;
- call additional variables a frontier without scientific value;
- claim consensus without independent convergence;
- claim first-study priority without novelty audit;
- claim no studies exist without broad validation;
- infer mechanism from association;
- infer causality from prediction;
- infer clinical efficacy from preclinical evidence;
- force theory when theory is not scientifically needed;
- select methodology before the research question is sufficiently clear.

---

# Stop Conditions

Do not mark SoTA complete when:

- the evidence corpus is not sufficiently verified or screened;
- the current evidence cutoff is unknown in a fast-moving field;
- important recent literature remains unsearched;
- major contradictory evidence has not been examined;
- key study-family dependence distorts apparent replication;
- category labels cannot be traced to evidence;
- established claims rely on one research group only without qualification;
- frontier claims depend only on novelty of software, geography, or variable combination;
- strong absence, consensus, or priority claims remain unvalidated;
- a formal certainty label is used without a formal certainty framework;
- the proposed gap is being presented as validated without `gap-validator`;
- novelty is being presented as established without `novelty-auditor`.

Use:

- `EVIDENCE_NOT_READY`
- `SOURCE_VERIFICATION_REQUIRED`
- `REFERENCE_INTEGRITY_REQUIRED`
- `SCREENING_UPDATE_REQUIRED`
- `SEARCH_UPDATE_REQUIRED`
- `CONTRADICTION_REVIEW_REQUIRED`
- `PRELIMINARY_SOTA`
- `GAP_VALIDATION_REQUIRED`
- `NOVELTY_AUDIT_REQUIRED`
- `NOT_READY_FOR_DOWNSTREAM_USE`

as appropriate.

---

# Success Criterion

`sota-builder` succeeds when a sufficiently verified, integrity-cleared, screened, synthesized, and current scholarly evidence base is transformed into a defensible intellectual map of the field that clearly distinguishes `ESTABLISHED`, `EMERGING`, `CONTESTED`, `UNRESOLVED`, and `FRONTIER` knowledge; when scientific evolution is explained without degenerating into a chronological article list; when evidence maturity, independent replication, contradiction, theory state, mechanism state, methodological state, measurement state, population and context boundaries, temporal development, validation, translation, and generalizability are represented at the appropriate level of confidence; when currentness is calibrated to field velocity rather than an arbitrary publication-year rule; when study-family dependence, publication bias, citation bias, research-group concentration, dataset dependence, prestige, quartile, Scopus status, target-journal strategy, and APC preferences do not distort scientific interpretation; when established claims do not exceed the available evidence, emerging evidence is not mistaken for consensus, contested findings remain visible, unresolved knowledge is not automatically called a gap, and frontier claims reflect substantive scientific boundaries rather than superficial novelty; when previous research can be positioned against the current field and closest competitors without inflated contribution claims; when candidate unresolved areas are routed to `gap-discovery` and `gap-validator`, novelty development to `novelty-builder` and `novelty-auditor`, theory and conceptual needs to their appropriate framework skills, methodology and analysis decisions downstream of a clear scientific question, and manuscript or reviewer workflows receive a current evidence-grounded scientific position; and when the final SoTA is traceable, balanced, current, bounded, transparent about limitations, and sufficiently robust to support defensible gap validation, novelty development, research-question construction, continuation-study selection, methodology design, and manuscript positioning.
