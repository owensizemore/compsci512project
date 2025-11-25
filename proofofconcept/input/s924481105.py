numlist = [eval(item) for item in input().split()]
numlist.sort()
numlist.reverse()
for i in range(len(numlist)):
	print(numlist[i], end = '')
	if i != len(numlist) - 1:
		print(end = ' ')
print()