# 小黎专属python固定模板
# 开发时间：2024/7/5 22:59
# 集合中的元素不重复且内容无序 不支持按照索引访问元素

# 集合的定义
my_set = {"xiaoli", "learn", "python"}
my_set_empty = set()
print(f"my_set内容是{my_set},类型是{type(my_set)}")
print(f"my_set内容是{my_set_empty},类型是{type(my_set_empty)}")
# 添加新元素
my_set.add("人生苦短")
print(my_set)
# 移除元素
my_set.remove("learn")
print(my_set)
# 随机取出一个元素
element = my_set.pop()
print(element)
print(my_set)
# 统计集合中元素的数量
print(len(my_set))
# 遍历 由于不支持索引查找元素 所以不支持while循环遍历
for element in my_set:
    print(element)
# 清空集合
my_set.clear()
print(my_set)

# 取两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
print(set1.difference(set2))  # set1有而set2没有的
# 消除2个集合的差集
set1.difference_update(set2)  # 消除set1中包含set2里的元素
print(set1)
# 合并两个集合
print(set1.union(set2))
