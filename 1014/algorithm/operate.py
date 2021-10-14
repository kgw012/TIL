# swea 13158 '연산'

from collections import deque

def calc(num, cmd):
    if cmd == 0:
        return num + 1
    if cmd == 1:
        return num - 1
    if cmd == 2:
        return num * 2
    return num - 10


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N, M = map(int, input().split())
        visits = [False] * 1000001

        que = deque()
        que.append((N, 0))
        visits[N] = True

        while que:
            num, level = que.popleft()

            if num == M:
                break
            
            for cmd in range(4):
                n_num = calc(num, cmd)

                if not 0 < n_num <= 1000000:
                    continue

                if visits[n_num]:
                    continue
                
                visits[n_num] = True
                que.append((n_num, level + 1))

        print(f'#{t} {level}')
