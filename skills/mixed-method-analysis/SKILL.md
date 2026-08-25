---
name: mixed-method-analysis
description: Plan, conduct, integrate, document, and audit mixed-method analysis after the quantitative and qualitative strands, research questions, methodology, sampling relationships, instruments, protocols, and strand-specific analyses are sufficiently clear. Use when a study requires integration of quantitative and qualitative evidence through connecting, building, merging, embedding, joint displays, case linkage, explanatory or exploratory sequence, or meta-inference, while preserving strand-specific rigor, timing, priority, contradictions, context, uncertainty, and explicit integration logic instead of treating mixed methods as two parallel analyses placed in the same manuscript.
---

# Mixed-Method Analysis

## Purpose

`mixed-method-analysis` determines how quantitative and qualitative evidence should be brought together so that the integrated result answers a mixed-method research question more strongly than either strand alone.

Its central question is:

> How should the quantitative and qualitative strands be connected, compared, transformed, merged, embedded, explained, expanded, or synthesized so that the final meta-inference is scientifically coherent, transparent, and faithful to both forms of evidence?

This skill operates after strand-specific analysis planning or execution.

It does not replace:

- `statistical-method-selector`;
- `qualitative-analysis`;
- `analysis-planner`;
- `methodology-architect`.

It integrates them.

---

# Core Principle

Use:

> Mixed methods requires integration.

A study is not mixed-method merely because it contains:

- a survey and interviews;
- numbers and quotations;
- a quantitative section and a qualitative section.

Integration must occur at one or more explicit points.

---

# Position in the Framework

Preferred architecture:

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
                           ↓
                    meta-inference
                           ↓
                   result-interpreter
```

Some designs integrate earlier:

```text
QUAN → QUAL
QUAL → QUAN
QUAN + QUAL
Embedded strand
Multiphase design
```

The sequence depends on the mixed-method design.

---

# Required Upstream Context

Use established information from:

- `analysis-planner`;
- `methodology-architect`;
- `statistical-method-selector`;
- `qualitative-analysis`;
- `sampling-strategy`;
- `instrument-design`;
- `protocol-builder`;
- `research-question-builder`;
- `theoretical-framework`;
- `conceptual-framework`.

Minimum useful context normally includes:

- mixed-method RQ;
- quantitative RQ;
- qualitative RQ;
- mixed-method design;
- timing;
- strand priority;
- sampling relationship;
- quantitative results;
- qualitative findings;
- case linkage when applicable;
- intended integration purpose;
- theory or framework when relevant.

Do not ask the researcher to repeat information already established.

---

# Readiness Gate

Classify:

- `READY_FOR_MIXED_METHOD_ANALYSIS`
- `MIXED_METHOD_RQ_UNCLEAR`
- `QUANTITATIVE_STRAND_NOT_READY`
- `QUALITATIVE_STRAND_NOT_READY`
- `INTEGRATION_PURPOSE_UNCLEAR`
- `SAMPLING_RELATIONSHIP_UNCLEAR`
- `CASE_LINKAGE_UNAVAILABLE`
- `MIXED_METHOD_DESIGN_UNCLEAR`
- `INTEGRATION_ALREADY_ESTABLISHED`
- `MIXED_METHOD_ANALYSIS_REQUIRES_REASSESSMENT`

Do not integrate strands mechanically if they answer unrelated questions.

---

# Mixed-Method Question

A genuine mixed-method question asks something that requires integration.

Examples:

- How do qualitative experiences explain the quantitative effect?
- How do quantitative patterns and qualitative mechanisms converge or diverge?
- Which qualitative categories can be transformed into variables for subsequent testing?
- Why did an intervention succeed for some groups but not others?
- How do statistical trends correspond to contextual implementation processes?

Do not treat separate strand questions as sufficient by themselves.

---

# Integration Purpose

Classify the primary purpose:

- `EXPLANATION`
- `EXPLORATION`
- `COMPLEMENTARITY`
- `TRIANGULATION`
- `DEVELOPMENT`
- `EXPANSION`
- `CONTEXTUALIZATION`
- `MECHANISM_ELABORATION`
- `VALIDATION`
- `DISCORDANCE_EXPLANATION`
- `CASE_PROFILING`
- `INTERVENTION_REFINEMENT`
- `IMPLEMENTATION_UNDERSTANDING`
- `THEORY_DEVELOPMENT`

More than one may apply.

---

# Mixed-Method Design Family

Common designs include:

- convergent;
- explanatory sequential;
- exploratory sequential;
- embedded;
- multiphase;
- transformative;
- intervention mixed methods;
- case-based mixed methods.

Do not label the design only after seeing which results are convenient to combine.

---

# Convergent Design

Typical structure:

```text
QUAN ─────┐
          ├── Integration
