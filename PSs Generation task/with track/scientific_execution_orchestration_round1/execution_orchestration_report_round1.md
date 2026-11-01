# Scientific Execution Orchestration — Round 1

## 1. Input status
This draft inherits the three Round 2 alignment outputs: `knowledge_alignment.yaml`, `knowledge_alignment_report.md`, and `expert_review_queue.yaml`. It covers the 47-paper evidence scope and adds the materials expert's SMILES/RECAP/porphyrin constraints and the computer expert's reinforcement-learning objective.

No executable generator, parser, RECAP implementation, DFT evaluator, environment, or parameter interface was supplied. Therefore all models are registered as `proposed`, the workflow is `draft`, and automatic parameter adjustment is disabled.

## 2. Execution objective and search space
Generate valid candidate SMILES by RECAP-compatible edits around a retained porphyrin scaffold, evaluate computable photophysical proxies, and select a diverse shortlist for expert review and later experimental validation. Porphyrin is treated as the default scaffold family based on the expert input, not as a universal optimum.

Hard search-space rules proposed for approval:
- standardized, valid SMILES with explicit charge and multiplicity metadata;
- retain the porphyrin core for the first run;
- permit only RECAP-compatible fragment edits and approved substituent/metal/axial-ligand changes;
- reject invalid valence/aromaticity, untracked metals or charges, and candidates outside evaluator applicability domain.

## 3. Metric fusion and ranking
Ranking is proposed rather than expert-approved. It weights direct relevance, computability, threshold availability, discrimination, cost, uncertainty, and compatibility with deterministic/cached SMILES-level RL evaluation.

| rank | metric_id | final_role | direction | threshold | ranking_basis | decision_status |
|---|---|---|---|---|---|---|
| 1 | D001 | primary_objective | target_range | {"value": null, "range": [600, 800], "unit": "nm", "status": "provisional_literature_band", "companion": "f >= 0.01 is a provisional screen"} | Directly linked to usable excitation; cheap enough for high-throughput TD-DFT surrogate/calculation and has a provisional band.; Current status is proposed, not expert-approved.; SMILES-level RL needs deterministic or cached evaluation. | proposed |
| 2 | D003 | hard_constraint | context_dependent | {"value": null, "range": [0.98, 1.13], "unit": "eV", "status": "provisional_branch_threshold", "note": "Type-II favors above; indirect Type-I may favor below"} | Mechanism branch gate prevents contradictory Type-I/Type-II rewards; threshold is evidence-backed but method dependent.; Current status is proposed, not expert-approved.; SMILES-level RL needs deterministic or cached evaluation. | proposed |
| 3 | D004 | secondary_objective | minimize | {"value": 0.4, "range": [0, 0.4], "unit": "eV", "status": "provisional_scaffold_local_heuristic"} | Mechanistically relevant ISC proxy with a literature heuristic; expensive and state-tracking sensitive.; Current status is proposed, not expert-approved.; SMILES-level RL needs deterministic or cached evaluation. | proposed |
| 4 | D005 | secondary_objective | maximize | {"value": 0.24, "range": [0.24, null], "unit": "cm^-1", "status": "provisional_state_pair_heuristic"} | Mechanistically relevant SOC proxy; useful for metal/heavy-atom and ICT comparisons but state-pair specific.; Current status is proposed, not expert-approved.; SMILES-level RL needs deterministic or cached evaluation. | proposed |
| 5 | D008 | diagnostic | context_dependent | {"value": null, "range": [], "unit": "method-specific", "status": "unresolved_percentile_or_family_target"} | Checks whether favorable gaps represent the intended CT state; descriptor standardization is incomplete.; Current status is proposed, not expert-approved.; SMILES-level RL needs deterministic or cached evaluation. | proposed |
| 6 | D006 | feature_only | none | {"value": null, "range": [], "unit": "eV", "status": "no_universal_threshold"} | Low-cost electronic feature, but raw frontier energies are method-dependent and not a direct endpoint.; Current status is proposed, not expert-approved.; SMILES-level RL needs deterministic or cached evaluation. | proposed |
| 7 | D010 | soft_constraint | context_dependent | {"value": null, "range": [], "unit": "method-specific", "status": "project_calibration_required"} | May expose polarity/shape risk, but no validated universal target and aggregation is not captured directly.; Current status is proposed, not expert-approved.; SMILES-level RL needs deterministic or cached evaluation. | proposed |
| 8 | I001 | deferred | maximize | {"value": null, "range": [], "unit": "dimensionless", "status": "deferred_until_matched_assay"} | Scientifically central but requires matched experiment and cannot be inferred reliably from a single DFT value.; Current status is proposed, not expert-approved.; SMILES-level RL needs deterministic or cached evaluation. | proposed |
| 9 | I003 | deferred | minimize | {"value": null, "range": [], "unit": "assay-specific", "status": "deferred_until_matched_assay"} | Final biological objective but not available as molecule-only evaluator; reserve for active-learning validation.; Current status is proposed, not expert-approved.; SMILES-level RL needs deterministic or cached evaluation. | proposed |


