# swea 1861 '정사각형 방'

from collections import deque

def bfs(i, j):
    global MAP, N, di, dj

    que = deque()
    level = 1
    que.append((i, j, level))

    while que:
        i, j, level = que.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if not 0<=ni<N or not 0<=nj<N:
                continue

            if MAP[ni][nj] != MAP[i][j] + 1:
                continue

            que.append((ni, nj, level + 1))
    
    return level
    

if __name__ == '__main__':
    T = int(input())

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for t in range(1, T + 1):
        N = int(input())
        MAP = []
        for _ in range(N):
            MAP.append(list(map(int, input().split())))
        
        max_cnt = 0
        answer = 10000000
        for i in range(N):
            for j in range(N):
                cnt = bfs(i, j)
                if cnt == max_cnt:
                    if MAP[i][j] < answer:
                        answer = MAP[i][j]
                if cnt > max_cnt:
                    max_cnt = cnt
                    answer = MAP[i][j]
        
        print(f'#{t} {answer} {max_cnt}')
