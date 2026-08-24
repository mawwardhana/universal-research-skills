---

name: research-landscape
description: Map the current structure of a research field or candidate research direction by organizing its major concepts, themes, theories, methods, populations, contexts, evidence streams, publication patterns, and scientific development. Use when a researcher needs to understand what a field currently contains before evaluating trends, emerging topics, State of the Art, research gaps, novelty, or future research opportunities.
---

# Research Landscape

## Purpose

`research-landscape` creates a structured map of a research field or candidate research direction.

Its role is to answer:

> What does the current scientific landscape around this research area actually look like?

The landscape should help the researcher understand:

* major themes;
* core concepts;
* dominant research questions;
* theoretical perspectives;
* methodological approaches;
* populations and contexts;
* major evidence streams;
* important publication patterns;
* areas of convergence and fragmentation;
* scientific maturity.

The purpose is not yet to declare:

* a research gap;
* novelty;
* a definitive State of the Art;
* the best next study.

Those decisions belong to downstream skills.

---

# Core Principle

Use:

> Map the field before judging the field.

Do not search only for evidence supporting the researcher's preferred idea.

The landscape must include:

* supporting evidence;
* contradictory evidence;
* competing approaches;
* alternative conceptualizations.

---

# Activation Conditions

Use this skill when:

* a broad research topic has been identified;
* `idea-discovery` produced candidate research directions;
* the researcher wants to understand a field;
* the user asks what has been studied in an area;
* a possible research direction needs evidence mapping;
* the researcher wants to know dominant themes or approaches;
* the field must be mapped before trend or gap analysis;
* previous research needs to be repositioned against current literature.

Typical requests include:

* "Map the research around this topic."
* "What does the literature currently focus on?"
* "What are the major research streams in this field?"
* "How has this field developed?"
* "What approaches are commonly used?"
* "Before choosing a topic, show me the research landscape."

---

# Relationship with Evidence Search

`research-landscape` organizes evidence.

It should normally rely on literature retrieved through appropriate evidence workflows.

Preferred evidence route:

`scopus-literature-search`
→ `source-verification`
→ `literature-screening`
→ `research-landscape`

When those skills are not yet available or when the user requests only preliminary mapping, create:

`PRELIMINARY_LANDSCAPE`

and clearly state that comprehensive literature verification is still required.

---

# Scopus-First Principle

When external literature search is required, prioritize:

1. peer-reviewed articles from active Scopus-indexed journals;
2. high-quality systematic reviews and meta-analyses when appropriate;
3. recent high-quality primary studies;
4. seminal foundational works;
5. contradictory or competing evidence;
6. relevant methodological papers.

Other scholarly platforms may be used for discovery and verification.

Never claim that a journal or article is Scopus-indexed unless current status has been verified.

---

# Evidence Recency

Research landscapes should represent the current field.

Use recent literature heavily when the topic is rapidly developing.

However:

* do not exclude seminal older work;
* do not assume newer automatically means better;
* do not replace foundational theory merely because it is old.

Distinguish:

* foundational literature;
* established literature;
* recent literature;
* emerging literature.

---

# 1. Define the Landscape Boundary

Before mapping, define what is inside and outside the landscape.

Possible boundary dimensions include:

* concept;
* phenomenon;
* population;
* intervention;
* exposure;
* outcome;
* technology;
* discipline;
* geographical scope;
* publication period;
* research design.

Record:

`LANDSCAPE_SCOPE`

Avoid scopes so broad that the resulting map becomes meaningless.

---

# 2. Clarify Terminology

Research areas often use multiple terms for similar concepts.

Identify:

* preferred terminology;
* synonyms;
* historical terminology;
* competing terminology;
* abbreviations;
* related concepts.

Example:

A field may use:

* workplace learning;
* informal workplace learning;
* work-based learning;
* learning at work.

Do not automatically merge concepts that are theoretically distinct.

---

# 3. Build a Concept Map

Identify major concepts and their relationships.

Possible categories:

* core concept;
* antecedent;
* mechanism;
* moderator;
* outcome;
* context;
* intervention;
* implementation factor;
* measurement construct.

When useful, represent:

```text
Core Phenomenon
├── Antecedents
├── Mechanisms
├── Outcomes
├── Boundary Conditions
├── Contexts
└── Applications
```

This is conceptual mapping, not causal proof.

---

# 4. Identify Major Research Themes

Group literature into coherent scientific themes.

Themes should reflect:

* recurring problems;
* conceptual questions;
* methodological approaches;
* applications;
* evidence streams.

Avoid creating themes based only on repeated keywords.

Classify themes when useful as:

* `CORE_THEME`
* `ESTABLISHED_THEME`
* `ACTIVE_THEME`
* `EMERGING_THEME_SIGNAL`
* `NICHE_THEME`

Final emerging-topic classification belongs to:

`emerging-topic-discovery`

---

# 5. Identify Research Streams

A research theme may contain several distinct streams.

Example:

Artificial intelligence in education may contain:

* AI-supported feedback;
* automated assessment;
* personalized learning;
* academic integrity;
* teacher adoption;
* learning analytics.

A landscape should make these distinctions visible.

---

# 6. Identify Dominant Scientific Questions

Determine what questions researchers repeatedly ask.

Possible forms:

* What is happening?
* What factors are associated?
* Why does it happen?
* Through what mechanism?
* Under what conditions?
* Can it be predicted?
* Can it be changed?
* Can it be implemented?
* Does it generalize?

Do not assume frequency means scientific importance.

---

# 7. Field Maturity Mapping

Determine the approximate maturity of each major research stream.

Possible stages:

* discovery;
* characterization;
* description;
* association;
* mechanism;
* validation;
* prediction;
* intervention;
* implementation;
* translation.

Different streams within the same topic may be at different maturity levels.

Do not force a single maturity label onto the entire field.

---

# 8. Theory Landscape

Identify important theories, conceptual frameworks, or disciplinary models.

For each major framework, determine:

* what it explains;
* where it is applied;
* whether it is dominant;
* whether competing theories exist;
* whether it is frequently tested or merely cited.

Possible status:

* `DOMINANT_FRAMEWORK`
* `ESTABLISHED_FRAMEWORK`
* `COMPETING_FRAMEWORK`
* `EMERGING_FRAMEWORK`
* `WEAK_THEORETICAL_STRUCTURE`

Do not treat citation frequency as proof of theoretical adequacy.

---

# 9. Construct and Variable Landscape

For quantitative research, identify frequently studied:

* predictors;
* outcomes;
* mediators;
* moderators;
* confounders;
* latent constructs.

For qualitative research, identify:

* central phenomena;
* participant experiences;
* recurring themes;
* interpretive lenses.

For experimental research, identify:

* intervention types;
* comparators;
* experimental conditions;
* outcome classes.

Do not generate new causal models merely from co-occurrence.

---

# 10. Methodological Landscape

Map the research designs used in the field.

Examples:

* cross-sectional;
* longitudinal;
* cohort;
* case-control;
* randomized controlled trial;
* quasi-experimental;
* laboratory experiment;
* field experiment;
* qualitative;
* case study;
* ethnography;
* mixed methods;
* systematic review;
* meta-analysis;
* computational modeling;
* machine learning.

Identify methodological concentration.

For example:

> Most available studies are cross-sectional.

This is a landscape observation.

It is not yet a confirmed methodological gap.

---

# 11. Analytical Landscape

Map common analytical approaches where relevant.

Examples:

* descriptive analysis;
* regression;
* multilevel modeling;
* SEM;
* PLS-SEM;
* survival analysis;
* mediation;
* moderation;
* longitudinal modeling;
* meta-analysis;
* machine learning;
* thematic analysis;
* content analysis.

Do not rank analysis quality based solely on sophistication.

---

# 12. Measurement Landscape

Identify major measurement approaches.

Examples:

* validated scales;
* self-report questionnaires;
* biomarkers;
* laboratory assays;
* administrative data;
* sensor data;
* interview protocols;
* observational coding.

Note measurement diversity and possible disagreement.

Measurement problems may later become research-gap signals.

Do not declare them gaps here.

---

# 13. Population Landscape

Identify populations commonly studied.

Examples:

* children;
* university students;
* older adults;
* patients;
* professionals;
* organizations;
* communities;
* species;
* ecosystems.

Classify:

* heavily studied populations;
* moderately studied populations;
* less represented populations.

Low publication frequency alone does not establish scientific importance.

---

# 14. Context Landscape

Map relevant contexts:

* country;
* cultural context;
* clinical setting;
* educational level;
* organizational setting;
* industry;
* environmental setting;
* laboratory condition;
* technological environment.

Do not equate geographical underrepresentation with novelty automatically.

Ask whether the context could plausibly affect the phenomenon.

---

# 15. Temporal Landscape

Determine how the field has developed over time.

Possible periods:

* foundational phase;
* expansion phase;
* consolidation phase;
* rapid-growth phase;
* current phase.

The exact periods should emerge from the literature.

Do not impose arbitrary decade categories unless useful.

---

# 16. Publication Growth Signal

When bibliographic data support it, examine whether publication volume is:

* stable;
* increasing;
* rapidly increasing;
* declining;
* fluctuating.

This is only a signal.

Formal trend assessment belongs to:

`trend-detection`

---

# 17. Seminal Literature

Identify foundational or highly influential literature where scientifically appropriate.

Seminal status may derive from:

* foundational concept;
* theory origin;
* landmark methodology;
* historically important empirical finding.

Do not define seminal work solely by citation count.

---

# 18. Recent Anchor Literature

Identify recent high-quality studies that help define the current field.

Prefer:

* current Scopus-indexed peer-reviewed literature;
* recent systematic reviews;
* major primary studies;
* methodological advances.

These papers help establish the transition from historical foundations to current science.

---

# 19. Evidence-Type Landscape

Determine what kinds of evidence dominate.

Examples:

* observational evidence;
* experimental evidence;
* qualitative evidence;
* mechanistic evidence;
* predictive evidence;
* implementation evidence;
* systematic synthesis.

This helps assess field maturity.

Do not convert evidence-type scarcity directly into a gap.

---

# 20. Evidence Convergence

Identify whether major findings appear:

* convergent;
* partially convergent;
* contradictory;
* highly context-dependent;
* method-dependent.

Use:

* `CONVERGENT_SIGNAL`
* `MIXED_SIGNAL`
* `CONTRADICTORY_SIGNAL`
* `CONTEXT_DEPENDENT_SIGNAL`
* `INSUFFICIENT_EVIDENCE`

Formal evidence synthesis belongs downstream to:

`evidence-synthesis`

---

# 21. Contradictory Evidence

Do not hide disagreement.

For major disagreements, record:

* what findings differ;
* study designs involved;
* populations involved;
* measurement differences;
* possible methodological explanations.

Do not resolve contradictions without evidence.

Contradictions may later become:

`POTENTIAL_GAP_SIGNAL`

---

# 22. Research Density

Identify areas of:

* high research concentration;
* moderate concentration;
* sparse literature.

Use cautiously.

Sparse literature may mean:

* genuine opportunity;
* immature field;
* low scientific relevance;
* terminology mismatch;
* inaccessible literature.

Do not automatically call sparse areas gaps.

---

# 23. Method–Topic Clusters

Identify whether certain methods dominate particular themes.

For example:

Theme A:
mostly qualitative.

Theme B:
mostly cross-sectional quantitative.

Theme C:
mostly laboratory experimental.

Such clustering may reveal how the field approaches different questions.

---

# 24. Population–Topic Clusters

Determine whether particular populations dominate specific themes.

This may later support:

* external-validation questions;
* boundary-condition questions;
* contextual research.

Do not declare missing populations as gaps before validation.

---

# 25. Geography–Topic Clusters

When relevant, identify where research is concentrated.

Possible categories:

* global;
* regional;
* country-specific;
* high-income-country dominated;
* low- and middle-income-country representation;
* specific ecosystem or region.

Geographical concentration should be interpreted scientifically rather than politically or strategically.

---

# 26. Interdisciplinary Structure

Determine whether the field draws from multiple disciplines.

Identify:

* contributing disciplines;
* shared concepts;
* different terminology;
* methodological differences;
* potential integration points.

Classify:

* `SINGLE_DISCIPLINE_DOMINANT`
* `MULTIDISCIPLINARY`
* `INTERDISCIPLINARY`
* `FRAGMENTED_ACROSS_DISCIPLINES`

Do not call interdisciplinary integration novel until evidence is assessed.

---

# 27. Technology Landscape

If technology is relevant, identify:

* established tools;
* emerging tools;
* data sources;
* platforms;
* instrumentation;
* computational approaches.

Technology adoption may signal emerging research directions.

Formal emerging-topic analysis belongs downstream.

---

# 28. Clinical or Practical Landscape

For applied fields, identify whether research is concentrated in:

* basic discovery;
* laboratory validation;
* clinical testing;
* field implementation;
* policy;
* real-world practice.

This helps identify translational maturity.

---

# 29. Research Ecosystem

When bibliographic evidence permits, identify important:

* journals;
* research groups;
* institutions;
* countries;
* collaborative networks.

Do not equate prolific output with superior scientific quality.

This information is descriptive.

---

# 30. Journal Landscape

Identify journals that repeatedly publish relevant research.

When possible, distinguish:

* highly relevant journals;
* adjacent journals;
* specialty journals;
* multidisciplinary journals.

Scopus status should be verified before being claimed.

Do not yet recommend journals for manuscript submission solely because they publish many articles on the topic.

Journal selection belongs downstream to:

`journal-matcher`

---

# 31. No-Mandatory-APC Awareness

Journal-cost policy is not a criterion for scientific landscape mapping.

However, when the Research Passport contains:

`prefer_no_mandatory_apc: true`

preserve this preference for later publication strategy.

Do not exclude scientifically relevant literature because its journal uses APCs.

Reference selection and publication-cost strategy are separate decisions.

---

# 32. Target-Journal Literature Awareness

If the researcher has a target journal, relevant articles from that journal may be represented within the landscape when scientifically appropriate.

They may help understand:

* topic emphasis;
* methods;
* scholarly conversation.

Do not artificially inflate the representation of the target journal.

---

# 33. Literature Quality Awareness

Do not treat all retrieved papers equally.

Consider:

* study design;
* methodological rigor;
* sample quality;
* measurement;
* analysis;
* peer-review status;
* replication;
* consistency.

Formal source-quality grading belongs to:

`source-verification`

---

# 34. Avoid Confirmation Bias

The landscape must actively include:

* supportive studies;
* negative studies;
* contradictory findings;
* alternative theories;
* competing methodologies.

Do not build a landscape that merely justifies the researcher's preferred idea.

---

# 35. Avoid Citation-Count Bias

Highly cited studies may be important.

But citation count can reflect:

* age;
* controversy;
* field size;
* popularity.

Do not equate citations with truth.

---

# 36. Avoid Publisher Bias

Do not prefer evidence merely because it comes from:

* Elsevier;
* Springer Nature;
* Wiley;
* Taylor & Francis;
* Sage;
* Emerald;
* another major publisher.

Evaluate the journal and study individually.

---

# 37. Landscape Completeness

Classify landscape confidence where useful:

* `COMPREHENSIVE`
* `SUBSTANTIAL`
* `PRELIMINARY`
* `LIMITED`

A landscape should be labeled `PRELIMINARY` when:

* only a small literature set was examined;
* database coverage is limited;
* Scopus verification has not yet occurred;
* terminology is still uncertain.

---

# 38. Landscape Output

When a full landscape is requested, structure it as:

## A. Landscape Scope

[...]

## B. Terminology and Conceptual Boundaries

[...]

## C. Major Research Themes

[...]

## D. Research Streams

[...]

## E. Dominant Scientific Questions

[...]

## F. Theory and Conceptual Frameworks

[...]

## G. Methodological Landscape

[...]

## H. Analytical Landscape

[...]

## I. Measurement Landscape

[...]

## J. Population and Context Landscape

[...]

## K. Temporal Development

[...]

## L. Evidence Types

[...]

## M. Convergence and Contradictions

[...]

## N. Interdisciplinary Structure

[...]

## O. Field Maturity

[...]

## P. Important Literature Anchors

[...]

## Q. Areas Requiring Deeper Investigation

