while True:
    try:
        l = raw_input().split()
        if len(l)==0:
            break
        l.sort()
        l.reverse()
        output = ' '.join(l)
        print output
    except:
        break
