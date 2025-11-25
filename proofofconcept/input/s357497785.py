# -*- coding:utf-8 -*-

data = input()
n = [0]*5
n[0],n[1],n[2],n[3],n[4] = map(int,data.split(' '))

count = 0
while True:
    for i in range(len(n)-1):
        if n[i] < n[i+1]:
            tmp = n[i]
            n[i] = n[i+1]
            n[i+1] = tmp
    count += 1
    if count == 5:
        break

for i in range(len(n)-1):
    print(n[i],end=' ')

print(n[len(n)-1])