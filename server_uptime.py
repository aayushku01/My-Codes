import time, os, schedule, smtplib,getpass
from email.mime.text import MIMEText

username = input('Enter Your Gmail Username (For Sending Mail) :- ')
password = getpass.getpass('Enter Your Gmail Password :- ')
a,b,c,d,e,f,time_off = 0,0,0,0,0,0,0
contents = ''
msg_list = []
msg = MIMEText(contents)
msg['From'] = username
s = smtplib.SMTP_SSL('smtp.gmail.com:465')

def login():
	global password,s
	s = smtplib.SMTP_SSL('smtp.gmail.com:465')
	try:
		global msg,username
		s.ehlo()
		s.login(username, password)
	except Exception:
		print('Authentication Error')
		username = input('Enter Your Username :- ')
		password = getpass.getpass('Enter Your Gmail Password :- ')
		login()


def mail_send():
	login()
	global s
	try:
		s.send_message(msg)
	finally:
		s.quit()
	
def server_down_mail():
	global msg,contents,msg_list,to,username
	contents = "Server Is Down"
	msg = MIMEText(contents)
	msg['Subject'] = 'Your Sever Is Down :( '
	msg['From'] = username
	msg['To'] = to  #Receiver's Mail Address
	mail_send()

def server_up_mail():
	global msg,contents,msg_list,time_off,to,username
	contents = str("Server is Now working Fine & Was Off For {0} seconds".format(time_off))
	msg = MIMEText(contents)
	msg['Subject'] = 'Your Sever Is Up :) '
	msg['From'] = username
	msg['To'] = to  #Receiver's Mail Address
	mail_send()

def mail():
	#learn SMTP
	server_down_mail()
	print('Mail Sent')
	ping1()

def ping():
	global a,c,e,host
	a=c=e = 0
	c = time.time()
	response = os.system("ping -c 1 " + host )
	e = time.time()
	print(round(e-c,2))
	if response == 0:
		print('Server is Up!')
	else:
		a = time.time()
		mail()

def ping1():
	global b,d,f,time_off
	d=b=f = 0
	d = time.time()
	response = os.system("ping -c 1 " + host )
	f = time.time()
	print(round(f-d,2))
	if response == 0:
		b = time.time()
		time_off = round(b+e+f-a-c-d,2)
		server_up_mail()
		print('2nd Mail Sent')
		print('Server Is Now On\n'+'And Was Off For {0} seconds.'.format(round(b+e+f-a-c-d,2)))
		ping()
	else:
		ping1()

login()
host = input('Write Hostname or Address :- ') #Or address of server
to = msg['To'] = input('Enter Email To Send information About Server :- ')  #Receiver's Mail Address

schedule.every(0.1).minutes.do(ping)

while True:
	schedule.run_pending()
	time.sleep(0)

