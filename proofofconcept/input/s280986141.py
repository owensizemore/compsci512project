#!/usr/bin/python

line = raw_input()
l = line.strip().split()
l.sort()
l.reverse()
out = ' '.join(l)
print out