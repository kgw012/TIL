from collections import deque

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    for _ in range(E):
        node1, node2 = map(int, input().split())
        adj[node1][node2] = 1
        adj[node2][node1] = 1

    S, G = map(int, input().split())

    queue = deque()
    visits = [0 for _ in range(V + 1)]
    levels = [0 for _ in range(V + 1)]

    queue.append(S)
    visits[S] = True
    while queue:
        node = queue.popleft()

        if node == G:
            break

        for next_node in range(1, V + 1):
            if visits[next_node] or adj[node][next_node] == 0:
                continue

            queue.append(next_node)
            levels[next_node] = levels[node] + 1
            visits[next_node] = True

    print('#{} {}'.format(t, levels[G]))
