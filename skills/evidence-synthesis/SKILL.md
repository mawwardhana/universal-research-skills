---
name: evidence-synthesis
description: Synthesize verified and screened scholarly evidence across studies to determine convergent findings, contradictory evidence, effect patterns, mechanisms, contextual differences, methodological explanations, evidence maturity, uncertainty, and defensible scientific conclusions. Use after literature screening and before State-of-the-Art development, research-gap validation, novelty assessment, theoretical positioning, methodology justification, scientific discussion, systematic review conclusions, or manuscript evidence integration.
---

# Evidence Synthesis

## Purpose

`evidence-synthesis` integrates findings across multiple verified and screened studies.

Its central question is:

> When the relevant evidence is considered together, what can we scientifically conclude, what remains uncertain, and why do studies agree or disagree?

The purpose is not to produce a sequence of article summaries.

The purpose is to identify:

- convergence;
- contradiction;
- consistency;
- heterogeneity;
- methodological differences;
- population differences;
- context effects;
- mechanism signals;
- temporal development;
- evidence maturity;
- uncertainty;
- defensible scientific conclusions.

Evidence synthesis forms the bridge between:

literature collection

and:

scientific interpretation.

---

# Core Principle

Use:

> Synthesize across studies, not paper by paper.

A strong synthesis should move from:

"Study A found X. Study B found Y. Study C found Z."

toward:

"Across the available evidence, X is generally supported under conditions A and B, while findings become inconsistent in population C, possibly because of differences in measurement and study design."

Do not force consensus where evidence is genuinely inconsistent.

---

# Activation Conditions

Use this skill after literature has been:

1. discovered;
2. sufficiently verified;
3. screened for relevance.

Typical upstream route:

`scopus-literature-search`
→ `source-verification`
→ `citation-chaining`
→ `literature-screening`
→ `evidence-synthesis`

Use before:

- `sota-builder`;
- `gap-discovery`;
- `gap-validator`;
- `novelty-builder`;
- theoretical framework development;
- methodological justification;
- scientific discussion;
- systematic-review conclusions;
- manuscript evidence integration.

---

# Input Requirements

Prefer a corpus containing, where available:

- verified bibliographic records;
- relevance classification;
- study design;
- population;
- context;
- methods;
- measurements;
- primary findings;
- effect estimates;
- uncertainty;
- limitations;
- evidence role;
- verification status.

Do not fabricate missing findings.

---

# 1. Define the Synthesis Question

Before synthesis, identify what is being synthesized.

Possible questions include:

- Does X influence Y?
- What mechanisms explain X?
- Which methods are used?
- How consistent is the evidence?
- What factors explain contradictory findings?
- What is currently established?
- What remains unresolved?
- How mature is this research field?

Do not synthesize without a clear scientific purpose.

---

# 2. Select the Synthesis Mode

Possible modes:

- `NARRATIVE_SYNTHESIS`
- `THEMATIC_SYNTHESIS`
- `CONFIGURATIVE_SYNTHESIS`
- `MECHANISM_SYNTHESIS`
- `METHOD_SYNTHESIS`
- `THEORY_SYNTHESIS`
- `CONTRADICTION_SYNTHESIS`
- `SOTA_SYNTHESIS`
- `GAP_VALIDATION_SYNTHESIS`
- `SYSTEMATIC_REVIEW_SYNTHESIS`
- `META_ANALYTIC_HANDOFF`

Choose according to the question and evidence.

Do not use meta-analytic language unless quantitative pooling has actually been performed.

---

# 3. Study-Level Evidence Extraction

For each included study, extract only information relevant to the synthesis question.

Possible fields:

```yaml
study:
  reference_id:
  citation:
  design:
  population:
  geography:
  context:
  sample:
  exposure_or_intervention:
  comparator:
  outcome:
  measurement:
  follow_up:
  analysis:
  main_finding:
  effect_direction:
  effect_size:
  uncertainty:
  statistical_significance:
  mechanism_signal:
  contextual_factors:
  methodological_features:
  limitations:
  evidence_role:
  contradiction_status:
  verification_status:
  integrity_status:
  screening_status:
  notes:
```

Do not fabricate missing information.

Unknown fields remain unknown.

---

# 4. Evidence Eligibility Gate

Before synthesis, confirm that materially important evidence has passed:

```text
source-verification
      ↓
reference-integrity-guard
      ↓
literature-screening
      ↓
evidence-synthesis
```

Do not synthesize records that remain:

- identity-unresolved;
- materially misrepresented;
- retracted for the relevant scientific claim;
- excluded from the purpose-specific corpus.

---

# 5. Purpose-Specific Corpus

Synthesis is always corpus-dependent.

A study may belong to:

- `SOTA_CORPUS`
- `GAP_CORPUS`
- `NOVELTY_CORPUS`
- `METHOD_CORPUS`
- `THEORY_CORPUS`
- `SYSTEMATIC_REVIEW_CORPUS`
- `META_ANALYSIS_CORPUS`
- `MANUSCRIPT_CORPUS`
- `CONTINUATION_CORPUS`

Do not assume one universal corpus answers every scientific question.

---

# 6. Corpus Version

When relevant, record:

```yaml
corpus:
  purpose:
  version:
  search_cutoff:
  screening_cutoff:
  included_records:
  included_studies:
  study_families:
  unresolved_records:
  notes:
```

Do not fabricate counts.

---

# 7. Study vs Publication

Preserve:

```text
publication
≠
independent study
```

Multiple papers may belong to one study family.

Do not interpret repeated reports from one cohort as independent replication.

Route ambiguity to:

`reference-integrity-guard`

---

# 8. Study-Family Synthesis

When several publications describe one study, synthesize them at the appropriate scientific unit.

Possible roles:

- protocol;
- baseline report;
- primary outcome;
- secondary outcome;
- subgroup analysis;
- follow-up;
- mechanistic analysis;
- methods paper.

Avoid double-counting the same participants or outcomes.

---

# 9. Evidence Unit

Choose the synthesis unit according to purpose.

Possible units:

- study;
- study family;
- effect estimate;
- theme;
- mechanism;
- construct relationship;
- method;
- theory;
- population;
- context;
- outcome;
- time period.

State the unit explicitly when ambiguity matters.

---

# 10. Synthesis Dimension

Possible synthesis dimensions include:

- direction of findings;
- magnitude;
- consistency;
- precision;
- mechanism;
- population;
- geography;
- setting;
- methodology;
- measurement;
- time;
- theory;
- evidence maturity.

Do not reduce every synthesis to statistical significance.

---

# 11. Direction-of-Effect Coding

Possible categories:

- `POSITIVE`
- `NEGATIVE`
- `NULL_OR_NO_CLEAR_ASSOCIATION`
- `MIXED_WITHIN_STUDY`
- `NONLINEAR`
- `CONTEXT_DEPENDENT`
- `NOT_APPLICABLE`
- `UNCLEAR`

Direction should reflect the scientific outcome definition.

---

# 12. Direction Coding Guard

Do not label:

```text
p > 0.05
```

automatically as:

```text
NULL_EFFECT
```

A non-significant estimate may be:

- imprecise;
- underpowered;
- compatible with meaningful effects;
- truly small;
- uncertain.

Preserve uncertainty.

---

# 13. Statistical Significance Guard

Statistical significance is not synonymous with:

- clinical importance;
- practical importance;
- causal truth;
- evidence strength;
- replication.

Use significance only as one descriptive feature when scientifically relevant.

---

# 14. Magnitude Synthesis

When effect sizes are comparable, examine:

- direction;
- magnitude;
- uncertainty;
- clinical or practical relevance.

Do not compare incompatible effect measures as though they were identical.

---

