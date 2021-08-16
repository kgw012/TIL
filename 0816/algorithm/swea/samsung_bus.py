# swea 6485 '삼성시의 버스 노선'

T = int(input())
for t in range(1, T+1):
    n = int(input())
    
    bus_stops = [0 for _ in range(5001)]
    for _ in range(0, n):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            bus_stops[i] += 1

    p = int(input())

    result_list = []
    for _ in range(p):
        c = int(input())

        result_list.append(bus_stops[c])
    
    print('#{}'.format(t), end=' ')
    print(*result_list, sep=' ')