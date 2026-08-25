---
name: scientific-discussion
description: Build a rigorous scientific discussion from already interpreted study results by comparing findings with verified scholarly evidence, current State of the Art, theory, mechanisms, competing explanations, contradictions, context, boundary conditions, and study limitations. Use when the researcher already has defensible result interpretations and needs to explain why the findings matter, how they converge with or diverge from prior studies, what mechanisms or theories are supported or challenged, which alternative explanations remain plausible, what the study contributes beyond existing literature, how far claims can be generalized, and what unresolved scientific questions remain, without turning the discussion into a literature summary, citation accumulation, post-hoc theory fitting, unsupported causality, or significance-driven storytelling.
---

# Scientific Discussion

## Purpose

`scientific-discussion` transforms defensibly interpreted findings into a coherent scientific explanation positioned against the current scholarly evidence base.

Its central question is:

> How should these findings be understood in relation to prior evidence, State of the Art, theory, mechanisms, competing explanations, context, contradictions, limitations, and the validated scientific contribution of the study?

This skill does not reinterpret raw software output from scratch.

It operates after `result-interpreter`.

It should not begin from:

- p-values alone;
- isolated coefficients;
- raw qualitative codes;
- unexplained model-fit statistics;
- software-generated labels;
- unverified citations.

---

# Core Principle

Use:

> Discussion explains scientific meaning; it does not merely repeat results or summarize literature.

The sequence is:

```text
Interpreted Finding
      ↓
Scientific Meaning
      ↓
Closest Prior Evidence
      ↓
Convergence / Divergence
      ↓
Theory / Mechanism
      ↓
Competing Explanation
      ↓
Context / Boundary Condition
      ↓
Validated Contribution
      ↓
Limitations
      ↓
Implication Handoff
```

Do not reverse this sequence.

---

# Position in the Framework

Preferred architecture:

```text
result-interpreter
      ↓
scientific-discussion
      ↓
implication-builder
```

Upstream evidence may come from:

```text
source-verification
      ↓
reference-integrity-guard
      ↓
evidence-synthesis
      ↓
sota-builder
```

The discussion must use verified evidence rather than citation volume.

---

# Required Upstream Context

Use established information from:

- `result-interpreter`;
- `evidence-synthesis`;
- `sota-builder`;
- `gap-validator`;
- `novelty-auditor`;
- `theoretical-framework`;
- `conceptual-framework`;
- `research-question-builder`;
- `hypothesis-builder`;
- `source-verification`;
- `reference-integrity-guard`;
- `phenomenon-evidence-builder` when real-world context is relevant.

Minimum useful context usually includes:

- research question;
- primary findings;
- secondary findings;
- prespecification status;
- effect magnitude or qualitative pattern;
- uncertainty;
- robustness;
- practical importance;
- hypothesis status;
- theory relationship;
- mechanism status;
- contradictions;
- unexpected findings;
- external-validity boundaries;
- supported and unsupported claims;
- validated gap;
- audited novelty;
- closest competitor studies;
- current State of the Art.

Do not ask the researcher to repeat information already established.

---

# Readiness Gate

Classify:

- `READY_FOR_SCIENTIFIC_DISCUSSION`
- `RESULT_INTERPRETATION_INCOMPLETE`
- `LITERATURE_CONTEXT_INCOMPLETE`
- `STATE_OF_ART_INCOMPLETE`
- `THEORY_STATUS_UNCLEAR`
- `CLOSEST_COMPETITOR_UNCLEAR`
- `SOURCE_VERIFICATION_INCOMPLETE`
- `DISCUSSION_ALREADY_ESTABLISHED`
- `SCIENTIFIC_DISCUSSION_REQUIRES_REASSESSMENT`

Do not build a confident discussion when the interpretation or evidence base is unstable.

---

# Discussion Object

The unit of discussion is not a paper.

It is a scientifically meaningful finding.

Possible discussion objects include:

- primary effect;
- secondary effect;
- null result;
- mediation result;
- moderation result;
- qualitative theme;
- mechanism;
- mixed-method meta-inference;
- pooled effect;
- prediction model performance;
- diagnostic performance;
- SEM relationship;
- PLS-SEM path;
- pharmacokinetic difference;
- pharmacogenetic association;
- unexpected result;
- contradiction;
- subgroup pattern.

---

# Finding Passport

For each finding use:

```yaml
discussion_finding:
  research_question:
  finding:
  prespecification_status:
  magnitude_or_pattern:
  uncertainty:
  robustness:
  claim_strength:
  closest_prior_evidence:
  convergence_status:
  theory_relationship:
  mechanism_status:
  alternative_explanations:
  context:
  boundary_conditions:
  contribution:
  limitation:
  implication_handoff:
```

