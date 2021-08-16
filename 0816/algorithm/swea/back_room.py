# swea 4408 '자기 방으로 돌아가기'

class Move:
    def __init__(self, st, fn):
        if st > fn:
            st, fn = fn, st
        self.st = (st - 1) // 2
        self.fn = (fn - 1) // 2


T = int(input())

for t in range(1, T+1):
    N = int(input())

    move_list = []
    for _ in range(N):
        st, fn = map(int, input().split())
        move_list.append(Move(st, fn))
    
    move_list.sort(key=lambda move: move.st)

    cnt = 0
    while len(move_list):
        st = move_list[0].st
        fn = move_list[0].fn
        move_list.pop(0)

        i = 0
        while i < len(move_list):
            move = move_list[i]
            if move.st > fn:
                fn = move.fn
                move_list.pop(i)
                continue
            i += 1
        
        cnt += 1
    
    print('#{} {}'.format(t, cnt))