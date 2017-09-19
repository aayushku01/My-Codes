from socket import *

s = socket(AF_INET,SOCK_STREAM)
server = input('Server u want to Connect :-')

def pscan(port):
	try:
		s.connect((server,port))
		return True
	except:
		return False

for x in range(1,25):
	if pscan(x):
		print('Port {0} is open!!!!!!!!!!!!!!!'.format(x))
	else:
		print('Port {0} is closed'.format(x))
