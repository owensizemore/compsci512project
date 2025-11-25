# Aizu Problem 0018: Sorting Five Numbers
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


print(' '.join([str(_) for _ in sorted([int(__) for __ in input().split()], reverse=True)]))