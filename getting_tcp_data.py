import socket

host = input('enter target host:')
port = input('enter target port:')

bufs = 4096

addr = (host,int(port))

if __name__ == '__main__':
	client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_sock.connect(addr)

	while True:
		data = 'GET/ HTTp/1.0\r\n\r\n'
		if not data:
			break
		client_sock.send(data.encode('utf-8'))
		data = client_sock.recv(bufs)
		if not data:
			break
		print(data.decode('utf-8'))

	client_sock.close()
