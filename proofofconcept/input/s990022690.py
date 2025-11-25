A=[int(i) for i in input().split()]
A.sort(reverse=True)
print(" ".join(map(str,A)))