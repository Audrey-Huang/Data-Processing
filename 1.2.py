import csv
import numpy as np
def fiveNumber(nums):
    """五数概括 Minimum（最小值）、Q1、Median（中位数、）、Q3、Maximum（最大值）"""
    Minimum=min(nums)
    Maximum=max(nums)
    Q1=np.percentile(nums,25)
    Median=np.median(nums)
    Q3=np.percentile(nums,75)
    return Minimum,Q1,Median,Q3,Maximum
count=0
with open('D:\\BIT\Course\\数据挖掘\\visit-patterns-by-census-block-group\\cbg_patterns.csv',encoding='UTF-8') as csv_file:
    row = csv.reader(csv_file, delimiter=',')
    next(row)  # 读取首行
    nums = []
    for r in row:
        if r[0]=='':
            count=count+1
            continue
        nums.append(float(r[0]))  # 将字符串数据转化为浮点型加入到数组之中
print('缺失数据个数为：',count)
print('5数概括为:',fiveNumber(nums))