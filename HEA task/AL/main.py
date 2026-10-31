import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime
from pathlib import Path
from initial import load_high_pd_examples_from_excel
from LLM import LLMWrapper
from KDAS import K_DAS_Algorithm
from prompt import inverse_design_prompt, power_density_prediction_prompt, calculate_target_power_density
import warnings

warnings.filterwarnings('ignore')


# ============================ 超参数配置 ============================
ROOT = Path(__file__).resolve().parent


class Config:
    # 文件路径配置
    EXAMPLES_DATA_PATH = str(ROOT / 'experinced examples.xlsx')
    MODEL_PATH = str(ROOT / 'gradient_boosting_model.joblib')
    RESULTS_DIR = str(ROOT / "experinced result")

    # 主动学习循环参数
    NUM_ITERATIONS = 50
    KDAS_CYCLES = 10
    TOP_K = 3

    # 示例选择参数
    HIGH_PD_EXAMPLES_TOP_N = 5
    SIMILAR_EXAMPLES_K = 3


    # UCB采集函数参数
    UCB_EXPLORATION_WEIGHT = 1

    # LLM预测参数
    LLM_NUM_PREDICTIONS = 3

    # 停止条件
    PERFORMANCE_THRESHOLD = 190.0

    # KDAS算法参数
    KDAS_CANDIDATE_SAMPLES = 10000
    KDAS_ALPHA_PARAMS = np.ones(8)  # 狄利克雷分布参数


