import sys
import math as mas

a=list(map(int,input().split()))
a.sort()
a.reverse()
print(*a)

#for i in sys.stdin:
#	a,b=map(int,i.split())
#	print(gcd(a,b),lcm(a,b))