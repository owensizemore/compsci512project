Num = list(map(int,input().split()))
Num.sort()
Num = Num[::-1]
for i in range(len(Num)):
    print(Num[i],end = ' ')