---
name: scientific-knowledge-alignment
version: 0.1.0
language: en
stage: knowledge-alignment
status: draft
purpose: Convert heterogeneous scientific evidence into structured knowledge-alignment documents that are traceable, reviewable, computable, and jointly certifiable by interdisciplinary experts.
applies_to:
  - Academic papers
  - Online ontologies and standard terminology repositories
  - Experimental reports and laboratory records
  - Database and dataset documentation
  - Computational reports
  - Expert interviews and experiential rules
outputs:
  - Structured knowledge-alignment document
  - Machine-readable knowledge objects
  - Expert validation and unresolved-issue list
non_goals:
  - Do not perform task orchestration at this stage
  - Do not select or optimize algorithms at this stage
  - Do not produce a final performance ranking of candidate solutions at this stage
---

# Scientific Knowledge Alignment Skill Rules

## 0. One-Sentence Description

**The knowledge-alignment stage converts heterogeneous evidence from the literature, online ontologies, experimental reports, and expert experience into a unified, traceable, reviewable, and computable “concept–variable–relationship–evidence” structure, while recording definitions, applicable conditions, acquisition methods, confidence, and expert-validation status, thereby providing a shared semantic foundation for subsequent task orchestration, algorithm optimization, and performance feedback.**

---

## 1. Roles and Objectives

This Skill serves as the “knowledge translation layer” in an interdisciplinary research and development workflow. It establishes a shared, stable, and auditable intermediate language among materials scientists, experimental scientists, computer scientists, data scientists, and algorithm engineers.

It must enable downstream users to answer the following questions:

1. What variables, constraints, and application scenarios specifically define “high performance”?
2. What are the precise definition, unit, conditions, and reasonable range of each variable?
3. Can each variable be measured, derived, physically computed, empirically estimated, predicted by machine learning, or only assessed by experts?
4. Which variables can be compared directly across sources, and which require condition alignment or must not be merged?
5. Which variables are suitable as machine-learning inputs, labels, intermediate variables, constraints, or evaluation metrics?
6. Which relationships are definitions, physical mechanisms, statistical correlations, proxy relationships, trade-offs, or expert hypotheses?
7. Where does each value, relationship, and rule come from, and can it be traced to a page, table, figure, experimental batch, or data file?
8. Which knowledge objects have been validated by domain experts, and which remain unreviewed, conflicting, or hypothesis-only?
9. Which information can directly enter subsequent task orchestration, and which first requires additional experiments, calculations, or expert judgment?

---

## 2. Stage Boundaries

### 2.1 Requirements of This Stage

- Terminology normalization and concept mapping;
- Variable definition and quantification description;
- Structuring of conditions, methods, samples, and data sources;
- Separation of numerical observations from literature claims;
- Classification of relationships among variables;
- Annotation of computability and learnability;
- Traceability of literature and data evidence;
- Recording of expert validation, disagreement, and intervention;
- Compilation of missing information, conflicting knowledge, and unresolved issues;
- Generation of dual views for materials experts and computational experts.

### 2.2 Tasks That Must Not Be Performed Prematurely

Unless explicitly requested by the user, do not:

- Directly select a specific machine-learning algorithm;
- Directly build a training pipeline;
- Directly perform hyperparameter optimization;
- Directly produce a final ranking of candidate molecules;
- Treat an author’s interpretation as a proven mechanism;
- Treat expert experience as experimental fact;
- Treat predicted values as measured values;
- Merge performance values from different sources when conditions are missing;
- Replace an unconfirmed multi-objective design requirement with a single vague composite score.

---

## 3. Input Evidence Classification

Each input must first be classified:

| Evidence Type | Code | Description |
|---|---|---|
| Academic literature | `LIT` | Journal papers, conference papers, preprints, and supplementary materials |
| Online ontology | `ONT` | OWL/RDF ontologies, standard terminology repositories, and controlled vocabularies |
| Experimental report | `EXP` | Laboratory records, instrument exports, experimental summaries, and internal laboratory documents |
| Computational report | `CMP` | Quantum-chemical calculations, molecular simulations, numerical computations, and software outputs |
| Database or dataset | `DB` | Public databases, internal databases, and dataset documentation |
| Expert knowledge | `EXT` | Expert interviews, experiential rules, manual judgments, and meeting notes |
| Standards and specifications | `STD` | International standards, industrial specifications, measurement protocols, and unit standards |

