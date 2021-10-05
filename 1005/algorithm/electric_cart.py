# swea 13040 '전자카트'

def dfs(ptr, cnt, total):
    global MAP, N
    if cnt == N - 1:
        global min_total

        total += MAP[ptr][0]
        
        if total < min_total:
            min_total = total
        return
    
    global visits
    for next in range(1, N):
        if visits[next]:
            continue
        
        visits[next] = True
        dfs(next, cnt + 1, total + MAP[ptr][next])
        visits[next] = False

    return


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        MAP = []
        for _ in range(N):
            MAP.append(list(map(int, input().split())))
        
        visits = [False for _ in range(N)]

        min_total = 21e8

        ptr = 0
        cnt = 0
        total = 0
        dfs(ptr, cnt, total)

        print(f'#{t} {min_total}')