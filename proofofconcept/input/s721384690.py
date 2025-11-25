a,b,c,d,e = map(int, input().split())
while True:
  if a < b:
    b,a = a,b
  elif b < c:
    c,b = b,c
  elif c < d:
    d,c = c,d
  elif d < e:
    e,d = d,e
  else:
    print(a,b,c,d,e)
    break
