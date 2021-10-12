# swea 1861 '정사각형 방'

def dfs(i, j):
    global N, MAP, memo, di, dj

    if memo[i][j] > 0:
        return memo[i][j]

    max_ret = 1
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if not 0<=ni<N or not 0<=nj<N:
            continue
        if MAP[i][j] + 1 != MAP[ni][nj]:
            continue

        ret = dfs(ni, nj) + 1
        max_ret = max(ret, max_ret)

    memo[i][j] = max_ret
    return max_ret


if __name__ == '__main__':
    T = int(input())

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for t in range(1, T + 1):
        N = int(input())
        MAP = []
        for _ in range(N):
            MAP.append(list(map(int, input().split())))

        memo = [[0 for _ in range(N)] for _ in range(N)]
        max_length = 0
        min_number = 21e8

        for i in range(N):
            for j in range(N):
                length = dfs(i, j)
                if length == max_length:
                    min_number = min(min_number, MAP[i][j])

                if length > max_length:
                    max_length = length
                    min_number = MAP[i][j]
        
        print(f'#{t} {min_number} {max_length}')
