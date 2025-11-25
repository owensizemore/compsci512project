L = [int(x) for x in input().split()]

L.sort(reverse=True)
print(" ".join(map(str,L)))
