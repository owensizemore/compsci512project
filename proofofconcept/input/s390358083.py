import sys

line = sys.stdin.readline()
line = line.split(" ")
inp = []
for i in line:
    inp.append(int(i))
inp.sort()
inp.reverse()
for i in inp:
    if inp.index(i)<len(inp)-1:
        print (i, end=" ")
    else:
        print (i)