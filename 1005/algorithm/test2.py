# 정올 1462 '보물섬'
# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=734&sca=3040

from collections import deque

if __name__ == '__main__':
    N, M = map(int, input().split())
    MAP = []
    for _ in range(N):
        MAP.append(list(input()))

    visits = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 'W':
                visits[i][j] = True
    
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    st_points = []

    for i in range(N):
        for j in range(M):
            if visits[i][j]:
                continue
            
            st_points.append((i, j))

            que = deque()
            que.append((i, j))

            while que:
                ti, tj = que.popleft()

                for d in range(4):
                    ni = ti + di[d]
                    nj = tj + dj[d]

                    if not 0 <= ni < N or not 0 <= nj < M:
                        continue
                    
                    if visits[ni][nj]:
                        continue
                    
                    visits[ni][nj] = True
                    que.append((ni, nj))
            
            st_points.append((ti, tj))

    max_distance = 0

    visits = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 'W':
                visits[i][j] = True

    for ti, tj in st_points:
        t_que = deque()
        level = 0
        t_que.append((ti, tj, level))

        while t_que:
            ti, tj, level = t_que.popleft()

            for d in range(4):
                ni = ti + di[d]
                nj = tj + dj[d]

                if not 0 <= ni < N or not 0 <= nj < M:
                    continue
                
                if visits[ni][nj]:
                    continue
                
                visits[ni][nj] = True
                t_que.append((ni, nj, level + 1))

        if level > max_distance:
            max_distance = level
    
    print(st_points)
    print(max_distance)