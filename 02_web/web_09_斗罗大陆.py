# http://play.ting89.com/down/down.php?url=http://mp3-f.ting89.com:9090/2018/36/斗罗大陆3龙王传说_赞扬/0128.mp3
import threading
import urllib.request
from urllib.parse import quote
import string


def main():
    for i in range(202, 331):
        url = "http://mp3-f.ting89.com:9090/2018/36/斗罗大陆3龙王传说_赞扬/0%d.mp3" % i
        url = quote(url, safe=string.printable)
        threading.Thread(target=download, args=(url,)).start()


def download(url):
    file_name = url[-8:]
    print(file_name)
    result = urllib.request.urlopen(url)
    content = result.read()

    result = content.replace(b"www.yousheng8.comTPE1", str.encode("0" + str(file_name[:-4])))

    with open(file_name, "bw") as file:
        file.write(result)
    print("finish -> %s" % file_name)


def change_name():
    for i in range(204, 210):
        with open("/Users/liboxin/Movies/a/0%d.mp3" % i, "wb+") as b:
            content = b.read()
            result = content.replace(b"TPE1", str.encode(""))
            b.seek(0)
            b.write(result)
            b.close()


if __name__ == '__main__':
    main()
    # change_name()
