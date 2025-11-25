numlist = [eval(item) for item in input().split()]
numlist.sort()
numlist.reverse()
for item in numlist:
	print(item, end = ' ')