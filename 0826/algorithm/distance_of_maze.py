from collections import deque

T = int(input())

for t in range(1, T+1):
    N = int(input())

    MAP = [['1' for _ in range(N + 2)] for _ in range(N+2)]

    st_i, st_j = 0, 0
    for i in range(1, N + 1):
        string = input().strip()
        for j in range(1, N + 1):
            MAP[i][j] = string[j - 1]
            if MAP[i][j] == '2':
                st_i, st_j = i, j

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    queue = deque()
    visits = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

    i, j = st_i, st_j
    queue.append((i, j))
    visits[i][j] = 1

    flag = False
    while queue:
        i, j = queue.popleft()
        if MAP[i][j] == '3':
            flag = True
            break

        for d in range(4):
            next_i = i + di[d]
            next_j = j + dj[d]
            if MAP[next_i][next_j] == '1' or visits[next_i][next_j]:
                continue

            queue.append((next_i, next_j))
            visits[next_i][next_j] = visits[i][j] + 1

    if flag:
        print('#{} {}'.format(t, visits[i][j] - 2))
    else:
        print('#{} {}'.format(t, 0))
