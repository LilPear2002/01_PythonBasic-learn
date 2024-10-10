# 小黎专属python固定模板
# 开发时间：2024/7/6 21:25

def test_func(compute):
    result = compute(1, 2)
    print(f"计算结果是{result},参数类型是{type(compute)}")


def compute(x,y):
    return x + y


test_func(compute)

