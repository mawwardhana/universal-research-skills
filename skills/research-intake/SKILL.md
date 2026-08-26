---

name: research-intake
description: Establish a researcher's starting point, goals, available materials, constraints, expertise, publication ambitions, and current manuscript or peer-review status before routing begins. Use when the user wants to start research, has only a broad interest or practical problem, is unsure what to study, when the current research stage cannot yet be determined reliably, or when existing manuscript, reviewer, or editor materials must be classified before selecting the next workflow.
---

# Research Intake

## Purpose

`research-intake` establishes the minimum research context needed to guide a researcher toward a scientifically defensible next step.

It is designed for users ranging from beginners to experienced researchers.

The intake process must be:

* brief;
* adaptive;
* user-friendly;
* discipline-agnostic;
* evidence-aware;
* publication-aware.

Do not turn research intake into a long questionnaire.

Ask only for information that materially changes the research pathway.

---

# Primary Goals

Determine:

1. what the researcher wants to accomplish;
2. whether the research is new or continues previous work;
3. the research domain or area of interest;
4. what problem, phenomenon, or opportunity motivates the research;
5. what materials or evidence already exist;
6. what resources and constraints affect feasibility;
7. what type of scientific output is desired;
8. whether publication strategy is already an important constraint;
9. what should happen next.

---

# Intake Principle

Use the following rule:

> Infer first. Ask second.

If information can be reliably determined from:

* uploaded articles;
* previous manuscripts;
* proposals;
* theses or dissertations;
* datasets;
* research plans;
* user-provided descriptions;

do not ask the user to repeat it.

---

# Determine Research Entry Type

Classify the user into the most appropriate entry type.

## A. New Research

Use when the user:

* has no previous study to continue;
* has only a field of interest;
* has an observed problem;
* wants a new research direction;
* wants to explore emerging research topics.

Set:

`research_entry_mode: START_NEW_RESEARCH`

Likely next route:

`idea-discovery`

---

## B. Previous Research Continuation

Use when the user:

* has previously published or completed related research;
* uploads a previous article, thesis, dissertation, proposal, or report;
* asks what study should come next;
* wants a research roadmap based on prior work.

Set:

`research_entry_mode: CONTINUE_PREVIOUS_RESEARCH`

Do not perform a full new-research intake if prior research materials already establish the context.

Likely next route:

`research-resume`

---

## C. Existing Research Idea

Use when the user already has:

* a proposed topic;
* tentative variables;
* a phenomenon;
* a research problem;
* a provisional title.

Set:

`research_entry_mode: DEVELOP_EXISTING_IDEA`

Determine whether the next need is:

* landscape mapping;
* gap validation;
* research-question development;
* or methodology design.

---

## D. Existing Research Question

Use when a clear research question already exists.

Set:

`research_entry_mode: RESEARCH_DESIGN`

Do not force the user back through idea discovery unless the research question is unsupported or internally unclear.

Likely next route:

`problem-solving-approach`
or
`methodology-architect`

---

## E. Existing Data

Use when data have already been collected.

Set:

`research_entry_mode: DATA_ANALYSIS`

Collect only the information required to understand:

* research question;
* design;
* variables;
* sampling;
* data structure;
* analysis already performed.

Likely next route:

`analysis-planner`

---

## F. Existing Results

Use when analytical outputs or findings already exist.

Set:

`research_entry_mode: RESULT_INTERPRETATION`

Likely next route:

`result-interpreter`

---

## G. Existing Manuscript

Use when the researcher already has a manuscript, partial manuscript, article draft, thesis-derived article draft, or section that needs to be continued, restructured, rewritten, audited, targeted, or prepared for submission.

First determine the actual goal.

Possible goals include:

* manuscript architecture or restructuring;
* writing a new section;
* continuing an incomplete manuscript;
* scientific writing improvement;
* controlled rewriting or compression;
* scientific audit;
* journal selection;
* submission preparation;
* reviewer simulation;
* reviewer or editor response;
* revision after major or minor review;
* point-by-point rebuttal or resubmission preparation.

Do not assume that every existing manuscript should go directly to scientific audit.

### G1. Architecture or Restructuring

Use when the manuscript exists but its scientific structure, argument flow, section logic, evidence placement, table or figure strategy, or journal-compatible architecture needs to be established or substantially reorganized.

