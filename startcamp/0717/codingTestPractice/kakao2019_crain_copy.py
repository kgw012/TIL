def solution(board, moves):
    n = len(board)
    board2 = [[] for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n):
            doll = board[i][j]
            if doll != 0:
                board2[j].append(doll)
    board = board2

    count = 0
    stk = []
    for move in moves:
        move -= 1
        if len(board[move]) == 0:
            continue
        doll = board[move].pop()

        if len(stk) == 0:
            stk.append(doll)
        else:
            if(doll == stk[-1]):
                stk.pop()
                count += 2
            else:
                stk.append(doll)
                
    answer = count
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))