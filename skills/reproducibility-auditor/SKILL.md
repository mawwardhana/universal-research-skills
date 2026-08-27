---
name: reproducibility-auditor
description: Audit whether a completed or near-completed research workflow can be reconstructed from the scientific record, source data, governed transformations, quality decisions, analysis datasets, scripts or procedures, software versions, parameters, outputs, and reported results. Use after data governance, data-quality review, and analysis are sufficiently mature, and before strong reproducibility claims, manuscript finalization, reviewer response, data sharing, or archival release. This skill distinguishes computational reproducibility from broader methodological replicability, identifies missing provenance or irreproducible steps, verifies result-to-data traceability, and produces a bounded reproducibility status without fabricating unavailable scripts, environments, source data, or execution success.
---

# Reproducibility Auditor

## Purpose

`reproducibility-auditor` determines whether another competent researcher could reconstruct what was actually done and recover the analytical path from source evidence to reported result using the available research record.

Its central question is:

> Can the study's analytical record be reconstructed transparently enough that the source data, transformations, analysis-ready dataset, analytical procedures, software environment, outputs, and reported results can be traced and, where feasible, rerun or independently checked?

The core traceability chain is:

```text
RESEARCH QUESTION
        ↓
PROTOCOL / REGISTERED PLAN
        ↓
SOURCE DATA
        ↓
DATA GOVERNANCE
        ↓
DATA QUALITY DECISIONS
        ↓
ANALYSIS DATASET
        ↓
ANALYSIS PROCEDURE
        ↓
SOFTWARE / VERSION / PARAMETERS
        ↓
ANALYTICAL OUTPUT
        ↓
REPORTED RESULT
```

This skill audits the chain.

It does not assume that having code is sufficient.

It does not assume that absence of code makes all research irreproducible.

---

# 1. Core Principle

The central principle is:

> **A research result is reproducible only to the extent that the scientific path producing it is sufficiently explicit, traceable, and reconstructable.**

Reproducibility is not a stylistic claim.

It is an evidentiary property of the research record.

---

# 2. Reproducibility vs Replicability

Use these distinctions:

`computational reproducibility`:
another researcher can rerun the same analytical workflow on the same data and obtain materially equivalent outputs.

`analytical reproducibility`:
another researcher can reconstruct the analytical procedure from the documented record even when exact execution artifacts are not fully available.

`methodological replicability`:
another researcher can repeat the study design or procedure with new data.

`conceptual replication`:
the underlying scientific claim is tested using a meaningfully different operationalization or design.

Do not collapse all of these into one status.

---

# 3. Activation Gate

Use `reproducibility-auditor` when:

- analysis has been completed;
- manuscript results already exist;
- data and scripts are being prepared for sharing;
- a reviewer requests code, data, or reproducibility evidence;
- a previous study is being continued or audited;
- a result cannot be regenerated reliably;
- multiple analysts produced outputs;
- software versions may have changed;
- interactive software was used without scripts;
- analysis involved manual steps;
- a research archive is being prepared;
- a repository or journal requires reproducibility materials;
- a long-term research program needs reusable analytical assets.

Do not invoke prematurely when:

- the methodology is not yet stable;
- the dataset has not passed governance or quality review;
- no analysis has been performed;
- the user is only asking for prospective reproducibility planning.

In prospective cases, provide reproducibility requirements rather than an audit verdict.

---

# 4. Required Upstream Inputs

Use, when available:

- research question;
- hypotheses where relevant;
- theoretical or conceptual framework where relevant;
- methodology architecture;
- protocol;
- preregistration or registration record;
- sampling strategy;
- instrument definitions;
- source data;
- raw-data manifest;
- data dictionary;
- codebook;
- transformation log;
- data-quality audit;
- analysis dataset;
- analysis plan;
- statistical method;
- qualitative analysis protocol;
- mixed-method integration plan;
- meta-analysis dataset;
- scripts;
- commands;
- software versions;
- package versions;
- random seeds;
- environment files;
- output tables;
- figures;
- logs;
- manuscript results;
- supplementary materials;
- data-availability statement;
- known deviations.

Do not invent missing artifacts.

---

# 5. Audit Scope

Audit, where relevant:

- research-question traceability;
- protocol traceability;
- preregistration alignment;
- source-data availability;
- source-data identity;
- data provenance;
- transformation reproducibility;
- data-quality decision reproducibility;
- analysis-dataset reconstruction;
- variable definition stability;
- derived-variable reconstruction;
- code availability;
- script completeness;
- manual-step documentation;
- software identity;
- software version;
- package version;
- operating environment;
- random seeds;
- model parameters;
- analysis options;
- graphical settings where scientifically relevant;
- output regeneration;
- result-to-output mapping;
- table reproducibility;
- figure reproducibility;
- manuscript-number consistency;
- sensitivity-analysis reproducibility;
- deviation traceability;
- data-sharing compatibility;
- archival completeness.

---

# 6. Reproducibility Status

Use one of:

- `REPRODUCIBLE`
- `SUBSTANTIALLY_REPRODUCIBLE`
- `PARTIALLY_REPRODUCIBLE`
- `REPRODUCIBILITY_AT_RISK`
- `NOT_REPRODUCIBLE`
- `INSUFFICIENT_INFORMATION`
- `NOT_APPLICABLE`

Do not use `REPRODUCIBLE` unless the claim is actually supported.

---

# 7. Reproducibility Dimensions

Evaluate separately:

- `DATA_REPRODUCIBILITY`
- `TRANSFORMATION_REPRODUCIBILITY`
- `ANALYSIS_REPRODUCIBILITY`
- `ENVIRONMENT_REPRODUCIBILITY`
- `OUTPUT_REPRODUCIBILITY`
- `REPORTING_REPRODUCIBILITY`
- `MANUAL_STEP_REPRODUCIBILITY`
- `METHODOLOGICAL_REPLICABILITY`

A study may be strong in one dimension and weak in another.

---

# 8. Audit Evidence Levels

Use:

- `DIRECTLY_VERIFIED`
- `DOCUMENTED_NOT_EXECUTED`
- `INFERRED_FROM_RECORD`
- `PARTIALLY_DOCUMENTED`
- `UNVERIFIED`
- `UNAVAILABLE`

Do not convert documentation into execution evidence.

---

# 9. Strongest Reproducibility Evidence

Strong evidence may include:

- preserved source data;
- immutable raw-data snapshot;
- versioned analysis dataset;
- executable scripts;
- environment file;
- package lock file;
- saved random seeds;
- machine-readable parameters;
- reproducible tables and figures;
- deterministic build process;
- independent rerun;
- matching rerun outputs;
- recorded manual decisions;
- result mapping.

---

# 10. Weak Reproducibility Evidence

Weak evidence may include:

- screenshots only;
- copied software output;
- undocumented menu clicks;
- analyst memory;
- unnamed spreadsheet;
- “final.sav” without provenance;
- “clean.xlsx” without transformation history;
- manuscript numbers without output source;
- code fragments without execution order;
- undocumented manual exclusions.

---

# 11. Traceability Backbone

Use:

```text
CLAIM
  ↓
MANUSCRIPT RESULT
  ↓
OUTPUT
  ↓
ANALYSIS PROCEDURE
  ↓
ANALYSIS DATASET
  ↓
TRANSFORMATION HISTORY
  ↓
SOURCE DATA
```

Every important inferential claim should be traceable through this backbone.

---

# 12. Research Question Traceability

Check whether each major analysis clearly maps to:

- research question;
- objective;
- hypothesis;
- exploratory question;
- sensitivity question.

Do not accept analyses that cannot be linked to a scientific purpose.

---

# 13. Protocol Traceability

Check whether the implemented analysis can be mapped to:

- protocol;
- methodology;
- approved deviations;
- analysis plan.

---

# 14. Registration Traceability

Where registration or preregistration exists, distinguish:

- prespecified;
- amended before analysis;
- amended after data inspection;
- exploratory;
- post-hoc.

Do not conceal deviations.

---

# 15. Source Data Identity

Verify:

```yaml
source_data_identity:
  source_id:
  source_name:
  source_version:
  extraction_date:
  source_location:
  access_status:
  checksum_if_available:
  notes:
```

If the source dataset cannot be identified, data reproducibility is compromised.

---

# 16. Raw Data Preservation

Check whether:

- original exports are preserved;
- original file names are known;
- original timestamps are documented;
- extraction filters are known;
- dynamic sources have snapshots or reproducible queries.

---

# 17. Data Governance Dependency

`research-data-governance` should establish:

- source;
- state;
- version;
- meaning;
- access;
- privacy;
- transformation history.

If these are unresolved, return upstream.

---

# 18. Data Quality Dependency

`data-quality-auditor` should establish:

- actual issues;
- corrections;
- retained unusual values;
- exclusions;
- corrected version;
- unresolved limitations.

Reproducibility audit must verify those decisions can be reconstructed.

---

# 19. Dataset Reconstruction Test

Ask:

> Can the analysis-ready dataset be regenerated from the governed upstream data?

Possible results:

- `FULLY_RECONSTRUCTABLE`
- `MOSTLY_RECONSTRUCTABLE`
- `PARTIALLY_RECONSTRUCTABLE`
- `NOT_RECONSTRUCTABLE`
- `NOT_TESTED`

---

# 20. Transformation Reconstruction

For each transformation determine whether there is:

- script;
- formula;
- documented rule;
- order of operations;
- input dataset;
- output dataset;
- version;
- verification.

---

# 21. Manual Transformation Guard

Manual steps are allowed.

But they must be documented.

Examples:

- manually corrected sample ID;
- manually relabeled category;
- manually excluded corrupted file;
- manually resolved ambiguous linkage.

A reproducible workflow can contain manual steps if those steps are explicit and recoverable.

---

# 22. Spreadsheet Reproducibility

Spreadsheet workflows require additional checks:

- formulas visible;
- formulas consistent;
- hidden sheets reviewed;
- hidden rows or columns reviewed;
- external links documented;
- manual edits documented;
- pivot tables reproducible;
- sort/filter state understood;
- cell references stable.

Do not claim reproducibility merely because the workbook is available.

---

# 23. Script Reproducibility

For scripted workflows check:

- execution order;
- dependencies;
- paths;
- hard-coded locations;
- package versions;
- functions;
- random seeds;
- environment;
- required input files;
- generated outputs.

---

# 24. Notebook Reproducibility

For notebooks check:

- cell execution order;
- hidden state;
- stale outputs;
- environment;
- external files;
- deterministic rerun;
- parameterization;
- nonexecuted cells.

A notebook that only works because of prior hidden state is not fully reproducible.

---

# 25. GUI-Based Analysis

GUI workflows can be reproducible if sufficiently documented.

Record:

- software;
- version;
- module;
- menu path;
- analysis options;
- variable assignment;
- filters;
- transformations;
- output settings;
- saved project file.

Do not penalize GUI analysis merely because it lacks code.

---

# 26. Jamovi Reproducibility

For Jamovi or similar analysis files preserve, where possible:

- `.omv` or project file;
- application version;
- module names;
- module versions;
- variable transformations;
- filters;
- computed variables;
- analysis options;
- output tables.

---

# 27. SPSS Reproducibility

Prefer:

- syntax;
- dataset version;
- output file;
- software version.

If only menu-based work exists, reconstruct and document settings.

---

# 28. R Reproducibility

Preserve:

- R version;
- package versions;
- scripts;
- seed;
- session information;
- environment or lock file where useful.

---

# 29. Python Reproducibility

Preserve:

- Python version;
- package versions;
- environment;
- scripts or notebooks;
- seed;
- input paths;
- command line;
- configuration files.

---

# 30. Stata Reproducibility

Preserve:

- Stata version;
- do-files;
- ado dependencies;
- dataset versions;
- logs.

---

# 31. SAS Reproducibility

Preserve:

- SAS version;
- program files;
- libraries;
- macros;
- logs;
- input datasets.

---

# 32. SQL Reproducibility

Preserve:

- query;
- database snapshot or version context;
- schema;
- filters;
- joins;
- date;
- database engine;
- relevant settings.

---

# 33. SmartPLS Reproducibility

Where relevant preserve:

- SmartPLS version;
- project file;
- model specification;
- indicator assignments;
- algorithm settings;
- bootstrap settings;
- missing-data handling;
- weighting scheme;
- interaction construction;
- output exports.

---

# 34. SEM / PLS-SEM Reproducibility

Preserve:

- measurement model;
- structural model;
- estimator;
- bootstrapping;
- seeds if applicable;
- missing-data method;
- convergence criteria;
- model modifications;
- final model version.

---

# 35. Qualitative Analysis Reproducibility

Qualitative reproducibility should not be reduced to identical coding.

Audit:

- corpus identity;
- transcript versions;
- translation;
- codebook;
- coding process;
- coder roles;
- memo trail;
- theme development;
- negative cases;
- reflexive decisions;
- software version where relevant.

Use `analytic transparency` where exact computational reproduction is inappropriate.

---

# 36. Mixed-Method Reproducibility

Audit:

- quantitative strand;
- qualitative strand;
- integration timing;
- linking variables;
- joint displays;
- meta-inference rules.

---

# 37. Meta-Analysis Reproducibility

Preserve:

- included studies;
- extraction dataset;
- effect calculations;
- conversions;
- dependency handling;
- effect model;
- heterogeneity estimator;
- subgroup rules;
- meta-regression;
- bias diagnostics;
- sensitivity analyses;
- software version.

---

# 38. Bibliometric Reproducibility

Where relevant preserve:

- database;
- search date;
- query;
- indexes;
- filters;
- export format;
- deduplication;
- cleaning;
- software;
- network parameters.

Database updates may make exact corpus reproduction impossible; document temporal dependence.

---

# 39. Experimental Reproducibility

Audit:

- experimental protocol;
- reagent lot;
- instrument;
- calibration;
- operator;
- timing;
- environmental conditions;
- randomization;
- blinding;
- replicate structure;
- raw measurements;
- preprocessing.

---

# 40. Laboratory Workflow Reproducibility

Preserve:

- sample IDs;
- run IDs;
- batch;
- protocol version;
- instrument output;
- QC;
- exclusions;
- reruns;
- calculation steps.

---

# 41. Genomic Reproducibility

Preserve:

- reference genome/build;
- pipeline;
- tool versions;
- parameters;
- raw reads;
- preprocessing;
- alignment;
- variant calling;
- annotation database version;
- filters.

---

# 42. Sanger Sequencing Reproducibility

Where relevant preserve:

- `.ab1`;
- `.seq`;
- forward/reverse identity;
- trimming decisions;
- consensus method;
- reference sequence;
- alignment parameters;
- SNP position definition.

---

# 43. Pharmacokinetic Reproducibility

Preserve:

- dose;
- sampling times;
- concentration data;
- units;
- BLQ handling;
- noncompartmental or modeling settings;
- software;
- derived PK calculations.

---

# 44. PBPK Reproducibility

Preserve:

- software version;
- model file;
- compound parameters;
- population;
- physiology inputs;
- simulation settings;
- individual vs population mode;
- seed if stochastic;
- scenarios;
- outputs.

---

# 45. Machine-Learning Reproducibility

Preserve:

- train/validation/test split;
- seed;
- feature preprocessing;
- model architecture;
- hyperparameters;
- training environment;
- stopping rule;
- metrics;
- threshold selection;
- final model object when appropriate.

---

# 46. AI-Assisted Analysis

If AI systems contribute to analysis, preserve where materially relevant:

- system/model identity;
- date;
- task;
- prompt or structured instruction;
- input scope;
- output;
- human review;
- acceptance/rejection decisions;
- non-determinism limits.

Do not overclaim deterministic reproducibility for stochastic AI services.

---

# 47. Software Identity

Record:

```yaml
software:
  name:
  version:
  operating_system:
  module_or_package:
  module_version:
  environment:
  notes:
```

---

# 48. Version Importance

A version is materially important when:

- algorithms changed;
- defaults changed;
- numerical behavior changed;
- modules changed;
- package APIs changed;
- output definitions changed.

Do not require version details when they are scientifically immaterial.

---

# 49. Package Locking

Where useful preserve:

- `requirements.txt`;
- `environment.yml`;
- `renv.lock`;
- container definition;
- equivalent lock file.

Do not require containers for every study.

---

# 50. Operating System Dependence

Assess only where relevant.

Potential differences may arise from:

- paths;
- locale;
- floating-point libraries;
- encoding;
- parallel processing;
- external binaries.

---

# 51. Locale Reproducibility

Preserve if relevant:

- decimal separator;
- date format;
- character encoding;
- timezone;
- language.

---

# 52. Randomness

Record random seeds where materially relevant.

Examples:

- bootstrap;
- permutation;
- imputation;
- train-test split;
- simulation;
- random initialization;
- stochastic optimization.

---

# 53. Determinism Status

Use:

- `DETERMINISTIC`
- `SEED_CONTROLLED`
- `PARTIALLY_STOCHASTIC`
- `NONDETERMINISTIC`
- `UNKNOWN`

---

# 54. Parameter Capture

Preserve analytical parameters such as:

- confidence level;
- bootstrap repetitions;
- convergence criteria;
- optimizer;
- weighting scheme;
- penalty;
- threshold;
- smoothing;
- bandwidth;
- number of components;
- number of clusters;
- random effects structure.

---

# 55. Default-Setting Guard

Do not write:

> “default settings were used”

when defaults differ by version or are scientifically important.

Record relevant defaults explicitly.

---

# 56. Analysis Procedure Identity

Every major analysis should have a stable identifier.

Example:

```yaml
analysis_procedure:
  analysis_id:
  research_question:
  dataset_version:
  method:
  software:
  parameters:
  script_or_project:
  output:
  status:
```

---

# 57. Analysis Order

Preserve execution dependencies.

Example:

```text
01_import
02_clean
03_derive_variables
04_primary_analysis
05_sensitivity_analysis
06_tables
07_figures
```

---

# 58. Hard-Coded Path Audit

Check scripts for paths tied to one machine.

Prefer relative or configurable paths.

Do not require rewriting if archival instructions sufficiently resolve paths.

---

# 59. External Dependency Audit

Identify:

- external databases;
- APIs;
- web resources;
- unpublished files;
- proprietary libraries;
- institutional servers.

These may limit full rerun capability.

---

# 60. Proprietary Software

Proprietary software does not automatically make analysis irreproducible.

But record:

- software;
- version;
- required license;
- project or syntax files;
- settings.

---

# 61. Restricted Data

Restricted data can still support reproducibility under controlled access.

Distinguish:

- reproducible internally;
- reproducible under controlled access;
- publicly reproducible;
- not reproducible due to inaccessible data.

---

# 62. Data Availability Status

Use:

- `OPEN_DATA`
- `CONTROLLED_ACCESS_DATA`
- `RESTRICTED_DATA`
- `NONSHAREABLE_WITH_JUSTIFICATION`
- `DATA_UNAVAILABLE`
- `STATUS_UNKNOWN`

---

# 63. Code Availability Status

Use:

- `OPEN_CODE`
- `CONTROLLED_CODE`
- `INTERNAL_CODE`
- `PROPRIETARY_WORKFLOW`
- `NO_CODE_BUT_DOCUMENTED_GUI_WORKFLOW`
- `CODE_UNAVAILABLE`
- `STATUS_UNKNOWN`

---

# 64. Output Identity

Each major output should have:

```yaml
output:
  output_id:
  analysis_id:
  dataset_version:
  file:
  table_or_figure:
  generation_method:
  timestamp:
  verification:
```

---

# 65. Table Reproducibility

For every important table ask:

- can the table be regenerated?;
- are all numbers traceable?;
- are formatting-only edits separated from analytical values?;
- were denominators preserved?;
- are rounding rules documented?;
- are footnotes consistent with analysis?

---

# 66. Figure Reproducibility

For every important figure ask:

- can the figure be regenerated?;
- is underlying data known?;
- are transformations known?;
- are axis decisions documented?;
- are smoothing or aggregation settings known?;
- were manual edits scientifically neutral?

---

# 67. Manual Figure Editing

Cosmetic editing is acceptable if it does not alter scientific meaning.

Document material changes.

Do not manually reposition data points to improve appearance.

---

# 68. Result Mapping

Each manuscript result should map to output.

Recommended:

```yaml
result_mapping:
  result_id:
  manuscript_location:
  claim:
  output_id:
  analysis_id:
  dataset_version:
  verification_status:
```

---

# 69. Numerical Consistency

Audit consistency between:

- software output;
- manuscript text;
- tables;
- figures;
- abstract;
- supplementary material.

---

# 70. Rounding Audit

Distinguish:

- analysis precision;
- stored precision;
- reported precision.

Do not treat harmless rounding differences as irreproducibility.

---

# 71. Percentage Reconciliation

Check:

```text
count / denominator × 100
```

where applicable.

Verify denominators change appropriately with missing data.

---

# 72. P-Value Reconciliation

Check that manuscript p-values match the actual analysis output.

Do not recalculate with a different model merely to force agreement.

---

# 73. Confidence Interval Reconciliation

Verify:

- estimate;
- lower bound;
- upper bound;
- confidence level;
- transformation scale.

---

# 74. Effect Size Reconciliation

Verify effect measure identity.

Examples:

- OR;
- RR;
- HR;
- mean difference;
- standardized mean difference;
- beta;
- correlation;
- path coefficient.

---

# 75. Model Identity

Ensure reported model corresponds to the actual fitted model.

Preserve:

- variable set;
- transformations;
- interactions;
- random effects;
- covariates;
- selection procedure.

---

# 76. Primary vs Sensitivity Analysis

Label clearly:

- primary;
- secondary;
- exploratory;
- sensitivity;
- post-hoc.

Do not substitute a favorable sensitivity result for the primary result without disclosure.

---

# 77. Sensitivity Reproducibility

Each sensitivity analysis should have:

- rationale;
- dataset version;
- analysis change;
- output;
- interpretation.

---

# 78. Missing Data Reproducibility

Preserve:

- missing codes;
- exclusion rules;
- imputation method;
- model;
- seed;
- number of imputations;
- pooling method.

---

# 79. Imputation Dataset Identity

Do not silently replace original missing values.

Preserve imputed datasets or enough information to regenerate them where feasible.

---

# 80. Outlier Decision Reproducibility

For removed or transformed outliers preserve:

- flagging method;
- source verification;
- scientific rationale;
- final decision;
- sensitivity impact.

---

# 81. Exclusion Reproducibility

Every exclusion affecting sample size should be recoverable.

---

# 82. Participant Flow Reproducibility

Participant flow counts should trace to data and exclusion rules.

---

# 83. Qualitative Theme Traceability

For qualitative studies, check whether:

```text
SOURCE MATERIAL
      ↓
CODING
      ↓
CATEGORIES
      ↓
THEMES
      ↓
INTERPRETATION
```

is sufficiently transparent.

Exact identical recoding is not required for interpretive reproducibility.

---

# 84. Mixed-Method Meta-Inference Traceability

Check whether integrated conclusions can be traced to both strands and the integration procedure.

---

# 85. Meta-Analysis Study Inclusion Traceability

Check:

```text
SEARCH
  ↓
SCREENING
  ↓
INCLUDED STUDIES
  ↓
EXTRACTION
  ↓
EFFECT DATA
  ↓
MODEL
  ↓
POOLED RESULT
```

---

# 86. Reproducibility Execution Test

When possible, execute:

- import;
- transformation;
- analysis;
- table generation;
- figure generation.

Compare results to archived outputs.

Do not claim an execution test occurred unless it actually occurred.

---

# 87. Execution Test Status

Use:

- `FULL_RERUN_PASS`
- `PARTIAL_RERUN_PASS`
- `RERUN_WITH_MINOR_DIFFERENCES`
- `RERUN_FAILED`
- `RERUN_NOT_ATTEMPTED`
- `RERUN_NOT_POSSIBLE`

---

# 88. Difference Classification

If rerun differs, classify:

- harmless formatting difference;
- rounding difference;
- package-version difference;
- stochastic difference;
- data-version difference;
- parameter difference;
- substantive numerical difference;
- substantive inferential difference;
- unresolved difference.

