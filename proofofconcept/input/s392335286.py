#!/usr/bin/python

import sys

for line in sys.stdin:
	l = line.strip().split()
	l.sort()
	l.reverse()
	out = ' '.join(l)
	print out