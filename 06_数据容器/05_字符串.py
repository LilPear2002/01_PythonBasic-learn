# 小黎专属python固定模板
# 开发时间：2024/7/5 21:42
# 字符串不可修改，支持重复元素且有序
my_str = "xiaoli is the best one"
print(my_str)
# 通过索引取值
print(my_str[2])
# index方法
print(my_str.index("is"))
# replace 替换
my_str2 = my_str.replace("xiaoli", "Lil Pear")
print(my_str2)
print(my_str) #不变
# split 字符串分割
mylist = my_str.split(" ")
print(mylist)
# 字符串规整
my_str3 = "  xiaoli  "
my_str4 = "12xiaoli212"
print(my_str3.strip())
print(my_str4.strip("12"))
# count
print(my_str.count("i"))
# len
print(len(my_str))
