---

name: continuation-opportunity-finder
description: Generate, compare, and prioritize scientifically defensible continuation-study opportunities from previous research, validated unresolved questions, current literature, research trajectory, researcher capabilities, feasibility constraints, and long-term program goals. Use when a researcher wants to determine the strongest next study after previous research or compare several possible continuation pathways.
---

# Continuation Opportunity Finder

## Purpose

`continuation-opportunity-finder` identifies and prioritizes possible next studies after previous research has been reconstructed, critically audited, and positioned against current evidence.

Its role is not merely to generate research ideas.

Its role is to answer:

> Given what has already been established, what remains unresolved, how the field has evolved, and what the researcher can realistically execute, which continuation studies represent the strongest scientific progression?

The preferred continuation should balance:

* scientific importance;
* evidence-supported gap;
* novelty potential;
* methodological progression;
* feasibility;
* research-program coherence;
* potential impact;
* publication relevance.

---

# Core Principle

Use:

> Continue because the science requires it, not merely because another variable, population, or location can be added.

A good continuation study should advance knowledge rather than mechanically repeat the previous study.

---

# Activation Conditions

Use this skill when:

* a previous study has been audited;
* a research trajectory has been mapped;
* unresolved questions have been identified;
* current literature has been reviewed;
* several possible next studies exist;
* the researcher asks what to study next;
* a research roadmap is being developed;
* a research program needs prioritization;
* a grant or publication strategy requires selecting the next study.

Typical requests include:

* "Which study should I conduct next?"
* "What is the strongest continuation of my previous article?"
* "I have several possible research directions. Which is best?"
* "Which continuation has the strongest novelty?"
* "What should become study 2 or study 3 in my roadmap?"
* "How should I continue my dissertation research?"

---

# Required Upstream Evidence

Prefer inputs from:

`research-resume`
→ `prior-research-auditor`
→ `research-trajectory-mapper`

and, when current evidence is required:

`citation-chaining`
→ `scopus-literature-search`
→ `source-verification`
→ `research-landscape`
→ `sota-builder`
→ `gap-discovery`
→ `gap-validator`

A continuation study should not be finalized solely from the limitation section of a previous paper.

---

# Critical Gap Rule

Candidate continuation opportunities may be generated from historical signals before literature validation.

However, they must be labeled:

`PROVISIONAL_CONTINUATION_OPPORTUNITY`

until the relevant gap has been validated.

Only after adequate evidence may a candidate become:

`VALIDATED_CONTINUATION_OPPORTUNITY`

Do not confuse:

potential opportunity

with:

validated research gap.

---

# Provenance

Maintain distinction among:

* `SOURCE_EXPLICIT`
* `SOURCE_INFERRED`
* `USER_PROVIDED`
* `EXTERNAL_EVIDENCE`
* `ANALYTICAL_INFERENCE`

Every major continuation rationale should be traceable to one or more of these sources.

---

# 1. Gather Continuation Signals

Collect continuation signals identified upstream.

Possible signals include:

* unresolved mechanism;
* inconsistent findings;
* null result;
* unexpected finding;
* limited external validity;
* cross-sectional limitation;
* weak measurement;
* lack of longitudinal evidence;
* lack of causal testing;
* lack of replication;
* incomplete theory testing;
* unvalidated model;
* unexplored subgroup;
* missing implementation evidence;
* translational opportunity;
* methodological weakness;
* new technology;
* emerging evidence;
* contradictory literature.

Do not convert every limitation into a candidate study automatically.

---

# 2. Remove Obsolete Opportunities

Current literature may show that a historical opportunity has already been addressed.

Classify historical signals as:

* `STILL_OPEN`
* `PARTIALLY_ADDRESSED`
* `SUBSTANTIALLY_RESOLVED`
* `REFRAMED`
* `SUPERSEDED`
* `NEW_GAP_EMERGED`
* `UNVERIFIED`

Do not recommend opportunities classified as:

`SUBSTANTIALLY_RESOLVED`

unless the new study has a different defensible contribution such as:

* independent replication;
* external validation;
* stronger methodology;
* contradictory evidence resolution.

---

# 3. Continuation Opportunity Taxonomy

Generate candidates using scientifically meaningful pathways.

## A. Direct Replication

Purpose:

Determine whether an important finding reproduces under similar conditions.

Appropriate when:

* original evidence is limited;
* sample is small;
* finding is unexpected;
* literature is inconsistent;
* replication evidence is absent.

Do not dismiss replication as unoriginal when it is scientifically necessary.

---

## B. Conceptual Replication

Test the same theoretical relationship using:

* different operationalization;
* different population;
* different context;
* different measurement;
* different method.

The scientific logic must remain clear.

---

## C. External Validation

Validate:

* model;
* instrument;
* prediction;
* finding;
* intervention;

in a genuinely independent dataset or population.

Often stronger than simply adding more predictors.

---

## D. Mechanism Study

Investigate:

> Why does the observed relationship occur?

Possible mechanisms include:

* biological pathway;
* psychological process;
* social mechanism;
* educational process;
* organizational process;
* behavioral mechanism.

Mechanisms must be theoretically grounded.

---

## E. Mediation Study

Appropriate when there is evidence that an intermediate process may explain:

`X → Y`

through:

`X → M → Y`

Do not add mediators solely because statistical software allows it.

---

## F. Boundary-Condition or Moderation Study

Investigate:

> When, for whom, or under what conditions does an effect change?

Possible moderators include scientifically justified:

* demographic characteristics;
* disease severity;
* environmental conditions;
* organizational context;
* intervention intensity;
* technology conditions;
* developmental stages.

Moderators require theoretical justification.

---

## G. Longitudinal Study

Appropriate when previous evidence cannot establish:

* temporal order;
* stability;
* development;
* change;
* long-term effects.

Possible designs include:

* cohort;
* panel;
* repeated measures;
* prospective follow-up;
* time series.

---

## H. Experimental or Causal Study

Appropriate when observational evidence is sufficiently mature and causal testing is feasible.

Possible designs:

* randomized experiment;
* quasi-experiment;
* field experiment;
* natural experiment.

Do not recommend experimental escalation when foundational evidence is weak.

---

## I. Measurement Advancement

Continue the research by improving:

* scale;
* instrument;
* biomarker;
* laboratory method;
* coding scheme;
* measurement validity;
* measurement reliability.

Measurement improvement may provide stronger contribution than adding new variables.

---

## J. Methodological Advancement

Address limitations in:

* study design;
* sampling;
* data collection;
* statistical modeling;
* qualitative rigor;
* causal inference;
* validation.

Methodological novelty must serve the research problem.

---

## K. Analytical Advancement

Apply a more suitable analysis when previous analytical limitations prevented adequate inference.

Examples:

* multilevel modeling;
* longitudinal modeling;
* survival analysis;
* causal inference;
* structural equation modeling;
* predictive modeling;
* machine learning.

Do not recommend advanced analysis merely because it appears sophisticated.

---

## L. Predictive Study

Move from explanation toward prediction.

Possible aims:

* risk prediction;
* classification;
* prognostic modeling;
* forecasting;
* decision support.

Prediction requires:

* appropriate validation;
* calibration;
* discrimination;
* out-of-sample evaluation.

Do not confuse explanatory models with predictive models.

---

## M. Intervention Development

Translate prior findings into an intervention.

Possible sequence:

```text
Evidence
↓
Mechanism
↓
Intervention design
↓
Pilot
↓
Effectiveness testing
```

Do not skip foundational stages without justification.

---

## N. Implementation Study

Investigate whether an evidence-based intervention or model can function in real-world settings.

Questions may include:

* adoption;
* feasibility;
* fidelity;
* acceptability;
* sustainability;
* scalability.

---

## O. Translational Study

Move research toward:

* clinical practice;
* education;
* policy;
* technology;
* industry;
* community application.

Translation should be proportional to evidence maturity.

---

## P. Contextual Extension

Examine whether findings apply in a scientifically meaningful new context.

A new location alone is insufficient.

Contextual extension is stronger when the new context tests:

* theory boundary;
* external validity;
* institutional variation;
* cultural mechanism;
* environmental difference;
* implementation condition.

---

## Q. Integrative Study

Combine previously separate but scientifically connected research streams.

Potential forms:

* interdisciplinary framework;
* multi-level model;
* biological + behavioral data;
* quantitative + qualitative integration;
* clinical + genomic evidence;
* education + technology;
* environmental + economic evidence.

