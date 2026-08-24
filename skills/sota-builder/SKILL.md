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