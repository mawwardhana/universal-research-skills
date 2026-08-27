---
name: data-quality-auditor
description: Audit governed research data for structural integrity, semantic consistency, value validity, duplicate and linkage integrity, missingness, temporal coherence, derived-variable correctness, outlier provenance, and fitness for the intended analysis. Use after research-data-governance has established source, version, variable meaning, transformation history, and access status, and before analysis-planner or statistical-method-selector finalizes analytical strategy. This skill distinguishes data errors from legitimate unusual observations, documents correction decisions, prevents result-driven cleaning, and produces a transparent analysis-readiness decision without silently deleting, recoding, imputing, or transforming data.
---

# Data Quality Auditor

## Purpose

`data-quality-auditor` evaluates whether governed research data are sufficiently coherent, plausible, internally consistent, traceable, and fit for the intended scientific analysis.

Its central question is:

> Given the governed dataset, its provenance, intended scientific use, expected structure, and documented measurement rules, what actual data-quality problems exist, which unusual values are legitimate, what requires correction or clarification, and is the dataset ready to support the planned analysis?

This skill does not perform cosmetic “data cleaning.”

It performs a scientific audit of the actual data.

The governing logic is:

```text
GOVERNED DATA
      ↓
STRUCTURAL INTEGRITY
      ↓
SEMANTIC INTEGRITY
      ↓
VALUE VALIDITY
      ↓
LOGICAL CONSISTENCY
      ↓
TEMPORAL CONSISTENCY
      ↓
DUPLICATE / LINKAGE INTEGRITY
      ↓
MISSINGNESS AUDIT
      ↓
DERIVED-VARIABLE AUDIT
      ↓
OUTLIER PROVENANCE
      ↓
ANALYSIS READINESS
```

---

# 1. Core Principles

The auditor must preserve the following principles:

```text
OUTLIER ≠ ERROR
MISSING ≠ ZERO
DUPLICATE ≠ ALWAYS DELETE
UNUSUAL VALUE ≠ INVALID VALUE
NON-NORMAL ≠ BAD DATA
STATISTICALLY INCONVENIENT ≠ BAD DATA
MODEL FAILURE ≠ DATA ERROR
SIGNIFICANCE ≠ DATA QUALITY
```

A data point should be corrected, excluded, recoded, or imputed only when there is a defensible reason independent of whether the resulting statistical findings become more desirable.

---

# 2. Activation Gate

Use `data-quality-auditor` when:

- a governed dataset exists;
- raw or source provenance is known;
- variable meaning is sufficiently documented;
- the user wants to prepare data for analysis;
- data have been merged or linked;
- derived variables have been created;
- missingness is substantial or unclear;
- outliers or impossible values are suspected;
- repeated measures or longitudinal data need consistency checks;
- laboratory or instrument outputs require quality review;
- manuscript or reviewer questions depend on data integrity;
- prior analyses may have used questionable data-cleaning decisions;
- or the dataset has not yet received a systematic quality audit.

Do not use this skill as a substitute for `research-data-governance`.

If provenance, variable definitions, or dataset version are unresolved, route upstream first.

---

# 3. Required Upstream Inputs

Use, when available:

- dataset identifier;
- dataset version;
- source data description;
- raw-data status;
- data dictionary;
- codebook;
- transformation log;
- sampling frame;
- inclusion criteria;
- exclusion criteria;
- unit of analysis;
- unit of observation;
- variable roles;
- valid ranges;
- valid categories;
- expected units;
- date rules;
- repeated-measure structure;
- merge or linkage rules;
- derived-variable formulas;
- missing-value codes;
- instrument version;
- laboratory reference information;
- expected row count;
- expected participant count;
- protocol constraints;
- analysis target;
- and known data issues.

Do not invent expected ranges or category rules when they are not available.

---

# 4. Quality Audit Scope

Audit, where relevant:

- file integrity;
- row and column structure;
- identifiers;
- data types;
- labels;
- allowed values;
- units;
- numeric ranges;
- categorical levels;
- impossible values;
- internal logic;
- cross-variable consistency;
- temporal consistency;
- repeated measures;
- duplicates;
- merge integrity;
- linkage integrity;
- missingness;
- derived variables;
- scoring;
- transformations;
- laboratory plausibility;
- device or batch effects;
- outlier provenance;
- sample-size consistency;
- eligibility consistency;
- and analysis readiness.

---

# 5. Quality Audit Levels

Use three levels:

## Level 1 — Structural Integrity

Checks whether the dataset is technically coherent.

Examples:

- expected files exist;
- expected columns exist;
- column names are unique;
- identifiers are present;
- data types are interpretable;
- row count is plausible;
- encoding is stable;
- delimiters are correct;
- dates parse correctly.

## Level 2 — Semantic Integrity

Checks whether values match the intended scientific meaning.

Examples:

- sex codes match the codebook;
- laboratory units are correct;
- visit labels correspond to protocol;
- outcome coding is consistent;
- derived variables use the correct source variables.

## Level 3 — Scientific Fitness

Checks whether the data can support the intended inference.

Examples:

- required outcome is sufficiently available;
- exposure and outcome timing are interpretable;
- repeated observations can be linked;
- major exclusions are defensible;
- critical covariates are not structurally absent;
- analysis unit is not violated by duplicates or merge errors.

---

# 6. Audit Status

Use one of:

- `DATA_QUALITY_PASS`
- `DATA_QUALITY_PASS_WITH_LIMITATIONS`
- `DATA_QUALITY_REQUIRES_CORRECTION`
- `DATA_QUALITY_REQUIRES_REVIEW`
- `DATA_QUALITY_BLOCKED`
- `DATA_QUALITY_NOT_APPLICABLE`

Do not declare `PASS` merely because automated checks return no errors.

---

# 7. Analysis Readiness Status

Use:

- `NOT_READY_FOR_ANALYSIS`
- `READY_AFTER_MINOR_CORRECTION`
- `READY_AFTER_DOCUMENTED_CORRECTION`
- `READY_WITH_LIMITATIONS`
- `READY_FOR_ANALYSIS_PLANNING`
- `LOCKED_FOR_ANALYSIS`

---

# 8. Error Classification

Classify each issue as:

- `CONFIRMED_ERROR`
- `PROBABLE_ERROR`
- `POSSIBLE_ERROR`
- `LEGITIMATE_UNUSUAL_VALUE`
- `EXPECTED_VARIATION`
- `STRUCTURAL_MISSINGNESS`
- `UNRESOLVED`
- `NOT_AN_ERROR`

Do not collapse uncertain values into confirmed errors.

---

# 9. Severity Classification

Use:

- `CRITICAL`
- `MAJOR`
- `MODERATE`
- `MINOR`
- `INFORMATIONAL`

A critical issue threatens the validity, traceability, or interpretability of the study.

---

# 10. Correction Decision

For every issue, use one of:

- `CORRECT`
- `RETAIN`
- `RECODE`
- `RELINK`
- `RECALCULATE`
- `RE-EXTRACT`
- `QUERY_SOURCE`
- `FLAG_ONLY`
- `EXCLUDE_WITH_JUSTIFICATION`
- `QUARANTINE`
- `NO_ACTION`
- `UNRESOLVED`

Never default automatically to deletion.

---

# 11. Structural File Checks

Check, where relevant:

- file opens correctly;
- file format matches expectation;
- encoding is valid;
- delimiter is correct;
- header row is correct;
- there are no hidden duplicated headers;
- no unexpected blank columns;
- no unexpected trailing rows;
- row count is plausible;
- column count is plausible;
- file version matches governance record.

---

# 12. Dataset Identity Check

Verify:

```yaml
dataset_identity:
  dataset_id:
  dataset_name:
  dataset_version:
  source_dataset:
  governed_status:
  analysis_target:
  audit_date:
  auditor_role:
```

If the dataset version cannot be identified, stop.

---

# 13. Row Count Audit

Compare:

- expected rows;
- observed rows;
- expected unique units;
- observed unique units;
- expected repeated measures;
- observed repeated measures.

A difference is not automatically an error.

Investigate.

---

# 14. Column Count Audit

Compare:

- expected variables;
- observed variables;
- missing expected variables;
- unexpected variables;
- duplicated variable names;
- renamed variables;
- deprecated variables.

---

# 15. Identifier Integrity

Check identifiers for:

- missing IDs;
- duplicate IDs;
- malformed IDs;
- unexpected prefixes;
- inconsistent length;
- leading-zero loss;
- spreadsheet scientific-notation conversion;
- accidental numeric conversion;
- reused identifiers;
- inconsistent case;
- whitespace.

Do not treat repeated participant IDs as duplicates when repeated measures are expected.

---

# 16. Unique Key Audit

Determine the intended unique key.

Examples:

```text
participant_id
participant_id + visit
sample_id
site_id + participant_id
study_id + outcome_id
```

Test whether observed data satisfy expected uniqueness.

---

# 17. Cardinality Audit

For merged data verify expected cardinality:

- one-to-one;
- one-to-many;
- many-to-one;
- many-to-many.

Unexpected many-to-many relationships are high-risk.

---

# 18. Data Type Audit

Check whether variables are stored and interpreted consistently as:

- integer;
- decimal;
- string;
- date;
- datetime;
- boolean;
- categorical;
- ordinal;
- binary;
- identifier.

Do not coerce data types silently.

---

# 19. Numeric-as-Text Audit

Check for:

- commas;
- decimal separators;
- unit suffixes;
- spaces;
- symbols;
- text placeholders;
- non-breaking spaces.

Examples:

```text
"12 mg"
"1,25"
"<0.05"
"ND"
"NA"
```

Each requires interpretation before conversion.

---

# 20. Text-as-Code Audit

Check categorical variables for mixed representations such as:

```text
1
"1"
"Male"
"M"
"male"
"MALE"
```

Do not recode until the codebook or source meaning is verified.

---

# 21. Category Level Audit

For each categorical variable compare:

- expected levels;
- observed levels;
- rare levels;
- unknown levels;
- misspellings;
- capitalization variants;
- leading/trailing spaces;
- retired codes;
- newly introduced codes.

---

# 22. Binary Variable Audit

Confirm that binary variables truly use two scientific states.

Examples:

```text
0 / 1
No / Yes
Absent / Present
Control / Intervention
```

Do not assume `0` and `1` meaning without the codebook.

---

# 23. Ordinal Variable Audit

Check:

- category order;
- score direction;
- skipped categories;
- reverse order;
- unknown labels.

Do not treat ordinal values as continuous merely because stored numerically.

---

# 24. Range Audit

For numeric variables define, where justified:

```yaml
range_rule:
  variable:
  minimum:
  maximum:
  basis:
  unit:
  hard_or_soft:
```

Distinguish:

- hard impossible range;
- expected physiological range;
- instrument range;
- operational range;
- statistical expectation.

---

# 25. Hard vs Soft Range

Hard range example:

```text
age < 0
```

Soft range example:

```text
heart rate = 190
```

The latter may be unusual but possible.

Do not delete soft-range observations automatically.

---

# 26. Unit Consistency Audit

Check:

- recorded unit;
- source unit;
- analysis unit;
- conversion history;
- mixed units within one variable;
- site-specific units;
- instrument-specific units.

Flag mixed-unit variables as high-risk.

---

# 27. Decimal and Locale Audit

Check whether values use:

```text
1.25
1,25
```

and whether the system interpreted them correctly.

Also check thousands separators.

---

# 28. Date Parsing Audit

Check:

- invalid dates;
- ambiguous date formats;
- month/day reversal;
- impossible calendar dates;
- timezone shifts;
- missing year;
- Excel serial dates;
- text dates.

---

# 29. Temporal Order Audit

Evaluate scientific sequences such as:

```text
birth_date
    <
enrollment_date
    ≤
intervention_date
    ≤
followup_date
    ≤
outcome_date
```

Adapt to study design.

---

# 30. Negative Duration Audit

Check for impossible or suspicious:

- negative follow-up;
- negative age;
- negative time-to-event;
- specimen collected after reported result date if impossible;
- discharge before admission;
- intervention before eligibility.

---

# 31. Repeated Measure Audit

For longitudinal data check:

- expected visits;
- duplicate visits;
- skipped visits;
- out-of-order visits;
- duplicated timestamps;
- inconsistent participant linkage;
- impossible time intervals.

---

# 32. Eligibility Consistency

Compare observed records against documented eligibility criteria.

Possible statuses:

- eligible;
- ineligible;
- eligibility unresolved;
- protocol deviation.

Do not silently exclude ineligible records before determining their role.

---

# 33. Inclusion/Exclusion Audit

Every analytical exclusion should be traceable to:

- protocol;
- prespecified analysis rule;
- quality failure;
- source error;
- scientifically justified post-hoc decision.

Do not exclude because of statistical inconvenience.

---

# 34. Cross-Variable Logic

Define rules such as:

```text
pregnancy = yes → sex variable must be compatible with study definition
death_date present → death_event should indicate event
medication_dose > 0 → medication_exposure should not be absent
followup_days = 0 → followup_date should equal baseline date
```

Use study-specific rules.

---

# 35. Conditional Logic Audit

Check variables that should only exist under conditions.

Examples:

```text
smoking_pack_years
```

may be applicable only to ever-smokers.

Do not classify structurally inapplicable fields as ordinary missing data.

---

# 36. Impossible Combination Audit

Examples:

- mutually exclusive categories both marked yes;
- intervention group inconsistent with randomization record;
- biological sample type inconsistent with assay;
- age inconsistent with date of birth;
- sex-specific procedure in incompatible record;
- impossible medication route.

Use domain evidence, not stereotype.

---

# 37. Duplicate Record Audit

Classify duplicates as:

- exact row duplicate;
- duplicate import;
- duplicate person;
- legitimate repeated encounter;
- repeated specimen;
- repeated test;
- duplicate linkage;
- unresolved.

---

# 38. Exact Duplicate Check

Exact duplicate rows may arise from:

- repeated import;
- concatenation;
- export error.

Even exact duplicates should be verified before deletion.

---

# 39. Near-Duplicate Check

Near duplicates may differ only in:

- timestamp;
- whitespace;
- one field;
- source record;
- corrected value.

Investigate whether they represent legitimate repeated observations.

---

# 40. Participant Duplicate Check

A participant may legitimately have:

- multiple visits;
- multiple samples;
- multiple outcomes;
- multiple admissions.

Use the intended observational unit.

---

# 41. Merge Integrity Audit

For each merge verify:

- key;
- expected cardinality;
- unmatched left records;
- unmatched right records;
- duplicate keys;
- row inflation;
- row loss;
- variable conflicts;
- suffix collisions.

---

# 42. Row Inflation Audit

Unexpected row multiplication after a merge is a critical warning.

Example:

```text
100 participants
before merge

250 rows
after supposed one-to-one merge
```

Investigate cardinality.

---

# 43. Row Loss Audit

Unexpected row loss may indicate:

- inner join;
- failed linkage;
- missing key;
- filtering;
- deduplication.

Trace the cause.

---

# 44. Linkage Quality Audit

For linked datasets assess:

- match rate;
- unmatched records;
- ambiguous matches;
- duplicate matches;
- false-match risk;
- missed-match risk;
- deterministic vs probabilistic linkage;
- clerical review status.

---

# 45. Linkage Uncertainty

If linkage is imperfect, preserve uncertainty.

Do not silently convert uncertain matches into exact identity.

---

# 46. Missingness Audit

Audit missing data by:

- variable;
- participant;
- timepoint;
- site;
- group;
- source;
- batch;
- reason;
- missingness code.

---

# 47. Missingness Type

Distinguish:

- source missing;
- structural missing;
- not applicable;
- not measured;
- refused;
- lost record;
- below detection limit;
- merge-created missing;
- derived-variable missing;
- censored;
- unknown.

---

# 48. Missingness Pattern

Assess whether missingness clusters by:

- treatment group;
- outcome status;
- site;
- time;
- instrument;
- severity;
- exposure;
- demographic subgroup.

Do not infer MCAR, MAR, or MNAR solely from visual pattern.

---

# 49. Missingness Threshold Guard

Do not apply universal rules such as:

```text
delete variable if >20% missing
```

without scientific justification.

Thresholds depend on:

- variable importance;
- study design;
- missingness mechanism;
- sample size;
- analysis method.

---

# 50. Zero vs Missing Audit

Verify whether zero means:

- true zero;
- not measured;
- below detection;
- absent;
- missing placeholder.

This is a common high-impact error.

---

# 51. Sentinel Value Audit

Check codes such as:

```text
9
99
999
-1
-9
9999
```

against the codebook.

Do not analyze sentinel missing codes as real measurements.

---

# 52. Blank String Audit

Blank values may represent:

- missing;
- whitespace;
- not applicable;
- failed import;
- hidden characters.

Inspect before recoding.

---

# 53. Derived Variable Audit

For each important derived variable verify:

- source variables;
- formula;
- units;
- missingness rule;
- rounding;
- threshold;
- category assignment;
- version;
- reproducibility.

---

# 54. Formula Recalculation

Recalculate derived variables independently where feasible.

Compare:

```text
stored_value
vs
recomputed_value
```

Record discrepancies.

---

# 55. Score Audit

For scales verify:

- item inclusion;
- reverse scoring;
- missing-item rules;
- weighting;
- subscale composition;
- total score range;
- instrument version.

---

# 56. Reverse-Scored Item Audit

A common error is failing to reverse-code items.

Verify direction against instrument documentation.

---

# 57. Threshold Audit

For categorized continuous variables document:

- threshold source;
- inclusive/exclusive boundary;
- unit;
- version;
- clinical or scientific basis.

---

# 58. Unit-Derived Variable Audit

Derived values may be wrong even when source values are individually correct if units are inconsistent.

Example:

```text
weight in grams
height in meters
BMI formula applied without conversion
```

---

# 59. Laboratory Data Audit

Where relevant check:

- impossible values;
- reference units;
- detection limits;
- instrument flags;
- calibration;
- batch;
- sample ID;
- rerun status;
- duplicate assays;
- hemolysis or specimen quality flags;
- reference range context.

---

# 60. Laboratory Reference Range Guard

Do not use population reference ranges as automatic invalidity thresholds.

A pathological value may be scientifically valid.

---

# 61. Detection Limit Audit

Distinguish:

- `BLD` — below detection limit;
- `BLQ` — below quantification limit;
- true zero;
- missing;
- failed assay.

Do not automatically substitute zero.

---

# 62. Batch Effect Audit

Check values by:

- batch;
- plate;
- run;
- machine;
- site;
- operator;
- reagent lot.

Unexpected clusters may indicate technical artifacts.

---

# 63. Instrument Audit

Where instrument metadata exist assess:

- calibration status;
- version;
- firmware;
- device switch;
- protocol change;
- unit change.

---

# 64. Survey Data Audit

Check:

- impossible response codes;
- skip-logic violations;
- duplicate submissions;
- completion time anomalies;
- straight-lining where relevant;
- contradictory responses;
- reverse scoring;
- scale completeness.

Do not automatically exclude respondents based on speed alone.

---

# 65. Qualitative Data Audit

For qualitative corpora assess:

- missing transcripts;
- corrupted recordings;
- transcript completeness;
- speaker labeling;
- anonymization;
- translation status;
- duplicate transcript versions;
- transcription discrepancies;
- codebook version alignment.

Do not reduce qualitative quality to numeric completeness.

---

# 66. Genomic Data Audit

Where relevant check:

- sample ID consistency;
- reference build;
- sequence quality;
- strand orientation;
- duplicated samples;
- contamination indicators;
- call rate;
- allele coding;
- reference/alternate consistency;
- batch;
- annotation version.

---

# 67. Imaging Data Audit

Check:

- image completeness;
- modality;
- acquisition parameters;
- corrupt files;
- duplicate images;
- patient-image linkage;
- preprocessing version;
- segmentation consistency;
- annotation consistency.

---

# 68. Pharmacokinetic Data Audit

Check:

- dose;
- dose unit;
- dosing time;
- sampling time;
- concentration unit;
- BLQ coding;
- duplicate samples;
- impossible time sequence;
- infusion duration;
- route;
- derived PK metrics;
- digitization provenance.

---

# 69. PBPK Data Audit

Distinguish:

- observed data;
- input parameters;
- simulation outputs;
- model versions;
- scenario variants.

Do not mix simulated and observed values.

---

# 70. Time-Series Audit

Check:

- time order;
- duplicate timestamps;
- irregular spacing;
- missing intervals;
- timezone;
- daylight-saving effects where relevant;
- sensor resets;
- clock drift.

---

# 71. Multisite Data Audit

Audit by site:

- coding;
- units;
- missingness;
- protocol deviations;
- recruitment pattern;
- measurement instruments;
- data completeness;
- harmonization quality.

Do not erase site-specific anomalies before investigation.

---

# 72. Outlier Audit

Outlier detection must be separated into:

```text
STATISTICAL UNUSUALNESS
vs
SCIENTIFIC INVALIDITY
```

A statistical outlier may be a true observation.

---

# 73. Outlier Provenance

For every flagged outlier record:

```yaml
outlier_review:
  record_id:
  variable:
  value:
  detection_method:
  source_verified:
  plausible:
  measurement_context:
  related_variables:
  decision:
  rationale:
  retained_value:
```

---

# 74. Outlier Detection Methods

Possible methods include:

- range checks;
- boxplot/IQR;
- robust z-score;
- standard z-score;
- leverage;
- residual diagnostics;
- domain threshold;
- multivariate distance;
- time-series anomaly;
- instrument flag.

No single method defines invalidity.

---

# 75. Univariate Outlier Guard

A value may be extreme univariately but plausible given:

- age;
- disease severity;
- treatment;
- subgroup;
- site;
- batch.

Context matters.

---

# 76. Multivariate Outlier Guard

A combination of individually plausible values may be inconsistent.

Example:

```text
weight = 45 kg
height = 2.10 m
BMI = 45
```

The derived value signals inconsistency.

---

# 77. Result-Blind Quality Rule

Quality decisions should ideally be made without considering whether they improve the preferred result.

Do not use:

- p-value;
- effect direction;
- significance;
- reviewer preference;
- journal prestige

as data-quality criteria.

---

# 78. Normality Guard

Non-normality is a distributional property.

It is not a data-quality defect.

Do not delete valid values to make a variable normal.

---

# 79. Homoscedasticity Guard

Heteroscedasticity is an analytical issue, not automatically a data error.

---

# 80. Model Convergence Guard

Model non-convergence may arise from:

- data sparsity;
- model specification;
- separation;
- collinearity;
- scale;
- optimization.

Do not assume data are “bad.”

---

# 81. Small Cell Audit

Check sparse categories when they affect:

- privacy;
- model estimation;
- subgroup interpretation;
- disclosure risk.

Do not collapse categories solely for significance.

---

# 82. Class Imbalance

In predictive datasets, class imbalance is not a quality defect by itself.

It may require analytical strategy.

---

# 83. Reproducible Correction Rule

Every correction should be reproducible.

Prefer:

```text
scripted correction
or
documented transformation
```

over silent manual editing.

---

# 84. Manual Correction Record

If manual correction is necessary:

```yaml
manual_correction:
  issue_id:
  record_id:
  variable:
  original_value:
  corrected_value:
  evidence:
  reason:
  date:
  responsible_role:
  verification:
```

---

# 85. Source Query Rule

When an observation is suspicious but unresolved:

- query source;
- inspect original record;
- inspect instrument;
- inspect case-report form;
- inspect source document.

Do not guess.

---

# 86. Correction Hierarchy

Prefer:

```text
SOURCE CORRECTION
      ↓
VERIFIED DATA CORRECTION
      ↓
DOCUMENTED ANALYSIS CORRECTION
```

Avoid correcting downstream while leaving an authoritative source silently wrong when governance permits source correction.

---

# 87. Quarantine

Use `QUARANTINE` when records are:

- structurally corrupted;
- source unresolved;
- linkage unresolved;
- privacy-compromised;
- or clearly not safe for current analysis.

Quarantine is not deletion.

---

# 88. Exclusion Rule

Exclusion is defensible when:

- prespecified;
- scientifically justified;
- source error confirmed;
- observation not part of target population;
- measurement invalid;
- or data unusable for the defined endpoint.

Record impact.

---

# 89. Sensitivity Preservation

When uncertain data decisions materially affect inference, preserve alternate defensible versions for sensitivity analysis.

Do not pretend one uncertain decision is uniquely correct.

---

# 90. Data Issue Register

Use:

```yaml
data_issue:
  issue_id:
  dataset_version:
  record_scope:
  variable_scope:
  issue_type:
  severity:
  evidence:
  error_status:
  decision:
  correction:
  rationale:
  verification:
  downstream_impact:
  status:
```

---

# 91. Issue Status

Use:

- `OPEN`
- `UNDER_REVIEW`
- `SOURCE_QUERY`
- `CORRECTED`
- `RETAINED_AS_VALID`
- `EXCLUDED_WITH_JUSTIFICATION`
- `QUARANTINED`
- `RESOLVED`
- `UNRESOLVED`

---

# 92. Quality Rules Register

Maintain:

| Rule ID | Variable/Scope | Rule | Basis | Severity | Action |
|---|---|---|---|---|---|

---

# 93. Hard Rule vs Soft Rule

Hard rule:

```text
impossible by definition
```

Soft rule:

```text
unusual and requires review
```

Do not treat soft rules as automatic exclusion criteria.

---

# 94. Quality Summary Matrix

| Domain | Pass | Issues | Critical | Action |
|---|---:|---:|---:|---|
| Structure | | | | |
| Identifiers | | | | |
| Types | | | | |
| Categories | | | | |
| Ranges | | | | |
| Units | | | | |
| Logic | | | | |
| Time | | | | |
| Duplicates | | | | |
| Merge/Linkage | | | | |
| Missingness | | | | |
| Derived variables | | | | |
| Outliers | | | | |
| Analysis readiness | | | | |

---

# 95. Critical Quality Failures

Examples:

- dataset identity unresolved;
- participant linkage corrupted;
- analysis unit cannot be reconstructed;
- outcome coding inconsistent with source;
- unit mismatch materially alters values;
- duplicate merge inflated sample size;
- primary endpoint derivation incorrect;
- widespread unknown sentinel values;
- major date logic impossible;
- derived variable formula wrong;
- source data unavailable for suspicious corrections.

---

# 96. Major Quality Issues

Examples:

- important variable partly miscoded;
- high unresolved missingness;
- site-specific unit inconsistency;
- duplicate participants unresolved;
- substantial merge failures;
- instrument version mismatch;
- incomplete longitudinal linkage.

---

# 97. Moderate Quality Issues

Examples:

- rare category typo;
- isolated date inconsistency;
- one unresolved outlier;
- noncritical derived-variable discrepancy.

---

# 98. Minor Issues

Examples:

- labels inconsistent;
- harmless whitespace;
- capitalization differences;
- noncritical formatting.

Do not inflate minor formatting into scientific risk.

---

# 99. Quality Audit Workflow

Use:

```text
1. Confirm dataset identity
2. Load governance rules
3. Check structure
4. Check identifiers
5. Check types and categories
6. Check ranges and units
7. Check logic
8. Check time
9. Check duplicates
10. Check merges/linkage
11. Check missingness
12. Check derived variables
13. Check outliers
14. Review issues
15. Confirm corrections
16. Re-run audit
17. Determine analysis readiness
```

---

# 100. Pre-Correction Snapshot

Before material corrections:

- preserve dataset version;
- save issue register;
- record audit date;
- preserve counts.

This allows correction impact to be traced.

---

# 101. Post-Correction Re-Audit

Every material correction should trigger relevant rechecks.

Do not assume correction solved the issue.

---

# 102. Row-Level Change Audit

After correction compare:

- changed records;
- changed variables;
- row count;
- ID count;
- missingness count;
- derived variable count.

---

# 103. Sample Size Reconciliation

Reconcile:

```text
source population
      ↓
eligible records
      ↓
included dataset
      ↓
analysis dataset
      ↓
analysis-specific sample
```

Unexpected differences require explanation.

---

# 104. Participant Flow Integrity

Quality audit should support participant-flow reporting.

Do not construct flow counts after the fact from memory.

---

# 105. Dataset Release Decision

Before releasing to analysis, verify:

- critical issues resolved;
- major issues resolved or bounded;
- unresolved issues documented;
- quality status recorded;
- corrected version created;
- governance record updated.

---

# 106. Quality Lock

A quality-approved dataset may be designated:

`QUALITY_REVIEW_COMPLETE`

This does not replace analytical review.

---

# 107. Handoff to Analysis Planner

Provide:

```yaml
analysis_quality_handoff:
  dataset_id:
  dataset_version:
  quality_status:
  analysis_readiness:
  row_count:
  unique_units:
  missingness_summary:
  duplicate_status:
  linkage_status:
  derived_variable_status:
  outlier_status:
  unresolved_issues:
  sensitivity_datasets:
  known_limitations:
```

---

# 108. Handoff to Statistical Method Selector

Provide data facts, not method recommendations:

- outcome distribution;
- variable scale;
- cluster structure;
- repeated measures;
- missingness;
- censoring;
- sparse cells;
- weights;
- validated sample size.

Do not select a statistical method merely because the data appear normal or non-normal.

---

# 109. Handoff to Qualitative Analysis

For qualitative data pass:

- corpus completeness;
- transcript quality;
- translation status;
- anonymization;
- duplicate status;
- missing-record status;
- codebook version.

---

# 110. Handoff to Mixed-Method Analysis

Pass strand-specific quality statuses separately.

Do not collapse one strand’s quality into the other.

---

# 111. Handoff to Meta-Analysis

For evidence synthesis datasets pass:

- extraction accuracy;
- duplicate-study status;
- effect-data verification;
- dependency status;
- missing effect components;
- conversion provenance.

---

# 112. Handoff to Result Interpreter

Provide quality limitations that materially affect interpretation.

Examples:

- high missingness;
- uncertain linkage;
- unresolved outlier;
- site unit mismatch corrected;
- sensitivity dataset required.

---

# 113. Handoff to Scientific Discussion

Data-quality limitations should be carried forward when they affect:

- bias;
- precision;
- measurement;
- external validity;
- robustness;
- reproducibility.

---

# 114. Handoff to Manuscript Workflow

Preserve facts needed for Methods and Results:

- cleaning decisions;
- exclusions;
- missing-data handling;
- quality checks;
- derived variables;
- participant flow;
- sensitivity analyses.

Do not invent generic statements such as:

> “Data were checked for completeness and accuracy.”

unless that is supported by the audit record.

---

# 115. Reviewer Response Relationship

When reviewers ask:

- Why were outliers removed?
- How were duplicates handled?
- How was missingness treated?
- Were implausible values verified?
- Was the dataset rechecked after correction?

Respond from the issue register and audit trail.

---

# 116. Relationship with Research Data Governance

`research-data-governance` establishes:

- source;
- version;
- meaning;
- transformation history;
- access;
- privacy.

`data-quality-auditor` evaluates the actual values and structural coherence.

If provenance is insufficient, return to:

`research-data-governance`

---

# 117. Relationship with Methodology Architect

If the dataset cannot support the intended design or endpoint, route to:

`methodology-architect`

Do not silently redefine the research question to fit available data.

---

# 118. Relationship with Protocol Builder

If recurring inconsistencies arise from data-collection procedures, route to:

`protocol-builder`

for operational correction.

