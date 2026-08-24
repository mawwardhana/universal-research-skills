---
name: phenomenon-evidence-builder
description: Discover, receive, verify, extract, organize, and contextualize authoritative real-world evidence about the phenomenon motivating a research problem, including official statistics, international and national agency data, government datasets, registries, surveillance systems, regulations, policies, institutional reports, credible event reporting, researcher-provided files, URLs, and factual data. Use when a study requires trustworthy evidence about magnitude, trend, burden, distribution, policy context, regulatory environment, service conditions, institutional conditions, or real-world occurrence for research intake, problem formulation, background development, proposal justification, grant writing, manuscript introductions, discussion, implications, or research-roadmap development.
---

# Phenomenon Evidence Builder

## Purpose

`phenomenon-evidence-builder` constructs a defensible evidence base describing the real-world phenomenon that motivates a research problem.

Its central question is:

> What trustworthy factual evidence demonstrates that this phenomenon exists, how large or important it is, how it is changing, who or what is affected, and under what real-world conditions it occurs?

This skill complements scholarly evidence.

It does not replace:

`scopus-literature-search`

because the two evidence streams answer different questions.

Conceptually:

```text
PHENOMENON EVIDENCE
"What is actually happening?"
        ↓
Authority-first evidence

versus

SCHOLARLY EVIDENCE
"What does science currently know about it?"
        ↓
Scopus-first scholarly evidence
```

Both may be required to construct a scientifically defensible research problem.

---

# Core Principle

Use:

> Real-world factual claims should be supported by the most authoritative original source reasonably available.

Phenomenon evidence should establish:

- existence;
- magnitude;
- prevalence;
- incidence;
- distribution;
- trend;
- burden;
- consequences;
- service conditions;
- institutional conditions;
- policy context;
- regulatory context;
- practical urgency.

It should not be used to manufacture:

- research gaps;
- scientific novelty;
- causal mechanisms;
- theoretical propositions.

---

# Evidence Architecture

Maintain two complementary evidence streams:

```text
              RESEARCH PROBLEM
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
PHENOMENON EVIDENCE     SCHOLARLY EVIDENCE
Authority-first            Scopus-first
          │                     │
          └──────────┬──────────┘
                     ▼
              SCIENTIFIC PROBLEM
                     ↓
                State of Art
                     ↓
              Validated Gap
                     ↓
              Audited Novelty
                     ↓
              Research Question
```

Do not collapse the two streams into one evidence standard.

---

# Authority-First Policy

For phenomenon evidence, prefer:

`AUTHORITATIVE_SOURCE_FIRST`

This differs from:

`SCOPUS_FIRST`

which applies primarily to scholarly scientific evidence.

Examples:

For national population statistics:

prefer the official national statistical agency.

For disease surveillance:

prefer the responsible health authority or authoritative surveillance system.

For international health statistics:

prefer authoritative international organizations or original national producers.

For regulations:

prefer official legislation or government repositories.

For institutional performance:

prefer the responsible institution's original documented records when appropriate.

Do not search Scopus for information that should properly come from an official statistical or regulatory source.

---

# Primary Evidence Roles

Phenomenon evidence may support:

- `PHENOMENON_EXISTENCE`
- `MAGNITUDE`
- `PREVALENCE`
- `INCIDENCE`
- `TREND`
- `BURDEN`
- `DISTRIBUTION`
- `AFFECTED_POPULATION`
- `GEOGRAPHIC_PATTERN`
- `SERVICE_CONDITION`
- `INSTITUTIONAL_CONDITION`
- `ECONOMIC_CONTEXT`
- `EDUCATION_CONTEXT`
- `ENVIRONMENTAL_CONTEXT`
- `POLICY_CONTEXT`
- `REGULATORY_CONTEXT`
- `PROGRAM_PERFORMANCE`
- `CURRENT_EVENT`
- `BACKGROUND_SIGNIFICANCE`
- `PROBLEM_JUSTIFICATION`
- `DISCUSSION_CONTEXT`
- `IMPLICATION_CONTEXT`
- `ROADMAP_RELEVANCE`

---

# Evidence That This Skill Does Not Establish by Itself

Phenomenon evidence does not by itself establish:

- `STATE_OF_THE_ART`
- `SCIENTIFIC_MECHANISM`
- `THEORETICAL_PROPOSITION`
- `CAUSAL_EFFECT`
- `VALIDATED_RESEARCH_GAP`
- `AUDITED_NOVELTY`

These require scholarly and scientific evidence.

---

# Supported Input Modes

This skill supports four main modes.

Use:

- `SEARCH`
- `FILE_UPLOAD`
- `URL_INPUT`
- `USER_PROVIDED_DATA`

Multiple modes may be combined.

---

