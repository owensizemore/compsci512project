s=list(map(int, input().split()))
s.sort()
s.reverse()

for i in s:
    print(i, end="")
    if i != s[4]:
        print(" ", end="")

print()