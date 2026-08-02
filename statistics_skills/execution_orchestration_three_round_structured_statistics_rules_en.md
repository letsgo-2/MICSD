# Structured Statistical Rules for Three Rounds of Execution Orchestration

Version: v1.1

## 1. Purpose

These rules are used to conduct consistent and reviewable structured statistics on multi-round outputs from the execution-orchestration agent, evaluating how the workflow evolves from candidate-solution design, through expert-feedback adjustments, and gradually converges into an executable solution connected to real models, scripts, and parameter interfaces.

These rules count only objects explicitly recorded in the outputs and do not infer unstructured information from natural-language descriptions. Model modules and interface parameters must be counted separately: the former indicates how many independent functional modules are included in the workflow, while the latter indicates how many configurable parameters these modules expose to humans or agents.

## 2. Input Files

By default, each round reads the following three fixed output files:

- `execution_orchestration_round{n}.yaml`
- `execution_orchestration_report_round{n}.md`
- `execution_review_queue_round{n}.yaml`

Where:

1. YAML is the primary data source for statistics;
2. The Markdown report is used to verify object meanings, round-by-round processes, and field semantics;
3. The review queue is used to assist in confirming unresolved statuses, but it is not included in the seven core statistics retained by these rules;
4. When YAML and the report are inconsistent, the locatable structured objects in YAML take precedence, and the discrepancy must be recorded.

## 3. Cross-Round Field Fusion Principles

Different rounds may use different field names. During statistics, fields must be fused by semantics rather than by a single field name:

| Statistical object | Preferred field | Acceptable semantically equivalent fields |
|---|---|---|
| Metrics | `metric_candidates` | `final_metrics`, or optimization metrics explicitly registered in the current round |
| Metric thresholds and scoring rules | `threshold` | `transformation`, `transform`, explicit discrete scoring rules, or complete calculation formulas |
| Weighted Reward components | `reward_profiles.*.components` | `reward_contract.weights_order`, or objectives or penalty terms with independent weights |
| Evidence objects | `evidence` | Structured evidence with an independent `evidence_id` or equivalent identifier |
| Model modules | `model_interfaces` | Registries of generative models, predictive models, computational modules, surrogate models, or constraint-checking modules |
| Interface-configurable parameters | `model_interfaces.*.parameters` | `current_rl_parameters`, or parameter slots exposed to humans or agents in model, scoring, or runtime configurations |
| Workflow stages | `execution_workflow.stages` | When Round 3 and similar rounds do not contain a `stages` field, count top-level execution modules |

Even if the same object appears repeatedly in both the report and YAML, it must be counted only once. Aliases, derived explanations, and different textual descriptions of the same metric must not be counted repeatedly.

## 4. Core Statistical Metrics

### 4.1 Number of Candidate Metrics

**Definition:** The number of independent metrics formally included in task modeling, ranking, screening, or the final optimization contract in the current round.

**Counting rules:**

- Round 1 and Round 2: count the entries in `metric_candidates`;
- Round 3: because the metrics have converged, count the entries in `final_metrics`;
- Aliases of the same metric count only once;
- Hard constraints, primary objectives, secondary objectives, and soft constraints may all be included;
- Names that appear only in narrative text and are not included in the structured metric list are not counted.

### 4.2 Number of Metrics with Explicit Thresholds or Scoring Rules

**Definition:** The number of metrics that already have explicit thresholds or complete scoring rules that can be directly judged, calculated, or encoded.

**Counting conditions:** A metric counts once if it satisfies any of the following conditions:

1. It has an explicit numerical threshold, numerical range, or Boolean gate;
2. It has a complete calculation formula;
3. It has explicit input conditions and a discrete output mapping;
4. Its scoring direction, boundaries, and transformation have all been determined and can be directly implemented.

**Not counted:**

- Only directional descriptions such as “maximize,” “minimize,” or “keep moderate”;
- Only “ranking” or “target range” without a range or complete calculation method;
- Rules explicitly marked as unresolved or awaiting expert definition and that cannot be directly executed;
- Heuristic rules that only provide the name of a scoring function but lack sufficient implementation information.

