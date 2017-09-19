a = 123
b = 6512
c = 123

if not(a >= c):
	print "1"

elif a < b:
	print "2"

else :
	print "3"



if a > b:
	print "4"

elif a == c:
	print "5"

elif b > c:
	print "6"

print "Now let us decrease b"

b %= 956

if a == c:
	print ".1"

if a > b:
	print ".2"

if b > c:
	print ".3"

if a < b:
	print ".4"

if a < c:
	print ".5"

if b < c:
	print ".6"