---

# 89. Material Reproducibility Difference

A difference is material when it changes:

- estimate meaning;
- effect direction;
- statistical conclusion;
- uncertainty;
- ranking;
- subgroup interpretation;
- qualitative theme;
- scientific conclusion.

---

# 90. Tolerance Guard

Do not require bit-for-bit identical numerical values when:

- floating-point variation;
- stochastic methods;
- package updates

produce scientifically immaterial differences.

---

# 91. Reproducibility vs Validity

A perfectly reproducible analysis can still be scientifically wrong.

Reproducibility does not establish:

- correct research question;
- correct design;
- correct statistical model;
- absence of bias;
- causal validity.

It establishes recoverability of the performed workflow.

---

# 92. Reproducibility vs Transparency

Transparency is necessary but not always sufficient.

A workflow may be transparently described yet impossible to rerun because data are lost.

---

# 93. Reproducibility vs Open Science

Open sharing improves accessibility but is not synonymous with reproducibility.

Restricted but well-governed research can be reproducible.

---

# 94. Reproducibility vs Replication

Do not claim that reproducing the original analysis independently confirms the scientific phenomenon.

That requires replication evidence.

---

# 95. Documentation Completeness

Check presence and adequacy of:

- README;
- file manifest;
- dataset manifest;
- codebook;
- transformation log;
- analysis plan;
- script index;
- software environment;
- output map;
- result map.

---

# 96. README for Reproducibility Package

A useful README should explain:

```text
1. Study identity
2. Research question
3. Folder structure
4. Data access
5. Dataset versions
6. Execution order
7. Software requirements
8. Scripts/project files
9. Outputs
10. Known limitations
```

---

# 97. File Manifest

Recommended:

| File | Role | Version | Input/Output | Required | Access |
|---|---|---|---|---|---|

---

# 98. Script Manifest

| Script | Purpose | Input | Output | Order | Environment |
|---|---|---|---|---:|---|

---

# 99. Result Manifest

| Result ID | Manuscript Location | Output | Analysis | Dataset Version | Verified |
|---|---|---|---|---|---|

---

# 100. Reproducibility Issue Register

Use:

```yaml
reproducibility_issue:
  issue_id:
  component:
  description:
  severity:
  evidence:
  consequence:
  repair_action:
  repair_status:
  residual_risk:
```

---

# 101. Severity Classification

Use:

- `CRITICAL`
- `MAJOR`
- `MODERATE`
- `MINOR`
- `INFORMATIONAL`

---

# 102. Critical Reproducibility Failures

Examples:

- analysis dataset lost;
- source-to-analysis transformation impossible to reconstruct;
- primary result cannot be linked to an output;
- model specification unknown;
- major manually edited output with no source;
- wrong dataset version used;
- core code missing and procedure undocumented;
- sample selection cannot be reconstructed.

---

# 103. Major Reproducibility Issues

Examples:

- package versions missing;
- derived variables partly undocumented;
- some sensitivity analyses cannot be rerun;
- GUI settings incomplete;
- random seed missing for stochastic method;
- manual corrections incompletely documented.

---

# 104. Moderate Issues

Examples:

- nonessential plot formatting unavailable;
- minor environment differences;
- some auxiliary analyses undocumented.

---

# 105. Minor Issues

Examples:

- inconsistent filenames;
- missing optional comments;
- formatting-only discrepancies.

---

# 106. Repairability

Classify issues:

- `FULLY_REPAIRABLE`
- `PARTIALLY_REPAIRABLE`
- `NOT_REPAIRABLE`
- `REQUIRES_SOURCE_ACCESS`
- `REQUIRES_ORIGINAL_ANALYST`
- `UNKNOWN`

---

# 107. Reproducibility Repair

Possible repair actions:

- recover original dataset;
- reconstruct transformations;
- write missing script;
- export GUI settings;
- preserve project file;
- document manual steps;
- create environment lock;
- map outputs to results;
- rerun analysis;
- regenerate tables;
- create README.

---

# 108. No Fabricated Repair

Do not pretend to reconstruct missing analysis logic if the record does not support it.

Mark uncertainty.

---

# 109. Analyst Memory

Analyst recollection may help reconstruct workflow but should be labeled as retrospective.

Do not treat memory as equivalent to contemporaneous documentation.

---

# 110. Retrospective Reconstruction

When rebuilding an old study, label:

- contemporaneously documented;
- retrospectively reconstructed;
- inferred;
- unverifiable.

---

# 111. Historical Software

If old software is unavailable, determine whether:

- compatible version exists;
- archived installer exists;
- equivalent method can be implemented elsewhere;
- exact reproduction is impossible.

Do not silently switch methods and call it exact reproduction.

---

# 112. Method Equivalence

An equivalent implementation may support analytical verification.

Label it:

`INDEPENDENT_EQUIVALENT_IMPLEMENTATION`

not exact rerun.

---

# 113. Independent Verification

Strong evidence may arise when a second analyst independently reconstructs the analysis.

Record:

- analyst;
- data version;
- method;
- implementation;
- comparison.

---

# 114. Double Programming

For high-stakes analyses, independent code implementations may be useful.

Do not require this universally.

---

# 115. Reproducibility Across Platforms

Cross-platform consistency may be tested when scientifically material.

---

# 116. Proprietary Black-Box Algorithms

If a proprietary tool hides implementation details, document:

- tool;
- version;
- settings;
- inputs;
- outputs.

Classify algorithmic transparency separately from operational reproducibility.

---

# 117. Web Applications

For analysis conducted in web apps preserve:

- app name;
- version/date;
- project export;
- settings;
- source data;
- screenshots only as supplemental evidence;
- exported outputs.

---

# 118. Dynamic Online Tools

If the tool changes over time, preserve date and version where possible.

---

# 119. API-Based Analysis

Record:

- API version;
- model or endpoint;
- parameters;
- request date;
- response;
- stochasticity.

---

# 120. Cloud Compute

Where relevant preserve:

- environment;
- container;
- hardware dependencies;
- workflow;
- job configuration.

---

# 121. Hardware Dependence

Hardware details matter mainly when they materially affect results.

Examples:

- GPU nondeterminism;
- specialized instrument;
- laboratory device;
- imaging scanner.

---

# 122. Containerization

Containers can improve reproducibility.

Do not require Docker or similar tools for every study.

---

# 123. Workflow Automation

Build systems or workflow engines may strengthen reproducibility when complexity justifies them.

---

# 124. Reproducibility Burden Proportionality

Use proportional auditing.

A simple descriptive study may need:

- dataset;
- documented transformations;
- saved analysis project;
- output map.

A complex computational study may need:

- environment lock;
- scripts;
- seeds;
- dependencies;
- build instructions;
- archived outputs.

---

# 125. Student Research

Do not impose industrial-scale reproducibility infrastructure on small student projects.

Require enough documentation to reconstruct the actual scientific workflow.

---

# 126. Clinical Research

Where applicable preserve:

- protocol version;
- analysis plan;
- data cut;
- population definitions;
- endpoint derivation;
- censoring;
- safety data processing.

---

# 127. Observational Research

Preserve:

- cohort definition;
- exposure definition;
- outcome definition;
- confounder definitions;
- inclusion/exclusion;
- missing data;
- model specification.

---

# 128. Cross-Sectional Research

Preserve:

- sampling;
- weighting;
- coding;
- outcome construction;
- design effect where relevant.

---

# 129. Longitudinal Research

Preserve:

- time origin;
- waves;
- repeated-measure structure;
- participant linkage;
- censoring;
- attrition decisions.

---

# 130. Diagnostic Research

Preserve:

- index test;
- reference standard;
- threshold;
- blinding;
- analysis set;
- sensitivity/specificity calculations.

---

# 131. Prediction Modeling

Preserve:

- dataset split;
- feature engineering;
- model specification;
- hyperparameters;
- calibration;
- threshold;
- validation.

---

# 132. Validation Studies

Preserve:

- original model;
- validation population;
- preprocessing;
- calibration;
- performance metric definitions.

---

# 133. Measurement Validation

Preserve:

- item set;
- scoring;
- factor model;
- reliability calculation;
- validity analysis;
- modifications.

---

# 134. Experimental Formulation Research

Preserve:

- formulation composition;
- batch;
- preparation procedure;
- instrument settings;
- test conditions;
- replicate structure;
- calculations.

---

# 135. Education Research

Preserve:

- instrument;
- scoring;
- class/school structure;
- intervention implementation;
- outcome timing;
- analysis project.

---

# 136. Social Science Research

Preserve:

- questionnaire version;
- coding;
- weighting;
- sampling;
- construct scoring;
- model specification.

---

# 137. Qualitative Interpretive Studies

Use transparency and auditability rather than demanding identical interpretive outcomes.

---

# 138. Research Data Sharing

Before public release, coordinate with `research-data-governance`.

Do not expose restricted data in the name of reproducibility.

---

# 139. Synthetic Reproducibility Data

Synthetic data can support code testing but do not prove full reproducibility on the real dataset.

---

# 140. Controlled Reproduction

If real data are restricted, classify:

`CONTROLLED_ACCESS_REPRODUCIBLE`

when independent rerun is possible under authorized conditions.

---

# 141. Data Availability Statement Audit

Check whether the manuscript statement matches reality.

Do not allow:

> “Data available upon reasonable request”

when sharing is prohibited or the data no longer exist.

---

# 142. Code Availability Statement Audit

Check whether code actually exists and is usable.

---

# 143. Supplementary Material Audit

Verify that supplements correspond to final analysis versions.

---

# 144. Repository Deposit Audit

Check:

- correct version;
- persistent identifier;
- license;
- README;
- metadata;
- access controls.

---

# 145. Archival Integrity

An archive should preserve:

- identity;
- version;
- relationships;
- access;
- documentation.

---

# 146. Checksum Verification

Use checksums where useful to verify archived file identity.

---

# 147. Reproducibility Passport

Recommended:

```yaml
reproducibility_passport:
  status:
  research_question_traceability:
  protocol_traceability:
  registration_traceability:
  source_data_status:
  analysis_dataset_status:
  transformation_status:
  data_quality_decision_status:
  script_or_workflow_status:
  environment_status:
  parameter_status:
  random_seed_status:
  output_status:
  result_mapping_status:
  rerun_status:
  data_availability:
  code_availability:
  critical_issues:
  unresolved_issues:
  next_action:
```

---

# 148. Reproducibility Audit Matrix

| Component | Available | Traceable | Rerunnable | Verified | Risk |
|---|---|---|---|---|---|
| Source data | | | | | |
| Raw data | | | | | |
| Transformations | | | | | |
| Quality decisions | | | | | |
| Analysis dataset | | | | | |
| Analysis workflow | | | | | |
| Software environment | | | | | |
| Parameters | | | | | |
| Outputs | | | | | |
| Reported results | | | | | |

---

# 149. Audit Decision Logic

```text
Can the analysis dataset be identified?
        │
   ┌────┴────┐
   │         │
  No        Yes
   │         │
BLOCK     Can transformations be reconstructed?
             │
        ┌────┴────┐
        │         │
       No        Yes
        │         │
   PARTIAL/RISK  Can analysis procedure be reconstructed?
                    │
               ┌────┴────┐
               │         │
              No        Yes
               │         │
           PARTIAL/RISK  Can outputs be linked to results?
                           │
                      ┌────┴────┐
                      │         │
                     No        Yes
                      │         │
                    RISK      Is rerun possible?
                                │
                           ┌────┴────┐
                           │         │
                          No        Yes
                           │         │
                     DOCUMENTED    EXECUTION
                    REPRODUCIBILITY TEST
```

---

# 150. Rerun Verification Record

```yaml
rerun_verification:
  rerun_id:
  date:
  operator_role:
  environment:
  dataset_version:
  workflow_version:
  outputs_compared:
  differences:
  material_difference:
  status:
  notes:
```

---

# 151. Result Traceability Record

```yaml
result_traceability:
  result_id:
  manuscript_section:
  text_or_table:
  analysis_id:
  output_id:
  dataset_version:
  script_or_project:
  verification_status:
```

---

# 152. Reproducibility Issue Table

