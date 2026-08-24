---

name: trend-detection
description: Detect and interpret temporal changes in a research field by evaluating publication growth, topic evolution, methodological shifts, theoretical changes, population focus, evidence maturity, and citation or adoption signals without equating simple publication volume with scientific importance. Use when a researcher wants to identify growing, declining, stable, shifting, or accelerating research directions before evaluating emerging topics, research gaps, or future opportunities.
---

# Trend Detection

## Purpose

`trend-detection` identifies meaningful temporal change within a research field.

Its central question is:

> What is genuinely changing in this field over time?

The purpose is not simply to count publications.

A research trend may involve:

* increasing scientific attention;
* changing research questions;
* methodological evolution;
* new theoretical approaches;
* new technologies;
* new populations;
* new evidence types;
* increasing validation;
* increasing implementation;
* decline of older approaches;
* convergence or fragmentation of research streams.

The skill should help distinguish:

`PUBLICATION_GROWTH`

from:

`SCIENTIFIC_TREND`

---

# Core Principle

Use:

> Trend is change in scientific activity or direction, not merely more papers.

Do not interpret publication volume alone as evidence that a topic is:

* important;
* novel;
* mature;
* impactful;
* worth researching.

Trend detection must consider context.

---

# Activation Conditions

Use this skill when the researcher asks:

* "What topics are trending?"
* "What is growing in this field?"
* "Which research approaches are becoming more common?"
* "What areas are declining?"
* "How has this field changed recently?"
* "What is the direction of current research?"
* "Which topics are gaining scientific attention?"
* "What research themes are accelerating?"

Prefer upstream input from:

`research-landscape`

because the landscape establishes the field structure before temporal change is evaluated.

---

# Evidence Requirement

Reliable trend detection normally requires bibliographic evidence across time.

Preferred evidence route:

`scopus-literature-search`
→ `source-verification`
→ `literature-screening`
→ `research-landscape`
→ `trend-detection`

If evidence coverage is incomplete, label output as:

`PRELIMINARY_TREND_ANALYSIS`

Do not present preliminary signals as established trends.

---

# Scopus-First Trend Policy

When literature data are required, prioritize:

1. relevant peer-reviewed articles from active Scopus-indexed journals;
2. recent literature with sufficient historical coverage;
3. systematic reviews and meta-analyses when appropriate;
4. major primary studies;
5. important methodological literature;
6. relevant seminal studies.

Other scholarly databases may support discovery and bibliographic metadata.

Never claim Scopus indexing without verification.

---

# 1. Define the Time Window

Trend interpretation requires an explicit or inferred time horizon.

Possible windows:

* last 3 years;
* last 5 years;
* last 10 years;
* full field history;
* pre/post major technological event;
* pre/post policy change;
* pre/post pandemic;
* custom period.

Choose a window appropriate to the field.

Fast-moving fields may require shorter windows.

Slow-moving fields may require longer windows.

Do not impose a five-year window universally.

---

# 2. Establish Historical Baseline

Before identifying change, determine what previously characterized the field.

Possible baseline characteristics:

* dominant themes;
* common methods;
* main theories;
* typical populations;
* dominant technologies;
* evidence maturity.

Without a baseline, "growth" lacks context.

---

# 3. Publication Volume Trend

When publication counts are available, classify:

* `RAPID_GROWTH`
* `STEADY_GROWTH`
* `STABLE`
* `DECLINING`
* `VOLATILE`
* `INSUFFICIENT_DATA`

Publication volume is only one trend dimension.

Do not stop the analysis here.

---

# 4. Normalize Growth When Possible

Absolute publication counts may be misleading because science overall grows over time.

When data permit, consider:

* share of publications within the parent field;
* growth relative to neighboring topics;
* growth relative to overall database expansion;
* annualized growth.

Do not create false precision when data are insufficient.

---

# 5. Theme Growth

Evaluate whether specific themes are:

* increasing;
* stable;
* declining;
* newly appearing;
* fragmenting;
* merging.

Possible status:

* `ACCELERATING_THEME`
* `GROWING_THEME`
* `STABLE_THEME`
* `DECLINING_THEME`
* `NEW_THEME_SIGNAL`
* `RESTRUCTURING_THEME`

Do not equate a few recent papers with an established growing theme.

---

# 6. Topic Share

When possible, examine whether a topic's share within the broader field is increasing.

This is often more informative than raw publication growth.

For example:

If the entire field grows 20% but Topic A grows 22%,

the topic may not be meaningfully accelerating.

If Topic B grows 150%,

that may represent stronger trend evidence.

Interpret cautiously.

---

# 7. Research Question Shift

Identify whether dominant questions are changing.

Possible progression:

```text
What is it?
      ↓
What is associated with it?
      ↓
Why does it happen?
      ↓
Can we predict it?
      ↓
Can we intervene?
      ↓
Can it be implemented?
```

A shift in question type may indicate scientific maturation.

---

# 8. Methodological Trend

Identify whether methods are changing.

Examples:

* cross-sectional → longitudinal;
* single-site → multicenter;
* regression → causal inference;
* conventional statistics → machine learning;
* descriptive qualitative → mixed methods;
* laboratory testing → real-world validation.

Possible status:

* `METHOD_ADOPTION_GROWING`
* `METHOD_STABLE`
* `METHOD_DECLINING`
* `METHOD_TRANSITION`
* `NEW_METHOD_SIGNAL`

Do not assume newer methods are superior.

---

# 9. Analytical Trend

Map changes in analysis when relevant.

Examples:

* mediation;
* moderation;
* multilevel modeling;
* SEM;
* PLS-SEM;
* survival models;
* predictive models;
* machine learning;
* network analysis;
* meta-analysis.

Interpret whether analytical change reflects:

* stronger scientific questions;
* technological availability;
* methodological fashion;
* genuine data complexity.

Do not confuse statistical fashion with scientific progress.

---

# 10. Theory Trend

Identify changes in theoretical structure.

Possible patterns:

* dominant theory remains stable;
* competing theory gains attention;
* theoretical integration increases;
* theory use declines;
* field becomes more atheoretical;
* theory refinement emerges.

Use:

* `THEORY_STABLE`
* `THEORY_EXPANDING`
* `THEORY_COMPETITION`
* `THEORY_INTEGRATION`
* `THEORETICAL_DECLINE`
* `INSUFFICIENT_EVIDENCE`

---

# 11. Population Trend

Determine whether research attention shifts toward:

* new age groups;
* clinical populations;
* geographic regions;
* professional groups;
* socioeconomic groups;
* species;
* ecosystems;
* institutions.

This may indicate:

* external validation;
* boundary-condition research;
* translational expansion.

Do not treat new population focus automatically as novelty.

---

# 12. Context Trend

Identify whether the field is moving into:

* clinical practice;
* schools;
* workplaces;
* industry;
* community settings;
* policy environments;
* low-resource settings;
* real-world implementation.

This may indicate research maturity.

---

# 13. Technology Trend

When technology is relevant, examine adoption of:

* AI;
* omics;
* digital health;
* sensors;
* automation;
* advanced materials;
* remote monitoring;
* learning analytics;
* simulation.

Distinguish:

`TECHNOLOGY_ADOPTION`

from:

`SCIENTIFIC_ADVANCEMENT`

Technology popularity alone does not establish a meaningful research opportunity.

---

# 14. Evidence Maturity Trend

Determine whether evidence types change over time.

Example:

```text
Case reports
      ↓
Observational studies
      ↓
Controlled studies
      ↓
Systematic reviews
      ↓
Implementation evidence
```

This may indicate maturation.

Possible status:

* `EVIDENCE_MATURING`
* `EVIDENCE_STABLE`
* `EVIDENCE_FRAGMENTED`
* `EVIDENCE_STILL_EARLY`

---

# 15. Validation Trend

Identify increasing emphasis on:

* replication;
* external validation;
* multicenter studies;
* cross-cultural validation;
* real-world testing.

This may signal that the field is moving beyond discovery.

---

# 16. Intervention Trend

Determine whether literature increasingly tests:

* intervention effectiveness;
* treatment;
* educational intervention;
* policy intervention;
* behavioral intervention;
* technological intervention.

Do not infer maturity from one or two trials.

---

# 17. Implementation Trend

Identify whether research increasingly addresses:

* adoption;
* feasibility;
* fidelity;
* scalability;
* implementation barriers;
* sustainability.

This may signal translational progress.

---

# 18. Translation Trend

Determine whether research is moving from:

basic knowledge

toward:

* clinical use;
* educational practice;
* industrial use;
* technology;
* policy;
* community implementation.

Use:

`TRANSLATIONAL_SHIFT_SIGNAL`

when evidence supports it.

---

# 19. Interdisciplinary Trend

Identify increasing integration across disciplines.

Examples:

* pharmacy + genomics;
* education + AI;
* ecology + economics;
* psychology + digital health;
* engineering + biomedical science.

Possible status:

* `INTERDISCIPLINARY_GROWTH`
* `STABLE_MULTIDISCIPLINARY_STRUCTURE`
* `NEW_INTEGRATION_SIGNAL`

Do not assume interdisciplinary work is automatically stronger.

---

# 20. Terminology Trend

Fields may change terminology.

Identify:

* old terms declining;
* new terms increasing;
* renamed concepts;
* conceptual reframing.

This is important because literature searches may miss older or newer work if terminology changes.

Pass terminology updates downstream to:

`scopus-literature-search`

---

# 21. Keyword Trend

Keyword frequency may support trend detection.

However, keywords may reflect:

* author labeling;
* indexing practices;
* fashionable terminology.

Do not use keyword counts alone.

Interpret keywords alongside:

* abstracts;
* methods;
* research questions;
* themes.

---

# 22. Citation Momentum

When reliable citation data exist, examine whether recent papers or themes show increasing citation attention.

Possible signals:

* rapidly cited recent work;
* influential methodological paper;
* emerging framework.

Citation momentum is supportive evidence only.

Do not equate citations with scientific truth.

---

# 23. Reference Burst Signal

When bibliometric tools provide citation-burst detection, it may identify rapidly increasing attention to specific works.

Treat as:

`ATTENTION_SIGNAL`

not:

`QUALITY_SIGNAL`

---

# 24. Journal Attention Shift

Determine whether new journals or journal categories begin publishing more on the topic.

Possible reasons:

* field expansion;
* interdisciplinary adoption;
* translation;
* technology diffusion.

Do not interpret journal growth without scope context.

---

# 25. Publisher Independence

Do not treat publication from a major publisher as evidence of trend strength.

Trend evidence should arise from:

* field-level patterns;
* journal-level patterns;
* topic-level evidence.

---

# 26. Geographic Trend

Identify whether research activity expands geographically.

Possible patterns:

* single-region concentration;
* global diffusion;
* LMIC growth;
* multicountry collaboration;
* new ecosystem participation.

Geographic expansion may indicate field maturity or broader relevance.

It is not novelty by itself.

---

# 27. Collaboration Trend

When metadata support it, assess:

* international collaboration;
* multicenter collaboration;
* interdisciplinary teams;
* institutional networks.

Increasing collaboration may signal:

* field consolidation;
* larger studies;
* translational development.

---

# 28. Funding Trend

When reliable data exist, identify whether research funding appears to increase in specific directions.

Use cautiously.

Funding attention is not equivalent to scientific importance.

---

# 29. Trend Strength

For each identified trend, classify confidence.

Possible status:

* `STRONG_TREND`
* `MODERATE_TREND`
* `EARLY_TREND_SIGNAL`
* `WEAK_SIGNAL`
* `NO_CLEAR_TREND`

Base confidence on multiple indicators where possible.

---

# 30. Multi-Signal Trend Rule

Prefer identifying strong trends when several signals agree.

Example:

Topic X:

* publication share increasing;
* new methods appearing;
* recent reviews emerging;
* cross-disciplinary adoption increasing.

This provides stronger trend evidence than publication growth alone.

---

# 31. Trend Sustainability

Distinguish potentially durable trends from short-lived attention.

Possible status:

* `LIKELY_DURABLE`
* `POSSIBLY_DURABLE`
* `EARLY_UNCERTAIN`
* `POSSIBLY_TRANSIENT`

Consider:

* scientific problem persistence;
* methodological utility;
* replication;
* theoretical integration;
* translational relevance.

Do not predict future popularity confidently.

---

# 32. Trend Saturation

A rapidly growing topic may also be crowded.

Classify when useful:

* `LOW_SATURATION`
* `MODERATE_SATURATION`
* `HIGH_SATURATION`
* `UNKNOWN`

High publication growth + high saturation may mean:

many papers

but limited opportunity for incremental work.

Do not equate trend strength with research opportunity.

---

# 33. Trend Opportunity Is Not Research Gap

A trend may identify:

`RESEARCH_ATTENTION`

but not:

`RESEARCH_GAP`

For example:

AI research may be rapidly increasing.

That does not mean:

"AI is a research gap."

Trend analysis must feed into later:

`emerging-topic-discovery`
and eventually:

`sota-builder`
→ `gap-discovery`
→ `gap-validator`

---

# 34. Declining Topics

Declining publication activity does not automatically mean a topic should be avoided.

Decline may reflect:

* scientific resolution;
* terminology change;
* technology replacement;
* funding change;
* research exhaustion;
* movement into applied practice.

Interpret carefully.

---

# 35. Mature Stable Fields

A stable field may still contain high-value questions.

Do not prioritize only rapidly growing topics.

Some mature fields produce important research through:

* replication;
* refinement;
* mechanism;
* implementation;
* translation.

---

# 36. Trend Comparison

When several candidate directions exist, compare them using:

| Direction | Publication Trend | Method Trend | Evidence Maturity | Saturation | Durability Signal |
| --------- | ----------------- | ------------ | ----------------- | ---------- | ----------------- |

