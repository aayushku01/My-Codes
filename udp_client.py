from socket import socket, AF_INET, SOCK_DGRAM

max_size = 4096
port = 12345

if __name__ == '__main__':
	sock = socket(AF_INET,SOCK_DGRAM)
	msg =  'Hello UDP'
	sock.sendto(msg.encode('utf-8'),('',port))
	data, addr = sock.recvfrom(max_size)
	print('Server Says:')
	print(repr(data))

