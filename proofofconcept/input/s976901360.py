numList = list(map(int, input().split()))

numList.sort(reverse=True)

print(' '.join(map(str, numList)))

