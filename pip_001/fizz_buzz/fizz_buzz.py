#!/usr/bin/env python

import sys

def modulo(x, y):
	""" Determines if we can divide x from y evenly. """
	if x % y == 0:
		return True
	else:
		return False

def stepper(limit=100):
	""" Steps through from 1 to limit and prints out a fizzbuzz sequence. """
	print "Our Upper Limit is %d! Let's go!" % limit
	for n in xrange(1, limit + 1):
	# 	if modulo(n, 5) and modulo(n, 3):
	# 		print "fizzbuzz"
		if modulo(n, 3):
			print "fizz",
			if modulo(n, 5):
				print "buzz"
			else:
				print ""
		elif modulo(n, 5):
			print "buzz"
		else:
			print n

if __name__ == '__main__':
	try:
		i = sys.argv[1]
	except IndexError:
		stepper()
	else:
		try:
			limit = int(i)
		except ValueError:
			stepper()
		else:
			stepper(limit)