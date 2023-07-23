import socket
import threading
from env import *
from config import *
from message import *

connections = {}  # Dictionary to store connections and their addresses

def handle_client(conn, addr):    
    print(f"[-] {addr} connected.")
    connections[str(addr)] = conn
    print(connections)
    add_listener(conn, addr)
    
    
def start(server):
    # Handle New Connections
    server.listen()
    print(f"[-] Listening on {HOST} : {PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

def sendMessage(addr, message):
    if addr in connections:
        conn = connections[addr]
        send(conn, message)
    else:
        print(f"[-] Error: Address {addr} is not connected.")


if __name__ == '__main__':
    
    print(f"[-] Intiailizing Server ...")
    config = Config(HOST, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(config.addr)
    server_thread = threading.Thread(target=start, args=(server,))
    server_thread.start()

    print('1 - Available Connections')
    print('2 - Send Message')

    while True:
        cmd = input('Enter Command: ')

        if cmd == '1':
            print('Available Connections:')
            for addr in connections.keys():
                print(f'- {addr}')
        elif cmd == '2':
            addr = input('Enter Address (IP:PORT): ')
            message = input('Enter Message: ')
            sendMessage(addr, message)
        else:
            print('[-] Invalid Command. Please try again.')







    