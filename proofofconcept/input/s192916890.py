a=map(int,input().split())
a.sort()
a=a[::-1]
print("%d %d %d %d %d"%tuple(a))