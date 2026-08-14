"""
动态柱状图绘制
 - 掌握列表的sort方法并配合lambda匿名函数完成列表排序
 - 完成图标所需的数据处理
 - 完成GDP动态图表配置

要求：
 - GDP数据处理为亿级
 - 有时间轴，按照年份为时间轴的点
 - x和y轴反转，同时每一年的数据只要前八名国家
 - 有标题，标题的年份会动态更改
 - 设置主题为LIGHT
"""

import json
from pyecharts.charts import Bar,Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *

# 打开文件
file = open("E:/dev/python/python_ai_base/chapter12/1960-2019全球GDP数据.csv","r",encoding="GB2312")

# 读取数据
file_data = file.readlines()

# 关闭文件
file.close()

# 去除第一条消息
file_data.pop(0)

# print(type(file_data)) # <class 'list'>
# 数据都是一行一行的字符串，例如：1960,美国,5.433e+11

# 将数据转换为字典存储，格式为：
# { 年份: [ [国家, gdp], [国家,gdp], ......  ], 年份: [ [国家, gdp], [国家,gdp], ......  ], ...... }
# { 1960: [ [美国, 123], [中国,321], ......  ], 1961: [ [美国, 123], [中国,321], ......  ], ...... }
data_dict = {}
for line in file_data:
    # split()
    parts = line.split(",")
    year = int(parts[0]) # 年份
    country = parts[1] # 城市
    gdp = float(parts[2]) # GDP
    # 处理字典里指定年份为空
    # try:
    #     data_dict[year].append([country,gdp])
    # except KeyError:
    #     data_dict[year] = []
    #     data_dict[year].append([country,gdp])
    if year not in data_dict:
        data_dict[year] = []
    data_dict[year].append([country,gdp])


# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})

# 排序年份
sorted_keys_list = sorted(data_dict.keys())
for year in sorted_keys_list:
    # 前8的国家
    data_dict[year].sort(key=lambda element : element[1],reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # x轴添加国家
        y_data.append(country_gdp[1] / 100000000)  # y轴添加gdp数据

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转x轴和y轴
    bar.reversal_axis()
    # 设置每一年的图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(pos_top="5%",title=f"{year}年全球前8GDP数据"),
        # 新增：调整图例到顶部居中，彻底避开底部时间轴
        legend_opts=LegendOpts(
            pos_top="5%",  # 距离图表顶部 5% 的位置
            pos_left="right"  # 水平居中显示
        )
    )
    timeline.add(bar, str(year))

# for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
# 在for中，将每一年的bar对象添加到时间线中

# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
# 绘图
timeline.render("1960-2019全球GDP前8国家.html")