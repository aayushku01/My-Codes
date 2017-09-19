import socket
from  _thread import *

host = ''
port = 55555

global s
global addr
global a

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((host,port))
except socket.error as e:
	print(str(e))

s.listen(5)

print('Waiting...')

def threaded_client(conn):
	conn.send(str.encode('Welcome, type your info\n'))
	
	while True:
		conn.send(str.encode('>'))
		data = conn.recv(2048)
		reply = 'Server output: '+ data.decode('utf-8').upper()
		print('Sent to client('+addr[0]+'):- '+data.decode('utf-8').upper())
		if not data:
			break
		conn.sendall(str.encode(reply))
	conn.close()

a = []

while True:

	conn, addr = s.accept()
	a.append(addr[0])
	print('connected to: '+addr[0]+':'+str(addr[1]))
	start_new_thread(threaded_client,(conn,))
	print(set(a))
s.close()