Each knowledge object must retain `source_type`.

---

## 4. Core Knowledge Objects

All output knowledge must be organized as structured objects rather than free-text summaries only.

### 4.1 ConceptCard

```yaml
concept_id: "CONCEPT-0001"
label_zh: ""
label_en: ""
definition: ""
concept_type: ""
synonyms: []
abbreviations: []
broader_concepts: []
narrower_concepts: []
related_concepts: []
external_mappings:
  - ontology_name: ""
    ontology_version: ""
    iri: ""
    mapped_relation: "exactMatch|closeMatch|broaderMatch|narrowerMatch"
scope_note: ""
exclusion_note: ""
source_ids: []
expert_status: "unreviewed|reviewed|approved|rejected|disputed"
```

Rules:

- The definition must describe the concept itself and must not be circular;
- Chinese labels, English labels, abbreviations, and synonyms must be stored separately;
- When reusing a concept from an online ontology, its IRI and ontology version must be retained;
- When no formal mapping can be found, a project-level concept may be created, but it must be marked as `local_extension`;
- Do not fabricate ontology mappings or guess IRIs.

### 4.2 VariableCard

```yaml
variable_id: "VAR-0001"
label_zh: ""
label_en: ""
symbol: ""
definition: ""
scientific_role: "structure|state|mechanism|property|performance|application_endpoint|constraint"
intrinsic_or_contextual: "intrinsic|contextual|mixed"
value_type: "continuous|integer|categorical|ordinal|interval|distribution|boolean"
quantity_kind: ""
unit:
  preferred_unit: ""
  unit_iri: ""
dimension: ""
valid_range:
  min: null
  max: null
  basis: ""
direction_preference: "maximize|minimize|target_range|context_dependent|none"
required_conditions: []
applicable_scope: []
exclusions: []
acquisition_modes: []
ml_role: []
comparability_class: ""
source_ids: []
expert_status: "unreviewed|reviewed|approved|rejected|disputed"
```

#### Acquisition Mode Codes

| Code | Meaning |
|---|---|
| `M` | Experimentally measurable |
| `D` | Derivable from other variables using an explicit formula |
| `P` | Computable using physical, chemical, or quantum-mechanical models |
| `S` | Estimable using semi-empirical formulas or approximate methods |
| `L` | Predictable using machine-learning or statistical models |
| `H` | Currently depends primarily on expert judgment |
| `U` | No operational definition is currently available |

Each acquisition mode must include:

```yaml
acquisition_detail:
  mode: "M|D|P|S|L|H|U"
  method_ids: []
  required_inputs: []
  output_uncertainty: ""
  expected_cost: "low|medium|high|very_high"
  fidelity: "screening|approximate|reference|gold_standard|unknown"
  applicability_scope: []
  known_biases: []
```

#### Machine-Learning Role Codes

`ml_role` may contain:

- `feature`
- `target`
- `intermediate_target`
- `condition`
- `constraint`
- `ranking_criterion`
- `validation_metric`
- `not_recommended`

When a variable is marked as `target`, the following must be specified:

```yaml
ml_target_detail:
  task_type: "regression|classification|ranking|generation|multi_objective_optimization"
  sample_granularity: "molecule|conformer|molecule_condition|experiment|sample|other"
  label_source: "experimental|computed|literature_curated|expert|mixed"
  recommended_split: "random|scaffold|time|source_group|leave_one_paper_out|other"
  evaluation_metrics: []
  leakage_risks: []
  applicability_domain: ""
```

### 4.3 ConditionCard

```yaml
condition_id: "COND-0001"
condition_type: "solvent|temperature|pressure|pH|oxygenation|concentration|excitation|light_dose|aggregation_state|instrument_setting|sample_state|other"
label: ""
value: null
unit: ""
normalized_value: null
normalized_unit: ""
controlled_or_observed: "controlled|observed|unknown"
source_ids: []
```

Rules:

- Conditions must not be hidden in notes;
- Conditions that substantially affect performance must be modeled explicitly;
- Unreported conditions must be marked as `not_reported` and must not be guessed;
- The same variable observed under different conditions should be represented as different “object–condition” observations.

### 4.4 MethodCard

