n = raw_input()
a = n.split()
a.sort()
a = a[::-1]
print " ".join(a)