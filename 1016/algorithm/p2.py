def dfs(calendar, answer, leave, d, cnt):
    if d >= 30 or cnt >= leave:
        h_max = 0
        h_cnt = 0
        for i in range(30):
            if calendar[i]:
                h_cnt += 1
            else:
                h_max = max(h_max, h_cnt)
                h_cnt = 0
        h_max = max(h_max, h_cnt)
        answer[0] = max(h_max, answer[0])
        return
    
    if calendar[d]:
        dfs(calendar, answer, leave, d + 1, cnt)
        return
    else:
        dfs(calendar, answer, leave, d + 1, cnt)
        calendar[d] = True
        dfs(calendar, answer, leave, d + 1, cnt + 1)
        calendar[d] = False
        return
    

def solution(leave, day, holidays):
    day_dict = {
        'MON': 5,
        'TUE': 4,
        'WED': 3,
        'THU': 2,
        'FRI': 1,
        'SAT': 0,
        'SUN': 6,
    }
    calendar = [False] * 30
    idx = day_dict[day]
    if day == 'SUN':
        calendar[0] = True

    while True:
        calendar[idx] = True
        idx += 1
        if idx >= 30:
            break
        calendar[idx] = True
        idx += 6
        if idx >= 30:
            break
    
    for d in holidays:
        calendar[d - 1] = True
    
    answer = [-1]
    dfs(calendar, answer, leave, 0, 0)
    return answer[0]