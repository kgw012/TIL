def dice(dice_nums, N, cnt):
    if cnt == N:
        print(*dice_nums, sep='')
        return

    for dice_num in range(1, 5):
        if visits[dice_num]:
            continue

        dice_nums[cnt] = dice_num
        visits[dice_num] = True
        dice(dice_nums, N, cnt + 1)
        visits[dice_num] = False


if __name__ == '__main__':
    N = int(input())
    visits = [False for _ in range(5)]
    dice_nums = [0 for _ in range(N)]
    dice(dice_nums, N, 0)