### Recommended initial ranking
1. **D001 — excitation wavelength/oscillator strength:** primary proxy objective because it directly screens light compatibility and is more feasible for iterative evaluation than biological endpoints. Use a band-pass, not a simple maximize-wavelength reward.
2. **D003 — triplet-energy branch gate:** hard mechanism gate. Select Type-II or indirect Type-I before scoring; their T1 directions must not be combined.
3. **D004 — ΔE(S1,Tn):** secondary ISC proxy with the reported <0.4 eV heuristic; requires state tracking and scaffold-local calibration.
4. **D005 — SOC:** secondary ISC proxy with the reported >0.24 cm−1 heuristic; state-pair-specific and not a direct ROS endpoint.
5. **D008 — CT character:** diagnostic/intermediate descriptor that protects against rewarding the wrong dark or pathological CT state.
6. **D006 and D010:** low-cost features/soft constraints; do not use as standalone rewards.
7. **I001 and I003:** scientifically important experimental objectives, deferred from molecule-only RL until matched assay data and a validated surrogate exist.

## 4. Threshold and reward recommendations
Provisional threshold guidance is inherited from Round 2 evidence and must be calibrated before activation:
- D001: target 600–800 nm; use oscillator strength f≥0.01 only as a literature screen, not a universal law.
- D003 Type-II: require T1 above a consistently computed oxygen-sensitization reference; the literature reports approximately 0.98 eV ideal and approximately 1.13 eV in solution. D003 Type-I: the indirect branch may require T1 below the Type-II threshold, but only with an active electron-transfer feasibility gate.
- D004: ΔE(S1,Tn)<0.4 eV is a soft, scaffold-local ISC heuristic.
- D005: SOC>0.24 cm−1 is a soft, state-pair-specific heuristic.
- D008: no universal numeric threshold; calibrate by scaffold family and retain state character.

Proposed trial reward after hard validity/scaffold/branch gates:
`R = 0.35 R_D001 + 0.15 R_D004 + 0.15 R_D005 + 0.10 R_D008 - uncertainty_penalty`, with D003 handled as a branch gate rather than a weighted objective. These weights are initial placeholders for calibration, not expert-approved scientific priorities. Use Pareto selection if objective conflicts are substantial.

## 5. Domain expert view
The domain expert's contribution defines the molecular representation, RECAP fragmentation rule, and porphyrin-centered search space. The domain expert must confirm whether porphyrin-core retention is a hard constraint, which metal/charge/axial-ligand edits are allowed, and which mechanism branch is scientifically intended. The domain expert also reviews whether DFT proxies plausibly connect to the selected Type-I or Type-II mechanism and must not treat a favorable proxy as proof of cell-level potency.

Current domain-expert blockers: branch selection, scaffold edit boundaries, acceptable charge/multiplicity, and approval of provisional thresholds.

