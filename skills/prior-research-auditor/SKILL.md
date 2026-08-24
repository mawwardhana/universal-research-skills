---

name: prior-research-auditor
description: Critically audit previous research articles, theses, dissertations, reports, proposals, or related research outputs to determine what was actually established, how strong the evidence is, what limitations and unresolved findings remain, and which elements require current literature revalidation before planning a continuation study.
---

# Prior Research Auditor

## Purpose

`prior-research-auditor` performs a structured scientific audit of previous research before that research is used as the foundation for a new study.

The purpose is not to summarize the document.

The purpose is to distinguish:

* what the previous study actually demonstrated;
* what the authors interpreted;
* what remained uncertain;
* which conclusions were stronger than the evidence;
* what methodological weaknesses constrained interpretation;
* what negative or unexpected findings deserve further attention;
* which historical limitations may generate continuation opportunities;
* which claims require validation against current literature.

This skill acts as a quality-control layer between:

`research-resume`

and later continuation workflows.

---

# Core Question

The central question is:

> What does this previous research genuinely establish, and what scientifically defensible opportunities remain after accounting for the strength and limitations of its evidence?

---

# Activation Conditions

Use this skill when:

* a previous article is uploaded;
* a thesis or dissertation is provided;
* a completed study will be used to design a follow-up study;
* a researcher wants to know what should come next;
* previous findings need critical examination;
* several prior studies must later be integrated into a research trajectory;
* limitations from an earlier study are being considered as possible research gaps.

Do not activate this skill merely to provide a simple summary unless the audit is relevant to the user's goal.

---

# Evidence Boundary

Audit the supplied research material first.

Do not silently supplement missing information using general knowledge.

When the source does not contain enough information, use:

`NOT_REPORTED`

or:

`INSUFFICIENT_INFORMATION`

When an interpretation is derived analytically rather than explicitly stated in the source, label it:

`ANALYTICAL_INFERENCE`

Current external literature should be evaluated in downstream literature workflows unless the user explicitly requests simultaneous external verification.

---

# Provenance Labels

Every important audit conclusion should conceptually distinguish among:

* `SOURCE_EXPLICIT`
* `SOURCE_INFERRED`
* `USER_PROVIDED`
* `ANALYTICAL_INFERENCE`
* `EXTERNAL_EVIDENCE`

Do not blur these categories.

---

# Audit Architecture

Audit previous research through the following dimensions.

---

# 1. Study Identity Audit

Extract when available:

* title;
* authors;
* year;
* publication type;
* journal or venue;
* DOI;
* research field;
* study location;
* study period.

If publication metadata are incomplete, do not fabricate them.

Record bibliographic uncertainty explicitly.

---

# 2. Research Problem Audit

Identify the actual scientific problem.

Separate:

## Background

General information explaining the topic.

## Practical Problem

A real-world issue motivating the study.

## Scientific Problem

An unresolved scientific uncertainty.

## Claimed Research Gap

What the authors believed was missing from previous knowledge.

These are not necessarily the same thing.

A strong audit should determine whether the study was driven primarily by:

* theoretical uncertainty;
* empirical inconsistency;
* methodological limitation;
* practical need;
* contextual absence;
* technological opportunity;
* translational problem.

Do not treat general importance statements as research gaps.

---

# 3. Objective–Question Alignment Audit

Determine:

* stated objective;
* stated research questions;
* stated hypotheses;
* implied questions when no explicit RQ exists.

Then assess whether they align.

Possible status:

* `FULLY_ALIGNED`
* `PARTIALLY_ALIGNED`
* `MISALIGNED`
* `NOT_ASSESSABLE`

Examples of misalignment:

* objective claims prediction but analysis is only descriptive;
* RQ asks causal effect but design is cross-sectional;
* hypothesis concerns mediation but mediator analysis was not performed;
* objective includes several outcomes but only some are analyzed.

Do not rewrite the objective merely to make the study appear coherent.

---

# 4. Theory and Concept Audit

Determine whether the study uses:

* explicit theory;
* conceptual model;
* empirical framework;
* disciplinary model;
* no identifiable theoretical framework.