```yaml
method_id: "METHOD-0001"
label_zh: ""
label_en: ""
method_type: "experimental|computational|data_processing|extraction|expert_judgement"
purpose: ""
inputs: []
outputs: []
parameters: []
software:
  name: ""
  version: ""
instrument:
  manufacturer: ""
  model: ""
reference_standard: ""
fidelity: ""
known_limitations: []
external_mappings: []
source_ids: []
expert_status: "unreviewed|reviewed|approved|rejected|disputed"
```

### 4.5 ObservationCard

```yaml
observation_id: "OBS-0001"
subject_id: ""
variable_id: ""
value: null
value_text: ""
unit: ""
normalized_value: null
normalized_unit: ""
uncertainty:
  type: "sd|se|ci|range|detection_limit|not_reported|other"
  value: null
  lower: null
  upper: null
conditions: []
method_id: ""
sample_id: ""
replicate_count: null
data_status: "measured|computed|estimated|predicted|digitized_from_figure|expert_assigned"
quality_flags: []
evidence_ids: []
expert_status: "unreviewed|reviewed|approved|rejected|disputed"
```

Mandatory rules:

1. A “variable = value” record without a subject is not allowed;
2. Cross-literature comparability must not be assumed when conditions are missing;
3. Measured, computed, estimated, and predicted values must be distinguished;
4. Values read from figures must be marked as `digitized_from_figure`;
5. When a paper reports only a range or category, it must not be converted into a precise value without justification;
6. Unit conversion must retain the original value, original unit, and conversion rule.

### 4.6 ClaimCard

```yaml
claim_id: "CLAIM-0001"
subject_id: ""
predicate: ""
object_id: ""
claim_type: "definition|mechanism|causal|correlation|proxy|tradeoff|comparison|design_hypothesis|expert_rule"
polarity: "supports|inhibits|increases|decreases|associated_with|no_effect|uncertain"
context: []
asserted_by_source: ""
supporting_evidence_ids: []
contradicting_evidence_ids: []
claim_status: "reported|expert_hypothesis|consensus|contested|refuted|insufficient_evidence"
confidence:
  extraction_confidence: "low|medium|high"
  evidence_strength: "low|medium|high"
  conclusion_confidence: "low|medium|high"
expert_status: "unreviewed|reviewed|approved|rejected|disputed"
notes: ""
```

Mandatory rules:

- Observation and Claim objects must be separated;
- An “author interpretation” must not automatically be promoted to a “proven mechanism”;
- Statistical correlation must not be expressed as causation;
- Expert experience must use `expert_hypothesis` or `expert_rule`;
- When the same relationship is disputed, no evidence may be deleted; the claim must be marked `contested`.

### 4.7 EvidenceCard

```yaml
evidence_id: "EVID-0001"
source_type: "LIT|ONT|EXP|CMP|DB|EXT|STD"
source_id: ""
title: ""
authors_or_owners: []
identifier:
  doi: ""
  url: ""
  report_id: ""
  dataset_id: ""
  ontology_iri: ""
version_or_date: ""
locator:
  page: ""
  section: ""
  table: ""
  figure: ""
  supplementary_item: ""
  file_path: ""
  row_or_record: ""
evidence_form: "text|table|figure|raw_data|metadata|ontology_axiom|expert_statement|software_output"
extracted_content: ""
extraction_method: "manual|llm_assisted|programmatic|ocr|digitization"
extracted_by: ""
reviewed_by: []
review_status: "unreviewed|machine_checked|human_checked|expert_approved|rejected"
evidence_direction: "support|contradict|neutral|context_only"
quality:
  source_quality: "low|medium|high"
  method_quality: "low|medium|high|unknown"
  completeness: "low|medium|high"
  reproducibility: "low|medium|high|unknown"
```

### 4.8 DesignRuleCard

```yaml
rule_id: "RULE-0001"
statement: ""
trigger:
  structural_pattern: ""
  context: []
action:
  modification: ""
expected_effects:
  - variable_id: ""
    direction: "increase|decrease|target_range|uncertain"
mechanism_hypothesis:
  claim_ids: []
exceptions: []
tradeoffs: []
evidence_ids: []
computational_translation:
  computable_feature: ""
  representation: "SMARTS|descriptor|graph_pattern|manual_annotation|unknown"
  testable_target: ""
  proposed_validation: ""
status: "expert_hypothesis|literature_rule|partially_validated|validated|rejected|contested"
expert_reviews: []
```

Rules:

- Non-computable experience must still be retained;
- A computable proxy feature should be provided whenever possible;
- When translation is not possible, use `unknown` rather than forcing numerical representation;
- Potential exceptions and performance trade-offs must be recorded.

