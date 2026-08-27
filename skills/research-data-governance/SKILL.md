---
name: research-data-governance
description: Design, document, and audit the governance architecture that connects source data, raw data, transformations, cleaned data, analysis-ready datasets, metadata, codebooks, derived variables, identifiers, access permissions, privacy safeguards, retention, archiving, sharing, and reproducibility requirements. Use after methodology, protocol, sampling, and measurement requirements are sufficiently clear and before data-quality auditing or analysis planning. This skill protects data provenance, version integrity, variable meaning, lawful and ethical access, reconstructability, and transparent handoff across the research lifecycle without silently changing scientific meaning or treating data cleaning as a cosmetic preprocessing step.
---

# Research Data Governance

## Purpose

`research-data-governance` defines how research data are created, received, named, documented, transformed, protected, versioned, linked, stored, shared, archived, and handed downstream so that the analytical dataset can be reconstructed from defensible source records.

Its central question is:

> What data exist or will exist, where did they come from, what do the variables mean, what transformations occurred, who may access them, how are versions controlled, and can another competent researcher reconstruct the analysis-ready dataset from the governed research record?

The skill is not merely a file-management checklist.

It is a scientific integrity layer.

```text
RESEARCH DESIGN
      ↓
SOURCE DATA
      ↓
RAW DATA
      ↓
DOCUMENTED TRANSFORMATIONS
      ↓
CURATED DATA
      ↓
ANALYSIS-READY DATASET
      ↓
ANALYTICAL OUTPUT
      ↓
REPORTED RESULT
```

---

# 1. Core Principle

> **Every analytically meaningful value must have a traceable origin, interpretation, transformation history, and governance status.**

Do not treat file naming, cleaning, coding, recoding, derivation, merging, linkage, de-identification, imputation, exclusion, unit conversion, aggregation, or versioning as scientifically neutral administrative actions.

Any of these may alter the evidence base.

---

# 2. Activation Gate

Use `research-data-governance` when one or more of the following apply:

- primary data will be collected;
- secondary data will be received;
- registry or administrative data will be used;
- laboratory or instrument data will be generated;
- multiple files, sites, or waves must be merged;
- derived variables are required;
- identifiers must be removed or transformed;
- data access is restricted;
- reproducible analysis is expected;
- longitudinal records require linkage;
- inherited data from previous research must be reconstructed;
- or downstream analysis requires defensible data lineage.

Do not force this skill when no research data are involved or when the data-management burden is trivial and already fully governed elsewhere.

If not applicable, state why.

---

# 3. Required Upstream Context

Use, when available:

- finalized research question;
- approved problem-solving approach;
- methodology architecture;
- protocol;
- sampling strategy;
- instrument or measurement plan;
- variable definitions;
- source population;
- unit of analysis;
- unit of observation;
- data-collection schedule;
- laboratory workflow;
- intervention or exposure logic;
- ethics or regulatory constraints;
- consent requirements;
- data-use agreements;
- and planned downstream analyses.

Do not invent missing governance requirements.

---

# 4. Governance Scope

Cover, where relevant:

- source identity;
- data ownership and stewardship;
- acquisition method;
- reference period;
- extraction date;
- version;
- schema;
- metadata;
- data dictionary;
- codebook;
- units;
- coding;
- identifiers;
- privacy status;
- linkage keys;
- missingness codes;
- derived variables;
- transformations;
- exclusions;
- quality flags;
- access levels;
- storage;
- backup;
- retention;
- archiving;
- sharing;
- disposal;
- audit trail;
- and reproducibility handoff.

---

# 5. Data Lifecycle Model

Use the following lifecycle unless the study requires a defensible alternative:

```text
SOURCE SYSTEM
      ↓
DATA ACQUISITION
      ↓
RAW / ORIGINAL DATA
      ↓
INGESTION RECORD
      ↓
STRUCTURAL HARMONIZATION
      ↓
CURATION
      ↓
DOCUMENTED TRANSFORMATIONS
      ↓
QUALITY REVIEW
      ↓
ANALYSIS-READY DATASET
      ↓
ANALYSIS
      ↓
OUTPUTS
      ↓
ARCHIVE / REPRODUCIBILITY PACKAGE
```

Do not collapse stages when doing so would erase provenance.

---

# 6. Data State Taxonomy

Use explicit states such as:

- `SOURCE_DATA`
- `RAW_DATA`
- `IMPORTED_DATA`
- `HARMONIZED_DATA`
- `CURATED_DATA`
- `CLEAN_DATA`
- `ANALYSIS_READY_DATA`
- `DERIVED_DATA`
- `LINKED_DATA`
- `DEIDENTIFIED_DATA`
- `ANONYMIZED_DATA`
- `RESTRICTED_DATA`
- `ARCHIVED_DATA`
- `SUPERSEDED_DATA`
- `QUARANTINED_DATA`

Avoid ambiguous labels such as:

- final;
- final2;
- latest;
- newest;
- fixed;
- clean-final;
- final-revised;
- use-this-one.

Version identity must be explicit.

---

# 7. Source Data

`SOURCE_DATA` is the most authoritative record from which research data are obtained.

Examples may include:

- case-report forms;
- electronic medical records;
- laboratory instruments;
- survey platforms;
- interview recordings;
- observation sheets;
- registries;
- administrative databases;
- official datasets;
- sequencing instruments;
- image systems;
- sensors;
- or repositories.

Do not assume the first spreadsheet received is the source record.

Record:

```yaml
source_data:
  source_system:
  source_owner:
  source_record_type:
  source_period:
  source_version:
  extraction_method:
  extraction_date:
  original_format:
  immutability_status:
  notes:
```

---

# 8. Raw Data Rule

> **Never overwrite the only copy of raw data.**

When possible, raw data should remain unchanged.

If a dynamic source is used, preserve enough information to recreate the extraction:

- extraction timestamp;
- query;
- filters;
- API parameters;
- source version;
- dashboard filters;
- or snapshot date.

---

# 9. Raw, Working, and Analysis Layers

A defensible project commonly distinguishes:

```text
/raw
/working
/analysis
```

`raw` contains original or authoritative exports.

`working` contains intermediate harmonization and transformation states.

`analysis` contains approved analysis-ready datasets.

Do not place manually edited analytical files into the raw layer.

---

# 10. Analysis-Ready Data

`ANALYSIS_READY_DATA` does not merely mean “software can open the file.”

The dataset should:

- correspond to the intended analysis target;
- have documented inclusions and exclusions;
- have documented derived variables;
- have documented missing-value handling;
- have documented units;
- preserve relevant time and cluster structure;
- include required quality flags;
- have a known version;
- and be reconstructable from upstream governed data.

---

# 11. Dataset Provenance Record

For each major dataset record:

```yaml
dataset_provenance:
  dataset_id:
  dataset_name:
  data_state:
  source_system:
  source_period:
  extraction_date:
  original_filename:
  current_filename:
  file_format:
  schema_version:
  dataset_version:
  parent_dataset:
  transformation_record:
  responsible_role:
  access_classification:
  privacy_status:
  quality_status:
  analysis_readiness:
  notes:
```

---

# 12. Variable Provenance Record

For analytically important variables record:

```yaml
variable_provenance:
  variable_name:
  label:
  scientific_role:
  source_variable:
  source_dataset:
  source_field:
  data_type:
  measurement_scale:
  unit:
  coding:
  missing_codes:
  transformation:
  derivation:
  reference_period:
  timepoint:
  population_scope:
  provenance_status:
  notes:
```

---

# 13. Scientific Variable Roles

Where relevant classify variables as:

- identifier;
- participant characteristic;
- exposure;
- intervention;
- comparator;
- outcome;
- endpoint;
- predictor;
- covariate;
- confounder;
- mediator;
- moderator;
- stratification variable;
- clustering variable;
- repeated-measure indicator;
- time variable;
- censoring indicator;
- event indicator;
- quality flag;
- batch indicator;
- site indicator;
- derived score;
- laboratory measurement;
- instrument item;
- or metadata variable.

Do not infer causal roles from column names alone.

---

# 14. Data Dictionary

Every nontrivial analysis-ready dataset should have a data dictionary.

Minimum fields:

```text
variable_name
label
description
data_type
allowed_values
unit
missing_value_code
source
derivation
scientific_role
timepoint
notes
```

For categorical variables include code-to-label mapping.

For numeric variables include units.

For dates include format and timezone where relevant.

---

# 15. Codebook

Use a codebook when category mappings, response coding, qualitative codes, instrument scoring, or transformation rules require additional documentation.

Do not use “data dictionary” and “codebook” interchangeably if doing so creates ambiguity.

---

# 16. Naming Conventions

Prefer stable machine-readable variable names such as:

```text
lower_snake_case
```

Avoid names such as:

```text
Age (Years)
Respondent No.
FINAL SCORE!!!
Variable 1 new
Column X
```

Human-readable labels may be stored separately.

---

# 17. File Naming and Versioning

A file name may include:

```text
project
dataset_role
version
date
status
```

Example:

```text
project_master_v001_2026-08-27_raw.csv
project_master_v004_2026-09-02_curated.csv
project_analysis_v007_2026-09-04_locked.csv
```

Distinguish:

- file version;
- schema version;
- protocol version;
- codebook version;
- analysis dataset version;
- analysis script version;
- manuscript result version.

Do not assume they evolve synchronously.

---

# 18. Dataset Lock

Possible statuses:

- `UNLOCKED`
- `PROVISIONALLY_LOCKED`
- `LOCKED_FOR_ANALYSIS`
- `UNLOCKED_FOR_CORRECTION`
- `SUPERSEDED`

A locked dataset can still contain limitations.

Locking means changes require explicit version control.

---

# 19. Transformation Log

Every scientifically meaningful transformation should be logged.

```yaml
transformation:
  transformation_id:
  timestamp:
  input_dataset:
  input_version:
  output_dataset:
  output_version:
  variable_or_scope:
  operation:
  rule:
  rationale:
  software_or_tool:
  script_or_command:
  responsible_role:
  verification:
  reversibility:
  notes:
```

---

# 20. Transformation Categories

Examples:

- parsing;
- renaming;
- type conversion;
- unit conversion;
- recoding;
- reverse scoring;
- standardization;
- aggregation;
- derivation;
- date arithmetic;
- time-window construction;
- linkage;
- deduplication;
- reshaping;
- filtering;
- exclusion;
- weighting;
- pseudonymization;
- de-identification;
- text processing;
- sequence processing;
- image processing.

---

# 21. Derived Variables

For every major derived variable record:

- source variables;
- formula;
- units;
- order of operations;
- missing-value behavior;
- reference period;
- thresholds;
- validation method;
- rationale.

Example:

```yaml
derived_variable:
  name: bmi
  sources:
    - weight_kg
    - height_m
  formula: weight_kg / (height_m ^ 2)
  unit: kg/m2
  missing_rule: missing if either source is missing
  validation:
  rationale:
```

Do not create scoring rules from memory when validated rules exist.

---

# 22. Composite Scores

For scales and composite indices document:

- instrument version;
- included items;
- item direction;
- reverse-scored items;
- weighting;
- missing-item rule;
- score range;
- subscale logic;
- interpretation;
- validation basis.

Do not silently modify scoring to improve reliability or significance.

---

# 23. Unit Governance

For measurements where units matter:

- record source unit;
- record analysis unit;
- document conversion;
- verify dimensional consistency.

Never mix:

```text
mg
g
µg
ng
```

or:

```text
mL
L
```

without explicit conversion.

---

# 24. Date and Time Governance

Document:

- date format;
- time format;
- timezone;
- reference date;
- visit date;
- specimen date;
- result date;
- enrollment date;
- follow-up date;
- event date.

Prefer unambiguous forms such as:

```text
YYYY-MM-DD
```

---

# 25. Missing Data Encoding

Distinguish:

- true missing;
- not applicable;
- not asked;
- refused;
- measurement failed;
- below detection limit;
- lost record;
- not yet available;
- structurally missing;
- censored;
- unknown.

Never assume blank, `0`, `99`, or `999` means missing without documentation.

---

# 26. Missingness Provenance

```yaml
missingness:
  variable:
  code:
  meaning:
  source_reason:
  introduced_at_stage:
  recoverable:
  analysis_handling:
  notes:
```

Distinguish source missingness from missingness introduced by merging, filtering, or transformation.

---

# 27. Duplicate Governance

Do not automatically delete duplicates.

Classify:

- exact duplicate;
- duplicate participant;
- legitimate repeated measurement;
- duplicated import;
- longitudinal revisit;
- linked multi-source record;
- unresolved potential duplicate.

Actual duplicate assessment belongs to `data-quality-auditor`.

---

# 28. Identifier Governance

Classify identifiers as:

- direct identifier;
- indirect identifier;
- study identifier;
- linkage identifier;
- pseudonym;
- anonymized identifier;
- system identifier.

Do not expose direct identifiers in analytical datasets without justification and permission.

---

# 29. Pseudonymization and Anonymization

Pseudonymization preserves controlled re-linkage.

Anonymization should be claimed only when re-identification risk is sufficiently addressed.

Removing names alone is not enough.

Consider:

- rare combinations;
- dates;
- geography;
- free text;
- genetic data;
- imaging;
- longitudinal trajectories;
- small subgroup size.

Prefer accurate labels such as:

- `PSEUDONYMIZED`
- `DEIDENTIFIED`
- `ANONYMIZED`
- `RESTRICTED_DATA`

---

# 30. Privacy and Access Classification

Recommended access statuses:

- `PUBLIC`
- `INTERNAL`
- `CONFIDENTIAL`
- `RESTRICTED`
- `HIGHLY_RESTRICTED`

Record:

```yaml
access_control:
  dataset:
  classification:
  authorized_roles:
  approval_required:
  access_location:
  remote_access_allowed:
  export_allowed:
  sharing_allowed:
  expiration:
  notes:
```

Do not invent legal classifications.

---

# 31. Ownership and Stewardship

Distinguish:

- data owner;
- data steward;
- data custodian;
- principal investigator;
- analyst;
- data manager;
- statistician;
- laboratory manager;
- repository manager;
- external collaborator.

Do not assign ownership merely to whoever possesses the file.

---

# 32. Data Use Agreements

For external data record:

- permitted purpose;
- prohibited purpose;
- permitted users;
- sharing restrictions;
- publication restrictions;
- retention terms;
- deletion requirements;
- linkage restrictions;
- re-identification restrictions.

Possession does not imply unrestricted reuse.

---

# 33. Consent and Regulatory Constraints

Where applicable determine whether consent permits:

- primary analysis;
- secondary analysis;
- future research;
- genetic analysis;
- data linkage;
- external sharing;
- international transfer;
- repository deposit.

Route unresolved questions to:

`ethics-regulatory-gate`

when available.

Until then use:

`CONSENT_SCOPE_UNRESOLVED`

or another explicit unresolved status.

---

# 34. Data Acquisition Record

```yaml
acquisition:
  source:
  source_url_or_location:
  source_version:
  source_date:
  extraction_query:
  filters:
  download_date:
  format:
  checksum:
  license:
  access_conditions:
  notes:
```

Dynamic APIs and dashboards require stronger provenance than static files.

---

# 35. Laboratory Data

Where relevant preserve:

- sample identifier;
- specimen source;
- collection date;
- processing date;
- batch;
- plate;
- instrument;
- calibration;
- reagent lot;
- operator;
- run identifier;
- QC result;
- raw signal;
- processed result;
- normalization;
- exclusion reason;
- rerun status.

Do not retain only final summary values when raw signal provenance is scientifically important.

---

# 36. Molecular and Genomic Data

Where applicable preserve:

- sample identifier;
- assay type;
- platform;
- reference genome;
- reference build;
- sequence file;
- alignment file;
- variant file;
- pipeline version;
- parameters;
- annotation database;
- annotation version;
- QC status;
- batch.

Do not allow reference-build ambiguity.

---

# 37. Imaging Data

Where applicable document:

- modality;
- acquisition protocol;
- device;
- calibration;
- preprocessing;
- compression;
- segmentation;
- annotation;
- reader;
- masking;
- derived feature extraction;
- transformation history.

---

# 38. Pharmacokinetic and PBPK Data

Distinguish:

- observed concentration data;
- digitized literature data;
- simulated data;
- population parameters;
- individual parameters;
- physiology inputs;
- compound inputs;
- model outputs;
- derived PK metrics.

Record source, units, time basis, dose basis, and model version.

Simulated data must never be presented as observed data.

---

# 39. Survey Data

Govern:

- instrument version;
- item identifiers;
- response options;
- skip logic;
- randomization;
- language version;
- administration mode;
- timestamp;
- completion status;
- duplicate response logic;
- scoring;
- reverse scoring;
- scale construction.

---

# 40. Qualitative Data

Govern:

- recording identity;
- transcript identity;
- transcription method;
- translation status;
- speaker labeling;
- redaction;
- anonymization;
- transcript version;
- coder access;
- codebook version;
- memo linkage;
- quotation permissions.

Do not erase context merely to fit tabular conventions.

---

# 41. Mixed-Method Data

Preserve the distinction between:

- quantitative dataset;
- qualitative corpus;
- integration key;
- linking variables;
- joint-display source;
- sequence;
- timing;
- strand-specific provenance.

---

# 42. Longitudinal Data

Record:

- participant identifier;
- wave;
- visit;
- event;
- time origin;
- elapsed time;
- calendar time;
- censoring;
- loss to follow-up;
- repeated measure.

Do not assume row order equals time order.

---

# 43. Multisite Data

Preserve:

- site identifier;
- site protocol version;
- local coding;
- local units;
- harmonization rule;
- local ethics constraints;
- transfer date;
- site-specific QC;
- site-specific deviations.

---

# 44. Harmonization

Classify mapping as:

- exact equivalence;
- semantic equivalence;
- unit-convertible;
- recodable;
- approximately comparable;
- partially comparable;
- not comparable;
- unresolved.

Do not force harmonization merely to increase sample size.

---

# 45. Merge and Linkage Governance

For each merge record:

```yaml
merge:
  merge_id:
  left_dataset:
  right_dataset:
  key:
  join_type:
  expected_cardinality:
  observed_cardinality:
  unmatched_left:
  unmatched_right:
  duplicate_keys:
  conflict_resolution:
  output_dataset:
  verification:
```

Many-to-many joins require explicit justification.

For record linkage also document:

- linkage fields;
- matching rule;
- thresholds;
- review;
- false-match risk;
- missed-match risk;
- uncertainty.

---

# 46. Exclusion Governance

Every exclusion affecting the analysis dataset should record:

- rule;
- rationale;
- protocol alignment;
- stage introduced;
- affected records;
- reversibility;
- downstream impact.

Do not delete records merely because they weaken significance.

---

# 47. Data Corrections

Preserve correction provenance:

```yaml
correction:
  record_id:
  variable:
  original_value:
  corrected_value:
  correction_type:
  evidence:
  reason:
  date:
  responsible_role:
  verification:
```

---

# 48. Audit Trail

The project should be able to answer:

- what changed;
- when;
- why;
- by whom or by which role;
- from which version;
- to which version;
- using what rule;
- with what verification.

Do not allow silent overwriting, recoding, deletion, imputation, winsorization, unit conversion, linkage, or duplicate removal.

---

# 49. Storage Architecture

A generic structure may be:

```text
project/
├── raw/
├── external/
├── working/
├── clean/
├── analysis/
├── metadata/
├── codebook/
├── scripts/
├── outputs/
├── documentation/
└── archive/
```

Adapt to institutional requirements.

Do not force this exact structure when another controlled architecture already exists.

---

# 50. Backup and Security

Where relevant define:

- primary storage;
- backup storage;
- backup frequency;
- encryption;
- access control;
- restoration method;
- responsible role.

A synchronized folder is not automatically a backup.

Before cloud storage assess institutional approval, privacy classification, data residency, access, encryption, sharing permissions, and deletion behavior.

---

# 51. Retention and Archiving

Record:

```yaml
retention:
  dataset:
  retention_period:
  retention_basis:
  archive_location:
  deletion_date:
  responsible_role:
  exceptions:
  notes:
```

Do not invent a universal retention period.

Archive packages may include:

- dataset manifest;
- analysis-ready dataset;
- codebook;
- transformation log;
- scripts;
- protocol;
- analysis plan;
- software versions;
- outputs;
- README;
- access rules.

---

# 52. Data Sharing

Before sharing determine:

- scientific purpose;
- consent compatibility;
- ethics compatibility;
- contractual restrictions;
- de-identification status;
- repository requirements;
- license;
- access model.

Possible modes:

- open;
- controlled access;
- mediated access;
- restricted collaboration;
- metadata-only;
- not shareable.

FAIR does not mean everything must be public.

---

# 53. Reproducibility Package

Prepare downstream handoff for `reproducibility-auditor`.

A package may contain:

```text
README
protocol
analysis_plan
data_dictionary
codebook
dataset_manifest
transformation_log
analysis_ready_dataset
scripts
software_versions
environment_information
outputs
result_mapping
```

Sensitive data may use controlled-access instructions, synthetic data, metadata, or reproducible access procedures.

---

# 54. Spreadsheet Governance

Spreadsheets are allowed but require safeguards.

Avoid:

- merged cells in data tables;
- color-only coding;
- multiple variables in one cell;
- formulas copied inconsistently;
- hidden calculations without documentation;
- mixed units;
- manual deletion without logs;
- sorting that detaches rows.

Do not assume Excel is invalid or scripts are automatically correct.

Evaluate actual provenance.

---

# 55. Precision and Detection Limits

Distinguish:

- measurement precision;
- storage precision;
- display precision;
- reporting precision.

Do not round source data prematurely.

For laboratory measures distinguish:

- below detection limit;
- below quantification limit;
- zero;
- missing;
- not measured.

---

# 56. Outliers and Imputation

Governance preserves the original value and decision trail.

It does not automatically remove outliers.

For imputation document:

