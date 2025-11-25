# -*- coding: utf-8 -*-
l = input().split()
print(' '.join(str(e) for e in sorted(l, reverse=True)))