# Scientific Execution Orchestration Report - Round 3

Generated: 2026-07-25  
Input stage: execution orchestration round 2 plus `SDPD/AGENT_INTERFACE.md`  
Status: **configuration and workflow proposal only; no SDPD training, prediction, or RL run was executed**.

## 1. Final Objective and Scope

The computer scientist has selected exactly three optimization metrics for the current RL workflow:

1. `ES1-ET1`: the predicted S1-T1 energy gap, implemented by SDPD as the `ST Gap` predictor output and `st_gap_score` reward component;
2. `charge`: implemented as `charge_score` from the decoration/formal-charge rules;
3. `symmetric`: implemented as `symmetry_score` from the decoration-pair reward.

The existing molecular-generation assumptions remain active:

- representation: SMILES;
- scaffold/decorations: scaffold-conditioned DecoratorModel;
- domain scaffold: porphyrin-like scaffold supplied through `configs/rl_configs.json`;
- optimization: DAP reinforcement learning;
- runtime predictor: three-output KA-GNN-compatible profile;
- source repository: `/Users/jimmmmmies/Desktop/alignment/SDPD`.

This round does not alter SDPD source code or configuration files. It records the intended configuration and the exact procedure to run after explicit confirmation.

## 2. SDPD Interface Findings

The interface document and current files establish the following implementation contract.

| Component | Current path | Role | Round3 relevance |
|---|---|---|---|
| RL configuration | `configs/rl_configs.json` | Main JSON parameter entrypoint | Contains the three final metric weights and output directory. |
| RL entrypoint | `data_preparation/run_rl.py` | DAP actor update and sampling loop | Must be launched from repository root. |
| Actor checkpoint | `pretrained_models/rl/best.pt` | Trainable actor initialization | Must match critic vocabulary and network structure. |
| Critic checkpoint | `pretrained_models/rl/best.pt` | Frozen prior/critic initialization | Current config uses same checkpoint as actor. |
| Runtime predictor | `data_preparation/prediction_model/rl_compatible_2025/` | Three-output KA-GNN profile | Outputs S1, T1, ST Gap. |
| Predictor checkpoint used at runtime | `data_preparation/prediction_model/pretrained_models/best.pth` | KA-GNN weights | Predictor wrapper currently hard-codes this path; JSON `model_path` alone does not switch it. |
| Predictor training config | `data_preparation/prediction_model/rl_compatible_2025/config/c_path.yaml` | Three-output predictor training parameters | Current `ka_gnn`, `dft`, MMFF, CGCNN, 4 layers, LR 0.0001, 501 epochs, batch 128, 80/10/10 split. |
| Predictor training CSV | `data_preparation/prediction_model/rl_compatible_2025/data/dft.csv` | S1/T1/ST Gap training data | Must match the checkpoint and graph cache. |
| Predictor graph cache | `data_preparation/prediction_model/rl_compatible_2025/data/processed/dft.pth` | Processed graphs and split | Must be invalidated if CSV, features, force field, or split changes. |
| RL output | `rl_runs/<timestamp>/diversity_memory.csv` | Saved high-scoring novel molecules | The current RL runner does not automatically save an updated actor checkpoint. |

## 3. Exact Metric Mapping

The order of the `weights` array is a stable SDPD interface and must not be changed:

```text
weights[0] = st_gap_score       -> ES1-ET1 objective
weights[1] = charge_score       -> charge objective
weights[2] = symmetry_score     -> symmetric objective
```

The current configuration is:

```json
"weights": [0.1, 0.3, 0.6]
```

Therefore, the current effective priority is:

1. `symmetric`: 0.6
2. `charge`: 0.3
3. `ES1-ET1`: 0.1

This is the **implemented reward priority**, not a new recommendation invented in this round. It is explicitly documented in `AGENT_INTERFACE.md` and should be treated as the computer scientist’s active selection unless they request new weights.

### 3.1 ES1-ET1 / ST-gap score

SDPD computes:

```text
gap_nonnegative = max(KA_GNN_ST_gap, 0)
st_gap_score = 1 / (1 + gap_nonnegative / scale)
```

Current `scale` is `1.0`. A failed prediction produces `NaN`, which becomes the configured `invalid_value=0.0` in the final component. Because this transformation monotonically favors smaller non-negative predicted gaps, the RL reward currently optimizes **smaller ES1-ET1** values.

