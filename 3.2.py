import pandas as pd
from pandas import Series,DataFrame,np
from scipy import stats
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
data = pd.read_csv('cbg_patterns.csv',encoding='UTF-8')
# 将空值形式的缺失值转换成可识别的类型
data = data.replace(' ', np.NaN)
#众数填充
data['distance_from_home'] = data['distance_from_home'].fillna(stats.mode(data['distance_from_home'])[0][0])
print('众数为：',stats.mode(data['distance_from_home'])[0][0])
print('填充后数据列表',data['distance_from_home'])

#绘制缺失数据处理后散点图
x = data['raw_visit_count']
y = data['date_range_end']
z= data['raw_visitor_count']
ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
#  将数据点分成三部分画，在颜色上有区分度
ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
ax.scatter(x[30:40], y[30:40], z[30:40], c='g')
ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()