---

# Discussion Priority

Discuss findings in this order unless the research logic clearly requires another order:

1. primary finding;
2. major secondary finding;
3. unexpected or contradictory finding;
4. mechanism or explanatory result;
5. robustness or sensitivity result;
6. contextual or subgroup finding.

Do not organize the discussion by output-table order.

---

# Opening the Discussion

The first paragraph should normally answer:

- What was the main finding?
- How strong was it?
- Was it expected?
- Why is it scientifically important?

Avoid opening with a generic literature summary.

---

# Main-Finding Opening Template

Prefer:

> The principal finding was that [finding], with [magnitude/pattern] and [uncertainty/robustness]. This result [supports/refines/challenges] the proposed explanation that [scientific meaning], while remaining bounded by [key limitation].

---

# Result Repetition Guard

Do not reproduce the entire Results section.

Discussion should use only the numerical detail necessary for interpretation.

---

# Literature Comparison Principle

Compare findings against the most relevant studies, not the largest possible number of citations.

Priority:

1. closest direct comparator;
2. strongest high-quality evidence;
3. recent synthesis;
4. seminal explanatory study;
5. contradictory evidence;
6. adjacent disciplinary evidence when necessary.

---

# Scopus-First Scholarly Context

When scholarly search is required, use the project's Scopus-first principle.

Fallback sources may include:

- OpenAlex;
- Crossref;
- PubMed;
- Semantic Scholar;
- publisher metadata.

Never claim direct Scopus verification unless it occurred.

---

# Source Verification Gate

Before a study supports a discussion claim, verify where feasible:

- title;
- authors;
- year;
- journal;
- DOI;
- article identity;
- retraction status;
- claim relevance.

Do not allow citation-looking text to become evidence automatically.

---

# Reference Integrity

Every citation should support the specific sentence or claim where it is placed.

Do not use:

- reference mashups;
- irrelevant citation clusters;
- prestige-only citations;
- target-journal padding;
- citations chosen because APC is favorable.

---

# Citation Role

Classify each reference role:

- `DIRECT_SUPPORT`
- `CONTRADICTORY_EVIDENCE`
- `MECHANISTIC_SUPPORT`
- `THEORY_SUPPORT`
- `METHOD_CONTEXT`
- `BACKGROUND_CONTEXT`
- `BOUNDARY_CONTEXT`

Do not cite references without a clear role.

---

# State-of-the-Art Alignment

The discussion should position findings against:

- established knowledge;
- emerging evidence;
- contested evidence;
- unresolved questions;
- active frontier.

Do not describe the literature as homogeneous when it is not.

---

# Convergence Status

For each finding classify:

- `CONSISTENT`
- `PARTIALLY_CONSISTENT`
- `EXTENDS`
- `REFINES`
- `CONTRADICTS`
- `MIXED`
- `NO_CLOSE_COMPARATOR`
- `INCONCLUSIVE`

---

# Consistent Finding

When a finding is consistent with prior evidence, explain what the replication or extension adds.

Do not stop at:

> This is consistent with previous studies.

Ask:

- Does it replicate in a new population?
- Does it strengthen a mechanism?
- Does it improve measurement?
- Does it add temporal evidence?
- Does it narrow uncertainty?
- Does it extend the boundary?

---

# Extension

A finding extends prior work when it adds a meaningful dimension such as:

- new mechanism;
- new population with scientific relevance;
- longitudinal evidence;
- stronger design;
- improved measurement;
- external validation;
- new context boundary;
- integrated mixed-method explanation;
- dose-response evidence;
- clinically relevant endpoint.

---

# Replication Value

Replication is scientifically valuable when it tests reproducibility or transportability.

Do not dismiss replication as "not novel" automatically.

---

# Contradictory Finding

When findings contradict prior evidence, assess:

1. measurement differences;
2. population differences;
3. intervention or exposure differences;
4. comparator differences;
5. timing;
6. design quality;
7. analytic model;
8. confounding;
9. sample size;
10. implementation;
11. random variation.

Do not choose one explanation merely because it protects the preferred conclusion.

---

# Contradiction Template

Prefer:

> This finding differs from [prior evidence]. The discrepancy may reflect [specific design/context differences], although sampling variation and residual bias remain plausible. Because [reason], the present result is better interpreted as evidence of a potential boundary condition than as definitive refutation.

---

# Contradictory Evidence Must Be Included

Actively seek evidence that challenges the preferred interpretation.

