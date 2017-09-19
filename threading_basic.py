import threading
from queue import Queue
import time

print_lock = threading.Lock()

def example_job(job):
	time.sleep(.5)

	with print_lock:
		print(threading.current_thread().name,job)

def threader():
	while True:
		job = q.get
		example_job(job)
		q.task_done()

q = Queue()

for x in range(15):
	t = threading.Thread(target=threader)
	t.daemon = True
	t.start()

start = time.time()

for job in range(25):
	q.put(job)

q.join()

print('Total Time = ',time.time()-start)
