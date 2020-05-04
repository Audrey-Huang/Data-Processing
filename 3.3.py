import pandas as pd
from numpy import *
from pandas import Series,DataFrame,np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
data = pd.read_csv('cbg_patterns.csv',encoding='UTF-8')
data['distance_from_home'].replace(' ',np.NAN)
# 将空值形式的缺失值转换成可识别的类型
#n为被插值位置，k为取前后的数据个数
def ployinter(n,k=50):
	y = data['distance_from_home'][list(range(n-k,n)) + list(range(n+1,n+1+k))]
	y = y[y.notnull()] #剔除空值
	return lagrange(y.index,list(y))(n)
#逐个元素判断是否需要插值
for j in range(len(data['distance_from_home'])):
	if(data['distance_from_home'].isnull())[j]:
			data['distance_from_home'][j]= ployinter(j)
print(data['distance_from_home'])
#绘制缺失数据处理后散点图
x = data['raw_visit_count']
y = data['raw_visitor_count']
z= data['distance_from_home']
ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
#  将数据点分成三部分画，在颜色上有区分度
ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
ax.scatter(x[30:40], y[30:40], z[30:40], c='g')
ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()


