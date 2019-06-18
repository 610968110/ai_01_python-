def main(lens):
    index = 0
    a, b = 0, 1
    while index < lens:
        ret = yield a  # 只要有yield，就不是函数，而是一个生成器模板，本质是类
        # print(ret)
        a, b = b, a + b
        index += 1
        if ret is not None:
            break


if __name__ == '__main__':
    p = main(10)
    # print(next(p))
    # result = p.send("~")  # send得值是yield的返回值，所以不能在第一次调用，至少要执行一次next后才可以
    # print(result)
    i = 0
    while True:
        r = next(p)
        if i >= 5:
            r = p.send("a")
        print(r)
        i += 1
