# 정올 1462 '보물섬'
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=734&sca=3040

from sys import stdin
from collections import deque

if __name__ == '__main__':
    N, M = map(int, stdin.readline().split())
    MAP = []
    for _ in range(N):
        MAP.append(list(stdin.readline().strip()))
    
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    max_distance = -1

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 'W':
                continue

            visits = [[False for _ in range(M)] for _ in range(N)]

            que = deque()
            level = 0
            que.append((i, j, 0))

            while que:
                ti, tj, level = que.popleft()

                for d in range(4):
                    ni = ti + di[d]
                    nj = tj + dj[d]

                    if not 0 <= ni < N or not 0 <= nj < M:
                        continue
                    
                    if MAP[ni][nj] == 'W':
                        continue

                    if visits[ni][nj]:
                        continue
                    
                    visits[ni][nj] = True
                    que.append((ni, nj, level + 1))

            if level > max_distance:
                max_distance = level

    print(max_distance)