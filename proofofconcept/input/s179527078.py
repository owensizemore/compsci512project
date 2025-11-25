a = list(map(int, input().split()))
a.sort()
a.reverse()
for i in  range(5):
  if i == 4:
    print(a[i])
  else:
    print(a[i], "", end = "")
