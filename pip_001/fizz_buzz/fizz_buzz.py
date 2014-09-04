#!/usr/bin/env python

upper_limit = 0
i = ""

import sys

try:
	i = sys.argv[1]
except IndexError:
	print "I see you didn't provide an Upper Limit as an argument."
	
while upper_limit == 0:
	try:
		upper_limit = int(i)
	except ValueError:
		print "I need an integer here. Help me out."
		i = raw_input("Please enter an Upper Limit now: ")

print "Our Upper Limit is %d! Let's go!" % upper_limit

for n in xrange(1, upper_limit + 1):
	if n % 3 == 0 and n % 5 == 0:
		print "fizzbuzz"
	elif n % 3 == 0:
		print "fizz"
	elif n % 5 == 0:
		print "buzz"
	else:
		print n
