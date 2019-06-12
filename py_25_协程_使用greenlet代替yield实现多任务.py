# 先使用  sudo pip3 install greenlet  安装

from greenlet import greenlet  # 这里要注意
import time


def task_1():
    while True:
        print("--1--")
        t2.switch()
        time.sleep(0.1)


def task_2():
    while True:
        print("--2--")
        t1.switch()
        time.sleep(0.1)


t1 = greenlet(task_1)
t2 = greenlet(task_2)

if __name__ == '__main__':
    t1.switch()
