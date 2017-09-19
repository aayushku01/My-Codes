import sshtunnel
from getpass import getpass

host = 'localhost'
port = 2222
user = 'aayush'

client = '192.168.126.216' #remote ip
cport = 2221 #remote port

from sshtunnel import SSHTunnelForwarder
sshpass = getpass('Enter Your password:')

server = SSHTunnelForwarder(ssh_address = (host,port),ssh_username=user,ssh_password=sshpass,remote_bind_address=(client,cport))

server.start()
print('connect the remote service vai : {0}'.format(server.local_bind_port))
try:
	while True:
		pass
except KeyboardInterrupt:
	print('Exiting')
	server.stop()

