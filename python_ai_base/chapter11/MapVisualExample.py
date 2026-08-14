"""
国内疫情地图
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 打开文件
file = open("E:/dev/python/python_ai_base/chapter11/疫情.txt","r",encoding="utf-8")

# 读取数据
file_data = file.read()

# json转换成py中的字典
file_dict_data = json.loads(file_data)

# 处理数据
# 从dict中读取各省份数据
province_data_list = file_dict_data["areaTree"][0]["children"]

# 组装每个省份和确诊人数为元组，并各个省的数据都封装入列表内
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"] # 省份名称
    province_confirm = province_data["total"]["nowConfirm"] # 确诊人数
    data_list.append((province_name,province_confirm))

# 绘制地图
map = Map()

# 添加数据
map.add("全国各省份疫情确诊人数",data_list,"china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100~9999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000~99999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000~99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033"},
        ]
    )
)

# 给文件命名
map.render("全国疫情地图.html")

# 关闭文件
file.close()
