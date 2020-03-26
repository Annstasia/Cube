'''def gen(left, s=0):
    n = 0
    if left == 0:
        return 1
    if left - 1 >= s + 1:
        n += gen(left - 1, s + 1)
    if s > 0:
        n += gen(left - 1, s - 1)
    return n
print(gen(int(input())))'''
print(3 / 4 ** 0.5)