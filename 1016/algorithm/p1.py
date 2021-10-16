def solution(registered_list, new_id):
    if new_id not in registered_list:
        return new_id

    registered_dict = dict()
    for id in registered_list:
        idx = 0
        while idx < len(id):
            if ord('0') <= ord(id[idx]) <= ord('9'):
                break
            
            idx += 1

        S = id[:idx]
        N = id[idx:]
        if N:
            n = int(N)
        else:
            n = 0
        
        registered_dict[S] = registered_dict.get(S, set())
        registered_dict[S].add(n)
        

    idx = 0
    while idx < len(new_id):
        if ord('0') <= ord(new_id[idx]) <= ord('9'):
            break
        
        idx += 1

    S = new_id[:idx]
    N = new_id[idx:]
    if N:
        n = int(N)
    else:
        n = 0
    
    N1 = str(n + 1)
    new_id = S + N1
    if S not in registered_dict:
        return new_id
    
    while n in registered_dict[S]:
        n += 1
    N1 = str(n)
    new_id = S + N1
    
    return new_id


if __name__ == '__main__':
    registered_list = ["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"]
    new_id = "cow"

    print(solution(registered_list, new_id))