QUAL ─────┘
```

The strands are collected or analyzed in a broadly parallel period.

Integration may compare:

- convergence;
- complementarity;
- expansion;
- contradiction.

---

# Explanatory Sequential Design

Typical structure:

```text
QUAN
 ↓
Initial Interpretation
 ↓
QUAL sampling / questions built from QUAN findings
 ↓
QUAL
 ↓
Integration
```

The qualitative strand should explain selected quantitative findings.

Do not collect generic interviews unrelated to the quantitative results.

---

# Exploratory Sequential Design

Typical structure:

```text
QUAL
 ↓
Concept / Category Development
 ↓
Instrument / Variable / Hypothesis Building
 ↓
QUAN
 ↓
Integration
```

The quantitative strand should test, estimate, validate, or extend what emerged qualitatively.

---

# Embedded Design

One strand is nested inside another.

Examples:

```text
QUAN dominant study
   └── embedded QUAL process evaluation
```

or:

```text
QUAL dominant study
   └── embedded QUAN descriptive measurement
```

The embedded strand must have a defined purpose.

---

# Multiphase Design

Multiple linked studies or phases may combine:

- exploration;
- development;
- testing;
- implementation;
- evaluation.

Each phase should have explicit linkage.

---

# Strand Priority

Classify:

- `QUAN_PRIORITY`
- `QUAL_PRIORITY`
- `EQUAL_PRIORITY`
- `PRIORITY_VARIES_BY_PHASE`

Priority affects interpretation.

Do not assume equal weight merely because both strands are present.

---

# Timing

Classify:

- `CONCURRENT`
- `SEQUENTIAL_QUAN_TO_QUAL`
- `SEQUENTIAL_QUAL_TO_QUAN`
- `MULTIPHASE`
- `ITERATIVE`

Timing should match the design logic.

---

# Integration Point

Possible integration points:

- research-question development;
- sampling;
- instrument development;
- data collection;
- analysis;
- interpretation;
- joint display;
- meta-inference;
- intervention refinement;
- theory development.

Record all actual integration points.

---

# Integration Strategies

Core strategies include:

- connecting;
- building;
- merging;
- embedding;
- transforming;
- comparing;
- case linking;
- joint displays;
- weaving;
- narrative contiguous reporting;
- meta-inference.

---

# Connecting

Connecting occurs when one strand determines sampling or participants for another.

Example:

```text
QUAN results
   ↓
select extreme / typical / discrepant cases
   ↓
QUAL interviews
```

Document the selection rule.

---

# Building

Building occurs when one strand shapes:

- instrument items;
- interview questions;
- variables;
- hypotheses;
- intervention components;
- sampling categories.

Example:

```text
QUAL themes
   ↓
questionnaire item development
   ↓
QUAN validation
```

---

# Merging

Merging combines two completed datasets or result sets for comparison.

Possible bases:

- common construct;
- common cases;
- common time point;
- common outcome;
- common domain.

---

# Embedding

Embedding places one form of evidence inside a larger design.

Examples:

- qualitative process evaluation inside an RCT;
- quantitative attendance metrics inside ethnography.

---

# Data Transformation

Possible forms:

- qualitizing quantitative data;
- quantitizing qualitative data.

Use only when scientifically useful.

Transformation does not remove the need to preserve original evidence.

---

# Quantitizing Qualitative Data

Possible examples:

- category presence;
- coded frequencies;
- profile scores;
- binary theme indicators.

Do not reduce interpretive meaning to counts without preserving context.

---

# Qualitizing Quantitative Data

Possible examples:

- trajectory profiles;
- case typologies;
- high / medium / low patterns used for contextual interpretation.

Do not create arbitrary categories from continuous measures merely for narrative convenience.

---

# Case Linking

Case-level integration requires a valid linkage key.

Example:

```yaml
case_link:
  participant_id:
  quantitative_record:
  qualitative_record:
  time_alignment:
  linkage_quality:
