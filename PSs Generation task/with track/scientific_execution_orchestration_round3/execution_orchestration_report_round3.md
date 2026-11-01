# Scientific Execution Orchestration — Round 3

## 1. Status and authorization boundary
This is a confirmation-ready update based on Round 2 orchestration. The cloned repository is at `SDPD/`. The computer scientist selected `E(S1)-E(T1)`, charge, and symmetry. **No SDPD command, training, inference, smoke test, configuration edit, or checkpoint modification was run in this round.** `run_authorized` is explicitly `false`.

## 2. Repository and interface mapping
| interface_id | name | status | entrypoint | config | metric_mapping | authorization |
|---|---|---|---|---|---|---|
| IF-R3-001 | RL execution interface | existing_proposed_no_run | SDPD/data_preparation/run_rl.py | SDPD/configs/rl_configs.json | {"component_0": "st_gap", "component_1": "charge_score", "component_2": "symmetry_score"} | Do not execute in Round 3; command is recorded for confirmation only. |
| IF-R3-002 | Scoring configuration interface | existing_editable_json_proposed | SDPD/configs/rl_configs.json | SDPD/configs/rl_configs.json | "" | Do not edit the repository config in Round 3; proposed values are reported for confirmation. |
| IF-R3-003 | Three-output predictor interface | existing_checkpoint_proposed_for_smoke_test | SDPD/data_preparation/prediction_model/rl_compatible_2025/main.py | SDPD/data_preparation/prediction_model/rl_compatible_2025/config/c_path.yaml | {"0": "S1", "1": "T1", "2": "ST Gap"} | Do not run in Round 3; smoke test requires confirmation. |
| IF-R3-004 | Charge and decoration-symmetry scorer | existing_source_level_interface_proposed_for_confirmation | SDPD/data_preparation/scoring_strategy/score_function.py::multiple_score | SDPD/configs/rl_configs.json | "" | No source modification or execution in Round 3. |


The current SDPD runtime path is: `run_rl.py` → `StandardScoringStrategy` → `multiple_score` → KA-GNN ST-gap predictor plus charge and decoration-symmetry rules. The current JSON configuration uses weights `[0.1, 0.3, 0.6]`, corresponding to ST-gap, charge, and symmetry in the scorer's component order. This mapping must be smoke-tested after authorization.

## 3. Selected metrics and current semantics
| metric_id | canonical_runtime_name | role | current_runtime_support | current_semantics | threshold | status |
|---|---|---|---|---|---|---|
| E(S1)-E(T1) | st_gap | primary_selected_metric | partial_existing | KA-GNN predicts raw ST gap; runtime normalizes as 1/(1 + max(raw_gap,0)/scale), with scale from scoring config and default 1.0. | No new hard threshold activated in Round 3; retain the Round 2 <0.4 eV ISC heuristic as scientific context only, not an SDPD runtime gate. | proposed_pending_confirmation |
| charge | charge_score | selected_structure_or_objective_metric | existing | For one decoration, both positive and negative atom charges score 1.0, one nonzero sign scores 0.5, and no nonzero atom charge scores 0.0. For multiple decoration parts, total formal charge 0 scores 0.0, even formal charge scores 1.0, and odd nonzero charge scores 0.5. | Existing discrete thresholds are encoded in the scorer; no additional threshold should be invented before confirmation. | existing_but_pending_scientific_confirmation |
| symmetry | symmetry_score | selected_structure_or_objective_metric | existing_decoration_level | Scores symmetry of decoration fragments using exact/near-identical Morgan-fingerprint grouping rules; the implementation is not a general 3D molecular point-group symmetry descriptor. | Current reward is rule-based (0, 0.25, 0.5, or 1.0 depending on decoration grouping); no external numeric symmetry threshold is activated. | existing_but_semantic_scope_requires_confirmation |


### Important semantic clarification
The selected `symmetry` metric is not a general molecular point-group symmetry descriptor. In SDPD it is a **decoration symmetry score** computed from Morgan-fingerprint grouping rules across decoration fragments. The selected `charge` metric is also a project-specific discrete heuristic, not a universal target for formal charge. These definitions are preserved for confirmation rather than silently replaced.

