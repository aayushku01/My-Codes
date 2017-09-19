import socket
import sys

if __name__ == '__main__':

	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	except socket.error as err:
		print('Got Fucked Up !')
		print('Reason: {0}'.format(str(err) ))
		sys.exit();
	print('Socket Created ! :)')
	
	tar_host = input('ENTER TARGET HOST TO CONNECT: ')
	tar_port = input('ENTER TARGET PORT TO CONNECT: ')

	try:
		sock.connect((tar_host, int(tar_port)))
		print("CONNECTED TO {1} ON PORT {0} YEAH ! ".format(tar_port,tar_host))
		sock.shutdown(2)	
	
	except socket.error as err:
		print('YOU WROTE A FUCKING WRONG ADDRESS !')
		print('REASON = {0}'.format(err))
		sys.exit();