```

Do not link cases probabilistically without documenting uncertainty.

---

# Case-Based Integration

Useful when:

- the same participants provide both data types;
- individual trajectories matter;
- outcome variation requires explanation.

Possible outputs:

- case profiles;
- case matrices;
- mixed-method typologies.

---

# Joint Display

A joint display visually integrates evidence.

Possible forms:

- side-by-side matrix;
- case-by-variable matrix;
- theme-by-statistic matrix;
- timeline;
- intervention-process-outcome display;
- convergence table;
- mechanism display.

The display should perform analysis, not decoration.

---

# Basic Joint Display

Example:

| Quantitative Finding | Qualitative Finding | Relationship | Integrated Interpretation |
|---|---|---|---|
| Higher adherence | Participants described strong family support | Convergence | Social support may help explain adherence differences |

---

# Joint Display Guard

Do not create a table where columns are merely copied from separate results without cross-strand interpretation.

---

# Convergence Assessment

Classify relationships between strands as:

- `CONVERGENCE`
- `COMPLEMENTARITY`
- `EXPANSION`
- `PARTIAL_CONVERGENCE`
- `DISCORDANCE`
- `SILENCE_QUAN`
- `SILENCE_QUAL`
- `NOT_COMPARABLE`

Do not force agreement.

---

# Convergence

Convergence occurs when different evidence supports a similar substantive interpretation.

It does not require identical wording or metrics.

---

# Complementarity

Complementarity occurs when one strand adds dimensions not captured by the other.

---

# Expansion

Expansion occurs when one strand broadens scope or reveals new aspects.

---

# Discordance

Discordance occurs when strands point toward different interpretations.

This is analytically valuable.

Do not hide contradictory findings.

---

# Silence

Silence occurs when one strand addresses something the other does not.

Silence is not necessarily contradiction.

---

# Discordance Analysis

When results conflict, investigate:

- measurement differences;
- timing;
- sample differences;
- context;
- response bias;
- implementation variation;
- conceptual mismatch;
- insufficient power;
- qualitative variation;
- missing cases;
- analytic assumptions.

---

# Sampling Relationship

Mixed-method sampling may be:

- identical;
- nested;
- parallel;
- multilevel;
- sequential;
- subset;
- independent but linked conceptually.

Record:

```yaml
sampling_relationship:
  quantitative_sample:
  qualitative_sample:
  relationship:
  linkage:
  rationale:
```

---

# Identical Sample

The same participants provide both quantitative and qualitative data.

Supports strong case-level integration.

---

# Nested Sample

The qualitative sample is a subset of the quantitative sample or vice versa.

Document selection logic.

---

# Parallel Samples

Different samples may represent the same population or phenomenon.

Integration is usually at construct or population level rather than individual case level.

---

# Multilevel Samples

Example:

- students provide survey data;
- teachers provide interviews;
- schools provide administrative data.

Integration occurs across levels.

Do not imply individual-level linkage where none exists.

---

# Sequential Sampling

One strand's results determine the next strand's sample.

This must be operationally documented.

---

# Extreme Case Sampling

May select cases with:

- unusually high outcomes;
- unusually low outcomes;
- unexpected residuals;
- discrepant patterns.

Do not select only cases that confirm expectations.

---

# Typical Case Sampling

Useful to understand ordinary patterns.

---

# Discrepant Case Sampling

Deliberately sample cases inconsistent with the dominant quantitative pattern.

This can strengthen explanation.

---

# Instrument Integration

One strand may inform instruments in another.

Examples:

- qualitative categories → survey items;
- quantitative anomalies → interview probes;
- implementation framework → both survey and interview domains.

---

# Construct Alignment

Before merging evidence, verify whether QUAN and QUAL actually address the same construct.

Do not merge:

- satisfaction scores;
- perceived trust;
- organizational commitment;

as if they were equivalent without conceptual justification.

---

# Measurement Alignment

Record:

```yaml
construct_alignment:
  construct:
  quantitative_measure:
  qualitative_domain:
  equivalence:
  limitations:
```

---

# Temporal Alignment

Integration may be invalid if strands represent very different time periods.

Check:

- baseline;
- intervention;
- follow-up;
- retrospective recall;
- policy period.

---

# Outcome-Process Integration

Common in intervention studies.

Example:

```text
Outcome effect
      +
Implementation process
      ↓
Why the intervention worked / did not work
```

---

# Mechanism Integration

Qualitative findings may help explain:

- how;
- why;
- for whom;
- under what conditions;

a quantitative association or effect occurs.

Do not claim mechanism solely from participant explanation without appropriate caution.

---

# Context-Mechanism-Outcome Integration

Useful for realist-informed work:

```text
Context
   ↓
Mechanism
   ↓
Outcome
```

Integrate quantitative outcome patterns with qualitative contextual evidence.

---

# Explanatory Integration

For explanatory sequential studies, qualitative analysis should directly address:

- unexpected quantitative findings;
- subgroup patterns;
- weak effects;
- strong effects;
- implementation variation;
- outliers.

---

# Exploratory Integration

For exploratory sequential designs, document how qualitative outputs became:

- constructs;
- items;
- variables;
- hypotheses;
- categories;
- interventions.

---

# Development Integration

When QUAL builds QUAN, preserve a traceability chain:

```text
Qualitative Quote
      ↓
Code
      ↓
Category
      ↓
Construct
      ↓
Item
      ↓
Quantitative Variable
```

Do not invent item meaning disconnected from qualitative evidence.

---

# Mixed-Method Causal Inference

Mixed methods can strengthen causal explanation through triangulation of:

- design;
- effect estimate;
- process;
- mechanism;
- implementation;
- context.

But qualitative explanation does not repair an invalid quantitative causal design.

---

# Mixed-Method Prediction

Qualitative evidence may improve:

- predictor discovery;
- usability;
- implementation;
- interpretation;
- decision context.

Prediction performance still requires quantitative validation.

---

# Mixed-Method Implementation Research

Often integrates:

- implementation outcomes;
- service outcomes;
- clinical / educational outcomes;
- barriers;
- facilitators;
- fidelity;
- adaptation;
- context.

Joint displays are especially useful.

---

# Strand-Specific Rigor

Mixed-method integration does not excuse weak strand analysis.

Quantitative strand should satisfy quantitative rigor.

Qualitative strand should satisfy qualitative rigor.

Use:

`WEAK_STRAND_LIMITS_META_INFERENCE`

when necessary.

---

# Strand Quality Matrix

| Strand | Design Quality | Measurement Quality | Analysis Quality | Limitations |
|---|---|---|---|---|

---

# Unequal Strand Quality

If one strand is substantially weaker, integrated conclusions should reflect that asymmetry.

Do not average evidence quality.

---

# Priority Weighting

Interpretation may give greater weight to:

- primary strand;
- stronger evidence;
- direct evidence;
- more relevant timing.

State the rationale.

---

# Mixed-Method Validity

Possible concerns include:

- integration validity;
- interpretive consistency;
- sampling fit;
- measurement alignment;
- timing fit;
- construct fit;
- inference transfer.

---

# Meta-Inference

A meta-inference is the integrated conclusion produced from both strands.

It should not simply repeat both findings.

Example:

Weak:
> Survey scores were high, and interviews were positive.

Stronger:
> High satisfaction scores were concentrated among participants who described rapid staff response and clear communication, suggesting that perceived responsiveness may be a key mechanism underlying the quantitative satisfaction pattern.

---

# Meta-Inference Structure

Recommended:

```yaml
meta_inference:
  mixed_method_question:
  quantitative_finding:
  qualitative_finding:
  integration_relationship:
  integrated_claim:
  mechanism_or_context:
  confidence:
  boundary_conditions:
  contradictions:
  limitations:
