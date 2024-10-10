# 小黎专属python固定模板
# 开发时间：2024/6/30 15:26
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t", end='')  # 不换行且对齐
        j += 1
    i += 1
    print()  # 换行