A discussion that ignores credible contradictory literature is incomplete.

---

# Theory Relationship

Classify:

- `SUPPORTS`
- `PARTIALLY_SUPPORTS`
- `REFINES`
- `EXTENDS`
- `CHALLENGES`
- `CONTRADICTS`
- `OUTSIDE_SCOPE`
- `INCONCLUSIVE`

---

# Theory Support Guard

Do not claim that a theory is "proven."

Prefer:

> The findings are consistent with a prediction of the theory.

---

# Theory Refinement

A study may refine theory by revealing:

- boundary conditions;
- moderator;
- mediator;
- temporal sequence;
- context dependency;
- measurement distinction;
- nonlinear relationship.

---

# Theory Contradiction

Contradictory findings may indicate:

- theory failure;
- scope boundary;
- operationalization problem;
- measurement problem;
- design limitation.

Do not assume theory failure immediately.

---

# Theory Retrofit Guard

Do not select a theory after seeing results solely because it explains the preferred pattern.

If theory was selected post hoc, label it clearly.

---

# Mechanism Status

Use:

- `DIRECTLY_TESTED`
- `INDIRECTLY_SUPPORTED`
- `PLAUSIBLE`
- `SPECULATIVE`
- `UNSUPPORTED`

---

# Mechanism Discussion

Mechanistic explanation should connect:

```text
Observed Pattern
      ↓
Biological / Behavioral / Social / Technical Process
      ↓
Expected Intermediate Consequence
      ↓
Observed Outcome
```

Each link should be supported or explicitly marked speculative.

---

# Biological Mechanism

Possible sources include:

- molecular pathways;
- receptor activity;
- metabolism;
- physiological response;
- inflammatory process;
- pharmacokinetics;
- pharmacodynamics.

Do not claim a biological mechanism when only an epidemiological association was observed.

---

# Pharmacological Mechanism

Distinguish:

- exposure;
- target engagement;
- pharmacodynamic response;
- clinical outcome.

Do not collapse these levels.

---

# Behavioral Mechanism

Possible pathways include:

- motivation;
- self-efficacy;
- habit;
- social reinforcement;
- opportunity;
- perceived norms.

Mechanism claims require evidence beyond correlation.

---

# Educational Mechanism

Possible mechanisms include:

- cognitive load;
- scaffolding;
- feedback;
- engagement;
- social interaction;
- metacognition;
- practice;
- transfer.

---

# Organizational Mechanism

Possible mechanisms include:

- learning culture;
- leadership;
- autonomy;
- psychological safety;
- resource access;
- coordination;
- incentives.

---

# Engineering Mechanism

Possible explanations include:

- material property;
- thermal behavior;
- mechanical stress;
- transport process;
- degradation;
- optimization constraint.

---

# Qualitative Mechanism

Qualitative evidence may illuminate how or why a process occurs.

Do not automatically convert participant explanations into causal proof.

---

# Mixed-Method Mechanism

Mixed-method convergence may strengthen explanatory plausibility when strands independently support linked parts of the mechanism.

---

# Alternative Explanation Requirement

For every major finding, identify at least one plausible competing explanation when scientifically relevant.

Examples:

- confounding;
- selection;
- measurement error;
- reverse causation;
- implementation variation;
- regression to the mean;
- chance;
- contextual heterogeneity.

---

# Competing Explanation Matrix

| Finding | Preferred Explanation | Competing Explanation | Evidence For | Evidence Against |
|---|---|---|---|---|

---

# Parsimony

Prefer the explanation requiring the fewest unsupported assumptions.

But do not oversimplify complex phenomena.

---

# Causal Guard

Discussion language must remain consistent with study design.

Cross-sectional study:

- association;
- relationship;
- pattern.

Randomized experiment:

- treatment effect, when assumptions hold.

Observational longitudinal study:

- temporal association;
- causal inference only with explicit causal design and assumptions.

---

# Causal Escalation Guard

Do not move:

```text
association
→ explanation
→ mechanism
→ effect
→ recommendation
```

without sufficient evidence at each step.

---

# Reverse Causation

For observational findings, ask whether Y could influence X.

Discuss when plausible.

---

# Residual Confounding

Even adjusted models may retain confounding.

Identify likely unmeasured factors.

---

# Collider Bias

If adjustment may condition on a collider, causal interpretation may be distorted.

---

# Overadjustment

Adjustment for mediators may attenuate total effects.

Interpret accordingly.

---

# Measurement Explanation

Differences across studies may reflect:

- different instruments;
- different thresholds;
- different outcome definitions;
- different reference periods;
- cultural adaptation;
- differential measurement error.

