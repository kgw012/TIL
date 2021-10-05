def dice(n, dices, visits, cnt):
    if cnt >= n:
        print(*dices, sep=' ')
        return

    for dice_num in range(1, 7):
        if visits[dice_num]:
            continue
        
        dices[cnt] = dice_num
        visits[dice_num] = True
        dice(n, dices, visits, cnt + 1)
        visits[dice_num] = False


if __name__ == '__main__':
    N = 3
    dices = [0 for _ in range(N)]
    visits = [0 for _ in range(7)]
    dice(N, dices, visits, 0)