# 小黎专属python固定模板
# 开发时间：2024/7/6 22:58
# 捕获异常的基本语法:
# 捕获所以异常
try:
    f = open("D:\\pycharm_workspace\\01_PythonBasic-learn\\09_异常、模块、包\\test.txt","r",encoding="UTF-8")
except:
    print("文件不存在 出现异常了 改为w模式")
    f = open("D:\\pycharm_workspace\\01_PythonBasic-learn\\09_异常、模块、包\\test.txt","w",encoding="UTF-8")

# 捕获指定的异常:
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")

# 捕获多个类型的异常:
try:
    # print(name)
    1/0
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未定义或者除以0的异常")

# finally 一定会执行的语句
try:
    f = open("D:\\pycharm_workspace\\01_PythonBasic-learn\\09_异常、模块、包\\test2.txt","r",encoding="UTF-8")
#     捕获全部异常的第二种写法
except Exception as e:
    print("文件不存在 出现异常了 改为w模式")
    f = open("D:\\pycharm_workspace\\01_PythonBasic-learn\\09_异常、模块、包\\test2.txt","w",encoding="UTF-8")
else:
    print("好高兴，无异常")
finally:
    print("一定会执行finally中的语句")
    f.close()
