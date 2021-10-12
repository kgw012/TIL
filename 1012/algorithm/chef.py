# swea 4012 '요리사'

def dfs(idx, cnt):
    global N, S, min_diff, visits
    if cnt == N//2:
        total1 = 0
        total2 = 0
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue

                if visits[i] and visits[j]:
                    total1 += S[i][j]
                
                if (not visits[i]) and (not visits[j]):
                    total2 += S[i][j]
        
        diff = abs(total1 - total2)
        min_diff = min(min_diff, diff)

        return

    if idx >= N:
        return

    dfs(idx + 1, cnt)
    visits[idx] = True
    dfs(idx + 1, cnt + 1)
    visits[idx] = False

    return


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        S = []
        for _ in range(N):
            S.append(list(map(int, input().split())))
        
        min_diff = 21e8
        visits = [False] * N
        dfs(0, 0)

        print(f'#{t} {min_diff}')