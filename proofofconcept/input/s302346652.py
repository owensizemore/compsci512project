def run():
    numbers = sorted(list(map(int, input().split())), reverse=True)
    print(' '.join([str(n) for n in numbers]))

if __name__ == '__main__':
    run()


