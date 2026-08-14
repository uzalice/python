"""
基础时间线柱状图
"""

from pyecharts.charts import Bar,Timeline
from pyecharts.options import *

# 2021年GDP
# 使用Bar()构建基础柱状图
bar1 = Bar()
# 添加x轴数据
bar1.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right")) # 标签位置在右边
# 反转x和y轴
bar1.reversal_axis()

# 2022年GDP
# 使用Bar()构建基础柱状图
bar2 = Bar()
# 添加x轴数据
bar2.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
bar2.add_yaxis("GDP",[80,40,30],label_opts=LabelOpts(position="right")) # 标签位置在右边
# 反转x和y轴
bar2.reversal_axis()

# 创建时间线对象
timeLine = Timeline()

# TimeLine对象添加bar柱状图
timeLine.add(bar1,"2021年GDP")
timeLine.add(bar2,"2022年GDP")

# 设置自动播放
timeLine.add_schema(
    play_interval=1000, # 自动播放时间间隔，时间单位为毫秒
    is_timeline_show=True, # 是否在自动播放时显示时间线
    is_auto_play=True, # 是否自动播放
    is_loop_play=True, # 是否循环自动播放
)

timeLine.render("基础柱状图-时间线.html")
