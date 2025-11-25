from math import *
PI = 3.1415926535898
while True:
	try:
		n = map(int, raw_input().strip().split(' '))
		n.sort()
		ans = ""
		c = False
		for x in reversed(n):
			if c:
				ans += ' '
			c = True
			ans += str(x)
		print ans
	except EOFError:
		break