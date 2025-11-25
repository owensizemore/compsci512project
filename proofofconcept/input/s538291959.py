x = map(int, raw_input().split(' '))
x.sort()
for i in range(len(x)):
   print x[-(i+1)],