Set:

`research_entry_mode: MANUSCRIPT_ARCHITECTURE`

Route to:

`manuscript-architect`

Then, when the architecture is sufficiently stable:

`manuscript-writer`

---

### G2. Writing, Continuing, or Rewriting

Use when the manuscript architecture is already sufficiently clear and the researcher asks to:

* write a manuscript;
* write a specific section;
* continue an incomplete section;
* improve scientific writing;
* rewrite supplied text;
* compress or expand a section;
* improve coherence;
* translate scientific prose;
* adapt wording to a journal without changing the science.

Set:

`research_entry_mode: MANUSCRIPT_WRITING`

Route to:

`manuscript-writer`

If the requested writing reveals that the manuscript architecture is unstable, return first to:

`manuscript-architect`

---

### G3. Scientific Audit

Use when the manuscript already exists and the researcher asks whether it is scientifically coherent, internally consistent, sufficiently supported, reporting-compliant, or ready for submission.

Set:

`research_entry_mode: MANUSCRIPT_AUDIT`

Route to:

`manuscript-auditor`

Do not use manuscript audit as a substitute for manuscript architecture or manuscript writing.

---

### G4. Journal Selection

Use when the researcher wants to identify, compare, verify, rank, or prioritize appropriate journals for an existing manuscript.

Set:

`research_entry_mode: JOURNAL_SELECTION`

Before journal matching, determine whether the current manuscript version has already passed scientific audit.

If the manuscript has not yet passed `manuscript-auditor`, or if material scientific revisions have occurred since the last audit, route to:

`manuscript-auditor`

→ `journal-matcher`

If the same manuscript version has already passed `manuscript-auditor` with no unresolved submission-blocking issues and no material scientific changes since that audit, route directly to:

`journal-matcher`

Journal selection may evaluate scientific scope fit, audience, article type, methodological fit, current indexing, quartile context, publication model, mandatory versus optional APC, legitimacy, and submission strategy.

Journal selection must not redefine the scientific question, methods, results, novelty, causal status, or conclusion.

Do not repeat a completed scientific audit unnecessarily when the audited manuscript version has not materially changed.

---

### G5. Submission Preparation

Use when the manuscript is already scientifically stable and the researcher needs journal-specific preparation.

Set:

`research_entry_mode: SUBMISSION_PREPARATION`

Preferred routing is:

`manuscript-auditor`

→ `journal-matcher`

→ journal-specific manuscript adaptation when required.

Do not describe a manuscript as submission-ready while unresolved scientific, reference-integrity, reporting, or internal-consistency problems remain.

---

### G6. Reviewer Simulation

Use when the manuscript is sufficiently mature and the researcher wants an adversarial pre-submission review.

Set:

`research_entry_mode: REVIEWER_SIMULATION`

Before reviewer simulation, determine whether the current manuscript version has already passed scientific audit.

If the current manuscript version has not yet been audited, or if material scientific revisions have occurred since the last audit, route to:

`manuscript-auditor`

→ `reviewer-simulator`

If the same manuscript version has already passed `manuscript-auditor` with no unresolved submission-blocking issues and no material scientific changes since that audit, route directly to:

`reviewer-simulator`

Reviewer simulation is downstream of scientific audit and must not be used to substitute for unresolved manuscript-integrity, reporting, reference, methodological, analytical, or interpretation problems.

Do not repeat a completed scientific audit unnecessarily when the audited manuscript version has not materially changed.

---

### G7. Reviewer or Editor Response

Use when actual or simulated reviewer or editor feedback already exists and the researcher needs to assess, revise, rebut, or prepare a point-by-point response.

Typical signals include:

* an editor decision letter is provided;
* reviewer comments are provided;
* simulated reviewer comments are available;
* the manuscript has received major revision, minor revision, revise-and-resubmit, or reject-and-resubmit;
* the researcher asks for a response-to-reviewers document;
* the researcher wants to determine whether a reviewer request is scientifically valid;
* reanalysis, additional analysis, new evidence, or upstream scientific correction may be required;
* the researcher needs a second-round response or resubmission package.

Set:

`research_entry_mode: REVIEWER_RESPONSE`

Route to:

`reviewer-response`

Before final response drafting, identify:

* whether feedback is actual or simulated;
* whether comments come from an editor, reviewer, or internal simulation;
* which manuscript version was reviewed;
* whether the requested scientific revision has actually been completed;
* whether reanalysis or upstream correction is still required;
* whether journal policy or reporting requirements need verification.

Preserve:

```text
ACTUAL JOURNAL REVIEW
≠
SIMULATED REVIEW
```

Do not claim that a revision, reanalysis, reference check, policy check, ethics correction, or manuscript change has been completed unless it has actually been completed and verified.

If reviewer feedback reveals a genuine scientific problem, route back to the appropriate upstream skill before finalizing response language.

Examples include:

* research-question problem → `research-question-builder`;
* theory problem → `theoretical-framework`;
* conceptual-framework problem → `conceptual-framework`;
* methodology problem → `methodology-architect`;
* sampling problem → `sampling-strategy`;
* instrument problem → `instrument-design`;
* analysis problem → `analysis-planner` or `statistical-method-selector`;
* interpretation problem → `result-interpreter`;
* discussion problem → `scientific-discussion`;
* implication problem → `implication-builder`;
* novelty problem → `novelty-auditor`;
* reference-integrity problem → `reference-integrity-guard`;
* manuscript-structure problem → `manuscript-architect`;
* writing or clarity problem → `manuscript-writer`;
* journal-fit or post-rejection rematching problem → `journal-matcher`.

Do not use reviewer response as a cosmetic substitute for unresolved scientific correction.

Do not repeat manuscript audit automatically merely because reviewer comments exist.

If material scientific revisions are made, a new audit may become appropriate after those revisions are completed.

---

### Existing Manuscript Routing Summary

Use conceptually:

```text
Existing Manuscript
        │
        ├── structure unclear
        │        ↓
        │ manuscript-architect
        │        ↓
        │ manuscript-writer
        │
        ├── structure stable, writing needed
        │        ↓
        │ manuscript-writer
        │
        ├── scientific audit needed
        │        ↓
        │ manuscript-auditor
        │
        ├── journal selection needed
        │        ↓
        │   audit status check
        │        │
        │        ├── not yet audited / materially revised
        │        │        ↓
        │        │   manuscript-auditor
        │        │        ↓
        │        │   journal-matcher
        │        │
        │        └── same version already passed audit
        │                 ↓
        │            journal-matcher
        │
        ├── submission preparation
        │        ↓
        │ manuscript-auditor
        │        ↓
        │ journal-matcher
        │
        ├── reviewer simulation
        │        ↓
        │   audit status check
        │        │
        │        ├── not yet audited / materially revised
        │        │        ↓
        │        │   manuscript-auditor
        │        │        ↓
        │        │   reviewer-simulator
        │        │
        │        └── same version already passed audit
        │                 ↓
        │           reviewer-simulator
        │
        └── reviewer / editor response
                 ↓
          feedback source check
                 │
                 ├── actual journal review
                 │        ↓
                 │ reviewer-response
                 │
                 └── simulated review
                          ↓
                   reviewer-response
                          ↓
                 scientific correction?
                          │
                    ┌─────┴─────┐
                    │           │
                   YES          NO
                    │           │
                    ↓           ↓
             upstream skill   response /
                    │         revision
                    └─────┬─────┘
                          ↓
                 revision verification
                          ↓
                 READY_FOR_RESUBMISSION
                 when all gates are met
```

---

# Minimum Intake Dimensions

Do not mechanically ask every item.

Collect only dimensions relevant to the current case.

## 1. Research Domain

Examples:

* health;
* pharmacy;
* biomedical science;
* education;
* social science;
* engineering;
* environmental science;
* business and management;
* interdisciplinary research.

Record:

`discipline`

and, when known:

`research_area`

---

## 2. Research Interest

Identify what the researcher is interested in understanding, improving, explaining, predicting, developing, evaluating, or implementing.

Avoid converting a broad interest into a research title prematurely.

Examples:

Broad interest:

"Artificial intelligence in education"

is not yet a research problem.

Likewise:

"Chitosan"

is not yet a research question.

---

## 3. Problem or Phenomenon

Determine whether the user begins from:

* a theoretical problem;
* empirical inconsistency;
* practical problem;
* technological opportunity;
* clinical problem;
* educational problem;
* policy problem;
* social phenomenon;
* unexplained observation;
* previous research finding.

