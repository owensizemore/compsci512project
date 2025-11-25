
if __name__ == '__main__':
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    print(*a)