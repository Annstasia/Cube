n, k = map(int, input().split())
comb = [i for i in range(1, k + 1)]
print(*comb)
def next(comb):
    for i in range(k - 1, -1, -1):
        if comb[i] <= n - k + i:
            comb[i] += 1
            for j in range(i + 1, k):
                comb[j] = comb[j - 1] + 1
            return True
    return False
while next(comb):
    print(*comb)
