user = input()
a = []
b = []
b = user.split()
for i in range(5):
    a.append(int(b[i]))
for j in range(4):
    for k in range(j+1, 5):  # j<k
        if a[j] < a[k]:
            tmp = a[j]
            a[j] = a[k]
            a[k] = tmp

for j in range(5):
    if j == 4:
        print(a[j])
    else:
        print(str(a[j]), end=" ")