```

---

# Meta-Inference Strength

Classify:

- `STRONG`
- `MODERATE`
- `TENTATIVE`
- `CONTRADICTORY`
- `INCONCLUSIVE`

Base strength on both strand quality and integration quality.

---

# Boundary Conditions

State when integrated claims may depend on:

- setting;
- subgroup;
- time;
- implementation;
- policy;
- organizational context;
- culture.

---

# Contradiction as Finding

A contradiction can itself be a substantive result.

Example:

> Survey scores suggested high confidence, but observations showed repeated procedural errors.

This may indicate a difference between perceived and demonstrated competence.

---

# Perception vs Behavior

Do not treat self-report and observed behavior as equivalent evidence.

Mixed methods can reveal this mismatch.

---

# Individual vs Aggregate Integration

Do not link individual quotations to group-level statistics as if they came from the same person unless case linkage exists.

---

# Ecological Integration Guard

Avoid attributing group-level patterns to individuals without evidence.

---

# Quantitative Uncertainty

Integration should preserve:

- confidence intervals;
- effect uncertainty;
- model limitations;
- sampling limitations.

Do not integrate a noisy estimate as a definitive fact.

---

# Qualitative Uncertainty

Preserve:

- contradictory cases;
- contextual variation;
- tentative themes;
- reflexive limitations.

---

# Missing Integration Data

If linkage variables are missing or samples are not comparable, use:

`INTEGRATION_LIMITED_BY_LINKAGE`

Do not fabricate correspondence.

---

# Attrition Across Strands

Sequential designs may experience:

- quantitative attrition;
- qualitative follow-up refusal;
- missing linkage.

Document implications.

---

# Integration Bias

Potential biases include:

- selecting only confirming quotes;
- emphasizing significant quantitative results;
- ignoring contradictory cases;
- selecting qualitative subsamples after outcome review without transparency;
- privileging one method for prestige.

---

# Confirmation Bias Guard

Actively search for cross-strand contradictions.

---

# Cherry-Picking Guard

Do not pair one dramatic quote with a statistical result and call it integration.

Use the broader qualitative pattern.

---

# Significance-Driven Integration Guard

Do not integrate only statistically significant quantitative findings.

Non-significant but substantively important findings may also require explanation.

---

# Effect-Size Integration

Prioritize effect magnitude and uncertainty over binary significance labels.

---

# Subgroup Integration

Qualitative data may explain subgroup heterogeneity.

But subgroup interpretation requires:

- sufficient quantitative support;
- interaction logic;
- adequate qualitative representation.

---

# Residual-Based Sampling

In explanatory work, qualitative sampling may use model residuals to identify:

- unexpectedly high outcomes;
- unexpectedly low outcomes.

Document this explicitly.

---

# Profile Integration

Create participant or case profiles combining:

- quantitative indicators;
- qualitative themes;
- context.

---

# Mixed-Method Typology

A typology may emerge from integrated patterns.

Example:

| Quantitative Pattern | Qualitative Pattern | Type |
|---|---|---|
| High adherence | Strong family support | Supported adherers |
| Low adherence | High treatment burden | Burden-limited participants |

Do not force all cases into a typology.

---

# Data Transformation Guard

Quantitization or qualitization changes the representation of evidence.

Always retain the original source for interpretation.

---

# Integration Software

Possible tools include:

- spreadsheets;
- R;
- Python;
- NVivo;
- MAXQDA;
- mixed-method matrices;
- visualization tools.

Software is secondary to integration logic.

---

# Software Independence

Do not choose a mixed-method design because software can generate a joint display.

---

# AI-Assisted Integration

AI may help:

- organize cross-strand tables;
- retrieve linked excerpts;
- suggest candidate correspondences.

Human review remains required.

---

# AI Integration Guard

AI must not:

- invent linkages;
- invent quotations;
- resolve contradictions automatically;
- assign causal explanations without evidence.

---

# Joint Display Types

Possible displays:

- convergence coding matrix;
- explanatory follow-up matrix;
- case-level display;
- theme-by-effect display;
- temporal display;
- process-outcome display;
- building traceability display;
- instrument-development display;
- context-mechanism-outcome display.

---

# Convergence Coding Matrix

| Domain | QUAN | QUAL | Relationship | Integrated Interpretation |
|---|---|---|---|---|

---

# Explanatory Follow-Up Matrix

| Quantitative Finding | Selected Cases | Qualitative Explanation | Meta-Inference |
|---|---|---|---|

---

# Exploratory Building Matrix

| Qualitative Category | Evidence | Proposed Construct | Proposed Item / Variable | Quantitative Test |
|---|---|---|---|---|

---

# Case-Level Joint Display

| Case | Quantitative Profile | Qualitative Profile | Convergence / Discordance | Interpretation |
|---|---|---|---|---|

---

# Process-Outcome Joint Display

| Process Evidence | Outcome Pattern | Context | Mechanism Hypothesis |
|---|---|---|---|

---

# Integration Memo

Recommended:

```yaml
integration_memo:
  date:
  domain:
  quan_finding:
  qual_finding:
  relationship:
  alternative_explanation:
  contradiction:
  confidence:
  next_check:
