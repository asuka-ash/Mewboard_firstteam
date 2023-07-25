import socket
import threading
import os
import hashlib
import time
from env import *
from config import *
from message import *

SERVER_LOGS = 'server_logs'
status = {
    'online': False,
}

# Define a global threading event
stop_threads = threading.Event()

def get_id(input_string):
    # Convert the input string to bytes (required for hashlib)
    input_bytes = input_string.encode('utf-8')

    # Create a SHA-256 hash object and compute the hash value
    sha256_hash = hashlib.sha256(input_bytes)

    # Get the hexadecimal representation of the hash value
    unique_id = sha256_hash.hexdigest()

    return 'agent_'+unique_id

connections = {}  # Dictionary to store connections and their addresses

def handle_client(conn, addr):    
    print(f"[-] {addr} connected.")
    
    _id = get_id(str(addr))

    initializeDirectory(SERVER_LOGS + '/' + _id)
    connections[_id] = {'connection':conn, 'address':str(addr), 'directory': SERVER_LOGS + '/' + _id}

    print(connections)
    add_listener(conn, addr)

    # Check if the stop_threads event is set
    while not stop_threads.is_set():
        # If the stop_threads event is set, break the loop and end the thread
        break

def start(server):
    # Handle New Connections
    server.listen()
    status['online'] = True
    print(f"[-] Listening on {HOST} : {PORT}")
    while status['online'] and not stop_threads.is_set(): # Add the stop_threads check
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
    print(f"[-] Server Status: {status['online']}")
    print(f"[-] Server Stopped Listening")
    server.close()

def sendMessage(_id, message):
    if _id in connections:
        conn = connections[_id]['connection']
        send(conn, message)
    else:
        print(f"[-] Error: ID {_id} is not valid.")

def cleanUp():
    global connections
    status['online'] = False

    # Set the stop_threads event to stop all running threads
    stop_threads.set()

    # Close all connections
    for _id in connections:    
        print("[-] Closing _id")
        conn = connections[_id]['connection']
        try:  # add error handling for sending message and closing connection
            sendMessage(_id, "DISCONNECT_MSG")
            conn.close()
        except Exception as e:
            print(f"[-] Error closing connection {_id}: {e}")
    
    # Clear the connections dictionary
    connections = {}

def initializeDirectory(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def connect():
    if not status['online']:  # only start a new thread if one isn't already running
        try:
            config = Config(HOST, PORT)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(config.addr)
        except:
            pass
        server_thread = threading.Thread(target=start, args=(server,))
        server_thread.start()
        status['online'] = True
    else:
        print("[-] Already Listening")

if __name__ == '__main__':
    
    print(f"[-] Intiailizing Server ...")
    initializeDirectory(SERVER_LOGS)
    connect()
    
    time.sleep(1)

    while True:
        print('------------------------------')
        print('0 - Status')
        print('1 - Available Connections')
        print('2 - Send Message')
        print('3 - Start Listening')
        print('4 - Stop Listening')
        print('------------------------------')

        cmd = input('Enter Command: ')

        if cmd == '0':
            print(status)
        elif cmd == '1':
            print('Available Connections:')
            for _id in connections.keys():
                print(f'- {_id} : {connections[_id]["address"]}')
        elif cmd == '2':
            _id = input('Enter Agent ID: ')
            message = input('Enter Message: ')
            sendMessage(_id, message)
        elif cmd == '3':
            connect()
        elif cmd == '4':
            cleanUp()
