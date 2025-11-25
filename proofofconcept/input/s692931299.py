x=input().split()
y=sorted(x,reverse=True)
for i in range(len(y)-1):
	print(y[i],end="")
	print(' ',end="")
print(y[len(y)-1])