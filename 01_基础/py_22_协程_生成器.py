def main(lens):
    """
    生成一个斐波那契数列
    :param lens:  长度
    :return:
    """
    index = 0
    a, b = 0, 1
    while index < lens:
        yield a  # 只要有yield，就不是函数，而是一个生成器模板，本质是类
        print("~~~~~")  # yield执行完，先不走这里，先走for循环的流程，然后再回到这里
        a, b = b, a + b
        index += 1


if __name__ == '__main__':
    #  生成器是一种特殊的迭代器,打印的都是yield后的值
    p = main(2)
    print(next(p))
    print(next(p))
    # -------------------------- 可以循环打印 --------------------------
    print("-" * 25, "可以循环打印", "-" * 25)
    for i in main(10):
        print(i)
    # -------------------------- while循环打印 --------------------------
    print("-" * 25, "while循环打印", "-" * 25)
    p = main(2)
    while True:
        try:
            # 用try代码块结束while循环
            print(next(p))
        except Exception as e:
            print("我正常结束了:", e.value)
            break
