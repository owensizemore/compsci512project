a = map(int, raw_input().split())
a.sort()
a.reverse()
print " ".join(map(str, a))