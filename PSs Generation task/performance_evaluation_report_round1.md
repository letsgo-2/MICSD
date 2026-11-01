# Scientific Performance Evaluation Report - Round 1

Generated: 2026-07-25  
Stage: performance evaluation after knowledge alignment round2 and execution orchestration round3  
Status: workflow, parameter, statistics, and plotting plan only. No new RDKit, ORCA, SDPD, Slurm, or statistical run has been executed in this round.

## 1. Input Scope

This round uses the following upstream files as its fixed evidence base:

| Source group | Files | Role in this evaluation plan |
|---|---|---|
| Knowledge alignment round2 | `knowledge_alignment_round2_report.md`, `knowledge_alignment_round2.yaml`, `expert_review_queue_round2.yaml` | Defines advantaged photosensitizer scaffolds, DFT/TD-DFT descriptors, threshold logic, expert questions, and mechanism-specific caveats. |
| Execution orchestration round3 | `execution_orchestration_report_round3.md`, `execution_orchestration_round3.yaml`, `execution_review_queue_round3.yaml` | Defines the active SDPD reward contract, RL configuration, model/checkpoint interface, run status, and unresolved execution confirmations. |
| SDPD repository | `SDPD/` | Provides the molecular generator, KA-GNN predictor, RL configuration, existing `rl_runs/` output schema, and drawing/analysis locations. |

The most important boundary condition is that execution orchestration round3 explicitly records: **no SDPD training, prediction, or RL run was executed in that round**. Therefore this report defines how performance should be computed once candidate molecules and DFT outputs exist; it does not invent molecular performance results.

## 2. Evaluation Objects

The current evaluation should treat the following as primary objects:

| Object | Source | Evaluation role |
|---|---|---|
| Generated candidate molecules | `SDPD/rl_runs/<timestamp>/diversity_memory.csv` after an approved RL run | Main molecular candidates for RDKit, ORCA, and statistical evaluation. |
| Existing example candidates | `SDPD/rl_runs/20251014-113340/diversity_memory.csv` | Historical/example data source suitable for dry-run parser and plotting-script validation only, unless experts approve it as a formal baseline. |
| SDPD reward model | `SDPD/configs/rl_configs.json` plus `data_preparation/run_rl.py` scoring contract | Model-level performance object: reward coverage, novelty gate, score distribution, and alignment with photophysical objectives. |
| KA-GNN ST-gap predictor | `SDPD/data_preparation/prediction_model/pretrained_models/best.pth` | Runtime proxy model producing S1, T1, and ST Gap; must be compared against ORCA recalculation for selected candidates. |
| ORCA DFT/TD-DFT result set | New Slurm-generated output directory | Higher-cost computational chemistry evidence for absorption, oscillator strength, triplet energetics, SOC, redox, and derived descriptors. |

## 3. Active Metrics and Interpretation

The active SDPD RL reward from round3 is:

```text
base_reward = 0.1 * st_gap_score + 0.3 * charge_score + 0.6 * symmetry_score
```

where the stable component order is `[ES1-ET1, charge, symmetric]`. The implemented runtime priority is therefore symmetry first, charge second, and ES1-ET1 third.

The performance evaluation must separate three metric layers:

| Layer | Metrics | Use |
|---|---|---|
| SDPD runtime metrics | `st_gap`, `st_gap_raw`, `total_score`, `Step`, canonical SMILES novelty, ring penalty pass/fail | Evaluate the generator and reward behavior under the implemented RL contract. |
| RDKit descriptors | molecular validity, canonical SMILES, duplicates, formal charge, ring count, aromatic ring count, heavy atoms, exact molecular weight, cLogP, TPSA, rotatable bonds, HBA/HBD, QED, Morgan fingerprint diversity, Bemis-Murcko scaffold, optional symmetry proxy | Fast structural QC, aggregation-risk proxies, diversity statistics, and candidate triage before ORCA. |
| ORCA/DFT descriptors | optimized geometry status, TD-DFT excitation energies, absorption wavelength, oscillator strength, T1-S0 gap, minimum S1-Tn gap, SOC(S1,Tn), HOMO/LUMO, redox proxies, derived DeltaG_ET | Photophysical validation and model/predictor calibration for top candidates. |

The knowledge-alignment thresholds should be used as initial analysis rules, not as final validated performance claims:

| Descriptor | Initial decision rule |
|---|---|
| Absorption wavelength | 600-800 nm high-score window; 650-750 nm preferred initial PDT window. |
| Oscillator strength | Rank-normalized within scaffold; near-zero target-transition oscillator strength is penalized. |
| T1-S0 gap | Type-II branch: >0.98 eV favorable, >1.13 eV conservative oxygen threshold. Type-I EET-blocking branch: <0.98 eV may be favorable only if the mechanism branch is explicitly selected. |
| Minimum S1-Tn gap | <0.4 eV favorable ISC heuristic; must be interpreted with SOC. |
| SOC(S1,Tn) | Rank within locked method/scaffold; no universal absolute threshold. |
| DeltaG_ET | DeltaG_ET < 0 indicates thermodynamic feasibility; overly negative values are not automatically better. |
| Aggregation risk | Penalize planar hydrophobic macrocycles lacking bulky or ionic substituent compensation. |

