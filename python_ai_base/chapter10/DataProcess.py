"""
数据处理-能够通过json模块对数据进行处理

"""

import json
from operator import pos

from pyecharts.charts import Line
from pyecharts.options import (
    TitleOpts,
    LabelOpts
)

# 读取美国,日本,印度的数据
us_file = open("E:/dev/python/python_ai_base/chapter10/美国.txt","r",encoding="utf-8")
jp_file = open("E:/dev/python/python_ai_base/chapter10/日本.txt","r",encoding="utf-8")
in_file = open("E:/dev/python/python_ai_base/chapter10/印度.txt","r",encoding="utf-8")

us_data = us_file.read()
jp_data = jp_file.read()
in_data = in_file.read()

# 消除前缀
us_data = us_data.replace("jsonp_1629344292311_69436(","")
jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
in_data = in_data.replace("jsonp_1629350745930_63180(","")

# 处理后缀
us_data = us_data[:-2] # 切片,去掉字符串后面两个字符
jp_data = jp_data[:-2] # 切片,去掉字符串后面两个字符
in_data = in_data[:-2] # 切片,去掉字符串后面两个字符

# 将json转化为dict
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend key
us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]

# 获取日期数据,用于x轴,到2020年(到314下标结束)
us_x_data = us_trend_data["updateDate"][:314]
jp_x_data = jp_trend_data["updateDate"][:314]
in_x_data = in_trend_data["updateDate"][:314]

# 获取确诊数据,用于y轴,取2020年(到314下标结束)
us_y_data = us_trend_data["list"][0]["data"][:314]
jp_y_data = jp_trend_data["list"][0]["data"][:314]
in_y_data = in_trend_data["list"][0]["data"][:314]

# 生成图表,构建折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(us_x_data) # x轴是公用的,所以使用一个国家的数据即可
# 添加y轴数据
line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))

# 全局配置选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图",pos_left="center",pos_bottom="1%")
)

# 渲染
line.render()


# 关闭文件对象
us_file.close()
jp_file.close()
in_file.close()

