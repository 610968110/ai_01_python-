import socket

# server = socket.socket(socket.SOL_SOCKET, socket.SO_REUSEADDR)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 1)
server.bind(("", 8888))
server.listen(128)
server.accept()
