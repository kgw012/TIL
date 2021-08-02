n = int(input())

dice_nums = []
for i in range(n):
    dice_nums.append(list(map(int, input().split())))

bottom_to_top = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}

get_side_idxes = {
    0: [1, 2, 3, 4],
    1: [0, 2, 4, 5],
    2: [0, 1, 3, 5],
    3: [0, 2, 4, 5],
    4: [0, 1, 3, 5],
    5: [1, 2, 3, 4]
}

max_total = 0
for i in range(6):
    top_idx = bottom_to_top[i]
    top_num = dice_nums[0][top_idx]
    side_idxes = get_side_idxes[i]
    # total = max(map(lambda idx: dice_nums[0][idx], side_idxes))
    total = max(dice_nums[0][idx] for idx in side_idxes)

    for j in range(1, len(dice_nums)):
        bottom_idx = dice_nums[j].index(top_num)
        top_idx = bottom_to_top[bottom_idx]
        top_num = dice_nums[j][top_idx]
        side_idxes = get_side_idxes[bottom_idx]
        # total += max(map(lambda idx: dice_nums[j][idx], side_idxes))
        total += max(dice_nums[j][idx] for idx in side_idxes)

    if max_total < total:
        max_total = total

print(max_total)
