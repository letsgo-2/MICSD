---
name: scientific-execution-orchestrator
version: 0.3.1
language: en-US
stage: execution-orchestration
status: draft
purpose: Convert knowledge-alignment results, rule assumptions provided by experts from each domain, and explicitly defined optimization objectives into an executable, adjustable, and reviewable model-optimization workflow.
fixed_inputs:
  - knowledge_alignment_report.md
  - knowledge_alignment.yaml
  - expert_review_queue.yaml
fixed_outputs:
  - execution_orchestration_report.md
  - execution_orchestration.yaml
  - execution_review_queue.yaml
---

# Scientific Execution Orchestration Skill

## 0. Purpose

This Skill is independent of the Knowledge Alignment Skill and serves as its downstream execution stage. It does not reorganize all knowledge from scratch. Instead, it prioritizes inheriting metrics, thresholds, conditions, evidence, and expert questions from upstream outputs, and completes the following:

1. Semantic fusion, ranking, and role confirmation of metrics;
2. Interface registration for models, surrogate models, and computational tools;
3. Construction of Rewards, constraints, search spaces, and execution workflows;
4. Controlled parameter adjustment, expert feedback, and iterative updates.

This Skill is not dependent on any specific case, nor does it require the upstream stage to contain a complete fixed schema. It should perform “semantic + field” fusion across YAML fields, Markdown tables, and natural-language content. Missing information must remain missing and must not be guessed.

---

## 1. Inputs and Outputs

### Fixed Inputs

Read in the following order:

1. `knowledge_alignment.yaml`: preferentially obtain structured metrics, proxy metrics, thresholds, evidence, and statuses;
2. `knowledge_alignment_report.md`: supplement definitions, scenarios, tables, and scientific explanations;
3. `expert_review_queue.yaml`: obtain unresolved metrics, thresholds, model requirements, and expert questions.

When files or fields are missing, record the missing information and continue processing the remaining content. Only critical missing information that affects the main objective, hard constraints, or model execution should be added to the blocking queue.

### Fixed Outputs

- `execution_orchestration_report.md`: expert-facing metric rankings, model recommendations, Reward design, workflows, and adjustment summaries;
- `execution_orchestration.yaml`: a unified configuration for agent execution;
- `execution_review_queue.yaml`: issues requiring expert confirmation, additional evidence, or handling.

---

## 2. Upstream Metric Fusion

### 2.1 Content to Extract

Prioritize identifying:

- Metric names, IDs, aliases, definitions, units, and applicable conditions;
- Candidate roles: objective, constraint, proxy, diagnostic, or intermediate metric;
- Optimization direction, thresholds, ranges, and acquisition methods;
- Evidence, source locations, confidence status, and expert status;
- Dependencies, conflicts, redundancies, and trade-offs among metrics;
- Feasible spaces, forbidden regions, and domain rules;
- Models, data, scripts, environments, server locations, and parameters;
- Expert questions that remain unresolved.

### 2.2 Fusion Rules

- Do not depend on fixed field names; determine identity using definitions, units, conditions, context, and evidence;
- Metrics with the same name but different definitions or conditions must be retained separately;
- When names differ but semantics are equivalent, establish aliases and merge them;
- When YAML and the report conflict, retain both versions side by side and submit them for expert review;
- Upstream rankings, thresholds, roles, and Rewards are candidate recommendations by default unless they have already been expert-approved;
- Newly added literature, online evidence, and expert opinions must retain their sources and must not overwrite upstream records;
- Missing fields must remain empty, and whether they enter the review queue should be determined by their importance.

```yaml
metric_candidate:
  metric_id: ""
  name: ""
  aliases: []
  definition: ""
  proposed_roles: []
  direction: "maximize|minimize|target_range|context_dependent|unknown"
  threshold: {value: null, range: [], unit: "", status: "unresolved"}
  conditions: []
  acquisition: []
  evidence_refs: []
  expert_status: "pending|approved|revised|rejected|disputed"
  unresolved_fields: []
```

---

## 3. Metric Ranking and Decision-Making

### 3.1 Ranking Basis

The agent should provide a reason for the ranking of each item and must consider at least:

- Direct relevance to the final scientific objective;
- Strength of evidence and expert consensus;
- Degree of measurability, computability, or predictability;
- Readiness of models, data, and scripts;
- Completeness of units, conditions, sample granularity, and applicability domain;
- Ability to distinguish among candidates;
- Computational, experimental, and human costs;
- Uncertainty, bias, redundancy, and conflict.

`high/medium/low` or `1–5` may be used to assist ranking, but a textual basis must be retained. A single composite score alone is not sufficient.

### 3.2 Final Roles

After expert confirmation, each metric should be assigned one primary role:

- `primary_objective`
- `secondary_objective`
- `hard_constraint`
- `soft_constraint`
- `diagnostic`
- `deferred`
- `excluded`

When the scenario or mechanistic route has not been determined, mutually exclusive branches may be created. Metrics with contradictory directions must not be activated within the same branch.

```yaml
metric_decision:
  metric_id: ""
  final_role: ""
  rank: null
  ranking_basis: []
  direction: ""
  threshold: {}
  evaluator_id: ""
  decision_status: "proposed|expert_approved|active|suspended"
  evidence_refs: []
  expert_feedback_refs: []
```

---

## 4. Evidence and Model Recommendations

When upstream information is insufficient to determine metrics, thresholds, or models, the agent may retrieve papers, datasets, model papers, software documentation, or online evidence, and propose:

- Predictive models, surrogate models, physics-based computational methods, or rule-based checkers;
- Training data, input features, and validation methods;
- Model applicability domain, cost, uncertainty, and limitations;
- Additional bases for thresholds, evaluation methods, or search strategies.

Each recommendation must specify the task, inputs and outputs, supported metrics, evidence sources, and current availability status. Models must not be selected solely on the basis of popularity, leaderboard position, or promotional claims in papers.

---

## 5. Unified Model Interface

```yaml
model_interface:
  model_id: "MODEL-001"
  name: ""
  role: "predictor|surrogate|physics_calculator|generator|constraint_checker|uncertainty_model"
  status: "proposed|available|validated|active|failed|deprecated"
  source: {type: "local|server|repository|package|paper|api", location: "", version: ""}
  entrypoint: {command: "", script: "", environment: "", working_directory: ""}
  human_provision:
    model_information_provided: false
    script_location_provided: false
    executable_interface_exposed: false
    parameter_interface_exposed: false
    access_level: "none|inspect_only|execute_fixed|adjust_parameters"
    authorized_parameters: []
    prohibited_actions: []
    provided_by: ""
    confirmation_ref: ""
  input_schema: []
  output_schema: []
  supported_metrics: []
  parameters: {}
  validation: {test_data: "", metrics: {}, applicability_domain: "", known_failures: []}
  evidence_refs: []
```

Requirements:

- Activated models must explicitly define inputs, outputs, units, versions, and failure states;
- Outputs must map to specific metrics and must not return only an uninterpretable total score;
- It must first be determined whether a human has explicitly provided model information, a script location, an executable entry point, and a parameter interface;
- When only a paper, model name, or description has been provided, the model may only remain in `proposed` status and must not be claimed to be callable;
- When a script location has been provided but the parameter interface has not been exposed, the model may only be tested or executed with a fixed configuration and parameters must not be changed autonomously;
- Controlled automatic parameter tuning may be enabled only after a human has explicitly exposed the parameter interface, provided the adjustable parameters and their boundaries, and authorized `adjust_parameters`;
- File accessibility does not imply permission to modify it. Authorization must not be inferred from the existence of a path;
- After execution authorization is obtained, a model path or script provided by an expert must undergo at least one small-scale test;
- Predicted values, proxy values, computed values, and experimental values must be strictly distinguished;
- When a model is unavailable, switch to a backup model, transfer the task to manual evaluation, or suspend the corresponding metric;
- Do not modify original models or production scripts provided by experts. Adapters, configuration copies, and run records must be stored separately.

Model exposure status constrains only model execution and automatic parameter tuning. It does not block metric organization, model recommendations, or workflow drafting. When authorization information is missing, write the issue to `execution_review_queue.yaml`.

---

