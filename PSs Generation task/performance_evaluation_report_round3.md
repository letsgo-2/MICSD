# Scientific Performance Evaluation Report - Round 3

Generated: 2026-07-25  
Stage: performance evaluation update after materials-expert synthesizability request  
Status: round2 evidence retained; synthesizability constraint added. No new ORCA, Slurm, RDKit batch execution, or figure generation was performed in this round.

## 1. Inputs, Versions, and Execution Status

Round3 updates `performance_evaluation_report_round2.md`, `performance_evaluation_round2.yaml`, and `performance_review_queue_round2.yaml` with a new materials-expert recommendation: **add a synthesizability constraint** to candidate ranking and next-round optimization.

The evidence base remains the `meloculardftcal` `pic16_s1` batch:

| Evidence | Path | Round3 use |
|---|---|---|
| Workflow interface | `meloculardftcal/AGENT_INTERFACE_EN.md` | Defines stages, RDKit enrichment, ORCA protocols, Slurm controls, and optimization interface. |
| Metrics report | `meloculardftcal/reports/pic16_s1/metrics.json` | Provides `SA_Score`, molecular weight, coverage, Pareto, and property summaries. |
| Final data table | `meloculardftcal/data/core/pic16_s1/final/pic16inpdftv22.csv` | Used to compute synthesizability-filter counts. |
| Environment report | `meloculardftcal/reports/environment.json` | Confirms local data-tool availability and lack of local ORCA/Slurm availability. |

The same execution caveat remains active: the committed table is complete at v22 level, but raw ORCA logs and Slurm outputs are not bundled, so normal-termination rates remain unavailable from this checkout.

## 2. Evaluation Subjects, Result Coverage, and Data Quality

The evaluated subject remains `pic16_s1` with 222 complete v22 rows and 191 records where `Imaginary == No`. The v22 table already contains `SA_Score` and `Molecular_Weight`, so the new synthesizability constraint can be applied immediately as a ranking/filter layer without rerunning DFT.

Current synthesizability-related distribution from `metrics.json`:

| Metric | Value |
|---|---:|
| `SA_Score` min | 5.022 |
| `SA_Score` median | 6.2455 |
| `SA_Score` mean | 6.3105 |
| `SA_Score` p75 | 6.5463 |
| `SA_Score` p90 | 6.963 |
| `SA_Score` max | 7.935 |
| Molecular weight median | 987.268 g/mol |
| Molecular weight mean | 1005.456 g/mol |

Data-quality implication: `SA_Score` is available for all 222 rows, so synthesizability can be treated as a complete constraint column. However, `SA_Score` is a computational proxy and should be reviewed together with route feasibility, purchasable building blocks, protecting-group burden, macrocycle/metal-complex synthesis complexity, and expert retrosynthetic judgment.

## 3. Real Expert Inputs, Skill-Inferred Concerns, and Basis

New real expert input:

| Expert input | Attribution | Action in round3 |
|---|---|---|
| Add a synthesizability constraint. | Materials scientist | Add `SA_Score`-based hard/soft filters, track molecular weight as a secondary practicality constraint, and update shortlist/reward recommendations. |

Skill-inferred concerns:

| Concern | Basis | Priority |
|---|---|---|
| A strict `SA_Score <= 6.0` filter may be too severe for this candidate space. | Only 51/222 all records and 43/191 no-imaginary records pass. | Medium |
| `SA_Score <= 6.5` is a practical first-pass cutoff. | 163/222 all records and 143/191 no-imaginary records pass; close to p75. | High |
| Molecular weight should be a companion constraint, not a replacement for SA Score. | Median MW is 987.27 g/mol and p75 is 1104.87 g/mol. | High |
| Route feasibility still requires expert review. | SA Score is proxy-only and cannot certify actual synthesis. | High |

## 4. Tools, Compute Environments, and External Evidence

No toolchain change is required to support the new constraint because `meloculardftcal` already computes `SA_Score` in stage `S51_ENRICH` via `04_data_processing/addrdkit.py` and records it in `pic16inpdftv22.csv`.

