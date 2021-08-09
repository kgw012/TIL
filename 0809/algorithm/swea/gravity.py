T = int(input())

for t in range(T):
    n = int(input())
    box_list = list(map(int, input().split()))
    max_fall = 0
    max_height = 0

    for i in range(n):
        height = box_list[i]
        if max_height >= height:
            continue

        max_height = height
        fall = n - i - 1
        if max_fall >= fall:
            continue
        
        for j in range(i + 1, n):
            if box_list[j] >= box_list[i]:
                fall -= 1

        if max_fall < fall:
            max_fall = fall
    
    print(f'#{t + 1} {max_fall}')