---

# Temporal Explanation

Timing can explain divergence.

Consider:

- baseline;
- acute effect;
- short-term;
- medium-term;
- long-term.

---

# Population Explanation

Differences may arise from:

- age;
- sex;
- disease severity;
- socioeconomic profile;
- ancestry;
- baseline risk;
- prior treatment;
- institutional setting.

---

# Contextual Explanation

Context may include:

- healthcare system;
- educational system;
- culture;
- policy;
- economic conditions;
- resource availability;
- technology access.

---

# Context Is Not Automatic Novelty

A new geographic location alone is not necessarily novel.

Explain why context changes the scientific inference.

---

# Boundary Condition

A boundary condition specifies when a finding is expected to hold or fail.

Examples:

- high baseline risk;
- certain dose range;
- high implementation fidelity;
- specific institutional context;
- particular age group.

---

# Boundary Condition Template

> The observed relationship appears strongest under [condition], suggesting that [condition] may define a boundary within which the proposed mechanism is most applicable.

---

# Null Finding Discussion

Do not treat a null result as failure.

Assess:

- precision;
- effect magnitude;
- power;
- intervention strength;
- measurement;
- adherence;
- ceiling/floor effects;
- context;
- theory.

---

# Precise Null-Like Finding

If uncertainty excludes meaningful effects, a null-like result can provide strong evidence against large effects.

---

# Imprecise Null

If the interval includes meaningful benefit and harm, call the result inconclusive.

---

# Unexpected Finding

Unexpected findings require:

- verification;
- robustness check;
- scientific explanation;
- exploratory label if post hoc.

---

# Unexpected Finding Guard

Do not build an elaborate theory around one unstable unexpected result.

---

# Negative Result Contribution

Negative findings may:

- narrow theory;
- reject an assumption;
- reveal boundary conditions;
- prevent ineffective intervention;
- reduce publication bias.

---

# Mixed Findings

When results differ across outcomes, do not force one summary.

Discuss whether outcomes capture different dimensions.

---

# Outcome Hierarchy

Keep primary outcomes central.

Do not shift emphasis to secondary outcomes because they are more favorable.

---

# Mediation Discussion

A significant indirect effect does not automatically establish a causal mechanism.

Discuss:

- temporal order;
- confounding;
- measurement;
- alternative mediators.

---

# Moderation Discussion

Moderation may reveal:

- subgroup heterogeneity;
- context dependency;
- boundary conditions.

Avoid overinterpretation when interaction estimates are imprecise.

---

# SEM Discussion

For SEM, distinguish:

- measurement findings;
- structural paths;
- indirect effects;
- model fit;
- alternative models.

Do not claim the model is true because fit indices are acceptable.

---

# PLS-SEM Discussion

Interpret:

- measurement quality;
- discriminant validity;
- path magnitude;
- R²;
- f²;
- Q²;
- predictive performance.

Do not turn significant paths into causal claims automatically.

---

# Predictive Model Discussion

Discuss:

- discrimination;
- calibration;
- external validation;
- overfitting;
- decision utility.

Do not interpret prediction as causal explanation.

---

# Diagnostic Study Discussion

Discuss:

- sensitivity;
- specificity;
- predictive values;
- likelihood ratios;
- threshold;
- prevalence;
- clinical context.

---

# Pharmacokinetic Discussion

Interpret parameters in relation to:

- dose;
- formulation;
- sampling;
- physiology;
- age;
- renal function;
- hepatic function;
- drug interactions.

---

# Pharmacogenetic Discussion

Discuss:

- genotype effect;
- allele frequency;
- ancestry;
- phenotype definition;
- drug exposure;
- treatment response;
- toxicity;
- replication;
- multiple testing.

Avoid overclaiming clinical implementation from one association study.

---

# Genetic Model Discussion

Explain why codominant, dominant, recessive, overdominant, or additive models may differ.

Do not privilege whichever model becomes significant.

---

# Formulation Study Discussion

Interpret:

- pH;
- viscosity;
- spreadability;
- adhesiveness;
- stability;
- release;
- antimicrobial activity;

as interconnected formulation properties.

Do not infer clinical efficacy without clinical evidence.

---

# Antimicrobial Discussion

Consider:

- diffusion limitations;
- solvent effects;
- concentration;
- viscosity;
- inoculum;
- assay type;
- MIC/MBC;
- organism biology.

Do not compare zone diameters across incompatible methods as direct potency measures.

---

# Qualitative Discussion

A qualitative discussion should connect themes to:

- context;
- prior studies;
- theory;
- mechanisms;
- variation;
- negative cases.

