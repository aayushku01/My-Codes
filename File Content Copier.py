from sys import argv 
from os.path import exists

a,b,c = argv

print "Write Add Of file from which you want to write"

b = raw_input("File To Read\n")

print "write add of file to which you want to write."

c = raw_input("File to write\n")

d = open(b)

f = d.read()

print "Hold Your Breath"

print "Now i am gona check weather your exists or not - %r " % exists(c)

print "you input file is %r long" % len(f)

print """now i am gona change the content of your second file

if you don't want to do it press 'Ctrl+C'

Else press 'Return'"""

raw_input(">")

e = open(c,'w')

g = e.write(f)

e.close()
d.close()	#very imp as if it is not done we can not read file.

h = open(c)

print h.read()

h.close()
