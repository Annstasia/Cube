def gen(left, a = []):
    if left == 0:
        print(*a)
        return
    gen(left - 1, a + [0])
    gen(left -1, a + [1])
    gen(left - 1, a + [2])
gen(3)