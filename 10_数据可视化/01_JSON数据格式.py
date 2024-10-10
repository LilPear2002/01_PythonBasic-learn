# 小黎专属python固定模板
# 开发时间：2024/7/8 21:44

import json

data = [{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]
# 将列表转换为JSON格式
json_str = json.dumps(data, ensure_ascii=False)
print(f"此JSON格式数据的内容是{json_str},类型是{type(json_str)}")
# 将字典转换为JSON格式
d = {"name": "周杰伦", "addr": "台北"}
json_str = json.dumps(d, ensure_ascii=False)
print(f"此JSON格式数据的内容是{json_str},类型是{type(json_str)}")

# 将JSON转换为python数据类型
l = json.loads(json_str)
print(l)