ls = map(int,raw_input().split())
ls.sort(reverse=True)
print " ".join(map(str,ls))