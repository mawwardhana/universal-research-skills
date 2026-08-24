---
name: gap-discovery
description: Discover and structure candidate research gaps from a verified State of the Art by examining unresolved questions, contradictory evidence, theoretical limitations, methodological weaknesses, missing validation, measurement problems, contextual boundary conditions, temporal uncertainty, implementation failures, and translational discontinuities. Use after State-of-the-Art development and before formal gap validation or novelty construction.
---

# Research Gap Discovery

## Purpose

`gap-discovery` converts unresolved scientific conditions identified in the State of the Art into explicit candidate research gaps.

Its central question is:

> Which unresolved conditions in the current scientific evidence may represent meaningful and researchable gaps?

The purpose is not to declare every unanswered question a research gap.

The purpose is to identify, classify, and prioritize:

`CANDIDATE_RESEARCH_GAPS`

that can later be stress-tested through:

`gap-validator`

A candidate gap remains provisional until validated against current evidence.

---

# Core Principle

Use:

> Unresolved does not automatically mean gap, and gap does not automatically mean worthwhile research.

A defensible research gap should eventually demonstrate:

1. a meaningful unresolved scientific condition;
2. evidence that the condition remains unresolved;
3. scientific or practical consequences of that uncertainty;
4. a plausible research pathway capable of addressing it.

`gap-discovery` addresses primarily points 1, 3, and 4.

`gap-validator` determines point 2 rigorously.

---

# Required Upstream Context

Prefer outputs from:

`scopus-literature-search`
→ `source-verification`
→ `reference-integrity-guard`
→ `citation-chaining`
→ `literature-screening`
→ `evidence-synthesis`
→ `sota-builder`

Important SoTA inputs include:

- established knowledge;
- emerging evidence;
- contested evidence;
- unresolved questions;
- scientific frontiers;
- methodological limitations;
- measurement limitations;
- contextual boundaries;
- evidence maturity;
- closest competitor studies.

Do not generate gaps from memory when a verified SoTA is available.

---

# Activation Conditions

Use this skill when the researcher asks:

- "What is the research gap?"
- "Which gaps exist in this literature?"
- "What remains unanswered?"
- "Where can I position my study?"
- "What should be researched next?"
- "Which unresolved issue could become my research problem?"
- "What gap remains after my previous study?"
- "Which part of the State of the Art creates a research opportunity?"

Do not use this skill as a substitute for literature search.

---

# Gap Discovery Status

All outputs from this skill should initially use:

`CANDIDATE_GAP`

or:

`POTENTIAL_GAP_SIGNAL`

Do not use:

`VALIDATED_RESEARCH_GAP`

until `gap-validator` has completed the validation process.

---

# 1. Start from the SoTA

The preferred discovery logic is:

```text
ESTABLISHED
What is already sufficiently known?

EMERGING
What is developing but still immature?

CONTESTED
Where does evidence disagree?

UNRESOLVED
What important scientific questions remain unanswered?

FRONTIER
Where is the field actively advancing?