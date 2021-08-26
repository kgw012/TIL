# swea 1226 '미로'

from collections import deque

T = 10

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T+1):
    input()
    MAP = []
    N = 16
    for _ in range(N):
        MAP.append(list(map(int, input())))

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                st_i, st_j = i, j
            if MAP[i][j] == 3:
                fn_i, fn_j = i, j

    queue = deque()
    queue.append((st_i, st_j))
    MAP[st_i][st_j] = 1

    flag = 0
    while queue:
        i, j = queue.popleft()
        if MAP[i][j] == 3:
            flag = 1
            break

        MAP[i][j] = 1

        for d in range(4):
            next_i = i + di[d]
            next_j = j + dj[d]

            if MAP[next_i][next_j] == 1:
                continue

            queue.append((next_i, next_j))

    print('#{} {}'.format(t, flag))
