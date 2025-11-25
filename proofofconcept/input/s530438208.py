# -*- coding: utf-8 -*-
l = [int(e) for e in input().split()]
print(' '.join(str(e) for e in sorted(l, reverse=True)))