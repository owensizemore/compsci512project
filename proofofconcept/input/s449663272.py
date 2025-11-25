l = input().split(' ')
for i in range(5):
    l[i] = int(l[i])
l.sort(reverse = True)
print(l[0], l[1], l[2], l[3], l[4])