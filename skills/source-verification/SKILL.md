---

name: source-verification
description: Verify scholarly sources before they are used as evidence by confirming publication existence, bibliographic consistency, DOI and metadata integrity, peer-review status, journal legitimacy, Scopus source and document status where verifiable, corrections or retractions, and evidence provenance. Use after literature discovery and before evidence synthesis, State-of-the-Art analysis, gap validation, novelty assessment, methodology justification, manuscript writing, or any citation-dependent scientific claim.
---

# Source Verification

## Purpose

`source-verification` determines whether a discovered scholarly record is sufficiently trustworthy and traceable to be used as scientific evidence.

Its central question is:

> Does this source actually exist, do its bibliographic elements belong together, is its publication status legitimate, and can its indexing and evidence status be defended?

This skill protects the framework from:

* fabricated references;
* metadata mismatches;
* incorrect DOI assignments;
* false Scopus claims;
* duplicate publications;
* retracted literature;
* predatory or questionable sources;
* unsupported peer-review assumptions;
* citation hallucination.

This skill verifies sources.

It does not independently determine:

* final evidence synthesis;
* research gaps;
* novelty;
* manuscript conclusions.

---

# Core Principle

Use:

> If a source cannot be verified, it must not silently enter the evidence base.

Verification uncertainty must remain visible.

Never convert:

`UNVERIFIED`

into:

`VERIFIED`

because the citation looks plausible.

---

# Activation Conditions

Use this skill after literature records are discovered through:

* Scopus;
* OpenAlex;
* Crossref;
* PubMed;
* Semantic Scholar;
* publisher platforms;
* citation chaining;
* uploaded bibliographies;
* previous manuscripts;
* user-provided references;
* reference-manager exports.

Use before those sources support:

* research landscape;
* trends;
* emerging-topic analysis;
* State of the Art;
* research-gap claims;
* novelty;
* theoretical arguments;
* methodology;
* analysis justification;
* scientific discussion;
* manuscript claims.

---

# Input Record

A candidate source may contain:

```yaml
title:
authors:
year:
journal:
doi:
issn:
publisher:
volume:
issue:
pages:
article_number:
document_type:
abstract:
provider:
source_url:
```

Not every field must exist.

Missing information should be verified where possible.

Do not invent missing fields.

---

# 1. Publication Existence Verification

First determine whether the publication itself can be confirmed.

Possible evidence:

* publisher page;
* DOI registration metadata;
* Crossref;
* PubMed record;
* Scopus direct record;
* OpenAlex record;
* official journal archive;
* trusted bibliographic database.

Use:

* `PUBLICATION_VERIFIED`
* `PUBLICATION_LIKELY`
* `PUBLICATION_NOT_VERIFIED`
* `PUBLICATION_NOT_FOUND`

Do not classify a paper as verified merely because a citation appears in another document.

---

# 2. Metadata Integrity

Verify that bibliographic elements belong to the same publication.

Check consistency among:

* title;
* authors;
* journal;
* year;
* DOI;
* volume;
* issue;
* pages or article number.

This protects against citation mashups.

Possible status:

* `METADATA_CONSISTENT`
* `METADATA_MINOR_VARIATION`
* `METADATA_CONFLICT`
* `METADATA_INCOMPLETE`
* `METADATA_UNVERIFIED`

Minor variations may include:

* punctuation;
* capitalization;
* author initials;
* online-first vs issue year.

Do not treat cosmetic differences as serious conflicts.

---

# 3. Title Verification

Confirm the canonical publication title where possible.

Compare:

* retrieved title;
* DOI metadata title;
* publisher title;
* database title.

Possible differences may arise from:

* subtitle omission;
* punctuation;
* capitalization;
* early-online version.

Do not rewrite titles based on memory.

---

# 4. Author Verification

Verify authorship against trusted metadata.

Check:

* author order;
* surnames;
* initials;
* major discrepancies.

Possible status:

* `AUTHORS_VERIFIED`
* `AUTHORS_MINOR_VARIATION`
* `AUTHORS_CONFLICT`
* `AUTHORS_UNVERIFIED`

Do not merge two papers merely because authors have similar names.

---

# 5. Publication Year Verification

