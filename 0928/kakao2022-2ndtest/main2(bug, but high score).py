from collections import deque

from _apis import start, get_waiting_line, get_game_result, get_user_info, put_match, change_grade, get_score


## 해당 파일은 잘못 코딩한 부분이 있으나(TIME_LIMIT 비교하는 부분), 점수는 이 파일이 더 잘나와서,, 추가로 제출합니다.


def parse_user_info(user_info):
    info_dict = dict()
    for info in user_info:
        info_dict[int(info['id'])] = int(info['grade'])
    
    return info_dict


def put_initial_grade(AUTH_KEY):
    user_info = get_user_info(AUTH_KEY)
    commands = []
    for info in user_info:
        command = {
            'id': info['id'],
            'grade': 4000,
        }
        commands.append(command)
    
    change_grade(AUTH_KEY, commands)
    return


def grade_strategy1(AUTH_KEY, game_result):
    GRADE_GAP_WEIGHT = 800
    MIN_GRADE_GAP = 150

    user_info = parse_user_info(get_user_info(AUTH_KEY))
    commands = []
    for res in game_result:
        win_id = int(res['win'])
        lose_id = int(res['lose'])
        time = int(res['taken'])

        grade_gap = max((40 - time) * GRADE_GAP_WEIGHT // 35, MIN_GRADE_GAP)
        print(f'grade_gap  : {grade_gap}')
        win_command = {
            'id': win_id,
            'grade': min(user_info[win_id] + grade_gap, 9999)
        }
        lose_command = {
            'id': lose_id,
            'grade': max(user_info[lose_id] - grade_gap, 0)
        }
        commands.append(win_command)
        commands.append(lose_command)

    change_grade(AUTH_KEY, commands)
    return


def match_strategy1(AUTH_KEY, waiting_users):
    waiting_users.sort(key=lambda x: x['from'])
    pairs = []

    idx = 0
    que = deque()
    while True:
        if len(que) == 2:
            pair = [que.popleft()['id'], que.popleft()['id']]
            pairs.append(pair)
        
        if idx >= len(waiting_users):
            break
        
        que.append(waiting_users[idx])
        idx += 1

    print(put_match(AUTH_KEY, pairs))
    return


def match_strategy2(AUTH_KEY, waiting_users: list, time):
    TIME_LIMIT = 3
    GRADE_GAP_LIMIT = 1000

    user_info = parse_user_info(get_user_info(AUTH_KEY))
    waiting_users.sort(key=lambda x: x['from'])
    pairs = []
    visits = []
    
    for idx1 in range(len(waiting_users)):
        if idx1 in visits:
            continue

        user1 = waiting_users[idx1]
        user1_id = user1['id']
        user1_from = user1['from']
        user1_grade = user_info[user1_id]

        # TIME_LIMIT 초과 시, 가장 grade gap이 낮은 유저와 매칭
        if user1_from - time > TIME_LIMIT:
            min_gap = 10000
            min_id = -1
            min_idx = -1
            for idx2 in range(idx1 + 1, len(waiting_users)):
                if idx2 in visits:
                    continue

                user2 = waiting_users[idx2]
                user2_id = user2['id']
                user2_from = user2['from']
                user2_grade = user_info[user2_id]
                grade_gap = abs(user1_grade - user2_grade)

                if grade_gap < min_gap:
                    min_id = user2_id
                    min_gap = grade_gap
                    min_idx = idx2

            visits.append(min_idx)
            pair = [user1_id, min_id]
            pairs.append(pair)
            print(pair)
            continue
        
        # grade gap이 GRADE_GAP_LIMIT 안에 들어오는 유저중 gap이 가장 작은 유저와 매칭
        user2_list = []
        for idx2 in range(idx1 + 1, len(waiting_users)):
            if idx2 in visits:
                continue

            user2 = waiting_users[idx2]
            user2_id = user2['id']
            user2_from = user2['from']
            user2_grade = user_info[user2_id]

            grade_gap = abs(user1_grade - user2_grade)

            if grade_gap <= GRADE_GAP_LIMIT:
                user2_list.append((user2_id, grade_gap, idx2))
        
        if user2_list:
            min_gap = 10000
            min_id = -1
            min_idx = -1
            for user2 in user2_list:
                if user2[1] < min_gap:
                    min_gap = user2[1]
                    min_id = user2[0]
                    min_idx = user2[2]
            
            visits.append(min_idx)
            pair = [user1_id, min_id]
            pairs.append(pair)
            
    print(put_match(AUTH_KEY, pairs))
    print(pairs)
    return


if __name__ == '__main__':
    TOKEN = ''
    problem = 1
    AUTH_KEY = start(TOKEN, problem)['auth_key']
    print(AUTH_KEY)

    # 초기 등급 설정
    put_initial_grade(AUTH_KEY)

    for time in range(596):
        game_result = get_game_result(AUTH_KEY)
        grade_strategy1(AUTH_KEY, game_result)

        waiting_users = get_waiting_line(AUTH_KEY)
        match_strategy2(AUTH_KEY, waiting_users, time)

    print(get_score(AUTH_KEY))