class CatalystActiveLearningSystem:
    def __init__(self, config=Config()):
        """
        初始化催化剂主动学习系统

        参数:
        - config: 配置对象，包含所有超参数
        """
        self.config = config

        # 加载初始数据和高功率密度示例
        self.examples = load_high_pd_examples_from_excel(config.EXAMPLES_DATA_PATH)
        self.best_power_density = max([ex['power_density'] for ex in self.examples])

        # 加载训练好的GBR模型
        self.gbr_model = joblib.load(config.MODEL_PATH)

        # 初始化LLM包装器
        self.llm = LLMWrapper()

        # 记录实验过程
        self.experiment_log = []
        self.all_examples_log = []  # 记录所有示例的完整历史

        # 创建结果保存目录
        os.makedirs(config.RESULTS_DIR, exist_ok=True)

        print(f"系统初始化完成: 加载{len(self.examples)}个示例, 当前最佳功率密度: {self.best_power_density:.4f}")

    def get_high_pd_examples(self, top_n=None):
        """获取功率密度最高的top_n个示例"""
        if top_n is None:
            top_n = self.config.HIGH_PD_EXAMPLES_TOP_N
        sorted_examples = sorted(self.examples, key=lambda x: x['power_density'], reverse=True)
        return sorted_examples[:top_n]

    def find_similar_examples(self, candidate_ratio, k=None):
        """
        在现有示例中寻找与候选配比最相似的k个示例
        使用欧氏距离作为相似度度量
        """
        if k is None:
            k = self.config.SIMILAR_EXAMPLES_K

        candidate_array = np.array(candidate_ratio)
        distances = []

        for example in self.examples:
            example_array = np.array(example['catalyst_ratio'])
            # 计算欧氏距离
            distance = np.linalg.norm(candidate_array - example_array)
            distances.append((distance, example))

        # 按距离排序，取前k个最相似的
        distances.sort(key=lambda x: x[0])
        return [ex for _, ex in distances[:k]]

    def ucb_acquisition(self, mean, std, exploration_weight=None):
        """上置信界(UCB)采集函数"""
        if exploration_weight is None:
            exploration_weight = self.config.UCB_EXPLORATION_WEIGHT
        return mean + exploration_weight * std

    def predict_with_llm_committee(self, catalyst_ratio, similar_examples, num_predictions=None):
        """
        使用LLM进行预测，返回多次预测的统计量
        """
        if num_predictions is None:
            num_predictions = self.config.LLM_NUM_PREDICTIONS

        prompt = power_density_prediction_prompt(catalyst_ratio, similar_examples)

        pred_values = []
        for _ in range(num_predictions):
            try:
                pred_value = self.llm.predict_power_density(prompt)
                if isinstance(pred_value, list):
                    # 如果返回的是列表，取第一个值
                    pred_value = pred_value[0] if pred_value else 0.5
                pred_values.append(float(pred_value))
            except Exception as e:
                print(f"LLM预测失败: {e}, 使用默认值0.5")
                pred_values.append(0.5)

        # 计算统计量
        mean_val = np.mean(pred_values) if pred_values else 0.5
        std_val = np.std(pred_values, ddof=1) if len(pred_values) > 1 else 0.1

        return {
            'values': pred_values,
            'mean': mean_val,
            'std': std_val
        }

    def validate_catalyst_ratio(self, ratio):
        """验证催化剂配比的合理性"""
        ratio_array = np.array(ratio)

        # 检查是否为八维向量
        if len(ratio_array) != 8:
            return False, "配比维度不正确"

        # 检查总和是否为1（允许微小误差）
        if not (0.99 <= sum(ratio_array) <= 1.01):
            return False, "配比总和不为1"

        # 检查所有值是否非负
        if any(x < 0 for x in ratio_array):
            return False, "存在负值配比"

        return True, "验证通过"

    def save_total_examples_to_csv(self):
        data = []
        for i, example in enumerate(self.examples):
            row = {
                'example_id': i + 1,
                'Pd': example['catalyst_ratio'][0],
                'Pt': example['catalyst_ratio'][1],
                'Cu': example['catalyst_ratio'][2],
                'Au': example['catalyst_ratio'][3],
                'Ir': example['catalyst_ratio'][4],
                'Ce': example['catalyst_ratio'][5],
                'Nb': example['catalyst_ratio'][6],
                'Cr': example['catalyst_ratio'][7],
                'power_density': example['power_density'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            data.append(row)

        df = pd.DataFrame(data)
        file_path = os.path.join(self.config.RESULTS_DIR, "total_examples_pool.csv")
        df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"总样本池已保存: {file_path}")

    def save_best_results_to_csv(self):
        """保存每轮最佳结果"""
        if not self.experiment_log:
            return

        # 准备数据
        data = []
        for log_entry in self.experiment_log:
            best_example = max(log_entry['top_candidates'],
                               key=lambda x: x['power_density'])

            row = {
                'iteration': log_entry['iteration'],
                'best_power_density': log_entry['new_best_power_density'],
                'Pd': best_example['catalyst_ratio'][0],
                'Pt': best_example['catalyst_ratio'][1],
                'Cu': best_example['catalyst_ratio'][2],
                'Au': best_example['catalyst_ratio'][3],
                'Ir': best_example['catalyst_ratio'][4],
                'Ce': best_example['catalyst_ratio'][5],
                'Nb': best_example['catalyst_ratio'][6],
                'Cr': best_example['catalyst_ratio'][7],
                'examples_count': log_entry['examples_count'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            data.append(row)

        # 创建DataFrame并保存为CSV
        df = pd.DataFrame(data)
        file_path = os.path.join(self.config.RESULTS_DIR, "best_results_per_iteration.csv")
        df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"最佳结果已保存: {file_path}")

    def run_active_learning_cycle(self, num_iterations=None, kdas_cycles=None, top_k=None):
        """
        运行主动学习循环

        参数:
        - num_iterations: 主循环迭代次数（如为None则使用配置值）
        - kdas_cycles: 每轮K-DAS算法选择点数（如为None则使用配置值）
        - top_k: 每轮最终选择的顶级候选点数（如为None则使用配置值）
        """
        # 使用配置值或参数值
        num_iterations = num_iterations or self.config.NUM_ITERATIONS
        kdas_cycles = kdas_cycles or self.config.KDAS_CYCLES
        top_k = top_k or self.config.TOP_K

        print(f"\n开始主动学习循环，共{num_iterations}轮迭代")
        print("=" * 50)

        for iteration in range(num_iterations):
            print(f"\n第 {iteration + 1}/{num_iterations} 轮迭代")
            print("-" * 30)

            # 1. 获取高功率密度示例和当前最佳值
            high_pd_examples = self.get_high_pd_examples()
            current_best_pd = self.best_power_density
            target_pd = calculate_target_power_density(current_best_pd)

            print(f"当前最佳功率密度: {current_best_pd:.4f}")
            print(f"目标功率密度: {target_pd:.4f}")

            # 2. LLM生成目标催化剂配比
            design_prompt = inverse_design_prompt(target_pd, high_pd_examples)
            generated_design_text = self.llm.generate_catalyst_ratio(design_prompt)
            generated_ratio = self.llm.extract_catalyst_ratio(generated_design_text)

            # 验证生成的配比
            is_valid, validation_msg = self.validate_catalyst_ratio(generated_ratio)
            if not is_valid:
                print(f"配比验证失败，使用随机配比")
                generated_ratio = self.llm._generate_random_ratio()

            print(f"生成目标配比成功")

            # 3. K-DAS算法选择候选点
            kdas = K_DAS_Algorithm(target_point=np.array(generated_ratio))
            all_selected_points = []

            for kdas_iter in range(kdas_cycles):
                # 生成候选样本（狄利克雷分布）
                candidate_samples = np.random.dirichlet(self.config.KDAS_ALPHA_PARAMS,
                                                        self.config.KDAS_CANDIDATE_SAMPLES)

                # 使用K-DAS选择点
                selected = kdas.select_points(candidate_samples, 1)
                all_selected_points.extend(selected)
                kdas.selected_points.extend(selected)

            print(f"K-DAS生成候选点: {len(all_selected_points)}个")

            # 4. 对每个候选点进行LLM预测和UCB评分
            candidate_predictions = []

            for i, point in enumerate(all_selected_points):
                point_ratio = point.tolist()

                # 寻找相似示例
                similar_examples = self.find_similar_examples(point_ratio)

                # LLM预测
                prediction_result = self.predict_with_llm_committee(point_ratio, similar_examples)

                # 计算UCB得分
                ucb_score = self.ucb_acquisition(prediction_result['mean'], prediction_result['std'])

                candidate_predictions.append({
                    'ratio': point_ratio,
                    'prediction': prediction_result,
                    'ucb_score': ucb_score
                })

            # 5. 选择UCB得分最高的top_k个点
            candidate_predictions.sort(key=lambda x: x['ucb_score'], reverse=True)
            top_candidates = candidate_predictions[:top_k]

            print(f"UCB筛选Top-{top_k}候选点")

            # 6. 使用GBR模型验证并获取最终预测值
            new_examples = []
            for i, candidate in enumerate(top_candidates):
                ratio_array = np.array(candidate['ratio']).reshape(1, -1)

                # GBR模型预测
                gbr_prediction = float(self.gbr_model.predict(ratio_array)[0])

                # 创建新示例
                new_example = {
                    'catalyst_ratio': candidate['ratio'],
                    'power_density': gbr_prediction
                }
                new_examples.append(new_example)

                print(f"候选点{i + 1} GBR预测: {gbr_prediction:.4f}")

            # 7. 更新示例集合
            self.examples.extend(new_examples)
            new_best = max([ex['power_density'] for ex in new_examples])
            if new_best > self.best_power_density:
                self.best_power_density = new_best

            # 记录实验日志
            log_entry = {
                'iteration': iteration + 1,
                'generated_target_ratio': generated_ratio,
                'top_candidates': new_examples,
                'new_best_power_density': self.best_power_density,
                'examples_count': len(self.examples)
            }
            self.experiment_log.append(log_entry)

            # 保存本轮结果到CSV文件
            self.save_total_examples_to_csv()
            self.save_best_results_to_csv()

            print(f"本轮完成: 新增{len(new_examples)}样本, 最佳功率密度: {self.best_power_density:.4f}")

            # 检查停止条件
            if self.best_power_density >= self.config.PERFORMANCE_THRESHOLD:
                print("达到性能阈值，终止迭代")
                break

        return self.experiment_log

    def save_final_summary(self):
        """保存最终总结"""
        summary = {
            'final_best_power_density': [self.best_power_density],
            'total_examples_count': [len(self.examples)],
            'total_iterations': [len(self.experiment_log)],
            'completion_time': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        }

        df = pd.DataFrame(summary)
        file_path = os.path.join(self.config.RESULTS_DIR, "experiment_summary.csv")
        df.to_csv(file_path, index=False, encoding='utf-8')

        print(f"实验总结已保存: {file_path}")


def main():
    """主函数"""
    print("催化剂主动学习系统启动")
    print("=" * 40)

    try:
        # 初始化配置和系统
        config = Config()
        system = CatalystActiveLearningSystem(config)

        # 运行主动学习循环
        experiment_log = system.run_active_learning_cycle()

        # 保存最终总结
        system.save_final_summary()

        # 输出最终结果
        print(f"\n主动学习完成")
        print("=" * 40)
        print(f"最终最佳功率密度: {system.best_power_density:.4f}")
        print(f"总示例数量: {len(system.examples)}")
        print(f"迭代轮数: {len(experiment_log)}")

        # 显示最佳配方
        best_example = max(system.examples, key=lambda x: x['power_density'])
        print(f"\n最佳催化剂配比:")
        metals = ['Pd', 'Pt', 'Cu', 'Au', 'Ir', 'Ce', 'Nb', 'Cr']
        for metal, ratio in zip(metals, best_example['catalyst_ratio']):
            print(f"{metal}: {ratio:.4f}")
        print(f"最佳功率密度: {best_example['power_density']:.4f}")

    except Exception as e:
        print(f"系统运行错误: {e}")


if __name__ == "__main__":
    main()
