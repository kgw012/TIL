from collections import deque

if __name__ == '__main__':
    MAP = [[0 for _ in range(3)] for _ in range(5)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    queue = deque()
    queue.append((0, 0))
    MAP[0][0] = 1

    while queue:
        i, j = queue.popleft()
        answer = MAP[i][j]

        for d in range(4):
            next_i = i + di[d]
            next_j = j + dj[d]

            if next_i < 0 or next_j < 0 or next_i >= len(MAP) or next_j >= len(MAP[0]):
                continue
            if MAP[next_i][next_j]:
                continue

            MAP[next_i][next_j] = MAP[i][j] + 1
            queue.append((next_i, next_j))

    print(answer)
