# swea 12670 '미로'(전용)

def check_maze(MAP, visits, i, j):
    if MAP[i][j] == '3':
        return 1

    global di
    global dj

    for d in range(4):
        next_i = i + di[d]
        next_j = j + dj[d]

        if visits[next_i][next_j] or MAP[next_i][next_j] == '1':
            continue

        visits[next_i][next_j] = True
        if check_maze(MAP, visits, next_i, next_j):
            return 1
        visits[next_i][next_j] = False

    return 0


if __name__ == '__main__':
    T = int(input())

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for t in range(1, T+1):
        N = int(input())

        MAP = [['1' for _ in range(N + 2)]]
        for i in range(1, N + 1):
            MAP.append(['1'])
            MAP[i].extend(list(input().rstrip()))
            MAP[i].extend('1')
        MAP.append(['1' for _ in range(N + 2)])

        st_i = 0
        st_j = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if MAP[i][j] == '2':
                    st_i, st_j = i, j
                    break
            else:
                continue
            break

        visits = [[False for _ in range(N + 2)] for _ in range(N + 2)]
        visits[st_i][st_j] = True
        result = check_maze(MAP, visits, st_i, st_j)
        print('#{} {}'.format(t, result))