## 4. End-to-End Workflow

### 4.1 Candidate Collection

1. Run the approved SDPD RL job from `SDPD/` after experts confirm the round3 review items: reward weights, runtime predictor checkpoint, CUDA availability, W&B mode, scaffold compatibility, and output path.
2. Store outputs under a new immutable directory such as `SDPD/rl_runs/<YYYYMMDD-HHMMSS>/`.
3. Use `diversity_memory.csv` as the first candidate table. Required columns are `SMILES`, `Scaffold`, `Step`, `st_gap`, `st_gap_raw`, and `total_score`.
4. Canonicalize SMILES with RDKit and generate `analysis_round1/candidates_clean_round1.csv`.

### 4.2 RDKit Fast Evaluation

For each candidate molecule:

1. Parse and sanitize the final `SMILES` field.
2. Generate canonical SMILES and remove duplicates.
3. Compute structural descriptors and rule flags.
4. Compute pairwise Morgan fingerprint distances and diversity summaries.
5. Select ORCA candidates by a transparent triage rule:

```text
ORCA shortlist = valid molecules
  AND total_score >= 0.77
  AND ring_penalty_pass == true
  AND duplicate_flag == false
  AND representative across score quantiles and scaffold/diversity clusters
```

Recommended first ORCA batch size is 20-50 molecules, depending on Slurm allocation and ORCA license/core limits.

### 4.3 ORCA DFT/TD-DFT Evaluation

Use a tiered protocol to balance cost and interpretability:

| Tier | Purpose | ORCA calculation |
|---|---|---|
| Tier 0 | Geometry preparation and failure screening | RDKit ETKDG conformers, MMFF94 pre-optimization, lowest-energy conformer export to XYZ. |
| Tier 1 | Ground-state geometry | `! B3LYP D3BJ def2-SVP CPCM(water) Opt TightSCF` for neutral/organic candidates; replace solvent if experts choose another medium. |
| Tier 2 | Absorption and oscillator strength | `! CAM-B3LYP def2-SVP CPCM(water) TightSCF` with `%tddft nroots 10 end` on the optimized geometry. |
| Tier 3 | Triplet and ISC proxies | TD-DFT/TDA triplet states with at least 10 roots; extract T1, S1, low-lying Tn, and compute `min(|S1-Tn|)`. |
| Tier 4 | SOC for top subset | ORCA SOC calculation for the top 5-15 candidates after Tier 2/3; rank SOC values only within the same method. |
| Tier 5 | Redox and Type-I thermodynamics | Single-point cation/anion energies or vertical redox estimates; derive Rehm-Weller-style DeltaG_ET after donor/acceptor/reference are fixed. |

Metal-containing candidates, especially Re(I), Gd, Cu, ZnPc-like systems, require expert-confirmed basis sets, ECPs, charge/multiplicity, and relativistic treatment before ORCA submission. Do not mix those outputs statistically with purely organic calculations unless the methods are explicitly harmonized.

### 4.4 Model-Performance Evaluation

Once ORCA values exist, evaluate the SDPD/KA-GNN model as a scientific proxy:

1. Match candidate canonical SMILES between `diversity_memory.csv`, RDKit descriptors, and ORCA summaries.
2. Compare `st_gap_raw` against ORCA-derived S1-T1 or selected ST-gap definition.
3. Report Pearson correlation, Spearman correlation, MAE, RMSE, signed bias, calibration slope, and Bland-Altman limits.
4. Stratify error by scaffold cluster, charge class, symmetry score, ring count, and molecular size.
5. Flag disagreement cases where SDPD ranks a molecule highly but ORCA violates the relevant photophysical threshold.

## 5. Required Tool Parameters

### 5.1 SDPD RL Parameters

Use the current round3 configuration unless experts change it:

| Parameter | Value |
|---|---|
| Repository root | `/Users/jimmmmmies/Desktop/alignment/SDPD` |
| Entry point | `python data_preparation/run_rl.py` |
| Config file | `configs/rl_configs.json` |
| Actor | `./pretrained_models/rl/best.pt` |
| Critic | `./pretrained_models/rl/best.pt` |
| Scaffold policy | Porphyrin scaffold from `configs/rl_configs.json` |
| Steps | `1000` |
| Batch size | `128` |
| Learning rate | `0.0001` |
| Learning strategy | `dap` |
| Sigma | `120` |
| Scoring weights | `[0.1, 0.3, 0.6]` for `[ES1-ET1, charge, symmetric]` |
| ST-gap scale | `1.0` |
| Invalid score | `0.0` |
| Diversity memory threshold | `minscore=0.77` |
| Output root | `./rl_runs` |

