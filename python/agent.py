import socket
from env import *
from config import *
from message import *
import threading

def handle_server(conn, addr):    
    print(f"[-] {addr} connected.")
    add_listener(conn, addr)

def start(agent):
    # Handle New Connections
    agent.connect(config.addr)
    print(f"[-] Agent is Connected on {HOST}, {PORT}")
    thread = threading.Thread(target=handle_server, args=(agent, config.addr))
    thread.start()

    i = 5
    while i:
        i -= 1
        msg = input('Input Message: ')
        send(agent, msg)

    send(agent, DISCONNECT_MSG)
    agent.close()
        
if __name__ == '__main__':
    print(f"[-] Intiailizing Agent ...")
    config = Config(HOST, PORT)
    agent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start(agent)







    