import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


FONT_FAMILY = ["Arial", "Helvetica", "DejaVu Sans"]
FONT_BASE = 11
FONT_TICK = 11
FONT_LABEL = 13

AXES_LW = 0.9
GRIDLINE = "0.88"  # 淡灰竖线网格
TEXT_DARK = "0.15"  # 深灰字体
OUTLINE = "0.15"  # 描边颜色


def set_publication_style():
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": FONT_FAMILY,
        "font.size": FONT_BASE,

        # ✅ 强制不加粗
        "axes.labelweight": "normal",
        "axes.titleweight": "normal",
        "font.weight": "normal",

        "axes.linewidth": AXES_LW,
        "axes.edgecolor": TEXT_DARK,
        "axes.labelcolor": TEXT_DARK,
        "axes.facecolor": "white",

        "xtick.color": TEXT_DARK,
        "ytick.color": TEXT_DARK,
        "xtick.direction": "in",
        "ytick.direction": "in",

        "figure.dpi": 300,
        "savefig.dpi": 600,
        "savefig.bbox": "tight",
        "savefig.facecolor": "white",

        "legend.fontsize": 10,
        "legend.frameon": True,
        "legend.fancybox": False,
        "legend.edgecolor": "0.8",
        "legend.framealpha": 0.95,
    })


set_publication_style()

# ==========================================
# 2. 数据准备
# ==========================================
METALS = ['Pd', 'Pt', 'Cu', 'Au', 'Ir', 'Ce', 'Nb', 'Cr']
x_coords = np.arange(len(METALS))

# --- Group 1: Experience-based (蓝色系) ---
DATA_EXP = np.array([0.546, 0.141, 0.017, 0.031, 0.012, 0.087, 0.108, 0.056])
LABEL_EXP = "Experience-based suggestions-Final formulation"
COLOR_EXP = "#0066FF"  # 经典高亮蓝

# --- Group 2: Random settings (橙红色系) ---
DATA_RND = np.array([0.431, 0.143, 0.045, 0.008, 0.033, 0.136, 0.187, 0.017])
LABEL_RND = "Random settings-Final formulation"
COLOR_RND = "#FF4500"  # 橙红色

# ==========================================
# 3. 绘图主逻辑
# ==========================================
fig, ax = plt.subplots(figsize=(8, 2))

# --- A. 绘制背景竖线网格 ---
for x in x_coords:
    ax.axvline(x, color=GRIDLINE, linestyle='-', linewidth=1.0, zorder=0)

# --- B. 绘制折线 (均为实线) ---
common_props = dict(
    linewidth=2.2,  # 线宽
    linestyle='-',  # 全部统一为实线
    markeredgecolor=OUTLINE,
    markeredgewidth=0.7,
    alpha=0.90  # 稍微调低一点点透明度，以便观察重叠部分
)

# 1. Experience (蓝色, 圆点)
ax.plot(
    x_coords, DATA_EXP,
    label=LABEL_EXP,
    color=COLOR_EXP,
    marker='o',  # 圆形标记
    markersize=6.5,
    zorder=10,
    **common_props
)

# 2. Random (橙红, 方块)
ax.plot(
    x_coords, DATA_RND,
    label=LABEL_RND,
    color=COLOR_RND,
    marker='s',  # 方形标记 
    markersize=6.5,
    zorder=11,
    **common_props
)

# --- C. 坐标轴与外观清理 ---
ax.set_xticks(x_coords)
ax.set_xticklabels(METALS, fontsize=FONT_TICK, fontweight='normal', color=TEXT_DARK)
ax.set_ylabel("Mass fraction", fontsize=FONT_LABEL, fontweight='normal', labelpad=10, color=TEXT_DARK)

# 隐藏边框
for sp in ax.spines.values():
    sp.set_visible(False)

# 隐藏刻度线
ax.tick_params(axis='x', length=0)
ax.tick_params(axis='y', length=0)

# 范围设置
ax.set_ylim(-0.02, 0.65)
ax.set_yticks([0.0, 0.2, 0.4, 0.6])
ax.set_xlim(-0.5, len(METALS) - 0.5)

# --- D. 添加图例 ---
ax.legend(loc='upper right')

# --- E. 保存 ---
outdir = Path(__file__).resolve().parent / "experinced plot"
outdir.mkdir(exist_ok=True)
save_path = outdir / "Fig8_c.png"
plt.savefig(save_path, dpi=600, bbox_inches='tight')
print(f"图表已保存: {save_path}")
plt.close(fig)
