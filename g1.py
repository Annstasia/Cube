def gen(left, k, a=[]):
    if left == 0:
        print(*a, k)
        return
    for i in range(left, k - 1, -1):
        gen(left - i, i, a + [k])


n = int(input())
for i in range(n, 0, -1):
    gen(n - i, i)
