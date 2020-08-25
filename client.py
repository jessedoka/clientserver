import socket
import pickle
import time 

HEADERSIZE = 10
USERNAME = input("what is your name! \n")
HOST = socket.gethostname()
PORT = 1420

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        while True:
            msg = input()
            if len(msg) > 0:
                msg = f"{USERNAME}: " + msg
                msg = pickle.dumps(msg)
                msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
                client_socket.send(msg)
                print(f'message has been sent succesfully')
                
except BrokenPipeError as e: 
    time.sleep(0.5)
    print('Server has Closed!')
    client_socket.close()
