---
name: ethics-regulatory-gate
description: Determine whether a proposed, ongoing, revised, or completed research activity may proceed ethically, institutionally, contractually, and regulatorily before data collection, data use, intervention, specimen handling, linkage, sharing, publication, or reuse. Use when research involves human participants, animals, biological materials, health data, identifiable or sensitive data, secondary data, AI-assisted research, clinical or laboratory procedures, biosafety, environmental or dual-use concerns, cross-border transfer, external collaborators, restricted datasets, consent constraints, or reviewer-driven methodological changes. This skill distinguishes scientific validity from ethical permission, legal compliance from ethical acceptability, de-identification from anonymity, public availability from unrestricted reuse, and approved protocol from unrestricted future modification. It produces a transparent proceed/revise/approval-required/block decision without inventing legal conclusions, ethics approvals, consent scope, institutional rules, or regulatory status.
---

# Ethics Regulatory Gate

## Purpose

`ethics-regulatory-gate` determines whether a research activity may proceed, must be revised, requires formal approval or amendment, or should be blocked until ethical, institutional, contractual, or regulatory requirements are resolved.

Its central question is:

> Given the research activity, participants or data involved, intervention or observation, risk profile, consent status, privacy implications, institutional rules, contractual obligations, and applicable regulatory context, what ethical and regulatory conditions must be satisfied before the activity can proceed?

This skill is a decision gate.

It is not a substitute for:

- an ethics committee;
- institutional review board;
- animal ethics committee;
- biosafety committee;
- data protection officer;
- institutional legal office;
- competent regulator;
- or authorized research governance body.

The skill identifies requirements, risks, unresolved issues, and routing needs.

---

# 1. Core Principles

Preserve the following distinctions:

```text
ETHICAL APPROVAL ≠ SCIENTIFIC VALIDITY
SCIENTIFIC VALUE ≠ ETHICAL PERMISSION
PUBLIC DATA ≠ UNRESTRICTED USE
DEIDENTIFIED ≠ AUTOMATICALLY ANONYMOUS
CONSENT ≠ UNLIMITED FUTURE USE
LEGAL ≠ NECESSARILY ETHICAL
ETHICAL ≠ NECESSARILY LEGAL
APPROVED PROTOCOL ≠ UNRESTRICTED MODIFICATION
DATA POSSESSION ≠ DATA OWNERSHIP
DATA OWNERSHIP ≠ UNLIMITED REUSE
TECHNICAL FEASIBILITY ≠ PERMISSION
```

---

# 2. Gate Outcomes

Use one of:

- `PROCEED`
- `PROCEED_WITH_CONDITIONS`
- `REVISE_BEFORE_PROCEEDING`
- `FORMAL_APPROVAL_REQUIRED`
- `AMENDMENT_REQUIRED`
- `INSTITUTIONAL_REVIEW_REQUIRED`
- `REGULATORY_REVIEW_REQUIRED`
- `DATA_USE_AUTHORIZATION_REQUIRED`
- `CONSENT_SCOPE_REVIEW_REQUIRED`
- `PRIVACY_REVIEW_REQUIRED`
- `BIOSAFETY_REVIEW_REQUIRED`
- `ANIMAL_ETHICS_REVIEW_REQUIRED`
- `BLOCKED_PENDING_RESOLUTION`
- `NOT_APPLICABLE`

Do not collapse all uncertainty into `PROCEED`.

---

# 3. Activation Gate

Use `ethics-regulatory-gate` when research involves one or more of:

- human participants;
- identifiable human data;
- sensitive personal data;
- health records;
- genetic data;
- biological specimens;
- tissue or biobank material;
- minors;
- cognitively impaired participants;
- economically or institutionally dependent participants;
- vulnerable populations;
- intervention or experimental treatment;
- clinical research;
- drug or device research;
- surveys involving sensitive topics;
- interviews involving risk;
- deception;
- covert observation;
- online communities;
- social media data;
- secondary data;
- linked datasets;
- geolocation;
- audio or video recordings;
- facial images;
- biometric information;
- AI-assisted research;
- automated decision systems;
- laboratory hazards;
- microorganisms;
- genetic modification;
- radiation;
- hazardous chemicals;
- animals;
- ecological release;
- dual-use concerns;
- cross-border data transfer;
- commercial partners;
- externally owned datasets;
- restricted repositories;
- publication of identifiable case material;
- reviewer-requested methodological changes affecting approved procedures;
- or retrospective reuse of old data.

---

# 4. Required Upstream Context

Use, when available:

- research question;
- study design;
- methodology;
- protocol;
- sampling strategy;
- participant population;
- recruitment plan;
- intervention;
- comparator;
- procedures;
- specimen collection;
- data sources;
- data governance plan;
- data quality status;
- consent form;
- participant information sheet;
- existing ethics approval;
- approval number;
- approval dates;
- amendments;
- data use agreements;
- collaboration agreements;
- institutional policies;
- biosafety approvals;
- trial registration;
- regulatory submissions;
- funding conditions;
- repository conditions;
- intended publication;
- data-sharing plan;
- future reuse plan.

Do not invent missing approvals or permissions.

---

# 5. Ethical Domain Classification

Classify applicable domains:

- `HUMAN_PARTICIPANTS`
- `HUMAN_DATA`
- `HEALTH_DATA`
- `GENETIC_DATA`
- `BIOLOGICAL_MATERIAL`
- `CLINICAL_INTERVENTION`
- `DRUG_RESEARCH`
- `DEVICE_RESEARCH`
- `SURVEY_RESEARCH`
- `QUALITATIVE_RESEARCH`
- `ONLINE_RESEARCH`
- `OBSERVATIONAL_RESEARCH`
- `SECONDARY_DATA`
- `DATA_LINKAGE`
- `AI_RESEARCH`
- `ANIMAL_RESEARCH`
- `BIOSAFETY`
- `ENVIRONMENTAL`
- `DUAL_USE`
- `CROSS_BORDER`
- `COMMERCIAL_COLLABORATION`
- `PUBLICATION_ETHICS`

Multiple domains may apply.

---

# 6. Scientific Value Gate

Ethical research should have sufficient scientific value to justify participant burden, data access, resource use, or risk.

Ask:

- Is the research question meaningful?
- Is the design capable of answering it?
- Is unnecessary duplication avoided?
- Is sample burden justified?
- Are procedures necessary?
- Are risks proportionate to value?

If the design is scientifically incapable of answering the question, ethics approval alone does not rescue it.

Route upstream when required.

---

# 7. Human Participant Gate

For human participant research assess:

- recruitment;
- inclusion;
- exclusion;
- voluntariness;
- consent;
- capacity;
- coercion;
- undue influence;
- burden;
- risk;
- benefit;
- privacy;
- confidentiality;
- withdrawal;
- compensation;
- injury management where relevant;
- dissemination.

---

# 8. Participant Identification

Record:

```yaml
participant_scope:
  population:
  age_range:
  vulnerability:
  recruitment_source:
  relationship_to_researcher:
  dependency_relationship:
  language_needs:
  accessibility_needs:
  capacity_considerations:
  notes:
```

---

# 9. Vulnerability

Potential vulnerability may arise from:

- age;
- illness;
- cognitive impairment;
- incarceration;
- economic dependency;
- educational dependency;
- employment dependency;
- emergency condition;
- stigmatized status;
- immigration status;
- limited literacy;
- power imbalance.

Do not label a population vulnerable without explaining the relevant mechanism.

---

# 10. Coercion and Undue Influence

Assess whether participation may be influenced by:

- authority relationships;
- grading;
- employment;
- clinical dependency;
- financial inducement;
- access to services;
- fear of penalty.

Compensation is not automatically coercive.

Assess proportionality.

---

# 11. Consent Gate

Determine whether consent is:

- required;
- waived by competent authority;
- altered;
- implied;
- documented;
- verbal;
- written;
- electronic;
- parental/guardian;
- assent plus permission;
- not applicable.

Do not independently grant a waiver.

---

# 12. Valid Consent Elements

Where applicable consent should address:

- study purpose;
- procedures;
- duration;
- risks;
- benefits;
- alternatives where relevant;
- confidentiality;
- voluntary participation;
- withdrawal;
- compensation;
- contacts;
- data use;
- specimen use;
- future reuse;
- sharing;
- publication;
- recording;
- commercial implications where relevant.

---

# 13. Consent Scope

Use explicit statuses:

- `PRIMARY_USE_ONLY`
- `SPECIFIED_SECONDARY_USE`
- `BROAD_FUTURE_RESEARCH`
- `SPECIFIC_DATA_LINKAGE`
- `SPECIMEN_REUSE_ALLOWED`
- `EXTERNAL_SHARING_ALLOWED`
- `CONTROLLED_SHARING_ONLY`
- `COMMERCIAL_USE_ALLOWED`
- `COMMERCIAL_USE_PROHIBITED`
- `SCOPE_UNCLEAR`
- `CONSENT_NOT_AVAILABLE`

Do not infer broad future permission from generic consent language.

---

# 14. Capacity to Consent

Where decision-making capacity may be limited, determine whether:

- capacity assessment is required;
- legal representative is required;
- assent is appropriate;
- reconsent is needed later;
- emergency exception exists under applicable rules.

Do not determine legal capacity without competent authority.

---

# 15. Minor Participants

When minors are involved assess:

- parental/guardian permission;
- child assent;
- age thresholds;
- maturity;
- privacy from parents where applicable;
- sensitive-topic risk;
- reconsent when participant reaches adulthood in longitudinal research.

---

# 16. Withdrawal

Clarify:

- withdrawal from intervention;
- withdrawal from follow-up;
- withdrawal from future data collection;
- withdrawal of unused specimens;
- withdrawal of already anonymized data;
- withdrawal after analysis.

Do not promise deletion if technically or legally impossible.

---

# 17. Risk Classification

Classify risk as:

- `MINIMAL`
- `ABOVE_MINIMAL`
- `HIGH`
- `UNKNOWN`

Use domain-appropriate definitions.

Do not invent institutional thresholds.

---

# 18. Risk Categories

Potential risk includes:

- physical;
- psychological;
- social;
- economic;
- legal;
- reputational;
- privacy;
- stigmatization;
- employment;
- insurance;
- family;
- community;
- biosafety;
- environmental;
- informational.

---

# 19. Risk-Benefit Assessment

Record:

```yaml
risk_benefit:
  risk_type:
  likelihood:
  severity:
  mitigation:
  residual_risk:
  direct_benefit:
  societal_value:
  justification:
```

Do not overstate direct benefit.

---

# 20. Clinical Risk

For clinical research consider:

- intervention risk;
- adverse events;
- stopping rules;
- emergency management;
- standard care;
- rescue treatment;
- monitoring;
- safety reporting.

---

# 21. Compensation

Assess:

- reimbursement;
- compensation for time;
- treatment-related cost;
- injury compensation where applicable;
- undue inducement risk.

Do not invent compensation rules.

---

# 22. Recruitment Materials

Review whether materials are:

- accurate;
- non-coercive;
- non-misleading;
- proportionate;
- consistent with approval.

---

# 23. Privacy Gate

Privacy concerns include:

- collection context;
- observation context;
- recording;
- location;
- online identity;
- sensitive behavior;
- health status;
- genetics;
- biometrics.

Privacy relates to collection and observation.

Confidentiality relates to handling information.

---

# 24. Confidentiality Gate

Assess:

- identifiers;
- access;
- storage;
- transfer;
- publication;
- sharing;
- retention;
- breach response.

Coordinate with `research-data-governance`.

---

# 25. Identifiability

Classify data as:

- `DIRECTLY_IDENTIFIABLE`
- `INDIRECTLY_IDENTIFIABLE`
- `PSEUDONYMIZED`
- `DEIDENTIFIED`
- `ANONYMIZED`
- `AGGREGATED`
- `UNKNOWN`

Do not call pseudonymized data anonymous.

---

# 26. Sensitive Data

Sensitive data may include:

- health;
- genetics;
- biometrics;
- sexual behavior;
- mental health;
- criminal history;
- financial status;
- political views;
- religion;
- ethnicity;
- immigration;
- precise location;
- children’s data.

Applicable legal definitions vary.

---

# 27. Re-identification Risk

Assess risk from:

- rare conditions;
- exact dates;
- small geography;
- occupation;
- combinations of variables;
- free text;
- images;
- genomic data;
- longitudinal trajectories.

---

# 28. Data Minimization

Collect only what is scientifically necessary.

Do not collect identifiers merely because they are convenient.

---

# 29. Purpose Limitation

Data collected for one purpose may not automatically be reused for another.

Check:

- consent;
- legal basis;
- institutional approval;
- agreement;
- repository terms.

---

# 30. Secondary Data Gate

For secondary data determine:

- source;
- original purpose;
- access terms;
- identifiability;
- consent scope;
- ethics status;
- data use authorization;
- current intended use.

Public availability does not automatically remove ethical obligations.

---

# 31. Public Data

Distinguish:

- legally public;
- technically accessible;
- publicly posted;
- intentionally public;
- scraped without expectation of research use.

Ethical expectations may differ.

---

# 32. Social Media Research

Assess:

- platform expectations;
- public/private context;
- username identifiability;
- quoting risk;
- scraping terms;
- vulnerable users;
- sensitive topics;
- re-identification.

---

# 33. Online Community Research

Do not assume open membership equals consent to research.

Consider contextual integrity.

---

# 34. Web Scraping

Assess:

- website terms;
- robots rules where relevant;
- personal data;
- copyrighted content;
- burden on service;
- ethical expectation;
- contractual restrictions.

Do not provide legal conclusions without verification.

---

# 35. Data Linkage Gate

Linkage may increase identifiability.

Assess:

- purpose;
- consent;
- key control;
- authorization;
- linkage method;
- re-identification risk;
- sharing restrictions.

---

# 36. Genetic Data Gate

Genetic data may implicate:

- participant;
- relatives;
- ancestry;
- disease risk;
- incidental findings;
- future use;
- re-identification.

---

# 37. Genomic Data Sharing

Assess:

- consent;
- repository access level;
- controlled access;
- population sensitivities;
- family implications;
- cross-border transfer.

---

# 38. Incidental Findings

Where research may generate clinically relevant findings, clarify:

- whether findings will be returned;
- validation requirements;
- clinical confirmation;
- participant preference;
- referral pathways;
- limitations.

Do not promise return without validated process.

---

# 39. Biological Material Gate

For specimens assess:

- collection;
- ownership/stewardship;
- consent;
- storage;
- future use;
- export;
- destruction;
- linkage;
- commercial use;
- biobank governance.

---

# 40. Existing Specimens

Existing samples may still require:

- consent review;
- ethics review;
- material transfer authorization;
- provenance verification.

---

# 41. Biobank Research

Check:

- access committee;
- consent model;
- permitted uses;
- sample depletion;
- return of results;
- cross-border transfer;
- data linkage.

---

# 42. Clinical Intervention Gate

Determine whether the project includes:

- investigational intervention;
- off-label use;
- behavioral intervention;
- diagnostic intervention;
- device;
- procedure.

This may trigger additional oversight.

---

# 43. Drug Research

Potential requirements may include:

- ethics approval;
- competent regulatory authority;
- trial registration;
- safety reporting;
- investigational product control;
- monitoring;
- pharmacy accountability.

Do not infer jurisdiction-specific requirements without verification.

---

# 44. Device Research

Consider:

- device classification;
- investigational status;
- safety;
- operator training;
- incident reporting;
- regulator requirements.

---

# 45. Clinical Trial Registration

Registration requirements depend on study type and jurisdiction.

Coordinate with `registration-preregistration-builder`.

Do not treat registration as ethics approval.

---

# 46. Observational Health Research

Even non-interventional health-record studies may require:

- ethics review;
- waiver;
- data access authorization;
- privacy review.

---

# 47. Case Reports and Case Series

Assess:

- identifiability;
- consent for publication;
- images;
- rare condition;
- institutional policy.

Research ethics and publication ethics may differ.

---

# 48. Qualitative Research Gate

Assess:

- sensitive topics;
- distress;
- disclosure;
- confidentiality;
- community risk;
- identifiable quotations;
- audio/video;
- group confidentiality.

---

# 49. Focus Groups

Participants may reveal information to each other.

Confidentiality cannot be guaranteed in the same way as one-to-one interviews.

---

# 50. Deception

Deception requires special justification.

Assess:

- necessity;
- risk;
- alternatives;
- debriefing;
- withdrawal after debriefing;
- competent approval.

---

# 51. Covert Observation

Assess:

- expectation of privacy;
- feasibility of consent;
- risk;
- public setting;
- vulnerable population;
- recording.

---

# 52. Animal Research Gate

For animal research assess:

- scientific necessity;
- species;
- number;
- procedures;
- pain/distress;
- anesthesia;
- analgesia;
- humane endpoints;
- housing;
- euthanasia;
- trained personnel;
- approval.

---

# 53. 3Rs Principle

Where applicable evaluate:

- Replacement;
- Reduction;
- Refinement.

Do not invent animal ethics approval.

---

# 54. Wildlife Research

Consider:

- permits;
- capture;
- handling;
- habitat disturbance;
- endangered species;
- biosafety;
- release.

---

# 55. Biosafety Gate

Assess whether work involves:

- infectious agents;
- recombinant material;
- genetically modified organisms;
- biological toxins;
- human specimens;
- sharps;
- aerosol-generating procedures.

Route to competent biosafety review where required.

---

# 56. Hazardous Chemical Gate

Assess:

- chemical hazards;
- exposure controls;
- storage;
- waste;
- emergency response;
- training.

This skill does not replace laboratory safety procedures.

---

# 57. Radiation Gate

Research involving ionizing or non-ionizing radiation may require specialized approval.

---

# 58. Environmental Gate

Assess potential:

- release;
- pollution;
- ecosystem disturbance;
- protected habitat impact;
- waste disposal.

---

# 59. Dual-Use Gate

Some research may have beneficial and harmful applications.

Assess:

- pathogen enhancement;
- surveillance misuse;
- harmful biological capability;
- sensitive technical information;
- security concern.

Route to competent institutional authority when relevant.

---

# 60. AI Research Gate

AI-related research may involve:

- personal data;
- automated decision-making;
- bias;
- explainability;
- high-impact decisions;
- surveillance;
- model training data;
- generated content;
- participant interaction.

---

# 61. AI as Research Tool

When AI assists research, document:

- task;
- input data;
- whether sensitive data are exposed;
- model/provider;
- retention terms;
- human review;
- output verification.

Do not upload restricted research data to external AI systems without authorization.

---

# 62. AI as Intervention

If participants interact with AI, assess:

- risk;
- misinformation;
- reliance;
- monitoring;
- disclosure;
- adverse outcomes;
- escalation procedures.

---

# 63. Automated Decision Research

High-stakes automated decisions may require stronger governance.

Examples:

- health;
- education;
- employment;
- finance;
- justice.

---

# 64. Cross-Border Data Transfer

Assess:

- sending country;
- receiving country;
- institution;
- data category;
- transfer agreement;
- consent;
- privacy requirements;
- hosting location.

Do not assume cloud transfer is jurisdiction-neutral.

---

# 65. International Collaboration

Clarify:

- lead institution;
- local ethics approval;
- reliance agreement;
- material transfer;
- data transfer;
- publication rights;
- community obligations.

---

# 66. Data Use Agreement Gate

Check whether intended use is permitted by agreement.

Do not infer permission from technical access.

---

# 67. Material Transfer Agreement Gate

For specimens or physical research materials assess whether transfer authorization is required.

---

# 68. Collaboration Agreement

Research governance may require clarity on:

- data ownership;
- authorship;
- IP;
- publication;
- confidentiality;
- responsibilities.

Authorship itself should follow contribution standards, not contract alone.

---

# 69. Intellectual Property

IP restrictions may affect:

- sharing;
- disclosure;
- patent timing;
- repository deposit.

They do not justify falsifying or withholding required scientific disclosure.

---

# 70. Confidential Commercial Data

Commercial confidentiality must be balanced with research transparency.

Mark unverifiable restrictions explicitly.

---

# 71. Conflict of Interest Gate

Identify potential:

- financial interest;
- supervisory conflict;
- institutional interest;
- sponsor influence;
- personal relationship;
- intellectual commitment.

---

# 72. Sponsor Influence

Clarify whether sponsor controls:

- design;
- analysis;
- publication;
- data access;
- interpretation.

Undisclosed control is a scientific integrity risk.

---

# 73. Publication Ethics Gate

Assess:

- consent for identifiable material;
- plagiarism;
- duplicate publication;
- redundant publication;
- image manipulation;
- authorship;
- undisclosed conflicts;
- data fabrication;
- data falsification.

---

# 74. Identifiable Images

Before publication assess:

- consent;
- masking sufficiency;
- metadata;
- rare features;
- context.

Eye bars alone may not guarantee anonymity.

---

# 75. Audio and Video

Recordings may carry strong identifiability.

Assess:

- consent;
- storage;
- transcription;
- retention;
- sharing;
- publication excerpts.

---

# 76. Sensitive Quotations

Exact quotations may be searchable online.