# 15. Effect-Measure Harmonization

Possible effect measures include:

- mean difference;
- standardized mean difference;
- odds ratio;
- risk ratio;
- hazard ratio;
- correlation;
- regression coefficient;
- prevalence ratio;
- diagnostic accuracy;
- model-performance metric.

Do not convert measures without a valid method.

---

# 16. Quantitative Pooling Boundary

`evidence-synthesis` may organize quantitative findings.

It must not claim pooled effects unless quantitative pooling was actually conducted.

Route formal quantitative pooling to:

`meta-analysis`

---

# 17. Meta-Analytic Handoff

When studies are sufficiently compatible and effect data are available:

```text
evidence-synthesis
      ↓
meta-analysis
```

Pass:

- study identities;
- effect measures;
- uncertainty;
- design;
- population;
- outcome;
- timepoint;
- dependence structure;
- heterogeneity-relevant features.

---

# 18. No Forced Meta-Analysis

Do not pool merely because several studies report numeric outcomes.

Pooling may be inappropriate because of:

- incompatible populations;
- different interventions;
- different outcome definitions;
- different timepoints;
- different designs;
- dependent samples;
- severe clinical heterogeneity.

Narrative synthesis may be more defensible.

---

# 19. Narrative Synthesis

Narrative synthesis should identify patterns across studies.

Preferred structure:

```text
finding pattern
      ↓
which evidence supports it
      ↓
where it differs
      ↓
why it may differ
      ↓
remaining uncertainty
```

Avoid article-by-article chronology unless the historical sequence is scientifically relevant.

---

# 20. Narrative Synthesis Template

Use:

```text
Across [evidence set], [pattern] is generally observed in [conditions/populations].
However, [contradictory or divergent pattern] appears in [conditions].
Differences may relate to [method/population/measurement/context].
The evidence therefore supports [calibrated conclusion], while [uncertainty] remains.
```

Do not insert causes unless supported.

---

# 21. Thematic Synthesis

`THEMATIC_SYNTHESIS` groups findings by scientifically meaningful themes.

Possible themes may reflect:

- mechanisms;
- barriers;
- facilitators;
- outcomes;
- contexts;
- methods;
- experiences;
- implementation factors.

Themes should emerge from evidence rather than arbitrary headings.

---

# 22. Theme Record

Use:

```yaml
theme:
  theme_id:
  label:
  supporting_studies:
  contradictory_studies:
  population_scope:
  context_scope:
  evidence_pattern:
  uncertainty:
  notes:
```

---

# 23. Configurative Synthesis

`CONFIGURATIVE_SYNTHESIS` organizes conceptual configurations rather than estimating one overall effect.

Useful for:

- conceptual mapping;
- qualitative evidence;
- mixed literatures;
- framework development;
- CKCA-like configuration tasks.

Possible configuration statuses:

- `WIDELY_SUPPORTED`
- `CONTEXT_SPECIFIC`
- `EMERGING`
- `CONTESTED`
- `ABSENT_IN_CORPUS`
- `INSUFFICIENT_EVIDENCE`

Do not equate absence in one corpus with absence from the global literature.

---

# 24. Mechanism Synthesis

`MECHANISM_SYNTHESIS` asks:

> Through what process could the observed relationship occur?

Distinguish:

- directly tested mechanism;
- mediator evidence;
- biological pathway evidence;
- theoretical mechanism;
- plausible but untested explanation.

---

# 25. Mechanism Strength

Possible labels:

- `DIRECTLY_TESTED`
- `PARTIALLY_TESTED`
- `SUPPORTED_INDIRECTLY`
- `HYPOTHESIZED`
- `SPECULATIVE`
- `NOT_EVALUATED`

Do not upgrade speculation into mechanism evidence.

---

# 26. Mechanism Chain

When supported:

```text
Exposure / Intervention
      ↓
Intermediate Process
      ↓
Mediator / Mechanism
      ↓
Outcome
```

Each arrow should have evidence appropriate to its claim.

---

# 27. Mediation Guard

A statistical mediation model does not automatically prove biological or causal mediation.

Consider:

- temporal ordering;
- confounding;
- measurement;
- causal assumptions;
- design.

---

# 28. Theory Synthesis

`THEORY_SYNTHESIS` may organize:

- original theory;
- refinements;
- competing theories;
- empirical support;
- boundary conditions;
- contradictions.

Route formal theory selection to:

`theoretical-framework`

---

# 29. Theory Evidence Table

Use:

| Theory | Supporting Evidence | Contradictory Evidence | Boundary Conditions | Current Status |
|---|---|---|---|---|

---

# 30. Method Synthesis

`METHOD_SYNTHESIS` compares:

- study design;
- measurement;
- sampling;
- analysis;
- validation;
- reproducibility;
- limitations.

Do not assume the newest method is best.

---

# 31. Method Comparison Matrix

Use:

| Method | Purpose | Strength | Limitation | Evidence Base | Context |
|---|---|---|---|---|---|

Route design selection to:

`methodology-architect`

and analytical-method selection to:

`statistical-method-selector`

when appropriate.

---

# 32. Measurement Synthesis

Compare instruments or measures by:

- construct;
- validity;
- reliability;
- sensitivity;
- specificity;
- responsiveness;
- population;
- language;
- setting.

Route new instrument development to:

`instrument-design`

---

# 33. Measurement Non-Equivalence

Different measures of a construct may produce different findings.

Do not synthesize them as identical without justification.

Possible status:

`MEASUREMENT_HETEROGENEITY`

---

# 34. Conceptual Synthesis

When studies operationalize overlapping constructs, distinguish:

- identical constructs;
- related constructs;
- nested constructs;
- competing constructs;
- terminological variants.

Route formal organization to:

`conceptual-framework`

---

# 35. Construct Drift Guard

A construct may change meaning across:

- disciplines;
- time;
- cultures;
- instruments.

Do not synthesize by label alone.

---

# 36. Population Synthesis

Compare evidence by:

- age;
- sex;
- disease severity;
- ethnicity when scientifically relevant;
- occupation;
- educational level;
- clinical status;
- species;
- other population features.

Do not generalize beyond represented populations without justification.

---

# 37. Geographic Synthesis

Geographic differences may reflect:

- healthcare systems;
- culture;
- policy;
- environment;
- infrastructure;
- socioeconomic conditions.

Do not treat country difference itself as mechanism evidence.

---

# 38. Context Synthesis

Relevant contexts may include:

- hospital;
- community;
- workplace;
- school;
- laboratory;
- market;
- regulatory environment;
- digital platform.

Context may explain heterogeneity.

---

# 39. Temporal Synthesis

Organize evidence across time when the field evolves.

Possible phases:

```text
Foundational
      ↓
Development
      ↓
Consolidation
      ↓
Contestation
      ↓
Current Frontier
```

Route formal trend analysis to:

`trend-detection`

---

# 40. Evidence Recency

Recent evidence may better represent current practice or technology.

Older evidence may remain essential for:

- foundational theory;
- seminal methods;
- long-term outcomes.

Do not apply recency mechanically.

---

# 41. Convergence

Convergence occurs when independent evidence points toward a similar scientific conclusion.

Assess:

- direction;
- magnitude;
- population;
- design;
- measurement;
- independence.

Do not count multiple publications from one cohort as stronger convergence.

---

# 42. Convergence Levels

Possible labels:

- `STRONG_CONVERGENCE`
- `MODERATE_CONVERGENCE`
- `WEAK_CONVERGENCE`
- `APPARENT_CONVERGENCE`
- `NO_CLEAR_CONVERGENCE`

These are qualitative synthesis labels unless a formal grading framework is used.

---

# 43. Convergence Record

Use:

