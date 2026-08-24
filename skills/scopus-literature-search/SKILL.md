---

name: scopus-literature-search
description: Design and execute transparent Scopus-first scholarly literature searches for any research topic, prioritizing relevant peer-reviewed evidence from Scopus-indexed sources while supporting fallbacks through OpenAlex, Crossref, PubMed, Semantic Scholar, and publisher metadata when direct Scopus access is unavailable. Use when literature must be discovered for research ideas, landscape mapping, trends, State of the Art, gap validation, novelty assessment, methodology, evidence synthesis, manuscript development, or continuation of previous research.
---

# Scopus Literature Search

## Purpose

`scopus-literature-search` is the primary scholarly literature discovery skill for Universal Research Skills.

Its purpose is to retrieve a broad but scientifically relevant body of literature while preserving:

* search transparency;
* reproducibility;
* source provenance;
* Scopus-first priority;
* terminology coverage;
* recency;
* seminal evidence;
* contradictory evidence;
* methodological diversity.

This skill performs **literature discovery**.

It does not independently establish:

* source credibility;
* final Scopus status;
* research gaps;
* novelty;
* evidence strength;
* journal suitability.

Those decisions require downstream verification and synthesis.

---

# Core Principle

Use:

> Search broadly enough to avoid missing the science, but verify rigorously before using the evidence.

The preferred search hierarchy is:

```text
Direct Scopus search when available
        ↓
Scholarly discovery providers
        ↓
Metadata normalization
        ↓
Source verification
        ↓
Evidence screening
```

Do not fabricate Scopus access.

Do not claim that a search was performed directly in Scopus unless Scopus was actually accessed.

---

# Universal Search Policy

The search process must be:

* topic-agnostic;
* discipline-aware;
* reproducible;
* iterative;
* multilingual when scientifically appropriate;
* resistant to confirmation bias;
* capable of supporting both new and continuing research.

The user should not need to understand database syntax before receiving help.

---

# Activation Conditions

Use this skill whenever scholarly evidence must be discovered for:

* research idea development;
* research landscape mapping;
* trend detection;
* emerging-topic analysis;
* continuation of previous research;
* forward or backward exploration;
* State-of-the-Art development;
* research-gap discovery;
* gap validation;
* novelty assessment;
* theoretical framework;
* conceptual framework;
* methodology design;
* statistical-method justification;
* systematic review preparation;
* meta-analysis preparation;
* manuscript writing;
* discussion development;
* journal positioning.

---

# Search Modes

Determine the purpose of the search before constructing queries.

Possible modes include:

* `EXPLORATORY`
* `LANDSCAPE`
* `CURRENT_EVIDENCE`
* `SOTA`
* `GAP_VALIDATION`
* `NOVELTY_VALIDATION`
* `CONTINUATION`
* `THEORY`
* `METHODOLOGY`
* `MEASUREMENT`
* `CONTRADICTORY_EVIDENCE`
* `TARGET_JOURNAL_CONTEXT`
* `SYSTEMATIC_REVIEW`
* `META_ANALYSIS`
* `MANUSCRIPT_SUPPORT`

Different purposes require different search breadth.

---

# 1. Determine Search Objective

Before searching, identify:

* research topic;
* research question when available;
* concepts;
* population;
* context;
* intervention or exposure;
* outcome;
* methodology when relevant;
* desired evidence type;
* time sensitivity.

Do not require all elements when the search is exploratory.

---

# 2. Search Question Decomposition

Break the topic into searchable concept blocks.

Example structure:

```text
Concept A
AND
Concept B
AND
Concept C
```

Each concept may contain synonyms connected by:

`OR`

Example:

```text
("workplace learning" OR "learning at work" OR "informal workplace learning")
AND
("artificial intelligence" OR AI OR "generative AI")
```

Do not create unnecessarily restrictive queries at the beginning.

---

# 3. Terminology Expansion

Generate terms from:

* synonyms;
* acronyms;
* spelling variants;
* historical terminology;
* disciplinary terminology;
* controlled vocabulary when available;
* broader concepts;
* narrower concepts.

Preserve concept boundaries.

