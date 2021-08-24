# swea 12669 'forth'

def calculate(lst):
    stk = []

    for c in lst:
        if c.isdigit():
            stk.append(int(c))
            continue

        if c == '.':
            if len(stk) != 1:
                return 'error'
            return stk.pop()

        if len(stk) == 0:
            return 'error'
        num2 = stk.pop()

        if len(stk) == 0:
            return 'error'
        num1 = stk.pop()

        result = 0
        if c == '+':
            result = num1 + num2
        elif c == '-':
            result = num1 - num2
        elif c == '*':
            result = num1 * num2
        elif c == '/':
            result = num1 // num2
        else:
            return 'error'

        stk.append(result)
    return result


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        lst = input().rstrip().split()
        result = calculate(lst)

        print('#{} {}'.format(t, result))