Distinguish where necessary between:

* online-first year;
* issue year;
* accepted year;
* print year.

Do not label minor online-vs-print year differences as fabrication.

Preserve the bibliographic year appropriate to the citation style and source.

---

# 6. Journal Verification

Confirm that the journal exists and that the article belongs to it.

Verify where possible:

* official journal title;
* ISSN/eISSN;
* publisher;
* journal homepage;
* article placement.

Use:

* `JOURNAL_VERIFIED`
* `JOURNAL_UNVERIFIED`
* `JOURNAL_CONFLICT`

Do not infer legitimacy merely from a professional-looking website.

---

# 7. DOI Verification

When DOI is present:

1. normalize it;
2. confirm it resolves or matches trusted metadata;
3. compare DOI metadata with the candidate record.

Use:

* `DOI_VERIFIED`
* `DOI_METADATA_MISMATCH`
* `DOI_NOT_FOUND`
* `NO_DOI`
* `DOI_UNVERIFIED`

A DOI is not valid merely because it follows the pattern:

`10.xxxx/...`

---

# 8. DOI Metadata Match

A verified DOI should correspond to the same:

* title;
* journal;
* authors;
* publication.

If DOI metadata describes another paper:

classify:

`DOI_METADATA_MISMATCH`

Do not replace the DOI with a guessed alternative.

Search for the correct record.

---

# 9. DOI Absence

Some legitimate publications may have no DOI.

This is common in:

* older literature;
* some regional journals;
* books;
* standards;
* reports.

Do not automatically reject a publication without a DOI.

Use other verification routes.

---

# 10. ISSN Verification

When journal identity matters, verify:

* print ISSN;
* electronic ISSN;
* title association.

ISSN is especially useful for:

* journal disambiguation;
* Scopus source verification;
* title changes.

Do not invent ISSN values.

---

# 11. Publisher Verification

Verify the publisher when relevant.

Publisher information helps establish:

* official journal ownership;
* publication policy;
* journal legitimacy.

Do not assume a publisher is legitimate merely because its name resembles a major publisher.

---

# 12. Peer-Review Status

Determine whether the publication is peer-reviewed when this can be established.

Possible status:

* `PEER_REVIEWED`
* `LIKELY_PEER_REVIEWED`
* `NOT_PEER_REVIEWED`
* `PEER_REVIEW_STATUS_UNVERIFIED`

Possible non-peer-reviewed outputs include:

* preprints;
* editorials;
* letters;
* news;
* white papers;
* reports.

A journal article format alone does not prove peer review.

---

# 13. Document Type Verification

Classify where possible:

* journal article;
* review;
* systematic review;
* meta-analysis;
* conference paper;
* editorial;
* letter;
* book chapter;
* preprint;
* protocol;
* correction;
* retraction;
* guideline;
* report.

Document type matters for evidence interpretation.

Do not treat every retrieved record as a primary research article.

---

# 14. Scopus Source Status

Verify journal/source status where possible.

Use:

* `SCOPUS_SOURCE_ACTIVE`
* `SCOPUS_SOURCE_DISCONTINUED`
* `SCOPUS_SOURCE_NOT_FOUND`
* `SCOPUS_SOURCE_UNVERIFIED`

Do not say:

> This journal is Scopus indexed

unless this status has been verified.

---

# 15. Scopus Document Status

Keep document-level verification separate from source-level verification.

Use:

* `SCOPUS_DOCUMENT_VERIFIED`
* `SCOPUS_DOCUMENT_NOT_FOUND`
* `SCOPUS_DOCUMENT_UNVERIFIED`

A journal being active in Scopus does not automatically prove a particular article is indexed.

---

# 16. Historical Scopus Coverage

Where publication-year accuracy matters, verify whether the journal was covered at that time.

Use:

* `COVERAGE_AT_PUBLICATION_VERIFIED`
* `COVERAGE_AT_PUBLICATION_LIKELY`
* `COVERAGE_AT_PUBLICATION_NOT_FOUND`
* `COVERAGE_AT_PUBLICATION_UNVERIFIED`

This is important when:

* a journal entered Scopus later;
* coverage was interrupted;
* the journal was discontinued.

---

# 17. Discontinued Scopus Sources

