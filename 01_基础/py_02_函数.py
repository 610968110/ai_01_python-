def test(string="李四"):  # 缺省参数，这里默认赋值了李四，缺省参数必须在末尾
    """
    这里是文档注释
    :param string:  字符串
    :return:  null
    """
    print(string)


test("张三")

# -------------------------- 全局变量的操作 --------------------------
print("-" * 25, "全局变量的操作", "-" * 25)

num = 1


def test1():
    global num  # 告诉后面num均为全局变量
    print("num -> %d" % num)


test1()
# -------------------------- 返回多个值 --------------------------
print("-" * 25, "返回多个值", "-" * 25)


def test2():
    return 1, 2, "3"  # 返回的是元祖，()省略了


# test2_ = test2()
(one, two, three) = test2()
print(one, two, three)
# -------------------------- 多值参数 --------------------------
print("-" * 25, "多值参数", "-" * 25)


def t(*args, **args_map):  # *列表  **字典
    print(args)
    print(args_map)


list_ = [1, 2, 3]
map_ = {"a": 1, "b": 2, "c": 3}
t(list_, map_)  # 错误，全赋值到列表里了
print("~~~~~~~~~~~~~")
t(_list=list_, _map=map_)  # 错误，全赋值到字典里了
print("~~~~~~~~~~~~~")
t(*list_, **map_)  # 正确  不知道为什么字典的key必须是string才行
