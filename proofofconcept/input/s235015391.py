l = map(int, raw_input().strip().split(" "));
print " ".join(map(str, sorted(l, lambda x, y: y - x)));