This is a strict definition, so this number may be smaller than the number of candidate metrics.

### 4.3 Number of Weighted Reward Components

**Definition:** The number of objective terms, reward terms, or penalty terms with independent weights in the current primary Reward.

**Counting rules:**

- Round 1 and Round 2: count the `components` in the current primary reward profile;
- Round 3: count `reward_contract.weights_order`;
- Hard gates without independent numerical weights are not counted;
- Inactive or deferred Reward branches are not counted;
- Additional gates without independent weights, such as ring-count penalties and duplicate penalties, are not counted;
- Even if the same metric appears in both the threshold table and the Reward, it counts as only one weighted component in this category.

### 4.4 Number of Evidence Objects

**Definition:** The number of independent structured evidence objects newly added or explicitly registered in the current round to support metrics, thresholds, model selection, or implementation judgments.

**Counting rules:**

- Count independent entries in the `evidence` array;
- Each independent `evidence_id` counts as 1;
- Upstream evidence that appears only as a reference and is not re-registered as an object in the current round is not counted again;
- The same paper, document, configuration, or code file may be counted separately when split into multiple evidence objects with different IDs and different source locations;
- General references in the report that are not included in the structured `evidence` list are not counted.

### 4.5 Number of Model Modules

**Definition:** The number of model modules in the current-round workflow that perform independent computational, generation, prediction, screening, or constraint functions.

**Counting rules:**

- Count models or computational modules in `model_interfaces` that perform independent functions;
- These may include generative models, predictive models, physics calculators, surrogate models, prior models, and constraint checkers;
- If the same module has both training and inference entry points but still performs the same function, count it only once;
- If the same checkpoint is shared across multiple roles, it may be counted as separate modules when its roles and functions in the workflow are different; if it is merely a repeated reference to the same function, count it only once;
- Configuration files, data files, output directories, runtime commands, and ordinary script locations are not counted as model modules;
- Both candidate modules and real implementation modules may be counted, but statuses such as `proposed|available|validated|active` should be retained to distinguish the design stage from the implementation stage.

This metric reflects the functional-module composition of the workflow, rather than the number of parameters or the degree of interface exposure.

### 4.6 Number of Interface-Configurable Parameters

**Definition:** The number of independent parameter slots exposed through structured interfaces by model modules to humans or agents for setting or adjustment.

**Counting rules:**

- Count configurable parameters directly related to model runtime, scoring, training, sampling, constraints, or optimization behavior;
- A parameter must have an explicit name and must be settable through a configuration file, function parameter, command-line argument, or another structured interface;
- Numerical values, Boolean values, enumeration values, mode names, model paths, and weights with explicit positional semantics may all be counted;
- Each parameter in an array with fixed positional semantics is counted separately; for example, three Reward weights count as 3;
- Per-sample data inputs such as `SMILES`, molecular graphs, and candidate lists are not configurable parameters;
- Paths used only for explanation, comments, status text, and implementation-behavior descriptions are not counted;
- Content that has only a suggested value but has not yet formed a settable interface may be marked as `proposed_parameter`, but it is not counted as an “actually configurable parameter”;
- If a parameter appears in the configuration but the current code does not read it, does not use it, or overrides it with a hard-coded value, it should be counted as an “exposed parameter” while also being marked as `ineffective`;
- It is recommended to report both:
  - `exposed_parameter_count`: the number of parameter slots declared in the structured interface;
  - `effective_parameter_count`: the number of parameters that can actually change model or workflow behavior in the current implementation.

**Definition used in this case:**

- Round 1: 7 proposed interface parameters;
- Round 2: 7 proposed interface parameters;
- Round 3: 23 exposed interface parameters, of which 20 are effective in the current implementation.

Fields not counted as parameters in Round 3:

- `config_file`: location of the configuration file;
- `model_path_runtime_behavior`: implementation-behavior description.

Parameters exposed in Round 3 but currently ineffective:

- `model_path_json`: the actual predictor checkpoint path is overridden by a hard-coded value in the code;
- `bucket_size`: currently read by the implementation but not used in screening behavior;
- `minsimilarity`: currently read by the implementation but not used in screening behavior.

### 4.7 Number of Workflow Stages

**Definition:** The number of top-level stages in the current-round execution workflow that have independent purposes, input actions, and outputs or state transitions.

**Counting rules:**

- When `execution_workflow.stages` exists, count its entries;
- When there is no `stages` field, count the top-level execution modules in `execution_workflow`, excluding metadata such as `status`;
- In Round 3, count the following separately:
  1. `preflight`
  2. `optional_predictor_training`
  3. `rl_execution`
  4. `post_run_expected`
- Steps, checks, and commands within a stage are not counted separately;
- Fields that only describe status or governance boundaries are not counted as stages.

## 5. Statistical Results for This Case

| Statistical metric | Round 1 | Round 2 | Round 3 |
|---|---:|---:|---:|
| Number of candidate/final metrics | 8 | 12 | 3 |
| Number of metrics with explicit thresholds or scoring rules | 4 | 2 | 3 |
| Number of weighted Reward components | 7 | 10 | 3 |
| Number of evidence objects | 4 | 7 | 3 |
| Number of model modules | 7 | 6 | 3 |
| Number of interface-configurable parameters | 7 | 7 | 23 (20 of which are effective) |
| Number of workflow stages | 6 | 5 | 4 |

## 6. Principles for Interpreting the Results of the Three Rounds

- The larger number of metrics, models, and stages in Round 1 indicates that the agent first established a candidate workflow covering the search space, constraints, physics-based evaluation, and reinforcement learning.
- The increase in candidate metrics and Reward components in Round 2 indicates that the agent responded to feedback from the materials expert by expanding and re-ranking computational metrics. The small number of explicit thresholds indicates that most project-specific thresholds were correctly retained for expert confirmation rather than being automatically filled in.
- The reduction in metrics, Reward components, and model modules in Round 3 indicates convergence of objectives after expert selection. At the same time, the number of interface-configurable parameters increased significantly and became connected to real configuration and code behavior, indicating that the workflow had transformed from conceptual recommendations into a reviewable runtime contract.
- A reduction in quantity does not mean a decline in capability. For later rounds, interpretation should incorporate interface binding, configuration clarity, and the executability of scoring rules.
- These statistics describe the orchestration structure and readiness for execution. They do not indicate that the model has already been trained, that the optimization process has already run, or that candidate-molecule performance has already been validated.

## 7. Quality Checks

After the statistics are completed, verify that:

- [ ] The corresponding YAML was read for every round;
- [ ] The same object in the report was not counted repeatedly;
- [ ] Round 3 `final_metrics` were mapped to metric statistics;
- [ ] Only the currently active Reward was counted, excluding deferred branches;
- [ ] Thresholds and scoring rules used a strict executable definition;
- [ ] Model modules were counted by independent function, without mistakenly counting configuration files, scripts, or output directories as models;
- [ ] Interface parameters counted only settable parameter slots, without mistakenly counting per-sample inputs as parameters;
- [ ] The exposed status and actual effective status of interface parameters were distinguished;
- [ ] Weight arrays were counted separately by elements with fixed positional semantics;
- [ ] Internal steps were not repeatedly counted as workflow stages;
- [ ] Statistical results can be located and verified from the original fields;
- [ ] “An execution command has been proposed” was not incorrectly written as “it has already been executed.”

## 8. Recommended Output Format

Subsequent statistical programs or manual statistics should output:

```yaml
round_statistics:
  - round: 1
    candidate_metrics: 8
    metrics_with_executable_threshold_or_score: 4
    weighted_reward_components: 7
    evidence_objects: 4
    model_modules: 7
    exposed_interface_parameters: 7
    effective_interface_parameters: null
    workflow_stages: 6
```

For each additional round, add another object with the same structure to the array so that a cross-round table can be generated directly.
