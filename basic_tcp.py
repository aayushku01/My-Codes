import socket

#create a TCP socket (SOC_STREAM)

s = socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0)
print('SOCKET CREATED ! :)')
