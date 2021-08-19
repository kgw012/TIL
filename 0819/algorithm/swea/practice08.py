def dfs(now):

    for next_node in range(len(adj)):
        if adj[now][next_node] == 1 and not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node)


if __name__ == '__main__':
    adj = [
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 0]
    ]

    visited = [0, 0, 0, 0]
    visited[0] = 1
    dfs(0)