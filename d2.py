x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x, y = map(int, input().split())
flag1 = 0
flag2 = 0
flag3 = 0
if (x - x1) * (y2 - y) == (x2 - x) * (y - y1) and (x2 - x)*(x1 - x) + (y2 - y) * (y1 - y) <= 0:
    print('In')
elif (x - x2) * (y3 - y) == (x3 - x) * (y - y2) and (x3 - x) * (x2 - x) + (y3 - y) * (y2 - y) <= 0:
    print('In')
elif (x - x3) * (y1 - y) == (x1 - x) * (y - y3) and (x1 - x) * (x3 - x) + (y1 - y) * (y3 - y) <= 0:
    print('In')
else:
    if (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1) > 0:
        flag1 = 1
    if (x3 - x2) * (y - y2) - (x - x2) * (y3 - y2) > 0:
        flag2 = 1
    if (x1 - x3) * (y - y3) - (x - x3) * (y1 - y3) > 0:
        flag3 = 1

    if flag1 == flag2 == flag3:
        print('In')
    else:
        print('Out')