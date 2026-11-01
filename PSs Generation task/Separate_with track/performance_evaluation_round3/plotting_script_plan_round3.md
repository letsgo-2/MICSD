# Plotting Script Plan — Round 3

Update the Round 2 plots to include synthesizability without conflating heuristic score with actual route feasibility. Store all artifacts in Round 3 paths and retain provenance/units in figure captions.

| Output | Specification |
|---|---|
| `fig01_sa_score_distribution_round3.png` | SA score distribution by core/Round 1/Round 2 and QC status; show n, median and IQR. |
| `fig02_photophysics_vs_sa_round3.png` | SA score against minimum S1–Ti gap, SOCME and SOCME/ΔE; color by scaffold and annotate photophysics leaders. |
| `fig03_pareto_sa_sensitivity_round3.png` | Compare photophysics-only and photophysics-plus-SA fronts; plot candidate retention over threshold sweep, with no threshold marked approved unless supplied by the materials expert. |
| `fig04_sa_vs_structural_complexity_round3.png` | SA score vs molecular weight, macrocycle count, rotatable bonds and complexity descriptors to reveal possible scaffold bias. |
| `fig05_route_review_status_round3.png` | Route feasibility status and risk reasons for shortlisted candidates; omit until expert route assessments exist. |
| `table01_synthesizability_summary_round3.csv` | n, missingness, median/IQR, mean/SD and quantiles by cohort, scaffold and QC subset. |
| `table02_sa_photophysics_pareto_round3.csv` | Candidate-level SA score, raw photophysics components, Pareto membership and provenance. |
| `table03_threshold_sensitivity_round3.csv` | Candidate counts/retention and photophysical metrics across a displayed threshold grid; grid is sensitivity visualization only, not policy. |
| `table04_route_review_round3.csv` | Candidate, route review outcome, disconnections, building blocks, risks, reviewer, evidence and unknowns. |

Statistical comparison across prior Round 1 and Round 2 cohorts remains descriptive because cohorts are disjoint and generation provenance is incomplete. If future sampling permits inference, use scaffold-aware bootstrap intervals and report effect sizes, denominators and the score implementation/hash. Keep SA score and decoration symmetry as separate columns; inspect their association before combining weights because the score itself incorporates a symmetry-related term. Never label a molecule synthesizable solely because its SA score is low.
