# 先使用  sudo pip3 install gevent  安装
# 使用gevent中的socket、sleep等不会发生阻塞
import gevent
import time
from gevent import monkey  # 将已经写好的sleep等换成gevent中的

monkey.patch_all()  # 把已经写好的sleep换成gevent中的


def task(*n):
    for i in range(n[0]):
        print(n[1], i)
        # gevent.getcurrent()  # 获取当前执行的gevent对象
        gevent.sleep(1)  # 不会阻塞线程，线程回去执行其他的事情
        # time.sleep(1)


if __name__ == '__main__':
    g = gevent.spawn(task, 5, "a")
    g1 = gevent.spawn(task, 5, "b")
    g.join()
    g1.join()
    # gevent.joinall([
    #     gevent.spawn(task, 5, "a"),
    #     gevent.spawn(task, 5, "b")
    # ])
