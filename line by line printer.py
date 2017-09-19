from sys import argv

a , infile = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print1(lc , f):
	print lc , f.readline()

ofile = open(infile)

print "Now let us print the whole file:"

print_all(ofile)

print "Now let us print it like tape:"

rewind(ofile)

print "now let us print line by line"

cl = 1

print1(cl,ofile) 

cl = cl + 1

print1(cl,ofile)

cl = cl + 1

print1(cl , ofile)

ofile.close()