Consider paraphrase or masking where ethically justified, while preserving scientific integrity.

---

# 77. Community-Level Harm

Research may harm communities even when individuals are de-identified.

Consider:

- stigmatization;
- discrimination;
- misrepresentation;
- extractive research;
- group privacy.

---

# 78. Indigenous and Local Community Research

Where applicable assess:

- community engagement;
- collective interests;
- governance;
- benefit sharing;
- culturally appropriate consent;
- data sovereignty.

Do not assume individual consent resolves collective concerns.

---

# 79. Benefit Sharing

Where relevant assess:

- access to findings;
- capacity building;
- community benefit;
- sample/data return;
- equitable partnership.

---

# 80. Justice

Evaluate whether:

- burdens are unfairly concentrated;
- benefits are unfairly restricted;
- vulnerable groups are used for convenience;
- exclusion lacks scientific basis.

---

# 81. Inclusion Ethics

Underrepresentation can itself be ethically important.

Do not exclude groups solely to simplify analysis unless scientifically justified.

---

# 82. Language Access

Consent and participant communication may require appropriate language and accessibility.

---

# 83. Accessibility

Consider:

- disability;
- visual;
- auditory;
- cognitive;
- digital access;
- mobility.

---

# 84. Remote Research

Assess:

- identity verification;
- consent;
- privacy;
- recording;
- platform security;
- crisis management;
- cross-border participation.

---

# 85. Emergency Research

Emergency research may involve special consent or waiver frameworks.

Do not independently authorize exceptions.

---

# 86. Retrospective Research

Retrospective design does not automatically mean no ethics review is needed.

---

# 87. Exemption

Only competent authorities determine formal exemption where required.

This skill may state:

`POTENTIAL_EXEMPTION_REVIEW`

not:

`EXEMPT`

unless documentation confirms it.

---

# 88. Existing Approval Verification

Record:

```yaml
ethics_approval:
  committee:
  institution:
  approval_number:
  protocol_title:
  version:
  approval_date:
  expiry_date:
  continuing_review:
  amendment_status:
  conditions:
  verification_status:
```

---

# 89. Approval Scope

Check whether current activity fits approved:

- objectives;
- population;
- sites;
- procedures;
- data;
- specimens;
- analyses;
- sharing;
- publication.

---

# 90. Amendment Gate

Potential amendment triggers include:

- new population;
- new site;
- new procedure;
- new intervention;
- new specimen;
- new primary outcome;
- new sensitive variable;
- new data linkage;
- new external collaborator;
- new sharing arrangement;
- new AI tool exposing data;
- materially changed risk;
- reviewer-requested additional experiment.

Do not assume minor manuscript changes require amendment.

---

# 91. Protocol Deviation

Distinguish:

- planned amendment;
- protocol deviation;
- violation;
- administrative correction.

Use institutional definitions where available.

---

# 92. Reviewer-Requested Changes

A reviewer request does not override ethics approval.

If reviewer-requested changes require:

- new participant contact;
- new specimens;
- new data linkage;
- new sensitive analysis;
- new intervention;

check approval requirements first.

---

# 93. New Analysis of Existing Data

New analysis may be permissible under existing scope or may require:

- amendment;
- secondary-use review;
- data-use authorization.

Assess before proceeding.

---

# 94. Future Use

Future use of data or specimens should be traced to:

- consent;
- ethics approval;
- governance policy;
- repository terms.

---

# 95. Data Retention Ethics

Retention should align with:

- consent;
- regulation;
- institution;
- funder;
- data-use agreement.

Do not invent a universal retention period.

---

# 96. Data Destruction

If required, document:

- data/specimen;
- authority;
- date;
- method;
- verification.

---

# 97. Data Breach

If a breach occurs, route immediately to institutional procedures.

Do not conceal or self-adjudicate notification requirements.

---

# 98. Adverse Event Gate

Clinical or interventional studies may require reporting of:

- adverse events;
- serious adverse events;
- unexpected events;
- protocol-related harm.

Applicable definitions vary.

---

# 99. Safety Monitoring

Assess whether the risk level requires:

- monitoring;
- independent oversight;
- stopping rules;
- data safety monitoring.

---

# 100. Research Misconduct Boundary

Ethics/regulatory review does not replace misconduct investigation.

Potential fabrication, falsification, or plagiarism should be routed to appropriate institutional integrity procedures.

---

# 101. Authorship Boundary

Authorship disputes are generally not ethics-approval issues unless linked to coercion, conflict, or misconduct.

---

# 102. Privacy Law Boundary

Do not provide definitive jurisdiction-specific legal advice unless verified.

Use:

- `LEGAL_REVIEW_REQUIRED`
- `PRIVACY_OFFICER_REVIEW_REQUIRED`

when uncertain.

---

# 103. Regulatory Verification

For named legal or regulatory requirements, verify current authoritative sources when the workflow supports external research.

Do not rely on memory for changing regulations.

---

# 104. Authority Hierarchy

Prefer, as applicable:

1. competent regulator;
2. national legislation or official legal source;
3. institutional ethics policy;
4. institutional research governance;
5. funder requirements;
6. repository terms;
7. professional guidance.

Do not let secondary commentary override primary authority.

---

# 105. Ethical Guidance vs Binding Rule

Distinguish:

- law;
- regulation;
- institutional policy;
- committee condition;
- professional guidance;
- best practice.

---

# 106. Jurisdiction Record

