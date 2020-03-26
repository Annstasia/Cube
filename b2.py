x, y,  x1, y1, x2, y2 = map(int, input().split())

if ((x - x1)*(x2 - x1) + (y - y1) * (y2 - y1)) < 0:
    print(((x - x1) ** 2 + (y - y1) ** 2) ** 0.5)
elif ((x - x2) * (x1 - x2) + (y - y2) * (x1 - x2)) < 0:
    print(((x - x2) ** 2 + (y - y2) ** 2) ** 0.5)
elif x1 == x2 and y1 == y2:
    print(((x - x1) ** 2 + (y - y1) ** 2) ** 0.5)
else:

    print("{:.5f}".format(abs((x2 - x1) * (y - y1) - (x - x1) * (y2 - y1)) / (((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5)))
