# Scientific Execution Orchestration Report — Round 1

Generated: 2026-07-17  
Input stage: knowledge-alignment round 2  
Input files:

- `knowledge_alignment_round2.yaml`
- `knowledge_alignment_round2_report.md`
- `expert_review_queue_round2.yaml`

Output purpose: design an executable workflow for reinforcement-learning-driven molecular generation and optimization of high-performance photosensitizer candidates. This orchestration inherits upstream metrics, scaffold evidence, thresholds, and expert-review items. It does not re-run knowledge alignment and does not select a final algorithm as experimentally validated.

## 1. Project Goal and Input Evidence

The project goal is to generate candidate molecules with higher photosensitive performance. The domain experts specify that molecular representation is normally **SMILES**, molecular fragmentation should use **RECAP**, and **porphyrin is a common scaffold**. The computer expert proposes building a **reinforcement learning (RL) framework** for molecular generation and optimization.

Primary upstream evidence is inherited from round-2 knowledge alignment:

| Evidence | Use in orchestration |
|---|---|
| R2-E001, R2-E002 | Phthalocyanine/ZnPc and porphyrinoid evidence: long-wavelength Q-band, high absorption coefficient, high singlet-oxygen potential, aggregation and solubility risks. |
| R2-E003, R2-E004 | AIE D-A / D-A-D scaffolds: ICT, aggregation-state photosensitization, ISC/ROS relevance. |
| R2-E005, R2-E006 | Type-I and metal-complex examples: Nile-blue Type-I photodrug and Re(I) CAIX-anchored photosensitizer. |
| R2-O001 | TD-DFT review evidence: TD-DFT can support absorption, ISC, T1-S0, SOC; therapeutic window 600-800 nm; Type-II triplet-energy thresholds 0.98 eV / conservative solution 1.13 eV. |
| R2-O002, R2-O003 | Type-I design evidence: S1-Tn gap <0.4 eV as ISC heuristic; T1-S0 branch conflict; electron-transfer design and redox matching. |
| R2-O004 | IUPAC definitions for oscillator strength, excitation energy, redox potential, ionization energy, electron affinity, and Rehm-Weller equation. |
| RDKit documentation | `Chem.MolFromSmiles`, sanitization, and `rdkit.Chem.Recap.RecapDecompose()` for RECAP fragment hierarchy. |
| RL molecular generation literature | REINVENT-style SMILES RL, staged learning, scalar multi-component scores, scaffold-constrained generation, validity/uniqueness/novelty/diversity checks, fragment-based hierarchical action spaces. |

## 2. Fused Metrics and Final Role Decisions

The upstream round-2 metrics are split into execution roles. The first active branch should be **porphyrin / porphyrinoid Type-II PDT**, because the user states porphyrin is common and the round-2 evidence gives clearer Type-II thresholds than Type-I redox thresholds. A second branch for hypoxia-tolerant Type-I PDT should be retained but not activated until electron-transfer definitions are reviewed.

