'''arr = list(input())
n = len(arr)
s_arr = sorted(arr)
def gen(left_num, a = []):
    if len(a) == n:
        print(*a)
        return
    for i in range(n):
        if left_num[i]:
            left_num[i] = False
            gen(left_num, a + [s_arr[i]])
            left_num[i] = True
gen([True] * n)'''
a = [1, 2]
print(a[3:])
'''
dels = [2]
def func(dels, i):
    for j in dels:
        if i % j == 0:
            return  False
    return True
for i in range(3, 500):
    if func(dels, i):
        dels.append(i)
print(dels)'''