If a journal is discontinued from Scopus:

do not automatically discard all historical articles.

Determine:

* whether it was covered at publication;
* why discontinuation occurred if relevant;
* whether the individual study is scientifically usable.

Use status transparently.

---

# 18. Scopus Claim Language

Use precise language.

Acceptable:

> The journal is currently verified as an active Scopus source.

or:

> Scopus status could not be verified.

Avoid:

> This is definitely a Scopus article.

unless document-level verification supports it.

---

# 19. PubMed Status

For biomedical records, PubMed may help verify publication identity.

Use:

* PMID;
* journal;
* title;
* metadata.

PubMed inclusion does not equal Scopus indexing.

Keep the two statuses separate.

---

# 20. OpenAlex Status

OpenAlex may support:

* existence verification;
* DOI matching;
* citation relationships;
* author metadata.

OpenAlex inclusion does not equal:

`SCOPUS_VERIFIED`

Use it as supporting bibliographic evidence.

---

# 21. Crossref Status

Crossref may support:

* DOI registration;
* title;
* author;
* publisher;
* publication date.

Crossref membership or registration does not establish:

* peer review;
* journal quality;
* Scopus indexing.

---

# 22. Semantic Scholar Status

Semantic Scholar may support:

* article discovery;
* citation relationships;
* metadata comparison.

Use as supplementary verification.

Do not use it alone to establish journal indexing.

---

# 23. Publisher Page as Primary Metadata

When available, the official publisher article page is a strong metadata source.

Use it to verify:

* title;
* authors;
* DOI;
* issue details;
* publication status.

However, publisher pages do not automatically prove Scopus indexing.

---

# 24. Predatory or Questionable Journal Signals

When journal legitimacy is uncertain, examine signals such as:

* unverifiable editorial board;
* fake indexing claims;
* misleading journal title;
* unclear publisher identity;
* extremely broad scope;
* suspicious peer-review claims;
* fabricated metrics;
* inconsistent archive;
* aggressive solicitation.

Do not label a journal "predatory" solely from one weak signal.

Use:

* `LEGITIMACY_VERIFIED`
* `LEGITIMACY_LIKELY`
* `QUESTIONABLE_SIGNAL`
* `LEGITIMACY_UNVERIFIED`

---

# 25. Journal Quality Is Not Evidence Quality

Do not infer:

Q1 = study methodologically strong.

Do not infer:

Q4 = study weak.

Source verification confirms publication integrity.

Scientific evidence quality must later consider the study itself.

---

# 26. Retraction Verification

Check retraction status when relevant.

Use:

* publisher notices;
* trusted retraction metadata;
* bibliographic databases.

Possible status:

* `NOT_KNOWN_RETRACTED`
* `RETRACTED`
* `EXPRESSION_OF_CONCERN`
* `RETRACTION_STATUS_UNVERIFIED`

Do not use retracted literature as supporting evidence.

---

# 27. Correction and Erratum

Check whether the article has:

* correction;
* erratum;
* corrigendum.

Use:

* `CORRECTION_PRESENT`
* `NO_CORRECTION_FOUND`
* `CORRECTION_STATUS_UNVERIFIED`

Determine whether correction materially changes:

* data;
* conclusions;
* bibliographic details.

---

# 28. Version of Record

When multiple versions exist:

* preprint;
* accepted manuscript;
* publisher version;

prefer the peer-reviewed version of record for final citation when available.

Keep earlier versions for historical or comparison purposes if necessary.

---

# 29. Duplicate Publication

Identify possible duplicates across:

* preprint vs published article;
* conference paper vs journal extension;
* duplicate database records;
* translated publication.

Use:

* `SAME_WORK_DIFFERENT_VERSION`
* `POSSIBLE_DUPLICATE_PUBLICATION`
* `DISTINCT_PUBLICATION`

Do not double count the same study.

---

# 30. Study-Level Duplicate

Two different articles may report results from the same dataset.

Flag:

`POSSIBLE_SHARED_DATASET`

when supported.

This is especially important for:

* systematic reviews;
* meta-analysis;
* evidence synthesis.

Do not assume shared datasets without evidence.

---

# 31. Reference Mashup Detection

