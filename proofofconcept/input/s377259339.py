def main():
    numbers = map(int, input().split())
    numbers = sorted(numbers, reverse=True)
    print(*numbers)

if __name__ == "__main__":
    main()