```yaml
jurisdiction:
  country:
  region:
  institution:
  regulator:
  applicable_rules:
  uncertainty:
```

Do not assume one-country rules apply globally.

---

# 107. Ethics Review Record

```yaml
ethics_review:
  activity:
  domain:
  participant_or_data_scope:
  consent_status:
  risk_status:
  privacy_status:
  approval_status:
  regulatory_status:
  contractual_status:
  amendment_status:
  unresolved_issues:
  gate_decision:
```

---

# 108. Ethical Issue Register

```yaml
ethical_issue:
  issue_id:
  domain:
  description:
  severity:
  affected_scope:
  requirement:
  evidence:
  mitigation:
  responsible_authority:
  status:
```

---

# 109. Severity

Use:

- `CRITICAL`
- `MAJOR`
- `MODERATE`
- `MINOR`
- `INFORMATIONAL`

---

# 110. Critical Ethics Failures

Examples:

- human research conducted without required approval;
- use beyond consent with no authorization;
- prohibited re-identification;
- unauthorized sensitive-data transfer;
- serious unmitigated participant risk;
- unapproved intervention;
- animal work without required oversight;
- major biosafety breach;
- publication of identifiable participant information without permission.

---

# 111. Major Ethics Issues

Examples:

- unclear consent scope;
- missing amendment;
- incomplete privacy safeguards;
- unresolved secondary-use authorization;
- uncertain data transfer terms;
- recruitment materials inconsistent with approval.

---

# 112. Moderate Issues

Examples:

- incomplete participant information wording;
- unclear retention explanation;
- minor consent-document inconsistency.

---

# 113. Minor Issues

Examples:

- administrative formatting;
- outdated contact detail;
- nonmaterial naming mismatch.

Do not trivialize issues that alter participant understanding.

---

# 114. Ethical Repair Actions

Possible actions:

- revise protocol;
- revise consent;
- seek amendment;
- seek new ethics review;
- seek data use authorization;
- de-identify;
- restrict access;
- remove unauthorized variable;
- revise recruitment;
- add monitoring;
- update sharing plan;
- obtain publication consent;
- stop activity pending review.

---

# 115. Gate Decision Logic

```text
Does the activity involve regulated or ethically sensitive scope?
        │
   ┌────┴────┐
   │         │
  No        Yes
   │         │
PROCEED    Is required approval/authorization known?
             │
        ┌────┴────┐
        │         │
       No        Yes
        │         │
REVIEW REQUIRED  Does current activity fit the approved scope?
                    │
               ┌────┴────┐
               │         │
              No        Yes
               │         │
       AMEND/REVIEW     Are consent/privacy/risk conditions satisfied?
                          │
                     ┌────┴────┐
                     │         │
                    No        Yes
                     │         │
              REVISE/BLOCK    PROCEED
```

---

# 116. Ethics Gate Passport

```yaml
ethics_regulatory_passport:
  status:
  ethical_domains:
  human_participant_status:
  animal_status:
  biological_material_status:
  data_privacy_status:
  consent_status:
  approval_status:
  amendment_status:
  regulatory_status:
  contractual_status:
  biosafety_status:
  cross_border_status:
  publication_ethics_status:
  unresolved_issues:
  next_action:
```

---

# 117. Relationship with Research Router

`research-router` should route here when the user asks:

- “Do I need ethics approval?”
- “Can I use this patient dataset?”
- “Can I reuse these samples?”
- “Can I publish this case?”
- “Can I add another analysis?”
- “Can I link these datasets?”
- “Can I upload these data to AI?”
- “Do I need an amendment?”
- “Can I share this dataset?”
- “Can I collect one more specimen after reviewer comments?”

---

# 118. Relationship with Research Intake

`research-intake` should capture:

- participant involvement;
- sensitive data;
- existing approvals;
- consent;
- specimens;
- intervention;
- external data;
- collaborators;
- jurisdictions.

Do not perform full ethics review at intake.

---

# 119. Relationship with Research Resume

When resuming prior research, verify whether existing approvals are:

- still active;
- expired;
- closed;
- applicable;
- amendable.

---

# 120. Relationship with Prior Research Auditor

`prior-research-auditor` may identify legacy ethical or consent limitations affecting continuation.

---

# 121. Relationship with Research Question Builder

If an ethically unacceptable research question requires invasive, deceptive, or unauthorized procedures, route back to `research-question-builder` for reframing where appropriate.

---

# 122. Relationship with Methodology Architect

Methodology must satisfy ethical constraints.

Do not allow convenience to produce unnecessary participant burden or risk.

---

# 123. Relationship with Problem-Solving Approach

The intended evidence-generation strategy should be ethically feasible.

---

# 124. Relationship with Protocol Builder

`protocol-builder` operationalizes:

- consent;
- recruitment;
- intervention;
- safety;
- privacy;
- withdrawal;
- incident handling.

Ethics requirements should be reflected there.

---

# 125. Relationship with Sampling Strategy

Sampling should be checked for:

- justice;
- coercion;
- vulnerability;
- exclusion fairness;
- recruitment appropriateness.

---

# 126. Relationship with Instrument Design

Instruments collecting sensitive information may require:

- stronger consent;
- privacy safeguards;
- distress management;
- optional responses.

---

# 127. Relationship with Research Data Governance

`research-data-governance` manages:

- identifiers;
- access;
- retention;
- sharing;
- linkage;
- archival controls.

