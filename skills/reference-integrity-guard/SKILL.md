---
name: reference-integrity-guard
description: Protect the integrity of citations and references across research outputs by auditing claim-to-source support, in-text citation and reference-list consistency, metadata accuracy, DOI integrity, duplicate references, unsupported Scopus claims, citation padding, reference mashups, fabricated references, and inappropriate source use. Use before finalizing State-of-the-Art analyses, research gaps, novelty claims, proposals, theses, manuscripts, reviewer responses, or any research output containing citations.
---

# Reference Integrity Guard

## Purpose

`reference-integrity-guard` protects the complete citation system of a research output.

Its central question is:

> Does every citation correspond to a real and appropriate source, does that source actually support the scientific claim being made, and is the reference represented accurately throughout the document?

The guard operates after individual sources have been discovered and verified.

Its responsibility is broader than source verification.

It audits relationships among:

- scientific claims;
- in-text citations;
- verified source records;
- reference-list entries;
- DOI and metadata;
- indexing claims;
- source relevance;
- citation purpose.

---

# Core Principle

Use:

> A real source can still be cited incorrectly.

A citation is scientifically valid only when:

1. the source exists;
2. the reference metadata are accurate;
3. the source is relevant to the claim;
4. the cited passage or finding supports the claim;
5. the citation is represented correctly in the reference list;
6. no unsupported indexing or quality claim is attached to it.

---

# Activation Conditions

Use this skill when citations or references are being prepared or audited for:

- State of the Art;
- research landscape;
- evidence synthesis;
- research-gap analysis;
- novelty claims;
- theoretical framework;
- conceptual framework;
- methodology;
- research proposal;
- grant proposal;
- thesis;
- dissertation;
- manuscript;
- scientific discussion;
- reviewer response;
- literature review;
- systematic review;
- meta-analysis.

Use especially before:

`manuscript-auditor`

and final submission.

---

# Required Upstream Inputs

Prefer reference records already processed through:

`scopus-literature-search`
→ `source-verification`

The guard should not assume that every citation appearing in a draft has already been verified.

When necessary, route questionable records back to:

`source-verification`

---

# 1. Claim–Citation Relationship

For each important scientific claim, determine:

- what is being asserted;
- whether citation support is required;
- which source supports it;
- whether the source supports the exact claim.

Possible status:

- `CLAIM_SUPPORTED`
- `CLAIM_PARTIALLY_SUPPORTED`
- `CLAIM_OVERSTATED`
- `CLAIM_UNSUPPORTED`
- `CITATION_NOT_REQUIRED`
- `SUPPORT_UNVERIFIED`

Do not infer support merely because the source discusses a similar topic.

---

# 2. Claim Granularity

Match source evidence to the level of claim.

For example:

Source evidence:

> Study A found an association between X and Y.

Do not cite it for:

> X causes Y.

Likewise:

Evidence from one population

does not automatically support:

> This relationship is universal.

Use proportional scientific language.

---

# 3. Claim Strength Audit

Compare wording with the strength of evidence.

Flag words such as:

- causes;
- proves;
- demonstrates conclusively;
- universally;
- always;
- definitively;
- eliminates;
- guarantees.

When the evidence supports only:

- association;
- preliminary evidence;
- observational pattern;
- possible mechanism;

recommend appropriate hedging.

Use:

`CLAIM_STRENGTH_APPROPRIATE`

or:

`CLAIM_STRENGTH_EXCEEDS_EVIDENCE`

---

# 4. Citation Placement

Determine whether a citation clearly supports the sentence or clause it follows.

Avoid ambiguous paragraph-end citations where multiple unsupported statements appear before the citation.

Prefer citation placement close to the supported claim.

---

# 5. Citation Scope

A citation may support:

- one sentence;
- part of a sentence;
- several linked statements.

Do not assume one citation supports an entire paragraph when the paragraph contains multiple independent claims.

---

# 6. Multiple-Source Claims

When a claim summarizes a broad evidence base, one source may be insufficient.

Consider whether support should come from:

- systematic review;
- meta-analysis;
- several independent studies;
- major consensus guideline.

Do not mechanically add many citations.

Use the minimum evidence needed for defensible support.

---

# 7. Citation Diversity

Avoid relying repeatedly on:

- one paper;
- one research group;
- one journal;
- one publisher;

when broader independent evidence exists.

Classify excessive dependence as:

`SOURCE_CONCENTRATION_SIGNAL`

This does not automatically invalidate the citations.

---

# 8. Self-Citation Integrity

Author self-citation is legitimate when scientifically relevant.

Do not remove self-citations merely because they are self-citations.

Flag only when:

- unrelated;
- excessive;
- strategically inserted without scientific function.

Use:

`SELF_CITATION_JUSTIFIED`
or
`SELF_CITATION_PADDING_SIGNAL`

---

# 9. Target-Journal Citation Integrity

Articles from the intended target journal may be especially useful when they:

- establish relevant theory;
- provide comparable methodology;
- report related findings;
- show contradictory evidence;
- define the journal's scholarly conversation.

Do not cite target-journal articles solely to influence editorial acceptance.

Use:

- `TARGET_JOURNAL_CITATION_RELEVANT`
- `TARGET_JOURNAL_CITATION_WEAKLY_RELEVANT`
- `TARGET_JOURNAL_CITATION_PADDING_SIGNAL`

Scientific relevance remains the criterion.

---

# 10. Scopus Citation Integrity

Do not attach claims such as:

- Scopus indexed;
- Q1;
- Q2;
- high-impact;
- reputable;

to a source unless those claims have been separately verified where needed.

Reference validity and journal metrics are separate.

---

# 11. In-Text Citation to Reference Match

Every in-text citation should have a corresponding reference-list entry.

Classify:

- `MATCHED`
- `CITATION_WITHOUT_REFERENCE`
- `AMBIGUOUS_MATCH`
- `REFERENCE_METADATA_CONFLICT`

No cited source should silently disappear from the reference list.

---

# 12. Reference to In-Text Citation Match

Every reference-list entry should normally be cited in the document.

Flag:

`UNCITED_REFERENCE`

Exceptions may include journal-specific bibliographic formats, appendices, or intentionally listed resources.

Do not retain unused references merely to increase bibliography length.

---

# 13. Duplicate References

Detect:

- exact duplicates;
- DOI duplicates;
- title duplicates;
- preprint + published version;
- minor formatting variants.

Classify:

- `DUPLICATE_REFERENCE`
- `SAME_WORK_DIFFERENT_VERSION`
- `POSSIBLE_DUPLICATE`
- `DISTINCT_SOURCE`

Prefer the peer-reviewed version of record when appropriate.

---

# 14. DOI Integrity

Verify that DOI in the reference list matches the cited publication.

Possible status:

- `DOI_MATCH`
- `DOI_MISMATCH`
- `DOI_MISSING`
- `DOI_NOT_APPLICABLE`
- `DOI_UNVERIFIED`

Never insert a guessed DOI.

---

# 15. Metadata Integrity

Check:

- title;
- authors;
- year;
- journal;
- volume;
- issue;
- pages/article number;
- DOI.

Flag:

`REFERENCE_METADATA_MISMATCH`

when fields appear to belong to different records.

---

# 16. Reference Mashup Protection

A reference must never combine:

- title from Study A;
- author from Study B;
- DOI from Study C;
- journal from Study D.

Classify:

`REFERENCE_MASHUP`

and remove it from scientific use until reconstructed from a verified record.

---

# 17. Fabricated Reference Protection

Warning signs include:

- title cannot be found;
- DOI resolves elsewhere;
- journal issue is impossible;
- author combination cannot be verified;
- citation appears only in AI-generated text.

Use:

`POTENTIAL_FABRICATED_REFERENCE`

Then route to:

`source-verification`

Do not silently retain it.

---

# 18. Reference Verification Status

For every reference used in a high-stakes scientific output, maintain conceptual status:

- `VERIFIED`
- `VERIFIED_WITH_NOTE`
- `UNVERIFIED`
- `EXCLUDED`
- `RETRACTED`
- `REFERENCE_MASHUP`

Critical claims should not rely on:

`UNVERIFIED`

sources.

---

# 19. Retraction Guard

If a reference is retracted:

do not use it to support scientific claims.

Possible exception:

the discussion itself concerns:

- retraction;
- research integrity;
- historical development.

Mark:

`RETRACTED_REFERENCE`

---

# 20. Correction Guard

If a source has a correction or erratum, determine whether the correction changes:

- data;
- analysis;
- conclusions;
- bibliographic information.

Use the corrected scientific interpretation.

---

# 21. Preprint Guard

If a preprint has a peer-reviewed published version:

prefer the peer-reviewed version.

Do not cite both as independent evidence.

If only preprint exists:

label it clearly.

---

# 22. Secondary Citation Guard

Avoid citing Source B for a finding originally reported by Source A when Source A is accessible and relevant.

Prefer primary source citation for:

- specific empirical findings;
- original theory;
- original measurement instrument.

Secondary sources may be used for synthesis or interpretation.

---

# 23. Review Citation Use

Systematic reviews and meta-analyses are useful for:

- consensus;
- effect synthesis;
- field-level evidence.

Do not use them to replace primary citations when discussing a specific study's detailed method or finding.

---

# 24. Seminal Citation Integrity

Seminal sources should be cited for their actual contribution.

Do not cite an old famous paper merely for prestige.

Example legitimate purposes:

- theory origin;
- method origin;
- historical conceptualization.

---

# 25. Recent Evidence Balance

Do not rely only on old foundational sources when the scientific claim concerns the current state of evidence.

Balance:

`FOUNDATIONAL_EVIDENCE`

with:

`CURRENT_EVIDENCE`

---

# 26. Citation Recency Bias

Do not automatically replace older high-quality evidence with newer weaker evidence.

Recent does not always mean better.

---

# 27. Citation Prestige Bias

Do not prefer a paper solely because it appears in a famous journal.

Scientific relevance and evidence quality matter more than prestige.

---

# 28. Publisher Bias

Do not favor or reject sources solely because of publisher identity.

Evaluate:

- paper;
- journal;
- study design;
- relevance.

---

# 29. APC Independence

Do not use APC status as a criterion for whether an article is scientifically citable.

Publication-cost preference applies to destination-journal selection, not evidence integrity.

---

# 30. Citation Padding

Citation padding includes unnecessary references added primarily to:

- increase bibliography length;
- cite a target journal;
- cite editors;
- cite reviewers;
- create appearance of broad scholarship.

Flag:

`CITATION_PADDING_SIGNAL`

Do not delete legitimate multiple citations when they represent genuinely different evidence.

---

# 31. Citation Overload

A sentence with many citations may still be appropriate.

However, examine whether all sources contribute meaningfully.

Use:

`CITATION_OVERLOAD_SIGNAL`

when several references provide redundant support.

---

# 32. Citation Under-Support

A strong scientific assertion may need broader evidence.

Use:

`INSUFFICIENT_CITATION_SUPPORT`

when one weak source is used for a broad claim.

---

# 33. Citation Purpose Classification

When useful, classify citations as:

- `BACKGROUND`
- `THEORY`
- `EMPIRICAL_SUPPORT`
- `CONTRADICTORY_EVIDENCE`
- `METHOD`
- `MEASUREMENT`
- `GUIDELINE`
- `CONTEXT`
- `SOTA`
- `GAP_SUPPORT`
- `NOVELTY_COMPARATOR`
- `DISCUSSION_COMPARATOR`