Integration must solve a scientific problem rather than merely increase complexity.

---

# 4. Candidate Generation

Generate a focused number of candidates.

Default:

3–7 strong candidates.

Do not overwhelm the researcher with dozens of loosely justified ideas.

Each candidate should answer:

1. What would be studied?
2. Why is it needed?
3. Which unresolved issue does it address?
4. How does it progress beyond prior research?
5. What evidence supports pursuing it?
6. What research design may be suitable?
7. What major feasibility challenge exists?
8. What scientific contribution could result?

---

# 5. Candidate Naming

Use a scientific description before producing polished titles.

Prefer:

> External validation of the existing prediction model in an independent population.

before:

> "Development of an Innovative..."

Avoid marketing language.

A publication title can be developed later.

---

# 6. Scientific Importance

Assess whether the candidate addresses a meaningful problem.

Possible rating:

* `HIGH`
* `MODERATE`
* `LOW`
* `NOT_ASSESSABLE`

Consider:

* consequence of unresolved knowledge;
* theoretical importance;
* clinical relevance;
* educational relevance;
* technological relevance;
* policy relevance;
* societal importance.

Importance should not be inferred solely from publication volume.

---

# 7. Gap Strength

Assess the underlying research gap.

Possible status:

* `VALIDATED_STRONG`
* `VALIDATED_MODERATE`
* `PARTIALLY_VALIDATED`
* `PROVISIONAL`
* `WEAK`
* `UNVERIFIED`

Only `gap-validator` should establish final gap status.

---

# 8. Novelty Potential

Estimate novelty potential without making a final novelty claim.

Possible forms:

* theoretical;
* conceptual;
* methodological;
* analytical;
* empirical;
* contextual;
* technological;
* translational;
* integrative.

Use:

* `HIGH_POTENTIAL`
* `MODERATE_POTENTIAL`
* `LOW_POTENTIAL`
* `REQUIRES_VALIDATION`

Final novelty belongs downstream to:

`novelty-builder`
→ `novelty-auditor`

---

# 9. Scientific Progression

Determine whether the candidate genuinely advances the existing research trajectory.

Classify:

* `MAJOR_PROGRESSION`
* `CLEAR_PROGRESSION`
* `INCREMENTAL_PROGRESSION`
* `REPETITIVE`
* `DISCONNECTED`

Strong candidates should usually avoid:

`REPETITIVE`

and:

`DISCONNECTED`

unless scientifically justified.

---

# 10. Theory Contribution Potential

Assess whether the candidate may:

* test theory;
* refine theory;
* extend theory;
* identify boundary conditions;
* integrate theories;
* challenge theory.

Do not require theoretical contribution in fields where methodological, empirical, or translational contribution is more appropriate.

---

# 11. Methodological Strength Potential

Determine whether the candidate improves on prior evidence through:

* stronger design;
* better sampling;
* longitudinal evidence;
* improved measurement;
* external validation;
* experimental control;
* multi-site data;
* causal inference;
* richer qualitative design.

Classify:

* `STRONG_IMPROVEMENT`
* `MODERATE_IMPROVEMENT`
* `MINOR_IMPROVEMENT`
* `NO_IMPROVEMENT`
* `UNKNOWN`

---

# 12. Feasibility Assessment

Evaluate candidate feasibility across relevant dimensions.

## Data Access

Can required data reasonably be obtained?

## Participant Access

Can the target population be recruited?

## Laboratory Capacity

Are required instruments, assays, or facilities available?

## Method Expertise

Does the team have or can it obtain necessary methodological expertise?

## Time

Can the study reasonably be completed within the required period?

## Funding

Are resources compatible with likely funding?

## Ethics

Are ethical or regulatory barriers manageable?

## Collaboration

Can missing expertise be acquired through collaboration?

Classify overall feasibility:

* `HIGH`
* `MODERATE`
* `LOW`
* `UNKNOWN`

Do not reject ambitious research solely because collaboration is needed.

---

# 13. Feasibility Is Not Scientific Priority

Avoid selecting:

the easiest study

when a slightly harder study offers substantially greater scientific progression.

Conversely, avoid selecting an extremely ambitious study that cannot realistically be completed.

Preferred candidates balance:

scientific value × feasibility.

---

# 14. Researcher Capability Fit

