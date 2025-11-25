import sys

for input_line in sys.stdin:
    input_line = raw_input().split()
    input_line.sort(reverse=True)
    print ' '.join(input_line)