Do not merge terms that are theoretically different merely because they appear similar.

---

# 4. Terminology Drift

For fields whose terminology changes over time, search both:

* historical terminology;
* current terminology.

This is essential for:

* trend detection;
* State-of-the-Art analysis;
* citation chaining;
* long-term research trajectories.

Failure to account for terminology drift may create false gaps.

---

# 5. Discipline-Aware Search Expansion

Different disciplines may describe similar phenomena differently.

Where appropriate, generate terms from adjacent disciplines.

Example:

A digital-health topic may involve terminology from:

* medicine;
* pharmacy;
* public health;
* computer science;
* behavioral science.

Do not force interdisciplinary expansion when it is not relevant.

---

# 6. Direct Scopus Search

When direct Scopus access is available, prioritize it.

Possible access forms may include:

* institutional Scopus interface;
* authorized Scopus API;
* other legitimate direct Scopus access.

Record:

`SCOPUS_ACCESS_MODE`

Possible values:

* `DIRECT_INTERFACE`
* `AUTHORIZED_API`
* `NO_DIRECT_ACCESS`
* `UNKNOWN`

Never claim direct Scopus retrieval when it did not occur.

---

# 7. Fallback Discovery

When direct Scopus access is unavailable, scholarly discovery may use:

* OpenAlex;
* Crossref;
* PubMed;
* Semantic Scholar;
* publisher platforms;
* discipline-specific scholarly databases where appropriate.

These sources support:

`DISCOVERY`

They do not automatically prove:

`SCOPUS_INDEXED`

Discovered records must proceed to verification.

---

# 8. Provider Roles

Use providers according to their strengths.

## Scopus

Preferred source for direct Scopus-indexed literature retrieval when legitimately available.

## OpenAlex

Useful for:

* broad scholarly discovery;
* concepts;
* authors;
* institutions;
* citations;
* related works;
* bibliographic exploration.

OpenAlex metadata do not replace Scopus-status verification.

## Crossref

Useful for:

* DOI validation;
* bibliographic metadata;
* publisher metadata;
* title normalization.

Crossref registration does not mean Scopus indexing.

## PubMed

Useful especially for:

* biomedical;
* clinical;
* health;
* pharmaceutical;
* life-science literature.

PubMed inclusion does not mean Scopus indexing.

## Semantic Scholar

Useful for:

* scholarly discovery;
* related papers;
* citation exploration.

It does not replace Scopus verification.

## Publisher Platforms

Useful for:

* article metadata;
* full-text availability;
* publication dates;
* issue information;
* journal policies.

Publisher presence does not by itself prove Scopus indexing.

---

# 9. Scopus Status Separation

Always distinguish among different verification levels.

Use conceptually separate fields:

```yaml
scopus_source_status:
scopus_document_status:
```

Possible source status values:

* `SCOPUS_SOURCE_ACTIVE`
* `SCOPUS_SOURCE_DISCONTINUED`
* `SCOPUS_SOURCE_NOT_FOUND`
* `SCOPUS_SOURCE_UNVERIFIED`

Possible document status values:

* `SCOPUS_DOCUMENT_VERIFIED`
* `SCOPUS_DOCUMENT_NOT_FOUND`
* `SCOPUS_DOCUMENT_UNVERIFIED`

Do not automatically set:

`SCOPUS_DOCUMENT_VERIFIED`

because:

`SCOPUS_SOURCE_ACTIVE`

is true.

---

# 10. Publication-Year Sensitivity

A journal may:

* enter Scopus after an article was published;
* later become discontinued;
* change coverage.

Therefore, where relevant, verify whether the source was covered around the publication year.

Use conceptually:

`SCOPUS_COVERAGE_AT_PUBLICATION`

Possible values:

* `VERIFIED`
* `LIKELY`
* `NOT_COVERED`
* `UNVERIFIED`

Do not make historical-indexing claims without evidence.

---

# 11. Scopus-First Does Not Mean Scopus-Only

The framework prioritizes Scopus-indexed peer-reviewed literature.

However, scientifically necessary non-Scopus sources may include:

* major official guidelines;
* government regulations;
* internationally recognized standards;
* authoritative statistical reports;
* seminal books;
* policy documents;
* technical standards.

Clearly distinguish these source types.

Do not discard essential authoritative evidence merely because it is not a journal article.

---

# 12. Peer-Reviewed Evidence Priority

For scientific claims, prefer:

1. systematic reviews and meta-analyses when appropriate;
2. strong primary study designs appropriate to the question;
3. validated methodological papers;
4. established theoretical sources;
5. other peer-reviewed evidence.

Evidence hierarchy must remain discipline-sensitive.

Do not assume RCTs are the highest evidence for every research question.

---

# 13. Recency Strategy

Use a combination of:

* recent literature;
* seminal literature.

For fast-moving fields:

prioritize recent evidence more heavily.

For mature theoretical fields:

older foundational literature may remain essential.

Do not impose one fixed publication window universally.

---

# 14. Default Recency Layers

When appropriate, divide literature into:

## Current

Recent literature defining the present field.

## Intermediate

Literature showing development.

## Foundational

Seminal or historically important sources.

The exact date boundaries should depend on field velocity.

---

# 15. Recent Literature Expansion

For current-evidence searches, emphasize:

* latest studies;
* recent systematic reviews;
* current methodological developments;
* newly published contradictory findings.

Do not rely solely on reviews when important primary evidence exists.

---

# 16. Seminal Literature Search

Seminal sources may be found through:

* highly recurring citations;
* theory origins;
* foundational methodological papers;
* backward citation chaining;
* expert-recognized landmark publications.

High citation count alone does not define seminal status.

---

# 17. Contradictory-Evidence Search

Every important evidence search should consider:

> What evidence might contradict the preferred interpretation?

Use search terms such as conceptually:

* no association;
* non-significant;
* conflicting;
* inconsistent;
* adverse;
* failed;
* replication;
* null;
* contradictory.

Do not mechanically rely only on negative keywords.

Also inspect reviews and citing studies for disagreement.

---

# 18. Competing-Theory Search

When theoretical claims matter, search for:

* competing theories;
* alternative mechanisms;
* alternative conceptualizations.

Do not build a theoretical framework using only supportive literature.

---

# 19. Competing-Method Search

When methodology is central, search for:

* alternative designs;
* validation studies;
* method comparison;
* sensitivity studies;
* methodological criticism.

Do not present one method as standard merely because it appears frequently.

---

# 20. Search Iteration

A good literature search is iterative.

Possible sequence:

```text
Initial Search
      ↓
Inspect Terminology
      ↓
Identify Missing Synonyms
      ↓
Refine Query
      ↓
Inspect Key Papers
      ↓
Citation Chaining
      ↓
Final Search Expansion
```

Do not assume the first query is sufficient.

---

# 21. Precision vs Recall

Balance:

`PRECISION`

and:

`RECALL`

Exploratory searches may favor recall.

Gap validation requires both:

* broad recall to avoid missing prior work;
* precise searches targeting the claimed gap.

Systematic reviews require explicit reproducible search logic.

---

# 22. Broad Search

Use broad search when:

* field boundaries are unclear;
* terminology is unstable;
* emerging topics are being explored;
* initial landscape mapping is required.

Avoid prematurely narrowing by:

* country;
* specific method;
* specific outcome;

unless those are scientifically essential.

---

# 23. Focused Search

Use focused searches for:

* specific research questions;
* gap validation;
* novelty validation;
* methodological justification;
* manuscript claims.

Focused search must remain broad enough to capture synonyms.

---

# 24. Gap-Validation Search

When supporting:

`gap-validator`

run multiple search formulations.

Search:

* exact proposed relationship;
* synonyms;
* broader terms;
* narrower terms;
* alternative terminology;
* related mechanisms;
* relevant population variants;
* adjacent disciplines.

One empty query result is never sufficient evidence of a research gap.

---

# 25. Novelty-Validation Search

For novelty assessment, actively search for the closest competing studies.

Ask:

> What paper is most similar to the proposed study?

Search combinations involving:

* same variables;
* same mechanism;
* same population;
* same methodology;
* same intervention;
* same outcome.

Novelty cannot be established by only searching the exact proposed title.

---

# 26. Continuation Search

When continuing previous research, search:

* previous article title;
* DOI;
* authors;
* main concepts;
* subsequent citing literature;
* replications;
* extensions;
* contradictory results.

Then assess how the field changed after the previous study.

---

# 27. Target-Journal Context Search

When a target journal is already known, relevant recent papers from that journal may be searched separately.

Purpose:

* understand scholarly conversation;
* assess methodological fit;
* identify relevant previous work;
* position the manuscript scientifically.

Do not allow target-journal searching to replace field-wide searching.

---

# 28. Target-Journal Citation Integrity

Never retrieve target-journal papers merely to increase citations to that journal.

A target-journal paper should be cited only when it contributes scientifically to:

* theory;
* methods;
* comparison;
* evidence;
* contradiction;
* interpretation.

No citation padding.

---

# 29. APC Independence

Article discovery must not be filtered based on APC.

A scientifically relevant paper remains relevant regardless of the journal's publication-cost model.

The preference for:

`NO_MANDATORY_APC`

belongs to:

* journal matching;
* publication strategy.

It must not bias evidence discovery.

---

# 30. Search by DOI

When a DOI is known:

* normalize it;
* verify metadata;
* use it to identify duplicates;
* use it for citation chaining when possible.

DOI absence does not automatically invalidate a legitimate scholarly article.

Older literature may legitimately lack a DOI.

---

# 31. DOI Normalization

Normalize DOI values by removing unnecessary forms such as:

* `https://doi.org/`
* `http://dx.doi.org/`
* `doi:`

Store canonical form where possible.

Example:

```text
10.xxxx/xxxxx
```

Do not alter the DOI itself.

---

# 32. Title Normalization

For deduplication, normalize titles carefully.

Possible normalization:

* lowercase comparison;
* punctuation normalization;
* whitespace normalization.

Do not modify the displayed bibliographic title unnecessarily.

---

# 33. Author Normalization

Author names may vary by:

* initials;
* ordering;
* diacritics;
* database representation.

Use DOI and title when possible to support deduplication.

Do not merge authors solely by similar names.

---

# 34. Duplicate Detection

Identify duplicates using combinations of:

1. DOI;
2. title;
3. authors;
4. year;
5. journal.

Possible status:

* `DUPLICATE_CONFIRMED`
* `POSSIBLE_DUPLICATE`
* `UNIQUE_RECORD`

Do not count duplicate database records as separate studies.

---

# 35. Preprints

Preprints may be discovered, especially in fast-moving fields.

Classify:

`PREPRINT`

Do not treat them as peer-reviewed literature.

Check whether a peer-reviewed version exists.

Prefer the peer-reviewed version when scientifically equivalent.

---

# 36. Conference Literature

Conference papers may be important in fields such as:

* computer science;
* engineering;
* technology.

Do not automatically exclude them.

Interpret evidence quality according to disciplinary norms.

---

# 37. Retracted Articles

When a source is known to be retracted:

classify:

`RETRACTED`

Do not use it as supporting evidence except when discussing:

* retraction;
* research integrity;
* historical context.

Pass retraction checking to downstream verification.

---

# 38. Corrected Articles

When important corrections or errata exist, preserve them.

Use:

* `CORRECTED`
* `ERRATUM_PRESENT`

where verified.

Do not silently cite outdated conclusions when corrections materially change them.

---

# 39. Language Strategy

Do not automatically limit searches to English if relevant evidence may exist in other languages.

However, international publication workflows may prioritize English-language peer-reviewed literature for broader comparability.

Record language restrictions when applied.

---

# 40. Geographic Search Strategy

Do not restrict geographically during initial searches unless geography is central to the research question.

For contextual research, use both:

## Global Search

to establish broader evidence.

## Context Search

to understand local or regional evidence.

This prevents false novelty based on local absence.

---

# 41. Search Logging

Every substantial search should record:

* database/provider;
* access mode;
* date searched;
* search objective;
* exact query or reproducible representation;
* filters;
* date range;
* result count when reliably available;
* notes.

