import math
x1, y1, x2, y2 = map(int, input().split())
print(math.acos((x1*x2 + y1*y2) / ((x1 * x1 + y1 * y1) ** 0.5 * (x2 * x2 + y2*y2) ** 0.5)))
