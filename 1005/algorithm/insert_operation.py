# 백준 14888 '연산자 끼워넣기'
# https://www.acmicpc.net/problem/14888

def calculate(n1, n2, op_idx):
    if op_idx == 0:
        return n1 + n2
    if op_idx == 1:
        return n1 - n2
    if op_idx == 2:
        return n1 * n2
    if op_idx == 3:
        if n1*n2 < 0:
            return -(abs(n1) // abs(n2))
        return n1 // n2

    return


def dfs(cnt, result):
    global N, numbers, ops, min_result, max_result
    if cnt >= N - 1:
        if result < min_result:
            min_result = result
        if result > max_result:
            max_result = result
        return
    
    for op_idx in range(4):
        if ops[op_idx] == 0:
            continue
        
        ops[op_idx] -= 1
        dfs(cnt + 1, calculate(result, numbers[cnt + 1], op_idx))
        ops[op_idx] += 1
    
    return


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    ops = list(map(int, input().split()))

    min_result = 21e8
    max_result = -21e8
    
    cnt = 0
    result = numbers[0]
    dfs(cnt, result)

    print(max_result)
    print(min_result)