This supports reproducibility.

---

# 42. Search Log Structure

Recommended:

```yaml
search_log:
  - provider:
    access_mode:
    date:
    purpose:
    query:
    filters:
    date_range:
    result_count:
    notes:
```

Do not fabricate result counts.

---

# 43. Search Coverage Status

Classify the search:

* `PRELIMINARY`
* `EXPANDED`
* `SUBSTANTIAL`
* `SYSTEMATIC`
* `UNKNOWN`

Do not describe a search as systematic unless it actually follows a systematic-review protocol.

---

# 44. Discovery Record

For every potentially relevant record, capture when available:

```yaml
title:
authors:
year:
journal:
doi:
issn:
publisher:
document_type:
abstract:
keywords:
provider:
source_url:
```

Then pass it to:

`source-verification`

---

# 45. Scopus Discovery Status

During discovery, use cautious status labels:

* `DIRECT_SCOPUS_RESULT`
* `DISCOVERED_REQUIRES_SCOPUS_VERIFICATION`
* `NON_SCOPUS_SOURCE_ALLOWED_BY_CONTEXT`
* `UNVERIFIED`

Do not use:

`SCOPUS_VERIFIED`

unless verification has actually occurred.

---

# 46. Search Result Ranking

Rank candidate records primarily by:

1. relevance to the research question;
2. evidence type;
3. methodological appropriateness;
4. recency when relevant;
5. foundational importance;
6. source verification status.

Do not rank solely by citation count or publisher reputation.

---

# 47. Relevance Classification

Use:

* `DIRECTLY_RELEVANT`
* `HIGHLY_RELEVANT`
* `SUPPORTING`
* `CONTEXTUAL`
* `MARGINALLY_RELEVANT`
* `IRRELEVANT`

Only retain marginal literature when it serves a specific purpose.

---

# 48. Search Stop Logic

A search may be sufficiently developed when:

* major terminology is covered;
* key themes recur consistently;
* recent relevant studies are captured;
* seminal literature is represented;
* contradictory evidence has been actively sought;
* repeated query expansion yields few new relevant concepts.

This is not equivalent to formal saturation in a systematic review.

---

# 49. Search Failure Recovery

If few relevant results are found:

1. broaden terminology;
2. remove unnecessary constraints;
3. search synonyms;
4. search broader concepts;
5. inspect references of relevant papers;
6. search adjacent disciplines;
7. check terminology changes;
8. search author names or research groups when justified.

Do not conclude:

"No research exists"

from one failed query.

---

# 50. False-Gap Prevention

Before any downstream gap claim, ensure that searches considered:

* synonyms;
* alternate spelling;
* historical terminology;
* conceptual equivalents;
* related populations;
* adjacent disciplines;
* forward citations;
* recent publications.

This is a mandatory safeguard.

---

# 51. Search Bias Prevention

Actively avoid:

* confirmation bias;
* prestige bias;
* publisher bias;
* recency bias;
* citation-count bias;
* geography bias;
* English-only bias when inappropriate;
* target-journal bias.

Searches should represent the scientific field rather than the preferred conclusion.

---

# 52. Evidence Diversity

Where scientifically relevant, retrieve multiple evidence types:

* systematic review;
* meta-analysis;
* experimental study;
* observational study;
* qualitative study;
* methodological study;
* validation study.

Do not mechanically require every type.

---

# 53. Search Output

When presenting a search result set, organize it by scientific function rather than providing an unstructured list.

Possible sections:

## Core Evidence

Directly addresses the research question.

## Recent Evidence

Defines the current field.

## Foundational Evidence

Provides historical or theoretical foundations.

## Contradictory Evidence

Challenges dominant interpretations.

## Methodological Evidence

Supports research design or analysis.

## Emerging Evidence

Represents newly developing work.

---

# 54. Minimum Search Record Table

When useful:

| Study | Year | Journal | DOI | Relevance | Evidence Role | Scopus Status |
| ----- | ---: | ------- | --- | --------- | ------------- | ------------- |

Do not display verified status unless verification has occurred.