# 1. SEARCH Mode

Use when the researcher asks the framework to find real-world evidence.

Possible requests include:

- official statistics;
- prevalence;
- incidence;
- demographic indicators;
- education statistics;
- health-system indicators;
- economic indicators;
- environmental indicators;
- policy documents;
- regulations;
- program reports;
- institutional statistics.

Prefer original authoritative producers.

---

# 2. FILE_UPLOAD Mode

Use when the researcher provides:

- PDF;
- spreadsheet;
- CSV;
- report;
- regulation;
- policy;
- institutional document;
- statistical table;
- dashboard export;
- registry extract.

Treat uploaded materials as candidate evidence.

Do not assume the material is authoritative merely because the researcher supplied it.

Verify:

- issuing organization;
- source type;
- date;
- population;
- geography;
- indicator definition;
- reference period;
- data status.

---

# 3. URL_INPUT Mode

Use when the researcher provides:

- official webpage;
- dashboard URL;
- data portal;
- policy webpage;
- regulation URL;
- institutional page;
- news URL.

Determine whether the URL is:

- original source;
- secondary source;
- aggregator;
- commentary;
- mirror.

Prefer original source recovery where possible.

---

# 4. USER_PROVIDED_DATA Mode

Use when the researcher manually supplies factual information.

Example:

> The prevalence is 32%.

If documentation is absent, classify:

`USER_PROVIDED_UNVERIFIED_FACT`

Do not discard it automatically.

Preserve it as a candidate fact while requesting or searching for:

- source documentation;
- original report;
- official dataset;
- URL;
- authoritative confirmation.

---

# Source Hierarchy

Use a context-sensitive hierarchy.

Preferred categories may include:

1. original official statistical source;
2. original international or national agency source;
3. official government dataset;
4. official registry or surveillance source;
5. official regulation or legislation repository;
6. original institutional report;
7. authoritative research infrastructure;
8. credible secondary reporting;
9. user-provided undocumented fact.

The hierarchy is not absolute.

The responsible original producer is usually preferred.

---

# International Organization Sources

Examples may include authoritative international bodies responsible for:

- health;
- education;
- population;
- labor;
- economics;
- development;
- environment;
- food;
- children;
- science;
- trade.

Evaluate:

- mandate;
- data provenance;
- methodology;
- update cycle;
- whether the organization is the original producer or aggregator.

Do not assume international automatically means superior to original national data.

---

# National Statistical Sources

National statistics are often preferred for:

- population;
- employment;
- education;
- economic conditions;
- household indicators;
- regional indicators;
- demographic characteristics.

Check:

- indicator definition;
- survey design;
- geographic coverage;
- reference year;
- revision status.

---

# Government Agency Sources

Government agencies may provide authoritative evidence for:

- health;
- education;
- environment;
- social services;
- licensing;
- regulation;
- disease surveillance;
- infrastructure;
- program performance.

Verify the responsible agency and publication status.

---

# Registry Evidence

Registries may support:

- disease occurrence;
- treatment patterns;
- service utilization;
- mortality;
- adverse events;
- professional registration;
- institutional participation.

Check:

- registry coverage;
- reporting completeness;
- inclusion criteria;
- reporting delays;
- denominator definition.

---

# Surveillance Evidence

Surveillance data may be:

- continuous;
- sentinel;
- periodic;
- passive;
- active.

Do not interpret surveillance estimates without understanding coverage.

---

# Institutional Evidence

Institutional records may be useful when the research problem concerns:

- one university;
- one hospital;
- one clinic;
- one company;
- one school;
- one laboratory;
- one program.

Classify:

`INSTITUTIONAL_EVIDENCE`

Do not generalize institutional findings automatically to larger populations.

---

# Regulation Evidence

Regulations may establish:

- legal requirement;
- formal authority;
- prohibited activity;
- mandatory standard;
- implementation responsibility;
- compliance obligation.

Regulation evidence supports legal or policy claims.

It does not prove:

- scientific effectiveness;
- causal impact;
- implementation success;
- behavioral response.

---

# Policy Evidence

Policy documents may establish:

- official goals;
- strategic priorities;
- implementation plans;
- targets;
- policy direction.

Distinguish:

`POLICY_INTENT`

from:

`OBSERVED_REALITY`

A target is not evidence that the target has been achieved.

---

# Program Reports

Program reports may support:

- reach;
- participation;
- output;
- implementation status;
- service coverage.

Check whether the report describes:

- target;
- output;
- outcome;
- impact.

Do not confuse these levels.

---

# News Evidence

News may be useful for:

- discovering a current event;
- identifying a newly reported problem;
- locating an original source;
- identifying relevant organizations.

News should normally be treated as:

`SECONDARY_EVENT_EVIDENCE`

