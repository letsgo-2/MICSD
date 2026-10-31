import numpy as np


class K_DAS_Algorithm:
    def __init__(self, target_point, lambda_param=0.5, sigma=1.0):
        """
               初始化K-DAS算法

               参数:
               - target_point: 目标点r (八维向量)
               - lambda_param: 权衡参数λ，控制相关性与多样性的平衡
               - sigma: 高斯核函数的带宽参数
        """
        self.target = target_point
        self.lambda_param = lambda_param
        self.sigma = sigma
        self.selected_points = []

    def gaussian_kernel(self, x, y):
        """高斯核函数 k(x, y) = exp(-||x-y||^2 / (2*sigma^2))"""
        distance_sq = np.sum((x - y) ** 2)
        return np.exp(-distance_sq / (2 * self.sigma ** 2))

    def acquisition_function(self, candidate_point):
        """K-DAS获取函数: α(x) = λ·k(r,x) - (1-λ)·max_{x_i∈S} k(x, x_i)"""
        relevance_term = self.gaussian_kernel(self.target, candidate_point)

        diversity_penalty = 0
        if self.selected_points:
            diversity_penalty = max([self.gaussian_kernel(candidate_point, xi)
                                     for xi in self.selected_points])

        return (self.lambda_param * relevance_term -
                (1 - self.lambda_param) * diversity_penalty)

    def select_points(self, candidate_samples, num_select):
        """从候选样本中选择得分最高的点"""
        scores = [self.acquisition_function(point) for point in candidate_samples]
        indices = np.argsort(scores)[-num_select:][::-1]
        selected = [candidate_samples[i] for i in indices]
        return selected


def main():
    np.random.seed(42)

    # 定义目标点（八维均匀分布）
    target_point = np.array([0.125] * 8)

    # 初始化K-DAS算法
    kdas = K_DAS_Algorithm(target_point)
    alpha_params = np.ones(8)

    all_selected_points = []

    # 进行10次循环，每次选择1个点
    for _ in range(10):
        # 生成10000个狄利克雷采样点
        candidate_samples = np.random.dirichlet(alpha_params, 10000)

        # 使用K-DAS算法选择1个点
        selected = kdas.select_points(candidate_samples, 1)

        # 将选中的点添加到已选集合中
        kdas.selected_points.extend(selected)
        all_selected_points.extend(selected)

    return all_selected_points


# 运行并输出结果
if __name__ == "__main__":
    result_points = main()

    print("最终生成的10个点集合：")
    for i, point in enumerate(result_points, 1):
        print(f"点{i}: {point} ")