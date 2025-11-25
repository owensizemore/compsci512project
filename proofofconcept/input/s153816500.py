a = [int(temp) for temp in input().split()]
a.sort(reverse = True)
a = [str(temp) for temp in a]
print(' '.join(a))