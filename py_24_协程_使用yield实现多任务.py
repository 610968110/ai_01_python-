import time


def tesk_1():
    while True:
        print("--1--")
        time.sleep(0.1)
        yield


def tesk_2():
    while True:
        print("--2--")
        time.sleep(0.1)
        yield


if __name__ == '__main__':
    t1 = tesk_1()
    t2 = tesk_2()
    while True:
        next(t1)
        next(t2)
