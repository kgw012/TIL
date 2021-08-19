# swea 1234 '비밀번호'

T = 10

for t in range(1, T+1):
    n, password = input().split()
    n = int(n)

    stk = []

    for c in password:
        if stk and c == stk[-1]:
            stk.pop()
        else:
            stk.append(c)

    result = ''.join(stk)

    print('#{} {}'.format(t, result))
