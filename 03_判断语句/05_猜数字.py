# 小黎专属python固定模板
# 开发时间：2024/6/26 17:01
import random
# 产生一个1-10之间的随机数字
num = random.randint(1,10)
# print(num)

guess_num = int(input("输入您猜测的数:"))
if guess_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num > num:
        print("猜大了")
    else:
        print("猜小了")
    guess_num = int(input("再猜一次吧:"))
    if guess_num == num:
        print("恭喜，第二次猜中了")
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")
        guess_num = int(input("再猜一次吧:"))
        if guess_num == num:
            print("恭喜，第三次猜中了")
        else:
            print("很遗憾，三次你都没猜中")