Relevant toolchain elements remain:

| Component | Use for synthesizability update |
|---|---|
| RDKit enrichment | Provides molecular descriptors and supports structural filtering. |
| `SA_Score` in v22 | Primary synthesizability proxy for ranking and filtering. |
| Molecular weight | Secondary practicality constraint, especially for large macrocycle-like candidates. |
| `plotsample.py` | Should select diverse candidates after synthesizability filtering. |
| ORCA/TD/SOC metrics | Remain photophysical objectives; should not override impossible synthesis. |

## 5. Metric Mapping, Analysis Plans, Evaluation Protocols, and Comparability

Round3 adds the following metric layer:

| Metric | Role | Direction | Initial rule |
|---|---|---|---|
| `SA_Score` | Synthesizability proxy | Minimize | Soft-prefer `<= 6.5`; strongly prefer `<= 6.0` where photophysical performance remains competitive; deprioritize `> 7.0` unless expert-justified. |
| `Molecular_Weight` | Secondary synthetic/developability practicality proxy | Minimize or cap | Use `<= 1100 g/mol` as a first-pass moderate cap and `<= 1200 g/mol` as a relaxed cap pending expert review. |

Recommended round3 ranking gate:

```text
eligible_for_round3_shortlist =
  Imaginary == "No"
  AND SA_Score <= 6.5
  AND Molecular_Weight <= 1100
  AND S1_wavelength_nm in the selected PDT window
  AND min_positive_S1-Ti < 0.4 eV
```

This gate should be treated as an initial decision rule, not a final synthesis guarantee. If it eliminates too many high-value photophysical candidates, keep a secondary exception list with explicit materials-expert approval.

## 6. Code, Script Execution, and Visualization Artifacts

No new scripts were executed in round3 beyond reading and calculating counts from the existing v22 table. The implementation points for future scripts are:

| Script or stage | Required update |
|---|---|
| `04_data_processing/addrdkit.py` | Keep `SA_Score` generation as a required v22 column. |
| `07_validation/collect_metrics.py` | Continue reporting `SA_Score`; optionally add pass counts for chosen SA thresholds. |
| `05_analysis/plotters/plot_summary.py` | Include visible `SA_Score` distribution and selected cutoff lines. |
| `05_analysis/plotters/plotsample.py` | Sample diverse candidates from the synthesizability-filtered pool. |
| SDPD reward/filter layer | Add a synthesizability reward or post-generation filter after expert confirmation. |

Suggested new table for the next analysis run: `analysis_round3/synthesizability_filtered_shortlist_round3.csv`.

## 7. Run and Model-Behavior Analysis: Computer-Expert View

The new constraint changes the optimization problem from electronic-property-only Pareto selection to constrained multi-objective selection. The computer-expert view should implement the constraint in a transparent sequence:

1. Filter to `Imaginary == No`.
2. Apply `SA_Score <= 6.5` as the default synthesizability gate.
3. Apply `Molecular_Weight <= 1100` as a moderate practicality cap.
4. Apply the selected wavelength window.
5. Apply `min_positive_S1-Ti < 0.4 eV`.
6. Rank or Pareto-sort remaining candidates by `min_positive_S1-Ti`, `max_SOCME_S1_Ti_value`, and `max_SOCME_over_deltaE_S1_Ti_value`.
7. Use diversity sampling to avoid selecting only close analogs.

Observed pass counts from the existing v22 table:

| Filter | All records | No-imaginary records |
|---|---:|---:|
| `SA_Score <= 6.0` | 51/222 | 43/191 |
| `SA_Score <= 6.5` | 163/222 | 143/191 |
| `SA_Score <= 7.0` | 203/222 | 177/191 |
| `Molecular_Weight <= 900` | 58/222 | 47/191 |
| `Molecular_Weight <= 1000` | 118/222 | 100/191 |
| `Molecular_Weight <= 1100` | 164/222 | 140/191 |
| `Molecular_Weight <= 1200` | 197/222 | 169/191 |
| `Imaginary == No`, `SA_Score <= 6.5`, `MW <= 1100` | 120/222 | 120/191 |
| `Imaginary == No`, `SA_Score <= 7.0`, `MW <= 1200` | 161/222 | 161/191 |
| `Imaginary == No`, `SA_Score <= 6.5`, 600-800 nm | 84/222 | 84/191 |
| `Imaginary == No`, `SA_Score <= 6.5`, 600-800 nm, `min_positive_S1-Ti < 0.4` | 76/222 | 76/191 |