```

---

# Meta-Inference Audit Trail

Preserve:

- strand results used;
- cases used;
- joint-display version;
- integration decisions;
- contradictions;
- revisions;
- excluded interpretations.

---

# Integration Versioning

Example:

```text
v0.1 — preliminary convergence matrix
v0.2 — added discrepant cases
v1.0 — finalized integrated interpretation
```

---

# Reporting Structure

Possible reporting strategies:

- weaving;
- contiguous;
- staged sequential;
- joint-display-centered.

Choose based on design.

---

# Weaving

Organize results by integrated domain.

Example:

```text
Theme / Domain 1
- quantitative evidence
- qualitative evidence
- integrated interpretation
```

This often makes integration visible.

---

# Contiguous Reporting

Report QUAN and QUAL in separate sections, then integrate.

If used, the final integration section must be substantive.

---

# Sequential Reporting

For sequential designs, report:

```text
Phase 1 findings
      ↓
Phase 2 design response
      ↓
Phase 2 findings
      ↓
Integration
```

---

# Mixed-Method Result Language

Prefer:

> The quantitative reduction in symptom score was concentrated among participants who described sustained adherence and strong family support, while participants reporting treatment burden showed smaller improvements.

Avoid:

> The quantitative and qualitative results were consistent.

unless the nature of consistency is explained.

---

# Triangulation

Triangulation may seek:

- convergence;
- complementarity;
- contradiction;
- completeness.

It is not limited to confirmation.

---

# Causal Meta-Inference Guard

Do not upgrade noncausal quantitative evidence into causal claims merely because qualitative narratives provide plausible mechanisms.

---

# Generalizability

Quantitative generalizability and qualitative transferability remain distinct.

Mixed methods does not automatically create universal generalizability.

---

# Ethical Integration

Linked datasets can increase re-identification risk.

Protect:

- linkage keys;
- quotations;
- sensitive attributes;
- small subgroup identities.

---

# Theory Integration

Theory may connect strands through:

- common constructs;
- mechanism;
- context;
- boundary conditions.

Do not force both strands into a theory that one contradicts.

---

# Conceptual Framework Integration

The conceptual framework may be updated after mixed-method analysis.

Record whether findings:

- support;
- refine;
- extend;
- contradict;
- contextualize;

the framework.

---

# Hypothesis Integration

Qualitative findings may:

- explain supported hypotheses;
- explain unsupported hypotheses;
- suggest moderators;
- reveal mechanisms;
- identify measurement problems.

Do not retroactively rewrite confirmatory hypotheses.

---

# Mixed-Method Mechanism Building

Possible sequence:

```text
QUAN effect pattern
      ↓
QUAL process evidence
      ↓
candidate mechanism
      ↓
cross-case check
      ↓
negative-case check
      ↓
integrated mechanism hypothesis
```

Label mechanism hypotheses appropriately.

---

# Mixed-Method Theory Building

Possible sequence:

```text
QUAL categories
      +
QUAN regularities
      ↓
Integrated propositions
      ↓
Conceptual model
      ↓
