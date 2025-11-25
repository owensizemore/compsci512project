# -*- coding: utf-8 -*-
import math

a=list(map(int, input().split()))

a.sort()
a.reverse()
print(*a)
