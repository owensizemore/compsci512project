#encoding=utf-8

num = map(int, raw_input().split())
num.sort()
num = num[::-1]
for i in xrange(len(num)):
    print num[i],