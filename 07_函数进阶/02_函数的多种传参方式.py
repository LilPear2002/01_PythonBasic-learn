# 小黎专属python固定模板
# 开发时间：2024/7/6 20:53

# 展示多种传参的形式
def user_info(name, age, gender):
    print(f"姓名是{name},年龄是{age},性别是{gender}")


# 位置传参
user_info('小明', 20, '男')

# 关键字传参
user_info(name='小王', age=19, gender='女')
user_info(age=19, gender='男', name='小黎')  # 位置可随意


# 缺省参数(默认参数必须写在最后面)
def user_info(name, age, gender='男'):
    print(f"姓名是{name},年龄是{age},性别是{gender}")


user_info('小明', 13)
user_info('小明', 13, gender='女')


# 位置不定长 不定长定义的形式参数会作为元组存在，接受不定长数量的参数传入
def user_info(*args):
    print(f"args的内容是{args}，类型是{type(args)}")


user_info(1, 2, 3, '小黎', '男孩')


# 关键字不定长 不定长定义的形式参数会作为字典存在，接受不定长数量的参数传入
def user_info(**kwargs):
    print(f"args的内容是{kwargs}，类型是{type(kwargs)}")


user_info(name="小黎", age=22, gender='男')