Classify theoretical use as:

* `THEORY_TESTED`
* `THEORY_APPLIED`
* `THEORY_USED_AS_BACKGROUND`
* `THEORY_IMPLICIT`
* `NO_CLEAR_THEORY`

Identify whether findings:

* support the theoretical expectation;
* partially support it;
* contradict it;
* do not meaningfully test it.

A contradiction may represent a future research opportunity.

---

# 5. Study Design Audit

Identify the actual design rather than relying only on the author's label.

Evaluate:

* research paradigm where relevant;
* observational vs experimental;
* cross-sectional vs longitudinal;
* prospective vs retrospective;
* controlled vs uncontrolled;
* exploratory vs confirmatory;
* quantitative vs qualitative vs mixed-method;
* laboratory vs field;
* primary vs secondary data.

Then assess whether the design can answer the stated research question.

Possible status:

* `DESIGN_APPROPRIATE`
* `DESIGN_PARTIALLY_APPROPRIATE`
* `DESIGN_LIMITS_INFERENCE`
* `DESIGN_MISMATCH`

---

# 6. Causal Inference Audit

If the study uses causal language, determine whether the design supports it.

Check for issues such as:

* temporal ambiguity;
* lack of randomization;
* uncontrolled confounding;
* reverse causality;
* selection bias;
* measurement bias.

Use conservative interpretation.

Examples:

Cross-sectional association:

do not convert into:

"X causes Y."

Observational longitudinal evidence may strengthen temporal reasoning but still does not automatically establish causality.

Record:

* `CAUSAL_LANGUAGE_SUPPORTED`
* `CAUSAL_LANGUAGE_PARTIALLY_SUPPORTED`
* `CAUSAL_LANGUAGE_OVERSTATED`
* `NOT_APPLICABLE`

---

# 7. Population and Sampling Audit

Extract:

* target population;
* accessible population;
* sample;
* sample size;
* sampling technique;
* inclusion criteria;
* exclusion criteria;
* recruitment method;
* attrition where applicable.

Assess:

## Representativeness

Can the sample reasonably represent the intended population?

## Selection Bias

Could recruitment systematically exclude important groups?

## Statistical Power

If the study reports a power calculation, evaluate it.

Do not invent power calculations when they were not conducted.

## Generalizability

Determine the population to which findings can reasonably apply.

Do not generalize beyond the evidence.

---

# 8. Measurement Audit

Examine:

* variable operationalization;
* instrument validity;
* instrument reliability;
* laboratory procedures;
* calibration;
* questionnaire scales;
* diagnostic definitions;
* observational coding;
* measurement timing.

Classify concerns such as:

* measurement validity;
* measurement reliability;
* common-method bias;
* self-report bias;
* recall bias;
* instrument adaptation issues;
* insufficient measurement detail.

If validation information is missing, report it as missing.

Do not assume an instrument is validated solely because it has been widely used.

---

# 9. Variable and Construct Audit

For quantitative studies, identify:

* independent variables;
* dependent variables;
* mediators;
* moderators;
* confounders;
* covariates;
* latent constructs;
* control variables.

Check whether:

* variables match the hypotheses;
* important confounders were omitted;
* operational definitions are defensible;
* conceptual and statistical roles are consistent.

For qualitative studies, identify:

* focal phenomenon;
* participant experience;
* analytic concepts;
* emergent themes.

For experimental studies, identify:

* intervention;
* comparator;
* dose/exposure;
* outcome;
* experimental conditions.

---

# 10. Analysis Audit

Identify the actual analytical methods.

Examples:

* descriptive statistics;
* t-test;
* ANOVA;
* non-parametric tests;
* regression;
* generalized linear models;
* SEM;
* PLS-SEM;
* survival analysis;
* multilevel models;
* longitudinal models;
* machine learning;
* thematic analysis;
* content analysis;
* grounded theory;
* meta-analysis.

Assess:

## Method–Question Alignment

Does the analysis answer the research question?

## Method–Data Alignment

Is the method appropriate for:

