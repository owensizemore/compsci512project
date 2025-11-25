line = [int(i) for i in input().split()]
line.sort(reverse=True)
for i in range(5):
  print(line[i], end=" " if i != 4 else "\n")