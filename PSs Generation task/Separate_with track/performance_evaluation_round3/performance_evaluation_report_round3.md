# Scientific Performance Evaluation — Round 3

## 1. Scope and update

This round updates `../performance_evaluation_round2/` in response to a **materials-scientist recommendation** to add a synthesizability constraint. This is recorded as real expert input, distinct from the Skill's analysis-based recommendations. The constraint is incorporated into the evaluation and plotting plan but is not activated as a hard gate: the expert did not provide a numeric threshold, and the available `SA_Score` is a heuristic, not route-level synthetic validation.

Round 2 evidence remains the quantitative baseline: 222 core `pic16_s1` rows, two disjoint 60-candidate generated cohorts, and registered `meloculardftcal` RDKit/ORCA/Slurm interfaces. There are still no model holdout metrics, per-run manifests, or bundled raw ORCA logs. No molecules were recalculated and no optimization or scheduler job was run in this update.

## 2. Synthesizability constraint: definition and operationalization

### Evidence and interpretation

`meloculardftcal` includes `SA_Score` in v22 enrichment. Its `04_data_processing/sascorer.py` implementation identifies the score as the Ertl–Schuffenhauer synthetic accessibility score, approximately on a 1–10 scale, and uses fragment contributions plus penalties for size, stereochemistry, spiro/bridgehead features, macrocycles, and symmetry. The interface declares the direction as **minimize**. It is therefore a useful computational *synthesizability proxy*, but it does not enumerate a synthetic route, prove reagent availability, estimate yield, or account reliably for all macrocyclic/charged photosensitizer chemistry. In particular, the score's symmetry term can reward symmetrical molecules, so it can interact with the Round 2 symmetry objective.

### Proposed policy (expert approval required)

1. Preserve all photophysical objectives and raw component values; add `SA_Score` as an independent feasibility dimension, not silently fold it into the existing weighted reward.
2. Initially use a **soft constraint / Pareto objective**: lower SA score preferred, while retaining photophysical quality and scaffold diversity. Display score distribution and frontiers alongside the photophysical objectives.
3. Select a numeric feasibility threshold only after the materials expert reviews real candidates and available synthetic precedent. Do not derive a hard cutoff from the sample median or treat a default percentile as a scientific threshold. Record the approved threshold, rationale, intended chemistry domain, and exception policy in the next run manifest.
4. For finalists, require a route-level review: plausible disconnections, commercially available or accessible building blocks, key bond-forming steps, protecting-group/functional-group compatibility, macrocycle assembly feasibility, charge/counterion and purification considerations, and known precedent. Record reviewer, evidence, route risk and unresolved steps.
5. Report SA score and route-review outcome separately. A low SA score cannot substitute for a plausible route, and an unavailable route review must remain “not assessed,” not “synthesizable.”

### Round 2 baseline context

The core `pic16_s1` set has SA score median 6.2455 (mean 6.3105; range 5.022–7.935). The generated 60-member cohorts have median SA scores 6.463 (Round 1) and 6.071 (Round 2), with means 6.4816 and 6.0649 respectively. The cohort difference is descriptive only: the sets have no shared SMILES, are not paired, and have no recorded generator/config lineage sufficient for causal attribution. These values support adding the descriptor to decision views; they do not justify declaring either cohort more synthesizable in practice.

## 3. Updated metrics and records

| Metric / evidence | Role | Direction / status |
|---|---|---|
| Minimum positive S1–Ti gap | Photophysical objective | Minimize, subject to mechanism and protocol context |
| SOCME and SOCME/ΔE | Photophysical objectives/descriptors | Preserve as separate components; inspect long-tailed ratio |
| LogP, TPSA, charge, molecular weight, flexibility | Application feasibility descriptors | Expert-defined context-specific constraints remain unresolved |
| `SA_Score` | New synthesizability proxy | Minimize; threshold requires materials-expert approval; not route validation |
| Route assessment | Real-world feasibility evidence | Required for prioritized finalists; currently unavailable |

