def int_sort(num1, num2):
	return cmp(int(num1), int(num2))

n = raw_input()
a = n.split()
a = sorted(a, cmp=int_sort)
a = a[::-1]
print " ".join(a)