- reason;
- method;
- variables;
- model;
- number of imputations;
- random seed where relevant;
- software;
- dataset version.

Do not overwrite raw missing values with imputed values without preserving provenance.

---

# 57. Predictive Research

For dataset splitting document:

- training set;
- validation set;
- test set;
- split rule;
- temporal split;
- site split;
- stratification;
- leakage safeguards.

Preprocessing fitted on training data must not silently use test-set information.

---

# 58. Dataset Freeze and Release

A controlled freeze may record:

```yaml
data_freeze:
  freeze_id:
  dataset_version:
  date:
  scope:
  reason:
  quality_status:
  authorized_by:
```

When releasing data for analysis record:

- release identifier;
- dataset version;
- analyst role;
- date;
- permitted purpose;
- restrictions;
- quality status;
- analysis plan version.

---

# 59. Analysis Dataset Manifest

```yaml
analysis_dataset_manifest:
  dataset_id:
  version:
  research_question:
  analysis_target:
  source_datasets:
  inclusion_rules:
  exclusion_rules:
  derived_variables:
  linkage:
  missingness:
  weights:
  transformations:
  quality_status:
  lock_status:
  release_date:
  notes:
```

---

# 60. Result-to-Data Traceability

Every major result should ultimately be traceable through:

```text
REPORTED RESULT
      ↓
ANALYTICAL OUTPUT
      ↓
ANALYSIS SCRIPT / PROCEDURE
      ↓
ANALYSIS DATASET VERSION
      ↓
TRANSFORMATION HISTORY
      ↓
SOURCE DATA
```

This relationship will later be tested by `reproducibility-auditor`.

---

# 61. Research Passport

Recommended fields:

```yaml
data_governance:
  status:
  source_data_identified:
  raw_data_preserved:
  dataset_versions_defined:
  data_dictionary_status:
  transformation_log_status:
  privacy_status:
  access_status:
  analysis_ready_status:
  data_lock_status:
  archive_status:
  reproducibility_handoff_status:
  unresolved_issues:
```

---

# 62. Governance Status

Use one of:

- `DATA_GOVERNANCE_READY`
- `DATA_GOVERNANCE_PARTIAL`
- `DATA_GOVERNANCE_REQUIRES_REVISION`
- `DATA_GOVERNANCE_BLOCKED`
- `DATA_GOVERNANCE_NOT_APPLICABLE`

Do not declare ready while critical provenance is unresolved.

---

# 63. Analysis Readiness Status

Use:

- `NOT_READY_FOR_ANALYSIS`
- `PROVISIONALLY_READY_FOR_ANALYSIS`
- `READY_FOR_DATA_QUALITY_AUDIT`
- `QUALITY_AUDIT_REQUIRED`
- `READY_FOR_ANALYSIS_PLANNING`
- `LOCKED_FOR_ANALYSIS`

Governance alone does not establish statistical quality.

---

# 64. Governance Completeness Matrix

| Domain | Status | Evidence | Risk | Action |
|---|---|---|---|---|
| Source provenance | | | | |
| Raw preservation | | | | |
| Dataset versioning | | | | |
| Variable definitions | | | | |
| Derived variables | | | | |
| Missingness coding | | | | |
| Linkage | | | | |
| Privacy | | | | |
| Access | | | | |
| Transformation log | | | | |
| Quality handoff | | | | |
| Analysis dataset | | | | |
| Retention | | | | |
| Archive | | | | |
| Reproducibility package | | | | |

---

# 65. Critical Governance Failures

Treat as critical when:

- source data cannot be identified;
- raw data were irreversibly overwritten;
- important variables have unknown origin;
- transformation history cannot be reconstructed;
- identifiers are exposed without justification;
- authorization may prohibit use;
- data versions cannot be distinguished;
- results cannot be linked to a dataset version;
- units are materially ambiguous;
- key derived variables lack derivation rules;
- major linkage is undocumented.

---

# 66. Governance vs Data Quality

Do not conflate these.

`research-data-governance` asks:

> Can we trace, understand, control, and reconstruct the data lifecycle?

`data-quality-auditor` asks:

> Are the actual values coherent, plausible, sufficiently complete, and fit for the intended analysis?

Governance precedes and supports quality auditing.

---

# 67. Governance vs Statistical Analysis

Do not allow statistical methods to redefine governance.

Examples:

- normality tests do not determine whether data are valid;
- significance does not determine whether observations should be retained;
- model convergence does not prove variable provenance;
- software acceptance does not prove correct coding.

---

# 68. Governance vs Methodology

Methodology defines what data are scientifically required.

Governance defines how those data are managed and traced.

If governance reveals that required data cannot be reconstructed, route back to:

`methodology-architect`

or:

`protocol-builder`

as appropriate.

---

# 69. Governance vs Instrument Design

`instrument-design` determines how concepts and outcomes are measured.

`research-data-governance` preserves:

- instrument version;
- item identity;
- coding;
- scoring;
- export format;
- transformation lineage.

Do not redesign an instrument merely to simplify data handling.

---

# 70. Handoff to Data Quality Auditor

Before `data-quality-auditor`, provide:

```yaml
quality_handoff:
  dataset_id:
  dataset_version:
  expected_rows:
  expected_units:
  expected_variables:
  identifiers:
  duplicates_policy:
  missing_codes:
  valid_ranges:
  valid_categories:
  logical_rules:
  temporal_rules:
  linkage_rules:
  derived_variables:
  known_issues:
  source_verification_status:
```

---

# 71. Handoff to Analysis Planner

Provide:

- dataset identity;
- version;
- unit of analysis;
- unit of observation;
- time structure;
- cluster structure;
- repeated-measure structure;
- variable roles;
- outcome definitions;
- predictor definitions;
- weights;
- missingness structure;
- censoring fields;
- linkage status;
- derived variables;
- quality status;
- lock status.

---

# 72. Handoff to Manuscript Workflow

Preserve enough information to support:

- data-source description;
- participant flow;
- variable definitions;
- data cleaning description;
- derived-variable description;
- missing-data description;
- linkage description;
- ethics and privacy statements;
- reproducibility statement;
- data-availability statement.

Do not invent these statements at manuscript stage.

---

# 73. Reviewer Response Handoff

If a reviewer asks about:

- data cleaning;
- exclusions;
- missingness;
- coding;
- transformations;
- versions;
- linkage;
- reproducibility;
- data availability;

retrieve the actual governance record.

Do not draft a confident rebuttal from memory.

---

# 74. Governance Decision Logic

```text
Are source data identifiable?
        │
   ┌────┴────┐
   │         │
  No        Yes
   │         │
BLOCK      Are raw data preserved?
             │
        ┌────┴────┐
        │         │
       No        Yes
        │         │
  HIGH RISK     Is variable meaning documented?
                  │
             ┌────┴────┐
             │         │
            No        Yes
             │         │
          REVISE     Are transformations traceable?
                       │
                  ┌────┴────┐
                  │         │
                 No        Yes
                  │         │
               REVISE     Are privacy/access constraints resolved?
                            │
                       ┌────┴────┐
                       │         │
                      No        Yes
                       │         │
                    BLOCK/      READY FOR
                    REVISE      QUALITY AUDIT
```

---

# 75. Minimal Governance Package

For a small project, the minimum may include:

- source-data description;
- preserved raw file;
- analysis dataset;
- data dictionary;
- transformation log;
- version identifiers;
- access status;
- analysis-readiness status.

Do not force enterprise-scale governance onto a trivial dataset.

---

# 76. Expanded Governance Package

For complex projects include, where relevant:

- data-management plan;
- source manifest;
- raw manifest;
- data dictionary;
- codebook;
- transformation log;
- quality rules;
- linkage record;
- privacy plan;
- access matrix;
- retention plan;
- archive plan;
- sharing plan;
- reproducibility package;
- software environment;
- analysis dataset manifest.

---

# 77. Data Management Plan

A project-level plan may contain:

```text
1. Data types
2. Data sources
3. Formats
4. Collection or acquisition
5. Metadata
6. File organization
7. Versioning
8. Storage
9. Backup
10. Access
11. Privacy
12. Security
13. Transformations
14. Quality assurance
15. Sharing
16. Retention
17. Archiving
18. Disposal
19. Responsibilities
20. Reproducibility
```

---

# 78. Source of Truth

Identify the authoritative current record for:

- raw data;
- codebook;
- analysis dataset;
- transformation scripts;
- protocol;
- analysis plan.

Avoid multiple competing “master” files.

---

# 79. Dataset Supersession

When a dataset is replaced, mark the prior one:

`SUPERSEDED_DATA`

and record:

- superseded by;
- reason;
- date;
- downstream outputs affected.

Do not delete the only record of a dataset that generated reported results.

---

# 80. Reanalysis Governance

If data change after analysis, record:

- old dataset version;
- new dataset version;
- reason;
- analyses rerun;
- outputs changed;
- conclusions changed;
- manuscript sections affected.

This is especially important for reviewer-response workflows.

---

# 81. Exploratory and Sensitivity Data

Use labels such as:

- `PRIMARY_ANALYSIS_DATASET`
- `EXPLORATORY_DATASET`
- `SENSITIVITY_DATASET`

when relevant.

Do not retroactively present exploratory preprocessing as confirmatory or preregistered.

---

# 82. Simulated and Synthetic Data

Clearly label simulated and synthetic datasets.

For simulated data preserve:

- generating model;
- parameters;
- random seed;
- sample size;
- software;
- version.

Do not mix simulated and observed records without an explicit indicator.

---

# 83. Public and Secondary Data

Public availability does not eliminate governance needs.

Still record:

- source;
- version;
- license;
- download date;
- transformation;
- citation;
- update status.

For secondary data also assess compatibility with the new research purpose.

---

# 84. Multi-Manuscript Projects

If multiple manuscripts use one parent dataset:

```text
PARENT DATASET
      ↓
MANUSCRIPT-SPECIFIC ANALYSIS DATASETS
      ↓
ANALYSIS OUTPUTS
      ↓
MANUSCRIPT VERSIONS
```

Avoid silent divergence.

---

# 85. Research Program Governance

Integrate with `research-roadmap` when the program depends on:

- cohort maintenance;
- registry development;
- biobank development;
- longitudinal databases;
- shared codebooks;
- validation datasets;
- reusable data infrastructure.

---

# 86. Evidence Separation

Do not mix without explicit labels:

- research data;
- scholarly evidence;
- phenomenon evidence;
- simulated data;
- administrative metadata.

Each supports different claims.

---

# 87. Phenomenon Evidence Relationship

`phenomenon-evidence-builder` may produce factual context data.

If those data enter analysis, route them through `research-data-governance`.

If they only support background claims, full analytical governance may not be required.

---

# 88. Meta-Analysis Relationship

For study-level extraction datasets preserve:

- study identifier;
- outcome;
- comparison;
- follow-up;
- effect estimate;
- standard error or variance;
- sample size;
- transformation;
- dependency structure;
- verification status.

Do not treat copied spreadsheet values as self-explanatory.

---

# 89. Statistical Method Selector Relationship

Provide governed data structure such as:

```text
binary outcome
clustered observations
repeated measures
time-to-event
sampling weights
```

not merely software labels such as:

```text
SPSS file
Jamovi file
SmartPLS file
```

---

# 90. Qualitative and Mixed-Method Relationships

Before `qualitative-analysis`, govern transcript version, anonymization, translation, codebook, and corpus provenance.

Before `mixed-method-analysis`, govern strand-specific datasets and integration keys.

---

# 91. Reproducibility Auditor Relationship

After analysis and before strong reproducibility claims, route to:

`reproducibility-auditor`

The future auditor should test whether:

```text
SOURCE DATA
      ↓
TRANSFORMATION
      ↓
ANALYSIS DATA
      ↓
ANALYSIS
      ↓
OUTPUT
      ↓
REPORTED RESULT
```

can actually be reconstructed.

---

# 92. Ethics and Registration Relationships

When unresolved questions involve consent, privacy, data-use authorization, biosafety, animal data, or regulatory restrictions, route to:

`ethics-regulatory-gate`

when available.

When governance must align with prespecified commitments, connect to:

`registration-preregistration-builder`

when available.

Track differences between:

- planned;
- registered;
- changed before analysis;
- post-hoc.

---

# 93. Governance Output Package

Produce only what the project needs:

1. Data Governance Summary
2. Dataset Registry
3. Source Data Manifest
4. Dataset Provenance Record
5. Variable Dictionary
6. Codebook
7. Transformation Log
8. Access Matrix
9. Privacy Classification
10. Analysis Dataset Manifest
11. Data Lock Status
12. Retention and Archive Plan
13. Data Sharing Status
14. Quality Audit Handoff
15. Analysis Planner Handoff
16. Reproducibility Handoff
17. Research Passport Update

---

# 94. Governance Summary Template

```yaml
research_data_governance:
  project:
  study_id:
  research_question:
  governance_status:
  source_data:
  raw_data_preserved:
  working_data:
  analysis_dataset:
  dataset_version:
  data_dictionary:
  codebook:
  transformation_log:
  identifiers:
  privacy:
  access:
  consent_constraints:
  regulatory_constraints:
  missingness_encoding:
  linkage:
  derived_variables:
  quality_handoff:
  lock_status:
  retention:
  archive:
  sharing:
  reproducibility_handoff:
  unresolved_issues:
```

---

# 95. Dataset Registry Template

| Dataset ID | Name | State | Version | Parent | Source | Access | Privacy | Quality | Lock |
|---|---|---|---|---|---|---|---|---|---|

---

# 96. Transformation Log Template

| ID | Input | Output | Variable/Scope | Operation | Rule | Rationale | Tool | Verification |
|---|---|---|---|---|---|---|---|---|

---

# 97. Access Matrix Template

| Dataset | Role | Read | Write | Export | Share | Re-identify | Approval |
|---|---|---:|---:|---:|---:|---:|---|

---

# 98. User-Friendly Behavior

Do not expose unnecessary internal terminology.

Instead of:

> “Your data governance ontology is incomplete.”

Prefer:

> “I can trace the dataset source and current analysis file, but the transformation from the raw file to the current version is not yet documented. We should reconstruct that step before treating the dataset as analysis-ready.”

Instead of:

> “Privacy classification unresolved.”

Prefer:

> “The file may still contain information that could identify participants, so we should clarify who may access it and whether a de-identified analysis copy is required.”

---

# 99. Avoid Administrative Overload

Use proportional governance.

The scientific minimum is:

> enough documentation and control to understand, protect, and reconstruct the data used for inference.

Do not force a large enterprise data-management plan onto a small student project.

---

# 100. No Cosmetic Governance

A beautifully organized folder can still contain:

- unknown variable origin;
- undocumented recoding;
- overwritten raw data;
- incorrect merges;
- unauthorized use.

Scientific traceability matters more than appearance.

---

# 101. No Software Worship

Do not assume governance quality because the researcher uses:

- REDCap;
- OpenClinica;
- Excel;
- SPSS;
- Jamovi;
- R;
- Python;
- SAS;
- Stata;
- SQL;
- cloud platforms;
- laboratory software.

Tools may support governance but do not guarantee it.

---

# 102. No Silent Data Cleaning

Never silently:

- trim values;
- coerce types;
- delete blanks;
- remove outliers;
- deduplicate;
- recode;
- impute;
- convert units;
- fix dates;
- rename categories.

Every scientifically relevant change must remain visible.

---

# 103. No Result-Driven Cleaning

Do not clean data differently because:

- a p-value is undesirable;
- an effect is small;
- a model does not converge;
- a hypothesis is unsupported;
- a journal preference exists.

Cleaning must be evidence-driven.

---

# 104. Publication Independence

Journal requirements may affect:

- data availability statements;
- repository deposit;
- supplementary formats.

They must not alter the scientific data record.

APC preference, journal prestige, quartile, or publication strategy must not influence:

- data retention;
- cleaning;
- access;
- evidence quality;
- dataset selection.

---

# 105. Stop Conditions

Stop and request clarification, upstream review, or governance repair when:

- source data cannot be identified;
- the only raw data were overwritten;
- major variables have unknown meaning;
- critical transformations cannot be reconstructed;
- the analysis dataset cannot be linked to a source;
- privacy status is unresolved for identifiable data;
- data-use authorization may be absent;
- consent scope may prohibit intended use;
- linkage keys are unreliable;
- units are materially ambiguous;
- multiple competing “final” datasets exist;
- major exclusions are undocumented;
- derived variables cannot be reproduced;
- the dataset used for reported results cannot be identified.

Use one or more statuses:

- `DATA_GOVERNANCE_REQUIRES_REVISION`
- `DATA_GOVERNANCE_BLOCKED`
- `SOURCE_DATA_UNRESOLVED`
- `PROVENANCE_UNRESOLVED`
- `PRIVACY_STATUS_UNRESOLVED`
- `ACCESS_STATUS_UNRESOLVED`
- `CONSENT_SCOPE_UNRESOLVED`
- `DATASET_VERSION_UNRESOLVED`
- `TRANSFORMATION_HISTORY_UNRESOLVED`
- `ANALYSIS_DATASET_NOT_READY`

Do not proceed merely to maintain workflow momentum.

---

# 106. Relationship with Research Router

`research-router` should route here when the user:

- has a dataset but provenance is unclear;
- is preparing data collection;
- is merging datasets;
- needs an analysis-ready file;
- is continuing previous research with inherited data;
- is preparing reproducible analysis;
- is responding to reviewer questions about data handling;
- needs sharing, retention, or archive planning.

---

# 107. Relationship with Research Intake and Resume

`research-intake` should capture whether the user already has:

- raw data;
- processed data;
- analysis data;
- codebook;
- scripts;
- source documentation;
- privacy constraints;
- data agreements.

`research-resume` should preserve existing data assets and identify whether old datasets require governance reconstruction.

---

# 108. Relationship with Previous Research and Roadmap Skills

`prior-research-auditor` may identify unresolved historical data provenance.

`research-trajectory-mapper` may identify data assets that support a long-term research niche.

`research-roadmap` may treat data infrastructure, registries, cohorts, biobanks, and validation datasets as scientific capabilities or dependencies.

---

# 109. Relationship with Problem-Solving and Methodology

`problem-solving-approach` defines the evidence required.

`methodology-architect` defines the design and data structure required.

`research-data-governance` ensures those requirements survive data generation and transformation.

If the required evidence cannot be reconstructed, route upstream.

---

# 110. Relationship with Protocol, Sampling, and Instrument Design

`protocol-builder` defines how data are operationally generated.

`sampling-strategy` defines how units enter the study.

`instrument-design` defines how concepts and outcomes are measured.

Governance preserves these decisions as explicit data structures and provenance records.

---

# 111. Relationship with Analysis Planner

Only route to `analysis-planner` when data meaning and structure are sufficiently clear.

A sophisticated analysis cannot rescue unknown data provenance.

---

# 112. Relationship with Result Interpretation and Discussion

`result-interpreter` should know:

- dataset version;
- quality status;
- missingness;
- exclusions;
- transformations;
- sensitivity datasets.

`scientific-discussion` should receive governance limitations that materially affect validity, measurement, missingness, linkage, selection, or reproducibility.

---

# 113. Relationship with Manuscript Workflow

`manuscript-architect` and `manuscript-writer` may use governance facts for:

- Methods;
- supplementary materials;
- data availability;
- reproducibility;
- privacy statements.

`manuscript-auditor` should verify that such claims correspond to the actual governance record.

Do not invent statements such as:

> “Data were anonymized.”

or:

> “Data are available upon request.”

without evidence.

---

# 114. Relationship with Reviewer Simulation and Response

`reviewer-simulator` may challenge:

- unclear cleaning;
- undocumented exclusions;
- missing-data handling;
- data availability;
- reproducibility;
- dataset provenance.

`reviewer-response` should route actual reviewer questions back to the governed record rather than answering from memory.

---

# 115. Compact User-Facing Output

Example:

```text
Data governance status: PARTIAL

Source data
- Original source identified.
- Raw export preserved.

Current analysis dataset
- Version identified.
- Major derived variables documented.

Still unresolved
- The merge between two source files is not fully documented.
- Missing-value code 99 is not formally defined.
- Access restrictions for identifiable linkage keys need clarification.

Next action
Reconstruct the merge record and missing-value dictionary before data-quality auditing.
```

---

# 116. Research Data Governance Passport

```yaml
research_data_governance_passport:
  project:
  status:
  source_data_status:
  raw_data_status:
  dataset_registry_status:
  data_dictionary_status:
  codebook_status:
  transformation_log_status:
  derived_variable_status:
  identifier_status:
  privacy_status:
  access_status:
  linkage_status:
  missingness_status:
  quality_handoff_status:
  analysis_dataset_version:
  lock_status:
  retention_status:
  archive_status:
  sharing_status:
  reproducibility_handoff_status:
  unresolved_issues:
  next_action:
```

---

# 117. Final Governance Rule

Never allow convenience to replace provenance.

Never allow software to replace scientific meaning.

Never allow a “clean” dataset to erase the path from source data to inference.

---

# Success Criterion

`research-data-governance` succeeds when the research data lifecycle is scientifically traceable, operationally controlled, ethically and institutionally defensible, and sufficiently documented that the source, meaning, version, transformation history, access status, privacy status, derived variables, missingness conventions, linkage logic, analysis-ready dataset, retention plan, archive state, and downstream handoffs can be understood and reconstructed without relying on undocumented memory; when raw or authoritative source data remain distinguishable from working, cleaned, linked, derived, and analysis-ready data; when every analytically meaningful transformation is explicit rather than silently embedded in software or spreadsheets; when privacy, consent, access, regulatory, and sharing constraints remain visible instead of being assumed away; when dataset versions and result provenance can be linked; when governance does not preempt data-quality assessment, statistical analysis, or scientific interpretation; and when the governed dataset can be handed transparently to `data-quality-auditor`, `analysis-planner`, and ultimately `reproducibility-auditor` without allowing convenience, publication strategy, software preference, or desired results to redefine the scientific evidence.
