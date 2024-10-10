# 小黎专属python固定模板
# 开发时间：2024/7/6 21:31

def test_func(compute):
    result = compute(1, 2)
    print(f"结果是:{result}")


# 将匿名函数作为参数传入
test_func(lambda x, y: x + y)