Use upstream capability mapping.

Consider:

* established expertise;
* methodological experience;
* laboratory infrastructure;
* clinical access;
* data access;
* collaborations;
* software capability;
* publication experience.

Classify:

* `CURRENTLY_READY`
* `READY_WITH_MINOR_SUPPORT`
* `REQUIRES_COLLABORATION`
* `REQUIRES_NEW_CAPABILITY`
* `CURRENTLY_LOW_FEASIBILITY`

This is not a judgment of researcher competence.

It is a planning variable.

---

# 15. Collaboration Opportunity

Identify collaboration when it could unlock a stronger research pathway.

Examples:

* biostatistics;
* molecular biology;
* clinical expertise;
* qualitative methodology;
* machine learning;
* economics;
* education science;
* engineering;
* implementation science.

Do not downgrade a candidate solely because interdisciplinary collaboration is needed.

---

# 16. Ethical Feasibility

Determine whether the continuation may require:

* new ethics approval;
* informed consent;
* secondary data approval;
* biospecimen permission;
* vulnerable-population safeguards;
* clinical trial registration;
* data protection.

Do not provide formal ethics clearance.

Identify requirements that may affect feasibility.

---

# 17. Data Requirement

For each candidate, specify conceptually:

* primary or secondary data;
* cross-sectional or longitudinal;
* experimental data;
* qualitative data;
* laboratory data;
* multimodal data;
* external validation data.

Do not design detailed data collection before the candidate is selected.

---

# 18. Methodological Direction

Provide only an initial methodological direction.

Examples:

* prospective cohort;
* controlled experiment;
* mixed-method evaluation;
* external validation study;
* longitudinal panel;
* qualitative mechanism study.

Detailed methodology belongs downstream to:

`methodology-architect`

---

# 19. Analysis Direction

Provide only the level necessary to compare candidates.

Detailed statistical selection belongs to:

`analysis-planner`
and
`statistical-method-selector`

Do not commit the project to software-specific methods prematurely.

---

# 20. Research Program Coherence

Assess whether the candidate strengthens the researcher's emerging niche or research program.

Classify:

* `VERY_HIGH`
* `HIGH`
* `MODERATE`
* `LOW`
* `DISCONNECTED`

A candidate may still be valuable if it intentionally opens a new research line.

Label that explicitly.

---

# 21. Roadmap Value

Determine whether the candidate creates future studies.

A high-roadmap-value study may:

* generate a validated model;
* establish a cohort;
* produce an instrument;
* create a biobank;
* establish a dataset;
* demonstrate a mechanism;
* validate an intervention;
* create a platform for multicenter research.

Classify:

* `HIGH`
* `MODERATE`
* `LOW`

---

# 22. Grant Potential

When relevant, identify whether the candidate could support:

* pilot grant;
* early-career grant;
* national research grant;
* international collaboration;
* translational grant;
* implementation grant.

Do not imply funding eligibility without verification.

---

# 23. Publication Potential

Publication potential should be assessed carefully.

Consider:

* scientific importance;
* methodological rigor;
* international relevance;
* novelty potential;
* evidence maturity;
* clarity of contribution;
* journal-scope availability.

Use:

* `STRONG`
* `MODERATE`
* `LIMITED`
* `UNKNOWN`

Never guarantee:

* publication;
* Q1 acceptance;
* Scopus acceptance.

---

# 24. Scopus-First Publication Awareness

For candidates intended for international publication, later journal matching should prioritize:

* active Scopus-indexed journals;
* strong scope fit;
* relevant article history;
* credible editorial practices;
* appropriate quality level.

Do not claim Scopus status without current verification.

---

# 25. No-Mandatory-APC Preference

Where requested, preserve:

`prefer_no_mandatory_apc: true`

Later journal matching should prioritize:

1. scientific fit;
2. active Scopus status;
3. publication quality;
4. no mandatory APC when comparable alternatives exist.

Possible cost status:

* `NO_MANDATORY_APC`
* `OPTIONAL_APC_HYBRID`
* `MANDATORY_APC`
* `APC_UNVERIFIED`

Do not allow publication cost to override scientific fit.

---

# 26. Target-Journal Intelligence Awareness

If the researcher already has candidate journals, later analysis may examine their recent relevant publications.

Valid purposes:

