#!/usr/bin/env python

dict = {"a": 1, "b": 2}

key = raw_input('Enter a key: ')

try:
	print dict[str(key)]
except KeyError:
	print "dude, that is not in this dictionary"