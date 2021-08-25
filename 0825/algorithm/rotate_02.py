#swea 12704 '회전'(전용)

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    front = 0
    rear = 0
    M %= N

    for _ in range(M):
        item = lst[front]
        front = (front + 1) % len(lst)
        lst[rear] = item
        rear = (rear + 1) % len(lst)

    print('#{} {}'.format(t, lst[front]))