* assess scope;
* understand current scholarly conversation;
* identify methodological fit;
* identify unresolved questions;
* position contribution.

Do not use target-journal citations as artificial citation padding.

---

# 27. Candidate Comparison Dimensions

Compare candidates using dimensions such as:

* scientific importance;
* validated gap strength;
* novelty potential;
* evidence support;
* methodological advancement;
* feasibility;
* researcher capability fit;
* collaboration requirement;
* ethical feasibility;
* research-program coherence;
* roadmap value;
* publication potential;
* translational potential.

Do not pretend these dimensions are perfectly objective.

Explain important trade-offs.

---

# 28. Priority Matrix

When useful, use:

| Candidate | Scientific Importance | Gap Strength | Novelty Potential | Method Advancement | Feasibility | Program Coherence | Roadmap Value |
| --------- | --------------------- | ------------ | ----------------- | ------------------ | ----------- | ----------------- | ------------- |

Use qualitative categories by default.

Numerical scoring may be used only when helpful and should not create false precision.

---

# 29. Optional Weighted Scoring

If the researcher wants explicit ranking, a configurable weighted score may be used.

Example default only:

* scientific importance: 20%
* gap strength: 20%
* novelty potential: 15%
* methodological progression: 15%
* feasibility: 15%
* research-program coherence: 10%
* roadmap value: 5%

These weights are not universal scientific truths.

Adapt them when the research context requires different priorities.

---

# 30. Candidate Status

Classify each candidate as one of:

* `PRIORITY_CANDIDATE`
* `STRONG_ALTERNATIVE`
* `CONDITIONAL_CANDIDATE`
* `NEEDS_MORE_EVIDENCE`
* `LOW_PRIORITY`
* `NOT_RECOMMENDED`

Provide rationale.

---

# 31. Recommended Next Study

Do not simply select the candidate with the highest apparent novelty.

The recommended study should have the strongest overall balance of:

* scientific need;
* validated gap;
* evidence support;
* methodological progression;
* feasibility;
* research trajectory;
* future value.

Explain why it is recommended.

---

# 32. Alternative Studies

Always preserve reasonable alternatives when uncertainty remains.

For example:

### Primary Option

Best overall scientific progression.

### Alternative A

Lower resource requirement.

### Alternative B

Higher innovation but higher risk.

### Alternative C

Best for external validation.

This helps researchers make informed choices.

---

# 33. Risk–Reward Classification

When useful:

## Low Risk / Moderate Reward

Examples:

* direct replication;
* external validation.

## Moderate Risk / High Reward

Examples:

* mechanism study;
* longitudinal design.

## High Risk / High Reward

Examples:

* new intervention;
* technological translation;
* novel predictive system.

Risk refers to research uncertainty and feasibility, not personal danger.

---

# 34. Decision Trade-Offs

Explicitly communicate important trade-offs.

Example:

> Candidate A has stronger novelty potential but requires longitudinal follow-up and larger funding. Candidate B is easier to execute and has strong external-validation value but offers a more incremental contribution.

Do not hide trade-offs behind a single score.

---

# 35. Research Question Preview

For the highest-priority candidates, a provisional question may be provided.

Label:

`PROVISIONAL_RESEARCH_QUESTION`

Final RQ development belongs to:

`research-question-builder`

---

# 36. Hypothesis Preview

Do not create hypotheses for every candidate.

When a candidate is confirmatory and theory supports hypotheses, provide only provisional directions.

Final hypotheses belong to:

`hypothesis-builder`

---

# 37. Novelty Preview

For each strong candidate, describe:

`POTENTIAL_NOVELTY`

Do not state:

"This is novel."

until:

`novelty-auditor`

has evaluated the claim.

---

# 38. Candidate Output Card

Recommended format:

## Candidate Study

**Scientific problem:**
[...]

**Continuation pathway:**
[Mechanism / Validation / Longitudinal / etc.]

**Why this study follows logically:**
[...]

**Current gap status:**
[...]

**Potential novelty:**
[...]

**Suggested design direction:**
[...]

**Major data requirement:**
[...]

**Feasibility:**
[...]

**Scientific contribution:**
[...]

**Research-program fit:**
[...]

**Roadmap value:**
[...]

**Major risk:**
[...]

**Evidence still needed:**
[...]

