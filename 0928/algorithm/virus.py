from collections import deque

# swea 12981 '바이러스'(전용)

T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for t in range(1, T + 1):
    N, M = map(int, input().split())

    MAP = []
    for i in range(N):
        MAP.append(list(map(int, input().split())))

    net_nums = [[0 for _ in range(M)] for _ in range(N)]
    net_num = 0

    que = deque()

    for i in range(N):
        for j in range(M):
            if net_nums[i][j]:
                continue

            if not MAP[i][j]:
                continue
            
            net_num += 1
            net_nums[i][j] = net_num
            que.append((i, j))

            while que:
                pi, pj = que.popleft()

                for d in range(4):
                    ni = pi + di[d]
                    nj = pj + dj[d]
                    if not 0 <= ni < N or not 0 <= nj < M:
                        continue
                    
                    if not MAP[ni][nj]:
                        continue

                    if net_nums[ni][nj]:
                        continue

                    net_nums[ni][nj] = net_nums[pi][pj]
                    que.append((ni, nj))
                
    
    infections = [False for _ in range(net_num + 1)]

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 2:
                num = net_nums[i][j]
                infections[num] = True
    
    cnt = 0
    for is_infected in infections:
        if is_infected:
            cnt += 1
    
    print(f'#{t} {cnt}')