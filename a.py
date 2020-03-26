import math

k = int(input())
a = [i for i in range(1, k + 1)]
n = int(input()) - 1
answer = []
for i in range(k):
    answer.append(a.pop(n // math.factorial(k - 1)))
    n = n % math.factorial(k - 1)
    k -= 1
print(*answer)