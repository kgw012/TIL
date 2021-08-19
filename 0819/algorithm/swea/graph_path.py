# swea 12627 '그래프 경로'(전용)

def check_path(nodes, s, G):
    if s == G:
        return 1

    if not nodes[s]['edges']:
        return 0

    for g in nodes[s]['edges']:
        if nodes[g]['visit']:
            continue

        nodes[g]['visit'] = True
        if check_path(nodes, g, G):
            return 1

    return 0


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    nodes = {}
    for v in range(1, V+1):
        nodes[v] = {'edges': list(), 'visit': False}

    for _ in range(1, E+1):
        s, g = map(int, input().split())
        nodes[s]['edges'].append(g)

    S, G = map(int, input().split())

    nodes[S]['visit'] = True
    result = check_path(nodes, S, G)

    print('#{} {}'.format(t, result))