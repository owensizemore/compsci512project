line = [int(i) for i in input().split()]
line.sort(reverse=True)
for l in line:
  print(l, end=" ")