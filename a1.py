left, k = map(int, input().split())
chars = list(map(chr, range(ord('0'), ord('9') + 1))) + list(map(chr, range(ord('a'), ord('z') + 1)))
chars = chars[:k]
def gen(left, a=''):
    if left == 0:
        print(a)
        return
    for i in range(k - 1, -1, -1):
        gen(left - 1, a + chars[i])
gen(left)