| Issue ID | Component | Severity | Evidence | Consequence | Repair | Status |
|---|---|---|---|---|---|---|

---

# 153. Rerun Comparison Table

| Output | Original | Rerun | Difference | Material? | Explanation |
|---|---|---|---|---|---|

---

# 154. User-Facing Status Example

```text
Reproducibility status: SUBSTANTIALLY REPRODUCIBLE

Strong
- Analysis dataset version is identified.
- Data transformations are scripted.
- Primary analysis syntax is available.
- Tables 1–3 can be linked to saved outputs.

Limitations
- Two sensitivity analyses were performed manually in the GUI and exact option settings were not preserved.
- The original package versions were not locked.
- Figure 2 contains manual cosmetic editing after export.

Material risk
- None identified for the primary conclusions.

Next action
Document the two GUI sensitivity analyses and archive the current software environment before final manuscript release.
```

---

# 155. User-Friendly Behavior

Instead of:

> “Environment provenance failed.”

Prefer:

> “The analysis code is available, but the package versions used for the original run were not recorded. The workflow is still largely reconstructable, although an exact rerun may produce small differences.”

Instead of:

> “Not reproducible.”

Prefer:

> “I can identify the reported result and the analysis dataset, but the transformation from the raw file to that dataset cannot currently be reconstructed. That prevents a full reproducibility claim.”

---

# 156. No Reproducibility Theater

Do not treat:

- GitHub repository;
- DOI;
- code upload;
- supplementary ZIP;
- notebook;
- OSF project

as proof of reproducibility by itself.

Audit whether the materials actually reconstruct the workflow.

---

# 157. No Code Fetish

Code is not mandatory for every research design.

A GUI-based workflow may be sufficiently reproducible if settings and project files are preserved.

A script may be irreproducible if inputs, versions, or execution order are missing.

---

# 158. No Open-Data Absolutism

Do not pressure researchers to violate:

- consent;
- privacy;
- ethics;
- contract;
- regulation

in the name of reproducibility.

---

# 159. No Exactness Fetish

Do not classify harmless floating-point or formatting differences as substantive reproducibility failures.

---

# 160. No Silent Method Substitution

If exact software is unavailable and another implementation is used, label the comparison accurately.

---

# 161. No Fabricated Rerun

Never state:

> “The analysis reproduces exactly”

unless an actual rerun or direct verification occurred.

---

# 162. No Fabricated Code

Do not create replacement code and present it as the original analytical script.

Newly reconstructed code must be labeled as reconstructed.

---

# 163. No Fabricated Data Availability

Never claim data are available when they are not.

---

# 164. No Fabricated Version

If software or package version is unknown, write:

`UNKNOWN`

not a guessed version.

---

# 165. No Publication-Driven Reproducibility Claim

Journal prestige, indexing, quartile, or APC does not establish reproducibility.

---

# 166. Reproducibility Repair Priority

Prioritize:

1. analysis dataset identity;
2. transformation history;
3. primary analysis specification;
4. output mapping;
5. reported-result mapping;
6. environment;
7. auxiliary analyses;
8. cosmetic artifacts.

---

# 167. Critical Repair Sequence

If primary result cannot be reconstructed:

```text
IDENTIFY DATASET
      ↓
RECOVER TRANSFORMATIONS
      ↓
RECOVER ANALYSIS SPECIFICATION
      ↓
REGENERATE OUTPUT
      ↓
COMPARE REPORTED RESULT
```

---

# 168. Reproducibility Freeze

Before submission or archival release, create a reproducibility freeze.

Record:

```yaml
reproducibility_freeze:
  freeze_id:
  date:
  manuscript_version:
  dataset_version:
  analysis_version:
  environment_version:
  output_version:
  archive_location:
```

---

# 169. Manuscript Version Linkage

The reproducibility package should correspond to a specific manuscript version.

Do not assume later edits preserve numerical identity.

---

# 170. Reviewer Revision Reproducibility

Reviewer-driven changes should generate:

- new dataset version if data changed;
- new analysis version if analysis changed;
- new output version;
- updated result mapping.

---

# 171. Reviewer Response Relationship

When reviewers request reanalysis, preserve both:

- original analysis;
- revised analysis.

Do not silently overwrite the original result.

---

# 172. Manuscript Auditor Relationship

`manuscript-auditor` should use reproducibility findings to identify unsupported claims about:

- data availability;
- code availability;
- analysis methods;
- exclusions;
- sensitivity analyses.

---

# 173. Manuscript Writer Relationship

`manuscript-writer` must not invent reproducibility language.

---

# 174. Journal Matcher Relationship

Journal reproducibility requirements may affect repository and supplement preparation.

They do not determine scientific reproducibility status.

---

# 175. Research Roadmap Relationship

`research-roadmap` may treat reproducible data and analytical infrastructure as reusable scientific capability.

---

# 176. Research Resume Relationship

When resuming prior research, use reproducibility status to determine whether old analyses can be safely extended.

---

# 177. Prior Research Auditor Relationship

`prior-research-auditor` may identify claims requiring reproducibility inspection.

---

# 178. Research Router Relationship

`research-router` should route here when the user asks:

- “Can this analysis be reproduced?”
- “Can we rerun the study?”
- “Which file produced this result?”
- “I lost the analysis steps.”
- “Can a reviewer reproduce my tables?”
- “Is my GitHub package sufficient?”
- “Can we reconstruct my old analysis?”
- “Which dataset version was used?”

---

# 179. Research Intake Relationship

At intake capture whether the user has:

- source data;
- analysis data;
- scripts;
- software project;
- outputs;
- manuscript;
- environment information.

Do not perform the full audit during intake.

---

# 180. Research Data Governance Relationship

If source, version, or transformations are unclear, route to:

`research-data-governance`

---

# 181. Data Quality Auditor Relationship

If quality decisions cannot be reconstructed, route to:

`data-quality-auditor`

---

# 182. Analysis Planner Relationship

If the implemented analysis does not match the intended analysis architecture, route to:

`analysis-planner`

for scientific review.

---

# 183. Statistical Method Selector Relationship

If the exact statistical model is unclear or inappropriate, reproducibility alone cannot solve it.

