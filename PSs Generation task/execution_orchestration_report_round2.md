# Scientific Execution Orchestration Report — Round 2

Generated: 2026-07-17  
Input stage: execution orchestration round 1 update  
Input files:

- `execution_orchestration_report_round1.md`
- `execution_orchestration_round1.yaml`
- `execution_review_queue_round1.yaml`

Update purpose: refine the execution workflow by **strongly reprioritizing the metrics requested by the materials expert**: `SOCME`, `HOMO-LUMO`, `Es1-Et1`, `Es1`, `charge`, `symmetry`, `SA`, `logP`, `TPSA`, and `WM`. The updated files remain in English and are saved separately with the `round2` suffix.

## 1. Project Goal and Update Scope

The project goal remains the same: to design an executable reinforcement-learning workflow for generating and optimizing photosensitizer molecules. The domain constraints remain unchanged:

- molecular representation: **SMILES**
- fragmentation rule: **RECAP**
- common scaffold: **porphyrin**
- optimization engine: **reinforcement learning**

This round does **not** replace the overall scaffold-constrained RL workflow from round1. Instead, it updates:

1. the **metric ranking**;
2. the **reward design priority**;
3. the **staged evaluation order**;
4. the **review queue**;
5. the **active branch recommendation**.

## 2. Metric Name Normalization

The materials expert requested a specific metric list. To make the workflow executable, the names are normalized as follows:

| Requested name | Interpreted meaning | Execution name |
|---|---|---|
| SOCME | spin-orbit coupling matrix element | `SOCME` |
| HOMO-LUMO | frontier orbital gap or frontier energy pair | `HOMO_LUMO_gap` |
| Es1-Et1 | singlet-triplet gap between S1 and T1 | `DeltaE_S1_T1` |
| Es1 | S1 excitation energy | `E_S1` |
| charge | formal charge and/or charge distribution | `charge_profile` |
| symmetry | molecular symmetry or symmetry proxy | `symmetry_score` |
| SA | synthetic accessibility | `SA_score` |
| logP | octanol/water partition coefficient | `logP` |
| TPSA | topological polar surface area | `TPSA` |
| WM | molecular weight | `MW` |

Important interpretation note:

- `SOCME`, `DeltaE_S1_T1`, and `E_S1` are **excited-state photophysics metrics**.
- `HOMO_LUMO_gap` is a **supporting electronic-structure metric**, not a direct photosensitizer endpoint.
- `charge_profile`, `symmetry_score`, `SA_score`, `logP`, `TPSA`, and `MW` are **molecular design and developability controls**.

## 3. Updated Metric Ranking and Final Roles

The materials expert requested strong reprioritization, so the round2 branch promotes the requested metrics into the center of the workflow. However, the ranking still respects physical relevance and execution feasibility.

| Rank | Metric | Final role | Direction | Threshold or guidance | Why this rank |
|---:|---|---|---|---|---|
| 1 | Valid SMILES + sanitization | hard_constraint | pass/fail | invalid -> score 0 | All downstream properties depend on valid molecules. |
| 2 | Porphyrin scaffold preservation | hard_constraint | pass/fail | required in round2 porphyrin branch | The user and domain expert still anchor the search in porphyrin chemistry. |
| 3 | `SOCME` | primary_objective | maximize | use same method; literature example suggests >0.24 cm^-1 can indicate effective ISC channels in porphyrin-PDI systems, but keep as soft threshold | Directly connected to ISC and ROS generation; now explicitly prioritized by the materials expert. |
| 4 | `DeltaE_S1_T1` (`Es1-Et1`) | primary_objective | minimize to branch-appropriate range | smaller gap often promotes ISC; must not collapse into fluorescence-dominated or non-radiative failure regime | Strongly linked to ISC physics; more aligned with expert request than the previous `S1-Tn` ranking. |
| 5 | `E_S1` (`Es1`) | primary_objective | target_range | map to target absorption window through `lambda = 1240/E`; for PDT, target visible/NIR compatible S1 energies | The expert requested Es1 directly; it controls the absorption band placement. |
| 6 | `HOMO_LUMO_gap` | secondary_objective | context_dependent | no universal threshold; lower gap usually red-shifts absorption, but not sufficient alone | Useful as a fast electronic proxy, especially before expensive TD-DFT. |
| 7 | `charge_profile` | soft_constraint / intermediate | target_range | favor charge states and distributions compatible with uptake, amphiphilicity, and scaffold branch | Charge affects localization, uptake, aggregation, and membrane interaction. |
| 8 | `symmetry_score` | intermediate / design control | context_dependent | moderate symmetry may help reproducibility; controlled asymmetry may improve charge distribution and amphiphilicity | Symmetry affects charge distribution and sometimes aggregation or delocalization; should not be over-optimized blindly. |
| 9 | `SA_score` | soft_constraint | minimize difficulty / maximize accessibility | use standard SA score or project synthesis rank; lower is easier | Needed to keep RL from drifting into unsynthesizable structures. |
| 10 | `logP` | soft_constraint | target_range | no universal hard threshold; keep in moderate amphiphilic range | Directly related to lipophilicity and uptake; too high raises aggregation risk, too low may hurt membrane permeation. |
| 11 | `TPSA` | soft_constraint | target_range | no universal hard threshold; avoid extremes | Balances polarity, uptake, and solubility. |
| 12 | `MW` (`WM`) | soft_constraint | target_range | avoid excessive growth; exact threshold branch-specific | Prevents reward gaming by oversized molecules. |

