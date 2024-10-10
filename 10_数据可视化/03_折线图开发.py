# 小黎专属python固定模板
# 开发时间：2024/7/8 22:32
import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts

f_us = open("D:\\pycharm_workspace\\01_PythonBasic-learn\\10_数据可视化\美国.txt", "r", encoding="UTF-8")
f_jp = open("D:\\pycharm_workspace\\01_PythonBasic-learn\\10_数据可视化\日本.txt", "r", encoding="UTF-8")
f_in = open("D:\\pycharm_workspace\\01_PythonBasic-learn\\10_数据可视化\印度.txt", "r", encoding="UTF-8")
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()
# 去除不符合规范的内容
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# JSON转字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']
# 获取日期数据用于x轴的数据 取2020年
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]
# 获取日期数据用于y轴的数据 取2020年
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表
# 创建对象
line = Line()
# x轴数据
line.add_xaxis(us_x_data)
# y轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))
# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%"),
)

# 生成图表
line.render()

# 关闭文件对象
f_us.close()
f_jp.close()
f_in.close()