### 4.9 ExpertReviewCard

```yaml
review_id: "REVIEW-0001"
reviewed_object_type: "concept|variable|method|observation|claim|rule|document"
reviewed_object_id: ""
expert:
  name_or_id: ""
  discipline: ""
  role: ""
review_action: "approve|revise|reject|request_evidence|mark_uncertain|resolve_conflict"
comments: ""
required_changes: []
confidence: "low|medium|high"
timestamp: ""
version_reviewed: ""
```

Mandatory rules:

- The version before a manual revision must be retained;
- Conflicting opinions from experts in different disciplines must not overwrite one another and must be recorded in parallel;
- Only `expert_approved` key variables and rules may enter subsequent task orchestration by default;
- Unvalidated content may be retained but must be clearly marked.

---

## 5. Relationship-Type Rules

### 5.1 Ontology Relationships

- `is_a`
- `part_of`
- `has_role`
- `has_property`
- `participates_in`

### 5.2 Definition and Formula Relationships

- `is_defined_by`
- `is_calculated_from`
- `has_unit`
- `is_normalized_by`
- `depends_on`

### 5.3 Measurement Relationships

- `is_measured_by`
- `requires_condition`
- `uses_reference`
- `has_detection_limit`
- `has_uncertainty`

### 5.4 Computational Relationships

- `is_computed_by`
- `requires_input`
- `approximates`
- `has_fidelity`
- `is_surrogate_for`

### 5.5 Mechanistic Relationships

- `promotes`
- `inhibits`
- `enables`
- `competes_with`
- `mediates`
- `transforms_into`

### 5.6 Data and Model Relationships

- `correlates_with`
- `is_predictive_of`
- `is_proxy_for`
- `tradeoff_with`
- `is_feature_for`
- `is_target_for`
- `constrains`

Prohibited:

- Do not use `causes` in place of an ordinary correlation;
- Do not use `improves` without specifying which variable improves;
- Do not use “high,” “low,” “good,” or “poor” without a comparison baseline or threshold;
- Do not interpret co-occurrence as a mechanistic relationship.

---

## 6. Source-Specific Extraction Rules

### 6.1 Academic Literature `LIT`

The following must be extracted:

- Title, authors, year, and DOI;
- Research object and application scenario;
- Molecular or sample identity;
- Variable definitions;
- Observed values, units, and uncertainty;
- Experimental or computational conditions;
- Methods, instruments, software, and key parameters;
- Author claims;
- Page, table, figure, and supplementary-material location;
- Scope and limitations of the conclusions.

The following must be distinguished:

```text
A value reported in a paper ≠ an author-proposed mechanism ≠ a conclusion validated by project experts
```

When only an abstract is available:

- The research topic and author claims may be extracted;
- Precise values lacking location and conditions must not be extracted;
- Mark `evidence_completeness: low`.

### 6.2 Online Ontology `ONT`

The following must be recorded:

- Ontology name;
- Ontology version or access date;
- Concept IRI;
- Preferred label and formal definition;
- Broader and narrower relationships;
- Related properties;
- License information;
- Mapping relationship.

Prohibited:

- Do not use search snippets in place of formal ontology definitions;
- Do not claim an exact mapping before validating the IRI;
- Do not conflate ontology classes, properties, and instances;
- Do not ignore ontology-version changes.

### 6.3 Experimental Report `EXP`

The following must be recorded:

- Experimental project and report identifier;
- Sample identifier, batch, and preparation process;
- Experimental objective;
- Instrument, software, and version;
- Experimental conditions and controlled variables;
- Raw-data path;
- Data-processing workflow;
- Number of replicates;
- Uncertainty, errors, and outliers;
- Report author, experimental operator, and date.

When conditions are missing:

- Mark them as `not_reported`;
- Generate a manual follow-up question;
- Do not fill them in automatically based on convention.

### 6.4 Computational Report `CMP`

The following must be recorded:

- Computational objective;
- Molecular structure and conformer;
- Theoretical method;
- Functional, basis set, and potential-energy model;
- Solvent model;
- Charge and multiplicity;
- Software and version;
- Convergence conditions;
- Input and output files;
- Computed values;
- Whether the result has been calibrated against experiments;
- Known approximations and failure cases.

### 6.5 Expert Knowledge `EXT`

The following must be recorded:

- Expert discipline and role;
- Original statement;
- Applicable objects and conditions;
- Expected effects;
- Mechanistic interpretation;
- Exceptions;
- Confidence;
- Literature or experimental support;
- Computable proxy;
- Proposed validation method.

Prohibited:

- Do not place expert experience in Observation objects;
- Do not omit expert identity and applicable scope;
- Do not fabricate numerical values merely to facilitate modeling.

---

## 7. Comparability and Normalization Rules

### 7.1 Comparability Levels

| Level | Description |
|---|---|
| `C0` | Not comparable: definitions or units are inconsistent |
| `C1` | Qualitative comparison only |
| `C2` | Comparable under the same method and conditions |
| `C3` | Comparable after unit conversion or standardization |
| `C4` | Cross-method calibration is available and the data can be merged with relatively high reliability |

### 7.2 Checks Required Before Comparison

- Are the variable definitions identical?
- Are the units and dimensions consistent?
- Are the measurement methods compatible?
- Are the reference standards consistent?
- Are solvent, temperature, concentration, and other conditions consistent?
- Is the sample state consistent?
- Is the value experimental or computational?
- Are aggregation, degradation, batch, or instrument effects present?
- Is uncertainty available?

### 7.3 Cases That Must Not Be Averaged Directly

- Conditions differ and the variable is strongly condition-dependent;
- Measurement principles differ and no calibration is available;
- Identically named variables have different definitions;
- One value is experimental and another is predicted;
- One value represents a single-molecule state and another an aggregated state;
- A clear source or batch effect exists;
- Essential conditions are missing and comparability cannot be assessed.

---

## 8. Workflow

### Step 0: Initialize the Research Context

```yaml
alignment_context:
  project_name: ""
  scientific_domain: ""
  application_scenario: ""
  material_or_molecule_scope: ""
  target_question: ""
  stakeholder_roles: []
  known_objectives: []
  known_constraints: []
  out_of_scope: []
```

When “high performance” is undefined, it must be decomposed into candidate objective variables and constraints rather than used as a single label.

### Step 1: Register Evidence

Create an EvidenceCard for each input and assign a unique `evidence_id`.

### Step 2: Align Terms and Concepts

- Extract terms;
- Merge synonyms;
- Distinguish homonyms;
- Map concepts to external ontologies;
- Create project-level extension concepts;
- Submit the results to domain experts for review.

### Step 3: Register Variables

- Create a VariableCard;
- Specify definition, unit, conditions, and range;
- Assign M/D/P/S/L/H/U;
- Assign machine-learning roles;
- Assign a comparability level;
- Mark fields requiring confirmation.

### Step 4: Structure Methods and Conditions

- Create MethodCards;
- Create ConditionCards;
- Bind conditions to each Observation;
- Do not describe critical conditions only in notes.

### Step 5: Extract Observations

- Extract values from tables, text, figures, supplementary materials, or reports;
- Record original and normalized values;
- Record errors, replicate counts, and data status;
- Bind observations to evidence locations.

### Step 6: Extract Claims and Relationships

- Extract structure–property, property–mechanism, and mechanism–performance relationships;
- Distinguish mechanisms, causal relationships, correlations, proxies, and trade-offs;
- Bind supporting and contradicting evidence;
- Record the conclusion status.

### Step 7: Structure Expert Experience

- Encode experience as DesignRuleCards;
- Specify applicable conditions, exceptions, and trade-offs;
- Attempt to define a computable proxy;
- When translation is impossible, retain the knowledge explicitly as pending computational translation.

### Step 8: Expert Validation

At minimum, support:

1. Terminology and concept validation;
2. Variable-definition validation;
3. Condition and method validation;
4. Key-observation validation;
5. Mechanism and design-rule validation;
6. Computability and learnability validation;
7. Downstream task-usability validation.

### Step 9: Consistency and Quality Checks

All checks in Section 10 must be executed.

### Step 10: Generate the Knowledge-Alignment Document

Generate all of the following:

- A human-readable report;
- Machine-readable objects;
- A materials-scientist view;
- A computer-scientist view;
- A list of conflicts and missing information;
- Expert-validation status;
- A list of knowledge objects eligible for the next stage.

---

## 9. Required Output Structure

### 1. Project Background and Alignment Objectives

- Application scenario;
- Material or molecular scope;
- Current problem;
- Participating disciplines;
- Evidence scope of the current round.

### 2. Decomposition of High-Performance Objectives

