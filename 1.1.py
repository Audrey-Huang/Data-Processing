from matplotlib import pyplot
import csv

#绘制柱状图
def drawBar(related_same_day_band):
    xticks = ['[]','["starbucks"]','["walmart"]','Other']
    brandGroup = {}
    count = 0
    for brands in related_same_day_band:
        brandGroup[brands] = brandGroup.get(brands, 0) + 1
        count=count+1
    brandGroup['Other'] = count-brandGroup.get('[]', 0)-brandGroup.get('["starbucks"]', 0)-brandGroup.get('["walmart"]', 0)
    #创建柱状图
    #第一个参数为柱的横坐标
    #第二个参数为柱的高度
    #参数align为柱的对齐方式，以第一个参数为参考标准
    pyplot.bar(range(4), [brandGroup.get(xtick, 0) for xtick in xticks], align='center')

    #设置柱的文字说明
    #第一个参数为文字说明的横坐标
    #第二个参数为文字说明的内容
    pyplot.xticks(range(4), xticks)

    #设置横坐标的文字说明
    pyplot.xlabel('related_same_day_band')
    #设置纵坐标的文字说明
    pyplot.ylabel('Frequency')
    #设置标题
    pyplot.title('related_same_day_band')
    #绘图
    pyplot.show()

with open('D:\\BIT\Course\\数据挖掘\\visit-patterns-by-census-block-group\\cbg_patterns.csv',encoding='UTF-8') as csv_file:
    row = csv.reader(csv_file, delimiter=',')
    next(row)  # 读取首行
    related_same_day_band = []
    for r in row:
        if r[0]=='':
            continue
        related_same_day_band.append(r[8])

drawBar(related_same_day_band)