future testing
```

Do not call this confirmed theory unless independently tested.

---

# Intervention Refinement

Mixed-method evidence may identify:

- effective components;
- burdensome components;
- fidelity problems;
- contextual barriers;
- unintended effects.

Use integration to refine intervention design transparently.

---

# Longitudinal Mixed Methods

Possible designs combine repeated quantitative measures with repeated qualitative interviews.

Integration may examine:

- trajectory;
- turning points;
- divergence;
- adaptation.

---

# Multilevel Mixed Methods

Different strands may exist at different levels.

Example:

```text
Student outcomes
      +
Teacher interviews
      +
School policy documents
```

Integration must respect level.

---

# Cross-Level Inference Guard

Do not infer individual mechanisms directly from organization-level narratives without evidence.

---

# Meta-Inference Confidence

Consider:

- quantitative precision;
- qualitative depth;
- sample relationship;
- measurement alignment;
- timing;
- integration quality;
- contradictions.

---

# Meta-Inference Confidence Record

```yaml
meta_inference_confidence:
  quantitative_strength:
  qualitative_strength:
  integration_strength:
  discordance:
  boundary_conditions:
  overall:
```

---

# Integration Failure Modes

Common failures:

- no mixed-method question;
- no integration point;
- separate samples with no conceptual link;
- decorative quotations;
- significance-driven qualitative follow-up;
- unexamined discordance;
- incompatible time periods;
- construct mismatch;
- weak strand quality;
- unsupported causal meta-inference.

---

# Integration Failure Status

Use:

- `PARALLEL_METHODS_NOT_MIXED`
- `INTEGRATION_WEAK`
- `INTEGRATION_PARTIAL`
- `INTEGRATION_COHERENT`
- `INTEGRATION_STRONG`

---

# Mixed-Method Analysis Passport

Recommended internal representation:

```yaml
mixed_method_analysis:
  status:
  mixed_method_rq:
  design:
  purpose:
  priority:
  timing:
  quantitative_strand:
  qualitative_strand:
  sampling_relationship:
  construct_alignment:
  temporal_alignment:
  integration_points:
  integration_strategy:
  case_linkage:
  joint_displays:
  convergence:
  complementarity:
  discordance:
  silence:
  data_transformation:
  theory_integration:
  meta_inferences:
  confidence:
  boundary_conditions:
  ethics:
  audit_trail:
  result_interpreter_handoff:
```

Unknown fields remain unknown.

---

# Minimal Output

For a simple request provide:

## Mixed-Method Question
[...]

## Design
[...]

## Integration Purpose
[...]

## Integration Point
[...]

## Integration Strategy
[...]

## Joint Display
[...]

## Discordance Check
[...]

## Meta-Inference
[...]

---

# Comprehensive Output

When full mixed-method analysis is requested:

## A. Mixed-Method Research Question
[...]

## B. Design Family
[...]

## C. Strand Priority
[...]

## D. Timing
[...]

## E. Quantitative Strand
[...]

## F. Qualitative Strand
[...]

## G. Sampling Relationship
[...]

## H. Construct Alignment
[...]

## I. Temporal Alignment
[...]

## J. Integration Points
[...]

## K. Connecting
[...]

## L. Building
[...]

## M. Merging / Embedding
[...]

## N. Data Transformation
[...]

## O. Case Linkage
[...]

## P. Joint Displays
[...]

## Q. Convergence
[...]

## R. Complementarity
[...]

## S. Discordance
[...]

## T. Theory / Mechanism Integration
[...]

## U. Meta-Inference
[...]

## V. Confidence
[...]

## W. Boundary Conditions
[...]

## X. Audit Trail
[...]

## Y. Interpretation Handoff
[...]

---

# Relationship with Analysis Planner

`analysis-planner` determines that mixed-method integration is required.

`mixed-method-analysis` specifies and performs that integration.

Use:

```text
analysis-planner
      ↓
