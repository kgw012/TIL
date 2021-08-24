#swea 12676 '배열 최소 합'(전용)

def dfs(i, total):
    global N
    global min_total
    if i == N:
        if total < min_total:
            min_total = total
        return

    if total >= min_total:
        return

    global lst
    global col_visits
    for j in range(N):
        if col_visits[j]:
            continue
        col_visits[j] = True
        dfs(i + 1, total + lst[i][j])
        col_visits[j] = False

    return


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        N = int(input())
        lst = []
        for _ in range(N):
            lst.append(list(map(int, input().split())))

        col_visits = [False for _ in range(N)]

        min_total = 10000

        dfs(0, 0)

        print('#{} {}'.format(t, min_total))