## 8. Separate Domain-Expert Views

Materials-scientist view:

- The new synthesizability constraint is justified because the candidate set has high molecular weight and moderate-to-high SA Scores.
- `SA_Score <= 6.5` keeps enough candidates for selection while removing the highest-complexity tail.
- Candidates with `SA_Score > 7.0` should require explicit route justification before being promoted.

Computational-chemistry view:

- Synthesizability filtering should be applied after excluding non-minima, not before geometry validation.
- Do not discard a uniquely strong photophysical candidate solely by SA Score without checking whether a plausible known scaffold route exists.

Computer-scientist view:

- Add `SA_Score` to reward calibration and candidate-selection scripts as a constraint or soft penalty.
- Preserve a two-tier shortlist: strict feasible set and exception set.

## 9. Figure Observations, Expert Interpretations, and Disagreements

No new figures were generated in round3. Required figure updates:

| Figure | Required addition |
|---|---|
| `score_distributions` or summary plot | Add SA Score histogram with cutoff lines at 6.0, 6.5, and 7.0. |
| Pareto plot | Mark candidates failing `SA_Score <= 6.5` or MW cap. |
| Wavelength plot | Compare 600-800 nm candidate counts before and after SA filtering. |
| Shortlist plot | Show strict feasible candidates separately from expert-exception candidates. |

Potential disagreement to resolve: a materials expert may prefer route-feasible analogs even when their electronic proxies are slightly worse, while the current Pareto logic may favor electronically optimal but synthetically difficult molecules.

## 10. Comparison with Baselines, Historical Rounds, and Published Work

Round3 does not change the round2 reference benchmark interpretation. The reference row `pic16` in `05_analysis/data/publishinpdftv22.csv` has `Imaginary=Yes`, so it remains an electronic-property benchmark, not a validated minimum.

New comparison requirement: future baseline comparisons should include `SA_Score` and molecular weight alongside electronic proxies. A candidate should not be called an optimization improvement if it improves SOC/gap metrics only by moving into a substantially less synthesizable region, unless the materials expert explicitly accepts that trade-off.

## 11. Cross-Domain Joint Evidence, Advantages, Trade-Offs, and Failure Modes

Advantages of adding synthesizability:

- Makes recommendations more actionable for experimental follow-up.
- Reduces risk of selecting molecules that are strong only computationally.
- Gives SDPD a clearer feedback signal for future generation constraints.

Trade-offs:

- Strict synthesizability filters may remove high-performing electronic candidates.
- SA Score alone can penalize unusual but known synthetic motifs or fail to capture route-specific feasibility.
- Molecular weight caps may be too restrictive for some photosensitizer scaffolds.

Failure modes:

- Treating `SA_Score <= 6.5` as a universal law rather than a project-initial cutoff.
- Optimizing only SA Score and drifting away from photophysical requirements.
- Applying molecular weight constraints without considering formulation or delivery strategy.

## 12. Candidate or Run Decision States

Updated decision states:

| Decision object | Round3 state |
|---|---|
| v22 table | Usable for synthesizability-aware ranking because `SA_Score` is complete. |
| Strict shortlist | Should use `Imaginary == No`, `SA_Score <= 6.5`, MW cap, wavelength window, and ISC proxy filters. |
| Exception shortlist | Allowed only for high electronic performance with explicit route review. |
| SDPD next optimization | Should add a synthesizability constraint or reward component after expert approval. |
| Experimental recommendation | Still pending route feasibility and synthesis planning. |

## 13. Data Gaps, Additional Computation, and Experimental-Validation Needs

New data gaps:

- No retrosynthetic route scores or reaction-step estimates are present.
- No building-block availability or cost screen is present.
- No expert-labeled synthesizable/non-synthesizable candidate set is present.
- No SDPD reward variant with `SA_Score` penalty has been run.

Additional needs:

1. Generate `SA_Score`-aware shortlist tables.
2. Ask the materials expert to label the top strict and exception candidates by route feasibility.
3. If available, add retrosynthesis or building-block screening as a second synthesizability layer.
4. Run sensitivity analysis for SA cutoffs 6.0, 6.5, and 7.0.

## 14. Adjustment Recommendations by This Skill and Their Evidence Basis

| Recommendation | Evidence basis | Target |
|---|---|---|
| Add `SA_Score <= 6.5` as the default hard gate for first shortlist generation. | Keeps 143/191 no-imaginary candidates and aligns near the p75 value. | Shortlist scripts. |
| Add `SA_Score <= 6.0` as a preferred tier, not a mandatory first gate. | Only 43/191 no-imaginary candidates pass, likely too restrictive initially. | Ranking annotations. |
| Add `SA_Score > 7.0` as an expert-review flag. | 177/191 no-imaginary records pass `<=7.0`, leaving a high-complexity tail. | Review queue and plots. |
| Pair SA Score with MW caps. | 120 candidates pass no-imaginary, SA<=6.5, and MW<=1100. | Feasibility filters. |
| Add a soft synthesizability penalty to SDPD next-round optimization. | Materials expert requested synthesizability and v22 already supplies SA Score. | SDPD reward design. |

## 15. Expert Adjustment Recommendations, Attribution, and Synthesized Plans

Expert-attributed adjustment:

```yaml
expert_adjustment:
  expert: materials_scientist
  request: add synthesizability constraint
  mapped_metrics:
    - SA_Score
    - Molecular_Weight
  proposed_default_rule: Imaginary == "No" AND SA_Score <= 6.5 AND Molecular_Weight <= 1100
  exception_policy: allow electronically exceptional candidates only after route review
```

Synthesized round4-ready plan:

1. Create strict and exception shortlists from `pic16inpdftv22.csv`.
2. Generate figures showing SA Score distribution and Pareto-front impact.
3. Ask materials expert to review route feasibility for strict top candidates and exception candidates.
4. Convert accepted synthesizability rules into SDPD reward/filter parameters.
5. Re-run candidate generation or post-generation selection with the new constraint.

## 16. Unresolved Issues, Limitations, and Recommendations for the Next Round

Unresolved issues:

- Confirm whether `SA_Score <= 6.5` is acceptable as the initial hard gate.
- Confirm whether MW `<=1100` or `<=1200` is the appropriate cap for this photosensitizer class.
- Confirm whether any high-SA candidate should be retained because it follows a known scaffold-specific synthetic route.
- Confirm whether synthesizability should be a hard filter, a soft reward penalty, or both.

Round3 conclusion: the materials-expert recommendation is directly actionable because the current v22 table already contains complete `SA_Score` values. The next optimization should become synthesizability-aware: filter validated minima, apply SA Score and MW constraints, then perform photophysical Pareto selection and diversity sampling. This preserves the strong electronic-property search while making the candidate set more realistic for synthesis planning.

## 阶段确认状态更新 2026-10-30

本次依照对话语义及后续阶段采用情况，直接确认相应阶段的知识认可、输入条件、指标考虑范围、最终优化指标和可合成性约束要求；不另存原件，也不在当前文件保留原状态字段。知识对齐第二轮的总体认可对应原有30条知识的原则确认，新增6类骨架仅确认其参考或工作骨架角色。执行编排第三轮明确选择 S1–T1 能隙、charge、symmetry；这一确认不扩展到奖励权重、检查点、具体阈值或科学有效性。具体数值、单位、阈值、精确骨架规则、计算参数和运行许可仍须单独确认。来源对话、行号和确认边界见对应 YAML 的 expert_feedback_reconciliation。此为事后状态解释，不新增独立专家签字或逐项核验记录。
