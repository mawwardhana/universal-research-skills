---
name: novelty-auditor
description: Stress-test proposed scientific novelty claims against the closest verified competitor studies, current State-of-the-Art evidence, alternative terminology, overlapping methods, mechanisms, populations, contexts, validation studies, citation networks, and recent literature. Use after novelty construction and before research-question finalization, methodology lock-in, grant submission, manuscript positioning, journal submission, or any strong claim that a study provides a novel scientific contribution.
---

# Novelty Auditor

## Purpose

`novelty-auditor` determines whether a proposed novelty claim remains defensible after deliberate attempts to weaken or invalidate it.

Its central question is:

> If we compare this proposed contribution with the strongest and closest existing research, does the claimed scientific advancement still remain meaningful?

The auditor should challenge:

- first-study claims;
- novelty boundaries;
- competitor comparisons;
- methodological novelty;
- contextual novelty;
- mechanistic novelty;
- validation novelty;
- translational novelty;
- claims of uniqueness.

The goal is not to protect the proposed study.

The goal is to prevent exaggerated or false novelty.

---

# Core Principle

Use:

> Novelty must survive comparison with the strongest competitor, not merely differ from the average paper.

A novelty claim should be reduced, reframed, or rejected when existing literature already contains substantially equivalent work.

A rejected novelty claim is a successful integrity outcome.

---

# Required Upstream Context

Prefer inputs from:

`scopus-literature-search`
→ `source-verification`
→ `reference-integrity-guard`
→ `citation-chaining`
→ `literature-screening`
→ `evidence-synthesis`
→ `sota-builder`
→ `gap-discovery`
→ `gap-validator`
→ `novelty-builder`

Important inputs include:

- validated gap;
- gap boundary;
- proposed novelty;
- novelty type;
- novelty boundary;
- closest competitor studies;
- competitor comparison;
- current State of the Art;
- proposed study design;
- scientific contribution;
- novelty risk.

Do not audit novelty from the study title alone.

---

# Activation Conditions

Use when the researcher asks:

- "Is this novelty strong enough?"
- "Can I claim this as novel?"
- "Has anyone already done this?"
- "Audit my novelty."
- "Is my contribution actually new?"
- "Will reviewers consider this novel?"
- "Is this study too similar to previous research?"
- "Can I say this is the first study?"

Use especially before:

- research-question finalization;
- methodology finalization;
- grant submission;
- dissertation proposal defense;
- manuscript submission;
- cover-letter novelty claims.

---

# Novelty Audit Status

Input should normally be:

`PROPOSED_NOVELTY`

Possible final outcomes:

- `NOVELTY_STRONGLY_DEFENSIBLE`
- `NOVELTY_DEFENSIBLE`
- `NOVELTY_DEFENSIBLE_WITH_NARROWER_CLAIM`
- `NOVELTY_PARTIALLY_SUPPORTED`
- `NOVELTY_REQUIRES_REFRAMING`
- `NOVELTY_WEAK`
- `LIKELY_DUPLICATIVE`
- `NOVELTY_REJECTED`
- `NOVELTY_INCONCLUSIVE`

Do not force a positive conclusion.

---

# 1. Restate the Proposed Novelty

Represent the claim explicitly.

Recommended structure:

```yaml
novelty_claim:
  validated_gap:
  proposed_advancement:
  novelty_type:
  scientific_contribution:
  novelty_boundary: