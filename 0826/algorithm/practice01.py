from collections import deque

if __name__ == '__main__':
    adj = [[0 for _ in range(8)] for _ in range(8)]

    adj[1][2] = 1
    adj[1][3] = 1
    adj[2][5] = 1
    adj[3][7] = 1
    adj[4][2] = 1
    adj[4][6] = 1
    adj[5][6] = 1
    adj[6][4] = 1
    adj[7][3] = 1
    adj[7][6] = 1

    queue = deque()
    visits = [0 for _ in range(8)]

    queue.append(1)
    level = 1
    visits[1] = 1

    while queue:
        node = queue.popleft()

        for next_node in range(1, 8):
            if visits[next_node] or adj[node][next_node] == 0:
                continue

            queue.append(next_node)
            visits[next_node] = visits[node] + 1

    print(*visits)

