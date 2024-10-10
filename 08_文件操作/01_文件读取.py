# 小黎专属python固定模板
# 开发时间：2024/7/6 22:09

# 打开文件
f = open("D:/pycharm_workspace/01_PythonBasic-learn/08_文件操作/test.txt", "r", encoding="UTF-8")
print(type(f))
# 读取文件
# print(f.read(9))  # 读取9个字节的内容
# print(f.read())
# io_list = f.readlines()  # 读取文件的全部行并存到列表中
# print(io_list)

# 读取每行数据
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1)
# print(line2)
# print(line3)

# for循环读取文件行
for line in f:
    print(line)
# 文件的关闭
f.close()
