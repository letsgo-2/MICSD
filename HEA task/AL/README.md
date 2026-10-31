# HEA Active Learning and Plotting

[中文说明](README_zh.md)

This directory contains the active-learning code, data, and plotting scripts for high-entropy alloy (HEA) catalyst optimization. The paths and settings below reflect the current code.

### Active-learning workflow and model files

| File | Purpose |
| --- | --- |
| `main.py` | Runs the active-learning workflow: calls `LLM.py` for formulation generation and candidate-performance prediction, uses `KDAS.py` to select candidates, and predicts power density with `gradient_boosting_model.joblib` before updating the sample pool. |
| `LLM.py` | Wraps large-language-model calls for catalyst-formulation generation and power-density prediction. |
| `KDAS.py` | Implements K-DAS candidate selection. |
| `prompt.py` | Defines prompts for formulation generation, performance prediction, and related tasks. |
| `initial.py` | Loads example formulations and power densities from Excel, using `experinced examples.xlsx` by default. |
| `GBR.py` | Trains a gradient boosting regression (GBR) model using `Data.xlsx` and saves it as `gradient_boosting_model.joblib`. |
| `gradient_boosting_model.joblib` | Stores the regression model loaded by the active-learning workflow to predict candidate power densities. |
| `config.py` | Reads API configuration from the `OPENAI_API_KEY`, `OPENAI_BASE_URL`, and `OPENAI_MODEL` environment variables. |
| `requirements.txt` | Lists Python dependencies and version requirements. |

The formulation element order is `Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr`. Training and example data use these element columns and the `max_power` column. Where an `abandoned` column is present, samples with a value of 1 are excluded according to the corresponding loading code.

By default, `main.py` loads `experinced examples.xlsx` and `gradient_boosting_model.joblib`, then writes results to `experinced result/`, including `total_examples_pool.csv`, `best_results_per_iteration.csv`, and `experiment_summary.csv`. Power densities for newly acquired candidates are GBR model predictions.

### Plotting scripts and data sources

All paths below are relative to this directory.

| Script | Input and processing | Output image |
| --- | --- | --- |
| `plot_a.py` | Reads `Data.xlsx`, fits a new GBR model, and plots predicted versus experimental values. | `experinced plot/Fig8_a.png` |
| `plot_b.py` | Reads `round2 plot/total_examples_pool.csv` for the experience-based scheme and `round1 plot/total_examples_pool.csv` for the traditional scheme (legend: `Trad settings`), then plots their best-so-far power-density convergence curves. | `experinced plot/Fig8_b.png` |
| `plot_c.py` | Plots the final-formulation comparison using two composition arrays defined directly in the script; it does not load CSV data or automatically extract the best formulation. | `experinced plot/Fig8_c.png` |
| `reproduce_figures.py` | Runs `plot_a.py`, `plot_b.py`, and `plot_c.py` in sequence. | All three images above, saved to `experinced plot/`. |

`plot_a.py` fits its own model rather than loading `gradient_boosting_model.joblib`. Its displayed metrics use all valid samples, including training samples. `plot_b.py` sorts by `example_id` when available, treats the first 10 samples as round 0, and groups subsequent samples into batches of 3 for up to 50 acquisition rounds. It does not calculate means or standard deviations across repeated runs. The active-learning output directory differs from the plotting input directories, so updating workflow results does not automatically update the plotting inputs.

The second formulation in `plot_c.py` currently retains the legend `Random settings-Final formulation`. This is the script's existing label; this README refers to the `round1 plot` scheme in `plot_b.py` as the traditional scheme.

### Usage

Install dependencies from this directory:

```powershell
python -m pip install -r requirements.txt
```

Before running active learning, configure the API environment variables and check the example-data path, model path, and results directory in `main.py`. Start the workflow with:

```powershell
python main.py
```

To regenerate only the three subfigures, ensure the plotting input files listed above exist, then run:

```powershell
python reproduce_figures.py
```

Run `python GBR.py` when retraining and saving the regression model is required; this overwrites the model file with the same name. `reproduce_figures.py` does not start the active-learning workflow, but it refits the plotting model through `plot_a.py`.

