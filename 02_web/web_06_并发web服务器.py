import socket
import gevent


def used_client(client):
    msg = client.recv(1024)
    print(msg)
    client.send(b"Http/1.1 200 OK\r\n")
    client.send(b"\r\n")
    client.send(b"<h1>hahaha</h1>")
    client.close()


def main():
    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    service.bind(("", 8899))
    service.listen(128)
    while 1:
        client, addr = service.accept()
        gevent.spawn(used_client, client)
        used_client(client)


if __name__ == "__main__":
    main()
