

import sys

lineNumber = 0
#for line in [ "xlmw mw xli tmgxyvi xlex m xsso mr xli xvmt." ]:
for line in sys.stdin.readlines():
    lineNumber += 1

    # get data
    List = map(int, line.strip().split(","))

    List = List.sort().reverse()

    print "%d %d %d %d %d" % (List[0], List[1], List[2], List[3], List[4])