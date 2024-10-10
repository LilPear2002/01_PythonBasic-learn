# 小黎专属python固定模板
# 开发时间：2024/7/12 13:35

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
# 创建柱状图对象
bar = Bar()
# 添加x轴数据
bar.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
bar.add_yaxis("GDP", [30, 20, 10],label_opts=LabelOpts(position="right"))
# 翻转xy轴
bar.reversal_axis()
# 绘图
bar.render("基础柱状图.html")
