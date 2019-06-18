from collections import Iterable
import time


# -------------------------- 判断是否是迭代器 --------------------------


def main():
    print("-" * 25, "判断是否是迭代器", "-" * 25)
    print(isinstance(1, Iterable))
    print(isinstance((1, 2), Iterable))


# -------------------------- 自定义迭代器 --------------------------
# class Person(object):
#
#     def __init__(self) -> None:
#         super().__init__()
#         self.names = list()
#
#     def __iter__(self):
#         """
#         写方法后即成为了迭代器
#         :return:
#         """
#         return MyIterator(self)
#
#     def add(self, name):
#         self.names.append(name)


# class MyIterator(object):
#
#     def __init__(self, obj) -> None:
#         super().__init__()
#         self.obj = obj
#         self.pos = 0
#
#     def __next__(self):
#         if self.pos < len(self.obj.names):
#             self.pos += 1
#             return self.obj.names[self.pos - 1]
#         else:
#             raise StopIteration  # 抛出这个异常，for循环就停止了


class Person(object):

    def __init__(self):
        self.names = list()
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos < len(self.names):
            name = self.names[self.pos]
            self.pos += 1
            return name
        else:
            raise StopIteration

    def add(self, name):
        self.names.append(name)


def main1():
    clazz = Person()
    print(isinstance(clazz, Iterable))
    clazz.add("张三")
    clazz.add("张四")
    clazz.add("张五")
    for name in clazz:
        print(name)
        time.sleep(1)
    else:
        print("我是正常结束的哦")


if __name__ == '__main__':
    # main()
    print("-" * 25, "自定义迭代器", "-" * 25)
    main1()