| Rank | Metric | Final role | Direction | Threshold guidance | Evaluator | Decision status | Evidence |
|---:|---|---|---|---|---|---|---|
| 1 | Valid SMILES and RDKit sanitization | hard_constraint | pass/fail | Must parse and sanitize; invalid molecules receive score 0 | RDKit validity checker | active | RDKit docs |
| 2 | Porphyrin/porphyrinoid scaffold preservation | hard_constraint for first branch | pass/fail or soft scaffold similarity | Require porphyrin core or approved porphyrinoid/phthalocyanine scaffold in round1 branch | scaffold checker | proposed | user input, R2-S001, R2-S007 |
| 3 | TD-DFT absorption wavelength `lambda_abs` | primary_objective | target_range | 600-800 nm high score; 650-750 nm preferred initial sweet zone | TD-DFT calculator / surrogate | proposed | R2-I001, R2-O001 |
| 4 | T1-S0 energy gap for Type-II | primary_objective | minimum threshold | >0.98 eV required for Type-II; >1.13 eV preferred conservative solution threshold | TD-DFT/TDA calculator | proposed | R2-I003, R2-O001 |
| 5 | Minimum S1-Tn energy gap | intermediate objective | minimize | <0.4 eV favorable ISC heuristic; not sufficient without SOC | TD-DFT state calculator | proposed | R2-I004, R2-O002 |
| 6 | Oscillator strength `f` | secondary_objective | maximize/rank | No universal hard threshold; penalize near-zero transition; rank within same method/scaffold | TD-DFT calculator / surrogate | proposed | R2-I002, R2-O004 |
| 7 | Aggregation-risk proxy | soft_constraint | minimize | Penalize planar hydrophobic macrocycles without bulky/ionic substituent compensation | rule checker / optional dimer calculation | proposed | R2-I008, R2-E001, R2-E002 |
| 8 | Synthetic accessibility / RECAP compatibility | soft_constraint | maximize accessibility | Favor candidates built from RECAP fragments and low synthetic-complexity edits | RECAP + SA checker | proposed | RDKit docs, fragment-based RL refs |
| 9 | Heavy atom / metal risk flag | diagnostic or branch constraint | context-dependent | Flag I/Br/Se/Re/Gd/Cu and high formal charge; do not auto-exclude unless expert confirms | risk checker | proposed | R2-I015, R2-S005 |
| 10 | Electron-transfer free energy `DeltaG_ET` | deferred primary for Type-I branch | minimize / negative | `DeltaG_ET < 0` indicates thermodynamic feasibility; requires donor/acceptor/substrate definition | redox/DFT calculator | suspended for round1 | R2-I006, R2-O002, R2-O003, R2-O004 |
| 11 | SOC(S1,Tn) | expensive intermediate | maximize/rank | No universal threshold; compute for top candidates only | SOC calculator | proposed-stage2 | R2-I005, R2-O001 |
| 12 | ICT descriptor | diagnostic/intermediate | target_range | Moderate CT preferred; over-strong CT with low oscillator strength penalized | NTO/CT analyzer | proposed-stage2 | R2-I007 |

## 3. Search Space and Molecular Representation

### 3.1 Representation

- Canonical molecule representation: **SMILES**.
- Internal validation: RDKit molecule parsing and sanitization.
- Fragment vocabulary: **RECAP fragments** extracted from known photosensitizers, uploaded paper examples if structures are available, and domain-approved porphyrin/porphyrinoid seed molecules.
- Scaffold anchor for round1: **porphyrin core** plus approved porphyrinoid variants such as phthalocyanine/ZnPc when explicitly enabled.

### 3.2 RECAP rule usage

Use RDKit `rdkit.Chem.Recap.RecapDecompose(mol, minFragmentSize=...)` to create a fragment hierarchy. Store fragments as canonical SMILES with attachment metadata. Generation actions should be constrained to RECAP-compatible fragment replacement, side-chain decoration, fragment addition, and fragment deletion where valence/sanitization checks pass.

### 3.3 Initial seed sets

1. Porphyrin scaffold seeds approved by the material expert.
2. Phthalocyanine/ZnPc seeds from the round-2 evidence branch.
3. Optional AIE D-A and Type-I seeds kept in inactive profiles until branch approval.

## 4. Model and Tool Interface Registry

| model_id | Name | Role | Status | Input | Output | Notes |
|---|---|---|---|---|---|---|
| MODEL-001 | RDKit SMILES validator | constraint_checker | proposed | SMILES | valid/sanitized molecule, canonical SMILES | Hard gate; invalid molecules score 0. |
| MODEL-002 | RDKit RECAP fragmenter | constraint_checker | proposed | RDKit Mol | RECAP hierarchy, fragment SMILES | Official API: `Recap.RecapDecompose`. |
| MODEL-003 | Scaffold checker | constraint_checker | proposed | SMILES, scaffold SMARTS | pass/fail, scaffold similarity | Porphyrin branch requires scaffold preservation. |
| MODEL-004 | RL molecule generator | generator | proposed | prior model, fragment vocabulary, reward profile | candidate SMILES | SMILES-based staged RL or fragment-level RL. |
| MODEL-005 | Fast property prefilter | constraint_checker | proposed | SMILES | MW, cLogP/logS proxy, formal charge, ring count, alert flags | Cheap stage before DFT. |
| MODEL-006 | TD-DFT absorption/state calculator | physics_calculator | proposed | 3D conformer, method config | lambda_abs, f, S/T state energies | Main expensive oracle for top candidates. |
| MODEL-007 | SOC calculator | physics_calculator | proposed-stage2 | selected excited states | SOC matrix elements | Top-candidate only. |
| MODEL-008 | Redox/DeltaG_ET calculator | physics_calculator | deferred | donor/acceptor/substrate definition | redox potentials, DeltaG_ET | Blocked until Type-I definitions are approved. |
| MODEL-009 | Surrogate model for TD-DFT metrics | surrogate | proposed | descriptors/SMILES/graph | predicted lambda_abs, T1-S0, f, uncertainty | Train after first DFT batch. |
| MODEL-010 | Uncertainty and diversity filter | uncertainty_model | proposed | candidate pool + predictions | uncertainty, novelty, diversity, scaffold bucket counts | Prevent mode collapse and overexploitation. |

