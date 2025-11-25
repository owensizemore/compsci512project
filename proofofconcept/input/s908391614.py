# coding=utf-8

number_list = list(map(int, input().split()))
number_list.sort()
number_list.reverse()
print(' '.join(map(str, number_list)))