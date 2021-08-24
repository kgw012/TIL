def dfs(adj, visits, path, node):
    if node == 3:
        print(path)
        return True

    for next_node in range(4):
        if visits[next_node]:
            continue

        if adj[node][next_node]:
            visits[next_node] = True
            dfs(adj, visits, path + str(next_node), next_node)
            visits[next_node] = False


if __name__ == '__main__':
    adj = [
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 0]
    ]

    visits = [False for _ in range(4)]
    visits[0] = True
    dfs(adj, visits, '0', 0)