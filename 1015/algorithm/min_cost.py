# swea 13164 '최소 비용'

import heapq

if __name__ == '__main__':
    T = int(input())

    INF = 21e8
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for t in range(1, T + 1):
        N = int(input())
        MAP = []
        for _ in range(N):
            MAP.append(list(map(int, input().split())))
        
        c_map = [[INF] * N for _ in range(N)]
        c_map[0][0] = 0
        
        min_heap = []
        c, i, j = 0, 0, 0
        heapq.heappush(min_heap, (c, i, j))
        
        while min_heap:
            c, i, j = heapq.heappop(min_heap)
            if i == N-1 and j == N-1:
                answer = c
                break

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if not 0<=ni<N or not 0<=nj<N:
                    continue

                nc = c + (max(0, MAP[ni][nj] - MAP[i][j])) + 1
                if nc >= c_map[ni][nj]:
                    continue
                
                heapq.heappush(min_heap, (nc, ni, nj))
                c_map[ni][nj] = nc

        print(f'#{t} {answer}')