This improves citation reasoning.

---

# 34. Gap Claim Citation Guard

A research gap should not rely only on citations showing:

> this topic is important.

Gap support should demonstrate:

- what has been studied;
- what remains unresolved;
- what evidence is missing;
- why the absence matters.

Use:

`GAP_CITATION_SUPPORT_ADEQUATE`

or:

`GAP_CITATION_SUPPORT_WEAK`

Final gap validation belongs to:

`gap-validator`

---

# 35. Novelty Citation Guard

Novelty claims require references to the closest existing studies.

Ask:

> Compared with which prior work is this study novel?

Use:

`NOVELTY_COMPARATOR_SOURCE`

Do not claim novelty from a literature list that avoids close competitors.

---

# 36. Theory Citation Guard

When attributing theory:

cite the original or authoritative source when possible.

Also include later refinements when needed.

Do not attribute a theory to a review that merely discusses it unless that is the intended source.

---

# 37. Method Citation Guard

When a method originates from a specific publication, cite:

- original method;
- validated adaptation;
- current guideline;

as appropriate.

Do not cite unrelated users of the method as the method's authority.

---

# 38. Instrument Citation Guard

Measurement tools should reference:

- original development paper;
- validation paper;
- culturally adapted validation where relevant.

Do not assume an instrument is validated because another study used it.

---

# 39. Statistical Method Citation Guard

Common basic statistics may not require citations.

Specialized methods may require:

- original methodology source;
- authoritative methodological reference;
- reporting guideline.

Avoid unnecessary citation of routine statistical procedures.

---

# 40. Discussion Citation Guard

Discussion citations should compare findings with existing evidence.

Use sources to show:

- agreement;
- disagreement;
- mechanism;
- boundary condition;
- implication.

Do not use citations merely to restate the introduction.

---

# 41. Claim-to-Source Evidence Map

When a high-stakes document is audited, build:

| Claim | Citation | Source Role | Support Level | Verification Status |
|---|---|---|---|---|

This allows transparent review of critical claims.

---

# 42. Support Level

Use:

- `DIRECT_SUPPORT`
- `STRONG_INDIRECT_SUPPORT`
- `PARTIAL_SUPPORT`
- `CONTEXT_ONLY`
- `CONTRADICTORY`
- `NO_SUPPORT`

Do not classify broad thematic similarity as direct support.

---

# 43. Unsupported Claim Handling

When a claim lacks support:

choose one of:

1. find appropriate evidence;
2. weaken the claim;
3. identify it as interpretation;
4. remove it.

Do not attach an unrelated citation merely to make the sentence appear referenced.

---

# 44. Citation Misrepresentation

Flag when a source is cited as showing:

- benefit,

when it actually reports:

- no benefit;

or as showing:

- causal effect,

when it reports:

- association.

Use:

`SOURCE_MISREPRESENTED`

This is a major integrity issue.

---

# 45. Quote Integrity

When direct quotations are used:

ensure:

- wording matches source;
- quotation marks are present;
- page/location is provided when required;
- meaning is not distorted by selective extraction.

Paraphrase is generally preferable in scientific manuscripts unless quotation is necessary.

---

# 46. Paraphrase Integrity

A paraphrase must preserve the scientific meaning of the source.

Do not paraphrase:

> may be associated

as:

> causes.

Use:

`PARAPHRASE_ACCURATE`
or
`PARAPHRASE_DISTORTS_SOURCE`

---

# 47. Citation Chain Integrity

When a claim has been repeated across review articles, trace back to the original evidence when possible.

This reduces propagation of citation errors.

---

# 48. Citation Circularity

Watch for multiple sources that all rely on the same original study.

Do not treat them as fully independent evidence.

Flag:

`DEPENDENT_CITATION_CHAIN`

when relevant.

---

# 49. Shared Dataset Awareness

Multiple articles may derive from the same dataset.

Do not count them as independent replication unless they truly are independent.

Use:

`POSSIBLE_SHARED_DATASET`

---

# 50. Reference Style Integrity

Check basic consistency in:

- author formatting;
- year formatting;
- journal title;
- volume/issue;
- pages;
- DOI format.

Final formatting style should follow the target journal or required citation standard.

Scientific integrity takes priority over cosmetic formatting.

---

# 51. Citation Style Is Downstream

Do not confuse:

reference accuracy

with:

reference style.

First ensure metadata are correct.

Then format them as:

- APA;
- Vancouver;
- IEEE;
- Harvard;
- journal-specific style.

---

# 52. Target Journal Citation Style

When a target journal is selected later:

apply its reference requirements.

Do not modify scientific source selection merely to match the journal's style.

---

# 53. Reference List Order

Ensure ordering follows the chosen citation system:

- alphabetical;
- numerical order of appearance;
- journal-specific rules.

This is a formatting issue, not evidence strength.

---

# 54. Orphan Citation

Use:

`ORPHAN_CITATION`

when an in-text citation has no reference-list match.

---

# 55. Orphan Reference

Use:

`ORPHAN_REFERENCE`

when a reference-list item is never cited.

---

# 56. Metadata Conflict Resolution

If manuscript metadata conflict with verified source metadata:

prefer verified canonical metadata.

Record the correction.

Do not silently preserve known errors.

---

# 57. DOI Normalization

Use canonical DOI representation internally when possible:

```text
10.xxxx/xxxxx
```

Treat the following as potentially equivalent representations when they resolve to the same DOI:

```text
https://doi.org/10.xxxx/xxxxx
http://dx.doi.org/10.xxxx/xxxxx
doi:10.xxxx/xxxxx
10.xxxx/xxxxx
```

Normalize presentation without changing the underlying DOI.

