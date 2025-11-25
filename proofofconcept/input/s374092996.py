s = list(map(int, input().split()))
s.sort(reverse=1)
for i in range(4):
    print(s[i], end=" ")
print(s[4])