## 5. Reward Design

### 5.1 Round1 active reward profile: porphyrin Type-II PDT

Use a staged scoring profile. Early stages should use cheap constraints and surrogates; later stages phase in TD-DFT and SOC, following staged-learning practice from REINVENT-style workflows.

```text
Score_round1 = Gate_validity * Gate_scaffold * Aggregate(
  R_abs_window,
  R_typeII_triplet_energy,
  R_ISC_gap,
  R_abs_intensity,
  P_aggregation,
  P_synthesis,
  P_risk
)
```

Recommended component weights for the first executable draft:

| Component | Weight | Transform | Evidence/Reason |
|---|---:|---|---|
| Valid SMILES gate | hard gate | invalid -> 0 | RDKit validity is prerequisite for all downstream scoring. |
| Porphyrin scaffold gate | hard/soft gate | absent -> 0 in scaffold-preserving branch | User states porphyrin is common scaffold; scaffold-constrained generation improves search relevance. |
| `R_abs_window` | 0.25 | trapezoid: 600-800 nm high, 650-750 nm peak | TD-DFT PDT review therapeutic window evidence. |
| `R_typeII_triplet_energy` | 0.25 | step/sigmoid: >0.98 eV pass, >1.13 eV preferred | Singlet oxygen threshold evidence from TD-DFT PDT review. |
| `R_ISC_gap` | 0.15 | high if min S1-Tn <0.4 eV | Type-I/ISC design review heuristic; still useful for triplet population. |
| `R_abs_intensity` | 0.10 | rank-normalized oscillator strength | IUPAC definition and TD-DFT output; proxy for absorption strength. |
| `P_aggregation` | -0.10 | penalty for planar hydrophobic macrocycle without bulky/ionic compensation | Pc/ZnPc paper evidence: aggregation decreases PDT effect. |
| `P_synthesis` | -0.10 | penalty for non-RECAP-compatible or high SA complexity | Fragment-based RL and RECAP workflow need synthesizable actions. |
| `P_risk` | -0.05 | diagnostic penalty for unapproved metal/heavy atom/high charge | Upstream risk queue; do not hard-exclude until expert approval. |

### 5.2 Deferred Type-I profile

Do not activate the Type-I reward in the same run as the Type-II profile because T1-S0 direction conflicts. Prepare it for a separate branch:

- `R_abs_window`: 600-800 nm, or branch-specific NIR target if approved.
- `R_ISC_gap`: min S1-Tn <0.4 eV favorable.
- `R_ET_thermo`: `DeltaG_ET < 0` favorable.
- `R_typeI_block_EET`: T1-S0 <0.98 eV may suppress Type-II EET.
- `P_risk`, `P_aggregation`, and validity/scaffold gates remain active.

## 6. Execution Workflow

### Stage 0 — Input normalization

1. Load round-2 knowledge files.
2. Register porphyrin scaffold SMARTS/SMILES from material expert.
3. Canonicalize all seed SMILES with RDKit.
4. Reject unsanitizable seeds and place them in the review queue.

### Stage 1 — RECAP vocabulary construction

1. Run RECAP decomposition on seed molecules.
2. Build fragment vocabulary with attachment points.
3. Tag fragments by source scaffold, charge, ring type, donor/acceptor character if available.
4. Freeze the porphyrin scaffold for the first branch; allow RECAP side-chain replacement and decoration.

### Stage 2 — RL environment definition

- State: current partial or complete molecule, scaffold identity, open attachment sites, fragment history, cheap descriptors.
- Action: select attachment site, select RECAP fragment, attach/replace/delete fragment, terminate episode.
- Transition: apply graph edit, sanitize with RDKit, canonicalize SMILES, update descriptors.
- Terminal condition: no open sites, max steps reached, invalid molecule, or agent termination.
- Reward: terminal scalar score plus optional dense validity/constraint feedback.

