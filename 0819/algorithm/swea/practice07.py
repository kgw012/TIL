def dfs(now):
    for next_v in range(8):
        if adj[now][next_v] == 1:
            dfs(next_v)

    print(now, end=' ')
    return


if __name__ == '__main__':
    adj = [[0 for _ in range(8)] for _ in range(8)]

    adj[0][1] = 1
    adj[0][2] = 1
    adj[1][3] = 1
    adj[1][4] = 1
    adj[2][5] = 1
    adj[5][6] = 1
    adj[5][7] = 1

    dfs(0)