* scale of measurement;
* distribution;
* repeated measurements;
* nested data;
* sample size;
* number of predictors;
* outcome type?

## Assumption Reporting

Were relevant assumptions assessed?

## Multiple Testing

Was multiplicity addressed when necessary?

## Effect Size

Were magnitude and uncertainty reported, or only p-values?

## Model Diagnostics

Were appropriate diagnostics reported?

Do not replace the previous study's analysis with a preferred method during the audit.

Instead identify what could be improved in future research.

---

# 11. Statistical Interpretation Audit

When statistical results are available, distinguish:

* statistical significance;
* effect magnitude;
* uncertainty;
* practical significance.

Flag common problems such as:

* significant = important;
* non-significant = no effect;
* p-value interpreted as probability the hypothesis is true;
* correlation interpreted as causation;
* R² interpreted without context;
* confidence interval ignored;
* subgroup findings overinterpreted;
* interaction ignored despite moderation claim.

Do not reclassify results without data support.

---

# 12. Qualitative Rigor Audit

For qualitative studies, examine where reported:

* sampling rationale;
* saturation;
* reflexivity;
* triangulation;
* coding procedure;
* researcher position;
* audit trail;
* member checking;
* credibility;
* dependability;
* confirmability;
* transferability.

Do not impose quantitative validity criteria on qualitative research.

---

# 13. Mixed-Methods Integration Audit

For mixed-method research, assess whether:

* quantitative and qualitative components are both meaningful;
* sequencing is justified;
* integration actually occurs;
* meta-inferences are supported.

Classify:

* `STRONG_INTEGRATION`
* `PARTIAL_INTEGRATION`
* `PARALLEL_WITH_LIMITED_INTEGRATION`
* `NOT_ASSESSABLE`

---

# 14. Finding-Level Audit

Do not audit only the paper-level conclusion.

Audit important findings individually.

For each major finding, identify:

* result;
* evidence type;
* effect direction;
* effect magnitude where available;
* uncertainty;
* statistical support;
* theoretical relevance;
* robustness;
* limitation.

Recommended conceptual structure:

| Finding | Evidence | Strength | Limitation | Continuation Signal |
| ------- | -------- | -------- | ---------- | ------------------- |

---

# 15. Primary Finding Audit

Identify which findings directly answer the main research objective.

Assess:

* evidence strength;
* consistency with analysis;
* consistency with conclusion;
* generalizability.

Do not let secondary results dominate the interpretation.

---

# 16. Negative Finding Audit

Explicitly identify:

* non-significant relationships;
* unsupported hypotheses;
* failed interventions;
* absent effects;
* null comparisons.

Negative findings must not be discarded automatically.

Evaluate whether they may result from:

* truly absent effect;
* inadequate power;
* measurement limitations;
* restricted range;
* inappropriate model;
* contextual boundary conditions.

Do not decide among these explanations without evidence.

Record them as possible continuation signals.

---

# 17. Unexpected Finding Audit

Identify findings that contradict:

* original hypothesis;
* theory;
* previous literature;
* expected direction.

Unexpected findings are especially important for future research.

Classify possible significance as:

* `POTENTIAL_MECHANISM_SIGNAL`
* `POTENTIAL_BOUNDARY_CONDITION`
* `POTENTIAL_CONTEXT_EFFECT`
* `POTENTIAL_MEASUREMENT_ARTIFACT`
* `POTENTIAL_ANALYTICAL_ARTIFACT`
* `REQUIRES_REPLICATION`

Do not present these possibilities as established explanations.

---

# 18. Robustness Audit

Determine whether the previous study provides evidence of robustness through methods such as:

* sensitivity analysis;
* alternative model specifications;
* subgroup analyses;
* validation dataset;
* replication;
* triangulation;
* bootstrapping;
* robustness checks.

Classify:

* `ROBUSTNESS_STRONG`
* `ROBUSTNESS_MODERATE`
* `ROBUSTNESS_LIMITED`
* `ROBUSTNESS_NOT_REPORTED`

Weak robustness may create a validation opportunity.

---

# 19. Contribution Audit

Assess contribution separately.

## Theoretical Contribution

