# 小黎专属python固定模板
# 开发时间：2024/7/6 22:47

# 文件不存在时会创建新文件并写入内容 若文件存在则清空原有的内容并写入新内容 若要追加 则调整为a模式
f1 = open("D:/pycharm_workspace/01_PythonBasic-learn/08_文件操作/test2.txt", "w", encoding="UTF-8")
f2 = open("D:/pycharm_workspace/01_PythonBasic-learn/08_文件操作/test.txt", "a", encoding="UTF-8")
f1.write("你知道的，Lil Pear会走起来的")  # 内容写入到内存中
f2.write("\n你知道的，Lil Pear会走起来的")  # 内容写入到内存中
f1.flush()  # 将内存中的内容写入到文件中
f2.flush()  # 将内存中的内容写入到文件中
f1.close()
f2.close()