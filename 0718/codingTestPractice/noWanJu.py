def solution(participant, completion):
    dic = {}
    for name in participant:
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1
    
    for name in completion:
        dic[name] -= 1
        if dic[name] == 0:
            del dic[name]
    
    answer = list(dic.keys())[0]
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))