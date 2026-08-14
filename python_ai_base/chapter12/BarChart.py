"""
演示基础柱状图的开发
"""

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 使用Bar()构建基础柱状图
bar = Bar()

# 添加x轴数据
bar.add_xaxis(["中国","美国","英国"])

# 添加y轴数据
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right")) # 标签位置在右边

# 反转x和y轴
bar.reversal_axis()

# 绘图
bar.render("基础柱状图.html")