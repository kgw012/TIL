# swea 1859 '백만 장자 프로젝트'

T = int(input())

for t in range(1, T+1):
    N = int(input())
    price_list = list(map(int, input().split()))

    i = 0
    result = 0
    while i < len(price_list):
        max_price = -1
        max_idx = -1

        for j in range(i, len(price_list)):
            if max_price < price_list[j]:
                max_price = price_list[j]
                max_idx = j
        
        buy_price = 0

        for j in range(i, max_idx + 1):
            buy_price += price_list[j]
            
        sell_price = max_price * (max_idx - i + 1)
        result += (sell_price - buy_price)

        i = max_idx + 1
    
    print('#{} {}'.format(t, result))