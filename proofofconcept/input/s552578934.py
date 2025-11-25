from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from sys import stdin
gen = (int(s) for s in stdin.readline().split())
print(' '.join(str(i) for i in sorted(gen, reverse=True)))