l = map(int,raw_input().split())
l.sort()
l.reverse()
l = list(map(str, l))
output = ' '.join(l)
print output
