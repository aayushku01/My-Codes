import socket
from time import ctime

host = 'localhost'
port = 12345
bufsiz = 1024
addr = (host,port)

if __name__ == '__main__':
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(addr)
	server_socket.listen(5)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:
	print('Server waitting for connection...')
	client_sock, addr1 = server_socket.accept()
	print('client connected from:{0}'.format(addr))
	
	while True:
		data = client_sock.recv(bufsiz)
		if not data or data.decode('utf-8') == 'END':
			break
		print('Received from client : {0}'.format(data.decode('utf-8')))
		print('Sending the server time to client:{0}'.format(ctime()))
		try:
			client_sock.send(bytes(ctime(), 'utf-8'))
		except KeyboardInterrupt:
			print('exited By User')
	client_sock.close()
server_socl.close()
