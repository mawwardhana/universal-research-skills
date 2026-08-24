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