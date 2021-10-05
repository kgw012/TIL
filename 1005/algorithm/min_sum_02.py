# swea 13037 '최소합'

def dfs(MAP, i, j):
    global N
    if i == N - 1 and j == N - 1:
        return MAP[i][j]
    
    if not 0 <= i < N or not 0 <= j < N:
        return 10000000
    
    return MAP[i][j] + min(dfs(MAP, i + 1, j), dfs(MAP, i, j + 1))


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
        total = dfs(MAP, i, j)

        print(f'#{t} {total}')
        