Do not reduce discussion to counting codes.

---

# Theme-to-Literature Mapping

For each major theme:

```yaml
theme_discussion:
  theme:
  meaning:
  closest_prior_evidence:
  convergence:
  divergence:
  mechanism:
  negative_cases:
  context:
  contribution:
```

---

# Mixed-Method Discussion

Use meta-inference.

Discuss:

- convergence;
- complementarity;
- expansion;
- discordance;
- silence.

---

# Discordance in Mixed Methods

Discordance can be scientifically productive.

It may reveal:

- different levels of analysis;
- measurement mismatch;
- perception-behavior gap;
- time-scale difference;
- hidden subgroup.

---

# Meta-Analysis Discussion

Discuss:

- pooled estimate;
- heterogeneity;
- prediction interval;
- risk of bias;
- small-study effects;
- generalizability.

Do not discuss only the pooled p-value.

---

# Heterogeneity as Scientific Information

Heterogeneity may reveal:

- treatment-response variability;
- context dependency;
- population differences;
- design differences.

---

# Prediction Interval

A prediction interval helps discuss likely variation in future comparable settings.

---

# Publication Bias Guard

Do not interpret funnel asymmetry as definitive proof of publication bias.

---

# Narrative Synthesis Discussion

When pooling is inappropriate, discuss:

- direction consistency;
- magnitude range;
- methodological differences;
- evidence quality;
- explanatory patterns.

---

# Closest Competitor Comparison

The most important comparison is often with the study closest to the present design and question.

Use:

```yaml
closest_competitor:
  study:
  similarity:
  key_difference:
  present_result:
  competitor_result:
  explanatory_difference:
  contribution:
```

---

# Novelty Integration

Novelty comes from the audited contribution, not from significance.

Discussion should clarify:

- what is new;
- what is not new;
- what is extended;
- what remains unresolved.

---

# What Is Novel

Possible meaningful novelty:

- mechanism;
- theory refinement;
- validated context boundary;
- improved method;
- stronger design;
- external validation;
- temporal evidence;
- integrated explanation;
- new clinically meaningful endpoint.

---

# What Is Not Novel

Do not present as novelty merely:

- new city;
- new university;
- another sample;
- another software package;
- same variables rearranged;
- extra mediator without rationale;
- significant p-value.

---

# Contribution Statement

Prefer:

> The contribution of this study lies not simply in observing [finding], which has been reported previously, but in showing that [new scientific contribution].

---

# Scientific Contribution Types

Classify:

- `THEORETICAL`
- `MECHANISTIC`
- `EMPIRICAL`
- `METHODOLOGICAL`
- `MEASUREMENT`
- `PREDICTIVE`
- `VALIDATION`
- `CONTEXTUAL_WITH_BOUNDARY_VALUE`
- `INTEGRATIVE`

---

# Contribution Strength

Use:

- `STRONG`
- `MODERATE`
- `LIMITED`
- `EXPLORATORY`

---

# Limitation Integration

Limitations belong inside the scientific interpretation, not only in a final disclaimer paragraph.

---

# Limitation Categories

Possible:

- design;
- sampling;
- measurement;
- confounding;
- missing data;
- multiplicity;
- model specification;
- implementation;
- generalizability;
- temporal scope;
- publication bias.

---

# Limitation Consequence

For each limitation state what it changes.

Example:

> The cross-sectional design limits causal interpretation.

Better than:

> This study has a cross-sectional design.

---

# Limitation Matrix

| Limitation | Affected Claim | Likely Direction | Severity | Mitigation |
|---|---|---|---|---|

---

# Limitation Severity

Classify:

- `MINOR`
- `MODERATE`
- `MAJOR`
- `CRITICAL`

---

# Limitation Does Not Mean Invalid

Avoid ritual self-criticism.

A limitation matters only through its effect on inference.

---

# Strengths

Discussion may identify strengths such as:

- strong design;
- validated measurement;
- representative sampling;
- longitudinal data;
- multimethod triangulation;
- robust sensitivity analyses;
- external validation.

Do not use strengths to cancel limitations.

---

# Generalizability

Discuss:

- target population;
- study population;
- settings;
- time;
- cultural context;
- health system;
- implementation conditions.

---

# Transferability

For qualitative research, discuss contextual transferability rather than statistical generalization when appropriate.

---

# Transportability

For causal or predictive studies, ask whether the result transports to other populations.

---

# Real-World Phenomenon Evidence

Official statistics and authoritative data may contextualize why findings matter.

They should not replace scholarly evidence for scientific mechanisms or research gaps.

