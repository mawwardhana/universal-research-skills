---
name: citation-chaining
description: Expand a verified scholarly literature corpus through backward citation, forward citation, related-paper, author, concept, and citation-network exploration to identify foundational studies, subsequent developments, replications, extensions, criticisms, contradictions, methodological advances, and overlooked evidence. Use after anchor papers have been identified and verified, especially for State-of-the-Art development, continuation of previous research, gap validation, novelty assessment, systematic evidence mapping, and manuscript positioning.
---

# Citation Chaining

## Purpose

`citation-chaining` expands a scholarly evidence corpus from one or more verified anchor publications.

Its central question is:

> What scientifically important literature becomes visible when we follow the intellectual relationships around the key papers rather than relying only on keyword searches?

Citation chaining complements database searching.

It is especially useful for finding:

- foundational studies;
- precursor theories;
- original methods;
- subsequent developments;
- replications;
- extensions;
- validations;
- contradictory findings;
- methodological criticism;
- competing explanations;
- recent citing studies;
- adjacent research streams;
- terminology that keyword searches may miss.

Citation chaining must not replace systematic keyword searching when comprehensive evidence coverage is required.

---

# Core Principle

Use:

> Keyword searching finds papers by terminology. Citation chaining finds papers by scientific relationship.

Both are necessary when evidence completeness matters.

Citation relationships must not be interpreted as agreement.

A citing paper may:

- support;
- extend;
- replicate;
- criticize;
- contradict;
- reinterpret;
- merely mention

the cited work.

---

# Activation Conditions

Use this skill when:

- one or more verified anchor papers exist;
- a previous article is being continued;
- seminal literature must be identified;
- recent developments after an earlier study must be mapped;
- State of the Art is being developed;
- a proposed research gap must be stress-tested;
- novelty must be compared with the closest prior studies;
- keyword searching appears incomplete;
- terminology has changed over time;
- contradictory evidence must be located;
- systematic evidence mapping requires citation expansion.

Typical requests include:

- "Who has cited this article?"
- "What research came after this study?"
- "Find the foundational papers behind this article."
- "Has anyone replicated this result?"
- "What studies challenged this paper?"
- "What is the research lineage of this idea?"
- "Use my previous article to find the next research direction."

---

# Required Upstream Condition

Anchor sources should preferably have passed:

`source-verification`

Do not build citation networks around:

- fabricated references;
- unresolved DOI conflicts;
- metadata mashups;
- uncertain publication identity.

Use:

`ANCHOR_VERIFIED`

before deep citation expansion whenever possible.

---

# Citation Chaining Modes

Possible modes include:

- `BACKWARD`
- `FORWARD`
- `BIDIRECTIONAL`
- `RELATED_PAPER`
- `AUTHOR_LINEAGE`
- `METHOD_LINEAGE`
- `THEORY_LINEAGE`
- `CONTRADICTION_SEARCH`
- `REPLICATION_SEARCH`
- `CONTINUATION_SEARCH`
- `NOVELTY_STRESS_TEST`

Choose the mode according to the research objective.

---

# 1. Anchor Paper Selection

Select anchor papers based primarily on scientific relevance.

Potential anchor types include:

- previous study by the researcher;
- seminal paper;
- current high-quality study;
- systematic review;
- methodological paper;
- theory paper;
- validation study;
- contradictory study.

Do not choose anchor papers solely because they are highly cited.

---

# 2. Anchor Record

Record when available:

```yaml
anchor:
  title:
  authors:
  year:
  journal:
  doi:
  scopus_source_status:
  scopus_document_status:
  evidence_role:
  verification_status: