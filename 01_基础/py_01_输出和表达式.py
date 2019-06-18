#! /Users/liboxin/PycharmProjects/untitled/venv3/bin/python3
"""
先用 which python3 查看python3的安装路径，然后用#!设置在第一行，就可以直接在命令行运行，不需要在python3的便以其中运行
命令行输入：
/Users/liboxin/PycharmProjects/untitled/py_01_输出和表达式.py
直接运行
"""
import random

i = 10
s = "啊"
print("啊" + str(i))

# 格式化输出
print("%d -> %d" % (1, 2))

# 位数  输出000001
print("我的学号是 ： %06d" % 1)

# 保存两位小数
print("价钱是 ： %.2f" % 1.123456)

# 检查类型
print("1的类型是：%s" % type(1))

# -------------------------- if条件语句 --------------------------
print("-" * 25, "if条件语句", "-" * 25)

# if判断语句  and or not
# age = int(input("请输入年龄:"))
age = random.randint(0, 120)  # 随机数
print("您的年龄是：%d" % age)
if age < 18:
    print("小孩")
    print("不能进网吧")
elif age <= 30:
    print("中年")
else:
    print("老年")

# if 0 不成立
# if 1  成立
# if 2  成立  只要不是0就成立
# if (11, 22)  成立  只要不是空的就成立
# if [1, 2]  成立  只要不是空的就成立
# if {1: 1, 2: 2}  成立  只要不是空的就成立
# if NONE  不成立

# -------------------------- for循环 --------------------------
print("-" * 25, "for循环", "-" * 25)

for i in range(5):  # 循环5次,0-4
    print(i)

list_name = ["a", "b"]
for name in list_name:
    print(name)

for name in list_name:
    print(name)
    # break
else:
    print("for循环没有经过break，全部执行完，则打印")