```yaml
convergence:
  finding:
  supporting_studies:
  independent_studies:
  designs:
  populations:
  consistency:
  important_exceptions:
  confidence:
  notes:
```

---

# 44. Contradiction

Contradictory evidence is evidence that materially challenges the dominant pattern.

It may involve:

- opposite direction;
- null result;
- different mechanism;
- different subgroup result;
- failed replication;
- incompatible theoretical interpretation.

Do not hide contradiction.

---

# 45. Contradiction Classification

Possible classes:

- `DIRECT_CONTRADICTION`
- `PARTIAL_CONTRADICTION`
- `CONTEXTUAL_DIVERGENCE`
- `METHOD_DEPENDENT_DIVERGENCE`
- `POPULATION_DEPENDENT_DIVERGENCE`
- `MEASUREMENT_DEPENDENT_DIVERGENCE`
- `TEMPORAL_DIVERGENCE`
- `APPARENT_ONLY`
- `UNRESOLVED`

---

# 46. Contradiction Matrix

Use:

| Study | Finding | Contradicts What? | Key Difference | Possible Explanation | Status |
|---|---|---|---|---|---|

---

# 47. Contradiction Explanation Guard

Do not explain contradictions by speculation alone.

Possible explanations should be labeled:

- `SUPPORTED`
- `PLAUSIBLE`
- `HYPOTHESIZED`
- `UNKNOWN`

---

# 48. Null Findings

Null or inconclusive findings should be synthesized alongside positive findings.

Do not treat them as methodological failures without evidence.

---

# 49. Failed Replication

A failed replication may indicate:

- original false positive;
- context dependence;
- measurement difference;
- insufficient replication fidelity;
- heterogeneity;
- chance.

Do not decide the explanation automatically.

---

# 50. Replication Synthesis

Classify:

- direct replication;
- conceptual replication;
- external validation;
- partial replication;
- failed replication.

Assess independence of samples and research groups.

---

# 51. Independent Evidence

Independent evidence usually means distinct:

- sample;
- cohort;
- dataset;
- research team;
- setting.

Shared data should be labeled.

---

# 52. Heterogeneity

Heterogeneity means meaningful variation in findings or study characteristics.

Possible sources include:

- population;
- exposure;
- intervention;
- outcome;
- measurement;
- dose;
- follow-up;
- design;
- analysis;
- context.

---

# 53. Heterogeneity Classification

Use when useful:

- `CLINICAL_HETEROGENEITY`
- `METHODOLOGICAL_HETEROGENEITY`
- `STATISTICAL_HETEROGENEITY`
- `CONCEPTUAL_HETEROGENEITY`
- `CONTEXTUAL_HETEROGENEITY`
- `TEMPORAL_HETEROGENEITY`

---

# 54. Statistical Heterogeneity Boundary

Formal statistics such as:

- I²;
- τ²;
- Q;

belong to quantitative synthesis when computed appropriately.

Do not report them without calculation.

Route to:

`meta-analysis`

---

# 55. Heterogeneity Explanation Matrix

Use:

| Difference | Studies Affected | Direction | Plausible Explanation | Evidence |
|---|---|---|---|---|

---

# 56. Moderator Signals

Evidence may suggest effect modification by:

- age;
- sex;
- dose;
- baseline severity;
- context;
- genotype;
- intervention intensity;
- follow-up;
- method.

Do not call a variable a moderator unless the evidence supports effect modification.

---

# 57. Subgroup Synthesis

Subgroup evidence should distinguish:

- prespecified subgroup;
- exploratory subgroup;
- post-hoc subgroup.

Do not generalize subgroup findings to the full population.

---

# 58. Dose–Response Synthesis

Assess whether evidence suggests:

- monotonic increase;
- monotonic decrease;
- threshold;
- U-shape;
- inverted U-shape;
- no pattern.

Do not infer dose response from isolated dose groups across incompatible studies.

---

# 59. Time–Response Synthesis

Time may change effects through:

- duration;
- latency;
- adaptation;
- follow-up;
- cumulative exposure.

Preserve timepoint comparability.

---

# 60. Causal Evidence Synthesis

For causal questions distinguish:

- randomized evidence;
- quasi-experimental evidence;
- longitudinal observational evidence;
- cross-sectional association;
- mechanistic evidence.

Do not average them conceptually as equivalent causal evidence.

---

# 61. Causal Claim Calibration

Use language proportional to the evidence.

Examples:

```text
associated with
predicts
is consistent with an effect
supports a possible causal role
causes
```

Use stronger wording only when design and assumptions support it.

---

# 62. Prediction Evidence Synthesis

Prediction synthesis may compare:

- discrimination;
- calibration;
- validation;
- generalizability;
- clinical utility.

Prediction does not establish causality.

---

# 63. Diagnostic Evidence Synthesis

Diagnostic synthesis may compare:

- sensitivity;
- specificity;
- AUC;
- likelihood ratios;
- thresholds;
- reference standards;
- spectrum effects.

Route formal quantitative diagnostic meta-analysis to:

`meta-analysis`

when appropriate.

---

# 64. Prognostic Evidence Synthesis

Compare:

- prognostic factors;
- model performance;
- time horizon;
- calibration;
- external validation.

Do not treat derivation performance as external validity.

---

# 65. Pharmacogenetic Evidence Synthesis

Possible dimensions:

- gene/SNP;
- genotype model;
- treatment;
- response outcome;
- toxicity outcome;
- population;
- allele frequency;
- adjustment;
- replication.

Do not treat different genetic models as interchangeable.

---

# 66. Pharmacokinetic Evidence Synthesis

Possible dimensions:

- population;
- drug;
- route;
- dose;
- PK parameter;
- assay;
- sampling;
- model;
- covariates.

Distinguish observed and model-derived parameters.

---

# 67. Pharmaceutical Formulation Synthesis

Possible dimensions:

- formulation;
- composition;
- preparation method;
- physicochemical characteristics;
- release profile;
- stability;
- biological activity;
- comparator.

Do not infer clinical effectiveness from in-vitro formulation performance.

---

# 68. Laboratory Evidence Synthesis

Separate:

- in vitro;
- ex vivo;
- animal;
- human;
- computational.

Do not collapse evidence levels.

---

# 69. Translational Gradient

Use when useful:

```text
Molecular / In Vitro
      ↓
Preclinical
      ↓
Early Human
      ↓
Clinical
      ↓
Implementation
```

Do not imply automatic translation across levels.

---

# 70. Qualitative Evidence Synthesis

For qualitative evidence synthesize:

- themes;
- experiences;
- meanings;
- barriers;
- facilitators;
- mechanisms;
- contexts.

Do not convert qualitative frequency into statistical prevalence.

Route specialized qualitative methodology to:

`qualitative-analysis`

---

# 71. Qualitative Theme Strength Guard

A theme appearing in many papers is not automatically more important than a theme appearing in fewer but information-rich studies.

Interpret qualitatively.

---

# 72. Mixed-Methods Synthesis

Mixed-method synthesis may integrate:

```text
Quantitative Pattern
      +
Qualitative Explanation
      ↓
Integrated Interpretation
```

Route formal integration design to:

`mixed-method-analysis`

---

# 73. Mixed-Methods Integration Modes

Possible relationships:

- convergence;
- complementarity;
- expansion;
- contradiction;
- explanation.

Do not force agreement between strands.

---

# 74. Evidence Role Synthesis

Organize studies by roles such as:

- direct evidence;
- mechanism evidence;
- method evidence;
- theory evidence;
- contradictory evidence;
- contextual evidence;
- replication;
- validation;
- novelty competitor.

Do not treat all roles as equivalent.

---

# 75. Direct vs Indirect Evidence

