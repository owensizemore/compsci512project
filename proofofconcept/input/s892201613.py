import sys

for s in sys.stdin:
    print(' '.join(map(str, sorted(map(int, s.split())))))