# jungol 1733 '오목'

def check(i, j, dol):
    global MAP
    global di
    global dj

    for d in range(4):
        flag = True
        for cnt in range(1, 5):
            next_i = i + cnt * di[d]
            next_j = j + cnt * dj[d]

            if MAP[next_i][next_j] == dol:
                continue
            else:
                flag = False
                break
        if flag:
            reverse_i = i - di[d]
            reverse_j = j - dj[d]
            next_i = i + 5 * di[d]
            next_j = j + 5 * dj[d]
            if MAP[reverse_i][reverse_j] == dol or MAP[next_i][next_j] == dol:
                continue
            else:
                return dol

    return 0


if __name__ == '__main__':
    MAP = list()

    MAP.append([0 for _ in range(21)])
    for i in range(1, 20):
        MAP.append([0])
        MAP[i].extend(list(map(int, input().split())))
        MAP[i].append(0)
    MAP.append([0 for _ in range(21)])

    di = [0, 1, -1, 1]
    dj = [1, 0, 1, 1]

    result = 0
    for i in range(1, 20):
        flag = False
        for j in range(1, 20):
            if MAP[i][j]:
                result = check(i, j, MAP[i][j])
                if result:
                    flag = True
                    break
        if flag:
            break

    print(result)
    if flag:
        print(i, j)