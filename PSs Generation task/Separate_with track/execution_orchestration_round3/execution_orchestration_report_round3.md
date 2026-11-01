# Scientific Execution Orchestration — Round 3

## 1. Scope and authorization status

Round 3 updates the Round 2 workflow after the computer scientist selected three metrics:

1. **E(S1)−E(T1)** / ST gap;
2. **charge**;
3. **symmetry**.

The cloned SDPD repository was inspected at `/Users/jimmmmmies/Desktop/alignment/SDPD/`. The proposal below maps these metrics to the repository’s existing predictor and scoring contracts, improves the execution workflow, and identifies the files that would be changed or generated after confirmation.

**Authorization boundary:** this round does not execute SDPD. No `python` training/prediction/RL command, dependency installation, checkpoint replacement, sampling run, or model modification was performed. The workflow remains `selected_metrics_confirmed_procedure_requires_authorization`.

## 2. Verified SDPD interface map

| Function | Verified path | Role in proposed procedure | Status |
|---|---|---|---|
| Agent contract | `SDPD/AGENT_INTERFACE_EN.md` | Defines path conventions, model registry, output contracts, and JSON/YAML parameter rules | Read-only inspected |
| RL configuration | `SDPD/configs/rl_configs.json` | Primary JSON interface for actor/critic, scaffold, RL budget, scoring weights, predictor checkpoint, and output directory | Read-only inspected; not modified |
| RL entrypoint | `SDPD/data_preparation/run_rl.py` | Executes sampling → scoring → DAP update → diversity-memory export | Proposal only; not run |
| Runtime predictor profile | `SDPD/data_preparation/prediction_model/rl_compatible_2025/` | Three-output S1/T1/ST-gap predictor profile | Existing contract; not run |
| Predictor training entrypoint | `SDPD/data_preparation/prediction_model/rl_compatible_2025/main.py` | Trains the three-output KA-GNN if retraining is approved | Proposal only; not run |
| Predictor config | `SDPD/data_preparation/prediction_model/rl_compatible_2025/config/c_path.yaml` | YAML interface for KA-GNN architecture/training parameters | Read-only inspected; not modified |
| Predictor input data | `SDPD/data_preparation/prediction_model/rl_compatible_2025/data/dft.csv` | S1/T1/ST-gap training data contract | Not changed |
| Predictor graph cache | `SDPD/data_preparation/prediction_model/rl_compatible_2025/data/processed/dft.pth` | Processed graph/split cache | Not changed |
| Runtime predictor checkpoint | `SDPD/data_preparation/prediction_model/pretrained_models/best.pth` | Runtime KA-GNN checkpoint loaded by the scoring wrapper | Read-only; never edit directly |
| RL actor/critic startup checkpoint | `SDPD/pretrained_models/rl/best.pt` | Actor initialization and frozen critic/prior | Read-only; never edit directly |
| Scoring orchestration | `SDPD/data_preparation/scoring_strategy/standard_strategy.py` | Joins scaffold/decorations, calls `multiple_score`, applies diversity filter | Read-only inspected |
| Metric scoring implementation | `SDPD/data_preparation/scoring_strategy/score_function.py` | Exposes `st_gap`, `charge_score`, and `symmetry_score` components | Read-only inspected |
| RL output directory | `SDPD/rl_runs/` | Configured output root; runner writes `diversity_memory.csv` | No run performed |

### Existing metric contract

The local `multiple_score` implementation returns these primary components:

- `st_gap`: normalized predicted ST gap, derived from the KA-GNN raw score using `1 / (1 + gap / scale)`;
- `charge_score`: current implementation-specific formal-charge heuristic;
- `symmetry_score`: decoration-pair similarity/repetition heuristic.

The current `SDPD/configs/rl_configs.json` contains `weights: [0.1, 0.3, 0.6]`. The code enumerates primary components in the order `st_gap`, `charge_score`, `symmetry_score`, so the current mapping is:

| Component | Current weight | Proposed interpretation |
|---|---:|---|
| `st_gap` / E(S1)−E(T1) | 0.1 | Selected photophysical objective, but currently underweighted relative to symmetry; confirm whether this is intentional. |
| `charge_score` / charge | 0.3 | Selected conditional targeting/solubility descriptor; current heuristic must be validated for the intended charge state. |
| `symmetry_score` / symmetry | 0.6 | Selected scaffold/decorating symmetry preference; current high weight may dominate the reward and needs expert confirmation. |