Do not infer that a DOI is valid merely because its syntax appears plausible.

Route uncertain DOI identity to:

`source-verification`

---

# 58. DOI Resolution Integrity

When DOI validation is required, distinguish:

- syntactically plausible DOI;
- resolvable DOI;
- DOI metadata match;
- DOI-to-article identity match.

Possible statuses:

- `DOI_VERIFIED`
- `DOI_RESOLVES_METADATA_MATCH`
- `DOI_RESOLVES_METADATA_CONFLICT`
- `DOI_NOT_RESOLVED`
- `DOI_NOT_AVAILABLE`
- `DOI_UNVERIFIED`

A DOI resolving to a real article does not prove that it belongs to the cited article.

---

# 59. Alternative Identifier Integrity

When DOI is absent, other identifiers may support identity checking.

Examples:

- PMID;
- PMCID;
- ISBN;
- ISSN;
- trial registration number;
- report number;
- dataset accession;
- clinical guideline identifier;
- regulation number.

Do not substitute one identifier type for another without labeling it correctly.

---

# 60. Version Integrity

Distinguish among:

- preprint;
- accepted manuscript;
- version of record;
- corrected version;
- retracted version;
- conference abstract;
- full conference paper;
- thesis chapter;
- journal article derived from thesis;
- dataset version.

Use the scientifically appropriate version for the claim.

Prefer the version of record when available and suitable.

---

# 61. Online-First and Final Publication

Early-online and issue-assigned records may differ in:

- publication year;
- pagination;
- issue;
- article number;
- DOI display.

Do not create duplicate references when they represent the same article.

Use canonical final metadata when available.

---

# 62. Duplicate Publication Detection

Two bibliographic records may represent the same scientific work.

Check:

- title similarity;
- DOI;
- authors;
- cohort;
- sample size;
- intervention;
- dates;
- outcome set.

Possible status:

`POSSIBLE_DUPLICATE_PUBLICATION`

Do not count duplicate publications as independent evidence.

---

# 63. Multiple Reports from One Study

A single study may produce several publications.

Classify relationships where possible:

- primary outcome report;
- secondary outcome report;
- follow-up;
- subgroup analysis;
- protocol;
- methods paper;
- economic analysis;
- biomarker analysis.

Do not merge scientifically distinct reports merely because they share a cohort.

Do not count them as independent replication when they are not independent.

---

# 64. Study-Family Record

When multiple papers belong to one study family, record:

```yaml
study_family:
  study_id:
  cohort_or_trial:
  shared_population:
  publications:
    - reference_id:
      role:
      outcome_domain:
      follow_up_period:
  independence_status:
  notes:
```

Unknown fields remain unknown.

---

# 65. Source Role Integrity

Every citation should have a defensible role.

Possible roles include:

- `BACKGROUND`
- `PHENOMENON`
- `THEORY`
- `MECHANISM`
- `METHOD`
- `INSTRUMENT`
- `PRIMARY_EVIDENCE`
- `SYSTEMATIC_REVIEW`
- `META_ANALYSIS`
- `GUIDELINE`
- `POLICY`
- `REGULATION`
- `STATISTICS`
- `CONTRADICTORY_EVIDENCE`
- `COMPARATOR`
- `NOVELTY_COMPETITOR`

Do not use a source outside the role its evidence can support.

---

# 66. Scholarly vs Phenomenon Source Boundary

Distinguish:

```text
SCHOLARLY EVIDENCE
      ↓
theory / mechanism / association / effect / method

PHENOMENON EVIDENCE
      ↓
magnitude / burden / trend / policy / regulation / real-world context
```

Official statistics can establish magnitude or trend.

They do not automatically establish scientific mechanism or causality.

Journal articles can establish scholarly knowledge.

They do not automatically replace current official statistics for population burden.

---

# 67. Authority-First Phenomenon Citation

For real-world factual claims, prefer the most authoritative original source available.

Examples:

- national statistics agency;
- ministry;
- WHO;
- World Bank;
- regulatory authority;
- official registry;
- institutional data owner.

When a news article reports an official statistic, recover the original authoritative source when possible.

---

# 68. News Citation Guard

News may be useful for:

- event discovery;
- public communication context;
- recent implementation events.

News should not normally be the final source for:

- official statistics;
- regulation text;
- scientific causal claims;
- clinical effectiveness claims.

Recover the underlying primary or authoritative source when possible.

---

# 69. Regulation and Policy Citation Guard

Regulations and policies may support:

- legal requirement;
- policy mandate;
- implementation target;
- regulatory status.

They do not by themselves prove:

- intervention effectiveness;
- biological mechanism;
- clinical efficacy;
- behavioral causality.

Verify the current status when the claim depends on active policy or regulation.

---

# 70. Dataset Citation Integrity

When datasets are cited, verify where possible:

- dataset title;
- producer;
- version;
- release date;
- coverage period;
- geography;
- population;
- access date when relevant;
- persistent identifier.

Do not cite a dataset as if it were a journal article.

---

# 71. Dashboard Citation Integrity

Dynamic dashboards require additional care.

Record when relevant:

- dashboard owner;
- indicator;
- geography;
- reference period;
- access date;
- extraction date.

Do not confuse access date with the period represented by the data.

---

# 72. Publication Date vs Reference Period

For statistics and reports distinguish:

```text
publication date
≠
reference period
```

A report published in 2026 may describe 2024 data.

State the period that the claim actually represents.

---

# 73. Geographic Fit

A source should not be generalized beyond its geographic evidence without justification.

Possible status:

- `GEOGRAPHY_MATCH`
- `GEOGRAPHY_PARTIAL_MATCH`
- `GEOGRAPHY_MISMATCH`
- `GEOGRAPHY_NOT_APPLICABLE`

---

# 74. Population Fit

Check whether the cited source actually concerns the relevant:

- age group;
- disease group;
- profession;
- education level;
- species;
- setting;
- industry;
- demographic subgroup.

Do not silently generalize from one population to another.

---

# 75. Temporal Fit

For time-sensitive claims, assess whether the evidence is sufficiently current.

Possible status:

- `TEMPORALLY_CURRENT`
- `TEMPORALLY_ACCEPTABLE`
- `HISTORICAL_BY_DESIGN`
- `POTENTIALLY_OUTDATED`
- `TEMPORAL_STATUS_UNKNOWN`

Older seminal evidence may remain scientifically important.

Recency should not erase foundational work.

---

# 76. Claim Context Fit

Evaluate whether the cited evidence matches the claim's:

- population;
- exposure;
- intervention;
- comparator;
- outcome;
- setting;
- time frame;
- design.

Topic similarity alone is not sufficient.

---

# 77. Causal Claim Citation Guard

A causal claim requires evidence capable of supporting causal interpretation.

Do not cite:

- cross-sectional association;
- uncontrolled descriptive evidence;
- simple correlation;

as sufficient proof of causal effect.

Use:

`CAUSAL_SUPPORT_INSUFFICIENT`

when appropriate.

---

# 78. Prediction Claim Citation Guard

Prediction evidence supports predictive performance.

It does not automatically support causal explanation.

Preserve:

```text
prediction
≠
causation
```

---

# 79. Mechanistic Claim Citation Guard

Mechanistic statements require evidence that actually addresses mechanism.

Do not infer mechanism from outcome association alone.

Possible status:

`MECHANISM_OVERINFERRED`

---

# 80. Clinical Recommendation Citation Guard

Clinical recommendations should be supported by evidence appropriate to the recommendation level.

Consider:

- guideline;
- systematic review;
- comparative clinical evidence;
- safety evidence;
- applicability.

Do not derive treatment recommendations from weak observational findings alone.

---

# 81. Policy Recommendation Citation Guard

Policy recommendations should distinguish:

- evidence of a problem;
- evidence of intervention effectiveness;
- implementation feasibility;
- legal or policy authority.

Do not treat a policy document as proof that the policy works.

---

# 82. Negative or Null Evidence Integrity

Do not rewrite:

```text
not statistically significant
```

as:

```text
no effect
```

unless the evidence supports equivalence or sufficiently precise absence.

Citation wording should preserve uncertainty.

---

# 83. Contradictory Evidence Integrity

Do not suppress credible contradictory studies merely because they weaken the preferred narrative.

Classify when relevant:

- `SUPPORTING`
- `CONTRADICTORY`
- `MIXED`
- `INCONCLUSIVE`

Balanced citation strengthens scientific integrity.

---

# 84. Consensus Claim Guard

Claims such as:

- "it is well established";
- "the literature agrees";
- "there is consensus";

require evidence of broad agreement.

One or two papers are usually insufficient.

Use:

`CONSENSUS_CLAIM_UNSUPPORTED`

when appropriate.

---

# 85. Absence Claim Guard

Claims such as:

- "no studies exist";
- "this has never been investigated";
- "there is no evidence";

are high-risk.

They require a sufficiently broad and current literature search.

Route to:

`scopus-literature-search`

and when needed:

`citation-chaining`

before accepting an absence claim.

---

# 86. First-Study Claim Guard

Claims such as:

- "the first study";
- "the first evidence";
- "the first application";

require adversarial verification.

Route novelty-related priority claims to:

`novelty-auditor`

Do not approve first-study language based only on a narrow search.

---

# 87. Gap Claim Support

A research gap should be supported by the state of evidence, not a single citation.

Preferred chain:

```text
verified literature
      ↓
screened evidence
      ↓
evidence synthesis
      ↓
state of the art
      ↓
gap validation
```

Reference integrity should not independently invent a gap.

---

# 88. Novelty Claim Support

Novelty claims should identify the closest scientific competitors.

Citation integrity requires:

- verified competitor identity;
- accurate representation;
- no selective omission;
- no false priority claim.

---

# 89. Citation Chaining Integrity Handoff

After reference records are sufficiently verified and safe to use, citation-network expansion may route to:

`citation-chaining`

The guard should not conduct uncontrolled citation expansion itself.

---

# 90. Primary-Source Recovery

When a secondary source points to a primary study central to a claim:

attempt to recover and verify the primary source when practical.

Use secondary citation transparently when primary recovery is not possible.

---

# 91. Secondary Citation Transparency

Do not cite a primary source as if it was directly inspected when only a secondary source was read.

Possible notation:

`PRIMARY_NOT_DIRECTLY_VERIFIED`

---

# 92. Quote Traceability

For direct quotations, record when useful:

```yaml
quotation:
  reference_id:
  exact_text:
  page_or_location:
  version:
  verification_status:
```

Never invent page numbers.

---

# 93. Paraphrase Traceability

A paraphrase must preserve:

- direction;
- magnitude;
- uncertainty;
- population;
- design;
- causal status.

A more fluent paraphrase must not become a stronger claim.

---

# 94. Numeric Claim Integrity

For numerical claims verify:

- numerator;
- denominator;
- percentage;
- units;
- confidence interval;
- time period;
- population;
- geography.

Do not copy a number while dropping its denominator or context.

---

# 95. Relative vs Absolute Risk Guard

Do not present relative effects as absolute effects.

Preserve the measure used by the source.

---

# 96. Unit Integrity

Check:

- mg vs g;
- mL vs L;
- percentage vs proportion;
- incidence vs prevalence;
- rate vs count;
- concentration units.

Unit errors can invalidate otherwise correct citations.

---

# 97. Direction-of-Effect Integrity

Ensure the manuscript does not reverse:

- increased vs decreased;
- protective vs harmful;
- positive vs negative association;
- higher vs lower risk.