A common hallucination pattern combines:

* one real title;
* different authors;
* wrong journal;
* unrelated DOI.

If metadata do not belong together, classify:

`REFERENCE_MASHUP`

This source must not enter the verified evidence set.

---

# 32. Citation Hallucination Detection

Possible warning signs:

* DOI resolves to unrelated article;
* title cannot be found in scholarly databases;
* journal volume/year combination impossible;
* authors mismatch all official sources;
* journal does not exist;
* citation exists only in AI-generated text.

Use:

`POTENTIAL_HALLUCINATED_REFERENCE`

until disproven or confirmed.

---

# 33. User-Provided References

Treat user-provided citations respectfully but verify them before scientific use when verification is required.

Do not assume the user intentionally supplied incorrect information.

Possible result:

> The citation appears to contain a DOI mismatch. The title exists, but the DOI belongs to another article.

Keep the correction evidence-based.

---

# 34. Previously Published Manuscript References

When auditing a previous paper, do not automatically reverify every reference unless required.

Prioritize verification of:

* critical scientific claims;
* questionable records;
* references reused in new manuscript;
* novelty-defining sources;
* target-journal positioning sources.

---

# 35. Evidence Role Classification

After source verification, classify its possible role:

* `CORE_EVIDENCE`
* `SUPPORTING_EVIDENCE`
* `CONTRADICTORY_EVIDENCE`
* `FOUNDATIONAL_EVIDENCE`
* `METHODOLOGICAL_EVIDENCE`
* `CONTEXTUAL_EVIDENCE`
* `EMERGING_EVIDENCE`

Role does not equal quality.

---

# 36. Evidence Design Classification

Where possible, identify:

* systematic review;
* meta-analysis;
* RCT;
* cohort;
* case-control;
* cross-sectional;
* qualitative;
* laboratory;
* simulation;
* validation;
* methodological paper.

This supports downstream evidence evaluation.

---

# 37. Evidence Quality Handoff

Do not conduct a complete risk-of-bias assessment here unless another skill requires it.

Source verification asks:

> Is this a legitimate and traceable scholarly source?

Evidence synthesis later asks:

> How strong is the evidence?

Keep those responsibilities separate.

---

# 38. Verification Confidence

Assign:

* `HIGH_CONFIDENCE`
* `MODERATE_CONFIDENCE`
* `LOW_CONFIDENCE`
* `UNVERIFIED`

Confidence should reflect the number and quality of independent verification signals.

---

# 39. Minimum Verification Rule

For a source to enter the verified evidence set, ideally confirm:

1. publication exists;
2. title matches;
3. authors substantially match;
4. journal matches;
5. publication year is defensible;
6. DOI matches if DOI exists;
7. peer-review/document status is understood;
8. retraction status is not problematic;
9. claimed Scopus status is verified separately if being claimed.

Not every historical source will satisfy every metadata field.

Use proportional judgment.

---

# 40. Verification Tiers

Use when useful:

## Tier V1 — Identity Verified

Publication existence and core metadata verified.

## Tier V2 — Scholarly Status Verified

V1 plus document type and peer-review status reasonably established.

## Tier V3 — Indexing Verified

V2 plus Scopus source/document status verified when relevant.

## Tier V4 — Integrity Checked

V3 plus retraction/correction and metadata-integrity checks.

Do not imply evidence quality from the tier.

---

# 41. Verification Outcome

Use:

* `VERIFIED_FOR_USE`
* `VERIFIED_WITH_NOTE`
* `USE_WITH_CAUTION`
* `UNVERIFIED_DO_NOT_USE`
* `RETRACTED_DO_NOT_USE`
* `REFERENCE_MASHUP_DO_NOT_USE`

Explain important notes.

---

# 42. Verified Reference Record

Recommended structure:

```yaml
reference:
  title:
  authors:
  year:
  journal:
  doi:
  issn:
  publisher:
  document_type:

verification:
  publication_status:
  metadata_status:
  doi_status:
  peer_review_status:
  journal_legitimacy:
  scopus_source_status:
  scopus_document_status:
  scopus_coverage_at_publication:
  retraction_status:
  correction_status:
  confidence:
  outcome:

provenance:
  providers_checked:
  verification_date:
```

