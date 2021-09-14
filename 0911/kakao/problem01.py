# 게시판 신고. 정답

def solution(id_list, report, k):
    report_dict = dict()
    id_dict = dict()
    for report_tmp in report:
        id, rep = report_tmp.split()

        if id in id_dict:
            id_dict[id].add(rep)
        else:
            id_dict[id] = set()
            id_dict[id].add(rep)

        if rep in report_dict:
            report_dict[rep].add(id)
        else:
            report_dict[rep] = set()
            report_dict[rep].add(id)

    answer = []
    for id in id_list:
        cnt = 0
        if id in id_dict:
            for rep in id_dict[id]:
                if len(report_dict.get(rep, 0)) >= k:
                    cnt += 1
        answer.append(cnt)

    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    print(solution(id_list, report, k))