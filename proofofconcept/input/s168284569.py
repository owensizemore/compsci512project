num = list(map(int, input().split()))

num.sort(reverse=True)

for i, n in enumerate(num):
    if i == len(num) - 1:
        print(n)
    else:
        print(str(n) + " ", end="")

