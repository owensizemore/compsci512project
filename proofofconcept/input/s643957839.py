# AOJ 0018 Sorting Five Numbers
# Python3 2018.6.11 bal4u

a = list(map(int, input().split()))
a.sort(reverse=True)
for i in a:
	print(i, end = " ")
print()