Did the study:

* test theory;
* refine theory;
* extend theory;
* challenge theory;
* combine theories;
* provide only empirical support?

## Methodological Contribution

Did it improve:

* design;
* measurement;
* analytic method;
* data source;
* experimental procedure?

## Empirical Contribution

Did it provide genuinely new evidence?

## Contextual Contribution

Was the context scientifically meaningful?

A different geographic location alone is generally insufficient to establish strong novelty.

## Practical Contribution

Does evidence support an actionable implication?

## Translational Contribution

Can findings move toward practice, policy, technology, clinical application, education, or industry?

Do not inflate contribution.

---

# 20. Limitation Audit

Separate limitations into two categories.

## Author-Stated Limitations

Limitations explicitly acknowledged in the source.

## Auditor-Detected Limitations

Limitations reasonably inferred from study design or reporting.

Always label auditor-detected limitations as:

`ANALYTICAL_INFERENCE`

Possible categories:

* theoretical;
* conceptual;
* design;
* sampling;
* measurement;
* analytical;
* temporal;
* contextual;
* reporting;
* reproducibility;
* implementation;
* external validity.

---

# 21. Limitation Severity

Classify where useful:

### Minor

Unlikely to change the major conclusion.

### Moderate

Requires caution and may affect interpretation.

### Major

Substantially restricts the conclusion or generalizability.

### Critical

Could invalidate a central conclusion.

Do not exaggerate severity merely to create research opportunities.

---

# 22. Research Gap Warning

A limitation is not automatically a research gap.

Use:

`POTENTIAL_GAP_SIGNAL`

rather than:

`CONFIRMED_RESEARCH_GAP`

until current literature has been searched.

The later route must include:

`gap-validator`

---

# 23. Future Research Recommendation Audit

Extract recommendations made by the authors.

For each recommendation determine:

* what problem it intended to solve;
* which limitation it addressed;
* whether it logically follows from the results;
* what type of continuation it suggests.

Classify:

* replication;
* external validation;
* mechanistic study;
* longitudinal study;
* experimental study;
* methodological improvement;
* new population;
* new context;
* mediation;
* moderation;
* predictive model;
* intervention;
* implementation;
* translation.

Status:

`HISTORICAL_FUTURE_DIRECTION`

Do not label:

`CURRENT_NOVEL_OPPORTUNITY`

until literature revalidation occurs.

---

# 24. Unexploited Opportunity Audit

Look beyond the author's own recommendation section.

Possible signals include:

* unexpected result;
* contradictory subgroup;
* weakly explored secondary outcome;
* unexplained mediator;
* inconsistent moderator;
* measurement problem;
* model instability;
* theoretically important null finding;
* unresolved causal direction;
* data structure not fully exploited;
* missing longitudinal dimension;
* absence of external validation.

These are:

`AUDITOR_IDENTIFIED_CONTINUATION_SIGNALS`

They are not yet validated research gaps.

---

# 25. Replication Need

Determine whether replication may be scientifically valuable.

Possible reasons:

* small sample;
* single site;
* unexpected finding;
* weak measurement;
* inconsistent literature;
* exploratory analysis;
* unusually large effect;
* unusual population;
* limited external validity.

Classify:

* `REPLICATION_HIGH_PRIORITY`
* `REPLICATION_POTENTIALLY_USEFUL`
* `REPLICATION_LOW_PRIORITY`
* `NOT_ASSESSABLE`

Replication is a valid scientific contribution when justified.

---

# 26. Validation Need

Determine whether the study requires:

* internal validation;
* external validation;
* cross-cultural validation;
* instrument validation;
* model validation;
* clinical validation;
* field validation;
* temporal validation.

A validation pathway may be more scientifically valuable than adding arbitrary new variables.

---

# 27. Mechanism Opportunity

If the previous study established an association but not mechanism, flag:

`MECHANISM_UNRESOLVED`

Potential future questions may involve:

* mediator;
* biological pathway;
* behavioral mechanism;
* organizational mechanism;
* educational process;
* causal chain.

Do not invent the mechanism.

