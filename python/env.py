import socket

PORT = 5009
HOST = socket.gethostbyname(socket.gethostname())
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'