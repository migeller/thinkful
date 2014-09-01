#!/usr/bin/env python

while True:
	s = raw_input('Enter something : ')
	if s == 'quit':
		break
	if len(s) < 3:
		print 'Too small!'
		continue
	print 'Input is of sufficient length'
print 'Done!'