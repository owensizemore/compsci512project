import sys

a = input()
n = list(map(int, a.strip().split()))

n.sort()
n.reverse()

for i in range(len(n)):
    print(n[i], end="")
    if i < len(n)-1:
        print(" ", end="")

print()