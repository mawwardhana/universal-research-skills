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
  anchor_id:
  title:
  authors:
  year:
  journal:
  doi:
  pmid:
  scopus_source_status:
  scopus_document_status:
  evidence_role:
  study_design:
  population:
  topic:
  method:
  theory:
  verification_status:
  retraction_status:
  notes:
```

Do not fabricate unavailable fields.

Unknown values remain unknown.

---

# 3. Anchor Eligibility Gate

Before deep chaining, determine whether the proposed anchor is sufficiently reliable.

Possible outcomes:

- `ANCHOR_VERIFIED`
- `ANCHOR_VERIFIED_WITH_LIMITATION`
- `ANCHOR_REQUIRES_SOURCE_VERIFICATION`
- `ANCHOR_REQUIRES_REFERENCE_INTEGRITY_CHECK`
- `ANCHOR_RETRACTED_BLOCK`
- `ANCHOR_IDENTITY_UNRESOLVED`

Preferred upstream sequence:

```text
source-verification
      ↓
reference-integrity-guard
      ↓
citation-chaining
```

Do not build a large citation network from an unresolved anchor identity.

---

# 4. Anchor Scientific Role

Classify each anchor by scientific role.

Possible roles include:

- `SEMINAL`
- `FOUNDATIONAL`
- `THEORY_ORIGIN`
- `METHOD_ORIGIN`
- `INSTRUMENT_ORIGIN`
- `PRIMARY_EMPIRICAL`
- `VALIDATION`
- `REPLICATION`
- `CONTRADICTORY`
- `SYSTEMATIC_REVIEW`
- `META_ANALYSIS`
- `RECENT_FRONTIER`
- `PREVIOUS_RESEARCH_OUTPUT`
- `CLOSEST_COMPETITOR`

Scientific role determines which chaining direction is most useful.

---

# 5. Multi-Anchor Strategy

Do not rely on a single anchor when the research question spans multiple scientific streams.

Potential anchor set:

```text
Seminal Anchor
      +
Recent Frontier Anchor
      +
Method Anchor
      +
Contradictory Anchor
      +
Closest Competitor
```

Use multiple anchors to reduce lineage bias.

---

# 6. Anchor Diversity

When feasible, diversify anchors across:

- time;
- research group;
- geography;
- theoretical tradition;
- methodological tradition;
- outcome definition;
- population;
- disciplinary perspective.

Do not deliberately select only papers supporting the preferred narrative.

---

# 7. Backward Citation Chaining

Backward chaining explores references cited by the anchor.

Primary purposes include:

- finding foundational studies;
- locating original theory;
- recovering original methods;
- tracing instrument development;
- identifying prior competing explanations;
- discovering earlier terminology.

Conceptually:

```text
Anchor Paper
      ↓
Reference List
      ↓
Earlier Scientific Lineage
```

---

# 8. Backward-Chaining Question

For each potentially relevant cited source ask:

> Why did the anchor cite this source, and does the earlier source materially help explain the scientific lineage of the current research problem?

A citation in the anchor does not automatically make the cited source relevant.

---

# 9. Original-Source Recovery

When an anchor cites a secondary source for a foundational idea, attempt to recover the original source.

Preferred direction:

```text
secondary citation
      ↓
original source
      ↓
source-verification
```

Do not attribute an idea to the secondary source when the original source is known and available.

---

# 10. Seminal Source Identification

A seminal source may be identified because it:

- introduced a theory;
- first formalized a construct;
- developed a method;
- validated an instrument;
- reported a foundational empirical result;
- changed the direction of a field.

High citation count alone does not prove seminal status.

---

# 11. Historical Lineage Guard

Older literature may use terminology different from current terminology.

Record legacy terms when discovered.

Example:

```yaml
terminology_lineage:
  current_term:
  historical_terms:
    - term:
      period:
      source:
  notes:
```

Use these terms to improve later database searching.

---

# 12. Forward Citation Chaining

Forward chaining explores publications that cite the anchor.

Primary purposes include:

- tracking subsequent developments;
- locating replications;
- identifying extensions;
- discovering criticisms;
- mapping methodological refinements;
- locating recent competing models;
- identifying current frontier studies.

Conceptually:

```text
Anchor Paper
      ↓
Citing Literature
      ↓
Subsequent Scientific Development
```

---

# 13. Forward-Chaining Question

For every citing paper ask:

> What scientific relationship does this paper actually have to the anchor?

Do not treat citation as agreement.

---

# 14. Citation Relationship Classification

Possible relationships include:

- `SUPPORTS`
- `REPLICATES`
- `PARTIALLY_REPLICATES`
- `FAILS_TO_REPLICATE`
- `EXTENDS`
- `REFINES`
- `APPLIES`
- `VALIDATES`
- `CRITIQUES`
- `CONTRADICTS`
- `REINTERPRETS`
- `USES_METHOD`
- `USES_INSTRUMENT`
- `USES_THEORY`
- `MENTIONS_ONLY`
- `BACKGROUND_ONLY`
- `RELATIONSHIP_UNCLEAR`

---

# 15. Citation Relationship Record

Use:

```yaml
citation_relationship:
  anchor_id:
  candidate_id:
  direction:
  relationship:
  scientific_topic:
  shared_population:
  shared_method:
  shared_theory:
  shared_outcome:
  relevance:
  verification_status:
  notes:
```

---

# 16. Citation Context Integrity

A citation's meaning should be interpreted from citation context when available.

A paper may cite an anchor:

- positively;
- neutrally;
- critically;
- only in background;
- only for method;
- only for a definition.

Do not infer the citation relationship from bibliographic linkage alone.

---

# 17. Forward Citation Date Guard

The citing publication must logically postdate the cited work, except for metadata anomalies or online-first timing.

Flag impossible chronology for verification.

Use:

`CITATION_DATE_CONFLICT`

when needed.

---

# 18. Bidirectional Chaining

Use `BIDIRECTIONAL` mode when both historical lineage and subsequent development matter.

Conceptually:

```text
Earlier Literature
        ↑
        │
   Anchor Paper
        │
        ↓
Later Literature
```

This is often useful for:

- State of the Art;
- gap validation;
- novelty auditing;
- continuation of previous studies.

---

# 19. Iterative Snowballing

Citation chaining may proceed through multiple generations.

Example:

```text
Anchor
  ↓
Generation 1
  ↓
Generation 2
  ↓
Generation 3
```

Do not expand indefinitely.

Use relevance and saturation criteria.

---

# 20. Generation Record

Record:

```yaml
citation_generation:
  generation:
  parent_reference:
  candidate_reference:
  direction:
  relationship:
  retained:
  exclusion_reason:
```

---

# 21. Chaining Depth

Possible depth settings:

- `ONE_GENERATION`
- `TWO_GENERATIONS`
- `UNTIL_SATURATION`
- `TARGETED_DEPTH`
- `FRONTIER_ONLY`
- `FOUNDATIONAL_ONLY`

Choose depth according to the objective.

---

# 22. Chaining Breadth

Possible breadth settings:

- `NARROW`
- `MODERATE`
- `BROAD`
- `SYSTEMATIC`

Do not call a broad exploratory chain systematic unless systematic procedures were actually used.

---

# 23. Stop Rule

Stop chaining when one or more defensible criteria are reached.

Possible stop conditions:

- conceptual saturation;
- no new relevant terminology;
- no new close competitors;
- no new contradictions;
- no new methodological lineage;
- pre-specified generation depth;
- pre-specified date boundary;
- purpose-specific evidence sufficiency.

---

# 24. Saturation Definition

Citation-chain saturation means:

> Additional citation expansion is no longer producing materially new evidence relevant to the defined scientific objective.

It does not mean every paper in the field has been found.

---

# 25. Related-Paper Expansion

`RELATED_PAPER` mode may use:

- bibliographic coupling;
- co-citation;
- shared references;
- semantic similarity;
- related-article systems.

Relatedness is a discovery signal, not proof of scientific relevance.

---

# 26. Bibliographic Coupling

Two papers are bibliographically coupled when they share cited references.

Use this to identify:

- parallel research streams;
- conceptually related work;
- competing studies;
- papers using common theory or methods.

Do not infer agreement from coupling.

---

# 27. Co-Citation

Two sources are co-cited when later literature cites them together.

Co-citation may reveal:

- influential conceptual pairs;
- competing theoretical traditions;
- common methodological foundations;
- clusters within a field.

Co-citation frequency is not evidence quality.

---

# 28. Citation Network Cluster

Possible cluster record:

```yaml
citation_cluster:
  cluster_id:
  dominant_topic:
  dominant_method:
  dominant_theory:
  key_sources:
  contradictory_sources:
  time_period:
  interpretation:
```

Do not force clusters when the evidence does not support them.

---

# 29. Author-Lineage Mode

`AUTHOR_LINEAGE` explores relevant research by key authors or research groups.

Useful when:

- an author has developed a sustained program;
- a method or theory evolved across multiple papers;
- a cohort generated multiple reports.

Do not treat all publications by the same author as relevant.

---

# 30. Author-Identity Guard

Similar names do not prove author identity.

Use verified identifiers when available:

- ORCID;
- affiliation;
- coauthor network;
- field;
- publication history.

Do not merge authors based only on initials.

---

# 31. Research-Group Bias Guard

A field may appear more consistent when citation chaining remains inside one research group.

Actively look for:

- independent replications;
- competing groups;
- external validations;
- criticisms.

---

# 32. Method-Lineage Mode

`METHOD_LINEAGE` traces:

- original method;
- methodological modifications;
- validation studies;
- comparison studies;
- application studies;
- known limitations.

Preferred chain:

```text
Method Origin
      ↓
Validation
      ↓
Refinement
      ↓
Current Application
```

---

# 33. Instrument Lineage

For measurement instruments trace:

- original development;
- translation;
- adaptation;
- validation;
- reliability;
- measurement invariance;
- population-specific performance.

Do not cite an adaptation as the original instrument source.

---

# 34. Theory-Lineage Mode

`THEORY_LINEAGE` traces:

- original formulation;
- major refinements;
- competing theories;
- boundary conditions;
- empirical tests;
- critiques;
- current forms.

Route formal theoretical synthesis to:

`theoretical-framework`

when needed.

---

# 35. Theory-Origin Guard

Do not attribute a theory to a later review simply because it explains the theory clearly.

Recover original or seminal sources when possible.

---

# 36. Continuation Search Mode

`CONTINUATION_SEARCH` is especially useful when the researcher provides a previous article, thesis, dissertation, or project.

Conceptually:

```text
Previous Research
      ↓
Who cited it?
      ↓
What happened next?
      ↓
What remained unresolved?
      ↓
What can be continued?
```

---

# 37. Previous-Research Anchor

When the researcher's previous work is the anchor, do not assume it is the most important paper in the field.

Use it as one entry point.

Combine with independent external anchors.

---

# 38. Continuation Evidence Record

Use:

```yaml
continuation_evidence:
  previous_output:
  subsequent_citing_studies:
  direct_replications:
  extensions:
  contradictions:
  unresolved_issues:
  closest_new_competitors:
  possible_continuation:
```

---

# 39. Replication Search Mode

`REPLICATION_SEARCH` seeks evidence testing whether a prior result is reproducible or generalizable.

Look for:

- direct replication;
- conceptual replication;
- external validation;
- cross-population replication;
- temporal replication;
- method replication.

---

# 40. Replication Classification

Possible classes:

- `DIRECT_REPLICATION`
- `CONCEPTUAL_REPLICATION`
- `EXTERNAL_VALIDATION`
- `PARTIAL_REPLICATION`
- `FAILED_REPLICATION`
- `NOT_A_REPLICATION`

Do not label a merely similar study as replication.

---

# 41. Replication Independence

Check whether the apparent replication uses:

- the same cohort;
- overlapping participants;
- the same database;
- the same research group;
- an independent sample.

Use:

`INDEPENDENT_REPLICATION`

only when defensible.

---

# 42. Contradiction Search Mode

`CONTRADICTION_SEARCH` actively seeks evidence that challenges the anchor.

Possible signals:

- opposite direction;
- null result;
- failed replication;
- methodological criticism;
- alternative mechanism;
- competing theory;
- population-specific reversal.

---

# 43. Contradiction Is Not Error

Contradictory evidence may reflect:

- different populations;
- different measurement;
- different exposure levels;
- different follow-up;
- different methods;
- genuine heterogeneity.

Do not automatically decide one study is wrong.

---

# 44. Contradiction Record

Use:

```yaml
contradiction:
  anchor:
  contrasting_source:
  issue:
  direction:
  population_difference:
  method_difference:
  outcome_difference:
  possible_explanation:
  verification_status:
```

---

# 45. Negative-Citation Search

Search for citation contexts containing scientific challenge language when feasible.

Potential signals:

- "however";
- "failed to replicate";
- "contrary to";
- "inconsistent with";
- "limitations";
- "questioned";
- "did not confirm".

These are discovery signals only.

Read context before classification.

---

# 46. Novelty Stress-Test Mode

`NOVELTY_STRESS_TEST` searches citation networks around the closest competitors.

Purpose:

> Find prior work that could defeat or narrow the proposed novelty claim.

Preferred route:

```text
closest competitor
      ↓
backward chaining
      +
forward chaining
      +
related papers
      ↓
novelty-auditor
```

---

# 47. Novelty Competitor Record

Use:

```yaml
novelty_competitor:
  reference:
  relationship_to_proposed_study:
  same_population:
  same_construct:
  same_method:
  same_mechanism:
  same_outcome:
  key_difference:
  threat_to_novelty:
```

---

# 48. Gap Validation Chaining

For a candidate gap:

```text
Candidate Gap
      ↓
Key Supporting Papers
      ↓
Citation Chaining
      ↓
Latest Citing Literature
      ↓
Adjacent Terminology
      ↓
Gap Still Open?
```

Route final adversarial assessment to:

`gap-validator`

---

# 49. Gap Closure Detection

Citation chaining should actively detect whether a supposed gap was already addressed.

Possible outcomes:

- `GAP_STILL_OPEN`
- `GAP_PARTIALLY_ADDRESSED`
- `GAP_SUBSTANTIALLY_RESOLVED`
- `GAP_REQUIRES_REFRAMING`
- `INCONCLUSIVE`

Do not validate the gap here.

Pass evidence onward.

---

# 50. State-of-the-Art Chaining

For SoTA, chaining can identify:

- foundational studies;
- established streams;
- recent refinements;
- contested findings;
- frontier studies;
- emerging methods.

Route synthesis to:

`sota-builder`

---

# 51. Evidence-Synthesis Chaining

Citation chaining discovers candidate evidence.

It does not itself perform final evidence synthesis.

Preferred route:

```text
citation-chaining
      ↓
source-verification
      ↓
reference-integrity-guard
      ↓
literature-screening
      ↓
evidence-synthesis
```

New discoveries must re-enter verification.

---

# 52. Candidate Source Status

Use:

- `DISCOVERED`
- `VERIFICATION_PENDING`
- `VERIFIED`
- `INTEGRITY_CLEARED`
- `SCREENING_PENDING`
- `INCLUDED`
- `EXCLUDED`

Do not call a newly discovered citation "included evidence."

---

# 53. Candidate Record

Use:

```yaml
candidate:
  candidate_id:
  discovered_from:
  discovery_mode:
  title:
  authors:
  year:
  journal:
  doi:
  relationship_to_anchor:
  relevance:
  verification_status:
  integrity_status:
  screening_status:
  notes:
```

---

# 54. Discovery Provenance

Every chained source should preserve provenance.

Example:

```text
Anchor A
  ↓ forward citation
Paper B
  ↓ backward citation
Paper C
```

Record enough information to reconstruct why the candidate entered the corpus.

---

# 55. Provenance Record

Use:

```yaml
provenance:
  candidate_id:
  parent_id:
  anchor_id:
  direction:
  generation:
  discovery_platform:
  discovery_date:
  query_or_relation:
```

Do not fabricate provider information.

---

# 56. Source Verification Loop

Every materially important newly discovered source should route through:

`source-verification`

Citation linkage does not verify identity.

---

# 57. Reference Integrity Loop

After source identity is verified, route important references through:

`reference-integrity-guard`

before using them to support:

- claims;
- gaps;
- novelty;
- theory;
- methods;
- discussion.

---

# 58. Retraction Guard

If an anchor or candidate is retracted:

- do not use it as valid scientific evidence;
- investigate whether later literature cites it critically or historically;
- identify corrected or replacement evidence.

Possible status:

`RETRACTED_SOURCE_NETWORK_CONTEXT_ONLY`

---

# 59. Correction Guard

If a source has an erratum or correction:

verify whether the correction affects the scientific relationship being traced.

---

# 60. Duplicate Guard

Citation networks may surface the same paper through multiple paths.

Deduplicate using:

- DOI;
- title;
- authors;
- year;
- journal;
- persistent identifier.

Do not count repeated discovery as independent evidence.

---

# 61. Study-Family Guard

Multiple publications may arise from one cohort or study.

Do not interpret:

```text
five publications
```

as:

```text
five independent studies
```

when they belong to one study family.

Route study-family integrity questions to:

`reference-integrity-guard`

---

# 62. Conference-to-Journal Duplication

A conference abstract and later journal article may represent the same study.

Prefer the more complete scientifically appropriate version where available.

Do not double-count.

---

# 63. Preprint-to-Publication Duplication

A preprint and journal article may represent versions of the same work.

Track version relationships.

Prefer the version of record when appropriate.

---

# 64. Database Search Complement

Citation chaining should complement:

`scopus-literature-search`

Preferred comprehensive logic:

```text
keyword search
      +
citation chaining
      +
verification
      ↓
screened corpus
```

---

# 65. Scopus-First Principle

When scholarly literature is being discovered, prefer Scopus as the primary structured discovery source when available.

But never claim:

> "Scopus was searched"

unless Scopus was actually searched.

---

# 66. Discovery Fallbacks

When direct Scopus access is unavailable, possible discovery aids may include:

- OpenAlex;
- Crossref;
- PubMed;
- Semantic Scholar;
- publisher pages;
- citation indexes;
- verified search-engine results.

Label the actual discovery source.

---

# 67. Google Scholar Guard

Google Scholar can be useful for citation discovery but may have:

- opaque indexing;
- duplicate records;
- non-peer-reviewed results;
- unstable citation counts.

Do not treat Google Scholar citation count as a scientific quality metric.

---

# 68. PubMed Citation Context

PubMed-related tools may assist discovery in biomedical fields.

Coverage differs by discipline.

Do not assume PubMed represents the full scholarly universe outside its scope.

---

# 69. Crossref Guard

Crossref is valuable for metadata and DOI relationships.

It is not a complete citation database for every field.

---

# 70. OpenAlex Guard

OpenAlex may provide useful citation graph relationships.

Treat graph linkage as discovery evidence that still requires source verification.

---

# 71. Semantic Similarity Guard

Semantic similarity may surface papers with no direct citation relationship.

Classify them as:

`RELATED_DISCOVERY`

rather than backward or forward citations.

---

# 72. Citation Count Guard

Citation count may help prioritize inspection.

It must not decide:

- scientific validity;
- inclusion;
- evidence strength;
- novelty;
- causal credibility.

---

# 73. Recent Literature Priority

For fast-moving fields, forward chaining from recent anchors can reveal studies newer than classical review papers.

Use recency purposefully.

Do not exclude older foundational literature merely because it is old.

---

# 74. Temporal Layering

A useful citation lineage may be organized as:

```text
Foundational
      ↓
Developmental
      ↓
Consolidation
      ↓
Contestation
      ↓
Current Frontier
```

This may feed:

`sota-builder`

---

# 75. Frontier Detection

Potential frontier signals include:

- recent high-relevance citing studies;
- new mechanism;
- new method;
- new population;
- independent replication;
- unresolved contradiction;
- emerging terminology.

Frontier status requires scientific assessment, not recency alone.

---

# 76. Emerging Topic Guard

Citation bursts or new clusters can indicate emerging activity.

Route formal emerging-topic analysis to:

`emerging-topic-discovery`

Do not equate citation burst with proven importance.

---

# 77. Trend Guard

Citation-network growth may complement:

`trend-detection`

But publication/citation volume does not alone establish scientific consensus.

---

# 78. Adjacent Discipline Expansion

Citation chains may cross disciplinary boundaries.

This can reveal:

- alternative terminology;
- analogous mechanisms;
- methods imported from another field;
- competing explanatory frameworks.

Do not broaden indefinitely.

Keep connection to the research question explicit.

---

# 79. Terminology Expansion

Every meaningful synonym or historical term discovered through chaining may update later search strings.

Record:

```yaml
terminology_expansion:
  term:
  source:
  relationship:
  use_in_search:
```

---

# 80. Concept Drift Guard

A term may change meaning over time or across disciplines.

Do not assume identical terminology means identical construct.

---

# 81. Construct Equivalence Guard

Before linking evidence across constructs, ask whether they are:

- identical;
- overlapping;
- nested;
- related but distinct;
- terminologically similar only.

Route conceptual questions to:

`conceptual-framework`

when needed.

---

# 82. Method Equivalence Guard

Different methods may operationalize the same scientific question.

Do not reject relevant literature solely because the exact software or analytical label differs.

This is especially important for gap validation.

---

# 83. Mechanism Equivalence Guard

Two studies may test conceptually equivalent mechanisms using different terminology.

Use citation chaining to recover hidden conceptual links.

Do not overmerge genuinely different mechanisms.

---

# 84. Population Generalization Guard

A citing paper in a different population may represent:

- extension;
- external validation;
- context-specific test;
- not a direct replication.

Classify accurately.

---

# 85. Geographic Expansion

Geographic differences may be scientifically important.

Record when relevant:

- country;
- region;
- healthcare system;
- educational system;
- culture;
- regulatory environment.

Do not treat new geography alone as strong novelty without substantive contribution.

---

# 86. Language Bias Guard

Citation networks can be biased toward English-language literature.

When relevant and feasible, consider non-English sources.

Do not claim language-comprehensive coverage unless it occurred.

---

# 87. Publication Bias Awareness

Highly visible citation networks may underrepresent:

- null findings;
- failed replications;
- negative studies;
- local journals;
- unpublished evidence.

Citation chaining cannot eliminate publication bias.

---

# 88. Self-Citation Guard

Author or research-group self-citation can inflate apparent lineage continuity.

Do not treat self-citation as independent validation.

---

# 89. Citation Cartel Guard

Unusual reciprocal citation patterns should not be interpreted as evidence strength.

Citation-network prominence and scientific validity are separate.

---

# 90. Review-Article Anchor Guard

Systematic reviews can be efficient anchors.

But their reference lists reflect:

- search dates;
- eligibility criteria;
- review scope.

Use forward chaining to update beyond the review date.

---

# 91. Narrative Review Guard

Narrative reviews may provide useful conceptual maps.

Do not assume comprehensive coverage.

Use them as discovery aids, not automatic evidence maps.

---

# 92. Meta-Analysis Anchor

A meta-analysis may help identify:

- primary studies;
- heterogeneity;
- moderators;
- publication-bias concerns.

Forward chaining can identify later studies after the meta-analysis search date.

---

# 93. Guideline Anchor

Clinical or policy guidelines may cite major evidence streams.

Use them carefully for discovery.

A guideline's citation hierarchy reflects its purpose and date.

---

# 94. Method Paper Anchor

Method papers may have large citation networks across unrelated application domains.

Filter by scientific relevance.

Do not inspect every citing application.

---

# 95. Theory Paper Anchor

Theory papers may be cited in many superficial contexts.

Prioritize citations that:

- test;
- refine;
- criticize;
- compare;
- extend

the theory.

---

# 96. Highly Cited Anchor Guard

A highly cited anchor can produce an unmanageable network.

Use targeted filters:

- date;
- field;
- citation context;
- method;
- population;
- relationship type.

---

# 97. Low-Cited Anchor Guard

Low citation count does not imply low relevance.

Recent, niche, regional, or highly specialized studies may be critical.

---

# 98. Citation Network Sampling

When networks are very large, sample transparently according to scientific purpose.

Possible strategies:

- newest relevant citing papers;
- closest conceptual matches;
- independent replications;
- critiques;
- methodological extensions;
- major review updates.

Do not call purposive sampling comprehensive.

---

# 99. Systematic Chaining Requirements

If citation chaining is part of a systematic review, record at minimum:

- anchor set;
- chaining direction;
- platforms;
- dates;
- generations;
- inclusion rules;
- deduplication;
- screening process.

Use transparent reproducible procedures.

---

# 100. Systematic Review Handoff

For systematic-review workflows, discovered candidates should route to:

`literature-screening`

Do not include them automatically.

---

# 101. Chaining Search Log

Use:

```yaml
chaining_log:
  date:
  anchor_id:
  mode:
  platform:
  direction:
  generation:
  candidates_found:
  candidates_retained_for_verification:
  notes:
```

Do not fabricate counts.

---

# 102. Candidate Exclusion Reasons

Possible discovery-stage exclusion reasons:

- `OFF_TOPIC`
- `WRONG_POPULATION`
- `WRONG_METHOD_RELATIONSHIP`
- `MENTION_ONLY`
- `DUPLICATE`
- `SAME_STUDY_FAMILY`
- `RETRACTED`
- `UNRESOLVED_IDENTITY`
- `NOT_RELEVANT_TO_OBJECTIVE`

Purpose-specific formal screening belongs to:

`literature-screening`

---

# 103. Mention-Only Citation Guard

A paper may cite an anchor only in a long background list.

Do not classify it as scientific continuation without evidence.

Use:

`MENTION_ONLY`

---

# 104. Method-Use Citation

A paper may cite an anchor only for a method.

Classify:

`USES_METHOD`

This can be useful for method lineage but not necessarily for topic continuation.

---

# 105. Instrument-Use Citation

A paper may cite an anchor only because it uses an instrument.

This is not necessarily evidence supporting the anchor's empirical conclusions.

---

# 106. Theory-Use Citation

A citing paper may adopt a theory without testing it.

Distinguish:

- `USES_THEORY`
- `TESTS_THEORY`
- `REFINES_THEORY`
- `CRITIQUES_THEORY`

---

# 107. Data-Source Citation

A paper may cite a dataset or registry.

Do not interpret data-source citation as empirical support.

---

# 108. Software Citation

Software citations usually indicate tool use.

Do not treat them as scientific replication.

---

# 109. Protocol Citation

A later result paper may cite a study protocol.

Link protocol and result publication when they belong to the same study family.

---

# 110. Citation Chain Graph

A conceptual graph may use:

```text
[Seminal Theory]
      ↓
[Anchor Study]
   ↙       ↘
[Replication] [Critique]
      ↓          ↓
