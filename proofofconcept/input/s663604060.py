numbers = list(map(int, input().split()))
numbers.sort()
numbers.reverse()
print(' '.join(map(str, numbers)))