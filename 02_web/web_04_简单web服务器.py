import socket


def main():
    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    service.bind(("", 8899))
    service.listen(128)
    # service.setblocking(False) # 设置为不阻塞，直接抛异常
    while 1:
        client, addr = service.accept()
        # client.setblocking(False) # 客户端设置为不阻塞，直接抛异常
        msg = client.recv(1024)
        print(msg)
        client.send(b"Http/1.1 200 OK\r\n")
        client.send(b"\r\n")
        client.send(b"<h1>hahaha</h1>")
        client.close()


if __name__ == "__main__":
    main()