Preserve:

```text
direct evidence
≠
supporting evidence
≠
contextual evidence
```

A related study may inform interpretation without directly answering the synthesis question.

---

# 76. Phenomenon Evidence Boundary

Real-world magnitude, burden, policy, regulation, and official statistics belong primarily to:

`phenomenon-evidence-builder`

Do not merge them into scholarly study synthesis as though they were equivalent research designs.

---

# 77. Dual Evidence Architecture

Preserve:

```text
PHENOMENON EVIDENCE
Authority-first
      │
      ├── burden
      ├── trend
      ├── policy
      └── regulation

SCHOLARLY EVIDENCE
Scopus-first
      │
      ├── theory
      ├── mechanism
      ├── association
      ├── effect
      └── method
```

They can meet in problem framing but have different evidentiary roles.

---

# 78. Official Statistics Guard

Official statistics may establish:

- prevalence;
- incidence;
- counts;
- trends;
- service utilization.

They do not automatically establish mechanism or intervention effect.

---

# 79. Policy and Regulation Guard

Policies and regulations may establish:

- mandate;
- legal requirement;
- implementation context.

They do not establish scientific efficacy merely because they exist.

---

# 80. Evidence Maturity

Assess how developed the evidence base is.

Possible dimensions:

- number of independent studies;
- replication;
- methodological diversity;
- population diversity;
- consistency;
- mechanism evidence;
- validation;
- external generalization.

---

# 81. Evidence Maturity Status

Possible qualitative statuses:

- `NASCENT`
- `EMERGING`
- `DEVELOPING`
- `MATURE`
- `CONTESTED_MATURE`
- `FRAGMENTED`
- `INSUFFICIENT_TO_CLASSIFY`

Do not equate publication count with maturity.

---

# 82. Evidence Maturity Record

Use:

```yaml
evidence_maturity:
  topic:
  status:
  independent_studies:
  replication:
  methodological_diversity:
  population_diversity:
  consistency:
  mechanism_support:
  external_validation:
  uncertainty:
```

---

# 83. Evidence Certainty Boundary

Formal certainty grading systems such as GRADE require their own methodology.

Do not claim:

- `high certainty`;
- `moderate certainty`;
- `low certainty`;

unless a recognized certainty framework was actually applied.

---

# 84. Confidence Language

When no formal grading framework was applied, prefer qualitative language such as:

- strong convergence;
- moderate convergence;
- limited evidence;
- inconsistent evidence;
- preliminary evidence;
- substantial uncertainty.

---

# 85. Risk-of-Bias Boundary

Evidence synthesis should respect formal risk-of-bias assessments when available.

Do not invent risk-of-bias judgments.

If appraisal is required, use the appropriate review or methodology workflow.

---

# 86. Quality Weighting Guard

Do not silently weight studies based on prestige or subjective preference.

If studies receive differential interpretive weight, explain why.

Potential reasons:

- design relevance;
- directness;
- precision;
- replication;
- measurement quality;
- bias assessment;
- sample independence.

---

# 87. Evidence Hierarchy Guard

Evidence hierarchies are purpose-dependent.

For example:

- RCTs may be strong for intervention efficacy;
- qualitative studies may be strongest for lived experience;
- mechanistic experiments may be essential for mechanism.

Do not impose one universal hierarchy.

---

# 88. Large Sample Guard

A large sample does not automatically make a study more valid.

Consider:

- bias;
- measurement;
- design;
- confounding;
- relevance.

---

# 89. Prestigious Journal Guard

Journal prestige does not determine evidence weight.

---

# 90. Citation Count Guard

Citation count does not determine evidence weight.

---

# 91. Scopus Guard

Scopus indexing supports discoverability and source verification.

It does not prove:

- methodological rigor;
- causal validity;
- result truth.

---

# 92. APC Independence

APC status must not influence scientific evidence synthesis.

---

# 93. Target-Journal Independence

Target-journal strategy must not alter scientific conclusions.

Do not synthesize toward what a journal is presumed to prefer.

---

# 94. Confirmation Bias Guard

Actively ask:

> Which included studies most strongly challenge the emerging synthesis?

Do not construct a synthesis only from supportive findings.

---

# 95. Contradictory Evidence Search Handoff

If contradictions appear underexplored:

route to:

`citation-chaining`

and/or:

`scopus-literature-search`

for targeted expansion.

---

# 96. Missing Competitor Guard

If synthesis is being used for gap or novelty work and a close competitor is suspected but not verified:

do not finalize.

Route to:

`source-verification`

and:

`gap-validator`

or:

`novelty-auditor`

as appropriate.

---

# 97. Evidence Gap vs Search Gap

Preserve:

```text
few included studies
≠
research gap
```

Sparse evidence may result from:

- narrow criteria;
- terminology mismatch;
- database limits;
- emerging field.

Route gap claims to:

`gap-discovery`

then:

`gap-validator`

---

# 98. Absence Claim Guard

Do not write:

> No studies exist.

unless a sufficiently broad, current, and validated search supports that statement.

Prefer calibrated wording.

---

# 99. Evidence Synthesis and Gap Discovery

`evidence-synthesis` may identify candidate unresolved areas.

Route:

```text
evidence-synthesis
      ↓
gap-discovery
```

Candidate gaps remain unvalidated.

---

# 100. Gap Validation Handoff

A candidate gap should be challenged using:

- closest studies;
- recent literature;
- alternative terminology;
- equivalent methods;
- adjacent disciplines;
- citation chaining.

Route to:

`gap-validator`

---

# 101. Novelty Builder Handoff

After a sufficiently validated or reframed gap:

route to:

`novelty-builder`

Use synthesis to identify what the evidence already contains.

---

# 102. Novelty Auditor Handoff

Novelty claims should be stress-tested by:

`novelty-auditor`

Evidence synthesis does not certify novelty.

---

# 103. State-of-the-Art Handoff

When the objective is to characterize:

- established knowledge;
- emerging knowledge;
- contested knowledge;
- unresolved knowledge;
- frontier;

route to:

`sota-builder`

---

# 104. SoTA Relationship

Conceptually:

```text
evidence-synthesis
      ↓
sota-builder
```

Evidence synthesis identifies patterns.

SoTA places those patterns in the current intellectual structure of the field.

---

# 105. Research Landscape Relationship

A broad synthesis may feed:

`research-landscape`

for domain structure and thematic mapping.

Do not confuse landscape mapping with evidence conclusions.

---

# 106. Trend Detection Relationship

When temporal patterns matter:

route to:

`trend-detection`

Synthesis may provide scientific interpretation of the trend.

---

# 107. Emerging Topic Relationship

When recent evidence forms a new cluster:

route to:

`emerging-topic-discovery`

Do not call a topic emerging from recency alone.

---

# 108. Theoretical Framework Relationship

When evidence supports or challenges explanatory frameworks:

route to:

`theoretical-framework`

Evidence synthesis should preserve competing theory evidence.

---

# 109. Conceptual Framework Relationship

When studies reveal relationships among constructs:

route to:

`conceptual-framework`

Do not infer conceptual arrows beyond evidence.

---

# 110. Hypothesis Relationship

Synthesis may provide empirical support for hypothesis construction.

Route testable proposition development to:

`hypothesis-builder`

when appropriate.

Do not create hypotheses solely because a statistical pattern is common.

---

# 111. Methodology Relationship

When evidence indicates methodological strengths or limitations:

route study-design decisions to:

`methodology-architect`

---

# 112. Analysis Planning Relationship

When evidence reveals analytical approaches used in the field:

route study-specific analysis planning to:

`analysis-planner`

---

# 113. Statistical Method Relationship

When methods differ materially:

