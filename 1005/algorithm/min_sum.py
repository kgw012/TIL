# swea 13037 '최소합'

def dfs(MAP, total, i, j):
    global N
    if i == N - 1 and j == N - 1:
        global min_total
        if total < min_total:
            min_total = total
        
        return

    global di, dj
    for d in range(2):
        ni = i + di[d]
        nj = j + dj[d]

        if not 0 <= ni < N or not 0 <= nj < N:
            continue
        
        dfs(MAP, total + MAP[ni][nj], ni, nj)


if __name__ == '__main__':
    T = int(input())

    di = [0, 1]
    dj = [1, 0]

    for t in range(1, T + 1):
        N = int(input())
        MAP = []
        for _ in range(N):
            MAP.append(list(map(int, input().split())))
        
        i, j = 0, 0
        min_total = 1000000
        total = MAP[i][j]

        dfs(MAP, total, i, j)
        
        print(f'#{t} {min_total}')