---

# Authority-First Context

For phenomenon evidence prioritize:

- official statistics;
- government datasets;
- international organizations;
- registries;
- institutional data;
- regulations;
- policy reports.

---

# Policy Context Guard

Policy documents support policy context, not causal scientific mechanisms.

---

# Target Journal Context

Target-journal literature may help identify the relevant scholarly conversation.

Do not cite target-journal articles merely for strategic padding.

---

# APC Independence

APC status must not influence scientific evidence selection.

---

# Discussion Paragraph Architecture

A strong paragraph often follows:

```text
Finding
   ↓
Interpretation
   ↓
Comparison with Prior Evidence
   ↓
Explanation
   ↓
Boundary / Limitation
   ↓
Contribution
```

Not every paragraph needs every element.

---

# Paragraph Template

> [Finding]. This suggests [scientific meaning]. The result is [consistent/partially consistent/in contrast] with [closest evidence], which reported [relevant result]. The difference may reflect [specific mechanism/context/design explanation]. However, [limitation or alternative explanation] remains plausible. Together, these findings indicate [bounded contribution].

---

# Discussion Flow

Recommended macro-structure:

```text
1. Main finding
2. Comparison with closest evidence
3. Mechanism / theory
4. Divergence / contradiction
5. Secondary findings
6. Unexpected findings
7. Robustness
8. Contribution
9. Limitations
10. Implication handoff
```

---

# Literature-Summary Guard

Do not write discussion as:

```text
Study A found...
Study B found...
Study C found...
Study D found...
```

without synthesis.

---

# Citation Density

More citations do not automatically create stronger discussion.

Use enough evidence to establish the scientific position.

---

# Citation Clustering

A cluster of citations should support the same claim.

Avoid mixing unrelated evidence.

---

# Direct Comparison

Prefer numerical or methodological comparison where possible.

Example:

> The present OR of 1.42 is smaller than the pooled estimate of 1.80 reported previously, possibly reflecting lower baseline risk.

---

# Qualitative Comparison

Compare:

- theme content;
- mechanism;
- context;
- negative cases;
- conceptual framing.

---

# Cross-Disciplinary Evidence

Use adjacent disciplines only when:

- terminology differs;
- mechanism crosses fields;
- direct literature is sparse.

Explain why the evidence is relevant.

---

# Temporal Recency

Prioritize current evidence for fast-moving topics.

But retain seminal theory when foundational.

---

# Preprint Guard

Preprints may inform emerging evidence but should be labeled as non-peer-reviewed.

---

# Retracted Literature

Retracted studies cannot support scientific conclusions.

---

# Unverified Literature

Unverified references cannot silently support claims.

---

# Contradiction Search

Before finalizing discussion, actively search for:

- negative studies;
- failed replications;
- opposing mechanisms;
- methodological critiques.

---

# Confirmation Bias Guard

Do not select only literature consistent with the result.

---

# Interpretation Symmetry

Apply the same evidentiary standard to favorable and unfavorable findings.

---

# Positive Result Guard

A positive result should not receive more causal confidence merely because it supports the hypothesis.

---

# Negative Result Guard

A null result should not be dismissed merely because it conflicts with expectations.

---

# Significance Asymmetry Guard

Do not discuss significant results deeply while ignoring non-significant primary results.

---

# Language Calibration

Strong evidence:

- demonstrates;
- supports;
- indicates.

Moderate evidence:

- suggests;
- is consistent with.

Weak/exploratory evidence:

- may indicate;
- raises the possibility;
- warrants investigation.

---

# Causal Language Calibration

Observational:

- associated with;
- related to.

Experimental:

- affected;
- increased;
- reduced;

when assumptions support causality.

---

# Mechanistic Language Calibration

Directly tested:

- supports a mechanism involving...

Indirect:

- is consistent with a mechanism involving...

Speculative:

- one possible explanation is...

---

# Theory Language Calibration

Avoid:

> Theory X was confirmed.

Prefer:

> The findings support the predicted relationship specified by Theory X under the present conditions.

---

# Limitation Language Calibration

Avoid:

> The study is weak because...

Prefer:

> This design limits inference about...

---

# Generalization Language Calibration

Avoid:

> These findings apply broadly.

Prefer:

> Generalization is most defensible to populations sharing [conditions].

---

# Discussion and Results Separation

Results answer:

> What was observed?

Discussion answers:

> What does it mean and why?

Do not merge them unintentionally.

---

# Discussion and Introduction Separation

Introduction establishes:

- problem;
- SoTA;
- gap;
- objective.

Discussion should not repeat the full introduction.

