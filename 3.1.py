from plotly import offline
import plotly.graph_objs as go
import numpy as np
import pandas as pd
def graph(data,filename):
    d = data['census_block_group']
    x = data['date_range_start']
    y = data['date_range_end']
    z = data['distance_from_home']
    xt = []
    yt = []
    zt = []
    data = []

    for i in range(0, len(x)):
        if i == len(x) - 1 or d[i] != d[i + 1]:
            data.append(go.Scatter3d(x=xt, y=yt, z=zt, mode='markers',
                                     marker=dict(), name=str(d[i])))
            xt = []
            yt = []
            zt = []
        else:
            xt.append(x[i])
            yt.append(y[i])
            zt.append(z[i])
    layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0))
    fig = go.Figure(data=data, layout=layout)
    offline.plot(fig, filename=filename, auto_open=False)

data = pd.read_csv('cbg_patterns.csv',encoding='UTF-8')
# 将空值形式的缺失值转换成可识别的类型
data = data.replace(' ', np.NaN)
print(data.columns)
#将每列中缺失值的个数统计出来
null_all = data.isnull().sum()
print(null_all)
#查看census_block_group列有缺失值的数据
a_null = data[pd.isnull(data['census_block_group'])]
#census_block_group列缺失占比
a_ratio = len(data[pd.isnull(data['census_block_group'])])/len(data) #0.0007
#丢弃缺失值,将存在缺失值的行丢失
new_drop = data.dropna(axis=0)
print(data.shape)
print(new_drop.shape)
graph(data,'D:\BIT\Course\数据挖掘\data processe\graph.html')
graph(new_drop,'D:\BIT\Course\数据挖掘\data processe\graph1.html')
#丢弃某几列有缺失值的行
#new_drop2 = data.dropna(axis=0, subset=['census_block_group','distance_from_home'])
#print(new_drop2.shape)#(9990,6)
