s=list(map(int, input().split()))
s.sort()
s.reverse()

for i in s:
    print(str(i)+" ", end="")

print()