Use:

`DIRECTION_MISMATCH`

when detected.

---

# 98. Statistical Estimate Integrity

Where a claim depends on a result, preserve the correct:

- effect estimate;
- uncertainty interval;
- p-value when relevant;
- model;
- adjusted/unadjusted status.

Do not cite an adjusted estimate as if it were unadjusted or vice versa.

---

# 99. Subgroup Integrity

Do not generalize subgroup findings to the full sample without justification.

Possible status:

`SUBGROUP_GENERALIZATION`

---

# 100. Outcome Integrity

Do not cite evidence for a surrogate outcome as if it directly demonstrated a clinical or real-world outcome.

Label surrogate outcomes appropriately.

---

# 101. Composite Outcome Integrity

When a source reports a composite outcome, do not attribute the effect to every component unless component results support it.

---

# 102. Abstract-Only Evidence Guard

Abstract-only evidence may be insufficient for complex claims.

Use:

`ABSTRACT_ONLY_LIMITATION`

when full-text verification is needed but unavailable.

Do not imply full-method verification from an abstract alone.

---

# 103. Supplementary Material Integrity

Important evidence may reside in supplementary materials.

When a claim depends on supplemental data:

verify the supplement when available.

Do not assume main-text summaries fully represent supplemental analyses.

---

# 104. Table and Figure Source Integrity

If data are extracted from a table or figure, preserve:

- table/figure identity;
- units;
- subgroup;
- footnotes;
- denominator.

Do not visually estimate exact numbers when exact values are unavailable unless explicitly labeled approximate.

---

# 105. Author Name Disambiguation

Similar author names do not prove common authorship.

Use identifiers such as ORCID only when verified.

Do not merge researchers based on initials alone.

---

# 106. Journal Title Disambiguation

Check journal identity carefully when titles or abbreviations are similar.

Do not infer legitimacy or indexing from name similarity.

---

# 107. Publisher Identity Guard

A publisher name alone does not establish:

- peer review;
- indexing;
- journal quality;
- source validity.

Verification remains source-specific.

---

# 108. Scopus Source vs Document Distinction

Preserve:

```text
journal/source indexed in Scopus
≠
specific document verified in Scopus
```

Do not collapse these statuses.

---

# 109. Quartile Claim Integrity

Quartile claims are contextual metadata.

Verify:

- metric system;
- year;
- subject category;
- source.

Do not describe quartile as intrinsic evidence quality.

---

# 110. Citation Count Integrity

Citation counts are time-dependent and provider-dependent.

When used, record:

- provider;
- access date.

Do not use citation count as a substitute for methodological quality.

---

# 111. APC and Evidence Independence

Publication cost must not determine whether evidence is scientifically included.

Preserve:

```text
evidence selection
≠
journal affordability preference
```

---

# 112. Target-Journal Independence

Target-journal strategy must not alter which scientific sources are needed.

Relevant target-journal papers may be cited.

Irrelevant target-journal papers must not be added for strategic reasons.

---

# 113. Reviewer-Requested Citation Guard

When reviewers request citations:

assess scientific relevance first.

Do not add a reviewer-suggested citation automatically.

Possible outcomes:

- `ADD_RELEVANT_REFERENCE`
- `PARTIALLY_RELEVANT`
- `NOT_REQUIRED`
- `SCIENTIFICALLY_IRRELEVANT`
- `VERIFY_BEFORE_USE`

---

# 114. AI-Generated Reference Guard

Any reference proposed by generative AI must be treated as unverified until checked.

Never allow:

```text
AI-generated citation
      ↓
final reference list
```

without verification.

---

# 115. Reference Import Guard

References imported from:

- citation managers;
- spreadsheets;
- RIS;
- BibTeX;
- EndNote XML;
- manuscript files;

may still contain errors.

Import is not verification.

---

# 116. OCR and Extraction Guard

Automatically extracted references may contain:

- character errors;
- broken DOI;
- merged authors;
- incorrect pagination.

Verify critical records before use.

---

# 117. Reference Mashup Detection

A mashup may combine:

- title from article A;
- authors from article B;
- DOI from article C.

If detected:

`REFERENCE_MASHUP`

Route to:

`source-verification`

Do not repair by guessing.

---

# 118. Fabrication Escalation

If a reference cannot be found after reasonable verification and appears fabricated:

use:

`POSSIBLE_FABRICATED_REFERENCE`

Do not silently replace it with a different real article.

---

# 119. Reference Conflict Record

When metadata providers disagree, record:

```yaml
reference_conflict:
  reference_id:
  field:
  value_a:
  source_a:
  value_b:
  source_b:
  preferred_value:
  resolution_basis:
  status:
```

---

# 120. Claim–Source Audit Record

For high-value claims use:

```yaml
claim_source_audit:
  claim_id:
  claim_text:
  claim_type:
  citation_required:
  reference_ids:
  support_level:
  population_fit:
  geographic_fit:
  temporal_fit:
  design_fit:
  causal_fit:
  verification_status:
  integrity_flags:
  action:
```

---

# 121. Reference Integrity Outcome

Possible reference-level outcomes:

- `REFERENCE_CLEARED`
- `REFERENCE_CLEARED_WITH_LIMITATION`
- `REFERENCE_CORRECTION_REQUIRED`
- `SOURCE_VERIFICATION_REQUIRED`
- `CLAIM_REVISION_REQUIRED`
- `REFERENCE_EXCLUDE`
- `RETRACTION_BLOCK`
- `REFERENCE_MASHUP`
- `POSSIBLE_FABRICATED_REFERENCE`

---

# 122. Claim Integrity Outcome

Possible claim-level outcomes:

- `SUPPORTED_AS_WRITTEN`
- `SUPPORTED_AFTER_NARROWING`
- `PARTIALLY_SUPPORTED`
- `REQUIRES_ADDITIONAL_SOURCE`
- `REQUIRES_PRIMARY_SOURCE`
- `UNSUPPORTED_REMOVE_OR_REVISE`
- `CAUSAL_OVERCLAIM`
- `NOVELTY_OVERCLAIM`
- `CONSENSUS_OVERCLAIM`
- `ABSENCE_CLAIM_UNVERIFIED`

---

# 123. Audit Priority

Prioritize:

1. claims central to the research question;
2. gap claims;
3. novelty claims;
4. causal or mechanistic claims;
5. numerical claims;
6. clinical or policy recommendations;
7. methods and instrument provenance;
8. discussion claims;
9. background claims;
10. cosmetic reference formatting.

Scientific risk comes before formatting perfection.

---

# 124. Critical Reference Set

Identify references whose failure would materially alter:

- research rationale;
- gap;
- novelty;
- theory;
- method;
- primary interpretation;
- conclusion.

These require the strongest verification.

Use:

`CRITICAL_REFERENCE`

---

# 125. Reference Integrity Matrix

Recommended table:

| Claim | Reference | Source Verified | Support | Integrity Flag | Action |
|---|---|---:|---|---|---|

Use a more detailed matrix when required.

---

# 126. Reference List Audit

Check the final reference list for:

- duplicates;
- orphan references;
- missing references;
- incomplete metadata;
- DOI mismatch;
- retractions;
- formatting inconsistency;
- source-role anomalies.

Do not treat formatting cleanup as completion if scientific integrity issues remain.

---

# 127. In-Text Citation Audit

Check:

- every citation resolves to a reference;
- numbering/order is consistent;
- author-year identity is correct;
- citation placement matches the supported claim;
- grouped citations are scientifically coherent.

---

# 128. Citation Group Audit

When several citations appear together, verify that each citation is relevant to the grouped claim.

Do not use a citation cluster to hide weak support.

---

# 129. Final Reference Eligibility Gate

A reference may enter the final evidence system only when:

- identity is sufficiently verified;
- integrity status is acceptable;
- it is relevant;
- it is actually used;
- it is not retracted;
- its role is scientifically appropriate.

---

# 130. Synthesis Entry Gate

Before a source feeds evidence synthesis:

```text
SOURCE VERIFIED
      ↓
REFERENCE INTEGRITY CLEARED
      ↓
PURPOSE-SPECIFIC SCREENING
      ↓
EVIDENCE SYNTHESIS
```

Reference integrity does not replace eligibility screening.

---

# 131. Gap and Novelty Gate

Before evidence supports gap or novelty:

```text
verified source
      ↓
integrity-cleared representation
      ↓
screened evidence
      ↓
state of the art
      ↓
gap validation
      ↓
novelty audit
```

---

# 132. Manuscript Gate

Before manuscript submission, critical references should have:

- verified identity;
- correct metadata;
- valid claim support;
- no unresolved retraction issue;
- no citation mashup;
- accurate in-text/reference-list mapping.

---

# 133. Reviewer Response Gate

When a reviewer challenges a citation:

do not defend the citation reflexively.

Reassess:

- source identity;
- relevance;
- support;
- wording;
- whether a stronger source is needed.

Route to:

`reviewer-response`

after integrity assessment when appropriate.

---

# 134. Research Passport Update

When supported, update:

```yaml
reference_integrity:
  audited_claims:
  audited_references:
  critical_references:
  cleared_references:
  corrected_references:
  excluded_references:
  orphan_citations:
  orphan_references:
  duplicate_references:
  retraction_flags:
  mashup_flags:
  unsupported_claims:
  causal_overclaims:
  novelty_overclaims:
  unresolved_items:
  next_stage:
```

Do not fabricate counts.

---

# 135. Reference Integrity Report

A full report may contain:

## A. Audit Scope
[...]

## B. Critical Claims
[...]

## C. Reference Identity Issues
[...]

## D. Claim–Source Support
[...]

## E. DOI and Metadata Issues
[...]

## F. Retraction / Correction Status
[...]

## G. Duplicate / Orphan Records
[...]

## H. Scopus and Journal-Metadata Claims
[...]

## I. Gap / Novelty Citation Risks
[...]

## J. Required Corrections
[...]

## K. Final Integrity Status
[...]

---

# 136. Compact Output

For a small audit use:

```text
Claim:
Reference:
Integrity status:
Support status:
Problem:
Required action:
```

---

# 137. Integrity Status Summary

Possible overall outcomes:

- `REFERENCE_INTEGRITY_CLEARED`
- `REFERENCE_INTEGRITY_CLEARED_WITH_MINOR_CORRECTIONS`
- `REFERENCE_CORRECTION_REQUIRED`
- `MAJOR_REFERENCE_INTEGRITY_PROBLEMS`
- `SOURCE_REVERIFICATION_REQUIRED`
- `NOT_READY_FOR_SCIENTIFIC_USE`

---

# 138. Relationship with Source Verification

`source-verification` asks:

> Is this source real, correctly identified, and sufficiently verified?

`reference-integrity-guard` asks:

> Is this source being used and represented correctly inside the research output?

Conceptually:

```text
source-verification
      ↓
reference-integrity-guard
```

Do not collapse the two functions.

---

# 139. Relationship with Citation Chaining

After anchor sources are verified and integrity-cleared:

`citation-chaining`

may expand backward and forward citation networks.

Newly discovered sources must return through verification before scientific use.

---

# 140. Relationship with Literature Screening

`literature-screening`

determines purpose-specific inclusion.

A real, integrity-cleared source may still be excluded because it does not meet the review or research criteria.

---

# 141. Relationship with Evidence Synthesis

`evidence-synthesis`

