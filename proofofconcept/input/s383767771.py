s=list(map(int, input().split()))
s.sort()

for i in s:
    print(str(i), end="")
    if i != s[-1]:
        print(" ", end="")

print()