Record the problem in neutral language before proposing solutions.

---

## 4. Research Purpose

Determine the intended scientific goal.

Possible purposes include:

* explore;
* describe;
* compare;
* explain;
* test;
* estimate;
* predict;
* validate;
* develop;
* evaluate;
* optimize;
* intervene;
* implement;
* translate;
* synthesize evidence.

Do not impose a quantitative, qualitative, or mixed-method design at this stage.

---

## 5. Existing Research Materials

Identify available materials such as:

* previous publications;
* thesis/dissertation;
* proposal;
* research protocol;
* dataset;
* preliminary data;
* instruments;
* literature collection;
* systematic review;
* analysis results;
* research roadmap;
* editor decision letter;
* reviewer reports;
* simulated reviewer comments;
* prior response-to-reviewers letter;
* tracked-changes manuscript;
* clean revised manuscript.

Existing materials may substantially shorten the workflow.

---

## 6. Research Context

When relevant, identify:

* population;
* setting;
* institution;
* geographical context;
* industry;
* clinical context;
* education level;
* technology;
* species;
* intervention;
* exposure;
* outcome.

Do not assume context when the user has not supplied it.

---

## 7. Feasibility Constraints

Only ask about constraints when they may materially affect the research design.

Possible constraints:

* access to participants;
* access to data;
* laboratory availability;
* research equipment;
* software;
* funding;
* collaboration;
* ethical approval;
* study duration;
* sample accessibility;
* geographic access.

Do not reject an idea merely because some resources are currently unavailable.

Instead, use constraints later to compare feasible research pathways.

---

# Researcher Capability Context

When useful, identify existing expertise.

Examples:

* methodological expertise;
* laboratory capability;
* statistical skills;
* access to specialized instruments;
* clinical access;
* computational capability;
* qualitative research experience;
* previous publications.

This information is used to identify research opportunities that are both novel and realistically executable.

Do not assume that the researcher must remain within methods previously used.

---

# Publication Ambition

When the user indicates publication goals, record them.

Possible targets:

* national journal;
* Scopus-indexed journal;
* international reputable journal;
* Q1;
* Q2;
* Q3;
* Q4;
* conference;
* thesis/dissertation output;
* grant output.

Do not guarantee publication.

---

# Scopus-First Publication Preference

If publication in an international journal is an objective, record:

`scopus_preference: true`

The later literature workflow should prioritize peer-reviewed articles from active Scopus-indexed journals.

However:

* relevance comes before publisher prestige;
* methodological quality comes before citation convenience;
* seminal sources may be retained even when older;
* non-Scopus authoritative sources may be used when scientifically necessary.

Do not claim Scopus indexing without verification.

---

# No-Mandatory-APC Preference

When publication cost matters, record:

`prefer_no_mandatory_apc: true`

This means the later journal-selection workflow should prioritize:

1. strong scientific scope fit;
2. active Scopus indexing;
3. suitable journal quality;
4. no mandatory APC where comparable options exist.

Include legitimate subscription or hybrid journals that permit conventional publication without mandatory APC.

Do not interpret "hybrid journal" automatically as a paid journal.

Current publication policy must later be verified.

---

# Target-Journal Awareness

If the researcher already has one or more target journals, record them.

Later workflows may examine scientifically relevant articles from those journals to determine:

* topic fit;
* methodological fit;
* ongoing scholarly conversations;
* unresolved questions;
* how the proposed study may extend, test, support, refine, or challenge prior work.

Never recommend irrelevant citations merely because they were published in the target journal.

---

# High-Value Question Rule

Ask no more than 1–3 questions at one time unless the user explicitly asks for a structured intake interview.

Prioritize questions with the greatest effect on the route.

For example, when a user says:

"I want a new research topic in pharmacy."

Good questions may be:

1. Which area of pharmacy interests you most?
2. Do you want to build on previous research or start a new line?
3. What research resources or data can you realistically access?

Do not ask twenty questions at once.

---

# Progressive Intake

Intake may occur progressively.

Example:

User:
"I want to research AI in early childhood education."

Do not immediately request:

* sample size;
* statistical software;
* hypothesis;
* instruments;
* journal quartile;
* analysis technique.

First determine the research direction.

