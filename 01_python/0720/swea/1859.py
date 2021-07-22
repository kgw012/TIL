test_cases = int(input())

for t in range(1, test_cases + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    sum_price = 0
    max_price = -1

    for i in range(n-1, -1, -1):
        price = arr[i]
        if price > max_price:
            max_price = price
        else:
            sum_price += (max_price - price)
    
    print('#{} {}'.format(t, sum_price))