Candidate-level record additions for future cohorts: `SA_Score`, score implementation/version, valid-SMILES/QC state, `synthesis_screen_status`, `approved_sa_threshold` (nullable until authorized), `sa_threshold_rationale`, route-review status, route summary/reference, building-block availability, key step count/risk, reviewer, and provenance. Keep missing route assessments null/unknown.

## 4. Updated plotting and statistics plan

Add `fig05_synthesizability_tradeoff_round3` (shift existing figure IDs as needed): SA score vs each primary photophysical objective; color by scaffold and shape by route-review status; indicate an approved threshold only when one exists. Add an SA score distribution by cohort and QC status, with counts and median/IQR. Extend the Pareto table with SA score as a separate objective and compare photophysics-only vs photophysics-plus-SA fronts; report retention/feasibility counts across a threshold-sensitivity curve, not a single unapproved cutoff. Keep objective directions explicit and prevent the symmetry contribution embedded in SA score from being confused with the separate decoration-symmetry metric.

Do not run significance tests on Round 1 vs Round 2 cohorts without a suitable sampling design and provenance. For future randomized/controlled cohorts, compare SA score distributions with scaffold-aware bootstrap intervals and report effect size and denominators. Route-review outcomes require descriptive risk/feasibility summaries; they should not be reduced to SA score correlation alone.

## 5. Next optimization recommendations

1. **Approve the synthesizability policy before changing generation rewards.** Materials expert should define intended role (soft objective vs hard exclusion), acceptable complexity region, exceptions for macrocyclic scaffold, and evidence standard for route feasibility. Keep the threshold unresolved until that decision exists.
2. **Run retrospective feasibility profiling first.** Compute/check SA scores for the candidate tables and stratify by scaffold, MW, macrocycle count, rotatable bonds and photophysical merit; identify top Pareto candidates whose complexity is score-driven versus route-driven. The current files already include `SA_Score`, so verify provenance and avoid recalculating under a different implementation without versioning.
3. **Use a two-stage selection funnel.** Broad molecular generation and photophysical Pareto screening first; then SA-score triage and expert route review for a manageable shortlist. This avoids prematurely removing promising photosensitizers using a heuristic that may penalize the intended macrocyclic scaffold.
4. **Perform threshold sensitivity analysis.** Show candidate retention and photophysical trade-offs over a range of SA thresholds, with no single threshold labeled approved until expert sign-off. If a hard cap is eventually selected, keep the former configuration and log the change as reversible.
5. **Calibrate the proxy against project-specific judgments.** Have the materials expert label a blinded, scaffold-stratified subset for route feasibility, then measure association and disagreement with SA score; document false-easy/false-hard examples. If disagreement is substantial, retain SA score only as a descriptor and prioritize route-based review or a better-calibrated predictor.
6. **Carry forward Round 2 safeguards.** First obtain immutable generation/config lineage and raw ORCA/Slurm provenance, quality-filter minima, update the application property window with expert rationale, and validate any surrogate on scaffold-held-out data before changing model or weighted reward settings.

## 6. Attribution and limitations

**Expert-provided request:** the materials scientist recommends a synthesizability constraint. **Skill-generated recommendation:** represent it initially with `SA_Score` as a transparent soft/Pareto feasibility proxy plus route-level review for finalists. No approved threshold or route assessments were supplied. Round 2 scientific values are inherited unchanged; no measured improvement from adding the constraint can be claimed. Review decisions are listed in `performance_review_queue_round3.yaml`.

## Dialogue-based status reconciliation (2026-10-31)

The current output states have been reconciled with the saved expert dialogue at the user's request. General knowledge acceptance, task inputs, selected metric roles, and the synthesizability requirement are recorded only within their supported scope. Existing disputes, unanswered review questions, missing protocols, numerical thresholds, route validation, model-validation gaps, and execution-authorization requirements remain explicit. No scientific values or execution permissions are newly certified, and the historical execution trace is unchanged. The scope and dialogue excerpts are recorded in the expert_feedback_reconciliation metadata of `performance_evaluation_round3.yaml`, `synthesizability_parameters_round3.yaml`.
