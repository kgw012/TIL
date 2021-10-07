def func(lst, level):
    global abc_lst, N, answer
    if level >= N:
        answer += 1
        return

    for c in abc_lst:
        if level >= 2:
            if c == lst[level - 1] and c == lst[level - 2]:
                continue
        
        lst.append(c)
        func(lst, level + 1)
        lst.pop()
    
    return


if __name__ == '__main__':
    abc_lst = ['A', 'B', 'C']
    N = 5

    answer = 0

    func([], 0)

    print(answer)
