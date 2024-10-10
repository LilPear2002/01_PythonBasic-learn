# 小黎专属python固定模板
# 开发时间：2024/7/5 22:02
"""
序列是指：内容连续、有序，可使用下标索引的一类数据容器
列表、元组、字符串，均可以视为序列
切片就是从一个序列中取出一个子序列
"""
mylist = [0,1,2,3,4,5,6]
mytuple = (0,1,2,3,4,5,6)
mystr = "0123456"
# 对列表进行切片，从1开始，4结束(不含索引4对应的元素)，步长为1(默认为1可不写)
mylist2 = mylist[1:4]
print(mylist2)
# 对元组进行切片，从头开始到尾结束，步长为1
mytuple2 = mytuple[:]
print(mytuple2)
# 对字符串进行切片，从头开始到尾结束，步长为2
mystr2 = mystr[0:len(mystr):2]
print(mystr2)

# 也可以反向取
# 对列表进行切片，从头开始到尾结束，步长为-1
mylist3 = mylist[::-1]
print(mylist3)
# 对元组进行切片，从3开始到1结束，步长为-1
mytuple3 = mytuple[3:1:-1]
print(mytuple3)
# 对字符串进行切片 从头开始到尾结束步长为-2
mystr3 = mystr[::-2]
print(mystr3)

