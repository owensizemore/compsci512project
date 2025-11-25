Num = list(map(int,input().split()))
Num.sort()
Num = Num[::-1]
for i in range(len(Num)):
    if i == len(Num)-1:
        print(Num[i])
    else:
        print(Num[i],end = ' ')