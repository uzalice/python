"""
演示pyecharts的基础入门

首先需要通过前面学习的pip命令快速安装pyecharts模块-这个是Echarts的Python版本

pyecharts模块中有很多配置选项,常用到2个类别的选项:
 - 全局配置选项
    set_global_opts方法-这里全局配置选项可以通过set_global_opts方法来进行配置
     - 配置图表的标题
     - 配置图例
     - 配置鼠标移动效果
     - 配置工具栏
     - 等整体配置项
 - 系列配置选项
"""

# 导包，导入Line功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import (
    TitleOpts,
    LegendOpts,
    VisualMapOpts,
    ToolboxOpts,
    LabelOpts
)

# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
line.add_yaxis("GDP",[30,20,10])
# 全局配置选项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True,pos_bottom="5%",pos_left="center"),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)

# 生成图表
line.render()