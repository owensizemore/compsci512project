# AOJ 0018 Sorting Five Numbers
# Python3 2018.6.11 bal4u

a = list(map(int, input().split()))
a.sort()
print(*a[::-1])