---

# 119. Relationship with Sampling Strategy

If duplicates, exclusions, or incomplete recruitment alter the effective sample, notify:

`sampling-strategy`

and:

`analysis-planner`

where relevant.

---

# 120. Relationship with Instrument Design

If item coding, scoring, instrument version, or measurement errors are found, route to:

`instrument-design`

---

# 121. Relationship with Reproducibility Auditor

After analysis, `reproducibility-auditor` should verify that quality decisions can be reproduced from:

- issue register;
- correction log;
- scripts;
- governed dataset versions.

---

# 122. Relationship with Ethics and Regulatory Gate

If quality review reveals:

- unauthorized records;
- privacy exposure;
- consent mismatch;
- prohibited linkage;

route to:

`ethics-regulatory-gate`

when available.

---

# 123. Relationship with Registration / Preregistration

If cleaning, exclusion, endpoint, or derived-variable decisions differ from prespecified plans, preserve this difference for:

`registration-preregistration-builder`

when available.

Do not conceal post-registration changes.

---

# 124. User-Friendly Behavior

Instead of:

> “There are 17 outliers.”

Prefer:

> “Seventeen observations are statistically unusual. At this stage they should be reviewed against the source and measurement context; they are not automatically errors.”

Instead of:

> “Remove duplicates.”

Prefer:

> “There are repeated IDs. We first need to determine whether these are duplicate imports or legitimate repeated measurements.”

---

# 125. Avoid Over-Automation

Automated checks are useful for:

- screening;
- counting;
- flagging;
- reproducibility.

They do not replace scientific review.

---

# 126. No Blind Cleaning

Do not automatically apply:

- listwise deletion;
- winsorization;
- standardization;
- log transformation;
- mean imputation;
- outlier removal;
- category collapsing.

These are analytical decisions, not generic quality fixes.

---

# 127. No Significance-Driven Decisions

Never decide data validity by:

- p-value;
- effect size direction;
- hypothesis support;
- journal preference.

---

# 128. No Software-Driven Decisions

Do not delete records merely because:

- Jamovi warns;
- SPSS flags;
- R model fails;
- SmartPLS shows low loading;
- a package reports an outlier;
- Excel changes the format.

Software signals require scientific interpretation.

---

# 129. No Normality Ritual

Do not use normality tests as a universal gate for data quality.

---

# 130. No Arbitrary Missingness Rule

Do not delete:

- participants;
- variables;
- timepoints

using arbitrary percentage cutoffs without study-specific rationale.

---

# 131. No Arbitrary Outlier Rule

Do not apply:

```text
|z| > 3 → delete
```

as a universal rule.

---

# 132. No Arbitrary Duplicate Rule

Do not apply:

```text
duplicated ID → delete
```

without determining observational unit.

---

# 133. No Arbitrary Range Rule

Do not assume any value outside a common clinical range is impossible.

---

# 134. No Journal-Driven Quality Decisions

Journal preferences must not redefine valid data.

---

# 135. Stop Conditions

Stop and request clarification or upstream correction when:

- dataset identity is unresolved;
- source data are unavailable for critical suspicious values;
- major variables lack meaning;
- units are ambiguous;
- linkage cannot be reconstructed;
- duplicate structure is unresolved;
- primary outcome derivation is uncertain;
- missing codes are unknown;
- a major merge may have inflated or lost records;
- participant IDs are corrupted;
- data access may be unauthorized;
- critical corrections cannot be verified.

Use statuses such as:

- `RETURN_TO_RESEARCH_DATA_GOVERNANCE`
- `RETURN_TO_PROTOCOL_BUILDER`
- `RETURN_TO_INSTRUMENT_DESIGN`
- `RETURN_TO_SAMPLING_STRATEGY`
- `DATA_QUALITY_REQUIRES_CORRECTION`
- `DATA_QUALITY_BLOCKED`
- `ANALYSIS_NOT_READY`

---

# 136. Data Quality Audit Record

Recommended schema:

```yaml
data_quality_audit:
  dataset_id:
  dataset_version:
  audit_date:
  governance_status:
  structural_integrity:
  identifier_integrity:
  type_integrity:
  categorical_integrity:
  range_integrity:
  unit_integrity:
  logic_integrity:
  temporal_integrity:
  duplicate_status:
  merge_status:
  linkage_status:
  missingness_status:
  derived_variable_status:
  outlier_status:
  critical_issues:
  major_issues:
  corrections:
  unresolved_issues:
  analysis_readiness:
  next_action:
```

---

# 137. Data Issue Table

| Issue ID | Variable/Record | Type | Severity | Evidence | Decision | Status |
|---|---|---|---|---|---|---|

---

# 138. Outlier Review Table

| Record | Variable | Value | Flag Reason | Source Verified | Plausible | Decision |
|---|---|---:|---|---|---|---|

---

# 139. Missingness Summary Table

| Variable | Missing n | Missing % | Structural | Unknown | Merge-created | Notes |
|---|---:|---:|---:|---:|---:|---|

---

# 140. Duplicate Review Table

| Key | Count | Expected? | Type | Decision | Notes |
|---|---:|---|---|---|---|

---

# 141. Merge Audit Table

| Merge | Expected Cardinality | Observed | Unmatched L | Unmatched R | Row Inflation | Status |
|---|---|---|---:|---:|---:|---|

---

# 142. Derived Variable Audit Table

