# swea 12627 '그래프 경로'(전용)

def check_path(adj, s, G):
    if s == G:
        return 1

    for g in range(1, len(adj)):
        if not adj[s][g]:
            continue

        adj[s][g] = 0
        if check_path(adj, g, G):
            return 1

    return 0


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    for _ in range(1, E+1):
        s, g = map(int, input().split())
        adj[s][g] = 1

    S, G = map(int, input().split())

    result = check_path(adj, S, G)

    print('#{} {}'.format(t, result))