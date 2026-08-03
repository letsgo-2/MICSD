# MICSD

[English](README.md) | [中文](README_CN.md)

This repository consolidates code and results for high-entropy alloy (HEA) active-learning evaluation, photosensitizer generation and performance evaluation, scientific knowledge alignment, and knowledge-base compilation. The directories represent largely independent workflows; there is no single entry point that runs the entire repository. Separate environments are therefore recommended for each task.

## Repository structure

```text
MICSD/
├── HEA task/                    # HEA active-learning results and offline performance evaluation
├── PSs Generation task/         # Photosensitizer generation, knowledge alignment, evaluation, and ka-wiki
├── llm-wiki-compiler-main/      # llmwiki TypeScript/Node.js source code
├── skills/                      # Scientific-workflow rules
├── statistics_skills/           # Statistical-analysis rules
└── EXTERNAL_REPOSITORIES.md     # Locations of separately maintained repositories
```

The `literature` and `markdown` directories contain placeholder files only in the GitHub repository; local literature collections and converted outputs are not included. The `SDPD` and `meloculardftcal` directories are also placeholders because their code is maintained in separate repositories.

## Multi-round dialogue examples

Two English multi-round dialogue examples are provided. They cover knowledge alignment, task orchestration, and performance evaluation:

- [`HEA task/multi_round_dialogue_example_EN.txt`](HEA%20task/multi_round_dialogue_example_EN.txt): optimization of an eight-element HEA catalyst composition.
- [`PSs Generation task/multi_round_dialogue_example_EN.txt`](PSs%20Generation%20task/multi_round_dialogue_example_EN.txt): photosensitizer molecule generation and evaluation.

## Environment overview

| Module | Recommended environment | Main dependencies or external software |
|---|---|---|
| HEA offline evaluation | Python 3.10 | NumPy, pandas, Matplotlib |
| Photosensitizer Round 1 performance evaluation | Python 3.10 | NumPy, pandas, Matplotlib, Seaborn, RDKit |
| `ka-wiki` / `llmwiki` | Node.js 24.16 (minimum 24) | npm, PowerShell 7, OpenAI-compatible API |
| SDPD | Linux x86_64, Python 3.10 | PyTorch 2.4.1, DGL, RDKit, CUDA, Git LFS |
| Molecular DFT workflow | Linux/HPC, Python 3.9+ | ORCA 6.0.1, OpenMPI 4.1.6, Slurm, Open Babel |

Recommended base tools:

- Git; Git LFS is also required when cloning the SDPD model files.
- Conda or Miniforge for scientific dependencies such as RDKit and Open Babel.
- Node.js 24 and npm for building `llm-wiki-compiler`.
- PowerShell 7 for the `ka-wiki` batch scripts.
- Bash/Linux only when running `.sh`, Slurm, or ORCA workflows.

## 1. Base Python environment

HEA analysis and general performance statistics can share a lightweight environment:

```bash
conda create -n micsd-analysis -c conda-forge python=3.10 numpy pandas matplotlib seaborn rdkit
conda activate micsd-analysis
pip install -r "PSs Generation task/performance_artifacts.round1/requirements.round1.txt"
```

Validate the installation:

```bash
python --version
python -c "import numpy, pandas, matplotlib, seaborn; from rdkit import Chem; print('Python environment OK')"
```

### HEA offline evaluation

The following scripts only read existing CSV/JSON data and generate statistics or figures. They do not train models or call an LLM. Run the commands from the `HEA task` directory:

```bash
cd "HEA task"

python performance_evaluation_round1/scripts/evaluate_al_performance_round1.py \
  --al-root AL/catalyst_active_learning_runnable \
  --output-dir performance_evaluation_round1

python performance_evaluation_round2/scripts/evaluate_total_pool_round2.py \
  --total-pool AL/catalyst_active_learning_runnable/outputs/total_pool.csv \
  --output-dir performance_evaluation_round2

python performance_evaluation_round3/scripts/generate_round3_starting_compositions.py \
  --output-dir performance_evaluation_round3
```

### Photosensitizer Round 1 performance evaluation

```bash
python "PSs Generation task/performance_artifacts.round1/scripts/rdkit_prepare.round1.py" --help
python "PSs Generation task/performance_artifacts.round1/scripts/write_orca_inputs.round1.py" --help
python "PSs Generation task/performance_artifacts.round1/scripts/plot_performance.round1.py" --help
```

`rdkit_prepare` prepares molecular structures, `write_orca_inputs` generates ORCA input files, and `plot_performance` plots the prediction results. When running the scripts, supply the input and output paths listed by each script's `--help` option.

## 2. Build llm-wiki-compiler

The project requires Node.js 24 or later. The version recorded for this repository is 24.16.0.

```bash
cd llm-wiki-compiler-main/llm-wiki-compiler-main
npm ci
npm run build
npm link
llmwiki --help
```

Development and validation commands:

```bash
npm test
npm run build
```

## 3. Run ka-wiki

