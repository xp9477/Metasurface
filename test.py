import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('dataset.csv', header=None)
# 取出前16个字段，并拼接为一个字符串
filename = ''.join(df.iloc[0, :16].astype(int).astype(str)) + '.txt'

x1 = np.linspace(12.5, 20, 101)
# 取出后面的所有浮点数数据，并存为列表
y1 = df.iloc[0, 16:].values.tolist()


x2, y2 = [], []
with open(f'D:\\paper2\\zeroone\\origin_data\\{filename}', "r") as f:
    for line in f:
        # 分割每行数据，获取x和y的值
        x_val, y_val = line.strip().split("\t")
        x_val, y_val = float(x_val), float(y_val)
        if x_val >= 12.5 and x_val <= 20:
            x2.append(x_val)
            y2.append(y_val)

# 创建一个画布和一个子图对象
fig, ax = plt.subplots()

ax.plot(x1, y1)
ax.plot(x2, y2)

# 设置子图的标题和坐标轴标签
ax.set_title("Comparison between interpolation data and original data")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")

# 显示图形
plt.show()
