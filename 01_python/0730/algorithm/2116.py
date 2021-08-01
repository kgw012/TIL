class Dice:

    parse_up_idx = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
    parse_side_list = {
        0: [1, 2, 3, 4],
        1: [0, 2, 4, 5],
        2: [0, 1, 3, 5],
        3: [0, 2, 4, 5],
        4: [0, 1, 3, 5],
        5: [1, 2, 3, 4]
    }

    def __init__(self, num_list, bottom_num):
        self.num_list = num_list
        self.bottom_idx = num_list.index(bottom_num)
        self.up_idx, self.side_idx_list = self.matching_dice(self.bottom_idx)
        self.up_num = num_list[self.up_idx]
        self.side_max = self.find_side_max()

    def matching_dice(self, bottom_idx):

        up_idx = self.parse_up_idx[bottom_idx]
        side_idx_list = self.parse_side_list[bottom_idx]

        return up_idx, side_idx_list

    def find_side_max(self):
        max = 0
        for idx in self.side_idx_list:
            num = self.num_list[idx]
            if max < num:
                max = num
        return max

# input
n = int(input())

dice_num_list = []
for i in range(n):
    dice = list(map(int, input().split()))
    dice_num_list.append(dice)
    
# 1번 주사위 정하기
# x의 숫자가 아래로 왔을때, 옆 면으로 올수 있는 숫자들 뽑아내기
# 뽑아낸 숫자들 중에 최대값 고르기
# total에 추가하기

total_list = []
first_num_list = dice_num_list[0]
for bottom_num in first_num_list:
    total = 0
    first_dice = Dice(first_num_list, bottom_num)

    next_bottom_num = first_dice.up_num
    first_side_max = first_dice.side_max
    total += first_side_max

    for i in range(1, n):
        num_list = dice_num_list[i]
        dice = Dice(num_list, next_bottom_num)
        
        next_bottom_num = dice.up_num
        side_max = dice.side_max
        total += side_max

    total_list.append(total)

print(max(total_list))