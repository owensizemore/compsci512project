a = []
a = [int(i) for i in input().split()]
a.sort(reverse=True)
b = " ".join([str(i) for i in a])
print(b)
