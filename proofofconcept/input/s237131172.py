x=input().split()
y=sorted(x,reverse=True)
a=[]
b=[]
for i in range(len(y)):
	if int(y[i])>=0:
		a.append(y[i])
	else:
		b.append(abs(int(y[i])))
b=sorted(b)
for i in range(len(b)):
	a.append(-b[i])
for i in range(len(a)-1):
	print(a[i],end="")
	print(' ',end="")
print(a[len(a)-1])