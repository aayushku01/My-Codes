import time
s = time.time()
from functools import reduce
import math

a = []
for i in str(math.factorial(973)):
    a.append(int(i))
    
print(reduce(lambda x,y:x+y,a))

print(time.time()-s)

#----------------------------------------------------------------------------------------------

start_time = time.time()
from functools import reduce

def fac(n):
    if n>1:
        return n*fac(n-1)
    elif n==0:
        return 1
    elif n==1:
        return 1
    elif n<0:
        return None


a = []

for i in str(fac(960)):
    a.append(int(i))

print(reduce(lambda x,y:x+y,a))
print(time.time() - start_time)

#-------------------------------------------------------------------------------------------
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

a = []
for  i in str(factorial(995)):
    a.append(int(i))


print(reduce(lambda x,y:x+y,a))
