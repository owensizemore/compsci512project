a = [ int(x) for x in input().strip().split() ]
a = sorted(a, reverse=True)
for i in range(len(a)):
    if i > 0:
        print(" ", end='')
    print(a[i], end='')
print()
