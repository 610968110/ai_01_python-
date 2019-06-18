import urllib.request


def main():
    req = urllib.request.urlopen("http://www.baidu.com")
    print(req.read())  # 网页的源代码


if __name__ == '__main__':
    main()