When a news article states:

> According to Organization X, 40%...

attempt:

`ORIGINAL_SOURCE_RECOVERY`

before using the news article as the primary source.

---

# Original Source Recovery

Use this workflow:

```text
Secondary Claim
      ↓
Identify Claimed Original Producer
      ↓
Locate Original Dataset / Report / Regulation
      ↓
Verify Indicator
      ↓
Verify Period
      ↓
Verify Population
      ↓
Use Original Source
```

If original source recovery fails:

retain the secondary source with lower confidence.

---

# Source Provenance

For every important factual claim, establish:

- who produced the information;
- where the data originated;
- who published it;
- whether the publisher is the producer or aggregator;
- whether revisions exist.

Use:

- `ORIGINAL_SOURCE`
- `AUTHORIZED_REPUBLISHER`
- `SECONDARY_SOURCE`
- `AGGREGATOR`
- `PROVENANCE_UNCLEAR`

---

# Publication Date vs Reference Period

Always distinguish:

`PUBLICATION_DATE`

from:

`REFERENCE_PERIOD`

Example:

A report published in 2026 may describe data from 2024.

Do not call the statistic:

> 2026 data

unless 2026 is actually the reference period.

---

# Data Recency

Assess recency relative to the phenomenon.

Use:

- `CURRENT`
- `RECENT`
- `OLDER_BUT_RELEVANT`
- `HISTORICAL`
- `OUTDATED_FOR_CLAIM`
- `RECENCY_UNKNOWN`

The newest publication is not always the newest observation.

---

# Trend Evidence

A trend requires multiple comparable observations.

Do not infer a trend from:

- one year;
- two incomparable datasets;
- changing indicator definitions;
- different populations.

Check comparability before stating:

- increased;
- decreased;
- stable;
- worsening;
- improving.

---

# Geography

Record geographic level accurately.

Possible levels:

- global;
- regional;
- national;
- provincial;
- state;
- district;
- city;
- institution;
- facility.

Do not generalize local data to national conditions without justification.

---

# Population

Record:

- target population;
- inclusion criteria;
- age;
- sex where relevant;
- disease status;
- occupation;
- education level;
- institutional status.

Do not combine population estimates with incompatible denominators.

---

# Unit

Always record units.

Examples:

- persons;
- percent;
- cases per 100,000;
- rate per 1,000;
- currency;
- index score;
- kilograms;
- tonnes;
- enrollment ratio.

Do not compare values with incompatible units.

---

# Numerator and Denominator

For rates and proportions, identify where possible:

- numerator;
- denominator.

A percentage without denominator context may be misleading.

---

# Indicator Definition

Record the exact conceptual definition of the indicator.

Example:

`unemployment rate`

may differ from:

`percentage without employment`

Do not merge similar labels without checking definitions.

---

# Observed vs Estimated vs Projected

Classify data as:

- `OBSERVED`
- `ESTIMATED`
- `MODELED`
- `PROJECTED`
- `TARGET`
- `UNKNOWN`

Do not present projections as observed facts.

---

# Estimate Uncertainty

When available, preserve:

- confidence interval;
- credible interval;
- standard error;
- uncertainty range;
- model uncertainty.

Do not imply false precision.

---

# Revised Data

Official statistics may be revised.

Use:

- `PRELIMINARY`
- `PROVISIONAL`
- `FINAL`
- `REVISED`
- `STATUS_UNKNOWN`

Prefer final or revised values where appropriate.

---

# Dynamic Dashboards

For dynamic dashboards record:

- dashboard name;
- producer;
- indicator;
- filter settings;
- geography;
- period;
- access date.

Use:

`DYNAMIC_SOURCE`

when values may change after access.

---

# API Data

When data come from an API, record:

- provider;
- endpoint or dataset;
- indicator;
- query parameters;
- retrieval date;
- version where available.

Preserve reproducibility.

---

# Dataset Metadata

For datasets identify where possible:

```yaml
dataset:
  title:
  producer:
  version:
  release_date:
  reference_period:
  geography:
  population:
  unit:
  indicator_definition:
  methodology:
  access_date:
```

---

# Fact-Level Evidence Schema

Recommended internal schema:

```yaml
phenomenon_fact:
  statement:
  indicator:
  value:
  unit:
  population:
  geography:
  reference_period:
  publication_date:
  source_title:
  issuing_organization:
  source_type:
  authority_level:
  original_source_status:
  source_url:
  access_date:
  evidence_role:
  data_status:
  verification_status:
  notes:
```

Do not invent unavailable fields.

---

# Verification Status

Use:

- `VERIFIED`
- `PARTIALLY_VERIFIED`
- `UNVERIFIED`
- `CONFLICTING`
- `SOURCE_NOT_RECOVERED`

