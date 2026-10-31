from openai import OpenAI
from config import API_KEY, API_BASE_URL, LLM_MODEL
import re
import numpy as np


class LLMWrapper:
    def __init__(self):
        if not API_KEY:
            raise RuntimeError("请先设置环境变量 OPENAI_API_KEY。")
        self.client = OpenAI(api_key=API_KEY, base_url=API_BASE_URL)

    def generate_catalyst_ratio(self, prompt):
        """生成催化剂配比（八维向量）"""
        response = self.client.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content

    def predict_power_density(self, prompt):
        """
        预测功率密度值 (单次预测，带重试机制)
        逻辑: 尝试最多 3 次，一旦获得有效数值立即返回。
        """
        max_retries = 3

        for i in range(max_retries):
            try:
                # API调用
                response = self.client.chat.completions.create(
                    model=LLM_MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.5,  # 稍微降低温度，提高数值稳定性
                    max_tokens=20
                )
                content = response.choices[0].message.content.strip()

                # 使用正则表达式提取数值
                value = None
                patterns = [
                    r"[-+]?\d*\.\d+([eE][-+]?\d+)?",  # 浮点数或科学计数法
                    r"[-+]?\d+",  # 整数
                ]

                for pattern in patterns:
                    match = re.search(pattern, content)
                    if match:
                        try:
                            val_temp = float(match.group(0))
                            # 验证数值范围合理性
                            if 0 <= val_temp <= 500.0:
                                value = val_temp
                                break  # 跳出正则匹配循环
                        except (ValueError, TypeError):
                            continue

                # === 核心修改点 ===
                # 如果获取到了有效值，直接返回这个值，不再继续循环
                if value is not None:
                    return value

                    # 如果没获取到，打印日志并进入下一次重试
                print(f"预测尝试 {i + 1}/{max_retries}: 无效输出 '{content}'，正在重试...")

            except Exception as e:
                print(f"预测尝试 {i + 1}/{max_retries} API错误: {e}")
                continue

        # 如果3次重试都失败了，返回默认值
        print("所有预测尝试均失败，返回默认值 0.5")
        return 0.5

    def extract_catalyst_ratio(self, text):
        """从文本中提取催化剂配比向量"""
        # 匹配八维向量格式
        pattern = r'\[([0-9\.,\s]+)\]'
        match = re.search(pattern, text)

        if match:
            numbers_str = match.group(1)
            # 提取所有数字
            numbers = re.findall(r'\d+\.?\d*', numbers_str)
            if len(numbers) == 8:
                try:
                    ratio = [float(x) for x in numbers]
                    total = sum(ratio)
                    # 归一化确保总和为1
                    if total > 0:
                        return [x / total for x in ratio]
                except (ValueError, TypeError):
                    pass

        # 提取失败时生成随机但合理的配比
        print("无法从文本提取配比，生成随机配比")
        return self._generate_random_ratio()

    def _generate_random_ratio(self):
        """生成随机但偏向重要金属的配比"""
        # 设置不同金属的基础权重（基于催化重要性）
        base_weights = {
            'Pd': 1.5,  # 钯 - 高活性
            'Pt': 1.8,  # 铂 - 高效催化剂
            'Cu': 1.2,  # 铜 - 成本优势
            'Au': 1.0,  # 金 - 稳定性
            'Ir': 1.3,  # 铱 - 耐苛刻条件
            'Ce': 1.1,  # 铈 - 氧化还原增强
            'Nb': 1.0,  # 铌 - 耐久性
            'Cr': 1.0  # 铬 - 选择性氧化
        }

        # 生成随机权重
        weights = [base_weights[metal] * np.random.uniform(0.8, 1.2)
                   for metal in ['Pd', 'Pt', 'Cu', 'Au', 'Ir', 'Ce', 'Nb', 'Cr']]

        # 归一化
        total = sum(weights)
        return [w / total for w in weights]


if __name__ == "__main__":
    wrapper = LLMWrapper()
    prompt = """
You are a robot that accurately predicts the power density of catalytic performance from descriptions of metal alloy ratios in the eight-element chemical space (Pd–Pt–Cu–Au–Ir–Ce–Nb–Cr). The power density reflects the energy output per unit volume or area achieved by the catalyst under standard operating conditions.
**Output Requirement**: Output must be a numerical value in W/cm² or W/kg (e.g., 21.85), representing the power density. No additional text or explanations are allowed.
**Target Catalyst Ratio for Prediction**:[0.18, 0.15, 0.12, 0.10, 0.13, 0.10, 0.12, 0.10]
Predicted Power Density =
"""
    p = wrapper.predict_power_density(prompt)
    print(p)