mixed-method-analysis
```

---

# Relationship with Statistical Method Selector

`statistical-method-selector` selects the quantitative method.

Its results become one evidence stream for integration.

---

# Relationship with Qualitative Analysis

`qualitative-analysis` develops themes, categories, cases, mechanisms, or theory.

These become the qualitative evidence stream for integration.

---

# Relationship with Methodology Architect

The mixed-method integration strategy must match the original mixed-method design.

Do not retrofit a design label after analysis.

---

# Relationship with Sampling Strategy

Sampling relationships determine which forms of integration are possible.

Do not perform participant-level merging without valid participant linkage.

---

# Relationship with Instrument Design

Construct alignment depends on whether quantitative and qualitative instruments address comparable concepts.

---

# Relationship with Protocol Builder

Timing, sequence, follow-up, and linkage procedures constrain integration.

---

# Relationship with Theoretical Framework

Theory may explain how strands are expected to connect.

Mixed-method findings may support, refine, or challenge theory.

---

# Relationship with Conceptual Framework

Integrated evidence may refine relationships, context, or mechanisms in the conceptual framework.

---

# Relationship with Result Interpreter

Pass final meta-inferences, contradictions, confidence, and boundaries to `result-interpreter`.

---

# User-Friendly Behavior

Prefer:

> Your survey and interviews are not yet integrated. Because the interviews were sampled from participants with unexpectedly high and low outcome scores, the strongest strategy is an explanatory joint display linking each quantitative pattern to the qualitative explanation and discrepant cases.

Or:

> This is exploratory sequential research. The qualitative categories should first be traced into proposed constructs and items, then the quantitative strand can test their structure. Integration occurs in that development chain, not merely in the discussion section.

Or:

> The survey suggests high self-confidence, but classroom observations show repeated implementation errors. That discordance is not a problem to hide; it may indicate a meaningful gap between perceived and demonstrated competence.

---

# Avoid These Behaviors

Do not:

- call a study mixed methods merely because it contains QUAN and QUAL data;
- report two disconnected result sections and claim integration;
- select only confirming quotations;
- integrate only statistically significant findings;
- ignore discordance;
- force convergence;
- merge constructs that are not conceptually equivalent;
- perform participant-level integration without linkage;
- ignore temporal mismatch;
- give equal evidentiary weight to strands of very different quality;
- reduce qualitative findings to counts without preserving meaning;
- let dramatic narratives override robust quantitative estimates;
- let statistical significance automatically override qualitative context;
- use a decorative joint display;
- invent mechanisms from correlation plus quotations;
- infer causality from mixed methods without causal design;
- hide sampling differences between strands;
- treat triangulation as automatic confirmation;
- allow software or AI to generate final meta-inference without researcher review.

---

# Stop Conditions

Do not classify mixed-method analysis as ready when:

- mixed-method RQ is unclear;
- one strand is not analytically ready;
- integration purpose is undefined;
- strand timing conflicts with the intended interpretation;
- sampling relationship is unknown;
- case linkage is required but unavailable;
- constructs are not comparable;
- integration consists only of juxtaposition;
- discordant findings are ignored;
- meta-inference exceeds the strength of one or both strands;
- causal interpretation exceeds design capability;
- AI or software output is being treated as integration without analytic review.

Use:

- `RETURN_TO_ANALYSIS_PLANNER`
- `RETURN_TO_STATISTICAL_METHOD_SELECTOR`
- `RETURN_TO_QUALITATIVE_ANALYSIS`
- `RETURN_TO_METHODOLOGY_ARCHITECT`
- `RETURN_TO_SAMPLING_STRATEGY`
- `MIXED_METHOD_ANALYSIS_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`mixed-method-analysis` succeeds when quantitatively and qualitatively analyzed evidence has been integrated through an explicit, design-consistent, transparent, and auditable strategy that identifies the mixed-method question, design family, strand priority, timing, sampling relationship, construct and temporal alignment, integration points, connecting, building, merging, embedding or transformation procedures, case linkage, joint displays, convergence, complementarity, expansion, discordance, silence, theory or mechanism relationships, uncertainty, boundary conditions, and final meta-inferences, while preserving strand-specific rigor and preventing decorative juxtaposition, significance-driven integration, forced agreement, invalid cross-level linkage, unsupported causal claims, software-driven synthesis, or AI-generated conclusions from replacing genuine mixed-method reasoning.
