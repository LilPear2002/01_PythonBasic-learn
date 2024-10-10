# 小黎专属python固定模板
# 开发时间：2024/7/3 14:30

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度为{count}")

my_len("xiaolizuishuai")
my_len("xiaoli")

print(f"字符串xioali的长度为{len('xiaoli')}")