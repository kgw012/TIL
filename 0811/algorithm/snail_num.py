T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T+1):
    n = int(input())

    lst = [[0 for _ in range(n+2)] for _ in range(n+2)]

    for i in range(1, n+2):
        lst[0][i] = -1
        lst[n + 1][i] = -1
        lst[i][0] = -1
        lst[i][n + 1] = -1

    i = 1
    j = 0
    num = 1
    d = 0
    while num <= n*n:
        next_i = i + di[d]
        next_j = j + dj[d]

        if lst[next_i][next_j]:
            d = (d + 1) % 4
            continue

        i = next_i
        j = next_j
        lst[i][j] = num
        num += 1

    print('#{}'.format(t))
    for i in range(1, n+1):
        print(*lst[i][1:n+1], sep=' ')