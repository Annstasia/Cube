def find(x1, y1, x2, y2, x3, y3, x4, y4):
    a1 = y1 - y2
    b1 = x2 - x1
    c1 = x1 *(y2 - y1) - y1 * (x2 - x1)
    a2 = y3 - y4
    b2 = x4 - x3
    c2 = x3 *(y4 - y3) - y3 * (x4 - x3)
    # print(a1, b1, c1, a2, b2, c2)
    '''if a1 * b2 == a2 * b1 and a1 * c2 == a2 * c1:
        print(2)
    elif a1 * b2 == a2 * b1:
        print(0)
    else:'''
    y = (a1*c2 - a2 * c1) / (a2 * b1 - a1 * b2)
    if a1 != 0:
        x = (-c1 - b1 * y) / a1
    else:
        x = (-c2 - b2 * y) / a2
    print(x, y)


x1, y1, x2, y2, x3, y3 = map(int, input().split())
a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
c = ((x2 - x3) ** 2 + (y3 - y2) ** 2) ** 0.5
k1 = a / b
x23 = (x2 + k1 * x3) / (1 + k1)
y12 = (y2 + k1 * y3) / (1 + k1)
k2 = c / a
x13 =  (x3 + k2 * x1) / (1 + k2)
y13 = (y3 + k2 * y1) / (1 + k2)
find(x1, y1, x23, y12, x2, y2, x13, y13)
