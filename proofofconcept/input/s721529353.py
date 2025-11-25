import sys

a = map(int, sys.stdin.readline().strip().split())
a.sort()
a.reverse()
print " ".join(a)