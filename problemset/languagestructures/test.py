# cat test.py | ./mapper.py

#! /usr/bin/env python3.4
import sys

N = int(sys.stdin.readline())
ans = []
for i in range(N):
    tri = sys.stdin.readline()[:-1].split(' ', 3)
    newlist = []
    for n in tri:
        newlist.append(int(n))
    newlist.sort()
    if newlist[0] * newlist[0] + newlist[1] * newlist[1] == newlist[2] * newlist[2]:
        ans.append("YES")
    else:
        ans.append("NO")
for a in ans:
    print(a)