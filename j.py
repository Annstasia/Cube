def check(x1, y1, x2, y2, x3, y3, x4, y4):
    if ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) * ((x2 - x1) * (y4 - y1) - (x4 - x1) * (y2 - y1)) < 0:
        return True
    elif (x1 - x3) * (y2 - y3) == (x2 - x3) * (y1 - y3) and (x1 - x3) * (x2 - x3) + (y2 - y3) * (y1 - y3) <= 0:
        return True
    elif (x1 - x4) * (y2 - y4) == (x2 - x4) * (y1 - y4) and (x1 - x4) * (x2 - x4) + (y2 - y4) * (y1 - y4) <= 0:
        return True
    elif (x3 - x1) * (y4 - y1) == (x4 - x1) * (y3 - y1) and (x3 - x1) * (x4 - x1) + (y4 - y1) * (y3 - y1) <= 0:
        return True
    elif (x3 - x2) * (y4 - y2) == (x4 - x2) * (y3 - y2) and (x3 - x2) * (x4 - x2) + (y4 - y2) * (y3 - y2) <= 0:
        return True

    else:
        return False

n, x, y = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
