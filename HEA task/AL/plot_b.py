import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
CSV_ARBITRARY_INIT = r"round2 plot/total_examples_pool.csv"
CSV_EXPERIENCED_RANDOM = r"round1 plot/total_examples_pool.csv"

LABEL_ARBITRARY_INIT = "Experience-based suggestions"
LABEL_EXPERIENCED_RANDOM = "Trad settings"

OUTDIR = str(ROOT / "experinced plot")


N_INIT = 10          # 初始点
BATCH_SIZE = 3       # 每轮新增点
N_ROUNDS = 50        # 采样轮数（acquisition rounds）

# =========================
# 统一绘图风格
# =========================
def set_paper_style():
    plt.rcParams.update({
        # Figure
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",

        # Axes box + ticks (黑框、刻度向内)
        "axes.edgecolor": "black",
        "axes.linewidth": 1.4,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.major.width": 1.2,
        "ytick.major.width": 1.2,
        "xtick.major.size": 6,
        "ytick.major.size": 6,
        "xtick.minor.size": 3,
        "ytick.minor.size": 3,

        # Fonts
        "font.size": 12,
        "axes.labelsize": 14,
        "axes.titlesize": 14,
        "legend.fontsize": 11,

        # No grid (你那张图没网格)
        "axes.grid": False,

        # Lines
        "lines.linewidth": 2.5,
    })


def load_best_so_far_by_rounds(csv_path: str,
                               n_init: int,
                               batch_size: int,
                               n_rounds: int) -> pd.DataFrame:
    """
    x 从 0 开始：
      - round=0: 初始 n_init 个点的 best
      - round=1..n_rounds: 每轮加入 batch_size 个点后的 best
    返回: DataFrame(round, best_so_far)
    """
    csv_path = ROOT / csv_path
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"找不到文件: {csv_path}")

    df = pd.read_csv(csv_path)

    if "power_density" not in df.columns:
        raise ValueError(f"{csv_path} 缺少列 power_density，实际列: {list(df.columns)}")

    # 按采样顺序：优先 example_id，否则保持原顺序
    if "example_id" in df.columns:
        df = df.sort_values("example_id").reset_index(drop=True)
    else:
        df = df.reset_index(drop=True)

    y = df["power_density"].astype(float).to_numpy()

    if len(y) < n_init:
        raise ValueError(f"{csv_path} 数据量不足：len={len(y)} < N_INIT={n_init}")

    # round 0: initial pool
    curr_best = float(np.max(y[:n_init]))
    rec = [{"round": 0, "best_so_far": curr_best}]

    # subsequent rounds
    vals = y[n_init:]
    max_rounds_available = len(vals) // batch_size
    rounds = min(int(n_rounds), int(max_rounds_available))

    for r in range(1, rounds + 1):
        batch = vals[(r - 1) * batch_size: r * batch_size]
        curr_best = max(curr_best, float(np.max(batch)))
        rec.append({"round": r, "best_so_far": curr_best})

    return pd.DataFrame(rec)


def plot_two_convergence(csv_a: str, label_a: str,
                         csv_b: str, label_b: str,
                         outdir: str,
                         n_init: int,
                         batch_size: int,
                         n_rounds: int,
                         filename: str = "Fig8_b.png"):
    os.makedirs(outdir, exist_ok=True)

    a = load_best_so_far_by_rounds(csv_a, n_init, batch_size, n_rounds)
    b = load_best_so_far_by_rounds(csv_b, n_init, batch_size, n_rounds)

    # 统一风格
    set_paper_style()

    fig, ax = plt.subplots(figsize=(10, 7))

    # 两条曲线：用 marker + 实线（更像论文图）
    ax.plot(a["round"], a["best_so_far"], marker="o", markersize=4.0,
            markerfacecolor="white", markeredgewidth=1.1, label=label_a)
    ax.plot(b["round"], b["best_so_far"], marker="o", markersize=4.0,
            markerfacecolor="white", markeredgewidth=1.1, label=label_b)

    ax.set_xlabel("Round")
    ax.set_ylabel(r"Best P (mW cm$^{-2}$)")

    # x 轴从 0 开始
    xmax = int(max(a["round"].max(), b["round"].max()))
    ax.set_xlim(0, xmax)

   
    for spine in ax.spines.values():
        spine.set_visible(True)

    # legend 简洁、无边框
    ax.legend(frameon=False, loc="lower right")

    fig.tight_layout()

    outpath = os.path.join(outdir, filename)
    fig.savefig(outpath, dpi=300)
    plt.close(fig)

    print(f">>> 已保存: {outpath}")


if __name__ == "__main__":
    plot_two_convergence(
        CSV_ARBITRARY_INIT, LABEL_ARBITRARY_INIT,
        CSV_EXPERIENCED_RANDOM, LABEL_EXPERIENCED_RANDOM,
        OUTDIR,
        n_init=N_INIT,
        batch_size=BATCH_SIZE,
        n_rounds=N_ROUNDS,
        filename="Fig8_b.png"
    )
