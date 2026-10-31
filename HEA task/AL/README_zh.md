# HEA 主动学习与绘图

[English](README.md)

本目录包含高熵合金（HEA）催化剂优化的主动学习代码、数据和绘图脚本。以下说明对应当前代码中的路径和设置。

### 主动学习与模型文件

| 文件 | 功能 |
| --- | --- |
| `main.py` | 主动学习主流程：调用 `LLM.py` 生成配方并预测候选性能，调用 `KDAS.py` 筛选候选点，再使用 `gradient_boosting_model.joblib` 预测功率密度并更新样本池。 |
| `LLM.py` | 封装大语言模型调用，生成催化剂配方并预测功率密度。 |
| `KDAS.py` | 实现 K-DAS 候选点筛选。 |
| `prompt.py` | 管理配方生成、性能预测等任务的模型提示词。 |
| `initial.py` | 从 Excel 读取示例配方及功率密度，默认使用 `experinced examples.xlsx`。 |
| `GBR.py` | 使用 `Data.xlsx` 训练梯度提升回归（GBR）模型，并保存为 `gradient_boosting_model.joblib`。 |
| `gradient_boosting_model.joblib` | 供主动学习流程加载的回归模型，用于预测候选配方的功率密度。 |
| `config.py` | 从环境变量读取 API 配置：`OPENAI_API_KEY`、`OPENAI_BASE_URL` 和 `OPENAI_MODEL`。 |
| `requirements.txt` | 列出 Python 依赖及版本要求。 |

配方的元素顺序为 `Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr`。训练数据和示例数据使用这些元素列及 `max_power` 列；存在 `abandoned` 列时，按相应读取代码排除值为 1 的样本。

当前 `main.py` 默认读取 `experinced examples.xlsx` 和 `gradient_boosting_model.joblib`，将结果写入 `experinced result/`，包括 `total_examples_pool.csv`、`best_results_per_iteration.csv` 和 `experiment_summary.csv`。新增候选的功率密度来自 GBR 模型预测。

### 绘图脚本与数据来源

以下路径均相对于本目录。

| 脚本 | 输入数据与处理 | 输出图片 |
| --- | --- | --- |
| `plot_a.py` | 读取 `Data.xlsx`，重新训练 GBR 模型，绘制预测值与实验值对比图。 | `experinced plot/Fig8_a.png` |
| `plot_b.py` | 读取 `round2 plot/total_examples_pool.csv`（经验建议方案）和 `round1 plot/total_examples_pool.csv`（传统方案，图例为 `Trad settings`），绘制两种方案的累计最优功率密度收敛曲线。 | `experinced plot/Fig8_b.png` |
| `plot_c.py` | 使用脚本中定义的两组配方比例数组，绘制最终配方对比图；不自动读取 CSV 或提取最优配方。 | `experinced plot/Fig8_c.png` |
| `reproduce_figures.py` | 依次运行 `plot_a.py`、`plot_b.py` 和 `plot_c.py`。 | 以上三个图片文件，统一保存到 `experinced plot/`。 |

`plot_a.py` 独立拟合模型，不加载已有的 `gradient_boosting_model.joblib`；其图中指标基于全部有效样本，包含训练样本。`plot_b.py` 按 `example_id` 排序（若存在该列），以前 10 个样本为第 0 轮，此后每 3 个样本为一轮，最多绘制 50 轮；它不汇总多次实验的均值或标准差。当前主流程的结果目录与绘图输入目录不同，更新主流程结果不会自动更新绘图输入文件。

`plot_c.py` 第二组配方的图例目前仍为 `Random settings-Final formulation`；这是脚本现有的文字标签。本文档将 `plot_b.py` 中的 `round1 plot` 对应方案称为传统方案。

### 使用方式

在本目录中安装依赖：

```powershell
python -m pip install -r requirements.txt
```

运行主动学习前，配置 API 环境变量，并确认 `main.py` 中的示例数据、模型路径和结果目录。主动学习入口为：

```powershell
python main.py
```

仅重新生成三个子图时，确认上述绘图输入文件存在后运行：

```powershell
python reproduce_figures.py
```

需要重新训练并保存回归模型时运行 `python GBR.py`；该脚本会覆盖同名模型文件。`reproduce_figures.py` 不启动主动学习主流程，但会通过 `plot_a.py` 重新拟合绘图所用模型。