### 5.2 RDKit Parameters

Recommended Python environment packages:

```text
python>=3.10
rdkit
pandas
numpy
scipy
scikit-learn
matplotlib
seaborn
pyyaml
```

Descriptor settings:

| Parameter | Value |
|---|---|
| SMILES input column | `SMILES` |
| Canonicalization | `Chem.MolToSmiles(mol, canonical=True, isomericSmiles=True)` |
| Sanitization | RDKit default sanitization; failed molecules are excluded from ORCA and counted. |
| Morgan fingerprint | radius `2`, `2048` bits, Tanimoto similarity |
| Conformer generation | ETKDGv3, up to `50` conformers for ORCA shortlist |
| MMFF optimization | MMFF94 if parameters exist; otherwise UFF with explicit flag |
| Ring penalty check | maximum decoration ring count `<=3` aligned with SDPD runtime gate |
| Aggregation proxy inputs | cLogP, aromatic ring count, heavy atom count, formal charge, TPSA, planarity proxy where available |

### 5.3 ORCA Parameters

Recommended default for organic first-pass candidates:

```text
%pal nprocs 16 end
%maxcore 3000
! B3LYP D3BJ def2-SVP CPCM(water) Opt TightSCF
```

TD-DFT absorption calculation:

```text
%pal nprocs 16 end
%maxcore 3000
! CAM-B3LYP def2-SVP CPCM(water) TightSCF
%tddft
  nroots 10
  maxdim 5
end
```

Triplet/ISC proxy calculation:

```text
%pal nprocs 16 end
%maxcore 3000
! CAM-B3LYP def2-SVP CPCM(water) TightSCF TDA
%tddft
  triplets true
  nroots 10
end
```

Parameters requiring expert confirmation before production:

| Parameter | Default placeholder | Reason |
|---|---|---|
| Solvent model | `CPCM(water)` | PDT context often aqueous, but experimental medium may differ. |
| Functional for geometry | `B3LYP-D3BJ` | Reasonable first-pass geometry; not a final benchmark. |
| Functional for TD-DFT | `CAM-B3LYP` | Better long-range CT behavior than local/hybrid-only choices. |
| Basis set | `def2-SVP` first pass, `def2-TZVP` validation subset | Cost control vs higher-quality confirmation. |
| Number of roots | `10` singlet and `10` triplet roots | Needed for S1, target absorption, and S1-Tn screening. |
| Metal treatment | unset | Must be specified per element, oxidation state, ECP, and spin. |
| Charge/multiplicity | derived from RDKit/formal charge, reviewed manually | Incorrect charge/multiplicity invalidates all DFT values. |

### 5.4 Slurm Parameters

Recommended job-array template for ORCA first-pass calculations:

```bash
#!/bin/bash
#SBATCH --job-name=ps_orca_r1
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=24:00:00
#SBATCH --array=0-49%10
#SBATCH --output=logs/orca_%A_%a.out
#SBATCH --error=logs/orca_%A_%a.err

module purge
module load orca

INPUT_LIST=orca_inputs_round1/input_list.txt
INPUT=$(sed -n "$((SLURM_ARRAY_TASK_ID + 1))p" "$INPUT_LIST")
orca "$INPUT" > "${INPUT%.inp}.out"
```

Cluster-specific fields to replace: partition name, ORCA module name/path, wall time, memory, job-array limit, and scratch-directory policy.

## 6. Statistics Plan

Produce the following tables:

| Table | Contents |
|---|---|
| `candidate_qc_round1.csv` | Raw candidate count, valid RDKit count, duplicate count, ring-penalty failures, charge classes, score coverage. |
| `rdkit_descriptors_round1.csv` | One row per valid canonical molecule with SDPD scores and RDKit descriptors. |
| `orca_summary_round1.csv` | One row per completed ORCA calculation with convergence flags and extracted photophysical descriptors. |
| `model_calibration_round1.csv` | KA-GNN vs ORCA error statistics and rank-consistency metrics. |
| `shortlist_round1.csv` | Final candidate shortlist with evidence columns and reasons for inclusion/exclusion. |

Compute at minimum:

- Count, mean, standard deviation, median, interquartile range, min, max for continuous descriptors.
- Frequency tables for charge class, symmetry score, ring-penalty status, ORCA convergence status, and threshold pass/fail.
- Pearson and Spearman correlations among `total_score`, `st_gap`, `st_gap_raw`, RDKit descriptors, and ORCA descriptors.
- Bootstrap 95% confidence intervals for correlation and top-k enrichment when sample size permits.
- Top-k overlap between SDPD ranking and ORCA-derived ranking for `k=10`, `20`, and `50` if enough candidates exist.
- Error stratification by scaffold cluster, charge state, and molecular-size bins.