route statistical method selection to:

`statistical-method-selector`

Do not choose methods merely because they are common in prior papers.

---

# 114. Result Interpretation Relationship

For a new study's results:

`result-interpreter`

may compare current findings with the synthesized prior evidence.

Do not rewrite the synthesis to fit the new result.

---

# 115. Scientific Discussion Relationship

A high-quality synthesis directly supports:

`scientific-discussion`

by supplying:

- convergent evidence;
- contradictory evidence;
- mechanisms;
- context differences;
- methodological explanations;
- remaining uncertainty.

---

# 116. Discussion Guard

Do not use evidence synthesis to produce citation-by-citation discussion.

Prefer cross-study comparison.

---

# 117. Implication Relationship

When synthesis supports implications:

route to:

`implication-builder`

Separate:

- scientific implication;
- clinical implication;
- policy implication;
- educational implication;
- methodological implication.

---

# 118. Manuscript Writer Relationship

`manuscript-writer` may convert synthesis into manuscript prose.

It must preserve:

- uncertainty;
- evidence direction;
- contradictions;
- scope.

---

# 119. Manuscript Auditor Relationship

`manuscript-auditor` may verify whether the manuscript's literature claims match the evidence synthesis.

---

# 120. Reviewer Simulator Relationship

`reviewer-simulator` may challenge:

- selective synthesis;
- missing contradictions;
- unsupported causal language;
- weak novelty;
- outdated evidence.

---

# 121. Reviewer Response Relationship

When reviewers challenge evidence interpretation:

route to:

`reviewer-response`

A reviewer request should not override the evidence.

---

# 122. Systematic Review Synthesis

For systematic reviews, narrative synthesis should preserve:

- protocol-defined scope;
- included-study set;
- risk-of-bias information when assessed;
- heterogeneity;
- certainty framework when actually applied.

Do not invent formal certainty grades.

---

# 123. Meta-Analysis Relationship

If statistical pooling is required:

route to:

`meta-analysis`

Evidence synthesis can later interpret the pooled result together with:

- heterogeneity;
- study quality;
- context;
- mechanisms.

---

# 124. Meta-Analysis Does Not Replace Synthesis

A pooled estimate does not answer every scientific question.

Interpret:

- direction;
- magnitude;
- heterogeneity;
- applicability;
- contradictions;
- mechanisms.

---

# 125. Qualitative Synthesis Handoff

For deep qualitative coding or qualitative meta-synthesis tasks:

route to:

`qualitative-analysis`

Evidence synthesis may integrate the resulting themes.

---

# 126. Mixed-Method Synthesis Handoff

For formal mixed-method integration:

route to:

`mixed-method-analysis`

---

# 127. Evidence Pattern

A synthesis should identify the dominant evidence pattern.

Possible statuses:

- `CONSISTENT_SUPPORT`
- `MOSTLY_SUPPORTIVE`
- `MIXED`
- `CONTEXT_DEPENDENT`
- `MOSTLY_NULL`
- `MOSTLY_CONTRADICTORY`
- `INSUFFICIENT`
- `TOO_HETEROGENEOUS_TO_SUMMARIZE`

---

# 128. Pattern Record

Use:

```yaml
evidence_pattern:
  question:
  status:
  supporting_studies:
  contradictory_studies:
  null_studies:
  key_contexts:
  key_methods:
  key_populations:
  uncertainty:
  interpretation:
```

---

# 129. Evidence Map

A synthesis map may organize:

```text
Question
   │
   ├── Supporting Evidence
   │
   ├── Contradictory Evidence
   │
   ├── Mechanistic Evidence
   │
   ├── Context-Specific Evidence
   │
   └── Unresolved Evidence
```

Do not place studies into categories without justification.

---

# 130. Convergence–Divergence Map

Use:

```text
                 Evidence
                    │
        ┌───────────┴───────────┐
        ↓                       ↓
   Convergent                Divergent
        │                       │
   conditions               explanations
        │                       │
        └───────────┬───────────┘
                    ↓
            Calibrated Conclusion
```

---

# 131. Evidence Matrix

Recommended:

| Study | Design | Population | Finding | Direction | Mechanism | Limitations | Role |
|---|---|---|---|---|---|---|---|

---

# 132. Contradiction Matrix

Recommended:

| Study | Finding | Conflict | Key Difference | Explanation Status |
|---|---|---|---|---|

---

# 133. Mechanism Matrix

Recommended:

| Mechanism | Supporting Studies | Directly Tested? | Context | Uncertainty |
|---|---|---|---|---|

---

# 134. Method Matrix

Recommended:

| Method | Studies | Purpose | Strength | Limitation | Result Pattern |
|---|---|---|---|---|---|

---

# 135. Population Matrix

Recommended:

| Population | Evidence Pattern | Studies | Generalizability |
|---|---|---|---|

---

# 136. Temporal Matrix

Recommended:

| Period | Key Evidence | Development | Remaining Issue |
|---|---|---|---|

---

# 137. Synthesis Conclusion

A synthesis conclusion should state:

1. what is supported;
2. under what conditions;
3. where evidence diverges;
4. why divergence may occur;
5. what remains uncertain.

---

# 138. Conclusion Strength Calibration

Possible wording:

- "The evidence consistently indicates..."
- "Most studies suggest..."
- "Evidence is mixed..."
- "The pattern appears context-dependent..."
- "Evidence remains limited..."
- "The available studies are insufficient to determine..."

Choose wording proportional to evidence.

---

# 139. No Vote Counting

Do not synthesize by simply counting:

```text
7 significant
3 non-significant
```

Vote counting ignores:

- precision;
- magnitude;
- design;
- sample size;
- independence;
- heterogeneity.

---

# 140. Directional Vote-Counting Boundary

Direction summaries may be used descriptively when effect data cannot be pooled.

Label them as descriptive, not formal effect estimation.

---

# 141. Publication Bias Awareness

A synthesis should consider that published evidence may overrepresent:

- positive findings;
- statistically significant findings;
- novel findings.

Do not infer absence of unpublished evidence.

---

# 142. Selective Outcome Reporting Awareness

Different papers may selectively report outcomes.

Do not assume missing outcomes were null.

---

# 143. Small-Study Effects

Small studies may show unstable or extreme estimates.

Do not dismiss them automatically.

Formal small-study-effect analysis belongs to:

`meta-analysis`

when appropriate.

---

# 144. Citation Network Bias

Highly connected studies may dominate narratives.

Do not let network prominence substitute for scientific relevance.

---

# 145. Research Group Dependence

Several supportive studies from one research group may provide less independent confirmation than several studies from unrelated groups.

Label research-group concentration when material.

---

# 146. Dataset Dependence

Several analyses of one database may represent multiple questions but not multiple independent populations.

Preserve dataset dependence.

---

# 147. Replication Independence Matrix

Use:

| Study | Sample | Dataset | Research Group | Independent? |
|---|---|---|---|---|

---

# 148. Sensitivity Synthesis

When conclusions depend on debatable inclusion choices, compare:

```text
Primary Corpus
      vs
Sensitivity Corpus
```

State whether the conclusion changes.

---

# 149. Sensitivity Dimensions

Possible sensitivity checks:

- exclude preprints;
- exclude high-risk records;
- include broader population;
- include adjacent methods;
- separate study families;
- remove duplicated cohorts.

Do not conduct post-hoc sensitivity checks only to obtain a preferred conclusion.

---

# 150. Robustness of Synthesis

Possible statuses:

- `ROBUST`
- `MODERATELY_ROBUST`
- `SENSITIVE_TO_SCOPE`
- `SENSITIVE_TO_FEW_STUDIES`
- `NOT_ROBUST`
- `UNKNOWN`