### 3.2 Charge score

For a single decoration:

- both positive and negative formal charges: `1.0`;
- only positive or only negative formal charges: `0.5`;
- no formal charge: `0.0`.

For multiple decorations:

- total molecular formal charge equal to zero: `0.0`;
- non-zero even total formal charge: `1.0`;
- non-zero odd total formal charge: `0.5`.

This is a discrete project-specific reward, not a continuous physical charge descriptor.

### 3.3 Symmetric score

The symmetry component uses the decoration-pair reward in `score_function.py`, with radius-2, 2048-bit Morgan fingerprints and position-pair rules for 3, 4, 6, and 8 decorations. It can return `0.0`, `0.25`, `0.5`, or `1.0`.

The input decoration separator contract is `|` and must not be changed without updating the scorer and its tests.

## 4. Current Total Reward and Gates

With `weights=[0.1,0.3,0.6]`, the current base reward is:

```text
base_reward =
    (0.1 * st_gap_score
   + 0.3 * charge_score
   + 0.6 * symmetry_score) / 1.0
```

The current runtime also applies:

- any decoration with more than 3 RDKit rings: total reward becomes `0`;
- duplicate canonical SMILES in the current batch or diversity memory: reward becomes `0`;
- only new molecules with final reward `>= 0.77` enter diversity memory;
- `bucket_size=25` and `minsimilarity=0.4` are parsed but are not used by the current `NoFilterWithPenalty` implementation.

## 5. Model and Parameter Registry

### 5.1 Current RL configuration

The current `configs/rl_configs.json` values are:

| Parameter | Current value | Meaning |
|---|---|---|
| `actor` | `./pretrained_models/rl/best.pt` | Trainable actor initialization |
| `critic` | `./pretrained_models/rl/best.pt` | Frozen critic/prior initialization |
| `n_steps` | `1000` | RL steps |
| `learning_rate` | `0.0001` | Actor Adam learning rate |
| `batch_size` | `128` | Sampling batch size; single-scaffold compatibility logic splits this into two groups of 64 |
| `randomize_scaffolds` | `false` | Scaffold randomization disabled |
| `output_dir` | `./rl_runs` | Timestamped RL output root |
| `learning_strategy.name` | `dap` | Direct Augmented Likelihood |
| `learning_strategy.parameters.sigma` | `120` | Reward strength in DAP augmented NLL |
| `use_kan` | `true` | Use KA-GNN scoring branch |
| `weights` | `[0.1, 0.3, 0.6]` | ST gap, charge, symmetry in that order |
| `scale` | `1.0` | ST-gap normalization scale |
| `invalid_value` | `0.0` | Score used after prediction failure |
| `minscore` | `0.77` | Diversity-memory insertion threshold |
| W&B | `project=molecule-rl`, `run_name=md-gd-baseline` | Logging metadata |

### 5.2 Predictor contract

The active three-output predictor contract is:

```text
index 0 = S1
index 1 = T1
index 2 = ST Gap = ES1-ET1
```

The extended ten-output predictor is **not** the active runtime contract for this round. It exposes additional heads but cannot be substituted into the current wrapper by changing only JSON, because the wrapper currently derives target dimensions and the checkpoint path with implementation-specific behavior.

### 5.3 Important checkpoint limitation

`KAGnnGapPredictor` currently hard-codes:

```text
./data_preparation/prediction_model/pretrained_models/best.pth
```

Changing `/scoring_strategy/scoring_function/model_path` in JSON does not switch the actual predictor weights. A checkpoint change therefore requires an explicit backup-and-replace operation or a source-code change to make the path configurable. This round does not perform either operation.

## 6. Confirmation-Only Run Procedure

The following is the intended procedure after the user confirms execution. It is documented here but has **not** been run.

### Step A — Preflight checks

Run from `/Users/jimmmmmies/Desktop/alignment/SDPD` and verify:

1. `pretrained_models/rl/best.pt` exists;
2. actor and critic use compatible vocabulary and network structure;
3. `data_preparation/prediction_model/pretrained_models/best.pth` exists;
4. the predictor checkpoint is compatible with the three-output wrapper;
5. the porphyrin scaffold attachment-point format matches the DecoratorModel vocabulary;
6. a CUDA-capable environment is available because current DecoratorModel/model code calls `.cuda()` explicitly;
7. JSON is valid with `python -m json.tool configs/rl_configs.json`;
8. the output directory is selected so the run does not overwrite a prior result.

