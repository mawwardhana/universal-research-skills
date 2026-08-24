---
name: evidence-synthesis
description: Synthesize verified and screened scholarly evidence across studies to determine convergent findings, contradictory evidence, effect patterns, mechanisms, contextual differences, methodological explanations, evidence maturity, uncertainty, and defensible scientific conclusions. Use after literature screening and before State-of-the-Art development, research-gap validation, novelty assessment, theoretical positioning, methodology justification, scientific discussion, systematic review conclusions, or manuscript evidence integration.
---

# Evidence Synthesis

## Purpose

`evidence-synthesis` integrates findings across multiple verified and screened studies.

Its central question is:

> When the relevant evidence is considered together, what can we scientifically conclude, what remains uncertain, and why do studies agree or disagree?

The purpose is not to produce a sequence of article summaries.

The purpose is to identify:

- convergence;
- contradiction;
- consistency;
- heterogeneity;
- methodological differences;
- population differences;
- context effects;
- mechanism signals;
- temporal development;
- evidence maturity;
- uncertainty;
- defensible scientific conclusions.

Evidence synthesis forms the bridge between:

literature collection

and:

scientific interpretation.

---

# Core Principle

Use:

> Synthesize across studies, not paper by paper.

A strong synthesis should move from:

"Study A found X. Study B found Y. Study C found Z."

toward:

"Across the available evidence, X is generally supported under conditions A and B, while findings become inconsistent in population C, possibly because of differences in measurement and study design."

Do not force consensus where evidence is genuinely inconsistent.

---

# Activation Conditions

Use this skill after literature has been:

1. discovered;
2. sufficiently verified;
3. screened for relevance.

Typical upstream route:

`scopus-literature-search`
→ `source-verification`
→ `citation-chaining`
→ `literature-screening`
→ `evidence-synthesis`

Use before:

- `sota-builder`;
- `gap-discovery`;
- `gap-validator`;
- `novelty-builder`;
- theoretical framework development;
- methodological justification;
- scientific discussion;
- systematic-review conclusions;
- manuscript evidence integration.

---

# Input Requirements

Prefer a corpus containing, where available:

- verified bibliographic records;
- relevance classification;
- study design;
- population;
- context;
- methods;
- measurements;
- primary findings;
- effect estimates;
- uncertainty;
- limitations;
- evidence role;
- verification status.

Do not fabricate missing findings.

---

# 1. Define the Synthesis Question

Before synthesis, identify what is being synthesized.

Possible questions include:

- Does X influence Y?
- What mechanisms explain X?
- Which methods are used?
- How consistent is the evidence?
- What factors explain contradictory findings?
- What is currently established?
- What remains unresolved?
- How mature is this research field?

Do not synthesize without a clear scientific purpose.

---

# 2. Select the Synthesis Mode

Possible modes:

- `NARRATIVE_SYNTHESIS`
- `THEMATIC_SYNTHESIS`
- `CONFIGURATIVE_SYNTHESIS`
- `MECHANISM_SYNTHESIS`
- `METHOD_SYNTHESIS`
- `THEORY_SYNTHESIS`
- `CONTRADICTION_SYNTHESIS`
- `SOTA_SYNTHESIS`
- `GAP_VALIDATION_SYNTHESIS`
- `SYSTEMATIC_REVIEW_SYNTHESIS`
- `META_ANALYTIC_HANDOFF`

Choose according to the question and evidence.

Do not use meta-analytic language unless quantitative pooling has actually been performed.

---

# 3. Study-Level Evidence Extraction

For each included study, extract only information relevant to the synthesis question.

Possible fields:

```yaml
study:
  reference_id:
  design:
  population:
  context:
  sample:
  exposure_or_intervention:
  comparator:
  outcome:
  measurement:
  analysis:
  main_finding:
  effect_direction:
  effect_size:
  uncertainty:
  limitations:
  evidence_role: