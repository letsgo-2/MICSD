import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from joblib import load 
import os
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import joblib


# =========================
# 统一绘图风格（与收敛曲线一致）
# =========================
def set_paper_style():
    plt.rcParams.update({
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",

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

        "font.size": 12,
        "axes.labelsize": 14,
        "axes.titlesize": 14,
        "legend.fontsize": 11,

        "axes.grid": False,
        "lines.linewidth": 2.5,
    })


# =========================
# 读取数据
# =========================
ROOT = Path(__file__).resolve().parent
FIGURES = ROOT / 'round2 plot'
FIGURES.mkdir(exist_ok=True)
a = pd.read_excel(ROOT / 'Data.xlsx')

# 数据预处理：过滤有效样本
ab = a['abandoned'].to_numpy() != 1
y = a['max_power'].to_numpy()
a1 = a[['Pd','Pt','Cu','Au','Ir','Ce','Nb','Cr']].to_numpy()

X = a1[ab]
a1 = a1[ab]
y = y[ab]

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(a1, y, test_size=0.2, random_state=19)

model = GradientBoostingRegressor(
    n_estimators=4096,
    random_state=0,
    learning_rate=1e-2,
    verbose=1
)
model.fit(X_train, y_train)



print("正在进行预测...")
y_pred = model.predict(X)

# =========================
# 指标
# =========================
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
mae = mean_absolute_error(y, y_pred)

error = np.abs(y - y_pred)

plot_max = max(y.max(), y_pred.max())
plot_min = min(y.min(), y_pred.min())
padding = 0.05 * (plot_max - plot_min)
x_min = plot_min - padding
x_max = plot_max + padding


# =========================
# 绘图（统一风格）
# =========================
print("正在绘图...")
set_paper_style()

fig, ax = plt.subplots(figsize=(8, 8))

sc = ax.scatter(
    y,
    y_pred,
    c=error,
    cmap="coolwarm",
    s=60,
    alpha=0.8,
    edgecolors="k",
    linewidths=0.5,
)

# Colorbar（也统一一下边框/刻度风格）
cbar = plt.colorbar(sc, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Absolute Error', rotation=270, labelpad=15)
cbar.outline.set_linewidth(1.2)
cbar.ax.tick_params(direction="in", width=1.0, length=5)

# 理想对角线（同款黑虚线）
ax.plot([x_min, x_max], [x_min, x_max], "k--", lw=2, alpha=0.6, label="Ideal")

stats = (
    f'$R^2 = {r2:.3f}$\n'
    f'$RMSE = {rmse:.3f}$\n'
    f'$MAE = {mae:.3f}$'
)

ax.text(
    0.05,
    0.95,
    stats,
    transform=ax.transAxes,
    fontsize=12,
    va="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.9, edgecolor="black", linewidth=1.0),
)


ax.set_xlabel("Exp. P (mW cm$^{-2}$)")
ax.set_ylabel("Pred. P (mW cm$^{-2}$)")

ax.set_xlim(x_min, x_max)
ax.set_ylim(x_min, x_max)
ax.set_aspect("equal")

# 四周边框显式存在（风格一致）
for spine in ax.spines.values():
    spine.set_visible(True)

# legend：无边框、干净
ax.legend(loc="lower right", frameon=False)

plt.tight_layout()

# =========================
# 保存
# =========================
outdir = str(FIGURES)
filename = "Fig8_a.png"
save_path = os.path.join(outdir, filename)

plt.savefig(save_path, dpi=300)
print(f"绘图完成，已保存至: {save_path}")
