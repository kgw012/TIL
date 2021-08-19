# swea 12632 '반복문자 지우기'(전용)

T = int(input())

for t in range(1, T+1):
    string = input().strip()

    stk = []

    for c in string:

        if stk and stk[-1] == c:
            stk.pop()
        else:
            stk.append(c)

    result = len(stk)

    print('#{} {}'.format(t, result))