---

# 39. Full Decision Output

When the user asks for a comprehensive recommendation, provide:

## A. Research Position

Where the current research stands.

## B. Validated Unresolved Questions

What remains genuinely open.

## C. Candidate Continuation Studies

3–7 candidates.

## D. Comparative Priority Matrix

Side-by-side evaluation.

## E. Recommended Next Study

Primary recommendation.

## F. Alternative Studies

Reasonable alternatives.

## G. Why This Study Comes Next

Scientific progression logic.

## H. Provisional Research Question

If appropriate.

## I. Methodological Direction

High-level only.

## J. Evidence Required Before Finalization

Remaining validation.

## K. Research Program Implication

How it supports future research.

---

# 40. Research Roadmap Awareness

Do not produce a complete multi-year roadmap yet unless requested.

The selected candidate should later feed into:

`research-program-builder`
→ `research-roadmap`

Conceptually:

```text
Previous Studies
      ↓
Research Trajectory
      ↓
Current Evidence
      ↓
Validated Gaps
      ↓
Continuation Candidates
      ↓
Priority Next Study
      ↓
Future Research Program
      ↓
Research Roadmap
```

---

# 41. Relationship with Gap Validator

`gap-validator` determines whether a gap is defensible.

`continuation-opportunity-finder` determines which validated or provisional gaps produce worthwhile next studies.

Do not replace gap validation.

---

# 42. Relationship with Novelty Builder

This skill identifies:

`POTENTIAL_NOVELTY`

`novelty-builder` later constructs the precise novelty claim.

---

# 43. Relationship with Novelty Auditor

Final novelty confidence requires:

`novelty-auditor`

Do not claim final novelty here.

---

# 44. Relationship with Methodology Architect

This skill suggests high-level design direction.

`methodology-architect` later develops:

* design;
* population;
* sampling;
* variables;
* measurement;
* protocol;
* validity strategy.

---

# 45. Relationship with Research Program Builder

This skill selects promising next studies.

`research-program-builder` organizes several studies into a coherent future scientific program.

---

# 46. Relationship with Research Roadmap

`research-roadmap` assigns:

* sequencing;
* timeline;
* milestones;
* expected outputs;
* collaboration;
* funding opportunities;
* publication strategy.

Do not duplicate it here.

---

# 47. Research Passport Update

When supported, update:

```yaml
continuation_opportunities:
  validated_unresolved_questions:
  candidates:
    - candidate:
      continuation_type:
      scientific_importance:
      gap_status:
      novelty_potential:
      methodological_progression:
      feasibility:
      program_coherence:
      roadmap_value:
      publication_potential:
      status:
  recommended_candidate:
  alternative_candidates:
  remaining_evidence_needs:
  next_stage:
```

Unknown values remain unknown.

---

# 48. Avoid These Behaviors

Do not:

* turn every limitation into a new study;
* generate dozens of superficial titles;
* prioritize novelty over scientific importance;
* prioritize easy data access over science;
* add arbitrary mediators or moderators;
* recommend advanced statistics as novelty;
* treat a different location as sufficient novelty;
* repeat the same design without justification;
* ignore null or contradictory findings;
* select a study before checking current evidence;
* guarantee publication;
* use target-journal citation padding;
* recommend expensive publication merely because a journal has high prestige.

---

# 49. User-Friendly Behavior

Present decisions clearly.

Instead of:

> Candidate 2 has a composite weighted score of 83.4.

Prefer:

> The mechanism study is the strongest scientific continuation because your previous research established the association but did not explain how the effect occurs. It offers greater progression than simply repeating the same model in another location.

Use scores only when they clarify rather than obscure judgment.

---

# 50. Stop Conditions

Do not recommend a final next study when:

* previous research has not been sufficiently reconstructed;
* key findings are unclear;
* current literature has not been checked where required;
* the proposed gap remains unverified;
* feasibility depends on unknown critical resources;
* candidate ranking would require unsupported assumptions.

Instead state what evidence is still needed.

---

# Success Criterion

`continuation-opportunity-finder` succeeds when the researcher receives a small, evidence-grounded set of scientifically meaningful continuation options, understands their trade-offs, and can identify the strongest next study without confusing historical limitations, speculative ideas, or publication strategy with validated research opportunity.
