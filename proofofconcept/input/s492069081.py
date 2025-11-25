
import sys

#input_file = open(sys.argv[1], "r")

#for line in input_file:
for line in sys.stdin:
    nums = map(int, line.split(' '))
    nums.sort(lambda x, y: cmp(y, x))
#    print ' '.join(map((lambda x: str(x)), nums))
    print ' '.join(map(str, nums))