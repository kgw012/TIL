# swea 1219 '길찾기'

def check_way(edges, visits, node):
    if node == 99:
        return 1

    for next_node in edges[node]:
        if visits[next_node]:
            continue

        visits[next_node] = True
        if check_way(edges, visits, next_node):
            return 1

    return 0


if __name__ == '__main__':
    T = 10

    for _ in range(1, T+1):
        t, n = map(int, input().split())

        edges = [list() for _ in range(100)]
        visits = [False for _ in range(100)]

        input_list = list(map(int, input().split()))
        for i in range(n):
            v1 = input_list[2 * i]
            v2 = input_list[2 * i + 1]

            edges[v1].append(v2)

        visits[0] = True
        result = check_way(edges, visits, 0)

        print('#{} {}'.format(t, result))