---

# Authority Level

Use context-sensitive labels such as:

- `PRIMARY_AUTHORITY`
- `AUTHORITATIVE_AGENCY`
- `OFFICIAL_INSTITUTION`
- `CREDIBLE_SECONDARY`
- `USER_PROVIDED`
- `AUTHORITY_UNCLEAR`

Authority must be judged relative to the claim.

---

# Verification Procedure

For important phenomenon claims:

```text
Claim
  ↓
Locate Source
  ↓
Identify Producer
  ↓
Verify Indicator
  ↓
Verify Population
  ↓
Verify Geography
  ↓
Verify Reference Period
  ↓
Verify Value
  ↓
Verify Data Status
  ↓
Record Provenance
```

---

# Claim-to-Source Integrity

Maintain:

```text
Real-world claim
      ↓
Phenomenon fact
      ↓
Original authoritative source
```

Do not use a source merely because it discusses the same topic.

The source must support the specific claim.

---

# Exact Value Guard

If a source states:

`31.7%`

do not casually rewrite it as:

`about one-third`

when exact precision matters.

Conversely, avoid false precision when source uncertainty is high.

---

# Relative Change Guard

Distinguish:

`percentage-point change`

from:

`percent change`

Example:

20% to 25% equals:

5 percentage points

but:

25% relative increase.

Do not confuse them.

---

# Absolute vs Relative Burden

Where relevant, distinguish:

- number of affected persons;
- proportion affected;
- population rate.

Large percentages in small populations may not represent large absolute burden.

---

# Per-Capita Guard

Raw counts may reflect population size.

Use rates when the research question concerns comparative burden and valid denominators exist.

---

# Missing Data

If official data are incomplete:

record:

`DATA_COVERAGE_LIMITATION`

Do not fill missing observations by assumption.

---

# Reporting Delay

Administrative and surveillance systems may have reporting lags.

Record:

`REPORTING_LAG`

when relevant.

Do not assume the latest available observation represents the current moment perfectly.

---

# Methodology Change

If indicator methodology changes across years:

flag:

`SERIES_BREAK`

Do not present a continuous trend without qualification.

---

# Geographic Boundary Change

If administrative boundaries change:

flag:

`GEOGRAPHIC_COMPARABILITY_LIMITATION`

Do not compare areas as though boundaries were unchanged.

---

# Population Definition Change

If denominator or inclusion criteria change:

flag:

`POPULATION_COMPARABILITY_LIMITATION`

---

# Conflict Between Official Sources

Authoritative sources may disagree.

Do not silently choose the preferred number.

Use:

`OFFICIAL_SOURCE_CONFLICT`

Investigate:

- indicator definition;
- reference period;
- methodology;
- population;
- revision;
- geographic scope;
- modeled vs observed status.

---

# Conflict Resolution

Use:

```text
Source A ≠ Source B
      ↓
Compare definitions
      ↓
Compare period
      ↓
Compare geography
      ↓
Compare population
      ↓
Compare methodology
      ↓
Compare data status
      ↓
Explain remaining difference
```

Do not average conflicting statistics arbitrarily.

---

# Source Independence

Several webpages may reproduce the same original data.

Do not count them as independent evidence.

Trace shared provenance.

---

# Duplicate Evidence Guard

Use:

`DUPLICATE_SOURCE_CHAIN`

when multiple secondary sources derive from one original source.

---

# Event Evidence

For current events, distinguish:

- event occurrence;
- reported interpretation;
- official response;
- verified consequences.

Do not infer long-term research significance from one event without broader evidence.

---

# Regulatory Status

For laws or regulations, determine:

- enacted;
- issued;
- amended;
- superseded;
- revoked;
- draft;
- effective;
- implementation pending.

Use:

- `ACTIVE`
- `SUPERSEDED`
- `REVOKED`
- `DRAFT`
- `STATUS_UNCLEAR`

Do not cite superseded regulation as current law without qualification.

---

# Policy Target vs Observed Outcome

Represent separately:

```text
Policy Target
"What should happen?"

Observed Data
"What actually happened?"
```

A discrepancy may help establish a real-world problem.

But it does not automatically prove a scientific gap.

---

# Institutional Target vs Performance

Similarly distinguish:

- institutional target;
- measured achievement;
- implementation evidence.

Do not treat strategic plans as evidence of actual performance.

---

# Baseline Evidence

Identify baseline when the study seeks to evaluate change.

A baseline should be:

- temporally appropriate;
- definitionally comparable;
- geographically comparable.

---

# Comparator Evidence

When comparing places or populations, verify:

- same indicator;
- same period;
- same measurement method;
- compatible denominators.

Do not compare incompatible official statistics.

---

# International Comparisons

