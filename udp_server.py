from socket import socket,AF_INET,SOCK_DGRAM
max_size = 4096

sock = socket(AF_INET,SOCK_DGRAM)
sock.bind(('',12345))
while True:
	data , addr = sock.recvfrom(max_size)
	resp = 'UDP server Sending data'
	print('Sending Data')
	sock.sendto(str.encode(resp),addr)