| Variable | Formula Verified | Unit Verified | Missing Rule Verified | Discrepancies | Status |
|---|---|---|---|---:|---|

---

# 143. Quality Audit Passport

```yaml
data_quality_passport:
  status:
  dataset_id:
  dataset_version:
  structural_status:
  semantic_status:
  duplicate_status:
  linkage_status:
  missingness_status:
  derived_variable_status:
  outlier_status:
  critical_issue_count:
  major_issue_count:
  unresolved_issue_count:
  corrected_dataset_version:
  analysis_readiness:
  sensitivity_data_required:
  next_action:
```

---

# 144. Compact User-Facing Output

Example:

```text
Data quality status: REQUIRES CORRECTION

What passed
- Dataset version and row structure are consistent.
- Participant IDs are valid.
- Most category codes match the codebook.

Issues requiring correction
1. Two laboratory variables contain mixed mg/L and µg/L units.
2. The clinical-laboratory merge created 14 unexpected duplicated participant-timepoint rows.
3. The derived BMI variable does not match recalculation in 6 records.

Needs review, not automatic deletion
- Eight statistically unusual creatinine values are source-consistent and may be clinically valid.

Next action
Correct the unit mapping and merge cardinality, recalculate BMI, then rerun the audit before analysis planning.
```

---

# 145. Audit Reproducibility

Where feasible, quality checks should be reproducible using:

- scripts;
- documented transformations;
- saved rules;
- issue registers;
- versioned outputs.

Do not rely only on memory or manual visual inspection.

---

# 146. Correction Provenance

The corrected dataset must receive a new version when material values change.

Do not overwrite the previous audited version.

---

# 147. Sensitivity Dataset Rule

If an unresolved but defensible decision could materially affect inference, preserve:

- primary dataset;
- alternate sensitivity dataset;
- decision rationale.

---

# 148. Quality Audit Completion Gate

The audit is complete only when:

- all critical issues are resolved or study-blocking;
- major issues are resolved or explicitly bounded;
- corrections are documented;
- corrected data are re-audited;
- analysis readiness is assigned;
- unresolved issues are transferred downstream.

---

# 149. Relationship with Research Router

`research-router` should route here when the user says:

- “check my data before analysis”;
- “clean this dataset”;
- “why are there duplicates?”;
- “are these outliers errors?”;
- “can I analyze this file?”;
- “my merge changed the row count”;
- “some variables have impossible values”;
- “I need to verify the dataset used in the manuscript.”

Do not interpret “clean” as permission for silent deletion.

---

# 150. Relationship with Research Intake

At intake, capture whether the user has:

- raw data;
- processed data;
- codebook;
- expected ranges;
- known issues;
- merge history;
- analysis goals.

Do not require a full audit during intake.

---

# 151. Relationship with Research Resume

If prior research is resumed, determine whether the historical analysis dataset has already been quality audited.

If not, reconstruct before strong reuse.

---

# 152. Relationship with Prior Research Auditor

A previous publication may reveal unresolved quality decisions.

Pass such issues to this skill when source data are available.

---

# 153. Relationship with Research Roadmap

Long-term research programs may require recurring data-quality gates for:

- cohort updates;
- registry refreshes;
- new sites;
- new assays;
- validation datasets.

---

# 154. Relationship with Result Interpreter

When results depend materially on data-quality decisions, `result-interpreter` must receive that context.

---

# 155. Relationship with Scientific Discussion

Do not bury unresolved quality issues.

Carry them into limitations where they affect scientific interpretation.

---

# 156. Relationship with Implication Builder

Do not generate strong implications from data whose critical quality problems remain unresolved.

---

# 157. Relationship with Manuscript Auditor

`manuscript-auditor` should verify that claims about:

- exclusions;
- missingness;
- cleaning;
- outliers;
- sample size

match the audit record.

---

# 158. Relationship with Reviewer Simulator

Reviewer simulation may test whether data-quality decisions are transparent and defensible.

---

# 159. Relationship with Reviewer Response

Reviewer-driven alternative cleaning must create a new analysis version rather than silently replacing the primary dataset.

---

# 160. Final Quality Rule

Never delete because a value is inconvenient.

Never correct because a model prefers it.

Never call a dataset clean merely because software stops warning.

Data quality is established by scientific coherence, provenance, and defensible review.

---

# Success Criterion

`data-quality-auditor` succeeds when a governed dataset has been systematically evaluated for structural integrity, identifier integrity, data types, categorical coding, numeric ranges, units, temporal logic, cross-variable consistency, duplicates, merge and linkage integrity, missingness, derived-variable correctness, scoring, laboratory or instrument plausibility, outlier provenance, and analysis fitness; when confirmed errors are distinguished from legitimate unusual observations and unresolved anomalies; when every correction, retention, exclusion, recoding, recalculation, relinking, or quarantine decision is evidence-based, traceable, versioned, and independent of desired statistical results; when arbitrary normality rules, significance-driven cleaning, automatic outlier removal, arbitrary missingness thresholds, and software-driven decisions are prevented; when corrected data are re-audited; when unresolved limitations are explicitly carried forward; and when the resulting dataset can be handed transparently to `analysis-planner`, appropriate analytical skills, `result-interpreter`, and ultimately `reproducibility-auditor` with a clear, reproducible record of what was checked, what changed, what remained uncertain, and why the dataset is or is not ready for analysis.