### Core ranking conclusion

Round2 changes the workflow from a **property-window-first** design to a **photophysics-core-first** design:

- Round1 core: `lambda_abs`, `T1-S0`, `S1-Tn`, oscillator strength, aggregation risk.
- Round2 core: `SOCME`, `DeltaE_S1_T1`, `E_S1`, `HOMO_LUMO_gap`, then charge/developability metrics.

This means the RL agent should now optimize **electronic structure first**, then use `charge`, `symmetry`, `SA`, `logP`, `TPSA`, and `MW` to keep molecules chemically and practically usable.

## 4. Reward Design Update

### 4.1 Round2 active reward profile

The recommended active profile is still **porphyrin scaffold-constrained RL**, but the reward now centers on the materials expert metrics:

```text
Score_round2 = Gate_validity * Gate_scaffold * Aggregate(
  R_SOCME,
  R_DeltaE_S1_T1,
  R_E_S1,
  R_HOMO_LUMO,
  R_charge,
  R_symmetry,
  P_SA,
  P_logP,
  P_TPSA,
  P_MW
)
```

Recommended initial weights:

| Component | Weight | Transform | Evidence or rationale |
|---|---:|---|---|
| Validity gate | hard gate | invalid -> 0 | Required for all downstream evaluation. |
| Scaffold gate | hard gate | no porphyrin core -> 0 | Keeps the search in the domain-approved chemical space. |
| `R_SOCME` | 0.22 | rank or sigmoid | SOCME is now the top photophysics metric; porphyrin-PDI evidence suggests meaningful ISC channels when SOC exceeds roughly 0.24 cm^-1 in that study, but keep it as soft guidance, not universal truth. |
| `R_DeltaE_S1_T1` | 0.20 | target low-moderate gap | Lower `DeltaE_S1_T1` tends to increase ISC efficiency. |
| `R_E_S1` | 0.18 | target_range via desired S1 energy window | `E_S1` directly controls excitation wavelength. |
| `R_HOMO_LUMO` | 0.10 | target_range or ranking | Fast electronic proxy; smaller gap often supports red-shifted absorption. |
| `R_charge` | 0.08 | target_range | Charge and charge distribution affect amphiphilicity, localization, and uptake. |
| `R_symmetry` | 0.05 | moderate target, not max | Use as a regularizer rather than a dominant target. |
| `P_SA` | -0.07 | penalty if poor accessibility | Prevents unrealistic high-scoring structures. |
| `P_logP` | -0.04 | penalty outside moderate range | Balances uptake and aggregation risk. |
| `P_TPSA` | -0.03 | penalty outside moderate range | Balances polarity and transport. |
| `P_MW` | -0.03 | penalty if too large | Prevents reward hacking by growing oversized molecules. |

### 4.2 Threshold guidance

Evidence-backed or cautiously usable threshold guidance:

| Metric | Guidance | Status |
|---|---|---|
| `SOCME` | Use same software/method; in the cited porphyrin-PDI study, values above 0.24 cm^-1 were treated as supporting efficient ISC channels | evidence-backed but scaffold/method specific |
| `DeltaE_S1_T1` | Smaller is generally favorable for ISC; do not treat “as small as possible” as universally safe | evidence-backed direction, threshold unresolved |
| `E_S1` | Convert to wavelength; keep absorption in visible/NIR target region appropriate to the project | evidence-backed direction |
| `HOMO_LUMO_gap` | Use for ranking and prefiltering; do not use alone as the final reward | evidence-backed caution |
| `charge_profile` | Cationic or amphiphilic porphyrins often improve interaction and uptake in some biological settings | evidence-backed but application specific |
| `symmetry_score` | Use as a weak regularizer only; asymmetric charge distribution may improve function in some cases | weakly supported; keep low weight |
| `SA_score` | Lower is easier; exact project threshold unresolved | standard practice, not paper-specific threshold |
| `logP` | Favor moderate amphiphilicity; extremes are undesirable | evidence-backed direction, threshold unresolved |
| `TPSA` | Avoid extremes; too low hurts polarity control, too high may hurt permeability | standard developability guidance |
| `MW` | Avoid monotonic growth; keep moderate and branch-specific | standard developability guidance |

