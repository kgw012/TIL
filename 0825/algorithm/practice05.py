from collections import deque


def enqueue_children(queue, node):
    global adj
    for i in range(len(adj)):
        if adj[node][i]:
            queue.append(i)
    return


if __name__ == '__main__':
    values = [0, 1, 1, 3, 2, 4, 5, 2]
    adj = [[0 for _ in range(8)] for _ in range(8)]
    adj[0][1] = 1
    adj[0][2] = 1
    adj[0][3] = 1
    adj[1][4] = 1
    adj[1][5] = 1
    adj[1][6] = 1
    adj[3][7] = 1

    queue = deque()
    enqueue_children(queue, 0)
    enqueue_children(queue, queue.popleft())
    print(*queue)