Route to:

`statistical-method-selector`

when required.

---

# 184. Qualitative Analysis Relationship

For qualitative workflows, audit transparency, corpus identity, coding, memo trail, and interpretive development.

---

# 185. Mixed-Method Analysis Relationship

Audit strand-specific reproducibility and integration reproducibility separately.

---

# 186. Meta-Analysis Relationship

Audit search-to-effect-to-model traceability.

---

# 187. Result Interpreter Relationship

If rerun outputs differ materially, route updated results to:

`result-interpreter`

Do not directly rewrite conclusions.

---

# 188. Scientific Discussion Relationship

Material reproducibility limitations should appear in scientific limitations where relevant.

---

# 189. Implication Builder Relationship

Do not strengthen implications when primary analytical results cannot be reconstructed.

---

# 190. Ethics Regulatory Relationship

If reproducibility requires access to restricted data, coordinate with:

`ethics-regulatory-gate`

when available.

---

# 191. Registration Relationship

If rerun reveals deviation from preregistration, preserve that information for:

`registration-preregistration-builder`

when available.

---

# 192. Stop Conditions

Stop and classify as blocked or insufficient when:

- analysis dataset cannot be identified;
- primary source data are irretrievably lost where required for reconstruction;
- transformation history for the primary endpoint is unavailable;
- primary analysis specification is unknown;
- outputs cannot be linked to reported results;
- multiple competing analysis versions exist with no way to identify the reported one;
- major manual decisions are undocumented;
- restricted data access prevents verification and no controlled process is available;
- critical software dependency cannot be recovered and no equivalent verification is possible.

Use statuses:

- `REPRODUCIBILITY_BLOCKED`
- `REPRODUCIBILITY_REQUIRES_REPAIR`
- `REPRODUCIBILITY_PARTIAL`
- `INSUFFICIENT_INFORMATION`
- `RETURN_TO_RESEARCH_DATA_GOVERNANCE`
- `RETURN_TO_DATA_QUALITY_AUDITOR`
- `RETURN_TO_ANALYSIS_PLANNER`

---

# 193. Audit Completion Gate

The audit is complete when:

- primary dataset identity is known;
- primary transformations are traceable;
- major quality decisions are traceable;
- analysis procedure is reconstructable;
- outputs are mapped;
- reported results are mapped;
- reproducibility limitations are explicit;
- rerun status is stated accurately;
- repair actions are documented.

---

# 194. Reproducibility Output Package

Produce, as needed:

1. Reproducibility Status
2. Traceability Matrix
3. Dataset-to-Result Map
4. Script/Workflow Manifest
5. Software Environment Record
6. Rerun Verification
7. Difference Report
8. Reproducibility Issue Register
9. Repair Plan
10. Data Availability Status
11. Code Availability Status
12. Archive Readiness
13. Research Passport Update

---

# 195. Reproducibility Audit Summary Template

```yaml
reproducibility_audit:
  project:
  study_id:
  manuscript_version:
  status:
  data_reproducibility:
  transformation_reproducibility:
  analysis_reproducibility:
  environment_reproducibility:
  output_reproducibility:
  reporting_reproducibility:
  methodological_replicability:
  rerun_status:
  data_availability:
  code_availability:
  critical_issues:
  major_issues:
  unresolved_issues:
  repair_actions:
  next_action:
```

---

# 196. Traceability Matrix Template

| Result | Output | Analysis | Dataset | Transformation | Source | Status |
|---|---|---|---|---|---|---|

---

# 197. Environment Record Template

```yaml
environment:
  operating_system:
  software:
  software_version:
  packages:
  package_versions:
  random_seed:
  locale:
  timezone:
  container_or_lockfile:
  notes:
```

---

# 198. Rerun Summary Template

| Component | Original Available | Rerun Attempted | Match | Material Difference |
|---|---|---|---|---|

---

# 199. Reproducibility Repair Plan Template

| Priority | Issue | Repair Action | Required Source | Feasible | Status |
|---:|---|---|---|---|---|

---

# 200. Research Passport Integration

Recommended:

```yaml
reproducibility:
  status:
  data_status:
  transformation_status:
  quality_decision_status:
  analysis_status:
  environment_status:
  output_status:
  reporting_status:
  rerun_status:
  archive_status:
  unresolved_issues:
  next_action:
```

---

# 201. Compact User-Facing Output

Example:

```text
Reproducibility status: PARTIALLY REPRODUCIBLE

What is traceable
- Analysis dataset v007 is identified.
- Primary regression syntax is available.
- Table 2 maps to saved output regression_primary_01.

What cannot yet be reconstructed
- The transformation that created the final exposure category is only described in analyst notes.
- Package versions used in the original run were not recorded.

Rerun status
- Primary regression rerun: not yet attempted.

Next action
Reconstruct and document the exposure-category transformation, then perform a controlled rerun of the primary model.
```

---

# 202. Final Reproducibility Rule

Never equate availability with reproducibility.

Never equate code with reproducibility.

Never equate exact numerical identity with scientific validity.

Never claim a rerun that did not happen.

The goal is a transparent, reconstructable scientific record.

---

# Success Criterion

`reproducibility-auditor` succeeds when the research record has been evaluated as an explicit traceability chain from research question and protocol through source data, governed transformations, data-quality decisions, analysis-ready dataset, analytical procedure, software environment, parameters, outputs, and reported results; when computational reproducibility, analytical reproducibility, methodological replicability, and conceptual replication are clearly distinguished; when every important reported result can be linked to the dataset and analytical procedure that produced it; when unavailable data, code, versions, manual decisions, stochasticity, proprietary dependencies, restricted access, and historical reconstruction are represented honestly rather than guessed; when rerun claims are made only after actual execution or direct verification; when material and immaterial rerun differences are distinguished; when data and code availability are separated from scientific reproducibility; when reproducibility repair actions are prioritized according to scientific consequence; when unresolved limitations remain visible in manuscript, reviewer-response, archival, and future-research workflows; and when the resulting audit allows another competent researcher to understand exactly what can be reconstructed, what can be rerun, what cannot be reproduced, why, and what evidence or repair would be required to strengthen the reproducibility of the scientific record.
