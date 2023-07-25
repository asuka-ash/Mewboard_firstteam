import socket
import threading
import time
from env import *
from config import *
from message import send, receive, add_listener

status = {
    "connected": False,
    "retry_connection": True
}

def handle_server(conn, addr):    
    try:
        print(f"[-] {addr} connected.")
        add_listener(conn, addr)
        status["connected"] = False
    except Exception as e:
        print(f"[-] Connection with {addr} closed: {e}")
        status["connected"] = False


def connect(agent):
    while not status["connected"] and status["retry_connection"]:
        try:
            agent.connect(config.addr)
            print(f"[-] Agent is Connected on {HOST}, {PORT}")
            thread = threading.Thread(target=handle_server, args=(agent, config.addr))
            thread.start()
            status["connected"] = True
        except Exception as e:
            print(e)
            print(f"[-] Cannot connect to Server on {HOST}, {PORT}.")
            choice = input("Do you want to run the agent offline? (yes/no): ")
            if choice.lower() == "yes":
                print("[-] Agent running in offline mode.")
                status["retry_connection"] = False
            else:
                time.sleep(2)

def sendMessage(agent, msg):
    if status["connected"]:
        try:
            send(agent, msg)
        except Exception as e:
            print("[-] Cannot send message: ", e)
    else:
        print("[-] Agent is not connected")

def start():
    
    agent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    agent.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connect(agent)
    
    while True:  # Continue asking for messages until a disconnect message is entered
        msg = input('Input Message: ')
        if msg == 'status':
            print(status)
        elif msg == 'connect':
            connect(agent)
        elif msg == DISCONNECT_MSG:  # Check if disconnect message is sent
            for thread in threading.enumerate():
                if thread != threading.current_thread() and not thread.isDaemon():
                    thread.join()  # wait for all non-daemon threads to finish
            break  # exit the loop
        else:
            sendMessage(agent, msg)

    # Make sure to send a disconnect message and close the connection at the end
    sendMessage(agent, DISCONNECT_MSG)
    agent.close()

if __name__ == '__main__':
    print(f"[-] Initializing Agent ...")
    config = Config(HOST, PORT)
    start()
