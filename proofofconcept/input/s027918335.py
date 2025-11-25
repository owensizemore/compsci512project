x = map(int, raw_input().split())
x.sort()
x.reverse()
output = ''
for num in x:
	output += str(num) + ' '
print output.strip()