International data may involve harmonized definitions.

Check:

- whether national definitions were harmonized;
- model-based estimates;
- standardization methods.

Do not assume raw national data are directly comparable.

---

# Real-World Burden

Burden may include:

- health burden;
- mortality;
- morbidity;
- educational loss;
- economic cost;
- social impact;
- environmental damage;
- service pressure;
- organizational consequences.

Use evidence appropriate to the burden type.

---

# Consequence Evidence

Distinguish:

`OBSERVED_CONSEQUENCE`

from:

`POTENTIAL_CONSEQUENCE`

Do not use speculative consequence language as established fact.

---

# Background Construction

When building a research background, use a logical progression:

```text
REAL-WORLD PHENOMENON
      ↓
MAGNITUDE / TREND
      ↓
CONSEQUENCE / BURDEN
      ↓
SCIENTIFIC KNOWLEDGE
      ↓
STATE OF THE ART
      ↓
VALIDATED GAP
      ↓
AUDITED NOVELTY
      ↓
RESEARCH QUESTION / OBJECTIVE
```

Phenomenon evidence should strengthen the beginning of this chain.

It should not substitute for the scholarly stages.

---

# Background Readiness

Assess whether the evidence base supports:

1. phenomenon existence;
2. magnitude;
3. trend where relevant;
4. affected population;
5. geographic context;
6. consequence or burden;
7. policy or regulatory context where relevant.

Use:

- `BACKGROUND_PHENOMENON_READY`
- `BACKGROUND_PHENOMENON_PARTIAL`
- `BACKGROUND_PHENOMENON_NOT_READY`
- `NOT_APPLICABLE`

---

# Background Claim Guard

Avoid unsupported claims such as:

> This problem is increasing rapidly.

unless a comparable time series supports it.

Avoid:

> This is a major national problem.

unless magnitude or burden supports that characterization.

---

# Urgency Guard

Do not exaggerate urgency.

Use terms such as:

- substantial;
- increasing;
- persistent;
- widespread;
- concentrated;
- policy-relevant;

only when evidence supports them.

---

# Problem Significance

Phenomenon evidence may establish:

> Why should anyone care about this problem?

Scholarly evidence must still establish:

> What is scientifically unresolved?

These are different questions.

---

# Phenomenon vs Scientific Problem

Maintain:

```text
REAL-WORLD PROBLEM
"What is happening?"

SCIENTIFIC PROBLEM
"What does current knowledge fail to explain,
validate, predict, or resolve?"
```

A strong real-world problem does not automatically equal a research gap.

---

# Research Gap Boundary

Do not state:

> Because prevalence is high, there is a research gap.

A research gap must be established by scholarly evidence.

Use:

`gap-validator`

for scientific gap claims.

---

# Novelty Boundary

Do not state:

> Because no local government report exists, the study is novel.

Novelty must be established relative to scientific literature and closest competing studies.

Use:

`novelty-auditor`

for novelty claims.

---

# Theory Boundary

Official statistics cannot establish theoretical mechanisms.

Route theoretical questions to:

`theoretical-framework`

and scholarly evidence workflows.

---

# Hypothesis Boundary

Phenomenon evidence may motivate a hypothesis.

It does not automatically determine hypothesis direction.

Hypothesis direction requires:

- theory;
- mechanism;
- empirical evidence.

Use:

`hypothesis-builder`

---

# Conceptual Framework Boundary

Phenomenon evidence may inform contextual factors.

It should not generate arbitrary arrows between constructs.

Use:

`conceptual-framework`

for scientific relationship construction.

---

# Methodology Boundary

Phenomenon evidence may help identify:

- target population;
- geography;
- institutional setting;
- practical constraints.

It should not dictate a statistical method.

Use:

`methodology-architect`

and:

`analysis-planner`

downstream.

---

# Discussion Use

Phenomenon evidence may contextualize findings.

Examples:

- national burden;
- service conditions;
- policy relevance;
- institutional context.

Do not use contextual evidence to overgeneralize findings beyond the study design.

---

# Implication Use

Phenomenon evidence may strengthen:

- policy implications;
- practice implications;
- institutional implications;
- implementation implications.

Implications must remain proportional to the actual study evidence.

---

# Roadmap Use

Phenomenon evidence may help prioritize future research according to:

- burden;
- trend;
- policy relevance;
- underserved population;
- service gap;
- institutional need.

But scientific sequencing should still consider:

- evidence maturity;
- validated gap;
- novelty;
- feasibility.

---

# Grant Use

For grant applications, phenomenon evidence may support:

- significance;
- urgency;
- population burden;
- national relevance;
- policy alignment;
- societal impact.

Do not substitute policy relevance for scientific contribution.

---

# Proposal Use