## 5. Updated Workflow Sequencing

### Stage 0 — Input and scaffold setup

No change from round1, except that the metric registry now explicitly records the normalized expert terms.

### Stage 1 — Fast prefilter before expensive photophysics

Use cheap metrics early:

1. Valid SMILES.
2. Porphyrin scaffold match.
3. MW.
4. Charge / formal charge.
5. logP.
6. TPSA.
7. SA.
8. Optional symmetry proxy.

Reason: these are cheaper than excited-state calculations and prevent wasted TD-DFT jobs.

### Stage 2 — Main photophysics evaluation

For surviving candidates, compute:

1. `E_S1`
2. `HOMO_LUMO_gap`
3. `DeltaE_S1_T1`
4. `SOCME`

Recommended order inside Stage 2:

- first `E_S1` and `HOMO_LUMO_gap` as the cheaper electronic screen;
- then `DeltaE_S1_T1`;
- finally `SOCME` for top candidates or when using a calibrated batch.

### Stage 3 — RL update policy

The RL agent should now receive a reward that is **denser on electronic descriptors** and **lighter on final experimental proxies**. This is appropriate because the expert explicitly wants stronger ordering on computational metrics.

### Stage 4 — Candidate selection

Top candidates should be selected using:

- high `SOCME`
- favorable `DeltaE_S1_T1`
- target `E_S1`
- acceptable `HOMO_LUMO_gap`
- acceptable charge / SA / logP / TPSA / MW

## 6. Recommended RL Action Policy Update

The generation environment still uses SMILES and RECAP, but round2 should bias the action policy toward edits that are likely to move the new core metrics:

- donor/acceptor substitutions that alter HOMO-LUMO separation;
- conjugation-length edits that shift `E_S1`;
- symmetry-breaking or symmetry-restoring edits that tune charge distribution;
- charged side-group replacement to adjust `charge_profile`, `logP`, and `TPSA`;
- fragment selection constrained by RECAP to keep SA manageable.

Suggested action categories:

1. Replace peripheral substituent.
2. Add or swap donor/acceptor fragment.
3. Insert linker variation affecting conjugation length.
4. Introduce or remove charged side group.
5. Stop.

## 7. What Changed from Round1

The most important differences are:

1. `SOCME` is now elevated from an expensive stage-2 helper metric to a top-ranked reward component.
2. `DeltaE_S1_T1` replaces `S1-Tn` as the more explicit materials-expert energy-gap target.
3. `E_S1` replaces `lambda_abs` as the direct optimization variable, while wavelength becomes a derived interpretation.
4. `HOMO_LUMO_gap`, `charge`, and `symmetry` are no longer only side descriptors; they are explicit ranking features.
5. `SA`, `logP`, `TPSA`, and `MW` are explicitly promoted into the reward/penalty layer.

## 8. Risks and Cautions

- `SOCME` should not be optimized without method locking; cross-method comparisons are unsafe.
- Very small `DeltaE_S1_T1` can help ISC, but not all low-gap molecules are good photosensitizers.
- `HOMO_LUMO_gap` is a proxy, not a final performance endpoint.
- `charge` and `symmetry` are context-sensitive; they can improve uptake or amphiphilicity but can also worsen aggregation or toxicity.
- `SA`, `logP`, `TPSA`, and `MW` must remain constraints, not dominant reward drivers.

## 9. Execution Status

Round2 recommendation: activate a **photophysics-centered porphyrin RL branch** with the new metric ranking, but keep final thresholds on `SOCME`, `DeltaE_S1_T1`, `charge`, `symmetry`, `SA`, `logP`, `TPSA`, and `MW` as **proposed** until experts approve the exact ranges.

## 10. Review Queue Summary

See `execution_review_queue_round2.yaml` for detailed expert questions. The highest-priority new items are:

- exact computational definition of `SOCME` and software/method;
- target range strategy for `DeltaE_S1_T1`;
- operational meaning of `symmetry`;
- acceptable ranges for `SA`, `logP`, `TPSA`, and `MW` in porphyrin-like photosensitizers.

## 11. Deliverable for Next Stage

The next executable implementation should use `execution_orchestration_round2.yaml` as the active configuration and keep round1 files unchanged for traceability.
