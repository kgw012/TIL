def go(MAP, rings, visits, cnt, M, N, L, i, j):
    if i == 0 and j == N - 1:
        return cnt - 1
    
    cnts = [100]
    for idx, (ri, rj) in enumerate(rings):
        if visits[idx]:
            continue

        d = abs(ri - i) + abs(rj - j)
        if d <= L:
            visits[idx] = True
            cnts.append(go(MAP, rings, visits, cnt + 1, M, N, L, ri, rj))
            visits[idx] = False

    return min(cnts)


T = int(input())

for t in range(1, T + 1):
    M, N, L = map(int, input().split())
    MAP = []
    for _ in range(M):
        MAP.append(list(map(int, input().split())))

    rings = []
    for i in range(M):
        for j in range(N):
            if MAP[i][j] == 1:
                rings.append((i, j))

    rings.append((0, N - 1))
    visits = [False] * (len(rings) + 1)
    answer = go(MAP, rings, visits, 0, M, N, L, M - 1, 0)
    if answer == 100:
        answer = -1
    print(f'#{t} {answer}')
