import os
import glob
from tqdm import tqdm
import matplotlib.pyplot as plt

# 定义要遍历的文件夹路径
folder_path = "D:\\paper2\\zeroone\\origin_data"

# 使用glob模块获取所有txt文件的路径列表
txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

# 创建一个画布和一个子图对象
fig, ax = plt.subplots()

# 遍历所有txt文件，并逐个读取文件内容画出坐标线
for file_path in tqdm(txt_files, desc="Processing files", unit="file"):
    with open(file_path, "r") as f:
        # 读取文件内容，并逐行处理
        x, y = [], []
        for line in f:
            # 分割每行数据，获取x和y的值
            x_val, y_val = line.strip().split("\t")
            x.append(float(x_val))
            y.append(float(y_val))
        # 将当前文件的坐标点作为一条线绘制到图上
        ax.plot(x, y)

# 设置子图的标题和坐标轴标签
ax.set_title("Line plot of coordinates")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")

# 显示图形
plt.show()
