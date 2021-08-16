# swea 1974 '스도쿠 검증'

T = int(input())

for t in range(1, T+1):
    MAP = []
    for _ in range(9):
        MAP.append(list(map(int, input().split())))
    
    row_check = [[False for num in range(10)] for row in range(9)]
    col_check = [[False for num in range(10)] for col in range(9)]
    box_check = [[False for num in range(10)] for box in range(9)]

    result = 1
    for row in range(9):
        for col in range(9):
            num = MAP[row][col]
            box = 3*(row // 3) + (col // 3)
            if row_check[row][num] or col_check[col][num] or box_check[box][num]:
                result = 0
                break
            row_check[row][num] = True
            col_check[col][num] = True
            box_check[box][num] = True
        if result == 0:
            break
    
    print('#{} {}'.format(t, result))