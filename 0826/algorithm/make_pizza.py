from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    c_list = list(map(int, input().split()))

    pizza_que = deque([i for i in range(M)])
    pit = deque()

    for _ in range(N):
        pit.append(pizza_que.popleft())

    while len(pit) > 1:
        pizza_num = pit.popleft()
        c_list[pizza_num] //= 2
        if c_list[pizza_num] == 0:
            if len(pizza_que):
                pit.append(pizza_que.popleft())
            continue
        pit.append(pizza_num)

    print('#{} {}'.format(t, pit.popleft() + 1))