---

# Discussion and Implications Separation

Discussion establishes scientific meaning.

Implications translate that meaning into:

- practice;
- policy;
- theory;
- future research;
- implementation.

Route these to `implication-builder`.

---

# Future Research

Future research should follow from unresolved uncertainty, not generic statements.

---

# Future Research Sources

Use:

- unresolved mechanism;
- boundary condition;
- contradictory result;
- imprecision;
- measurement limitation;
- external validation need;
- replication need.

---

# Generic Future Research Guard

Avoid:

> Future studies should use larger samples.

unless sample size directly limits inference.

---

# Replication Recommendation

Specify what should be replicated:

- population;
- method;
- exposure;
- outcome;
- mechanism.

---

# Methodological Recommendation

Recommend design changes only when they address a demonstrated limitation.

---

# Theory Development Recommendation

Recommend theory refinement when results reveal:

- missing mediator;
- moderator;
- nonlinearity;
- boundary;
- temporal mismatch.

---

# Scientific Discussion Matrix

Recommended:

| Finding | Prior Evidence | Relationship | Explanation | Boundary | Contribution |
|---|---|---|---|---|---|

---

# Theory Matrix

| Finding | Theory Prediction | Status | Mechanistic Interpretation | Required Revision |
|---|---|---|---|---|

---

# Contradiction Matrix

| Present Finding | Contradictory Study | Key Difference | Plausible Explanation | Confidence |
|---|---|---|---|---|

---

# Contribution Matrix

| Finding | What Was Already Known | What This Study Adds | Strength |
|---|---|---|---|

---

# Limitation Matrix

| Limitation | Inference Affected | Direction of Concern | Severity |
|---|---|---|---|

---

# Discussion Passport

Recommended internal representation:

```yaml
scientific_discussion:
  status:
  main_findings:
  closest_prior_evidence:
  convergence:
  contradictions:
  theory_relationship:
  mechanism_status:
  competing_explanations:
  context:
  boundary_conditions:
  strengths:
  limitations:
  generalizability:
  contribution_type:
  contribution_strength:
  what_is_novel:
  what_is_not_novel:
  unresolved_questions:
  implication_handoff:
```

Unknown fields remain unknown.

---

# Discussion Workflow

Use:

```text
1. Import interpreted findings
2. Rank findings by scientific importance
3. Identify closest prior evidence
4. Verify sources
5. Classify convergence/divergence
6. Evaluate theory relationship
7. Evaluate mechanism
8. Generate competing explanations
9. Identify context and boundaries
10. Position contribution
11. Integrate limitations
12. Identify unresolved questions
13. Calibrate claim language
14. Hand off implications
```

---

# Minimal Output

For a simple request provide:

## Main Finding
[...]

## Relation to Prior Evidence
[...]

## Scientific Explanation
[...]

## Theory / Mechanism
[...]

## Contradictions
[...]

## Contribution
[...]

## Limitations
[...]

## Unresolved Question
[...]

---

# Comprehensive Output

When full discussion is requested:

## A. Main Finding
[...]

## B. Closest Prior Evidence
[...]

## C. Convergence / Divergence
[...]

## D. Effect or Pattern Magnitude
[...]

## E. Theory Relationship
[...]

## F. Mechanism
[...]

## G. Competing Explanations
[...]

## H. Context
[...]

## I. Boundary Conditions
[...]

## J. Secondary Findings
[...]

## K. Unexpected Findings
[...]

## L. Contradictions
[...]

## M. Robustness
[...]

## N. Strengths
[...]

## O. Limitations
[...]

## P. Generalizability / Transferability
[...]

## Q. Scientific Contribution
[...]

## R. What Is Novel
[...]

## S. What Is Not Novel
[...]

## T. Unresolved Questions
[...]

## U. Implication Handoff
[...]

---

# Discussion Handoff to Implication Builder

Pass:

```yaml
implication_handoff:
  supported_scientific_claims:
  contribution:
  theory_implications:
  mechanism_implications:
  practical_relevance:
  policy_relevance:
  clinical_relevance:
  methodological_relevance:
  boundary_conditions:
  limitations:
  unresolved_questions:
  confidence:
```

---

# Relationship with Result Interpreter

`result-interpreter` determines what the study's results support.

`scientific-discussion` explains those supported findings relative to the wider evidence base.

Use:

```text
result-interpreter
      ↓
scientific-discussion
```

Do not reopen unsupported claims that were rejected upstream.

---

# Relationship with Evidence Synthesis

`evidence-synthesis` provides organized verified evidence.

`scientific-discussion` uses it to explain convergence, divergence, and mechanisms.

