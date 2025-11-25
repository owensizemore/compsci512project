s = input().split()
arr = [int(s[i]) for i in range(5)]
arr.sort(reverse=True)
for i in range(len(arr)):
    if i != len(arr)-1:
        print(arr[i], end=" ")
    else:
        print(arr[i])