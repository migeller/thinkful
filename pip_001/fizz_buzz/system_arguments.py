#!/usr/bin/env python

import sys

print "The name of this script is {}".format(sys.argv[0])
print "User supplied {} arguments at run time".format(len(sys.argv) - 1)

for arg in sys.argv[1:]:
  print arg