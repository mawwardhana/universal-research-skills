---
name: literature-screening
description: Screen discovered and verified scholarly records for relevance and eligibility using transparent, research-purpose-specific inclusion and exclusion criteria. Use after database searching and citation chaining to create a defensible literature corpus for research landscapes, State-of-the-Art analysis, research-gap validation, novelty assessment, systematic reviews, meta-analyses, methodology development, and manuscript evidence synthesis.
---

# Literature Screening

## Purpose

`literature-screening` determines which scholarly records should enter a research evidence corpus for a specific scientific purpose.

Its central question is:

> Of all the literature we discovered and verified, which studies are actually relevant and eligible for the question we are trying to answer?

Literature screening protects the framework from:

- topic drift;
- irrelevant evidence;
- duplicate records;
- inappropriate document types;
- wrong populations;
- wrong outcomes;
- wrong methods;
- weak relevance;
- hidden selection bias;
- selective inclusion of supportive studies.

Screening must be transparent and reproducible.

---

# Core Principle

Use:

> Discovery finds possibilities. Screening determines eligibility.

A source can be:

- real;
- peer reviewed;
- Scopus indexed;

and still be irrelevant to the research question.

Verification does not equal inclusion.

---

# Activation Conditions

Use this skill after literature has been obtained through:

- `scopus-literature-search`;
- `citation-chaining`;
- OpenAlex;
- Crossref;
- PubMed;
- Semantic Scholar;
- publisher platforms;
- uploaded bibliographies;
- previous research materials.

Use before:

- `evidence-synthesis`;
- `sota-builder`;
- `gap-discovery`;
- `gap-validator`;
- `novelty-builder`;
- systematic review;
- meta-analysis;
- manuscript evidence integration.

---

# Screening Modes

Possible screening modes include:

- `EXPLORATORY`
- `LANDSCAPE`
- `TREND`
- `EMERGING_TOPIC`
- `SOTA`
- `GAP_VALIDATION`
- `NOVELTY_VALIDATION`
- `CONTINUATION_RESEARCH`
- `THEORY`
- `METHODOLOGY`
- `MEASUREMENT`
- `SYSTEMATIC_REVIEW`
- `META_ANALYSIS`
- `MANUSCRIPT_SUPPORT`

Screening strictness should depend on the purpose.

---

# 1. Define the Screening Question

Before screening, identify what the literature corpus is intended to support.

Examples:

- map a research field;
- assess current evidence;
- evaluate a mechanism;
- validate a research gap;
- identify competing studies;
- justify methodology;
- prepare a systematic review.

Do not screen without knowing the scientific purpose.

---

# 2. Define Eligibility Criteria

Eligibility criteria may include:

- population;
- phenomenon;
- intervention;
- exposure;
- comparator;
- outcome;
- study design;
- publication type;
- time period;
- language;
- context;
- methodology;
- peer-review status;
- indexing requirements.

Only include criteria that are scientifically necessary.

---

# 3. Use Question-Appropriate Frameworks

When useful, structure eligibility using appropriate frameworks.

Examples:

## PICO

- Population
- Intervention
- Comparator
- Outcome

Useful for many clinical questions.

## PECO

- Population
- Exposure
- Comparator
- Outcome

Useful for observational or exposure research.

## PCC

- Population
- Concept
- Context

Useful for scoping reviews.

## SPIDER

- Sample
- Phenomenon of Interest
- Design
- Evaluation
- Research type

Useful for qualitative or mixed-method research.

Do not force PICO onto every discipline.

---

# 4. Inclusion Criteria

Define explicit inclusion criteria.

Examples:

- directly relevant population;
- relevant outcome;
- specified study design;
- peer-reviewed article;
- relevant research period;
- appropriate language;
- relevant methodological approach.

Criteria should be determined before final study selection whenever possible.

---

# 5. Exclusion Criteria

Possible exclusions include:

- irrelevant population;
- wrong outcome;
- wrong context;
- purely editorial material;
- conference abstract without sufficient data;
- duplicate publication;
- retracted article;
- insufficient methodological detail;
- outside predefined scope.

Do not create exclusion criteria merely to remove contradictory studies.

---

# 6. Relevance Categories

Use:

- `DIRECTLY_RELEVANT`
- `HIGHLY_RELEVANT`
- `SUPPORTING`
- `CONTEXTUAL`
- `MARGINALLY_RELEVANT`
- `IRRELEVANT`

The same article may have different relevance depending on the research purpose.

---

# 7. Screening Stages

When appropriate, use:

```text
Identification
      ↓
Deduplication
      ↓
Title Screening
      ↓
Abstract Screening
      ↓
Full-Text Screening
      ↓
Final Inclusion