## 6. Reward and Constraints

Use only approved metrics or metrics explicitly marked for trial execution.

Construction order: confirm roles and thresholds → bind evaluators → define normalization and missing-value handling → apply hard constraints → compute objectives and soft constraints → set weights and uncertainty handling → obtain expert approval.

```yaml
reward_component:
  component_id: "RC-001"
  metric_id: ""
  evaluator_id: ""
  role: "objective|hard_constraint|soft_constraint"
  direction: "maximize|minimize|target_range"
  threshold: {}
  normalization: "minmax|zscore|rank|piecewise|custom|none"
  weight: null
  uncertainty_penalty: ""
  missing_policy: "reject|penalize|skip|manual_review"
  status: "proposed|approved|active|suspended"
  evidence_refs: []
```

Rules:

- Hard constraints take precedence over weighted scores;
- Metrics with different dimensions must be normalized first;
- Thresholds must be marked as inherited, literature-supported, expert-proposed, or run-calibrated;
- Weights may be adjusted by experts;
- Proxy metrics must not be presented as terminal performance;
- When uncertainty is high or the candidate is outside the applicability domain, apply a penalty, request review, or reject it;
- When multi-objective conflicts are significant, prioritize retaining Pareto results.

---

## 7. Workflow

Default process:

```text
Read upstream files → Fuse and rank metrics → Experts confirm scenarios and roles
→ Register and test models → Define search space, constraints, and Reward
→ Small-scale trial run → Expert review → Formal generation, screening, or optimization
→ Analyze results, adjust parameters, and output feedback
```

```yaml
workflow:
  workflow_id: "WF-001"
  status: "draft|ready|running|paused|completed|failed"
  search_space: {definition: "", allowed_regions: [], forbidden_regions: [], expert_rules: []}
  nodes:
    - node_id: ""
      action: "load|generate|predict|calculate|check|score|select|optimize|review|export"
      model_id: ""
      inputs: []
      outputs: []
      retry_policy: ""
      stop_on_failure: true
  budget: {max_candidates: null, max_evaluations: null, max_runtime: "", compute_limit: ""}
  stopping_conditions: []
```

Before formal execution, a small-scale test must be performed for inputs and outputs, units, missing values, constraint triggering, and Reward direction.

---

## 8. Parameter Adjustment Interface

```yaml
parameter_control:
  parameter_id: "PARAM-001"
  target: "model|generator|optimizer|reward|constraint|workflow"
  name: ""
  current_value: null
  allowed_range: []
  allowed_values: []
  adjustment_mode: "manual|expert_approved_auto|fixed"
  trigger: ""
  max_change_per_round: null
  rollback_value: null
  change_history: []
```

Within expert-approved boundaries, parameters for training, generation, search, soft constraints, Reward weights, and computational budgets may be adjusted.

Automatic model-parameter adjustment must additionally satisfy all of the following: `executable_interface_exposed: true`, `parameter_interface_exposed: true`, `access_level: adjust_parameters`, and the target parameter must be included in `authorized_parameters` and within `allowed_range/allowed_values`. If any condition is not met, the process must automatically downgrade to a manual recommendation or fixed-parameter execution.

Do not automatically modify scientific-objective definitions, unapproved hard constraints, forbidden regions, metric directions, critical safety thresholds, model applicability domains, original data, original models, or production scripts.

Each adjustment must record the old value, new value, reason, triggering signal, result, and rollback status.

---

## 9. Expert Feedback

Supported actions: `approve | revise | reject | request_evidence | request_test | pause | resume`

```yaml
expert_feedback:
  feedback_id: "FB-001"
  target_type: "metric|threshold|model|reward|constraint|parameter|workflow|result"
  target_id: ""
  action: ""
  expert_role: ""
  comments: ""
  requested_changes: []
  evidence_refs: []
  timestamp: ""
  applied_in_version: ""
```

Expert modifications must not overwrite old versions. Conflicting opinions must be retained side by side and added to the review queue. Modifications that affect an active workflow must trigger another small-scale test and may trigger metric re-ranking, model replacement, parameter rollback, or re-optimization.

### 9.1 Dual-Expert Activity Records

