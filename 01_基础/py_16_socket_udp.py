import socket


def main():
    # AF_INET是固定的代表ipv_4;SOCK_STREAM代表tcp,SOCK_DGRAM代表udp
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udp.sendto(b"hello", ("192.168.0.1", 8080))
    udp.sendto("hello".encode("utf-8 "), ("192.168.0.1", 8080))  # 如果之前没有绑定端口，则随机一个端口

    # 接收相关
    local_addr = ("", 8080)  # 绑定ip和端口，""空的表示现在的ip
    udp.bind(local_addr)
    while True:
        result = udp.recvfrom(1024)  # 1024代表接收的最大字节,format: (b"msg", (ip, port))
        print(result[0].decode("utf-8"))  # 这里注意，例如win发送的是gbk编码，这时会解析失败

    # udp.close()


if __name__ == '__main__':
    main()
