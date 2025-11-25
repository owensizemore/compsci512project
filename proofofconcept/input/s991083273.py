while True:
    try:
        print "%d %d %d %d %d" % tuple(sorted(list(map(eval,raw_input().split()))))
    except EOFError: break