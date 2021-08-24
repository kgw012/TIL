def dice(dice_nums, N, cnt):
    if cnt == N:
        print(*dice_nums, sep='')
        return

    for dice_num in range(1, 5):
        dice_nums[cnt] = dice_num
        dice(dice_nums, N, cnt + 1)


if __name__ == '__main__':
    N = int(input())
    dice_nums = [0 for _ in range(N)]
    dice(dice_nums, N, 0)