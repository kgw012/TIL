# swea 12625 '종이 붙이기'(전용)

def glue(cnt):
    if cnt == 1:
        return 1
    if cnt == 2:
        return 3

    return glue(cnt - 1) + 2 * glue(cnt - 2)


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        result = glue(N // 10)

        print('#{} {}'.format(t, result))