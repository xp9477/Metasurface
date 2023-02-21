import os
import glob
import csv
import numpy as np

# 定义要遍历的文件夹路径
folder_path = "D:\\paper2\\zeroone\\origin_data"

# 使用glob模块获取所有txt文件的路径列表
txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

# 创建一个空列表，用于存储所有的数据
all_data = []

# 遍历所有txt文件，并逐个读取文件内容提取坐标点
for file_path in txt_files:
    # 从文件路径中提取文件名
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    # 将文件名转换为一个列表，每个元素为0或1
    file_name_list = [int(digit) for digit in file_name]
    # 读取文件内容，并逐行处理
    x, y = [], []
    with open(file_path, "r") as f:
        for line in f:
            # 分割每行数据，获取x和y的值
            x_val, y_val = line.strip().split("\t")
            x_val, y_val = float(x_val), float(y_val)
            if x_val >= 12.5 and x_val <= 20:
                y.append(y_val)
    # 对当前文件的符合条件的坐标点进行插值操作，生成101个点
    y_interp = np.interp(np.linspace(0, 1, 101), np.linspace(0, 1, len(y)), y)
    # 将当前文件的101个采样点和对应的y值组成一行数据，并添加到所有数据的列表中
    all_data.append(file_name_list + y_interp.tolist())

# 将所有数据写入CSV文件中
with open("dataset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # 逐行写入数据
    for line_data in all_data:
        writer.writerow(line_data)

# 提示数据写入完成
print("Data saved to dataset.csv")