These are qualitative unless formally defined.

---

# 151. Competing Explanation Synthesis

For every important pattern ask:

> What alternative explanation could account for this evidence?

Possible alternatives:

- confounding;
- selection;
- measurement;
- reverse causation;
- publication bias;
- contextual differences;
- model specification.

Do not invent explanations without evidence.

---

# 152. Competing Explanation Matrix

Use:

| Explanation | Evidence For | Evidence Against | Status |
|---|---|---|---|

---

# 153. Boundary Conditions

A finding may be valid only under particular:

- populations;
- doses;
- contexts;
- methods;
- time periods.

Identify boundary conditions rather than overgeneralizing.

---

# 154. Boundary Condition Record

Use:

```yaml
boundary_condition:
  finding:
  condition:
  supporting_studies:
  exception_studies:
  confidence:
```

---

# 155. Generalizability

Assess whether the evidence can reasonably extend beyond studied contexts.

Possible statuses:

- `BROADLY_GENERALIZABLE`
- `PARTIALLY_GENERALIZABLE`
- `CONTEXT_SPECIFIC`
- `INSUFFICIENT_TO_JUDGE`

Do not overgeneralize.

---

# 156. External Validity Guard

Replication across:

- populations;
- settings;
- geographies;
- time;

strengthens external validity.

But conceptual differences may still matter.

---

# 157. Applicability

Applicability asks whether evidence is relevant to the target decision or setting.

Separate applicability from internal validity.

---

# 158. Translational Applicability

For biomedical evidence, distinguish:

- biological plausibility;
- preclinical effect;
- clinical efficacy;
- clinical effectiveness;
- implementation feasibility.

Do not skip translational stages.

---

# 159. Implementation Evidence

Implementation evidence may address:

- feasibility;
- adoption;
- fidelity;
- acceptability;
- sustainability;
- cost.

Do not treat efficacy evidence as implementation evidence.

---

# 160. Economic Evidence Boundary

Cost or economic evidence may require dedicated economic methodology.

Do not infer cost-effectiveness from cost alone.

---

# 161. Safety Synthesis

Safety evidence may differ from efficacy evidence.

Synthesize:

- adverse events;
- severity;
- frequency;
- exposure duration;
- population;
- causality assessment.

Do not infer safety from absence of reported adverse events.

---

# 162. Rare Outcome Guard

Rare outcomes may require large datasets or long follow-up.

Do not treat lack of events in small studies as proof of absence.

---

# 163. Missing Data Across Studies

Studies may report incomplete variables.

Do not impute missing study-level findings unless a valid method is used.

Label:

`NOT_REPORTED`

---

# 164. Unclear Evidence

When details are unavailable:

use:

- `UNCLEAR`
- `NOT_REPORTED`
- `FULL_TEXT_REQUIRED`
- `AUTHOR_CLARIFICATION_REQUIRED`

rather than guessing.

---

# 165. Evidence Conflict Resolution

Conflicts should be investigated through:

1. study design;
2. population;
3. measurement;
4. intervention/exposure definition;
5. analysis;
6. time;
7. context;
8. independence;
9. bias assessment if available.

Do not resolve conflicts by prestige.

---

# 166. Outlier Study

A study whose findings differ strongly from others should not be removed merely for being an outlier.

Investigate why.

---

# 167. Outlier Explanation

Possible statuses:

- `METHODOLOGICALLY_EXPLAINED`
- `POPULATION_EXPLAINED`
- `MEASUREMENT_EXPLAINED`
- `CONTEXT_EXPLAINED`
- `STATISTICAL_CHANCE_POSSIBLE`
- `UNEXPLAINED`

---

# 168. Evidence Evolution

A field may change after:

- new technology;
- new measurement;
- new treatment;
- new theory;
- policy change.

Synthesis should not force old and new evidence into one static conclusion.

---

# 169. Superseded Evidence

Older evidence may be superseded if methods or definitions changed materially.

Do not discard historical evidence; label its current role.

---

# 170. Consensus Guard

Do not declare consensus unless broad, independent, and consistent evidence supports it.

Use:

`NO_FORMAL_CONSENSUS_ASSESSMENT`

when no consensus method was applied.

---

# 171. Contested Evidence

A field may remain contested despite many publications.

Potential signals:

- competing theories;
- repeated contradictory findings;
- methodological disputes;
- context-specific results.

This is a valid scientific state.

---

# 172. Emerging Evidence

Emerging evidence may show:

- few recent studies;
- novel mechanism;
- preliminary replication;
- rapidly increasing attention.

Do not call it established.

---

# 173. Established Evidence

Established evidence should show more than publication volume.

Look for:

- independent replication;
- consistency;
- methodological maturity;
- broad testing;
- stable definitions.

---

# 174. Unresolved Evidence

Unresolved evidence may result from:

- contradiction;
- insufficient studies;
- weak measurement;
- inconsistent methods;
- missing populations;
- inadequate follow-up.

This may feed gap discovery.

---

# 175. Frontier Evidence

Frontier evidence may involve:

- newest mechanism;
- emerging method;
- unresolved contradiction;
- under-tested population;
- new integration.

Formal classification belongs to:

`sota-builder`

---

# 176. Evidence Synthesis for SoTA

Provide to `sota-builder`:

```yaml
sota_input:
  established_patterns:
  emerging_patterns:
  contested_patterns:
  unresolved_patterns:
  frontier_signals:
  methodological_evolution:
  theory_evolution:
  contradictions:
  evidence_maturity:
```

---

# 177. Evidence Synthesis for Gap Discovery

Provide to `gap-discovery`:

```yaml
gap_input:
  unresolved_questions:
  weakly_tested_relationships:
  inconsistent_findings:
  population_boundaries:
  method_boundaries:
  mechanism_uncertainties:
  validation_needs:
  replication_needs:
```

Do not label these validated gaps.

---

# 178. Evidence Synthesis for Gap Validation

Provide to `gap-validator`:

```yaml
gap_validation_input:
  candidate_gap:
  direct_evidence:
  close_competitors:
  gap_threats:
  recent_evidence:
  adjacent_methods:
  contradictory_evidence:
  terminology_variants:
```

---

# 179. Evidence Synthesis for Novelty Builder

Provide to `novelty-builder`:

```yaml
novelty_input:
  what_is_established:
  what_is_partially_addressed:
  what_is_unresolved:
  closest_competitors:
  methodological_frontier:
  theoretical_frontier:
  contextual_frontier:
```

---

# 180. Evidence Synthesis for Novelty Auditor

Provide to `novelty-auditor`:

```yaml
novelty_audit_input:
  novelty_claim:
  closest_competitors:
  overlapping_contributions:
  prior_priority_claims:
  methodological_equivalents:
  cross_disciplinary_analogues:
  unresolved_threats:
```

---

# 181. Evidence Synthesis for Theory

Provide to `theoretical-framework`:

```yaml
theory_input:
  candidate_theories:
  empirical_support:
  contradictions:
  boundary_conditions:
  competing_explanations:
  mechanism_evidence:
```

---

# 182. Evidence Synthesis for Methodology

Provide to `methodology-architect`:

```yaml
methodology_input:
  common_designs:
  stronger_designs:
  recurring_limitations:
  measurement_patterns:
  sampling_patterns:
  methodological_gaps:
```

---

# 183. Evidence Synthesis for Discussion

Provide to `scientific-discussion`:

```yaml
discussion_input:
  convergent_findings:
  contradictory_findings:
  mechanisms:
  methodological_explanations:
  contextual_explanations:
  boundary_conditions:
  unresolved_uncertainty:
```

---

# 184. Evidence Synthesis for Manuscript

Provide to `manuscript-writer`:

```yaml
manuscript_evidence:
  claim:
  synthesis_conclusion:
  supporting_references:
  contradictory_references:
  uncertainty:
  permitted_language_strength:
```

---

# 185. Claim–Synthesis Record

Use:

```yaml
claim_synthesis:
  claim_id:
  proposed_claim:
  evidence_pattern:
  supporting_studies:
  contradictory_studies:
  directness:
  uncertainty:
  allowed_wording:
  prohibited_overstatement:
```

---

# 186. Claim Strength Guard

The manuscript claim must not be stronger than the synthesis.

If evidence is mixed:

do not write:

> X causes Y.

Prefer:

> Evidence regarding the association between X and Y is mixed.

---

# 187. Evidence Traceability

Every major synthesis statement should be traceable to the included evidence set.

Avoid unsupported generalizations.

---

# 188. Reference Cluster Traceability

For each synthesis statement, preserve which sources support:

- main pattern;
- exception;
- mechanism;
- explanation.

---

# 189. Contradictory Source Visibility

Contradictory sources should remain visible in outputs.

Do not hide them in notes when they materially change interpretation.

---

# 190. Evidence Map Record

Use:

```yaml
evidence_map:
  question:
  supporting:
  contradictory:
  mechanism:
  contextual:
  methodological:
  unresolved:
  conclusion:
```

---

# 191. Synthesis Passport

Use:

```yaml
evidence_synthesis:
  purpose:
  corpus_version:
  synthesis_mode:
  study_unit:
  evidence_pattern:
  convergence:
  contradiction:
  heterogeneity:
  mechanism_status:
  evidence_maturity:
  major_boundary_conditions:
  major_uncertainties:
  sensitivity_status:
  formal_certainty_framework_used:
  meta_analysis_performed:
  unresolved_items:
  next_stage:
```

Do not fabricate values.

---

# 192. Synthesis Status

Possible statuses:

- `NOT_STARTED`
- `CORPUS_NOT_READY`
- `SYNTHESIS_IN_PROGRESS`
- `CONTRADICTION_REVIEW_REQUIRED`
- `META_ANALYSIS_HANDOFF`
- `SEARCH_UPDATE_REQUIRED`
- `SYNTHESIS_COMPLETE`
- `READY_FOR_SOTA`
- `READY_FOR_GAP_DISCOVERY`
- `READY_FOR_GAP_VALIDATION`
- `READY_FOR_NOVELTY_DEVELOPMENT`
- `READY_FOR_DISCUSSION`

---

# 193. Corpus Readiness Gate

Before synthesis, verify:

- screening purpose is known;
- critical records are verified;
- duplicates are resolved;
- study families are identified when material;
- retractions are handled;
- major full-text uncertainties are documented.

---

# 194. Synthesis Completion Gate

Before `SYNTHESIS_COMPLETE`, verify:

- major findings are represented;
- contradictions are represented;
- heterogeneity is examined;
- mechanism claims are calibrated;
- uncertainty is explicit;
- evidence roles are distinguished;
- no obvious selective citation remains.

---

# 195. SoTA Readiness Gate

Before `READY_FOR_SOTA`, ensure enough evidence exists to distinguish:

- established;
- emerging;
- contested;
- unresolved;
- frontier.

---

# 196. Gap Readiness Gate

Before `READY_FOR_GAP_VALIDATION`, ensure:

- latest close competitors are included;
- gap threats are visible;
- equivalent methods are considered;
- alternative terminology is considered;
- contradictory evidence is not suppressed.

---

# 197. Novelty Readiness Gate

Before `READY_FOR_NOVELTY_DEVELOPMENT`, ensure:

- what is already known is explicit;
- closest competitors are visible;
- candidate novelty does not rest only on geography, software, or extra variables;
- unresolved priority threats are identified.

---

# 198. Discussion Readiness Gate

Before `READY_FOR_DISCUSSION`, ensure synthesis can explain:

- agreement;
- disagreement;
- mechanisms;
- context;
- limitations;
- remaining uncertainty.

---

# 199. Search Update Trigger

Trigger targeted updating when:

- corpus is outdated;
- a key recent competitor is suspected;
- contradiction is underexplored;
- a review search date is old;
- a reviewer identifies new evidence.

Route to:

`scopus-literature-search`

and/or:

`citation-chaining`

---

# 200. Source Reverifiability Trigger

If a key record becomes questionable:

route to:

`source-verification`

Do not continue synthesis on unresolved critical identity.

---

# 201. Reference Integrity Trigger

If claim–source representation becomes questionable:

route to:

`reference-integrity-guard`

---

# 202. Screening Reassessment Trigger

If new evidence or new criteria affect eligibility:

route to:

`literature-screening`

Do not insert a paper directly into the synthesis without screening when eligibility matters.

---

# 203. Meta-Analysis Trigger

Route to:

`meta-analysis`

when:

- effect estimates are compatible;
- quantitative pooling answers the question;
- study dependence can be handled;
- statistical synthesis is justified.

---

# 204. Theory Trigger

Route to:

`theoretical-framework`

when the synthesis identifies:

- competing theories;
- explanatory gaps;
- boundary conditions;
- theory adaptation needs.

---

# 205. Conceptual Framework Trigger

Route to:

`conceptual-framework`

when:

- construct relationships need formal organization;
- alternative conceptual structures exist;
- variables/constructs need role classification.

---

# 206. Methodology Trigger

Route to:

`methodology-architect`

when the synthesis identifies a design decision for the new study.

---

# 207. Statistical Method Trigger

Route to:

`statistical-method-selector`

when the synthesis identifies competing analytical methods for the same research question.

---

# 208. Qualitative Analysis Trigger

Route to:

`qualitative-analysis`

when detailed qualitative coding or synthesis is required.

---

# 209. Mixed-Method Trigger

Route to:

`mixed-method-analysis`

when formal integration of quantitative and qualitative strands is required.

---

# 210. Result Interpretation Trigger

Route to:

`result-interpreter`

when synthesizing prior evidence specifically to interpret new empirical results.

---

# 211. Scientific Discussion Trigger

Route to:

`scientific-discussion`

when the evidence pattern must be transformed into a manuscript-level comparative explanation.

---

# 212. Implication Trigger

Route to:

`implication-builder`

when conclusions support implications that must be separated by level and strength.

---

# 213. Manuscript Trigger

Route to:

`manuscript-writer`

when the synthesis is scientifically stable and prose is needed.

---

# 214. Reviewer Trigger

Route to:

`reviewer-response`

when actual reviewer or editor feedback challenges the evidence synthesis.

---

# 215. Reviewer Simulation Trigger

Route to:

`reviewer-simulator`

when adversarial pre-submission testing of synthesis claims is desired.

---

# 216. Synthesis Error: Article Parade

Avoid:

```text
Study A found...
Study B found...
Study C found...
```

without cross-study interpretation.

This is summary, not synthesis.

---

# 217. Synthesis Error: Forced Consensus

Do not convert mixed evidence into:

> The literature consistently shows...

when meaningful contradictions exist.

---

# 218. Synthesis Error: Significance Counting

Do not decide a conclusion by counting significant p-values.

---

# 219. Synthesis Error: Prestige Weighting

Do not privilege a study merely because it appears in a prestigious journal.

---

# 220. Synthesis Error: Selective Recency

Do not cite only recent supportive evidence while ignoring older contradictory evidence.

---

# 221. Synthesis Error: Mechanism Invention

Do not invent mechanisms to make inconsistent evidence appear coherent.

---

# 222. Synthesis Error: Geographic Novelty

Do not infer a scientific gap merely because no study in one country was included.

---

# 223. Synthesis Error: Software Novelty