## 7. Plotting Script Plan

Create a plotting script at `analysis_round1/plot_performance_round1.py` after result tables exist. It should accept explicit file paths and never infer the latest run implicitly.

Planned CLI:

```bash
python analysis_round1/plot_performance_round1.py \
  --rdkit analysis_round1/rdkit_descriptors_round1.csv \
  --orca analysis_round1/orca_summary_round1.csv \
  --calibration analysis_round1/model_calibration_round1.csv \
  --outdir analysis_round1/figures_round1
```

Planned figures:

| Figure | Plot type | Scientific purpose |
|---|---|---|
| `score_distributions_round1.png` | Histogram/KDE of `total_score`, `st_gap`, `st_gap_raw` | Check SDPD reward spread and selection pressure. |
| `rdkit_qc_summary_round1.png` | Bar chart | Show validity, duplicates, ring penalties, charge classes. |
| `diversity_umap_round1.png` | UMAP or PCA on Morgan fingerprints | Visualize chemical diversity and scaffold clusters. |
| `score_vs_descriptors_round1.png` | Scatter matrix or selected scatter plots | Relate SDPD reward to cLogP, TPSA, molecular weight, ring count, formal charge. |
| `orca_absorption_round1.png` | Histogram plus threshold bands | Evaluate 600-800 nm and 650-750 nm absorption windows. |
| `s1_tn_soc_round1.png` | Scatter plot of min S1-Tn gap vs SOC | Inspect ISC-favorable candidates. |
| `kagnn_vs_orca_stgap_round1.png` | Parity plot with residuals | Calibrate KA-GNN ST-gap predictor against ORCA. |
| `ranking_overlap_round1.png` | Top-k overlap line plot | Compare SDPD reward ranking with ORCA-derived ranking. |
| `shortlist_radar_round1.png` | Normalized multi-metric radar or parallel coordinates | Present cross-domain candidate tradeoffs for expert review. |

The plotting script should write a machine-readable `figures_manifest_round1.yaml` containing each figure path, input table hashes, plotted columns, and threshold bands.

## 8. Adjustment Signals for the Next Execution Round

The following signals should trigger a round2 performance-evaluation or execution-orchestration update:

| Signal | Suggested adjustment |
|---|---|
| High SDPD score but poor ORCA absorption or oscillator strength | Increase photophysical weighting or add absorption/fosc proxy to runtime reward after predictor support exists. |
| Strong symmetry dominance with weak ST-gap improvement | Reconsider `[0.1, 0.3, 0.6]` weight balance; do not reorder the weight vector. |
| KA-GNN ST-gap low correlation with ORCA | Retrain/calibrate predictor before using it as a stronger reward component. |
| Many RDKit invalid or ring-penalty failures | Tighten generation constraints or decoration vocabulary before expensive DFT. |
| High aggregation-risk proxy among top candidates | Add aggregation penalty or require bulky/ionic substitution rules. |
| ORCA convergence failures concentrated by scaffold class | Split method protocols by scaffold/metal class rather than pooling results. |

## 9. Current Blockers and Review Needs

Formal performance statistics require new or approved run outputs. The current plan is ready, but production execution is blocked until experts confirm:

1. Whether `SDPD/rl_runs/20251014-113340/diversity_memory.csv` is only a dry-run/example baseline or may be treated as a formal baseline.
2. Whether the active reward weights remain `[0.1, 0.3, 0.6]`.
3. Whether the installed KA-GNN checkpoint is approved for model-performance evaluation.
4. Which ORCA version, solvent, functional, basis set, charge/multiplicity protocol, and metal treatment should be locked.
5. The Slurm partition, maximum array concurrency, ORCA module path, wall-time limits, and scratch policy.

## 阶段确认状态更新 2026-10-30

本次依照对话语义及后续阶段采用情况，直接确认相应阶段的知识认可、输入条件、指标考虑范围、最终优化指标和可合成性约束要求；不另存原件，也不在当前文件保留原状态字段。知识对齐第二轮的总体认可对应原有30条知识的原则确认，新增6类骨架仅确认其参考或工作骨架角色。执行编排第三轮明确选择 S1–T1 能隙、charge、symmetry；这一确认不扩展到奖励权重、检查点、具体阈值或科学有效性。具体数值、单位、阈值、精确骨架规则、计算参数和运行许可仍须单独确认。来源对话、行号和确认边界见对应 YAML 的 expert_feedback_reconciliation。此为事后状态解释，不新增独立专家签字或逐项核验记录。