### Step B — Optional predictor training or checkpoint replacement

This step is **not required** if the existing runtime checkpoint is approved. If retraining is requested, the documented command is:

```bash
cd data_preparation/prediction_model/rl_compatible_2025
mkdir -p data/processed
python main.py
cd ../../..
```

After expert review of the resulting checkpoint, the documented installation target is:

```text
data_preparation/prediction_model/pretrained_models/best.pth
```

The existing target must be backed up before replacement. No retraining or replacement was performed in this round.

### Step C — RL execution command

The documented RL command is:

```bash
python data_preparation/run_rl.py \
  --config configs/rl_configs.json \
  --seed 42
```

This command must be run from the SDPD repository root. It will create a timestamped output directory under `rl_runs/`, run the actor/critic DAP loop, and write `diversity_memory.csv` periodically and at completion.

## 7. Expected Output Paths

If the workflow is later confirmed and successfully run, expected outputs are:

| Output | Expected path |
|---|---|
| RL run directory | `/Users/jimmmmmies/Desktop/alignment/SDPD/rl_runs/<YYYYMMDD-HHMMSS>/` |
| High-scoring novel molecules | `/Users/jimmmmmies/Desktop/alignment/SDPD/rl_runs/<YYYYMMDD-HHMMSS>/diversity_memory.csv` |
| W&B artifacts | W&B location determined by configured mode and credentials |
| Predictor training cache | `/Users/jimmmmmies/Desktop/alignment/SDPD/data_preparation/prediction_model/rl_compatible_2025/data/processed/dft.pth` |
| Predictor training runs | `/Users/jimmmmmies/Desktop/alignment/SDPD/data_preparation/prediction_model/rl_compatible_2025/runs/` |
| Installed runtime predictor checkpoint | `/Users/jimmmmmies/Desktop/alignment/SDPD/data_preparation/prediction_model/pretrained_models/best.pth` |

No new run output path has been created by this round.

## 8. Recommended Execution Interpretation

The active workflow is not a generic three-objective physics optimizer. It is the SDPD implementation of:

```text
SMILES scaffold decoration
  -> KA-GNN ST-gap prediction
  -> discrete charge score
  -> discrete symmetry score
  -> weighted reward [0.1, 0.3, 0.6]
  -> ring and novelty penalties
  -> DAP actor update
```

The user should confirm whether the current weights are intended. If the intended priority is different, only the `weights` array should be changed after confirmation, preserving the stable order `[ES1-ET1, charge, symmetric]`. Do not reorder the array.

## 9. Known Limitations and Risks

- The current RL runner does not automatically save the updated actor checkpoint; `pretrained_models/rl/best.pt` remains the startup checkpoint.
- The current saved result contract is `diversity_memory.csv`; it is not a complete actor checkpoint or a full per-step molecule trajectory.
- The predictor JSON `model_path` is not authoritative because the wrapper hard-codes the checkpoint path.
- The current charge and symmetry scores are project-specific discrete rules, not general continuous molecular descriptors.
- The `ES1-ET1` reward is based on predicted ST Gap and rewards smaller non-negative gaps through the current formula; it is not direct experimental validation of photodynamic efficacy.
- The current `minscore=0.77` is a memory insertion threshold, not a scientifically validated performance threshold.
- Current prior/RL execution requires CUDA unless device handling is refactored and regression-tested.

## 10. Round3 Review Status

Round3 status: **ready for user confirmation, not executed**.

The only execution decision that remains is confirmation of the current runtime parameters, especially:

- whether `[0.1, 0.3, 0.6]` is the intended priority for `[ES1-ET1, charge, symmetric]`;
- whether the existing runtime predictor checkpoint is approved;
- whether W&B should remain enabled, be offline, or be disabled;
- whether a new timestamped output directory is acceptable.

## 11. Round3 Deliverables

Use `execution_orchestration_round3.yaml` as the machine-readable run plan and `execution_review_queue_round3.yaml` for the remaining confirmation questions. The original round1 and round2 artifacts remain unchanged.
