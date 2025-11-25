a = [int(i) for i in input().split()]
sort = sorted(a, reverse=True)
for i in range(5):
    if i == 4:
        print(sort[i])
    else:
        print(sort[i], end = " ")
        