A proposal background may integrate:

```text
Authoritative phenomenon evidence
+
Verified scholarly evidence
+
Validated scientific gap
+
Audited novelty
```

This creates stronger justification than either evidence stream alone.

---

# User-Provided File Handling

When the researcher uploads a document:

1. identify document type;
2. identify producer;
3. determine whether it is original;
4. identify publication date;
5. identify reference period;
6. extract relevant factual claims;
7. verify definitions;
8. record limitations.

Do not summarize the entire document unless requested.

Extract only evidence relevant to the research problem.

---

# Spreadsheet Handling

For spreadsheets:

identify:

- sheet;
- variable;
- unit;
- period;
- geography;
- population;
- missing values;
- data dictionary;
- source notes.

Do not interpret column labels without context when ambiguous.

---

# PDF Report Handling

For reports:

identify:

- executive summary;
- methods;
- indicator definitions;
- tables;
- appendices;
- revisions.

Do not rely only on promotional summaries when methodological details are available.

---

# Dashboard Handling

For dashboards:

record:

- filters;
- date;
- geography;
- indicator;
- access date.

Take care with dynamically changing values.

---

# URL Handling

For user-provided URLs:

determine:

- official status;
- producer;
- page type;
- original-source status;
- publication date;
- data period.

Do not assume a `.gov` or institutional domain automatically validates every claim.

---

# Credible News Handling

When news is the only available evidence:

record:

`SECONDARY_SOURCE_ONLY`

and lower confidence.

If original-source recovery later succeeds:

replace the primary support with the original source while retaining the news only when useful for event context.

---

# Current Event Guard

Fast-changing events may require:

`CURRENT_EVENT_STATUS`

with access date and time-sensitive qualification.

Do not present unstable counts as permanent facts.

---

# Data Extraction Rule

Extract only:

- directly supported values;
- directly supported definitions;
- clearly stated periods;
- clearly stated geographic scopes.

Do not infer missing data silently.

---

# Derived Calculations

If calculation is required:

label:

`DERIVED_VALUE`

and preserve:

- source inputs;
- formula;
- result.

Do not present derived values as directly reported statistics.

---

# Transformation Guard

If data are:

- aggregated;
- normalized;
- converted;
- standardized;

document the transformation.

---

# Evidence Table

When useful:

| Claim | Value | Unit | Population | Geography | Period | Source | Status |
|---|---:|---|---|---|---|---|---|

Do not omit reference periods.

---

# Source Audit Table

When useful:

| Source | Producer | Source Type | Original? | Authority | Period | Verification |
|---|---|---|---|---|---|---|

---

# Conflict Table

When official sources conflict:

| Source | Value | Definition | Period | Population | Method | Explanation |
|---|---:|---|---|---|---|---|

---

# Phenomenon Evidence Synthesis

After extraction, synthesize evidence into:

## Phenomenon
[...]

## Magnitude
[...]

## Trend
[...]

## Population
[...]

## Geography
[...]

## Burden
[...]

## Policy or Regulatory Context
[...]

## Evidence Limitations
[...]

## Remaining Evidence Need
[...]

Do not overstate certainty.

---

# Evidence Confidence

Classify:

- `HIGH_CONFIDENCE`
- `MODERATE_CONFIDENCE`
- `LOW_CONFIDENCE`
- `CONFLICTING`
- `INSUFFICIENT`

Confidence may depend on:

- authority;
- provenance;
- methodological transparency;
- recency;
- coverage;
- consistency.

---

# Phenomenon Evidence Status

Use:

- `PHENOMENON_EVIDENCE_READY`
- `PHENOMENON_EVIDENCE_PARTIAL`
- `PHENOMENON_EVIDENCE_WEAK`
- `PHENOMENON_EVIDENCE_CONFLICTING`
- `PHENOMENON_EVIDENCE_NOT_REQUIRED`

---

# Data Quality Dimensions

Where relevant assess:

- completeness;
- accuracy;
- timeliness;
- consistency;
- representativeness;
- transparency;
- comparability.

Do not assign false precision to quality judgments.

---

# Representativeness Guard

Administrative records may represent:

> recorded cases

not:

> all cases in the population.

State the denominator and coverage clearly.

---

# Selection Bias Awareness

Institutional or service data may reflect:

- service users;
- enrolled participants;
- reported cases.

Do not generalize automatically to non-users.

---

# Underreporting Awareness

Some phenomena may be underreported.

If authoritative documentation recognizes underreporting:

preserve that caveat.

Do not estimate undocumented underreporting independently.

---

# Modeled Estimates

International organizations may publish modeled estimates.

Use them when scientifically appropriate.

Label clearly:

`MODELED_ESTIMATE`

Do not present them as direct observation.

---

# Projection Evidence

