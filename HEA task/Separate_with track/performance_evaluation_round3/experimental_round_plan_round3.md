# Experimental Round 3 Plan

## Purpose

Evaluate whether a controlled shift toward the descriptive round2 high-performance composition region improves measured device peak power density under matched conditions. The shift is a hypothesis for testing, not an established causal rule.

## Design logic

- `R3-CONTROL-CENTROID`: full-pool composition control.
- `R3-HIGH-CENTROID`: round2 high-performance centroid, emphasizing the observed Pd/Ce shift and lower Au fraction.
- `R3-TOP5-CENTROID`: top-five descriptive centroid.
- `R3-GRADIENT-*`: three interpolation points between the high-performance and full-pool centroids.
- `R3-PD-AU-CONTRAST-*`: controlled Pd/Au contrast perturbations.
- `R3-DIVERSE-*`: local perturbations around the high-performance centroid to measure sensitivity and guard against selection collapse.

The complete compositions are in `adjusted_composition_design_round3.csv`. Only nonnegativity and closure are enforced because approved element-specific bounds were not supplied. All designs require materials-scientist approval before synthesis.

## Measurement protocol requirements

For every design, record the actual prepared composition basis, nominal and measured fractions, batch/sample ID, device protocol, operating conditions, P_peak unit, replicate number, raw measurement, uncertainty, and failed-run reason. Use at least technical replicates under matched conditions and randomize measurement order where practical.

## Acceptance and analysis gate

Do not replace `estimated_power_density` with a model output. Populate it only after the experiment with measured P_peak and uncertainty. Compare round3 versus round2 under matched conditions using replicate-aware summaries, confidence intervals, MAE/RMSE/R² and rank metrics for predictions, and composition-support diagnostics. Retrain the model only after preserving the pre-round3 model and provenance.
