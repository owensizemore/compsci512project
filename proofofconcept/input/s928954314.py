nums = input().split()
print(" ".join(nums.sort(reverse=True) or nums))