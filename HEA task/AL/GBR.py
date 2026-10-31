import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import joblib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# 读取数据
a = pd.read_excel(ROOT / 'Data.xlsx')

# 数据预处理：过滤有效样本
ab = a['abandoned'].to_numpy() != 1
print(ab.sum())
y = a['max_power'].to_numpy()
a1 = a[['Pd','Pt','Cu','Au','Ir','Ce','Nb','Cr']].to_numpy()

# 应用过滤
a1 = a1[ab]
y = y[ab]

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(a1, y, test_size=0.4, random_state=42)
model = GradientBoostingRegressor(n_estimators=4096, random_state=0, learning_rate=1e-2,verbose=1)
model.fit(X_train, y_train)

# 测试集预测和评估
y_pred_test = model.predict(X_test)
print("测试集平均绝对误差:", np.abs(y_test - y_pred_test).mean())
print("测试集相关系数:", np.corrcoef(y_test, y_pred_test)[0, 1])

# 全数据集预测
y_pred_all = model.predict(a1)
print("全数据集预测最大值:", max(y_pred_all))

joblib.dump(model, ROOT / 'gradient_boosting_model.joblib')
print("模型保存成功！")