[Extension] [Alternative Model]
```

Do not create graph edges that are not supported by real citation or scientific relationships.

---

# 111. Graph Node Types

Possible nodes:

- article;
- review;
- theory;
- method;
- instrument;
- dataset;
- guideline;
- protocol;
- conference paper.

Use type labels when relevant.

---

# 112. Graph Edge Types

Possible edges:

- cites;
- supports;
- replicates;
- extends;
- contradicts;
- critiques;
- validates;
- uses method;
- uses theory;
- shares cohort.

Do not infer non-citation scientific edges without evidence.

---

# 113. Graph Interpretation Guard

Network centrality does not prove:

- truth;
- methodological rigor;
- causal validity;
- novelty.

Use network structure for discovery and intellectual mapping only.

---

# 114. Cluster Dominance Guard

A large citation cluster may reflect:

- popularity;
- disciplinary size;
- indexing coverage;
- self-reinforcement.

Do not equate size with scientific superiority.

---

# 115. Bridge Paper Detection

A bridge paper connects previously separate research streams.

Bridge papers may be useful for:

- interdisciplinary synthesis;
- new terminology;
- method transfer;
- emerging concepts.

Verify scientific relevance.

---

# 116. Isolated Evidence

A scientifically important paper may be weakly connected in citation networks.

Do not discard isolated papers merely because network centrality is low.

---

# 117. Citation Lag

New papers may have few citations simply because they are recent.

Do not use citation count to filter out recent frontier studies.

---

# 118. Citation Obsolescence

Older highly cited papers may have been superseded.

Use forward chaining to identify:

- corrections;
- updated methods;
- newer evidence;
- failed replications.

---

# 119. Supersession Record

Use:

```yaml
supersession:
  earlier_source:
  later_source:
  reason:
  replacement_type:
  evidence:
```

Do not declare supersession solely because a later paper exists.

---

# 120. Correction of Scientific Lineage

If citation chaining reveals that the assumed origin of an idea was wrong:

update the lineage transparently.

Do not preserve an inaccurate historical narrative for convenience.

---

# 121. Closest Competitor Detection

For novelty work, prioritize papers sharing the greatest overlap in:

- question;
- population;
- construct;
- mechanism;
- method;
- outcome;
- contribution.

Route to:

`novelty-auditor`

for final comparison.

---

# 122. Competitor Proximity Matrix

Use:

| Candidate | Question | Population | Method | Mechanism | Outcome | Novelty Threat |
|---|---:|---:|---:|---:|---:|---:|

Qualitative judgments should be explained.

---

# 123. Gap Threat Matrix

Use:

| Candidate | Addresses Gap? | Direct/Indirect | Publication Date | Verification | Gap Threat |
|---|---|---|---|---|---|

---

# 124. Contradiction Matrix

Use:

| Source | Relationship | Direction | Key Difference | Possible Explanation |
|---|---|---|---|---|

---

# 125. Replication Matrix

Use:

| Source | Replication Type | Independent Sample | Population | Result | Verification |
|---|---|---|---|---|---|

---

# 126. Theory Lineage Matrix

Use:

| Source | Role | Original/Refinement/Critique | Boundary Condition | Current Relevance |
|---|---|---|---|---|

---

# 127. Method Lineage Matrix

Use:

| Source | Method Role | Validation | Modification | Limitation | Current Use |
|---|---|---|---|---|---|

---

# 128. Temporal Development Matrix

Use:

| Period | Key Source | Scientific Development | Evidence Status |
|---|---|---|---|

---

# 129. Citation Chaining Passport

Use when useful:

```yaml
citation_chaining:
  objective:
  anchor_count:
  modes:
  platforms:
  generations:
  start_date:
  end_date:
  discovered_candidates:
  verified_candidates:
  retained_candidates:
  contradictions_found:
  replications_found:
  closest_competitors_found:
  terminology_expansions:
  saturation_status:
  unresolved_items:
  next_stage:
```

Do not fabricate counts.

---

# 130. Chaining Status

Possible workflow statuses:

- `NOT_STARTED`
- `ANCHOR_VERIFICATION_REQUIRED`
- `CHAINING_IN_PROGRESS`
- `VERIFICATION_IN_PROGRESS`
- `SCREENING_REQUIRED`
- `SATURATION_NOT_REACHED`
- `PURPOSE_SATURATION_REACHED`
- `READY_FOR_SYNTHESIS`
- `READY_FOR_GAP_VALIDATION`
- `READY_FOR_NOVELTY_AUDIT`

---

# 131. Objective-Specific Readiness

For SoTA:

`READY_FOR_SOTA_SYNTHESIS`

For gap validation:

`READY_FOR_GAP_VALIDATION`

For novelty:

`READY_FOR_NOVELTY_AUDIT`

For continuation:

`READY_FOR_CONTINUATION_ASSESSMENT`

Do not use these statuses if major relevant citation branches remain unexplored.

---

# 132. Search Completeness Guard

Citation chaining cannot prove absolute literature completeness.

Use calibrated wording such as:

> Citation chaining did not identify additional directly relevant studies within the defined search scope.

Avoid:

> No other studies exist.

---

# 133. Absence Claim Guard

If chaining appears to support an absence claim, validate with database searching.

Preferred route:

```text
citation-chaining
      +
scopus-literature-search
      ↓
