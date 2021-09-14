# 건물 붕괴게임. 정확성(10)&효율성(7) 중 정확성만 정답.

def solution(board, skill):
    for sk in skill:
        type, r1, c1, r2, c2, degree = sk

        type = 1 if type == 2 else -1

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                board[r][c] += (type * degree)

    cnt = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] > 0:
                cnt += 1

    return cnt