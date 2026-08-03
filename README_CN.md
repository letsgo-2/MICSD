# MICSD

[English](README.md) | [中文](README_CN.md)

本仓库汇总了高熵合金（HEA）主动学习评估、光敏剂生成与性能评估、科学知识对齐，以及知识库编译相关的代码和结果。各目录是相对独立的工作流，不存在一个能够一次运行全部内容的统一入口；建议按任务分别创建环境。

## 仓库结构

```text
MICSD/
├── HEA task/                    # HEA 主动学习结果与离线性能评估
├── PSs Generation task/         # 光敏剂生成、知识对齐、性能评估及 ka-wiki
├── llm-wiki-compiler-main/      # llmwiki TypeScript/Node.js 源码
├── skills/                      # 科学工作流规则
├── statistics_skills/           # 统计规则
└── EXTERNAL_REPOSITORIES.md     # 独立仓库位置说明
```

`literature` 和 `markdown` 目录在 GitHub 中仅保留占位文件，不包含本地文献和转换产物。`SDPD` 与 `meloculardftcal` 也只保留占位目录，其代码分别维护在独立仓库中。

## 多轮对话示例

仓库提供两组英文多轮对话示例，覆盖知识对齐、任务编排和性能评估三个阶段：

- [`HEA task/multi_round_dialogue_example_EN.txt`](HEA%20task/multi_round_dialogue_example_EN.txt)：八元高熵合金催化剂组成优化。
- [`PSs Generation task/multi_round_dialogue_example_EN.txt`](PSs%20Generation%20task/multi_round_dialogue_example_EN.txt)：光敏剂分子生成与评估。

## 环境概览

| 模块 | 推荐环境 | 主要依赖/外部软件 |
|---|---|---|
| HEA 离线评估 | Python 3.10 | NumPy、pandas、Matplotlib |
| 光敏剂 Round 1 性能评估 | Python 3.10 | NumPy、pandas、Matplotlib、Seaborn、RDKit |
| `ka-wiki` / `llmwiki` | Node.js 24.16（最低 24） | npm、PowerShell 7、OpenAI-compatible API |
| SDPD | Linux x86_64、Python 3.10 | PyTorch 2.4.1、DGL、RDKit、CUDA、Git LFS |
| 分子 DFT 工作流 | Linux/HPC、Python 3.9+ | ORCA 6.0.1、OpenMPI 4.1.6、Slurm、Open Babel |

基础工具建议安装：

- Git；克隆 SDPD 模型文件时还需要 Git LFS。
- Conda/Miniforge，用于安装 RDKit、Open Babel 等科学计算依赖。
- Node.js 24 和 npm，用于构建 `llm-wiki-compiler`。
- PowerShell 7，用于运行 `ka-wiki` 的批处理脚本。
- Bash/Linux，仅在执行 `.sh`、Slurm 和 ORCA 工作流时需要。

## 1. Python 基础环境

HEA 分析和普通性能统计可以共用一个轻量环境：

```bash
conda create -n micsd-analysis -c conda-forge python=3.10 numpy pandas matplotlib seaborn rdkit
conda activate micsd-analysis
pip install -r "PSs Generation task/performance_artifacts.round1/requirements.round1.txt"
```

验证安装：

```bash
python --version
python -c "import numpy, pandas, matplotlib, seaborn; from rdkit import Chem; print('Python environment OK')"
```

### HEA 离线评估

以下脚本只读取现有 CSV/JSON 数据并生成统计表或图片，不会训练模型或调用 LLM。命令从 `HEA task` 目录运行：

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

### 光敏剂 Round 1 性能评估

```bash
python "PSs Generation task/performance_artifacts.round1/scripts/rdkit_prepare.round1.py" --help
python "PSs Generation task/performance_artifacts.round1/scripts/write_orca_inputs.round1.py" --help
python "PSs Generation task/performance_artifacts.round1/scripts/plot_performance.round1.py" --help
```

其中 `rdkit_prepare` 负责结构准备，`write_orca_inputs` 生成 ORCA 输入，`plot_performance` 根据预测结果绘图。实际执行时必须提供脚本 `--help` 中列出的输入和输出路径。

## 2. 构建 llm-wiki-compiler

项目要求 Node.js 24 或更新版本，仓库记录的版本为 24.16.0。

```bash
cd llm-wiki-compiler-main/llm-wiki-compiler-main
npm ci
npm run build
npm link
llmwiki --help
```

开发和验证命令：

```bash
npm test
npm run build
```

