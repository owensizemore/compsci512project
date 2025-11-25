# -*- coding: utf-8 -*-

import sys
import os

lst = list(map(int, input().split()))
lst.sort(reverse=True)

print(*lst)