Use:

`UNVERIFIED`

when necessary.

---

# 55. Search Output Is Not Evidence Synthesis

Do not turn retrieval directly into conclusions.

Conceptual workflow:

```text
Search
   ↓
Verification
   ↓
Screening
   ↓
Synthesis
   ↓
State of the Art
   ↓
Gap / Novelty
```

Each stage has separate responsibilities.

---

# 56. Relationship with Source Verification

`scopus-literature-search` discovers records.

`source-verification` determines whether:

* bibliographic metadata are accurate;
* publication exists;
* DOI is valid;
* peer-review status is credible;
* source is legitimate;
* Scopus status can be verified.

Do not duplicate detailed verification here.

---

# 57. Relationship with Reference Integrity Guard

`reference-integrity-guard` later prevents:

* fabricated references;
* metadata mashups;
* wrong DOI;
* title-author mismatches;
* duplicate references;
* unsupported Scopus claims.

This skill must preserve enough metadata for that process.

---

# 58. Relationship with Citation Chaining

`citation-chaining` expands from key articles using:

* backward references;
* forward citations;
* related-paper networks.

Use it after initial anchor papers have been identified.

---

# 59. Relationship with Literature Screening

`literature-screening` determines whether discovered records should be included for a specific analytical purpose.

Search retrieval is not final inclusion.

---

# 60. Relationship with Evidence Synthesis

`evidence-synthesis` integrates verified and screened evidence across studies.

Do not synthesize from unverified snippets.

---

# 61. Research Passport Update

When supported, update:

```yaml
literature:
  search_mode:
  scopus_access_mode:
  search_objective:
  concept_blocks:
  synonyms:
  databases:
  search_logs:
  records_discovered:
  current_sources:
  foundational_sources:
  contradictory_sources:
  methodological_sources:
  emerging_sources:
  scopus_verification_pending:
  search_coverage:
  next_stage:
```

Unknown values remain unknown.

---

# 62. User-Friendly Behavior

Do not burden the user with database syntax unless needed.

For example:

Instead of:

> You must create TITLE-ABS-KEY Boolean queries.

Prefer:

> I will first translate your topic into several concept groups and synonyms so the search does not miss studies that use different terminology.

When useful, expose the reproducible query afterward.

---

# 63. Do Not Fabricate Search Activity

Never say:

* "Scopus returned 218 articles"
* "I searched Scopus"
* "This article is Scopus indexed"

unless those actions or facts were actually verified.

If direct Scopus access is unavailable, say so through the appropriate workflow state and use legitimate fallback discovery.

---

# 64. Do Not Fabricate References

Never generate plausible-looking:

* titles;
* authors;
* journals;
* DOIs;
* volumes;
* pages.

A reference that cannot be verified must not enter the verified evidence set.

---

# 65. No Vibe Citing

Never construct a reference by combining:

* title from one paper;
* authors from another;
* DOI from another;
* journal metadata from another.

Metadata components must belong to the same verified scholarly record.

---

# 66. Unverified Reference Rule

If a reference cannot be verified:

use:

`REFERENCE_UNVERIFIED`

and exclude it from final evidence-dependent claims until resolved.

Do not downgrade uncertainty into silent acceptance.

---

# 67. Research Integrity Rule

Search completeness is less important than fabricated certainty.

It is acceptable to state:

> I could not verify this source.

It is not acceptable to invent missing bibliographic information.

---

# Stop Conditions

Do not proceed as if literature discovery is adequate when:

* major terminology remains unresolved;
* search coverage is clearly narrow;
* only supportive evidence was retrieved;
* key records remain unverifiable;
* the claimed gap depends on one empty search;
* Scopus status is being assumed rather than checked.

Identify what search expansion or verification remains necessary.

---

# Success Criterion

`scopus-literature-search` succeeds when the framework has produced a transparent, reproducible, sufficiently broad, relevance-focused scholarly literature corpus that prioritizes Scopus-indexed evidence, preserves metadata and provenance, includes contradictory and foundational evidence, and is ready for rigorous source verification without fabricating access, indexing status, or references.
