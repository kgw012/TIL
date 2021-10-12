# swea 5650 '핀볼 게임'

def start(i, j, d):
    global N, MAP, di, dj, wall_dict, wormhall_dict

    point = 0

    while True:
        ni = i + di[d]
        nj = j + dj[d]

        m = MAP[ni][nj]

        if m < 0:
            break

        if m == 0:
            i, j = ni, nj
            continue
        
        if m <= 5:
            i, j = ni, nj
            d = wall_dict[m][d]
            point += 1
            continue

        if m <= 10:
            i, j = map(int, wormhall_dict[f'{ni} {nj}'].split())
            continue

    return point


if __name__ == '__main__':
    T = int(input())

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    wall_dict = {
        1: {
            0: 1,
            1: 3,
            2: 0,
            3: 2
        },
        2: {
            0: 3,
            1: 0,
            2: 1,
            3: 2
        },
        3: {
            0: 2,
            1: 0,
            2: 3,
            3: 1
        },
        4: {
            0: 1,
            1: 2,
            2: 3,
            3: 0
        },
        5: {
            0: 1,
            1: 0,
            2: 3,
            3: 2
        }
    }

    for t in range(1, T + 1):
        N = int(input())
        MAP = [[5] * (N + 2)]
        for i in range(1, N + 1):
            MAP.append([5])
            MAP[i].extend(list(map(int, input().split())))
            MAP[i].append(5)
        MAP.append([5] * (N + 2))
        
        wormhall_dict = dict()
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if MAP[i][j] >= 6:
                    for i2 in range(1, N + 1):
                        for j2 in range(1, N + 1):
                            if i == i2 and j == j2:
                                continue

                            if MAP[i][j] == MAP[i2][j2]:
                                wormhall_dict[f'{i} {j}'] = f'{i2} {j2}'
                                wormhall_dict[f'{i2} {j2}'] = f'{i} {j}'
        
        answer = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if MAP[i][j] != 0:
                    continue

                for d in range(4):
                    save_m = MAP[i][j]
                    MAP[i][j] = -1

                    point = start(i, j, d)
                    answer = max(answer, point)

                    MAP[i][j] = save_m
        
        print(f'#{t} {answer}')