| Objective or Constraint | Variable ID | Definition | Optimization Direction | Conditions | Validated? |
|---|---|---|---|---|---|

### 3. Core Concept Table

| Concept ID | Chinese and English Labels | Definition | Synonyms | External Ontology Mapping | Expert Status |
|---|---|---|---|---|---|

### 4. Core Variable Registry

| Variable ID | Definition | Unit | Condition Dependence | M/D/P/S/L/H/U | ML Role | Comparability | Expert Status |
|---|---|---|---|---|---|---|---|---|

### 5. Methods and Conditions Table

List experimental methods, computational methods, data-processing methods, and critical environmental conditions separately.

### 6. Observation Summary

| Subject | Variable | Value | Unit | Conditions | Method | Data Status | Evidence |
|---|---|---|---|---|---|---|---|

### 7. Relationship and Mechanism Graph

Group relationships into:

- Definition relationships;
- Physical or chemical mechanisms;
- Statistical correlations;
- Proxy relationships;
- Performance trade-offs;
- Hypotheses requiring validation.

### 8. Literature Claims and Conflicts

| Claim ID | Claim | Type | Supporting Evidence | Contradicting Evidence | Current Status | Expert Opinion |
|---|---|---|---|---|---|---|

### 9. Materials-Expert Design Rules

| Rule ID | Original Experience | Applicable Scope | Expected Effect | Computable Proxy | Exceptions | Status |
|---|---|---|---|---|---|---|

### 10. Computer-Scientist View

The following must be specified:

- Variables available as inputs;
- Variables available as labels;
- Variables available for intermediate supervision;
- Condition variables;
- Constraint variables;
- Label-scarce items;
- High-cost computational items;
- Missing-data patterns;
- Data-leakage risks;
- Recommended data-splitting strategy;
- Variables currently unsuitable for learning.

### 11. Expert Validation and Intervention Records

Display validation status, comments, and version by object.

### 12. Missing Information, Conflicts, and Open Issues

```yaml
issue_id: ""
issue_type: "missing_definition|missing_condition|missing_value|conflicting_claim|ontology_mapping|expert_disagreement|comparability|other"
description: ""
affected_objects: []
required_expert: ""
recommended_action: ""
priority: "low|medium|high|critical"
```

### 13. Input List for the Next Stage

List only the following objects that meet the minimum quality requirements and can enter task orchestration:

- Objective variables;
- Constraints;
- Available features;
- Condition variables;
- Reliable observations;
- Validated rules;
- Uncertainty information;
- Applicability-domain boundaries.

Do not automatically generate an algorithmic solution at this stage.

---

## 10. Mandatory Quality Checks

### 10.1 Completeness Checks

- [ ] Every concept has a definition;
- [ ] Every variable has a unit or is explicitly marked as dimensionless/categorical;
- [ ] Every condition-dependent variable lists its critical conditions;
- [ ] Every observation has a subject, variable, value status, and evidence;
- [ ] Every claim has a source;
- [ ] Every expert rule has an applicable scope;
- [ ] Every critical knowledge object has a validation status.

### 10.2 Traceability Checks

- [ ] Literature evidence is located to a page, table, figure, or supplementary item;
- [ ] Online ontologies record an IRI and version/access date;
- [ ] Experimental reports record a report ID, sample ID, and raw-data location;
- [ ] Computational reports record software, version, method, and input conditions;
- [ ] Expert knowledge records expert role and time.

### 10.3 Scientific Consistency Checks

- [ ] Correlation has not been represented as causation;
- [ ] Author interpretations have not been represented as proven mechanisms;
- [ ] Predicted values have not been represented as experimental values;
- [ ] Incomparable data have not been merged;
- [ ] Vague “high performance” has not replaced specific variables;
- [ ] Differences in conditions, methods, and samples have been recorded;
- [ ] Outliers and conflicting evidence have been recorded.

### 10.4 Computational Usability Checks

- [ ] Every proposed label has a defined sample granularity;
- [ ] Every proposed feature is available for newly generated objects;
- [ ] High-cost features are identified;
- [ ] Label-leakage risks are identified;
- [ ] Data grouping and batch effects are identified;
- [ ] The applicability domain is identified;
- [ ] Directly computable, approximately computable, and learnable variables are distinguished.

### 10.5 Expert-Validation Checks

