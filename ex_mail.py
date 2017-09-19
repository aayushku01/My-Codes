# Import smtplib for the actual sending function
import smtplib,getpass

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

username = input('Enter Your Username (Sender) :- ')

contents = []
def msg_ex():
	global contents
	while True:
		try:
			a = input('>')
			contents.append(a)
		except EOFError:			#Ctrl+D
			print('\n')
			break


def msg_main():
	global contents
	msg1 = input('Write Msg Main Body :- \n>')
	contents.append(msg1)
	msg_ex()
	

msg_main()

msg = MIMEText('\n'.join(contents))

msg['From'] = 'aayushku01@gmail.com'
msg['To'] = input('Write Username for sending Msg (receiver) :- ')
msg['Subject'] = input('Write Subject :- ')

def mail_send():
	try:
		global msg,username
		password = getpass.getpass('Enter Pass :- ')
		s = smtplib.SMTP_SSL('smtp.gmail.com:465')
		s.ehlo()
		s.login(username,password)
		try:
			s.send_message(msg)
		finally:	
			s.quit()

	except Exception:
		print('Authentication Error')
		mail_send()

mail_send()
