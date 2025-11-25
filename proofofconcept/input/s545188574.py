#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

for s in sys.stdin:
  d = map(int , s.split())
  d.sort()
  d.reverse()
  for e in d:
    print e,