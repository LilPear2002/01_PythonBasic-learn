# 小黎专属python固定模板
# 开发时间：2024/7/5 23:22
# 字典存储的元素是键值对 key不允许重复
my_dict = {"黎鸿翔": 99, "xiaoli": 98, "Lil Pear": 97}
my_dict_empty = {}  # 空字典
my_dict_empty2 = dict()
print(f"my_dict的内容是{my_dict},类型是{type(my_dict)}")
print(f"my_dict_empty的内容是{my_dict_empty},类型是{type(my_dict_empty)}")
print(f"my_dict_empty2的内容是{my_dict_empty2},类型是{type(my_dict_empty2)}")
# 通过key获取value
score = my_dict["xiaoli"]
print(score)
# 修改或新增
my_dict["黎鸿翔"] = 99.5  # key存在则修改value
my_dict["孙悟空"] = 99.9  # 若key不存在则为新增
print(my_dict)
# 删除
value = my_dict.pop("孙悟空")
print(value)
print(my_dict)
# 获取全部的key
keys = my_dict.keys()
print(keys)
# 遍历字典
# 方式一
for key in keys:
    print(f"字典的key是{key},value是{my_dict[key]}")

print('-------------------')
#     方式二:
for key in my_dict:
    print(f"字典的key是{key},value是{my_dict[key]}")
#     长度
print(len(my_dict))
# 清空
my_dict.clear()
print(my_dict)
# 定义嵌套字典
stu_score_dict = {
    "黎鸿翔": {
        "语文": 97,
        "数学": 110,
        "英语": 107
    },
    "xiaoli": {
        "语文": 92,
        "数学": 140,
        "英语": 137
    },
    "Lil Pear": {
        "语文": 90,
        "数学": 120,
        "英语": 100
    }
}
print(stu_score_dict)
# 取value
print(stu_score_dict["黎鸿翔"]["数学"])
