while True:
    a = list(map(int, (input().split())))
    a = sorted(a, reverse=True)
    for i in range(4): print(a[i],end=' ')
    print(a[4])
