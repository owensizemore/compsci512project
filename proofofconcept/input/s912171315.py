n=map(int,raw_imput().split())
ans=[]
n.sort()
n.reverse()
for i in n:
	ans.append(str(i))
print(' '.join(ans))