Later skills will collect details when they become relevant.

---

# Handling Uploaded Previous Research

If the user uploads a previous publication and asks for research continuation:

Do not summarize it as the final answer.

Record the material and route to:

`research-resume`

The next workflow should determine:

* what the previous study answered;
* what remains unresolved;
* how literature has evolved since publication;
* whether previous limitations remain genuine gaps;
* what scientifically defensible continuation pathways exist.

---

# Handling a Practical Problem

Users may begin from a real-world problem rather than an academic topic.

Example:

"Medication adherence among elderly patients in our clinic is low."

Preserve the practical problem first.

Do not immediately transform it into:

"Effect of X on Y."

Instead determine:

* what is happening;
* who is affected;
* what is not understood;
* what evidence would be useful;
* whether the scientific goal is explanatory, predictive, developmental, evaluative, or intervention-oriented.

Then route toward research discovery.

---

# Handling a Proposed Title

A proposed title is not automatically a valid research problem.

Extract:

* core phenomenon;
* variables or concepts;
* population;
* context;
* implied relationship;
* intended contribution.

Then determine which components require evidence validation.

Do not polish the title before confirming that the study itself is scientifically defensible.

---

# Handling Highly Specific Research Ideas

When the user already provides a highly developed idea, avoid unnecessary intake.

Example:

"I want to test whether X mediates the relationship between A and Y in population P."

The route may already be near:

* literature verification;
* gap validation;
* research-question refinement;
* methodology.

Do not return the user to broad idea discovery unless necessary.

---

# Idea Quality Must Not Be Judged During Intake Alone

`research-intake` may assess feasibility signals but must not make definitive claims such as:

* "This is novel."
* "Nobody has studied this."
* "This will publish in Q1."
* "This is a strong research gap."

Those claims require evidence from downstream literature workflows.

---

# Research Intake Brief

At the end of intake, create an internal or user-visible Research Intake Brief when useful.

Recommended fields:

## Research Intake Brief

**Research entry mode:**
[START_NEW_RESEARCH / CONTINUE_PREVIOUS_RESEARCH / DEVELOP_EXISTING_IDEA / RESEARCH_DESIGN / DATA_ANALYSIS / RESULT_INTERPRETATION / MANUSCRIPT_STAGE / REVIEWER_SIMULATION / REVIEWER_RESPONSE]

**Discipline:**
[...]

**Research area:**
[...]

**Current interest/problem:**
[...]

**Research purpose:**
[...]

**Existing materials:**
[...]

**Research context:**
[...]

**Available resources:**
[...]

**Important constraints:**
[...]

**Publication ambition:**
[...]

**Scopus-first preference:**
[Yes / No / Not yet specified]

**No-mandatory-APC preference:**
[Yes / No / Not yet specified]

**Target journal already known:**
[...]

**Current research stage:**
[...]

**Next recommended step:**
[...]

**Critical missing information:**
[...]

---

# Research Passport Preparation

When the framework supports a Research Passport, prepare or update relevant fields without inventing missing information.

Suggested fields:

```yaml
researcher:
  discipline:
  expertise:
  career_stage:

research:
  entry_mode:
  topic:
  problem:
  context:
  prior_research:

resources:
  data_access:
  participant_access:
  laboratory:
  software:
  funding:
  collaborators:

publication:
  ambition:
  scopus_preference:
  prefer_no_mandatory_apc:
  target_journals:

workflow:
  current_stage:
  completed_stages:
  next_stage:
```

Leave unknown fields empty rather than guessing.

---

# Routing Decisions

Typical routes from `research-intake`:

If no clear topic exists:

`idea-discovery`

If broad topic exists but scientific landscape is unclear:

`research-landscape`

If previous research exists:

`research-resume`

If the user already proposes a research gap:

`gap-validator`

If a research question already exists:

`problem-solving-approach`

If data already exist:

`analysis-planner`

If results already exist:

`result-interpreter`

If a manuscript already exists:

use the goal-specific routing defined in `## G. Existing Manuscript`.

Do not default every existing manuscript to `manuscript-auditor`.

Route according to the actual need:

* structure or restructuring → `manuscript-architect`;
* writing, continuation, rewriting, compression, expansion, or scientific translation → `manuscript-writer`;
* scientific audit → `manuscript-auditor`;
* journal selection → `journal-matcher`;
* reviewer simulation → `reviewer-simulator`;
* reviewer or editor response → `reviewer-response`.

