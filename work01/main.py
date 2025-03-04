import time

size = 10000  # 矩阵的大小 10000x10000

# 使用list创建矩阵并测量时间
start_list = time.time()
matrix_list = [[i * size + j for j in range(size)] for i in range(size)]
end_list = time.time()
list_creation_time = end_list - start_list
print(f"生成列表矩阵耗时: {list_creation_time} 秒")

# 使用tuple创建矩阵并测量时间
start_tuple = time.time()
matrix_tuple = tuple(tuple(row) for row in matrix_list)
end_tuple = time.time()
tuple_creation_time = end_tuple - start_tuple
print(f"生成元组矩阵耗时: {tuple_creation_time} 秒")

# 遍历并修改列表矩阵中的元素
start_list_mod = time.time()
for i in range(size):
    for j in range(size):
        matrix_list[i][j] += 1
end_list_mod = time.time()
list_modification_time = end_list_mod - start_list_mod
print(f"修改列表矩阵耗时: {list_modification_time} 秒")

# 遍历并修改元组矩阵中的元素（注意：元组是不可变的，因此需要重新生成）
start_tuple_mod = time.time()
matrix_tuple_modified = []
for row in matrix_tuple:
    modified_row = tuple(element + 1 for element in row)
    matrix_tuple_modified.append(modified_row)
end_tuple_mod = time.time()
tuple_modification_time = end_tuple_mod - start_tuple_mod
print(f"修改元组矩阵耗时: {tuple_modification_time} 秒")

# 输出结果
print("\n总结:")
print(f"生成列表矩阵耗时: {list_creation_time} 秒")
print(f"生成元组矩阵耗时: {tuple_creation_time} 秒")
print(f"修改列表矩阵耗时: {list_modification_time} 秒")
print(f"修改元组矩阵耗时: {tuple_modification_time} 秒")