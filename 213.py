import socket
import os
from threading import Thread
import _thread

def listener(client, address):
    print("Accepted connection from: ", address)

    while True:
        data = client.recv(1024)
        if not data:
            break
        else:
            print(repr(data))
            client.send(data)

    client.close()

host = socket.gethostname()
port = 10016

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(3)
th = []

while True:
    print("Server is listening for connections...")
    client, address = s.accept()
    th.append(Thread(target=listener, args = (client,address)).start())

s.close()

