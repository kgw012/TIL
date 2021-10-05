T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    c_stk = list(map(int, input().split()))
    t_stk = list(map(int, input().split()))

    c_stk.sort()
    t_stk.sort()

    answer = 0

    while c_stk and t_stk:
        if c_stk[-1] <= t_stk[-1]:
            answer += c_stk.pop()
            t_stk.pop()
        else:
            c_stk.pop()
    
    print(f'#{t} {answer}')
