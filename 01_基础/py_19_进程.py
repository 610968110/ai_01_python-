import multiprocessing
import time


def song(name):
    time.sleep(1)
    print("%s在唱歌" % name)


def dance():
    time.sleep(1)
    print("小明在跳舞")


def main():
    multiprocessing.Process(target=song, args=("大明",)).start()
    multiprocessing.Process(target=dance).start()

    queue = multiprocessing.Queue(2)
    queue.put(1)
    queue.put(2)
    print(queue.full())
    task = queue.get()  # 取出第一个,没有回阻塞
    # task2=queue.get_nowait()  # 没有不阻塞，直接抛异常
    print(task)
    # 这里阻塞了
    queue.put(3)
    # print(queue.qsize())


if __name__ == '__main__':
    main()
