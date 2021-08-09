T = int(input())
for t in range(T):
    cards_str = input().strip()
    cnt_list = [0 for i in range(12)]

    for card in cards_str:
        num = int(card)
        cnt_list[num] += 1
    
    i = 0
    check_cnt = 0
    while i < 10:
        if cnt_list[i] >= 3:
            cnt_list[i] -= 3
            check_cnt += 1
            continue
        
        if cnt_list[i] and cnt_list[i + 1] and cnt_list[i + 2]:
            cnt_list[i] -= 1
            cnt_list[i + 1] -= 1
            cnt_list[i + 2] -= 1
            check_cnt += 1
            continue

        i += 1

    if check_cnt < 2:
        print(f'#{t + 1} Lose')
    else:
        print(f'#{t + 1} Baby Gin')