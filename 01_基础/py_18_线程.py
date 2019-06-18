import time
import threading


def song(name):
    for i in range(5):
        print("%s正在唱歌 %d" % (name, i))
        time.sleep(1)


def dance():
    for i in range(5):
        print("小明正在跳舞 %d" % i)
        time.sleep(1)


def main():
    threading_enumerate = threading.enumerate()  # 线程信息
    print(len(threading_enumerate))  # 当前运行线程数量,只有一个主线程
    threading.Thread(target=song, args=("大明",)).start()
    threading.Thread(target=dance).start()
    print("\n", len(threading.enumerate()))  # 当前运行线程数量，3个线程
    # song()
    # dance()


# -------------------------- 继承线程 --------------------------
print("-" * 25, "继承线程", "-" * 25)


class MyThread(threading.Thread):

    def run(self) -> None:
        super().run()
        print("继承线程")


def main1():
    MyThread().start()


# -------------------------- lock --------------------------
print("-" * 25, "lock", "-" * 25)

lock = threading.Lock()


def sleep():
    lock.acquire()  # 互斥锁
    print("我在睡觉")
    time.sleep(3)
    lock.release()  # 释放锁


def lockTest():
    threading.Thread(target=sleep).start()
    threading.Thread(target=sleep).start()


if __name__ == '__main__':
    main()
    main1()
    lockTest()
