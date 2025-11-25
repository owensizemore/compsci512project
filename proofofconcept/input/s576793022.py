l = [int(s) for s in raw_input().split()]
l = [str(s) for s in sorted(l, reverse=True)]
print ' '.join(l)