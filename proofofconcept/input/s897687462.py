import sys

for input_line in sys.stdin:
    input_line = input_line.split()
    input_line.sort(reverse=True)
    print ' '.join(input_line)