This mapping is a repository fact, not an endorsement of the weights. The Round 3 improvement is to make the mapping and its assumptions explicit before execution.

## 3. Proposed metric configuration

### 3.1 E(S1)−E(T1)

Use the three-output KA-GNN runtime profile because its documented output contract is `0 = S1`, `1 = T1`, and `2 = ST Gap`. The predictor checkpoint is `SDPD/data_preparation/prediction_model/pretrained_models/best.pth`, and its source profile is `SDPD/data_preparation/prediction_model/rl_compatible_2025/`.

The runtime score is a **predictive surrogate**, not a new quantum-chemical calculation and not direct evidence of ΦΔ, ROS rate, or phototoxicity. The procedure must record raw ST-gap predictions, normalized scores, model checkpoint path, profile configuration, invalid values, and out-of-domain warnings.

The initial direction is `minimize_gap_with_context`, implemented by the existing decreasing normalization. The exact target regime and whether a smaller gap is desirable for the selected mechanism must be approved; no universal gap threshold is introduced.

### 3.2 Charge

Retain charge as a selected conditional descriptor, but split its semantics into:

1. **formal-charge validity:** derived from the molecule’s explicit SMILES/protonation/counterion representation;
2. **targeting/application score:** an expert-defined function for the intended compartment and assay.

The current SDPD heuristic is not a general charge model: for one decoration it checks positive/negative atom charges; for multiple decorations it uses total formal-charge parity. This must be treated as an implementation proxy requiring materials/formulation review, not as a universal charge optimum or localization predictor.

Before execution, specify pH, protonation/tautomer policy, counterion treatment, and whether the reward should prefer neutral, ionic, zwitterionic, or a defined charge distribution.

### 3.3 Symmetry

Retain symmetry as a selected scaffold/decorator descriptor. The current implementation uses decoration fragment fingerprint identity and pair-pattern rules; it is not a general point-group symmetry calculation. The workflow must therefore label it `decoration_symmetry_proxy`, preserve the decoration string, and avoid calling it molecular point-group symmetry.

Before execution, specify whether the objective is exact repeated decoration, graph symmetry, conformer-aware point-group symmetry, or another materials-science definition. The proposed first execution uses the existing proxy only for compatibility testing, not as validated physical symmetry.

## 4. Improved proposed execution procedure

### Phase 0 — Confirmation gate; no execution before approval

The project owner must confirm the selected metric semantics, reward weights, scaffold list, output directory, checkpoint versions, and whether a dry-run/preflight is authorized. Until then, all commands in this report are documentation only.

### Phase 1 — Immutable snapshot and configuration copy

1. Record SDPD repository commit, Python/dependency environment, file checksums, and checkpoint paths.
2. Copy `SDPD/configs/rl_configs.json` to the Round 3 proposal/output area; do not edit the repository’s source configuration before approval.
3. Copy the selected predictor configuration to the proposal area for review. The active SDPD predictor still resolves its config relative to its own profile directory, so a reviewed copy must be explicitly reconciled before execution.
4. Confirm that actor/critic vocabularies and checkpoint architecture are compatible.

### Phase 2 — Metric preflight without RL

After confirmation, run only the smallest authorized evaluator test:

1. Check a fixed, reviewed SMILES fixture containing valid neutral, charged, zwitterionic, invalid, and repeated-decoration cases.
2. Verify predictor output shape and index mapping: S1, T1, ST Gap.
3. Verify that `multiple_score` returns `st_gap`, `charge_score`, `symmetry_score`, `st_gap_raw`, and ring penalty fields.
4. Verify component ordering, weight mapping, invalid-value handling, finite values, and no silent checkpoint substitution.
5. Save the preflight report and do not enter RL unless all checks pass.

### Phase 3 — Controlled RL pilot

Only after explicit approval of Phase 2:

1. Use the approved copied configuration, an approved porphyrin scaffold, and a small pilot budget.
2. Run from the SDPD repository root as required by `AGENT_INTERFACE_EN.md`; do not run the KA-GNN profile from the wrong directory.
3. Keep `n_steps`, `batch_size`, learning rate, DAP `sigma`, diversity settings, and weights fixed for the first pilot.
4. Record every candidate batch, raw/normalized metric component, combined reward, invalid molecule, ring penalty, diversity-memory change, and runtime failure.
5. Preserve the existing warning that `run_rl.py` writes `diversity_memory.csv` but does not automatically save the updated actor checkpoint. If an actor checkpoint is required, define and approve a separate export procedure before running.

### Phase 4 — Review and iteration

Review the pilot for metric dominance, invalid rate, charge-proxy behavior, symmetry-proxy collapse, ST-gap applicability, scaffold coverage, and reward saturation. Adjust only approved JSON/YAML parameters, record old/new values and rollback, and never edit `.pt`/`.pth` checkpoints directly.

## 5. Proposed output paths

All paths below are explicit and are **proposed destinations**, not evidence that the files have been generated:

| Artifact | Proposed path | Generation status |
|---|---|---|
| Round 3 report | `/Users/jimmmmmies/Desktop/alignment/execution_orchestration_round3/execution_orchestration_report_round3.md` | Generated now |
| Round 3 machine config | `/Users/jimmmmmies/Desktop/alignment/execution_orchestration_round3/execution_orchestration_round3.yaml` | Generated now |
| Round 3 review queue | `/Users/jimmmmmies/Desktop/alignment/execution_orchestration_round3/execution_review_queue_round3.yaml` | Generated now |
| Round 3 trace | `/Users/jimmmmmies/Desktop/alignment/execution_orchestration_round3/execution_trace_round3.jsonl` | Generated now |
| Proposed copied RL config | `/Users/jimmmmmies/Desktop/alignment/execution_orchestration_round3/proposed_sdpd_configs/rl_configs_round3.json` | Destination reserved; not copied/modified in this proposal |
| Proposed copied predictor config | `/Users/jimmmmmies/Desktop/alignment/execution_orchestration_round3/proposed_sdpd_configs/c_path_round3.yaml` | Destination reserved; not copied/modified in this proposal |
| Preflight report | `/Users/jimmmmmies/Desktop/alignment/execution_orchestration_round3/preflight_round3/preflight_report.json` | Not generated; requires confirmation |
| Preflight metric records | `/Users/jimmmmmies/Desktop/alignment/execution_orchestration_round3/preflight_round3/metric_records.jsonl` | Not generated; requires confirmation |
| Pilot RL output root | `/Users/jimmmmmies/Desktop/alignment/SDPD/rl_runs/round3_pilot/` | Not created or run |
| Pilot diversity memory | `/Users/jimmmmmies/Desktop/alignment/SDPD/rl_runs/round3_pilot/diversity_memory.csv` | Not generated; runner output if authorized |
| Pilot run log | `/Users/jimmmmmies/Desktop/alignment/SDPD/rl_runs/round3_pilot/run.log` | Not generated; proposed wrapper output |
| Optional actor checkpoint | `/Users/jimmmmmies/Desktop/alignment/SDPD/rl_runs/round3_pilot/actor_final.pt` | Not generated; requires separate checkpoint-export approval |

## 6. Confirmation requested

Before execution, confirm all of the following:

1. Use SDPD’s existing three-output `kagnn_3out` runtime profile for E(S1)−E(T1).
2. Treat charge and symmetry as the existing implementation proxies for the first preflight, or provide revised definitions.
3. Approve or revise the current weights `[0.1, 0.3, 0.6]`; they strongly favor symmetry over ST gap.
4. Approve the proposed copied-config and preflight output paths.
5. Authorize preflight only, or authorize the later RL pilot separately. This report requests confirmation and does not execute either stage.

## Dialogue-based status reconciliation (2026-10-31)

The current output states have been reconciled with the saved expert dialogue at the user's request. General knowledge acceptance, task inputs, selected metric roles, and the synthesizability requirement are recorded only within their supported scope. Existing disputes, unanswered review questions, missing protocols, numerical thresholds, route validation, model-validation gaps, and execution-authorization requirements remain explicit. No scientific values or execution permissions are newly certified, and the historical execution trace is unchanged. The scope and dialogue excerpts are recorded in the expert_feedback_reconciliation metadata of `execution_orchestration_round3.yaml`, `execution_review_queue_round3.yaml`.