## 6. Computer expert view
The computer expert receives an RL-ready interface: SMILES state, RECAP action vocabulary, porphyrin scaffold validator, deterministic metric evaluators, uncertainty/OOD checks, component rewards, and full provenance. The generator and evaluators remain proposed because no executable paths, versions, environments, or parameter interfaces were provided. Automatic tuning is prohibited until the interfaces and authorized parameter ranges are exposed.

Recommended RL state/action contract:
- State: standardized partial/full SMILES, molecular graph, porphyrin-core mask, charge/multiplicity, applied RECAP edits, cached evaluator outputs, and uncertainty flags.
- Action: select a legal RECAP fragment/edit, attach at an allowed site, terminate, or reject; mask actions violating scaffold, valence, charge, or evaluator rules.
- Transition record: parent SMILES, child SMILES, action, validity, edit trace, evaluator configuration, outputs, uncertainty, reward, and failure reason.
- Selection: retain validity, uniqueness, scaffold retention, diversity, and Pareto-frontier statistics; do not select solely by one proxy.

## 7. Model and interface registry
| model_id | name | role | status | entrypoint | supported_metrics |
|---|---|---|---|---|---|
| MODEL-001 | SMILES RL molecular generator | generator | proposed | {"command": "", "script": "", "environment": "", "working_directory": ""} | D001, D003, D004, D005, D008 |
| MODEL-002 | SMILES parser/standardizer | constraint_checker | proposed | {"command": "", "script": "", "environment": "", "working_directory": ""} | structure validity, scaffold retention, RECAP edit legality |
| MODEL-003 | DFT/TD-DFT evaluator | physics_calculator | proposed | {"command": "", "script": "", "environment": "", "working_directory": ""} | D001, D003, D004, D005, D006, D008, D010 |
| MODEL-004 | Uncertainty and applicability checker | uncertainty_model | proposed | {"command": "", "script": "", "environment": "", "working_directory": ""} | all active proxy metrics |


## 8. Workflow
1. Load and standardize seed SMILES, RECAP vocabulary, porphyrin rule, and approved branch configuration.
2. Generate candidates using masked legal RECAP actions.
3. Check SMILES validity, charge/multiplicity metadata, porphyrin retention, RECAP legality, uniqueness, and basic domain rules.
4. Calculate D001/D003/D004/D005/D006/D008/D010 with one approved, versioned protocol and cache results by standardized structure plus configuration hash.
5. Check convergence, uncertainty, and applicability domain; reject or manually review failed/OOD candidates.
6. Apply the selected Type-I or Type-II branch gate, compute component rewards, and log all raw values and units.
7. Select diverse Pareto/top-k candidates; stop if validity, diversity, OOD, or reward-direction checks fail.
8. Submit the shortlist to domain and computer experts; only then export candidates for experimental validation.

Mandatory smoke test before formal RL: valid/invalid SMILES, RECAP action legality, porphyrin retention, units, missing-value handling, DFT failure handling, branch-gate direction, reward monotonicity, uncertainty penalties, uniqueness/diversity, and reproducibility.

## 9. Parameter adjustment and run policy
All controls are fixed or manual in this draft. No automatic parameter changes are authorized because the generator/evaluator interfaces and allowed ranges are absent. After expert approval, only reward weights, generation budget, and explicitly authorized optimizer parameters may be adjusted; scientific targets, hard constraints, mechanism branch, and source evidence cannot be changed automatically.

## 10. Review queue and stopping conditions
See `execution_review_queue_round1.yaml`. The workflow must pause for missing model interfaces, unresolved Type-I/Type-II conflict, unapproved DFT thresholds, invalid units or reward direction, high OOD/uncertainty, scaffold-rule violations, or expert veto.

## 11. Evidence and limitations
Threshold guidance is inherited from Round 2 sources X001, X006, and X008 and is explicitly provisional. DFT/TD-DFT values are proxy or branch-gating quantities, not direct biological outcomes. Experimental ΦΔ, phototoxicity, dark toxicity, photostability, aggregation, localization, and hypoxia performance remain deferred until matched datasets and assays are available.