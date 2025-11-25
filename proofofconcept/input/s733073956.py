l = list(map(int, input().split))
l.sort()
l.reverse()
print(" ".join(map(str, l)))