# 小黎专属python固定模板
# 开发时间：2024/7/5 20:25
# 元组不可修改，支持重复元素且有序
# 定义元组
t1 = (2,"Hello",True)
# 定义空元祖
t2 = ()
t3 = tuple()
print(f"t1的类型是{type(t1)},内容是{t1}")
print(f"t2的类型是{type(t2)},内容是{t2}")
print(f"t3的类型是{type(t3)},内容是{t3}")
# 定义单个元素的元组
t4 = ("hello")
t5 = ("hello",)
print(f"t4的类型是{type(t4)},内容是{t4}")
print(f"t5的类型是{type(t5)},内容是{t5}")
# 元组的嵌套
t6 = ((1,2,3),(4,5,6))
print(f"t6的类型是{type(t6)},内容是{t6}")
# 取目标索引的值
print(t6[1][2])
# index
print(t1.index("Hello"))
# count
print(t1.count(True))
# len
print(len(t1))
# while遍历
index = 0
while index < len(t1):
    print(t1[index])
    index += 1

# for遍历
for element in t1:
    print(element)

# 不可以直接修改元组中的元素 否则会报错
# 但是若元组中包含列表 则可以修改该列表中的元素
