#! -*- coding:utf-8 -*-
nums = map(int, raw_input().split())
nums_sort = sorted(nums,reverse=True)
ans = " ".join(map(str,nums_sort))
print ans