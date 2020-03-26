def step(s):
    flag = 0
    x = 0
    y = 0
    steps = 0
    was = [[0, 0]]
    for i in range(len(s)):

        if s[i] == 'L':
            flag = (flag - 1) % 4
        elif s[i] == 'R':
            flag = (flag + 1) % 4
        else:
            steps += 1
            if flag == 1:
                x += 1
            elif flag == 0:
                y += 1
            elif flag == 2:
                y -= 1
            elif flag == 3:
                x -= 1
            if [x, y] in was:
                return steps
            was.append([x, y])
            print(was, [x, y])
    if steps == 0:
        return steps
    return -1


print(step(input()))