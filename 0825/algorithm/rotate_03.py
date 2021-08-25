#swea 12704 '회전'(전용)

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    que = [0 for _ in range(2 * N)]
    front = 0
    rear = 0
    M %= N

    for _ in range(M):
        item = lst[front]
        front += 1
        lst[rear] = item
        rear += 1

    print('#{} {}'.format(t, lst[front]))
