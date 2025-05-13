

#第三次作业


import functools
import statistics
import math
from typing import List, Callable


def stats_decorator(metrics: List[str] = None) -> Callable:
    """带参数的装饰器工厂函数，动态选择统计指标

    :param metrics: 需要计算的统计指标列表，可选值：SUM, AVG, VAR, RMS
    """
    # 设置默认计算全部指标
    if metrics is None:
        metrics = ['SUM', 'AVG', 'VAR', 'RMS']
    else:
        metrics = [m.upper() for m in metrics]

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            results = {}

            # 根据参数计算统计指标
            if 'SUM' in metrics:
                results['SUM'] = sum(data)

            if 'AVG' in metrics:
                try:
                    results['AVG'] = statistics.mean(data)
                except statistics.StatisticsError:
                    results['AVG'] = 0.0

            if 'VAR' in metrics:
                try:
                    results['VAR'] = statistics.variance(data)
                except statistics.StatisticsError:
                    results['VAR'] = 0.0

            if 'RMS' in metrics:
                if data:
                    squared = [x ** 2 for x in data]
                    results['RMS'] = math.sqrt(sum(squared) / len(data))
                else:
                    results['RMS'] = 0.0

            # 格式化输出结果
            print("\n=== 统计结果 ===")
            for metric, value in results.items():
                print(f"{metric}: {value:.4f}")
            print("================\n")

            return data  # 保持返回原始数据

        return wrapper

    return decorator


# 使用示例
@stats_decorator(metrics=['sum', 'avg', 'rms'])  # 参数不区分大小写
def datasampling():
    """随机数据生成函数"""
    import random
    return [random.gauss(0, 1) for _ in range(20)]  # 生成正态分布数据


# 测试不同参数组合
@stats_decorator()  # 默认计算全部指标
def full_stat_data():
    import random
    return [random.randint(1, 100) for _ in range(15)]


if __name__ == "__main__":
    print("示例1：自定义指标")
    data1 = datasampling()
    print("原始数据样例:", data1[:5], "...\n")

    print("\n示例2：全量指标")
    data2 = full_stat_data()
    print("原始数据样例:", data2[:5], "...")
