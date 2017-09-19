from sys import argv 

a,b = argv

print "Write Add Of file To Open\n"

b = raw_input("File To Open")

c = open(b,'w')

print "Hold Your Breath"

print """"Now I am Clearing the content of your file

if you don't want to do it press 'Ctrl+C'

Else press 'Return'"""

raw_input(">")

c.truncate()

print "Now  i am gona ask you for 3 lines to enter to write in program:"

l1 = raw_input(">Line 1:")
l2 = raw_input(">Line 2:")
l3 = raw_input(">line 3:")

print "now i am gona write then to your file"

c.write(l1)
c.write("\n")
c.write(l2)
c.write("\n")
c.write(l3)
c.write("\n")

print "Now your file's content has been changed. \n Now i am gona show you the new file"

print "If you have trust on me then press 'Ctrl+C' else press 'Return' "

raw_input("?")

c.close()	#very imp as if it is not done we can not read file.

d = open(b)

print d.read()

d.close()
