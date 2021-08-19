# swea 12626 '괄호 검사'(전용)

T = int(input())

for t in range(1, T+1):
    string = input().strip()

    stk = []

    result = 1
    for c in string:
        if c == '(' or c == '{':
            stk.append(c)
        elif c == ')':
            if not stk:
                result = 0
                break
            pop_c = stk.pop()
            if pop_c != '(':
                result = 0
                break
        elif c == '}':
            if not stk:
                result = 0
                break
            pop_c = stk.pop()
            if pop_c != '{':
                result = 0
                break

    if stk:
        result = 0

    print('#{} {}'.format(t, result))