Do not infer novelty merely because a different software package was used.

---

# 224. Synthesis Error: Variable Addition

Adding variables does not automatically create meaningful novelty.

---

# 225. Synthesis Error: Publication Volume

Many publications do not prove maturity, consensus, or effect.

---

# 226. Synthesis Error: One Review Dependency

Do not let one review define the entire evidence landscape when primary studies or newer evidence are needed.

---

# 227. Synthesis Error: Secondary-Source Substitution

Recover primary sources when central claims depend on them and primary verification is feasible.

---

# 228. Synthesis Error: Unverified Full Text

Do not claim detailed study-level findings if only metadata or abstract were available.

---

# 229. Synthesis Error: Corpus Drift

Do not silently add or remove studies during interpretation.

Update the corpus version and screening status.

---

# 230. Synthesis Error: Study-Family Inflation

Do not treat multiple publications from the same cohort as independent confirmation.

---

# 231. Synthesis Error: Target-Journal Bias

Do not modify the evidence conclusion to fit a target journal.

---

# 232. Synthesis Error: APC Bias

Do not alter evidence inclusion or interpretation based on APC status.

---

# 233. Synthesis Error: Reviewer Appeasement

Do not change scientific synthesis merely to satisfy reviewer preference when evidence does not support the requested claim.

---

# 234. Evidence Synthesis Table

Recommended:

| Finding | Supporting Evidence | Contradictory Evidence | Context | Explanation | Conclusion |
|---|---|---|---|---|---|

---

# 235. Evidence Maturity Table

Recommended:

| Domain | Replication | Consistency | Diversity | Mechanism | Maturity |
|---|---|---|---|---|---|

---

# 236. Boundary Condition Table

Recommended:

| Finding | Holds When | Weakens When | Evidence |
|---|---|---|---|

---

# 237. Uncertainty Table

Recommended:

| Question | What Is Known | What Is Uncertain | Why |
|---|---|---|---|

---

# 238. Gap Signal Table

Recommended:

| Unresolved Area | Evidence Basis | Possible Gap Type | Validation Needed |
|---|---|---|---|

Do not label candidate signals as validated gaps.

---

# 239. Novelty Threat Table

Recommended:

| Competitor | Overlap | Difference | Threat Level | Verification |
|---|---|---|---|---|

---

# 240. Full Output

For a comprehensive task provide:

## A. Synthesis Question
[...]

## B. Corpus and Scope
[...]

## C. Synthesis Mode
[...]

## D. Core Evidence Pattern
[...]

## E. Convergent Evidence
[...]

## F. Contradictory Evidence
[...]

## G. Heterogeneity
[...]

## H. Mechanisms
[...]

## I. Population and Context Differences
[...]

## J. Methodological Explanations
[...]

## K. Evidence Maturity
[...]

## L. Boundary Conditions
[...]

## M. Uncertainty
[...]

## N. Candidate Gap Signals
[...]

## O. Novelty Threats
[...]

## P. Calibrated Scientific Conclusion
[...]

## Q. Readiness Status
[...]

## R. Recommended Next Skill
[...]

---

# 241. Compact Output

For a small synthesis use:

```text
Question:
Evidence pattern:
Supporting evidence:
Contradictory evidence:
Main explanation:
Uncertainty:
Conclusion:
Next step:
```

---

# 242. User-Friendly Behavior

Prefer:

> Across the included studies, the relationship is mostly supportive, but it is not uniform. The strongest divergence appears in studies using a different measurement approach, so the safest conclusion is that the association is supported under some measurement conditions rather than universally established.

Or:

> The studies do not form a simple consensus. Human clinical evidence is limited, while in-vitro and animal studies provide stronger mechanistic support. These evidence levels should remain separate.

Or:

> Several papers appear supportive, but three come from the same cohort. I would treat them as one study family rather than three independent replications.

Or:

> The evidence may suggest a gap, but synthesis alone cannot validate it. The candidate gap should now be tested by `gap-validator`.

---

# 243. Avoid These Behaviors

Do not:

- fabricate study findings;
- fabricate effect sizes;
- fabricate sample sizes;
- fabricate certainty grades;
- fabricate risk-of-bias judgments;
- claim meta-analysis when pooling was not performed;
- count statistical significance as evidence strength;
- suppress contradictory studies;
- count duplicate publications as independent evidence;
- count one cohort multiple times as replication;
- mix direct, supporting, and contextual evidence without labels;
- treat mechanism hypotheses as proven mechanisms;
- infer causality from association-only evidence;
- claim consensus without broad support;
- claim absence of evidence from a narrow corpus;
- certify a research gap;
- certify novelty;
- choose a methodology solely because it is common;
- use journal prestige, quartile, citation count, APC, or target-journal strategy to weight scientific truth;
- strengthen language merely to satisfy reviewers;
- turn an evidence synthesis into an article-by-article literature list.

---

# Stop Conditions

Do not mark evidence synthesis complete when:

- the purpose-specific corpus is undefined;
- critical included studies remain unverified;
- retracted or duplicate records materially contaminate the corpus;
- study-family dependence materially distorts apparent replication;
- major contradictory evidence has not been examined;
- effect measures are being compared incompatibly;
- mechanism claims exceed the available evidence;
- a required search update has not been completed;
- a gap or novelty conclusion is being inferred without adversarial downstream validation;
- formal certainty language is being used without an actual certainty framework;
- a claimed pooled effect has not been formally calculated;
- the synthesis conclusion cannot be traced to the included studies.

Use:

- `CORPUS_NOT_READY`
- `SOURCE_VERIFICATION_REQUIRED`
- `REFERENCE_INTEGRITY_REQUIRED`
- `SCREENING_REASSESSMENT_REQUIRED`
- `SEARCH_UPDATE_REQUIRED`
- `CONTRADICTION_REVIEW_REQUIRED`
- `META_ANALYSIS_REQUIRED`
- `GAP_VALIDATION_REQUIRED`
- `NOVELTY_AUDIT_REQUIRED`
- `SYNTHESIS_INCOMPLETE`
- `NOT_READY_FOR_DOWNSTREAM_USE`

as appropriate.

---

# Success Criterion

`evidence-synthesis` succeeds when a purpose-specific corpus of sufficiently verified, integrity-cleared, and screened scholarly evidence is transformed into a traceable cross-study scientific interpretation rather than an article-by-article summary; when study families, duplicate publications, shared datasets, evidence roles, effect directions, magnitudes, uncertainty, populations, contexts, methods, measurements, mechanisms, temporal development, replication, contradiction, and heterogeneity are distinguished accurately; when statistical significance, publication count, citation count, journal prestige, Scopus status, target-journal strategy, and APC preferences do not substitute for evidence strength; when contradictory and null evidence are represented rather than suppressed; when causal, mechanistic, predictive, diagnostic, prognostic, qualitative, mixed-method, experimental, pharmacogenetic, pharmacokinetic, formulation, and translational evidence are interpreted according to their appropriate inferential roles; when formal meta-analysis, certainty grading, or risk-of-bias claims are made only if those procedures were actually performed; when evidence maturity, boundary conditions, generalizability, competing explanations, and remaining uncertainty are calibrated transparently; when phenomenon evidence remains distinct from scholarly evidence while both can inform broader problem framing; when candidate unresolved areas are routed to `gap-discovery` and `gap-validator`, candidate contributions to `novelty-builder` and `novelty-auditor`, intellectual-state classification to `sota-builder`, methodological decisions to the appropriate design or analysis skill, and manuscript-level interpretation to `scientific-discussion`; and when every major synthesis conclusion is sufficiently supported, balanced, current, and traceable to the underlying evidence to serve as a scientifically defensible basis for the next research workflow.