Unknown fields remain unknown.

---

# 43. Verification Date

Scopus coverage, journal status, and publication policies can change.

Record:

`verification_date`

for time-sensitive verification.

Do not imply that old verification remains permanently current.

---

# 44. Verification Provider Independence

When possible, corroborate critical metadata using more than one source.

Example:

```text
Publisher
+
Crossref
+
Scopus
```

or:

```text
PubMed
+
Publisher
+
Crossref
```

Independent agreement increases confidence.

---

# 45. Verification Conflict

If providers disagree:

do not silently choose whichever supports the preferred conclusion.

Record:

`VERIFICATION_CONFLICT`

Investigate:

* version differences;
* metadata errors;
* online-first dates;
* journal title changes;
* source coverage differences.

---

# 46. Search Result vs Verification

Do not confuse:

`DISCOVERED`

with:

`VERIFIED`

A source can be discovered by any provider but still fail verification.

---

# 47. Scopus-First Does Not Lower Verification Standards

A record appearing in a Scopus search is strong indexing evidence.

However, citation metadata should still be internally consistent.

Do not copy incorrect metadata blindly if another verified source reveals an error.

---

# 48. Non-Scopus Authoritative Sources

Some legitimate sources are intentionally outside Scopus.

Examples:

* WHO guideline;
* government regulation;
* ISO standard;
* national statistical report;
* official technical guidance.

Use:

`AUTHORITATIVE_NON_SCOPUS_SOURCE`

where appropriate.

Do not describe them as inferior merely because they are not journal articles.

---

# 49. Preprint Handling

Use:

`PREPRINT_NOT_PEER_REVIEWED`

When a peer-reviewed version exists:

prefer:

`PEER_REVIEWED_VERSION`

for final evidence.

Do not cite both as independent studies when they represent the same work.

---

# 50. Conference Paper Handling

In disciplines where conference proceedings are major scholarly outlets, assess according to disciplinary norms.

Do not automatically downgrade them solely because they are conference papers.

Still verify:

* venue;
* authors;
* title;
* DOI;
* publication.

---

# 51. Thesis and Dissertation Handling

Theses and dissertations may provide useful:

* methods;
* data;
* contextual evidence.

They are not equivalent to peer-reviewed journal articles.

Classify appropriately.

---

# 52. Systematic Review Verification

For review articles, verify:

* publication exists;
* review type;
* journal;
* DOI;
* peer review;
* indexing.

Downstream synthesis should separately evaluate review quality.

---

# 53. Meta-Analysis Verification

Meta-analysis status should be verified from the article itself.

Do not infer from title alone.

---

# 54. Citation Count

Citation count may be preserved as contextual metadata.

Do not use citation count to decide whether a source is true.

---

# 55. Journal Metrics

Quartile, CiteScore, SJR, or impact metrics are not required for basic source verification.

They belong primarily to:

* journal evaluation;
* publication strategy.

Do not confuse journal metrics with source identity.

---

# 56. APC Status Separation

APC status is irrelevant to whether a source is valid evidence.

Do not downgrade or exclude evidence because the source journal charges APC.

Publication-cost policy belongs to later journal selection.

---

# 57. Target-Journal Source Verification

Articles from a target journal must undergo the same verification standards as all other sources.

Do not lower standards because citing them may appear strategically useful.

---

# 58. Citation Padding Guard

If a target-journal article has weak relevance:

do not classify it as core evidence.

Scientific relevance determines citation use.

---

# 59. False Scopus Claim Prevention

Never infer Scopus indexing from:

* publisher reputation;
* journal website badge;
* Google Scholar;
* Crossref;
* PubMed;
* OpenAlex;
* Semantic Scholar;
* DOAJ alone.

Use actual verification where possible.

---

# 60. Source Verification Output

When reporting a small set of sources, use:

| Source | Publication | DOI | Peer Review | Scopus Source | Scopus Document | Integrity | Outcome |
| ------ | ----------- | --- | ----------- | ------------- | --------------- | --------- | ------- |

Avoid displaying unavailable metadata as if verified.

---

# 61. Verification Failure Reasons

Possible reasons include:

* publication cannot be found;
* DOI mismatch;
* author mismatch;
* title mismatch;
* journal mismatch;
* source unverifiable;
* suspected duplicate;
* retraction;
* questionable publication status.

Record the reason explicitly.

---

# 62. Verification Recovery

When verification fails:

1. search exact title;
2. search DOI;
3. search title + first author;
4. search journal archive;
5. check Crossref;
6. check publisher;
7. check PubMed/OpenAlex when relevant;
8. check Scopus status separately.

Do not immediately discard a potentially legitimate source without reasonable verification effort.

---

# 63. Gray Zone Rule

If verification remains unresolved:

use:

`UNVERIFIED_DO_NOT_USE`

for evidence-dependent claims.

This implements a conservative integrity policy.

Do not use:

> probably real

as sufficient verification.

---

# 64. Final Reference Eligibility

A source may enter final references when:

* it is actually cited in the text;
* its metadata are verified enough for accurate citation;
* its scientific role is legitimate;
* it is not retracted;
* it is relevant.

Do not add verified references that are never used.

---

# 65. Relationship with Scopus Literature Search

`scopus-literature-search` discovers.

`source-verification` verifies.

Do not repeat broad literature searching here except when necessary to resolve verification.

---

# 66. Relationship with Reference Integrity Guard

`source-verification` validates individual sources.

`reference-integrity-guard` later audits the complete citation and reference system across a research output.

Conceptually:

```text
DISCOVER
   ↓
VERIFY SOURCE
   ↓
USE SOURCE
   ↓
GUARD ENTIRE REFERENCE SYSTEM
```

---

# 67. Relationship with Literature Screening

A verified source may still be irrelevant.

`literature-screening`

determines inclusion for a specific research purpose.

Verification does not equal inclusion.

---

# 68. Relationship with Evidence Synthesis

Only verified and appropriately screened sources should feed:

`evidence-synthesis`

when evidence-dependent scientific conclusions are being formed.

---

# 69. Relationship with Gap Validation

Research-gap claims must not rely on unverified sources.

Pass verified literature to:

`gap-validator`

---

# 70. Relationship with Novelty

Novelty must not rely on:

* fabricated citations;
* unverified competitor studies;
* false absence assumptions.

Verified literature is required before:

`novelty-builder`
and:
`novelty-auditor`

---

# 71. Relationship with Manuscript Writing

Before final manuscript citation use:

all critical references should have adequate verification.

No invented or mashup references may enter the manuscript.

---

# 72. Research Passport Update

When supported, update:

```yaml
source_verification:
  records:
    - reference_id:
      publication_status:
      metadata_status:
      doi_status:
      peer_review_status:
      journal_legitimacy:
      scopus_source_status:
      scopus_document_status:
      retraction_status:
      correction_status:
      confidence:
      outcome:
      providers_checked:
      verification_date:
  verified_count:
  unverified_count:
  excluded_count:
  conflicts:
  next_stage:
```

Do not fabricate counts.

---

# 73. User-Friendly Behavior

Do not overwhelm users with metadata unless relevant.

Prefer:

> This article is real and the DOI matches the publisher record. The journal's Scopus source status is verified, but I have not yet verified the article at document level.

rather than:

> Verified.

Precision builds trust.

---

# 74. Avoid These Behaviors

Do not:

* fabricate verification;
* claim Scopus based on publisher reputation;
* assume DOI syntax means validity;
* ignore DOI mismatch;
* merge metadata from different papers;
* treat source discovery as verification;
* treat peer review as automatic;
* hide retractions;
* treat target-journal papers preferentially;
* use APC status to judge scientific validity;
* equate journal quartile with evidence quality.

---

# Stop Conditions

Do not allow a source to support a critical scientific claim when:

* publication existence is not verified;
* metadata are materially conflicting;
* DOI belongs to another article;
* retraction invalidates the source;
* Scopus status is being claimed without verification;
* the record appears to be a citation mashup.

Resolve or exclude the source.

---

# Success Criterion

`source-verification` succeeds when every source intended for scientific use has a defensible identity, consistent bibliographic metadata, understood publication and peer-review status, transparent Scopus-status verification where relevant, integrity checks for correction or retraction, and a clear eligibility outcome before entering the evidence base.
