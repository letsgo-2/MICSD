import pandas as pd
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_high_pd_examples_from_excel(file_path=ROOT / 'experinced examples.xlsx'):

    # 读取Excel文件
    df = pd.read_excel(file_path)

    # 数据预处理：过滤掉abandoned列为1的样本
    df_valid = df[df['abandoned'] != 1] if 'abandoned' in df.columns else df

    # 提取所需的列：八种金属的配比和最大功率
    ratios_array = df_valid[['Pd', 'Pt', 'Cu', 'Au', 'Ir', 'Ce', 'Nb', 'Cr']].to_numpy()
    power_densities = df_valid['max_power'].to_numpy()


    examples = []
    for i in range(len(ratios_array)):
        # 将每行数据转换为目标字典格式
        example = {
            'catalyst_ratio': ratios_array[i].tolist(),  # 将numpy数组转换为列表
            'power_density': float(power_densities[i])  # 确保功率密度为浮点数
        }
        examples.append(example)

    return examples




# 使用示例
if __name__ == "__main__":

    examples = load_high_pd_examples_from_excel()

    print(f"成功加载 {len(examples)} 条有效数据。")

    # 打印前两条数据作为示例
    for i, example in enumerate(examples[:5]):
        print(f"示例 {i + 1}: {example}")

