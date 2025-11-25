import sys

line = sys.stdin.readline()
line = line.split(" ")
inp = []
for i in line:
    inp.append(int(i))
inp.sort()
inp.reverse()
for i in range(len(inp)):
    if i<len(inp)-1:
        print (inp[i], end=" ")
    else:
        print (inp[i])