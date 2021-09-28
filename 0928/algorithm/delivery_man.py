# swea 13008 '배달맨'(전용)

from collections import deque

T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for t in range(1, T + 1):
    H, W, N = map(int, input().split())

    MAP = []
    for h in range(H):
        MAP.append(input())
    

    i, j = 0, 0
    total = 0

    for num in range(1, N + 1):
        visits = [[0 for _ in range(W)] for _ in range(H)]
        visits[i][j] = True
        que = deque()
        que.append((i, j, 0))
        
        while que:
            pi, pj, cnt = que.popleft()

            if MAP[pi][pj] == str(num):
                total += cnt
                i, j = pi, pj
                break

            for d in range(4):
                ni = pi + di[d]
                nj = pj + dj[d]

                if not 0 <= ni < H or not 0 <= nj < W:
                    continue
                
                if visits[ni][nj]:
                    continue

                if MAP[ni][nj] == '#':
                    continue
                
                visits[ni][nj] = True
                que.append((ni, nj, cnt + 1))

    print(f'#{t} {total}')