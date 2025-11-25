if __name__ == "__main__":
    a = map(int,raw_input().split())

    a.sort()
    a.reverse()
    for i in a:
        print i,