gap-validator
```

---

# 134. Novelty Claim Guard

Citation chaining can challenge novelty but should not independently certify it.

Route to:

`novelty-auditor`

---

# 135. Evidence Strength Guard

The number of connected citations does not determine evidence strength.

Evidence strength depends on:

- design;
- execution;
- bias;
- precision;
- consistency;
- applicability.

---

# 136. Quality Assessment Boundary

Formal risk-of-bias or quality assessment belongs to the relevant review or methodological workflow.

Citation chaining may flag concerns but should not fabricate quality scores.

---

# 137. Metadata Integrity

For every retained candidate verify enough metadata to prevent:

- title-author mismatch;
- DOI mismatch;
- duplicate identity;
- journal confusion.

Route to:

`source-verification`

and:

`reference-integrity-guard`

---

# 138. Full-Text Boundary

A citation-network record may be discovered without full text.

Label:

- `FULL_TEXT_VERIFIED`
- `ABSTRACT_ONLY`
- `METADATA_ONLY`
- `FULL_TEXT_UNAVAILABLE`

Do not make detailed scientific claims from metadata alone.

---

# 139. Abstract-Only Guard

Abstract-only records may support discovery.

They may be insufficient for:

- detailed method comparison;
- nuanced contradiction classification;
- causal interpretation;
- novelty claims.

---

# 140. Citation Context Source

When citation context is available, record its source.

Possible sources:

- full text;
- abstract;
- indexing platform;
- citation-context database.

Do not fabricate quotation context.

---

# 141. Direct Quote Guard

If quoting citation context:

- preserve wording;
- preserve source identity;
- follow copyright limits;
- do not invent page numbers.

---

# 142. Automated Tool Guard

Automated citation-network tools may help discover candidates.

They must not automatically decide:

- inclusion;
- scientific validity;
- novelty;
- gap status.

Human-readable scientific reasoning remains necessary.

---

# 143. API and Provider Guard

Provider/API outputs can be incomplete or stale.

Do not infer missing citations mean no relationship exists.

---

# 144. Current-Status Verification

For time-sensitive literature landscapes, verify the most recent relevant citing literature before finalizing:

- SoTA;
- gap;
- novelty;
- continuation.

---

# 145. Living Evidence Workflow

For rapidly evolving topics, citation chaining may be repeated periodically.

This does not convert the workflow into a living systematic review unless formal living-review procedures are used.

---

# 146. Citation Chaining for Manuscript Discussion

Chaining may identify:

- closest comparators;
- contradictory studies;
- mechanistic literature;
- methodological differences.

Route narrative synthesis to:

`scientific-discussion`

Do not add citations solely to make a discussion appear comprehensive.

---

# 147. Citation Chaining for Manuscript Positioning

For manuscript positioning, identify:

- closest competing studies;
- most relevant prior work;
- current frontier;
- meaningful differentiation.

Do not pad citations from the target journal.

---

# 148. Journal Independence

Journal selection must not redefine the citation corpus.

Preserve:

```text
scientific evidence selection
≠
target-journal citation strategy
```

---

# 149. APC Independence

Publication-cost preferences do not affect scholarly evidence discovery.

Do not exclude evidence because its journal charges APCs.

---

# 150. Reviewer-Requested Chaining

If a reviewer identifies a missing study:

- verify the study;
- inspect its citation lineage if scientifically important;
- update the manuscript only when relevant.

Route response preparation to:

`reviewer-response`

---

# 151. Reviewer Simulation Use

`reviewer-simulator` may use citation-chain findings to challenge:

- missing competitors;
- outdated literature;
- unsupported novelty;
- missing contradictions.

Citation chaining itself does not simulate reviewers.

---

# 152. Continuation Opportunity Handoff

When chaining around previous research identifies new directions, route to:

`continuation-opportunity-finder`

Do not convert every citing paper into a continuation proposal.

---

# 153. Research Resume Handoff

When citation chaining is used to resume earlier research:

`research-resume`

may use the updated literature lineage to determine current stage and next workflow.

---

# 154. Theoretical Framework Handoff

When chaining reveals competing or evolving theories, route to:

`theoretical-framework`

for formal theory selection or integration.

---

# 155. Conceptual Framework Handoff

When chaining reveals construct relationships requiring formal organization, route to:

`conceptual-framework`

---

# 156. Methodology Handoff

When chained literature reveals alternative or newer methods:

route method-selection questions to:

`methodology-architect`

Do not choose a method solely because it is newer.

---

# 157. Statistical Method Handoff

When citation chains reveal analytical alternatives:

route to:

`statistical-method-selector`

for method appropriateness.

---

# 158. Evidence-Synthesis Handoff

When a sufficiently verified and screened corpus exists:

route to:

`evidence-synthesis`

---

# 159. SoTA Handoff

When the objective is intellectual-state mapping:

route to:

`sota-builder`

---

# 160. Gap Discovery Handoff

Citation-chain findings may generate candidate gaps.

Route candidate formulation to:

`gap-discovery`

Do not treat uncited areas as validated gaps.

---

# 161. Gap Validation Handoff

When a specific gap claim must be attacked:

route to:

`gap-validator`

with:

- closest studies;
- recent citing studies;
- adjacent terminology;
- contradictory evidence;
- related methods.

---

# 162. Novelty Builder Handoff

When citation chains reveal a defensible opportunity:

route to:

`novelty-builder`

after gap validation where appropriate.

---

# 163. Novelty Auditor Handoff

All serious novelty claims should be stress-tested by:

`novelty-auditor`

Citation chaining supplies competitor evidence.

---

# 164. Source Verification Relationship

`citation-chaining` discovers candidate sources.

`source-verification` establishes whether those sources are real and correctly identified.

Conceptually:

```text
citation-chaining
      ↓
source-verification
```

for newly discovered candidates.

---

# 165. Reference Integrity Relationship

After source identity is sufficiently verified:

```text
source-verification
      ↓
reference-integrity-guard
```

before the candidate is used to support substantive claims.

---

# 166. Literature Screening Relationship

For purpose-specific reviews:

```text
citation-chaining
      ↓
verification
      ↓
literature-screening
```

A citation relationship does not equal eligibility.

---

# 167. Evidence Synthesis Relationship

Citation chaining expands the pool.

`evidence-synthesis` integrates included evidence.

Do not collapse discovery and synthesis.

---

# 168. State-of-the-Art Relationship

`sota-builder` uses chained evidence to understand:

- origins;
- evolution;
- contested findings;
- frontier.

Citation chaining does not independently declare the SoTA.

---

# 169. Gap Relationship

`gap-discovery` may use citation patterns to generate candidate gaps.

`gap-validator` determines whether the gap survives adversarial search.

---

# 170. Novelty Relationship

`novelty-builder` proposes contribution.

`novelty-auditor` attempts to defeat it.

Citation chaining helps locate the closest prior art.

---

# 171. Output: Anchor Summary

Provide when useful:

```text
Anchor:
Scientific role:
Verification status:
Chaining mode:
Why selected:
```

---

# 172. Output: Chaining Map

Example:

```text
Foundational Sources
        ↓