For projections:

record:

- projection horizon;
- assumptions;
- model source.

Use:

`PROJECTED_VALUE`

Do not write:

> will reach

when uncertainty is substantial.

Prefer:

> is projected to reach

---

# Historical Evidence

Historical statistics may be useful for:

- long-term trend;
- policy evolution;
- baseline comparison.

Do not use historical data as current magnitude.

---

# Regulatory Timeline

When regulation changes over time:

```text
Original Regulation
      ↓
Amendment
      ↓
Current Active Regulation
```

Use current status when discussing present requirements.

---

# Policy Evolution

Policy history may explain institutional or service changes.

Do not assume policy publication caused observed outcomes without causal evidence.

---

# Source Citation Integrity

A phenomenon claim should never be supported by a source that merely mentions the organization or topic.

Verify direct support.

---

# Reference Integrity

When publication metadata are required, integrate with:

`reference-integrity-guard`

where relevant.

Do not fabricate:

- report title;
- publication year;
- URL;
- organization;
- document number.

---

# Source Verification

Use:

`source-verification`

when verification is needed for:

- report identity;
- publisher;
- DOI for scholarly reports;
- document metadata;
- citation integrity.

Phenomenon-source authority assessment remains distinct from scholarly indexing verification.

---

# Search Escalation

If an official statistic is difficult to find:

```text
Official Producer Search
      ↓
Official Data Portal
      ↓
Official Report
      ↓
Authorized International Aggregator
      ↓
Credible Secondary Source
```

Do not immediately settle for secondary reporting.

---

# Search Failure

If authoritative evidence cannot be found:

state:

`AUTHORITATIVE_EVIDENCE_NOT_FOUND`

Do not invent a statistic.

---

# Evidence Absence

Absence of official data may itself be relevant.

But distinguish:

> no data located

from:

> no data exist.

Use:

`DATA_NOT_LOCATED`

unless absence has been verified.

---

# Background Evidence Minimum

For empirical research involving an important real-world problem, a strong background often benefits from evidence for:

1. existence;
2. magnitude;
3. trend or persistence;
4. consequence;
5. target-context relevance.

Not every study requires all five.

---

# Minimal Output

For a simple request, provide:

## Key Phenomenon Fact
[...]

## Source
[...]

## Reference Period
[...]

## Context
[...]

## Verification Status
[...]

Avoid unnecessary complexity.

---

# Comprehensive Output

When full phenomenon-evidence development is requested, use:

## A. Research Problem Context
[...]

## B. Phenomenon Definition
[...]

## C. Phenomenon Existence Evidence
[...]

## D. Magnitude
[...]

## E. Trend
[...]

## F. Population
[...]

## G. Geography
[...]

## H. Distribution
[...]

## I. Burden or Consequence
[...]

## J. Service or Institutional Conditions
[...]

## K. Policy Context
[...]

## L. Regulatory Context
[...]

## M. Source Hierarchy
[...]

## N. Original Source Recovery
[...]

## O. Data Quality
[...]

## P. Conflicting Evidence
[...]

## Q. Evidence Limitations
[...]

## R. Background Readiness
[...]

## S. Phenomenon Evidence Status
[...]

## T. Recommended Next Step
[...]

---

# Research Passport Update

When supported, update:

```yaml
phenomenon_context:
  phenomenon:
  population:
  geography:
  reference_period:
  evidence_need:
  evidence_status:
  magnitude:
  trend:
  burden:
  affected_population:
  policy_context:
  regulatory_context:
  institutional_context:
  official_statistics_available:
  dataset_available:
  regulation_or_policy_available:
  institutional_data_available:
  original_sources:
  secondary_sources:
  user_provided_urls:
  user_provided_files:
  unverified_facts:
  conflicts:
  limitations:
  verification_required:
  background_readiness:
  phenomenon_evidence_next_stage:
```

Unknown fields remain unknown.

---

# Relationship with Research Intake

`research-intake` identifies whether real-world factual evidence is:

- available;
- partial;
- absent;
- required;
- useful;
- not central.

When evidence is required or useful:

route to:

`phenomenon-evidence-builder`

Do not ask researchers to repeat files or URLs already supplied.

---

# Relationship with Research Router

`research-router` should route here when the user needs evidence about:

> What is happening in the real world?

Use this skill for:

- official statistics;
- reports;
- policies;
- regulations;
- datasets;
- real-world events;
- institutional facts.

Use:

`scopus-literature-search`

when the question is:

> What does scientific research know about it?

---

# Relationship with Scopus Literature Search

Maintain:

```text
phenomenon-evidence-builder
Authority-first

parallel with

scopus-literature-search
Scopus-first
```

The two workflows may operate simultaneously.

Neither replaces the other.

