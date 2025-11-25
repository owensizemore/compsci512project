def main():
    A = input().split()
    A.sort()
    A.reverse()   
    _str = " ".join(A)
    print(_str)

if __name__ == '__main__':
    main()