---

# Relationship with SoTA Builder

`sota-builder` establishes the current scientific position.

`scientific-discussion` positions the present findings within that position.

---

# Relationship with Gap Validator

`gap-validator` established whether the research problem was genuinely unresolved.

Discussion should show whether the present findings reduce that uncertainty.

---

# Relationship with Novelty Auditor

`novelty-auditor` established what the contribution could legitimately claim as new.

Discussion must preserve that boundary.

---

# Relationship with Theoretical Framework

Use theory to explain results only when scientifically justified.

Do not force theoretical framing when formal theory is not central.

---

# Relationship with Conceptual Framework

Use findings to evaluate:

- proposed relationships;
- boundaries;
- mediators;
- moderators;
- missing constructs.

---

# Relationship with Phenomenon Evidence Builder

Real-world data may explain why findings matter in context.

Do not use phenomenon evidence to prove scholarly novelty.

---

# Relationship with Implication Builder

`scientific-discussion` stops at scientific meaning.

`implication-builder` translates that meaning into consequences and recommendations.

---

# User-Friendly Behavior

Prefer:

> The main finding is consistent with previous studies, but the contribution is not simply replication. The present study shows that the relationship remains evident under a different measurement approach and after controlling for key confounders, which strengthens confidence in its robustness.

Or:

> The result differs from the dominant literature. Rather than treating this as an error, the difference appears scientifically informative because the present sample had substantially lower baseline severity and a shorter exposure period. These conditions may define a boundary within which the previously reported effect is attenuated.

Or:

> The significant indirect effect is compatible with the proposed mechanism, but it does not establish the mechanism causally because mediator and outcome were measured at the same time. The discussion should therefore describe the mechanism as plausible rather than proven.

Or:

> The qualitative and quantitative strands do not fully converge. Quantitative scores improved, while participants continued to describe implementation barriers. This discordance suggests that measured outcome improvement may coexist with unresolved process limitations.

---

# Avoid These Behaviors

Do not:

- repeat results without interpretation;
- summarize literature study by study;
- cite irrelevant papers;
- use citation volume as evidence strength;
- hide contradictory evidence;
- force agreement with prior studies;
- force theory support;
- retrofit theory after seeing preferred results without disclosure;
- turn association into causation;
- turn mediation into proven mechanism;
- treat statistical significance as novelty;
- treat geographic difference as novelty automatically;
- use target-journal citation padding;
- let APC status influence evidence selection;
- overgeneralize beyond the population;
- minimize important limitations;
- exaggerate strengths;
- present exploratory findings as confirmatory;
- generate generic future-research recommendations;
- make recommendations before implication analysis;
- claim practical effectiveness from laboratory performance alone;
- claim clinical utility from predictive discrimination alone;
- claim model truth from fit indices alone.

---

# Stop Conditions

Do not classify the discussion as ready when:

- result interpretation is incomplete;
- the main finding is unclear;
- closest prior evidence is unknown;
- citations are unverified;
- contradictory literature has not been considered;
- theory is being forced post hoc;
- causal language exceeds design;
- mechanism is speculative but presented as established;
- novelty exceeds the audited contribution;
- limitations are listed without inference consequences;
- generalization exceeds the sampled context;
- discussion is primarily a literature summary;
- unsupported claims rejected by `result-interpreter` have reappeared.

Use:

- `RETURN_TO_RESULT_INTERPRETER`
- `RETURN_TO_EVIDENCE_SYNTHESIS`
- `RETURN_TO_SOTA_BUILDER`
- `RETURN_TO_GAP_VALIDATOR`
- `RETURN_TO_NOVELTY_AUDITOR`
- `RETURN_TO_THEORETICAL_FRAMEWORK`
- `SCIENTIFIC_DISCUSSION_REQUIRES_REVISION`

when appropriate.

---

# Success Criterion

`scientific-discussion` succeeds when defensibly interpreted findings have been positioned against verified current scholarly evidence, the State of the Art, closest competitor studies, theory, mechanisms, competing explanations, contradictions, contextual and temporal differences, boundary conditions, strengths, limitations, and generalizability, and when the discussion clearly distinguishes what was already known from what the study genuinely adds, identifies what is novel and what is not novel, preserves uncertainty and causal boundaries, actively addresses credible contradictory evidence, calibrates explanatory language to evidence strength, and produces a scientifically coherent handoff to `implication-builder` without degenerating into result repetition, literature listing, citation padding, post-hoc theory fitting, significance-driven storytelling, unsupported mechanistic or causal claims, or exaggerated contribution.
