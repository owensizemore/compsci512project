lst = sorted(list(map(int, input().split())), reverse=True)
for i in range(len(lst)):
    if i != len(lst) - 1:
        print(lst[i], end = " ")
    else:
        print(lst[i])
