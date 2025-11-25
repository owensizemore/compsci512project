import sys
from functools import reduce
l = sorted(map(int,sys.stdin.readline().rstrip().split(' ')))[::-1]
print(' '.join(map(str,l)))