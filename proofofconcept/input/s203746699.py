l = map(int, raw_input().strip().split(" "));
print " ".join(sorted(l, lambda x, y: y - x));