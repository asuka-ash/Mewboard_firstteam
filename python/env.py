import socket

PORT = 3000
HOST = socket.gethostbyname(socket.gethostname())
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'