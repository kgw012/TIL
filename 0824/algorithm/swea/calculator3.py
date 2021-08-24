# swea 1224 '게산기3'

def postfix_notation(string):
    global op_rank

    result = ''
    stk = []
    for c in string:
        if c.isdigit():
            result += c
            continue

        if len(stk) == 0 or c == '(':
            stk.append(c)
            continue

        if c == ')':
            while stk[-1] != '(':
                result += stk.pop()
            stk.pop()
            continue

        while len(stk) and op_rank[stk[-1]] >= op_rank[c]:
            result += stk.pop()

        stk.append(c)

    while len(stk):
        result += stk.pop()

    return result


def calculate(string):
    stk = []

    for c in string:
        if c.isdigit():
            stk.append(int(c))
            continue

        num2 = stk.pop()
        num1 = stk.pop()

        result = 0
        if c == '+':
            result = num1 + num2
        else:
            result = num1 * num2

        stk.append(result)

    return stk.pop()


if __name__ == '__main__':
    op_rank = {
        '(': 0,
        '+': 1,
        '*': 2
    }

    T = 10

    for t in range(1, T+1):
        N = int(input())
        string = input().rstrip()
        result = calculate(postfix_notation(string))

        print('#{} {}'.format(t, result))

