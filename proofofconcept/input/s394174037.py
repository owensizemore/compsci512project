ns = map(int, raw_input().split(" "))
count = 0
for loop in xrange(4):
	for i in xrange(4):
		if ns[i] < ns[i+1]:
			print ns[i+1]
			ns[i] , ns[i+1] = ns[i+1] , ns[i]
print ns[0],ns[1],ns[2],ns[3],ns[4]