Do not add a final novelty judgment.

---

# 37. Trend Map

When useful:

```text
Field
│
├── Theme A
│   └── Rapid Growth
│
├── Theme B
│   └── Stable
│
├── Theme C
│   └── Declining
│
└── Theme D
    └── Early Emerging Signal
```

---

# 38. Trend Output Structure

When a full trend analysis is requested, use:

## A. Time Window

[...]

## B. Historical Baseline

[...]

## C. Publication Growth

[...]

## D. Theme Trends

[...]

## E. Research Question Shifts

[...]

## F. Methodological Trends

[...]

## G. Theoretical Trends

[...]

## H. Population and Context Trends

[...]

## I. Technology Trends

[...]

## J. Evidence Maturity

[...]

## K. Interdisciplinary Trends

[...]

## L. Strongest Trend Signals

[...]

## M. Potentially Declining Areas

[...]

## N. Saturation Assessment

[...]

## O. Durability Assessment

[...]

## P. Areas for Emerging-Topic Analysis

[...]

---

# 39. Trend Evidence Table

When useful:

| Trend | Evidence Signal | Strength | Sustainability | Interpretation |
| ----- | --------------- | -------- | -------------- | -------------- |

---

# 40. Preliminary vs Validated Trend

Use:

`PRELIMINARY_TREND_SIGNAL`

when:

* evidence is sparse;
* only one source is used;
* search coverage is narrow;
* temporal data are incomplete.

Use:

`VALIDATED_TREND_SIGNAL`

when several independent indicators support the conclusion.

---

# 41. Relationship with Research Landscape

`research-landscape` answers:

> What is in the field?

`trend-detection` answers:

> What is changing in the field?

Do not duplicate broad landscape mapping.

---

# 42. Relationship with Emerging Topic Discovery

`trend-detection` identifies changing activity.

`emerging-topic-discovery` determines whether a new research area is genuinely emerging.

A growing mature topic is not necessarily emerging.

---

# 43. Relationship with State of the Art

Trend analysis does not determine the scientific frontier alone.

A highly trending topic may still have weak evidence.

`sota-builder` later integrates:

* evidence quality;
* current consensus;
* contradictions;
* unresolved questions.

---

# 44. Relationship with Gap Discovery

Trend signals may indicate areas worth deeper investigation.

But:

trend ≠ gap.

Gap discovery requires evidence about what remains unresolved.

---

# 45. Scopus-First Research Opportunity

If a trend appears promising, later evidence searching should prioritize active Scopus-indexed literature.

Do not generate final research ideas solely from trend data.

---

# 46. No-Mandatory-APC Awareness

Publication-cost preference does not affect trend identification.

Do not exclude literature because the journal charges APC.

Preserve:

`prefer_no_mandatory_apc`

only for later journal selection.

---

# 47. Target-Journal Awareness

If a target journal is known, its publication pattern may be examined as one signal.

But the trend should represent the field broadly.

Do not define the field's trend from one target journal alone.

---

# 48. Research Passport Update

When supported, update:

```yaml
trend_detection:
  time_window:
  baseline_period:
  publication_pattern:
  theme_trends:
  methodological_trends:
  theoretical_trends:
  population_trends:
  context_trends:
  technology_trends:
  evidence_maturity_trends:
  interdisciplinary_trends:
  saturation:
  durability:
  strong_trends:
  early_signals:
  declining_areas:
  confidence:
  next_stage:
```

Unknown fields remain unknown.

---

# 49. Avoid These Behaviors

Do not:

* equate more papers with scientific progress;
* claim novelty from trend data;
* claim a research gap from growth or decline;
* chase fashionable keywords;
* assume newer methods are better;
* use citation count as evidence quality;
* ignore saturation;
* ignore declining areas;
* fabricate bibliometric numbers;
* infer trends from one journal;
* treat target-journal publications as representative of the entire field;
* let APC status influence scientific trend analysis.

---

# User-Friendly Behavior

Explain trend findings in practical scientific language.

Prefer:

> Research on predictive models is increasing, but most studies remain internally validated. The trend suggests movement toward prediction, while external validation still needs separate evidence assessment.

Avoid:

> Prediction is the hottest trend and therefore the best topic.

---

# Stop Conditions

Do not claim a strong trend when:

* temporal evidence is insufficient;
* the literature search is incomplete;
* terminology changed substantially;
* only publication counts are available;
* field boundaries are unclear.

Label uncertainty and identify what further evidence is needed.

---

# Success Criterion

`trend-detection` succeeds when temporal changes in a research field are identified using multiple scientific signals and interpreted without confusing publication growth, popularity, novelty, evidence quality, or research opportunity.
