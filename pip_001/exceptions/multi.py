#!/usr/bin/env python

import sys

try:
	file_name = sys.argv[1]
except IndexError:
	print "Hey! You forgot to include an argument of a file to open!"

try:
	f = open(file_name, 'r')
except NameError:
	print "We didn't get a valid file name."
except IOError as (err_number, err_string):
	print "We got an IOError of {0}: {1}".format(err_number, err_string)
else:
	s = f.readline()
	s = s.strip()
	print s