---

# Relationship with Evidence Synthesis

Phenomenon evidence may later complement:

`evidence-synthesis`

but should remain visibly distinct from scholarly evidence.

Do not merge official statistics into scientific-effect synthesis as though they were equivalent study designs.

---

# Relationship with State of the Art

`sota-builder`

is built primarily from scholarly evidence.

Phenomenon evidence may provide context.

It should not determine the State of the Art by itself.

---

# Relationship with Gap Validator

`gap-validator`

must evaluate scientific uncertainty using scholarly evidence.

A serious real-world problem does not prove a research gap.

---

# Relationship with Novelty Auditor

`novelty-auditor`

determines whether the proposed scientific contribution is genuinely distinct.

Phenomenon magnitude does not prove novelty.

---

# Relationship with Research Question Builder

Phenomenon evidence may help define:

- population;
- geography;
- practical context;
- policy relevance;
- urgency.

But:

`research-question-builder`

must still derive the RQ from validated scientific uncertainty.

---

# Relationship with Theoretical Framework

Official or institutional evidence may demonstrate that a phenomenon occurs.

It does not explain why it occurs scientifically.

Use:

`theoretical-framework`

for explanatory theory or mechanisms.

---

# Relationship with Conceptual Framework

Phenomenon evidence may inform:

- context;
- population boundary;
- environmental conditions;
- regulatory setting.

It should not generate unsupported conceptual relationships.

---

# Relationship with Methodology Architect

Phenomenon evidence may inform:

- study population;
- setting;
- sampling frame;
- feasibility;
- policy context.

Detailed design remains the responsibility of:

`methodology-architect`

---

# Relationship with Scientific Discussion

After results are available, phenomenon evidence may help contextualize:

- societal relevance;
- policy relevance;
- institutional implications;
- real-world magnitude.

Do not allow contextual evidence to inflate causal conclusions.

---

# Relationship with Implication Builder

Use verified phenomenon evidence to help assess:

- practical significance;
- implementation relevance;
- policy relevance;
- population impact.

Implications must still remain proportional to the actual results.

---

# Relationship with Manuscript Writer

For introductions, phenomenon evidence may support early background paragraphs.

Recommended logic:

```text
Phenomenon
↓
Magnitude
↓
Burden
↓
Scientific Knowledge
↓
Gap
↓
Novelty
↓
Objective
```

Do not overload the introduction with statistics unrelated to the RQ.

---

# User-Friendly Behavior

Prefer:

> The latest official dataset reports 18.4% for the target population in 2025. The report itself was published in 2026, so I would describe this as a 2025 estimate published in 2026, not as 2026 prevalence.

Or:

> The news article cites the Ministry as the source. I would use the original ministry report for the statistic and retain the news only as secondary context.

Or:

> This regulation establishes the legal requirement, but it cannot show whether the policy is effective. Effectiveness requires empirical research evidence.

---

# Avoid These Behaviors

Do not:

- invent official statistics;
- treat news as the preferred source when an original source exists;
- call publication year the data year automatically;
- present projections as observations;
- confuse policy targets with actual outcomes;
- use regulations as evidence of causal effectiveness;
- treat a high burden as proof of a research gap;
- treat absence of local statistics as scientific novelty;
- silently resolve conflicting official data;
- combine incompatible indicators;
- ignore population definitions;
- ignore geographic boundaries;
- ignore measurement-unit differences;
- generalize institutional data to national populations;
- use Scopus as the primary source for official statistics when an authoritative producer exists;
- optimize factual evidence for dramatic storytelling;
- fabricate URLs, report titles, or publication metadata.

---

# Stop Conditions

Do not classify phenomenon evidence as ready when:

- critical factual claims remain unsupported;
- original-source provenance is unclear for major claims;
- population is ambiguous;
- geography is ambiguous;
- reference period is unknown and materially important;
- values from conflicting official sources remain unexplained;
- projections are being presented as observations;
- policy targets are being presented as achieved outcomes;
- secondary reporting is being used despite readily recoverable original evidence.

Use:

- `PHENOMENON_EVIDENCE_REQUIRES_REVISION`
- `AUTHORITATIVE_EVIDENCE_NOT_FOUND`
- `PHENOMENON_EVIDENCE_PARTIAL`

when appropriate.

---

# Success Criterion

`phenomenon-evidence-builder` succeeds when real-world claims about the research problem are supported by appropriately authoritative and preferably original sources, factual values are preserved with their correct indicators, units, populations, geographies, reference periods, data status, and provenance, secondary reporting is traced back to original evidence where possible, conflicting or limited evidence is made explicit, and phenomenon evidence is used to establish real-world significance without being confused with scholarly evidence for theory, mechanism, research-gap validation, or novelty.