def solution(board, moves):
    n = len(board[0])
    board2 = [[] for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n):
            if(board[i][j] != 0):
                board2[j].append(board[i][j])
    board = board2
    stk = []
    count = 0
    for num in moves:
        num = num - 1
        if(len(board[num]) == 0): continue
        doll = board[num].pop()
        if(len(stk) > 0):
            top = stk[-1]
            if(doll == top):
                stk.pop()
                count += 2
            else:
                stk.append(doll)
        else:
            stk.append(doll)
    answer = count
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))