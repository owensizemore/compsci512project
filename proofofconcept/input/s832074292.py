l = list(map(int,input().split()))
l.sort(reverse=True)
l = [str(i) for i in l]
print(' '.join(l))