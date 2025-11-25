import string
print string.join(map(str, sorted(map(int, raw_input().split()), reverse=True)))