- [ ] Core concepts have been reviewed by domain experts;
- [ ] Core variables have been jointly reviewed by domain and computational experts;
- [ ] Key methods and conditions have been reviewed by experimental or computational experts;
- [ ] Conflicting opinions have not been overwritten;
- [ ] Unvalidated content is clearly marked;
- [ ] All manual interventions retain version history and rationale.

---

## 11. Evidence-Confidence Rules

Do not use a single overall confidence score. The following must be represented separately:

1. `extraction_confidence`: whether the information was extracted correctly;
2. `source_quality`: whether the source itself is reliable;
3. `method_quality`: whether the experimental or computational method is reliable;
4. `evidence_strength`: how strongly the evidence supports the claim;
5. `conclusion_confidence`: whether the combined evidence supports the conclusion;
6. `expert_consensus`: whether experts agree.

Recommended levels: `low / medium / high`.

When multiple sources conflict, reduce `conclusion_confidence` rather than applying a simple majority vote.

---

## 12. Versioning and Change Rules

```yaml
document_version: ""
created_at: ""
updated_at: ""
created_by: ""
change_summary: ""
source_set_version: ""
ontology_versions: []
expert_review_round: ""
```

Rules:

- A change in a concept definition must create a new version;
- A change in a variable unit, formula, or applicable scope must create a new version;
- Expert rejection must not delete the previous record;
- When evidence is updated, the validation status of related objects must be reassessed;
- Downstream stages may only reference explicitly versioned knowledge objects.

---

## 13. Failure and Stop Conditions

Automatic merging must stop and an expert-review item must be generated when:

- The same variable has multiple incompatible definitions;
- The unit cannot be confirmed;
- The sample identity cannot be confirmed;
- Critical conditions are missing;
- A literature claim clearly conflicts with the reported data;
- Online ontology mapping is ambiguous;
- Experts have unresolved disagreements;
- A variable is proposed as a label but its sample granularity is unclear;
- A variable is proposed as an input but is unavailable for newly generated objects;
- No calibration basis exists across methods;
- Only secondary reporting is available and the primary evidence cannot be found.

---

## 14. Delivery Threshold for Subsequent Stages

A knowledge object may be marked:

```yaml
ready_for_task_orchestration: true
```

only when all minimum requirements below are satisfied:

- The definition is explicit;
- The ID is stable;
- The source is traceable;
- Conditions and units are explicit;
- Data status is explicit;
- Computability or learnability is explicit;
- Applicable scope is explicit;
- Critical conflicts have been resolved or explicitly retained;
- At least one review has been completed by the corresponding disciplinary expert.

Otherwise, use:

```yaml
ready_for_task_orchestration: false
blocking_reasons: []
```

---

## 15. Dual-Expert Summaries

### 15.1 Materials-Scientist Summary

Use domain language to explain:

- Research object and performance objectives;
- Main structure–property–mechanism chains;
- Validated and unvalidated design rules;
- Critical experimental conditions;
- Literature consensus and disagreements;
- Experimental or computational evidence still required.

### 15.2 Computer-Scientist Summary

Use modeling language to explain:

- Sample unit;
- Available inputs;
- Available labels;
- Condition variables;
- Intermediate variables;
- Constraints and optimization objectives;
- Data volume and missingness;
- High-cost and low-cost features;
- Comparability and batch effects;
- Data-leakage risks;
- Applicability domain;
- Content that cannot yet be modeled and the reasons.

---

## 16. Default Output Format

By default, generate all of the following:

1. `knowledge_alignment_report.md`: complete human-readable report;
2. `knowledge_objects.yaml`: machine-readable knowledge objects;
3. `expert_review_queue.yaml`: items requiring expert validation and intervention;
4. `task_orchestration_ready.yaml`: objects eligible for the next stage.

When the user requests only one file, embed the machine-readable YAML as an appendix in the Markdown document.

---

## 17. Final Behavioral Principles

- Center the process on evidence rather than fluent narration;
- Center the process on variables and conditions rather than paper abstracts;
- Prioritize traceability and reviewability rather than automatic completion;
- Prioritize shared interdisciplinary understanding rather than the terminology of a single discipline;
- Retain uncertainty when uncertain;
- State missing information explicitly;
- Display conflicts rather than hiding them;
- Expert experience may be preserved but must not be presented as fact;
- Computational convenience does not imply scientific correctness;
- Ontology consistency does not imply data comparability;
- Any knowledge entering subsequent task orchestration must have an explicit version and expert status.