should synthesize evidence only after source identity, citation integrity, and screening are sufficiently secure.

Do not synthesize fabricated, mashup, retracted, or materially misrepresented records.

---

# 142. Relationship with State of the Art

`sota-builder`

depends on accurate evidence representation.

Reference integrity should protect SoTA classification from:

- incorrect source identity;
- selective citation;
- overstated findings;
- false consensus;
- false absence.

---

# 143. Relationship with Gap Validation

`gap-validator`

requires an integrity-cleared evidence base.

A gap cannot be validated merely because references are sparse or incorrectly represented.

---

# 144. Relationship with Novelty Builder

`novelty-builder`

may use verified competitor studies to define what is scientifically new.

Reference integrity protects against false competitor comparison.

---

# 145. Relationship with Novelty Auditor

`novelty-auditor`

stress-tests priority and contribution claims.

All novelty-defining references must be sufficiently verified and accurately represented.

---

# 146. Relationship with Theoretical Framework

`theoretical-framework`

may depend on:

- seminal theory;
- later refinements;
- competing theories;
- boundary conditions.

Reference integrity should preserve original theory attribution and later evolution.

---

# 147. Relationship with Methodology

Methods, instruments, algorithms, and protocols require accurate provenance.

Route methodology-selection questions to:

`methodology-architect`

while preserving citation integrity here.

---

# 148. Relationship with Analysis Planning

Statistical or analytical citations should support the actual method used.

Route method-choice questions to:

`analysis-planner`

or:

`statistical-method-selector`

when needed.

---

# 149. Relationship with Scientific Discussion

`scientific-discussion`

depends on balanced and accurate comparison with previous evidence.

Reference integrity must prevent:

- cherry-picking;
- contradictory-evidence suppression;
- direction reversal;
- causal overstatement.

---

# 150. Relationship with Manuscript Writer

`manuscript-writer`

may improve citation placement and prose.

It must not invent sources or strengthen claims beyond verified evidence.

---

# 151. Relationship with Manuscript Auditor

`manuscript-auditor`

may use reference-integrity findings as part of scientific-readiness assessment.

Unresolved major integrity issues should block submission readiness.

---

# 152. Relationship with Journal Matcher

`journal-matcher`

must not influence scientific source selection.

Journal fit and reference integrity are separate decisions.

---

# 153. Relationship with Reviewer Simulator

`reviewer-simulator`

may challenge:

- weak support;
- outdated evidence;
- citation padding;
- missing contradictory literature;
- inappropriate methods citations.

Integrity findings may inform simulated reviewer concerns.

---

# 154. Relationship with Reviewer Response

`reviewer-response`

may route citation disputes here for verification.

Do not add reviewer-requested references without relevance and integrity assessment.

---

# 155. User-Friendly Behavior

Prefer precise explanations.

Example:

> The article is real, but the cited sentence is stronger than what the study actually supports. The safest correction is to narrow the claim rather than simply keep the citation.

Or:

> The DOI resolves, but it belongs to a different article. This reference should not be used until the correct source identity is recovered.

Or:

> These two papers use the same cohort, so they should not be treated as independent replication.

Avoid unexplained integrity codes when plain language is more useful.

---

# 156. Avoid These Behaviors

Do not:

- fabricate a reference;
- fabricate a DOI;
- repair metadata by guessing;
- treat DOI syntax as verification;
- treat Scopus source indexing as document verification;
- treat quartile as evidence quality;
- cite retracted literature as valid evidence;
- merge metadata from different papers;
- add references only to increase citation count;
- add target-journal citations strategically;
- suppress contradictory evidence;
- overstate causal or mechanistic support;
- misrepresent secondary evidence as primary;
- claim a primary source was read when it was not;
- count shared cohorts as independent replication;
- substitute citation formatting for scientific integrity;
- allow APC preferences to alter evidence selection;
- approve "first study" or "no studies exist" without adequate validation.

---

# Stop Conditions

Do not clear the reference system when any critical issue remains unresolved, including:

- possible fabricated reference;
- reference mashup;
- DOI-to-article mismatch;
- retracted source supporting a substantive claim;
- materially conflicting metadata;
- central claim unsupported by its citations;
- critical causal overclaim;
- unverified first-study or absence claim central to novelty;
- unresolved orphan citation affecting scientific traceability;
- incorrect source being used to justify theory, method, result, gap, or novelty.

Use:

- `SOURCE_VERIFICATION_REQUIRED`
- `CLAIM_REVISION_REQUIRED`
- `REFERENCE_CORRECTION_REQUIRED`
- `RETRACTION_BLOCK`
- `NOVELTY_REVALIDATION_REQUIRED`
- `NOT_READY_FOR_SCIENTIFIC_USE`

as appropriate.

---

# Success Criterion

`reference-integrity-guard` succeeds when the complete citation and reference system of a research output is scientifically traceable and defensible: every critical reference has a sufficiently verified identity; in-text citations and reference-list entries correspond correctly; DOI and bibliographic metadata are accurate enough for reliable use; retractions, corrections, duplicates, shared-study relationships, orphan citations, orphan references, and reference mashups are identified; each citation supports the claim at the appropriate level of strength, population, geography, time, design, and causal status; scholarly evidence is distinguished from phenomenon, policy, regulatory, and statistical evidence; contradictory evidence is not selectively suppressed; Scopus status, journal metrics, target-journal strategy, and APC preferences are kept separate from scientific evidence quality; gap, novelty, theory, methods, discussion, manuscript, reviewer-simulation, and reviewer-response workflows receive integrity-cleared evidence; unsupported or overstated claims are narrowed, re-sourced, or removed rather than cosmetically defended; and no reference is allowed to support a critical scientific conclusion while its identity, integrity, or claim-to-source relationship remains materially unresolved.
