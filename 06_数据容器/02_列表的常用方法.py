# 小黎专属python固定模板
# 开发时间：2024/7/5 19:46

mylist = ["xiaoli",666,"python"]
# 查找某元素的下标索引 若不存在会报错
print(mylist.index("python"))
# 修改目标索引对应元素的值
mylist[2] = "小黎"
print(mylist)
# 在目标索引处插入元素
mylist.insert(1,"python")
print(mylist)
# 在尾部追加一个元素
mylist.append("人生苦短")
print(mylist)
# 在尾部追加一个数据容器中的元素
mylist2 = [1,2,3]
mylist.extend(mylist2)
print(mylist)
# 删除目标索引处的元素 两种方法 第一种方法可以得到返回值
element = mylist.pop(2)
print(element)
print(mylist)
del mylist[6]
print(mylist)
# 删除某元素在列表中的第一个匹配项
mylist.remove("人生苦短")
print(mylist)
# 统计某元素的个数
print(mylist.count("xiaoli"))
# 统计所有元素的个数
print(len(mylist))
# 清空列表
mylist.clear()
print(mylist)

