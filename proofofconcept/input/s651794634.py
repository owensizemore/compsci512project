lis=list(map(int,input().split()))
lis.sort()
for i in range(4,-1,-1):
    if i!=4:
        print(" ",end="")

    print(lis[i],end="")

print("")