## 4. Proposed execution procedure for confirmation
| step | name | action | command | expected_output |
|---|---|---|---|---|
| 0 | Confirmation gate | Obtain explicit authorization to run any SDPD command or edit any SDPD JSON/YAML/Python file. | None | Authorization record; otherwise stop with no execution. |
| 1 | Repository integrity check | Inspect git status and record commit/repository version without modifying files. | cd SDPD && git status --short && git rev-parse HEAD | Clean/known baseline and commit hash. |
| 2 | Configuration validation | Validate the selected RL JSON and confirm paths/checkpoints exist. | python -m json.tool SDPD/configs/rl_configs.json | Valid JSON; no training or inference. |
| 3 | Predictor smoke test | Run a minimal, separately logged predictor test on a tiny approved SMILES set and verify output index 2 is ST Gap. | cd SDPD/data_preparation/prediction_model/rl_compatible_2025 && python main.py | Only after authorization: checkpoint loads, output contract and units are recorded. |
| 4 | Scorer smoke test | Evaluate the scorer on valid/invalid SMILES and decoration cases; verify st_gap, charge_score, symmetry_score, weighted total and invalid fallback. | cd SDPD && python -c '<approved scorer smoke-test command to be supplied after authorization>' | Only after authorization: metric mapping and reward directions verified. |
| 5 | RL dry-run/small budget | Run the smallest authorized RL budget with W&B disabled, fixed seed, separate output directory, and actor checkpoint preservation. | cd SDPD && python data_preparation/run_rl.py --config configs/rl_configs.json --seed 42 | Only after authorization: timestamped diversity_memory.csv and component logs. |
| 6 | Post-run audit | Inspect raw ST gap, charge, symmetry, validity, diversity, scaffold retention and checkpoint behavior; do not overwrite baseline artifacts. | not specified; audit scripts to be confirmed | Run report and expert review package. |


### Procedure conditions
- Step 0 is a hard gate: no later step may run without explicit authorization.
- Preserve the Round 2 config and checkpoints; write any authorized experiment to a separate timestamped output directory.
- Validate JSON before use; do not edit binary `.pt` or `.pth` checkpoints.
- Run predictor and scorer smoke tests before any RL loop.
- Confirm that output index 2 is ST Gap, that component order is `[st_gap, charge_score, symmetry_score]`, and that invalid values follow the configured fallback.
- Disable W&B unless explicitly enabled; preserve raw component scores and `st_gap_raw`.
- The proposed RL command is recorded only; it was not executed.

## 5. Configuration and model information update
### Existing SDPD configuration
`SDPD/configs/rl_configs.json` currently specifies actor/critic `./pretrained_models/rl/best.pt`, one porphyrin-like scaffold, `n_steps=1000`, `batch_size=128`, `learning_rate=0.0001`, DAP `sigma=120`, KA-GNN enabled, weights `[0.1, 0.3, 0.6]`, scale `1.0`, invalid fallback `0.0`, and predictor checkpoint `./data_preparation/prediction_model/pretrained_models/best.pth`.

### Proposed Round 3 interface update
No repository file is modified in Round 3. The proposed configuration retains the existing selected-metric order and weights, adds a confirmation run name, and requires W&B disabled until authorization. The exact proposed values are recorded in `execution_orchestration_round3.yaml` under `IF-R3-002`.

### Independently identified interface discrepancy
`AGENT_INTERFACE_EN.md` describes a configurable predictor model path, but `data_preparation/prediction_model/kagnn_gap_predictor.py` currently assigns a hard-coded `./data_preparation/prediction_model/pretrained_models/best.pth` path in the inspected source. This is recorded as a blocking review item; no fix was applied.

## 6. Workflow improvements from Round 2
1. Replace abstract proposed model entries with repository-specific paths and output contracts.
2. Add a pre-RL checkpoint/output-contract smoke test.
3. Add an explicit scorer semantic test for charge and decoration symmetry.
4. Preserve raw `st_gap_raw`, normalized ST-gap, charge score, symmetry score, validity, diversity and checkpoint behavior in the audit record.
5. Separate repository inspection, predictor smoke test, scorer smoke test, and RL execution into independently authorized stages.
6. Keep the workflow paused when the checkpoint path, output contract, metric semantics, or weight order is uncertain.

## 7. Domain-expert and computer-expert views
### Domain-expert view
The domain expert must confirm whether the current charge heuristic and decoration symmetry are scientifically intended for porphyrin candidate generation. In particular, the scorer's preference for both positive and negative atom charges in the single-decoration case and its grouping-based symmetry reward should not be treated as general chemical laws.

### Computer-expert view
The computer expert receives a concrete SDPD path map and a three-component runtime contract. The RL actor/critic, DAP strategy, KA-GNN predictor, scorer, configuration, output directory and checkpoint locations are identified. The computer expert must confirm component order, checkpoint compatibility, JSON values, W&B policy, and whether the actor checkpoint is preserved after a run.

## 8. Blocking review queue
See `execution_review_queue_round3.yaml`. The primary blockers are explicit execution authorization, checkpoint/output compatibility, charge and symmetry semantic confirmation, weight approval, and the hard-coded predictor-path discrepancy.

## 9. Output paths
- Report: `scientific_execution_orchestration_round3/execution_orchestration_report_round3.md`
- Machine-readable orchestration: `scientific_execution_orchestration_round3/execution_orchestration_round3.yaml`
- Review queue: `scientific_execution_orchestration_round3/execution_review_queue_round3.yaml`
- Execution trace: `scientific_execution_orchestration_round3/execution_trace_round3.jsonl`
- Source repository inspected but not modified: `SDPD/`

## 10. Confirmation requested
Please confirm the proposed procedure and, separately, authorize any desired execution stage. Until explicit authorization is provided, the SDPD RL command remains unexecuted and all Round 3 model statuses remain proposed.