def main():
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    for x in a:
        print(x, end = " ")
    print()




if __name__ == "__main__":
    main()