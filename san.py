import numpy as np
import functools


# 定义装饰器
def stats_decorator(*stats):
    """
    带参数的装饰器，用于对函数生成的样本集进行统计操作。
    参数：
        *stats: 可变参数，允许传入 'SUM'、'AVG'、'VAR'、'RMSE' 的任意组合。
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 调用原函数获取样本数据
            data = func(*args, **kwargs)

            # 确保数据是数值型数据
            if not isinstance(data, (list, tuple, np.ndarray)):
                raise ValueError("数据必须是列表、元组或numpy数组形式")

            # 初始化结果字典
            result = {}

            # 计算统计项
            if 'SUM' in stats:
                result['SUM'] = np.sum(data)
            if 'AVG' in stats:
                result['AVG'] = np.mean(data)
            if 'VAR' in stats:
                result['VAR'] = np.var(data)
            if 'RMSE' in stats:
                mean = np.mean(data)
                mse = np.mean((np.array(data) - mean) ** 2)
                result['RMSE'] = np.sqrt(mse)

            # 返回统计结果
            return result

        return wrapper

    return decorator


# 示例函数
@stats_decorator('SUM', 'AVG', 'VAR', 'RMSE')
def generate_data():
    """
    示例函数，生成一个包含数值型数据的列表。
    """
    import random
    return [random.randint(1, 100) for _ in range(10)]


# 测试
result = generate_data()
print(result)