## 3. 运行 ka-wiki

进入 `PSs Generation task/ka-wiki` 后创建本地 `.env`。该文件已被 Git 忽略，不要提交 API Key：

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

`llmwiki` 使用 `dotenv`，因此从包含 `.env` 的 `ka-wiki` 目录启动即可：

```powershell
Set-Location "PSs Generation task/ka-wiki"
llmwiki status --json
llmwiki compile --verbose --concurrency 1 --lang en-US
```

需要人工审核候选项时：

```powershell
llmwiki compile --review --verbose --concurrency 1 --lang en-US
llmwiki status --json
```

`enable_source_batch.ps1` 和 `run_remaining_batches_review.ps1` 用于分批启用源文件。它们目前包含历史机器上的绝对路径，运行前应将脚本中的 `$Root` 改为当前 `ka-wiki` 绝对路径。

## 4. 获取独立仓库

GitHub 版本的 `PSs Generation task/SDPD` 和 `PSs Generation task/meloculardftcal` 只有占位文件。需要执行对应代码时，请先获取独立仓库：

```bash
git lfs install
git clone https://github.com/letsgo-2/SDPD.git SDPD
git clone https://github.com/letsgo-2/meloculardftcal.git meloculardftcal
```

可以将克隆结果放到任意工作目录；若希望保持本项目的目录布局，请先移除相应占位目录中的 `.gitkeep`，再将仓库克隆到 `PSs Generation task/SDPD` 和 `PSs Generation task/meloculardftcal`。

### SDPD 环境

SDPD 推荐 Linux x86_64、Python 3.10 和 NVIDIA CUDA 环境。当前 DecoratorModel 的 prior、强化学习和随机采样路径会显式创建 CUDA tensor，因此这些流程需要可用的 NVIDIA GPU。DGL 必须安装与 PyTorch 2.4.1 及本机 CUDA 对应的构建版本。

```bash
cd SDPD
conda create -n sdpd python=3.10
conda activate sdpd
pip install -r requirements.txt
```

完成后先验证关键组件：

```bash
python -c "import torch, dgl, rdkit; print(torch.__version__, torch.cuda.is_available())"
```

完整的数据准备、prior 训练、KA-GNN 训练和强化学习命令参见 SDPD 仓库的 `README_CN.md` 或 `README_EN.md`。

### meloculardftcal 环境

数据解析和可视化环境优先使用仓库提供的 Conda 配置：

```bash
cd meloculardftcal
conda env create -f environment.yml
conda activate dft-workflow
python 07_validation/check_environment.py
```

完整量化计算还要求：

- ORCA 6.0.1；
- 与 ORCA 构建匹配的 OpenMPI 4.1.6；
- Slurm 调度器；
- Open Babel 的 `obabel` 命令；
- Linux 计算节点和足够的 CPU/内存资源。

集群配置应从 `config/cluster.env.example` 复制为本地配置，并设置 ORCA 可执行文件、模块名、分区、MPI rank 和内存参数。不要将 ORCA 安装包、许可证相关文件、GBW 波函数或大规模原始日志提交到 Git。

## 5. ORCA Round 1 集群任务

`PSs Generation task/performance_artifacts.round1/scripts/run_orca_array.round1.sh` 是 Slurm 数组任务模板。提交前至少设置：

```bash
export PROJECT_DIR=<absolute-project-directory>
export ORCA_MODULE=<cluster-orca-module-name>
sbatch "PSs Generation task/performance_artifacts.round1/scripts/run_orca_array.round1.sh"
```

模板默认请求 8 CPU、24 GB 内存和 24 小时时限。正式运行前应根据集群策略、候选数和 ORCA 输入修改数组范围及资源参数。

## 6. 安全与可复现性

- `.env`、API Key 和本机凭据不得提交。
- 本仓库已忽略 `ka-wiki/.env` 及两个历史上包含本机配置的编译脚本。
- 建议为每次重要运行记录 Git commit、Python/Node/ORCA 版本、CUDA/DGL 版本和输入数据版本。
- ORCA、SDPD 与 LLM 编译均可能消耗大量算力或 API 额度，正式运行前先用小样本验证路径和参数。
- Windows 适合文档、统计分析和 `ka-wiki`；CUDA 训练、Bash/Slurm 和 ORCA 批处理更适合 Linux/HPC。

## 快速环境检查

```bash
git --version
git lfs version
python --version
node --version
npm --version
```

在 DFT 集群上额外检查：

```bash
obabel -V
orca --version
sinfo --version
```