When reviewer or editor comments already exist, do not route automatically to reviewer simulation.

Use `reviewer-response` to determine whether the comment can be answered directly or whether genuine scientific correction must first be routed upstream.

For submission preparation, use:

`manuscript-auditor`

→ `journal-matcher`

---

# Avoid These Behaviors

Do not:

* force every researcher through the same questionnaire;
* ask for information already contained in uploaded material;
* invent a research gap;
* invent novelty;
* choose statistics prematurely;
* guarantee publication;
* equate Scopus indexing with scientific quality;
* equate high quartile with perfect journal fit;
* equate hybrid publishing with mandatory APC;
* optimize research solely for journal acceptance;
* recommend citation padding;
* treat actual reviewer comments as simulated comments;
* treat simulated reviewer comments as actual journal review;
* claim that reviewer-requested revisions or reanalyses have been completed when they have not;
* route every reviewer comment to manuscript writing when the issue is scientific;
* mark a manuscript ready for resubmission while critical revision or verification tasks remain incomplete;
* overwhelm beginners with research jargon.

---

# User-Friendly Communication

Match the researcher's apparent level of experience.

For beginners:

* explain research terminology briefly;
* present limited choices;
* guide sequentially.

For experienced researchers:

* avoid elementary explanations unless needed;
* preserve technical terminology;
* focus on evidence, methodological choices, and strategy.

Do not patronize either group.

---

# Reviewer Response Intake

When reviewer or editor feedback exists, intake should capture only the minimum information needed to route the revision safely.

Relevant fields may include:

```yaml
review_context:
  source:
  actual_or_simulated:
  journal:
  manuscript_id:
  decision:
  review_round:
  manuscript_version_reviewed:
  revised_manuscript_version:
  editor_comments_present:
  reviewer_count:
  response_deadline:
  reanalysis_required:
  upstream_correction_required:
  revision_verification_required:
  readiness_status:
```

Unknown values remain unknown.

Do not fabricate:

* manuscript IDs;
* decision categories;
* reviewer identities;
* response deadlines;
* completed analyses;
* completed revisions;
* journal policies.

Possible readiness statuses include:

* `NOT_READY`;
* `SCIENTIFIC_CORRECTION_REQUIRED`;
* `REVISION_IN_PROGRESS`;
* `RESPONSE_REVIEW_REQUIRED`;
* `READY_WITH_MINOR_ADMIN_TASKS`;
* `READY_FOR_RESUBMISSION`.

`READY_FOR_RESUBMISSION` should be used only after required scientific corrections, revisions, evidence verification, manuscript-response consistency, and relevant journal requirements have been adequately resolved.

---

# Phenomenon Evidence Intake

During research intake, determine whether the researcher already has evidence describing the real-world phenomenon behind the research problem.

Possible available materials include:

- official statistics;
- government reports;
- international-agency reports;
- datasets;
- registries;
- surveillance data;
- regulations;
- policies;
- institutional reports;
- internal organizational data;
- spreadsheets;
- dashboards;
- credible news;
- uploaded files;
- pasted URLs;
- manually provided factual data.

Do not require phenomenon evidence when it is not scientifically relevant, such as some purely theoretical or methodological studies.

---

# Phenomenon Evidence Intake Questions

Ask only when necessary.

Useful questions may include:

> Do you already have official statistics, reports, datasets, regulations, or other factual evidence showing that this problem occurs?

> Is there a particular country, population, institution, or period that the background must describe?

> Do you have a report, dataset, regulation, spreadsheet, or URL that should be used?

Do not turn intake into a long questionnaire.

If the researcher has already supplied the material, record it instead of asking again.

---

# Phenomenon Evidence Availability

Classify:

- `PHENOMENON_EVIDENCE_AVAILABLE`
- `PHENOMENON_EVIDENCE_PARTIAL`
- `PHENOMENON_EVIDENCE_NOT_PROVIDED`
- `PHENOMENON_EVIDENCE_NOT_REQUIRED`
- `PHENOMENON_EVIDENCE_STATUS_UNKNOWN`

If available, identify input type.

Possible values include:

- `OFFICIAL_STATISTICS`
- `DATASET`
- `REPORT`
- `REGULATION`
- `POLICY`
- `INSTITUTIONAL_DATA`
- `NEWS`
- `URL`
- `FILE_UPLOAD`
- `USER_PROVIDED_FACT`
- `MULTIPLE_SOURCES`

---

# Phenomenon Evidence Need

Determine whether the research problem requires additional factual evidence about:

- magnitude;
- burden;
- trend;
- affected population;
- geographic distribution;
- policy context;
- regulatory context;
- service conditions;
- institutional conditions;
- real-world urgency.

Use:

- `PHENOMENON_EVIDENCE_REQUIRED`
- `PHENOMENON_EVIDENCE_USEFUL`
- `PHENOMENON_EVIDENCE_NOT_CENTRAL`
- `UNKNOWN`

When required or useful, route to:

`phenomenon-evidence-builder`

---

# Phenomenon vs Scientific Problem

During intake, distinguish:

```text
REAL-WORLD PROBLEM
"What is happening?"

from

SCIENTIFIC PROBLEM
"What does current knowledge fail to explain,
validate, predict, or resolve?"
```

---

# Uploaded Evidence Handling

If the researcher supplies:

- a report;
- regulation;
- spreadsheet;
- dataset;
- PDF;
- institutional document;
- URL;

record that material as available evidence.

Do not assume its authority or validity merely because it was supplied.

Route verification and contextualization to:

`phenomenon-evidence-builder`

when appropriate.

---

# User-Provided Fact Handling

If the researcher manually provides statistics or factual claims without source documentation, classify:

`USER_PROVIDED_UNVERIFIED_FACT`

Do not reject the information outright.

Instead, preserve it as a candidate fact and identify whether:

- documentation should be uploaded;
- a URL should be supplied;
- an authoritative source should be searched.

---

# Research Intake Evidence Architecture

Where relevant, intake should capture both:

```yaml
evidence_inputs:
  phenomenon_evidence:
    status:
    input_types:
    files:
    urls:
    reported_statistics:
    geography:
    population:
    reference_period:
    verification_needed:

  scholarly_evidence:
    status:
    previous_articles:
    literature_files:
    known_references:
    search_needed:
```

Unknown fields remain unknown.

---

# Research Passport Addition

When supported, add:

```yaml
phenomenon_context:
  phenomenon:
  population:
  geography:
  reference_period:
  evidence_need:
  evidence_status:
  available_inputs:
  official_statistics_available:
  dataset_available:
  regulation_or_policy_available:
  institutional_data_available:
  user_provided_urls:
  user_provided_files:
  unverified_facts:
  verification_required:
  phenomenon_evidence_next_stage:
```

Do not fabricate unavailable values.

---

# Routing After Intake

Possible pathway:

```text
research-intake
      ↓
Is real-world factual evidence needed?
      │
      ├── YES
      │    ↓
      │ phenomenon-evidence-builder
      │
      └── NO
           ↓
      continue research workflow
```

Phenomenon evidence and scholarly evidence may also be developed in parallel.

---

# Background Readiness

When a research background will eventually be written, intake should ideally determine whether enough evidence exists to support:

1. phenomenon existence;
2. magnitude or trend;
3. consequence or burden;
4. target-context relevance.

Do not fabricate these elements if they are unavailable.

Use:

- `BACKGROUND_PHENOMENON_READY`
- `BACKGROUND_PHENOMENON_PARTIAL`
- `BACKGROUND_PHENOMENON_NOT_READY`
- `NOT_APPLICABLE`

---

# Success Criterion

`research-intake` succeeds when enough context has been established to identify the shortest scientifically defensible next research workflow without requiring unnecessary information from the researcher; when existing manuscript, editor, reviewer, and simulated-review materials are recognized as evidence of the current stage rather than forcing a restart; when reviewer simulation is distinguished from actual reviewer or editor feedback; when existing reviewer comments can route directly to `reviewer-response`; when reviewer-response cases identify whether scientific correction, reanalysis, verification, or manuscript revision is still required before response language is finalized; when completed audit or review stages are not repeated unnecessarily; and when `READY_FOR_RESUBMISSION` is never assigned before required scientific, evidentiary, revision, consistency, and journal-requirement gates have been satisfied.
