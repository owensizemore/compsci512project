nums = map(int, raw_input().split())
nums.sort(reverse=True)
print " ".join(map(str, nums))