import socket


def main():
    """
    客户端
    :return: ...
    """
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect(("192.168.1.1", 8080))
    tcp.send(b"hello")
    tcp.close()


def main1():
    """
    服务端
    :return: ...
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", 7788))  # 易错点，这里是元祖，需要加个括号
    server.listen(128)  # 最大连接客户端数
    # 等待连接,返回一个元祖,该函数仅仅获取客户端返回值，不写该函数客户端也可以连接上
    client_socket, client_addr = server.accept()

    client_msg = server.recv(1024)  # 接收消息
    print(client_msg)
    client_socket.send(b"hello too  - -!!!")
    server.close()


# if not client_msg:  如果收到的消息为NONE，则客户端断开连接

if __name__ == '__main__':
    main()
    # main1()
