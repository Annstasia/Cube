def next(arr):
    for i in range(n - 1, 0, -1):
        # print(i, arr[i], arr[i-1])
        if arr[i] > arr[i - 1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            print(''.join(arr))
            return True
    return False


arr = list(input())
n = len(arr)
if not next(arr):
    print(''.join(sorted(arr)))