[...]

## R. Next Recommended Analysis

[...]

---

# 39. Landscape Matrix

When useful:

| Theme | Main Question | Common Methods | Main Population | Evidence Maturity | Current Signal |
| ----- | ------------- | -------------- | --------------- | ----------------- | -------------- |

Current signal may include:

* established;
* active;
* contradictory;
* immature;
* emerging signal.

Do not label "gap" here.

---

# 40. Theme Map

When useful:

```text
Research Field
│
├── Theme A
│   ├── Subtheme A1
│   └── Subtheme A2
│
├── Theme B
│   ├── Subtheme B1
│   └── Subtheme B2
│
└── Theme C
```

Keep classifications evidence-based.

---

# 41. Maturity Map

When appropriate:

| Research Stream | Discovery | Association | Mechanism | Validation | Intervention | Implementation |
| --------------- | --------- | ----------- | --------- | ---------- | ------------ | -------------- |

Use only stages relevant to the field.

---

# 42. Density Map

When evidence allows:

* `DENSE`
* `MODERATE`
* `SPARSE`
* `UNCERTAIN`

Density is descriptive and not equivalent to research opportunity.

---

# 43. Transition to Trend Detection

After landscape mapping, route to:

`trend-detection`

when the researcher needs to know:

* what is increasing;
* what is declining;
* which approaches are accelerating;
* which topics are gaining attention.

---

# 44. Transition to Emerging Topic Discovery

Route to:

`emerging-topic-discovery`

when the researcher needs to identify:

* newly developing concepts;
* recently appearing methods;
* new combinations of disciplines;
* early scientific signals.

---

# 45. Transition to State of the Art

Route eventually to:

`sota-builder`

when the researcher needs to determine:

* what is currently established;
* what constitutes the best current evidence;
* what is contested;
* what remains unresolved.

`research-landscape` maps breadth.

`sota-builder` evaluates the current scientific frontier.

Do not duplicate these functions.

---

# 46. Transition to Gap Discovery

Do not jump directly from a broad landscape observation to a confirmed gap.

Required logic:

```text
Landscape
↓
Evidence Synthesis
↓
State of the Art
↓
Gap Discovery
↓
Gap Validation
```

---

# 47. Research Passport Update

When supported, update:

```yaml
research_landscape:
  scope:
  terminology:
  core_concepts:
  themes:
  research_streams:
  dominant_questions:
  theories:
  methods:
  analyses:
  measurements:
  populations:
  contexts:
  temporal_pattern:
  evidence_types:
  convergence_signals:
  contradiction_signals:
  interdisciplinary_structure:
  maturity:
  density:
  seminal_sources:
  recent_anchor_sources:
  confidence:
  next_stage:
```

Unknown values remain unknown.

---

# 48. Avoid These Behaviors

Do not:

* declare novelty;
* declare a research gap;
* invent literature;
* fabricate citation metadata;
* ignore contradictory evidence;
* treat publication volume as scientific quality;
* equate geographic absence with novelty;
* equate sparse literature with opportunity;
* equate advanced methods with stronger evidence;
* overrepresent a target journal;
* exclude relevant literature because of APC policy;
* confuse landscape mapping with systematic review.

---

# User-Friendly Behavior

Explain the field as a map, not a bibliography dump.

Instead of presenting fifty paper summaries, organize them into meaningful scientific structures.

For example:

> The literature appears to fall into four main streams. Most work addresses X and Y, while mechanism studies are less mature. Longitudinal evidence is limited, but that should still be verified before treating it as a research gap.

This helps the researcher understand where the field stands without prematurely making novelty claims.

---

# Stop Conditions

Do not present a landscape as comprehensive when:

* literature coverage is insufficient;
* terminology remains unresolved;
* only one database or narrow query has been used;
* source verification is incomplete;
* key subfields may be missing.

Label the map as preliminary and identify what must be searched next.

---

# Success Criterion

`research-landscape` succeeds when the researcher can see the current structure, major themes, conceptual and methodological patterns, evidence maturity, and scientific development of a field clearly enough to proceed to trend analysis, emerging-topic discovery, State-of-the-Art evaluation, and eventually research-gap validation.
