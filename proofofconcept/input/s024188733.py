#!/usr/bin/python

line = raw_input()
l = map(int, line.strip().split())

l.sort()
l.reverse()
l = map(str, l)
out = ' '.join(l)
print out