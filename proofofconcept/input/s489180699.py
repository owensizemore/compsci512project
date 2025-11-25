

import sys

lineNumber = 0

#for line in ["3 6 9 7 5"]:
for line in sys.stdin.readlines():
    lineNumber += 1

    # get data
    List = map(int, line.strip().split(" "))

    List.sort()

    print "%d %d %d %d %d" % (List[4], List[3], List[2], List[1], List[0])