Ethics requirements should constrain governance.

---

# 128. Relationship with Data Quality Auditor

Data-quality correction must not violate:

- consent;
- authorization;
- privacy;
- protocol.

---

# 129. Relationship with Analysis Planner

Analysis must remain within authorized data scope.

Do not create new sensitive constructs from data if doing so exceeds approved purpose without review.

---

# 130. Relationship with Statistical Method Selector

Statistical sophistication does not create ethical permission.

---

# 131. Relationship with Qualitative Analysis

Protect:

- participant identity;
- sensitive quotations;
- group confidentiality;
- contextual risk.

---

# 132. Relationship with Mixed-Method Analysis

Integration may increase identifiability.

Review linkage and combined datasets.

---

# 133. Relationship with Meta-Analysis

Meta-analysis generally uses published data, but ethics may still arise with:

- individual participant data;
- unpublished confidential data;
- restricted datasets.

---

# 134. Relationship with Result Interpreter

Ethical limitations may bound interpretation.

Example:

- consent scope restricts subgroup analysis;
- privacy prevents fine-grained reporting.

---

# 135. Relationship with Scientific Discussion

Ethical constraints may be legitimate study limitations and should be reported transparently where relevant.

---

# 136. Relationship with Implication Builder

Do not recommend implementation beyond the ethical and regulatory evidence.

---

# 137. Relationship with Manuscript Architect

Ensure manuscript architecture accommodates:

- ethics statement;
- consent statement;
- registration;
- data availability;
- conflict of interest;
- funding;
- protocol deviations.

---

# 138. Relationship with Manuscript Writer

`manuscript-writer` must not invent:

- ethics approval;
- consent;
- waiver;
- registration;
- trial number;
- data-sharing permission.

---

# 139. Relationship with Manuscript Auditor

`manuscript-auditor` should compare manuscript ethics statements with actual records.

---

# 140. Relationship with Journal Matcher

Journal requirements may exceed minimum institutional requirements.

They do not create retrospective ethical approval.

---

# 141. Relationship with Reviewer Simulator

Reviewer simulation may identify ethics/reporting vulnerabilities.

---

# 142. Relationship with Reviewer Response

Reviewer requests that alter participant or data scope must pass this gate before implementation.

---

# 143. Relationship with Reproducibility Auditor

`reproducibility-auditor` should evaluate whether the permitted and governed research record can be reconstructed without overriding ethics, privacy, consent, confidentiality, contractual restrictions, or regulatory obligations.

Reproducibility should not override privacy or consent.

Restricted or sensitive data can still support reproducible research through appropriately authorized controlled-access procedures.

If reproducibility requirements appear to conflict with consent scope, privacy safeguards, data-use agreements, participant rights, or regulatory restrictions, preserve those constraints and route the unresolved issue back through `ethics-regulatory-gate` rather than weakening protections merely to make data or code publicly accessible.

---

# 144. Relationship with Research Roadmap

Long-term research programs should plan:

- renewal;
- amendments;
- cohort consent;
- biobank governance;
- secondary use;
- data sharing;
- cross-border collaboration.

---

# 145. Relationship with Registration / Preregistration Builder

`registration-preregistration-builder` should distinguish:

- ethics approval;
- study registration;
- protocol registration;
- preregistration.

None substitutes automatically for the others.

---

# 146. Ethics Gate Output Package

Produce, as needed:

1. Ethics Scope Classification
2. Approval Status
3. Consent Status
4. Risk Assessment
5. Privacy Assessment
6. Regulatory Status
7. Contractual Status
8. Amendment Need
9. Biosafety Status
10. Cross-Border Status
11. Publication Ethics Status
12. Unresolved Issues
13. Gate Decision
14. Required Next Action
15. Research Passport Update

---

# 147. Ethics Decision Summary Template

```yaml
ethics_regulatory_gate:
  project:
  activity:
  domains:
  scientific_value_status:
  participant_status:
  consent_status:
  privacy_status:
  risk_status:
  approval_status:
  amendment_status:
  regulatory_status:
  contractual_status:
  biosafety_status:
  cross_border_status:
  publication_ethics_status:
  gate_decision:
  required_actions:
  unresolved_issues:
```

---

# 148. Consent Review Template

| Element | Present | Clear | Applicable | Action |
|---|---|---|---|---|
| Purpose | | | | |
| Procedures | | | | |
| Risk | | | | |
| Benefits | | | | |
| Voluntary participation | | | | |
| Withdrawal | | | | |
| Privacy/confidentiality | | | | |
| Data reuse | | | | |
| Specimen reuse | | | | |
| Sharing | | | | |
| Publication | | | | |
| Contact | | | | |

---

# 149. Approval Scope Matrix

| Activity | Approved | Current Scope | Amendment Needed | Evidence |
|---|---|---|---|---|

---

# 150. Risk Matrix

| Risk | Likelihood | Severity | Mitigation | Residual Risk | Acceptability |
|---|---|---|---|---|---|

---

# 151. Data Ethics Matrix

| Data Type | Identifiability | Consent Scope | Access | Sharing | Status |
|---|---|---|---|---|---|

---

# 152. Regulatory Requirement Matrix

| Requirement | Authority | Applicable? | Verified | Action |
|---|---|---|---|---|

---

# 153. Compact User-Facing Output

Example:

```text
Ethics/regulatory status: AMENDMENT REQUIRED

What is already covered
- Existing approval covers the current participant population.
- Existing consent covers the primary clinical analysis.

What is new
- The proposed linkage with genetic data is not clearly described in the approved protocol.
- Future external sharing is not clearly covered by the consent language.

What should happen next
1. Confirm the consent scope for genetic linkage.
2. Submit an amendment or secondary-use request to the competent ethics body if required.
3. Do not perform the new linkage until authorization is confirmed.

This is a governance recommendation, not a substitute for the formal ethics committee decision.
```

---

# 154. User-Friendly Behavior

Instead of:

> “This is illegal.”

Prefer:

> “I cannot establish from the available information that this use is authorized. The applicable institutional or legal authority should confirm whether the proposed use is permitted.”

Instead of:

> “No ethics needed.”

Prefer:

> “The activity appears low risk, but formal exemption or non-human-subject determination should be made by the competent institutional authority if your institution requires it.”

---

# 155. No Approval Fabrication

Never invent:

- approval number;
- committee name;
- approval date;
- exemption;
- waiver;
- registration number;
- regulatory authorization.

---

# 156. No Legal Overclaiming

Do not state definitive jurisdiction-specific legal conclusions without verified authority.

---

# 157. No Ethics Washing

Do not treat an approval letter as proof that:

- the study is scientifically valid;
- the analysis is correct;
- the reporting is accurate;
- the consent covered every future use.

---

# 158. No Public-Data Shortcut

Public availability is not automatically ethical permission for any use.

---

# 159. No Consent Shortcut

Signed consent is not unlimited permission.

---

# 160. No De-identification Shortcut

Removing names does not automatically eliminate re-identification risk.

---

# 161. No Reviewer Override

Reviewer requests do not override ethics or regulatory requirements.

---

# 162. No Publication Override

Journal acceptance does not retroactively legitimize unapproved research.

---

# 163. No Software Override

Software capability does not create ethical permission.

---

# 164. No Funding Override

Funder approval does not substitute for ethics or regulatory review.

---

# 165. No Institutional Assumption

Different institutions may apply different review procedures.

Do not assume universal administrative pathways.

---

# 166. Stop Conditions

Stop and require formal resolution when:

- required approval appears absent;
- consent scope is incompatible with intended use;
- privacy risk is unresolved;
- high-risk participant procedures lack oversight;
- intervention authorization is unclear;
- restricted data are being transferred without authorization;
- participant identity would be disclosed without permission;
- animal work lacks required review;
- biosafety risk is unresolved;
- reviewer-requested new procedures exceed approved scope;
- cross-border transfer requirements are unclear;
- legal or institutional prohibition may apply.

Use:

- `BLOCKED_PENDING_RESOLUTION`
- `FORMAL_APPROVAL_REQUIRED`
- `AMENDMENT_REQUIRED`
- `CONSENT_SCOPE_REVIEW_REQUIRED`
- `PRIVACY_REVIEW_REQUIRED`
- `REGULATORY_REVIEW_REQUIRED`
- `DATA_USE_AUTHORIZATION_REQUIRED`
- `BIOSAFETY_REVIEW_REQUIRED`
- `ANIMAL_ETHICS_REVIEW_REQUIRED`
- `LEGAL_REVIEW_REQUIRED`

---

# 167. Gate Completion

The gate is complete when:

- applicable ethical domains are identified;
- participant or data scope is clear;
- consent status is clear;
- privacy status is clear;
- risk is characterized;
- approval status is known;
- amendment need is assessed;
- regulatory uncertainty is visible;
- contractual constraints are visible;
- required authorities are identified;
- a proceed/revise/review/block decision is recorded.

---

# 168. Ethics Regulatory Passport

```yaml
ethics_regulatory_passport:
  project:
  gate_status:
  domains:
  participants:
  vulnerable_population:
  consent:
  privacy:
  identifiability:
  risk:
  ethics_approval:
  amendment:
  regulator:
  data_use_authorization:
  biosafety:
  animal_ethics:
  cross_border:
  contracts:
  publication_ethics:
  unresolved_issues:
  required_action:
```

---

# 169. Final Ethics Rule

Never allow scientific convenience to replace permission.

Never allow technical access to replace authorization.

Never allow publication pressure to override participant rights, privacy, safety, or regulatory obligations.

When authority is uncertain, preserve uncertainty and route to the competent body.

---

# Success Criterion

`ethics-regulatory-gate` succeeds when the proposed, ongoing, revised, reused, shared, or published research activity has been evaluated across the ethical, participant, consent, privacy, identifiability, risk, biological-material, animal, biosafety, AI, contractual, cross-border, regulatory, and publication-governance domains that actually apply; when scientific validity is distinguished from ethical permission and legal compliance; when public availability, de-identification, consent, data possession, existing approval, registration, and journal requirements are prevented from being treated as unlimited authorization; when the current activity is explicitly compared with the approved or permitted scope; when amendments, waivers, secondary-use review, privacy review, data-use authorization, regulatory review, biosafety review, or animal ethics review are identified without being fabricated; when reviewer-driven changes are prevented from bypassing prior approvals; when jurisdiction-specific uncertainty is represented honestly rather than guessed; when participant rights, community interests, privacy, safety, data protection, and research integrity remain visible throughout the workflow; and when the final gate decision clearly states whether the research may proceed, may proceed with conditions, must be revised, requires competent approval or authorization, or must remain blocked until the relevant ethical or regulatory issue is resolved.
