data = raw_input().split(' ')
data = sorted(map(int, data))[::-1]
print ' '.join(data)