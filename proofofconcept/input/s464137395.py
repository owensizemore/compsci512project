lst = map(int, raw_input().split())
lst.sort()
lst.reverse()
ans = str(lst[0])
for i in range(1, 5):
	ans = ans + ' ' + str(lst[i])
print ans
