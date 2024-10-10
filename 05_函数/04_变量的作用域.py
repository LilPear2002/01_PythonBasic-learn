# 小黎专属python固定模板
# 开发时间：2024/7/3 15:26

num = 100

def testA():
    num = 300
    print(f"testA:{num}")


def testB():
    global num #定义为全局变量
    num = 200
    print(f"testB:{num}")


testA()
print(num)
testB()
print(num)

