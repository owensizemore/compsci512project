data = raw_input().split(' ')
data = map(str, sorted(map(int, data))[::-1])
print ' '.join(data)