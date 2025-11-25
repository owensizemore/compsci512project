while 1:
    try:
        n = (int(x) for x in input().split())
    except:break

    n = sorted(n,reverse=True)
    for i in range(5):
        if i :
            print(" ", end="")
        print(n[i],end="")
    print()