Mechanisms require theoretical and empirical grounding.

---

# 28. Boundary-Condition Opportunity

If results may differ by:

* population;
* age;
* sex/gender where scientifically appropriate;
* geography;
* organizational context;
* intervention intensity;
* disease severity;
* technology adoption;
* environmental condition;
* time;

record:

`BOUNDARY_CONDITION_SIGNAL`

This may later justify moderator analysis or comparative research.

---

# 29. Temporal Opportunity

Cross-sectional research may leave questions about:

* directionality;
* development;
* stability;
* temporal sequence;
* long-term outcomes.

Record:

`TEMPORAL_GAP_SIGNAL`

This may later justify:

* longitudinal design;
* cohort study;
* repeated measures;
* panel data;
* time-series analysis.

---

# 30. Translational Opportunity

Determine whether evidence is mature enough to potentially progress from:

observation
→ validation
→ mechanism
→ intervention
→ implementation
→ translation

Do not recommend intervention prematurely if foundational evidence remains weak.

---

# 31. Research Maturity Assessment

Classify the previous research program approximately as:

* `DISCOVERY_STAGE`
* `CHARACTERIZATION_STAGE`
* `ASSOCIATION_STAGE`
* `MECHANISM_STAGE`
* `VALIDATION_STAGE`
* `PREDICTION_STAGE`
* `INTERVENTION_STAGE`
* `IMPLEMENTATION_STAGE`
* `TRANSLATION_STAGE`

This classification supports later roadmap development.

Do not force every discipline into a strictly linear progression.

---

# 32. Evidence Strength Classification

For important findings, use a conservative classification:

* `STRONG`
* `MODERATE`
* `LIMITED`
* `VERY_LIMITED`
* `NOT_ASSESSABLE`

Base strength on relevant factors such as:

* design;
* sample;
* measurement;
* analysis;
* uncertainty;
* robustness;
* consistency.

Do not reduce evidence quality to journal quartile.

---

# 33. Publication Venue Is Not Evidence Quality

Do not assume:

Q1 = strong evidence.

Do not assume:

Q4 = weak evidence.

Journal indexing and quartile may inform publication context, but scientific evidence must be evaluated from the study itself.

---

# 34. Current Literature Revalidation

After the audit, classify which elements require current literature verification.

Typical items:

* original research gap;
* novelty claim;
* theoretical positioning;
* contradictory findings;
* future-research recommendations;
* methodological alternatives;
* external validation status.

Set:

`CURRENT_LITERATURE_REVALIDATION_REQUIRED: YES`

for most research-continuation cases.

---

# 35. Scopus-First Revalidation

The downstream evidence refresh should prioritize:

1. active Scopus-indexed peer-reviewed journals;
2. systematic reviews and meta-analyses where appropriate;
3. recent high-quality primary studies;
4. important seminal literature;
5. forward citations;
6. competing or contradictory studies.

Other scholarly databases may support discovery and verification.

No source should be described as Scopus-indexed without verification.

---

# 36. No-APC Publication Awareness

Do not select a target journal during this audit unless explicitly requested.

However, preserve the framework preference:

When future journal matching occurs, prioritize scientifically appropriate active Scopus-indexed journals with no mandatory APC where comparable options exist.

Do not sacrifice scientific fit for publication cost.

---

# 37. Target-Journal Citation Integrity

If later evaluating target-journal literature:

use articles from that journal only when scientifically relevant.

Valid purposes include:

* supporting an established concept;
* comparing methods;
* extending a published model;
* challenging a finding;
* addressing an unresolved question.

Invalid purpose:

* increasing citation count to the target journal merely to influence acceptance.

---

# 38. Audit Output

When a detailed audit is requested, use a structure similar to:

## Prior Research Audit

### A. Study Identity

[...]

### B. Scientific Problem

[...]

### C. Objective and Research Questions

[...]

### D. Theoretical Position

[...]

### E. Research Design

[...]

### F. Population and Sampling

[...]

### G. Measurement

[...]

### H. Analysis

[...]

### I. Primary Findings

[...]

### J. Negative Findings

[...]

### K. Unexpected Findings

