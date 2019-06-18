import multiprocessing
import time


def song(name):
    time.sleep(1)
    print("%s在唱歌" % name)


def main():
    pool = multiprocessing.Pool(processes=3 )
    for i in range(10):
        pool.apply_async(func=song, args=("大明",))

    pool.close()
    # 这里要阻塞一下，如果不等待pool执行完，就和主进程一起挂掉了
    pool.join()  # 必须在close之后


if __name__ == '__main__':
    main()
