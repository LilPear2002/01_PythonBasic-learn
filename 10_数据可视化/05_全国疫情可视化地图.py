# 小黎专属python固定模板
# 开发时间：2024/7/11 22:19

# 读取数据文件
import json

from pyecharts.charts import Map
from pyecharts.options import *

f = open("D:\\pycharm_workspace\\01_PythonBasic-learn\\10_数据可视化\疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()
# 取各省的数据
# 将字符串JSON转换为字典
data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组，并各个省的数据都封装到列表中
data_list = []  # 绘图所需要用的数据列表
for province_data in province_data_list:
    province_name = province_data["name"] + "省"  # 省份名称
    province_confirm = province_data["total"]["confirm"]  # 确诊人数
    data_list.append((province_name, province_confirm))

# 创建地图对象
map = Map()
# 添加数据
map.add("各省份确诊人数", data_list, "china")
# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033"},
        ]
    )
)
# 绘图
map.render("全国疫情地图.html")