In addition to feedback objects, the actual contributions and interventions of two types of experts in execution orchestration must also be recorded:

```yaml
expert_activity:
  activity_id: "EA-001"
  expert_role: "domain_expert|computer_expert"
  action_type: "provide|define|rank|constrain|recommend|configure|approve|revise|test|pause|resume"
  target_type: "metric|threshold|search_space|model|script|reward|parameter|workflow|result"
  target_id: ""
  contribution: ""
  decision_or_effect: ""
  evidence_refs: []
  timestamp: ""
  status: "recorded|applied|pending|reverted"
```

- The **domain-expert view** records scientific-objective interpretations, metric priorities, threshold rationales, feasible spaces, constraints, forbidden regions, mechanistic judgments, and interventions concerning the scientific reasonableness of results;
- The **computer-expert view** records model and data selection, script and server locations, input/output interfaces, environments and versions, validation plans, adjustable parameters, optimization strategies, and run-failure handling;
- Metrics, Reward weights, constraints, or strategies jointly confirmed by both types of experts must retain separate activity records for each expert. Conflicting opinions must not be merged into false consensus;
- `execution_orchestration_report.md` must contain two subsections, “Domain-Expert View” and “Computer-Expert View,” separately summarizing their contributions, decisions, interventions, unresolved issues, and effects on the current workflow.

---

## 10. Checks and Stopping

Before execution, confirm that: metrics have been fused; activated metrics have roles, directions, conditions, and evaluators; hard constraints do not conflict; model exposure and access levels have been confirmed; executable model interfaces have been tested; Reward directions are correct; automatically adjustable parameters have boundaries and rollback values; and the workflow has a budget and stopping conditions.

Pause execution when any of the following occurs:

- The main objective, hard constraints, or thresholds contain unresolved conflicts;
- Units, conditions, or sample granularity cannot be confirmed;
- Model outputs cannot be mapped to metrics;
- Predictions are outside the applicability domain or uncertainty is unacceptable;
- Reward direction is opposite to the scientific objective;
- Parameter adjustments exceed the permitted range;
- Model, script, or environment versions cannot be traced;
- Experts pause or reject a critical object;
- The budget or stopping conditions are reached without valid improvement.

---

## 11. Minimum Output Structure

### `execution_orchestration.yaml`

```yaml
metadata: {}
upstream_inputs: {}
execution_context: {}
metric_candidates: []
metric_decisions: []
model_interfaces: []
reward_components: []
workflow: {}
parameter_controls: []
expert_feedback_history: []
expert_activity_log: []
run_history: []
version_history: []
```

### `execution_review_queue.yaml`

```yaml
review_items:
  - issue_id: "EO-ISSUE-001"
    category: "metric|threshold|model|reward|constraint|parameter|workflow|evidence"
    question: ""
    affected_ids: []
    recommendation: ""
    evidence_refs: []
    required_expert: ""
    priority: "low|medium|high|critical"
    blocking: false
    status: "open|resolved|deferred"
```

### `execution_orchestration_report.md`

Must include: input status; metric fusion and ranking; final objectives, constraints, and thresholds; model exposure and access status; models and interfaces; Reward and workflow; parameters and run results; Domain-Expert View; Computer-Expert View; expert feedback, unresolved issues, and recommendations for the next round.

---

## 12. Behavioral Guidelines

- Inherit upstream information without binding to a specific case;
- Prioritize semantic fusion and retain uncertainty when information is missing;
- Metric rankings must have supporting reasons, and final decisions may be modified by experts;
- Maintain explicit links among metrics, thresholds, models, Rewards, and parameters;
- Invoke, test, and replace models through unified interfaces, and explicitly record model exposure level and human authorization;
- Automatic adjustment must be based on an executable interface, a parameter interface, and explicit authorization, and must include boundaries, records, and rollback;
- Record the contributions, decisions, and interventions of domain experts and computer experts separately and form a dual-expert view;
- Strictly distinguish predicted, proxy, computed, and experimental results;
- Non-critical missing information does not block execution; critical conflicts enter the expert queue;
- Formal execution must be reproducible, pausable, revisable, and reversible.
