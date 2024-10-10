# 小黎专属python固定模板
# 开发时间：2024/6/24 15:09
name = "小黎"
age = 22
# 方式一
# %s 即将内容转换为字符串放入占位位置
message1 = "我的名字是%s" %name
message2 = "我的名字是%s,年龄是%d" %(name,age)
print(message1)
print(message2)

# 数字精度控制 (会做四舍五入)
message3 = "我的名字是%s,年龄是%.2f" %(name,age)
print(message3)

# 方式二 比较快捷 不关心精度控制
print(f"我的名字是{name},年龄是{age}")

print("我的名字是",name,"年龄是",age)

age = 22.0
print("我的年龄是{:.2f}".format(age))