[...]

### L. Evidence Strength

[...]

### M. Contribution

[...]

### N. Author-Stated Limitations

[...]

### O. Auditor-Detected Limitations

[...]

### P. Historical Future Directions

[...]

### Q. Unexploited Research Signals

[...]

### R. Research Maturity

[...]

### S. Current Literature Revalidation Needed

[...]

### T. Recommended Next Workflow

[...]

---

# 39. Continuation Signal Table

When appropriate, generate:

| Signal                | Source                   | Scientific Meaning | Evidence Strength       | Needs Current Validation |
| --------------------- | ------------------------ | ------------------ | ----------------------- | ------------------------ |
| Finding or limitation | Source explicit/inferred | Why it matters     | Strong/Moderate/Limited | Yes/No                   |

Do not label a signal as novelty before validation.

---

# 40. Vulnerability Table

When useful:

| Issue              | Severity | Effect on Previous Conclusion | Future Research Implication       |
| ------------------ | -------- | ----------------------------- | --------------------------------- |
| Example limitation | Moderate | Limits external validity      | External validation may be useful |

Do not create vulnerabilities that the source does not support.

---

# 41. Research Passport Update

When a Research Passport exists, update relevant fields such as:

```yaml
prior_research_audit:
  study:
  objective_alignment:
  theory_status:
  design_status:
  sampling_status:
  measurement_status:
  analysis_status:
  causal_inference_status:
  primary_findings:
  negative_findings:
  unexpected_findings:
  evidence_strength:
  limitations:
  continuation_signals:
  research_maturity:
  current_revalidation_required:
  provenance:
```

Unknown fields must remain unknown.

---

# 42. Multiple Previous Research Outputs

If multiple related outputs are available:

audit each sufficiently to establish:

* scientific contribution;
* methodological progression;
* findings;
* unresolved signals.

Then route to:

`research-trajectory-mapper`

Do not repeatedly generate isolated summaries.

---

# 43. Relationship with Research Resume

`research-resume` answers:

> Where is this research program currently positioned?

`prior-research-auditor` answers:

> How strong and complete is the scientific foundation provided by the previous study?

Do not duplicate the full routing logic from `research-resume`.

---

# 44. Relationship with Research Trajectory Mapper

`prior-research-auditor` analyzes individual studies.

`research-trajectory-mapper` later integrates multiple studies across time to determine:

* recurring research themes;
* progression;
* stagnation;
* diversification;
* research niche;
* future program coherence.

---

# 45. Relationship with Gap Validator

This skill may identify:

`POTENTIAL_GAP_SIGNAL`

Only `gap-validator` may later determine whether the gap remains defensible after current literature search.

---

# 46. Relationship with Novelty Auditor

Do not make final novelty claims here.

Novelty is downstream of:

current literature
→ State of the Art
→ gap validation
→ novelty builder
→ novelty auditor

---

# 47. User-Friendly Reporting

Do not overwhelm the user with every audit dimension when only a focused question is asked.

Adapt depth.

For example:

If the user asks:

"What should I study after this article?"

Provide the most decision-relevant audit findings first.

Then explain that the candidate directions must be checked against current literature before one is considered genuinely novel.

---

# 48. Critical Integrity Rule

Never create an attractive continuation study by distorting what the previous study found.

Especially do not:

* turn non-significant results into significant effects;
* describe exploratory findings as confirmatory;
* conceal contradictory findings;
* invent missing limitations;
* overstate causal evidence;
* present author speculation as empirical finding.

---

# Stop Conditions

Pause downstream continuation recommendations when:

* the prior research cannot be reliably reconstructed;
* critical methodological information is missing;
* the main result is internally inconsistent;
* the source material is incomplete enough to change interpretation;
* a proposed continuation depends on a historical gap that has not been revalidated.

State what needs to be resolved.

---

# Success Criterion

`prior-research-auditor` succeeds when previous research has been critically evaluated well enough to distinguish established evidence from uncertainty, identify scientifically meaningful continuation signals, and prepare those signals for current literature revalidation without prematurely declaring research gaps or novelty.