Anchor
   ┌────┼────┐
   ↓    ↓    ↓
Replication
Extension
Contradiction
   ↓
Current Frontier
```

Use only supported relationships.

---

# 173. Output: Candidate Table

Recommended:

| Candidate | Discovery Path | Relationship | Verification | Retain? |
|---|---|---|---|---|

---

# 174. Output: Scientific Development Table

Recommended:

| Period | Source | Relationship to Anchor | Scientific Development |
|---|---|---|---|

---

# 175. Output: Contradictory Evidence Table

Recommended:

| Source | Contradiction Type | Key Difference | Relevance |
|---|---|---|---|

---

# 176. Output: Replication Table

Recommended:

| Source | Replication Type | Independent? | Outcome |
|---|---|---|---|

---

# 177. Output: Competitor Table

Recommended:

| Source | Similarity | Difference | Threat to Novelty |
|---|---|---|---|

---

# 178. Full Output

For a comprehensive task provide:

## A. Objective
[...]

## B. Verified Anchors
[...]

## C. Backward Chaining
[...]

## D. Forward Chaining
[...]

## E. Related-Paper Expansion
[...]

## F. Theory / Method Lineage
[...]

## G. Replications
[...]

## H. Contradictory Evidence
[...]

## I. Closest Competitors
[...]

## J. Terminology Expansion
[...]

## K. Verification Status
[...]

## L. Saturation / Stop Rule
[...]

## M. Recommended Next Skill
[...]

---

# 179. Compact Output

For a small chaining request provide:

```text
Anchor:
Direction:
Most relevant discoveries:
Key relationship:
Verification status:
Next step:
```

---

# 180. User-Friendly Behavior

Prefer:

> This paper is useful as a forward-citation lead, but it only mentions the anchor in the background. I would not treat it as a replication.

Or:

> The strongest continuation signal is not the most highly cited paper. It is the later independent study that tested the same mechanism in a different population.

Or:

> Citation chaining found a 2025 study that appears to address part of the proposed gap. It should be verified and then sent to `gap-validator` before we keep the original gap claim.

---

# 181. Avoid These Behaviors

Do not:

- build networks around fabricated or unresolved anchors;
- assume citation means agreement;
- assume high citation count means high evidence quality;
- assume low citation count means irrelevance;
- treat related-paper algorithms as proof of relevance;
- count duplicate records as separate evidence;
- count one cohort's multiple papers as independent replication;
- ignore contradictory evidence;
- stay inside one research group's citation network;
- use target-journal citations strategically;
- allow APC preferences to alter evidence discovery;
- claim comprehensive coverage from exploratory chaining;
- claim "no studies exist" from citation chaining alone;
- certify novelty without `novelty-auditor`;
- validate gaps without `gap-validator`;
- include discovered papers before verification and screening;
- invent citation contexts, relationships, or provider results.

---

# Stop Conditions

Do not mark citation chaining complete when:

- anchor identity remains unresolved;
- critical newly discovered sources remain unverified;
- a major relevant citation branch has not been inspected;
- the objective requires forward and backward chaining but only one direction was performed;
- the proposed gap or novelty claim depends on unexplored recent literature;
- citation-chain saturation has not been reached or a pre-specified stop rule has not been satisfied;
- duplicate or study-family relationships materially distort the apparent evidence count;
- contradictory evidence has been discovered but not characterized;
- a retracted anchor remains treated as valid evidence.

Use:

- `ANCHOR_VERIFICATION_REQUIRED`
- `SOURCE_VERIFICATION_REQUIRED`
- `REFERENCE_INTEGRITY_REQUIRED`
- `CHAINING_INCOMPLETE`
- `SCREENING_REQUIRED`
- `GAP_REVALIDATION_REQUIRED`
- `NOVELTY_REAUDIT_REQUIRED`
- `NOT_READY_FOR_SYNTHESIS`

as appropriate.

---

# Success Criterion

`citation-chaining` succeeds when one or more scientifically relevant and sufficiently verified anchor sources have been expanded through transparent backward, forward, bidirectional, related-paper, author, method, theory, replication, contradiction, continuation, or novelty-stress-test pathways according to the research objective; when every important discovered source retains provenance showing how and why it entered the corpus; when citation relationships are classified by actual scientific function rather than assumed agreement; when foundational sources, subsequent developments, independent replications, extensions, criticisms, contradictions, methodological evolution, terminology changes, and closest competitors are actively sought rather than selectively filtered; when citation count, network centrality, author prestige, target-journal strategy, and APC preferences do not override scientific relevance; when duplicates, shared study families, preprint/version relationships, self-citation patterns, and retractions do not distort interpretation; when newly discovered sources return through `source-verification` and `reference-integrity-guard` before substantive scientific use; when purpose-specific inclusion is handed to `literature-screening`; when evidence integration is handed to `evidence-synthesis`; when State-of-the-Art, gap, and novelty conclusions are routed respectively to `sota-builder`, `gap-validator`, and `novelty-auditor` rather than being declared from citation links alone; when the chaining process stops according to an explicit relevance, depth, or saturation rule; and when the resulting literature lineage is sufficiently traceable, balanced, current, and scientifically defensible to support the next research workflow.
