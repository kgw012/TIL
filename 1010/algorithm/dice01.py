def dice(n, dices, cnt):
    if cnt >= n:
        print(*dices, sep=' ')
        return

    for dice_num in range(1, 7):
        dices[cnt] = dice_num
        dice(n, dices, cnt + 1)


if __name__ == '__main__':
    N = 3
    dices = [0 for _ in range(N)]
    dice(N, dices, 0)