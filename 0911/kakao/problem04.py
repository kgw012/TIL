# 양궁대회. 정답

def calc_point(info, l_info):
    point = 0
    l_point = 0
    for i in range(11):
        if l_info[i] > info[i]:
            l_point += (10 - i)
        elif l_info[i] == 0 and info[i] == 0:
            continue
        else:
            point += (10 - i)

    return l_point - point


def dfs(val_dict):
    n = val_dict['n']
    idx = val_dict['idx']
    cnt = val_dict['cnt']
    info = val_dict['info']
    l_info = val_dict['l_info']

    if cnt >= n or idx >= 11:
        max_point = val_dict['max_point']
        max_l_info = val_dict['max_l_info']
        point = calc_point(info, l_info)
        if max_point == point:
            if len(max_l_info) <= 1:
                return
            for i in range(10, -1, -1):
                if l_info[i] < max_l_info[i]:
                    return
                elif l_info[i] > max_l_info[i]:
                    break
        if max_point <= point:
            val_dict['max_point'] = point
            val_dict['max_l_info'] = l_info.copy()

        return

    for i in range(idx, 10):
        if info[i] >= (n - cnt):
            continue

        val_dict['idx'] = i + 1

        val_dict['cnt'] += (info[i] + 1)
        val_dict['l_info'][i] = info[i] + 1
        dfs(val_dict)
        val_dict['cnt'] -= (info[i] + 1)
        val_dict['l_info'][i] = 0
        dfs(val_dict)

    val_dict['idx'] = 11
    val_dict['cnt'] = n
    val_dict['l_info'][10] = n - cnt
    dfs(val_dict)
    val_dict['idx'] = 10
    val_dict['cnt'] = cnt
    val_dict['l_info'][10] = 0
    return


def solution(n, info):
    max_point = 0
    l_info = [0 for _ in range(11)]
    max_l_info = [-1]

    val_dict = {
        'n': n,
        'info': info,
        'l_info': l_info,
        'max_point': max_point,
        'max_l_info': max_l_info,
        'cnt': 0,
        'idx': 0,
    }
    dfs(val_dict)

    return val_dict['max_l_info']


if __name__ == '__main__':
    n = 10
    info = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    print(solution(n, info))