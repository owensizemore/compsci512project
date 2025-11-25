N = list(map(int, input().split()))
N.sort()

for i in range(5) :
    if(i != 4) :
        print(N[4 - i], end = " ")
    else :
        print(N[0])
