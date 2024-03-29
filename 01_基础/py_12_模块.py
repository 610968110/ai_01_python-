# -------------------------- 导入文件中任何没有锁进的代码，都会执行一遍 --------------------------
print("-" * 25, "导入文件中任何没有锁进的代码，都会执行一遍", "-" * 25)
# import py_02_函数
# import py_02_函 数 as two
# __import__("py_02_函数")  # 完全一样
#
# py_02_函数.test("啊")
# two.test("嘤嘤嘤")

# __file__查看模块完整路径
# -------------------------- 导入模块部分内容 --------------------------
print("-" * 25, "导入模块部分内容", "-" * 25)
# from py_09_类 import Dog
#
#
# class BlackDog(Dog):
#     def __init__(self):
#         super(BlackDog, self).__init__("黑泥鳅")
#
#
# dog = BlackDog()
# dog.eat()

# -------------------------- 一般这么测试 --------------------------
print("-" * 25, "一般这么测试", "-" * 25)
print("__name__ = %s" % __name__)


def test():
    print("测试")


def main():
    test()


# 如果是被其他模块引入 则判断失败,__name__为当前模块名(py_12_...)
if __name__ == '__main__':
    main()
