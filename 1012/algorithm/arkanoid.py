# swea 5656 '벽돌 깨기'

from collections import deque

def shoot(tmp_map, i, j):
    global H, W

    que = deque()
    que.append((i, j))

    while que:
        i, j = que.popleft()

        for length in range(1, tmp_map[i][j]):
            for d in range(4):
                ni = i + length * di[d]
                nj = j + length * dj[d]

                if not 0<=ni<H or not 0<=nj<W:
                    continue
                
                que.append((ni, nj))
        
        tmp_map[i][j] = 0
    
    for j in range(W):
        for i in range(H-1, -1, -1):
            if tmp_map[i][j]:
                que.append(tmp_map[i][j])
                tmp_map[i][j] = 0

        i = H - 1
        while que:
            tmp_map[i][j] = que.popleft()
            i -= 1
    
    return


def dfs(tmp_map, cnt):
    global N, min_block, W, H
    if cnt >= N:
        block_cnt = 0
        for j in range(W):
            for i in range(H - 1, -1, -1):
                if not tmp_map[i][j]:
                    break
                block_cnt += 1
        
        min_block = min(min_block, block_cnt)
        return
    
    for j in range(W):
        for i in range(H):
            if tmp_map[i][j]:
                tmp_map2 = [m[:] for m in tmp_map]
                shoot(tmp_map2, i, j)
                dfs(tmp_map2, cnt + 1)
                break
        else:
            dfs(tmp_map, cnt + 1)

    return


if __name__ == '__main__':
    T = int(input())

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for t in range(1, T + 1):
        N, W, H = map(int, input().split())

        MAP = []
        for _ in range(H):
            MAP.append(list(map(int, input().split())))
        
        min_block = 21e8

        dfs(MAP, 0)

        print(f'#{t} {min_block}')