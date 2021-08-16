# swea 5432 '쇠막대기 자르기'

T = int(input())

for t in range(1, T+1):
    st = input()

    cnt = 0
    stk = []
    flag = False
    for s in st:
        if s == '(':
            stk.append(0)
            flag = True
        else:
            if flag:
                stk.pop()
                cnt += len(stk)
            else:
                stk.pop()
                cnt += 1
            flag = False
    
    print('#{} {}'.format(t, cnt))