### Stage 3 — Cheap prefilter and first RL pass

1. Train or initialize a SMILES/fragment RL prior.
2. Generate candidates around porphyrin scaffold.
3. Apply validity, scaffold, RECAP compatibility, charge, molecular-size, and aggregation-risk filters.
4. Keep diverse candidate buckets to avoid repeated analogs.

### Stage 4 — Physics evaluation loop

1. Select top diverse candidates for TD-DFT.
2. Compute absorption wavelength, oscillator strength, T1-S0, S1-Tn gaps.
3. Update candidate rewards with measured computational values.
4. Train/update surrogate model with uncertainty estimates.
5. Send high-uncertainty or high-score diverse candidates to the next DFT batch.

### Stage 5 — Expert review and branch update

1. Review threshold failures and high-score candidates with material and computation experts.
2. Decide whether to activate Type-I branch.
3. Decide whether metal/heavy-atom candidates are allowed.
4. Update reward profile and constraints without overwriting the round1 record.

## 7. Evidence, Thresholds, and Cautions

- The 600-800 nm absorption window and 0.98/1.13 eV triplet thresholds are literature-supported initial thresholds, not final acceptance criteria.
- The S1-Tn <0.4 eV rule is a heuristic for ISC and must be paired with SOC or experimental validation.
- Oscillator strength has no universal threshold; use ranking and near-zero penalties.
- RECAP compatibility improves synthetic plausibility but does not prove synthesis feasibility.
- SMILES-based RL is practical and supported by REINVENT-style literature, but it can suffer validity/diversity issues; RDKit gates and diversity filters are mandatory.
- Fragment-level action spaces reduce invalid generation and align better with RECAP, but require curated fragment vocabularies and attachment-site rules.

## 8. Suggested Metric Ordering

For the first executable branch, use this order:

1. Validity and sanitization.
2. Porphyrin scaffold preservation.
3. TD-DFT absorption wavelength in target range.
4. Type-II T1-S0 energy threshold.
5. S1-Tn gap as ISC proxy.
6. Oscillator strength ranking.
7. Aggregation-risk penalty.
8. Synthetic accessibility / RECAP compatibility.
9. Heavy atom, metal, and charge risk diagnostics.
10. Optional SOC for top candidates.
11. Deferred Type-I ET metrics.

This ordering reflects direct relevance to the user’s porphyrin-scaffold RL task, evidence strength, calculation readiness, and cost.

## 9. Review Status

Current orchestration status: **proposed, not expert-approved**.

Blocked before active execution:

- Expert-provided porphyrin scaffold representation or SMARTS.
- Approved DFT method stack and computational budget.
- Decision whether Type-I branch is active or deferred.
- Decision whether metal complexes are allowed.

## 10. Execution Review Queue Summary

See `execution_review_queue_round1.yaml` for detailed questions. The highest-priority questions are scaffold definition, Type-II versus Type-I branch selection, DFT method selection, and whether thresholds are soft rewards or hard filters.

## 11. Deliverable for Next Stage

The next stage can implement the workflow using the YAML configuration in `execution_orchestration_round1.yaml`. The minimum viable implementation is:

1. RDKit SMILES validator.
2. RDKit RECAP fragmenter.
3. Porphyrin scaffold checker.
4. Fragment-based RL generator.
5. Cheap descriptor and aggregation-risk prefilter.
6. TD-DFT batch evaluator for top candidates.
7. Surrogate model and active-learning loop after the first computational batch.

## 阶段确认状态更新 2026-10-30

本次依照对话语义及后续阶段采用情况，直接确认相应阶段的知识认可、输入条件、指标考虑范围、最终优化指标和可合成性约束要求；不另存原件，也不在当前文件保留原状态字段。知识对齐第二轮的总体认可对应原有30条知识的原则确认，新增6类骨架仅确认其参考或工作骨架角色。执行编排第三轮明确选择 S1–T1 能隙、charge、symmetry；这一确认不扩展到奖励权重、检查点、具体阈值或科学有效性。具体数值、单位、阈值、精确骨架规则、计算参数和运行许可仍须单独确认。来源对话、行号和确认边界见对应 YAML 的 expert_feedback_reconciliation。此为事后状态解释，不新增独立专家签字或逐项核验记录。
