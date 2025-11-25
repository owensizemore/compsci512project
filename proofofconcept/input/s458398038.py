x = map(int,raw_input().split(' '))
x.sort()
x.reverse()
output = ''
for val in x:
	output += str(val) + ' '
print output.strip()