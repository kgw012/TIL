C_COST = 1
Q_COST = 2

T = int(input())

for t in range(1, T + 1):
    S = input()

    # 천지인 자판 확인
    OFFSET = ord('a')
    prev = S[0]
    c_cnt = (ord(prev) - OFFSET) % 3 + 1

    for i in range(1, len(S)):
        c = S[i]
        if (ord(prev) - OFFSET)//3 == (ord(c) - OFFSET)//3:
            c_cnt += 1
        
        c_cnt += (ord(c) - OFFSET) % 3 + 1
        prev = c
    
    c_cost = c_cnt * C_COST

    # 쿼티 자판 확인
    q_cnt = len(S)
    q_cost = q_cnt * Q_COST

    # 대소 비교 후 정답 출력
    answer = ''

    if c_cost < q_cost:
        answer = 'CHEONJIIN'
    elif c_cost > q_cost:
        answer = 'QWERTY'
    else:
        answer = 'DRAW'
    
    print('#{} {}'.format(t, answer))
