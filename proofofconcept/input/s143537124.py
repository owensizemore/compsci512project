line = input().split()
print(' '.join(sorted(line, key=int, reverse=True)))