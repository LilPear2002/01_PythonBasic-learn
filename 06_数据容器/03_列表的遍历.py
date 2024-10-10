# 小黎专属python固定模板
# 开发时间：2024/7/5 20:17

# 使用while循环遍历
def list_while_func():
    mylist = ["xiaoli", 666, "最帅", True]
    index = 0
    while index < len(mylist):
        print(mylist[index])
        index += 1

# 使用for循环遍历
def list_for_func():
    mylist = ["xiaoli", 666, "最帅", True]
    for element in mylist:
        print(element)

list_while_func()
list_for_func()
