if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(*sorted(a, reverse=True))
