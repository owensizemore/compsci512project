def main():
    A = list(map(int,input().split()))
    A.sort()
    A.reverse()   
    print(*A)

if __name__ == '__main__':
    main()