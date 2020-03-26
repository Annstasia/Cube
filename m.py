import math
n = int(input())
if n % 2 == 1:
    print(0)
else:
    print((math.factorial(n) // math.factorial(n//2) ** 2) // (n // 2 + 1))