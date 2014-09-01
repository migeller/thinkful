#!/usr/bin/env python

upper_limit = 100

for n in xrange(1, upper_limit + 1):
	if n % 3 == 0 and n % 5 == 0:
		print "fizzbuzz"
	elif n % 3 == 0:
		print "fizz"
	elif n % 5 == 0:
		print "buzz"
	else:
		print n