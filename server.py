import socket 
import pickle
from threading import _start_new_thread
import time 

HEADERSIZE = 10
HOST = socket.gethostname()
PORT = 1420

def new_socket(connection, address):
    while True:
        time.sleep(0.5)
        full_msg = b''
        new_msg = True
        while True:
            msg = connection.recv(16)
            if new_msg:
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            full_msg += msg
            if len(full_msg)-HEADERSIZE == msglen:
                print(pickle.loads(full_msg[HEADERSIZE:]))
                new_msg = True
                full_msg = b""


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(0.9)
print(f'binding the port, {PORT}')
server_socket.bind((HOST, PORT))
time.sleep(0.7)
print('Server is now listening!')
server_socket.listen(10)

while True:
    connection, address = server_socket.accept()
    time.sleep(0.3)
    print(f'connected with {address}')
    _start_new_thread(new_socket, (connection, address))

