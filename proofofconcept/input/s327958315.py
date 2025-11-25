l = [int(i) for i in input().split()]
l.sort()
l.reverse()
print(' '.join([str(i) for i in l]))