Create a local `.env` file after entering `PSs Generation task/ka-wiki`. This file is ignored by Git; do not commit API keys:

```dotenv
LLMWIKI_PROVIDER=openai
LLMWIKI_MODEL=<model-name>
OPENAI_BASE_URL=<openai-compatible-base-url>
OPENAI_API_KEY=<your-api-key>
LLMWIKI_OUTPUT_LANG=en-US
LLMWIKI_COMPILE_CONCURRENCY=1
LLMWIKI_REQUEST_TIMEOUT_MS=1800000
LLMWIKI_PROMPT_BUDGET_CHARS=500000
LLMWIKI_EMBED_BATCH_SIZE=32
LLMWIKI_EMBEDDING_MODEL=text-embedding-3-large
OPENAI_EMBEDDINGS_BASE_URL=<embeddings-base-url>
```

`llmwiki` uses `dotenv`, so launch it from the `ka-wiki` directory that contains the `.env` file:

```powershell
Set-Location "PSs Generation task/ka-wiki"
llmwiki status --json
llmwiki compile --verbose --concurrency 1 --lang en-US
```

To review candidates manually:

```powershell
llmwiki compile --review --verbose --concurrency 1 --lang en-US
llmwiki status --json
```

`enable_source_batch.ps1` and `run_remaining_batches_review.ps1` enable source files in batches. They currently contain absolute paths from the machine on which they were created. Before running them, change `$Root` in each script to the absolute path of the current `ka-wiki` directory.

## 4. Obtain the external repositories

The GitHub versions of `PSs Generation task/SDPD` and `PSs Generation task/meloculardftcal` contain placeholder files only. Obtain the separate repositories before running their code:

```bash
git lfs install
git clone https://github.com/letsgo-2/SDPD.git SDPD
git clone https://github.com/letsgo-2/meloculardftcal.git meloculardftcal
```

The repositories can be cloned into any working directory. To preserve this project's directory layout, first remove `.gitkeep` from the corresponding placeholder directory, then clone the repositories into `PSs Generation task/SDPD` and `PSs Generation task/meloculardftcal`.

### SDPD environment

SDPD is intended for Linux x86_64 with Python 3.10 and NVIDIA CUDA. The current DecoratorModel prior, reinforcement-learning, and random-sampling paths explicitly create CUDA tensors, so these workflows require an available NVIDIA GPU. Install a DGL build compatible with PyTorch 2.4.1 and the CUDA version on the host system.

```bash
cd SDPD
conda create -n sdpd python=3.10
conda activate sdpd
pip install -r requirements.txt
```

Validate the key components before proceeding:

```bash
python -c "import torch, dgl, rdkit; print(torch.__version__, torch.cuda.is_available())"
```

For complete data-preparation, prior-training, KA-GNN-training, and reinforcement-learning commands, see `README_CN.md` or `README_EN.md` in the SDPD repository.

### meloculardftcal environment

Use the repository's Conda configuration for data parsing and visualization:

```bash
cd meloculardftcal
conda env create -f environment.yml
conda activate dft-workflow
python 07_validation/check_environment.py
```

Complete quantum-chemical calculations also require:

- ORCA 6.0.1;
- OpenMPI 4.1.6 matching the ORCA build;
- the Slurm scheduler;
- the Open Babel `obabel` command; and
- Linux compute nodes with sufficient CPU and memory resources.

Copy `config/cluster.env.example` to a local configuration file and set the ORCA executable, module name, partition, MPI rank, and memory parameters. Do not commit ORCA installers, license-related files, GBW wavefunction files, or large raw logs to Git.

## 5. ORCA Round 1 cluster job

`PSs Generation task/performance_artifacts.round1/scripts/run_orca_array.round1.sh` is a Slurm array-job template. Set at least the following variables before submission:

```bash
export PROJECT_DIR=<absolute-project-directory>
export ORCA_MODULE=<cluster-orca-module-name>
sbatch "PSs Generation task/performance_artifacts.round1/scripts/run_orca_array.round1.sh"
```

By default, the template requests 8 CPUs, 24 GB of memory, and a 24-hour time limit. Before a production run, adjust the array range and resource parameters to the cluster policy, candidate count, and ORCA inputs.

## 6. Security and reproducibility

- Never commit `.env` files, API keys, or local credentials.
- This repository ignores `ka-wiki/.env` and two historical compilation scripts that contain local machine configuration.
- For every important run, record the Git commit, Python/Node/ORCA versions, CUDA/DGL versions, and input-data version.
- ORCA, SDPD, and LLM compilation can consume substantial computing resources or API credits. Validate paths and parameters with a small sample before a production run.
- Windows is suitable for documentation, statistical analysis, and `ka-wiki`; Linux/HPC is preferable for CUDA training, Bash/Slurm, and ORCA batch processing.

## Quick environment checks

```bash
git --version
git lfs version
python --version
node --version
npm --version
```

On the DFT cluster, also check:

```bash
obabel -V
orca --version
sinfo --version
```
