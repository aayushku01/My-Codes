import time, os, schedule, redis

host = input('Write Hostname or Address :- ') #Or address of server
rd = redis.StrictRedis(host='localhost', db=0)
redis_db_flush = os.system('redis-cli flushall')
time_start = time.time()

redis_db_flush

def ping1():
	global host,time_start,rd
	response = os.system("ping -c 1 " + host )
	if response == 0:
		time2 = time.time()
		print('Server is Up!')
		rd.set(round(time2-time_start,2),1)
	else:
		time2 = time.time()
		rd.set(round(time2-time_start,2),0)

def ping():
	global host,time_start,rd
	response = os.system("ping -c 1 " + host )
	if response == 0:
		rd.set(0,1)
		print('Server is Up!')
		time2 = time.time()
		rd.set(round(time2-time_start,2),1)
	else:
		time2 = time.time()
		rd.set(round(time2-time_start,2),0)


schedule.every(0.1).minutes.do(ping)

while True:
	schedule.run_pending()
	time.sleep(0)
