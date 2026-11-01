# Plotting and Statistical Analysis Plan — Round 2

This plan extends the Round 1 plotting plan using the `meloculardftcal` metrics and plotting ecosystem. Keep outputs in round-specific paths and do not overwrite the repository's committed reference artifacts.

| Output | Purpose and safeguards |
|---|---|
| `fig01_core_metric_distributions_round2.png` | S1/T1, S1−T1, minimum positive S1−Ti, SOCME and SOCME/ΔE distributions; show n, quantiles and ratio-tail diagnostics. |
| `fig02_pareto_qc_sensitivity_round2.png` | Compare 2D/3D Pareto fronts on all rows, no-imaginary rows and log-verified subset, with objective directions and units. |
| `fig03_reference_comparison_round2.png` | Compare against `pic16` only as an electronic-property comparator; mark `Imaginary=Yes` and protocol compatibility. |
| `fig04_property_space_round2.png` | LogP vs TPSA, showing the current zero-hit visualization window as unvalidated rather than a biological pass criterion. |
| `fig05_candidate_cohort_round2.png` | Round1_n60 vs Round2_n60; clearly label disjoint/unpaired n=60 sets and descriptive-only comparison. |
| `fig06_run_qc_resources_round2.png` | Termination, frequency, retry/failure, walltime and RSS summaries, only when raw logs and scheduler accounting are available. |
| `table01_metric_summary_round2.csv` | n, valid n, median/IQR, mean/SD, quantiles, missingness and protocol per metric. |
| `table02_pareto_members_round2.csv` | Candidate IDs, objective values, dominance status, protocol, QC and structure identifiers. |
| `table03_candidate_cohort_descriptives_round2.csv` | Cohort summaries; no inferential test until sampling and generation provenance justify it. |
| `table04_run_provenance_round2.csv` | Job ID, termination, frequency, protocol/config hash, resources and parser status per candidate. |

Do not infer model accuracy from candidate property columns. Report raw components alongside weighted score and ratios. The SOCME/ΔE distribution is heavily right-tailed (core mean 6.26, median 3.46, maximum 110.16), so use robust quantiles and inspect extreme structures. Failed or imaginary-frequency rows must remain represented in denominators and sensitivity views. Keep protocol labels explicit, and use scaffold-level bootstrap intervals where an approved inferential design exists.
