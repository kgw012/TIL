if __name__ == '__main__':
    MAP = [
        [3, 2, 1, 7],
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [1, 1, 1, 1]
    ]

    dr = [-1, -1, 1, 1]
    dc = [-1, 1, 1, -1]

    r, c = map(int, input().split())
    max_value = 0
    max_r = 0
    max_c = 0

    for d in range(4):
        next_r = r + dr[d]
        next_c = c + dc[d]

        if next_r >= len(MAP) or next_r < 0 or next_c >= len(MAP[0]) or next_c < 0:
            continue

        value = MAP[next_r][next_c]
        if value > max_value:
            max_r = next_r
            max_c = next_c
            max_value = value

    print('({}, {}) : {}'.format(max_r, max_c, max_value))
