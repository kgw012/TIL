from _apis import start, get_waiting_line, get_game_result, get_user_info, put_match, change_grade, get_score


# 최고 점수를 낸 실행파일은 아니지만, 버그가 있던 부분을 수정한 파일입니다.

def parse_user_info(user_info):
    '''
    list인 user_info를 'key=id, value=grade' 형태의 dict로 변환하는 함수
    '''

    info_dict = dict()
    for info in user_info:
        info_dict[int(info['id'])] = int(info['grade'])
    
    return info_dict


def calc_grade_gap(user_info, user1, user2):
    '''
    두 user 사이의 grade_gap을 계산하는 함수
    '''
    user1_grade = user_info[user1['id']]
    user2_grade = user_info[user2['id']]
    return abs(user1_grade - user2_grade)


def put_initial_grade(AUTH_KEY, initial_grade):
    '''
    맨 처음 모든 user들의 grade를 initial_grade로 시작하도록 하는 함수
    '''
    
    user_info = get_user_info(AUTH_KEY)
    commands = []
    for info in user_info:
        command = {
            'id': info['id'],
            'grade': initial_grade,
        }
        commands.append(command)
    
    res = change_grade(AUTH_KEY, commands)
    return res


def grade_strategy(AUTH_KEY, game_result, GRADE_GAP_WEIGHT, MIN_GRADE_GAP):
    '''
    게임 결과를 이용하여 등급 변화를 주는 함수.
    전략 1) 승자에게는 grade_gap만큼 등급이 오르고, 패자에게는 같은 값만큼 등급이 떨어진다.
    전략 2) 게임에 걸린 시간이 길 수록 grade_gap은 작어진다.(가중치로 GRADE_GAP_WEIGHT 이용)
    전략 3) grade_gap은 MIN_GRADE_GAP보다 작아질 수 없다.
    '''

    user_info = parse_user_info(get_user_info(AUTH_KEY))

    commands = []

    for result in game_result:
        win_id = int(result['win'])
        lose_id = int(result['lose'])
        time = int(result['taken'])

        # 게임에 걸린 시간을 점수 변화량에 반영하는 계산식(GRADE_GAP_WEIGHT 가중치 이용)
        grade_gap = max((40 - time) * GRADE_GAP_WEIGHT // 35, MIN_GRADE_GAP)

        # print(f'grade_gap  : {grade_gap}')

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

    res = change_grade(AUTH_KEY, commands)
    return res


def match_strategy(AUTH_KEY, waiting_users, time, TIME_LIMIT, GRADE_GAP_LIMIT):
    '''
    대기중인 유저 목록을 받아 매칭시켜 주는 함수.
    전략 1) 유저는 TIME_LIMIT을 초과하여 대기하지 않는다.
    전략 2-1) 유저의 대기시간이 TIME_LIMIT 이내일 때 :
        현재 대기중인 유저들 중 가장 grade_gap이 작은 유저가 GRADE_GAP_LIMIT 내에 있다면 매칭시킨다.
    전략 2-2) 유저의 대기시간이 TIME_LIMIT을 초과했을 때 :
        현재 대기중인 유저들 중 가장 grade_gap이 작은 유저와 매칭한다.
    '''

    user_info = parse_user_info(get_user_info(AUTH_KEY))

    waiting_users.sort(key=lambda x: x['from'])         # 대기중인 유저들을 가장 먼저 대기한 순서대로 정렬
    pairs = []
    visits = set()      # 이미 pair에 등록된 idx를 저장해놓는 set

    for idx1, user1 in enumerate(waiting_users):
        if idx1 in visits:
            continue

        # user1에 대해 가장 grade_gap이 작은 유저 찾기
        min_gap = 10000
        min_idx = -1
        min_user_id = -1

        for idx2 in range(idx1 + 1, len(waiting_users)):
            if idx2 in visits:
                continue
            
            user2 = waiting_users[idx2]
            grade_gap = calc_grade_gap(user_info, user1, user2)

            if grade_gap < min_gap:
                min_gap = grade_gap
                min_idx = idx2
                min_user_id = user2['id']
        
        # user1의 대기시간이 TIME_LIMIT 이내일 때
        if time - user1['from'] <= TIME_LIMIT:
            # user2와의 grade_gap이 MIN_GRADE_GAP 이내인지 확인
            if min_gap <= MIN_GRADE_GAP:
                visits.add(min_idx)
                pair = [user1['id'], min_user_id]
                pairs.append(pair)

        # user1의 대기시간이 TIME_LIMIT를 초과할 때
        else:
            visits.add(min_idx)
            pair = [user1['id'], min_user_id]
            pairs.append(pair)
    
    res = put_match(AUTH_KEY, pairs)
    print(res)
    return res


if __name__ == '__main__':
    SCENARIO = 1            # 시나리오 번호
    INITIAL_GRADE = 4000    # 맨 처음 초기화할 grade

    GRADE_GAP_WEIGHT = 800  # 게임결과 반영에 사용할 등급 차이에 대한 가중치
    MIN_GRADE_GAP = 150     # 게임결과 반영에 사용할 최소 등급변화량
    
    TIME_LIMIT = 2          # 매칭에 사용할 최대 대기시간
    GRADE_GAP_LIMIT = 1000  # 매칭에 사용할 최대 등급차이

    TOKEN = ''
    AUTH_KEY = start(TOKEN, SCENARIO)['auth_key']
    print(AUTH_KEY)

    # 초기 등급 설정
    put_initial_grade(AUTH_KEY, INITIAL_GRADE)

    for time in range(596):
        game_result = get_game_result(AUTH_KEY)
        grade_strategy(AUTH_KEY, game_result, GRADE_GAP_WEIGHT, MIN_GRADE_GAP)          # 게임 결과를 이용하여 유저들의 점수를 반영

        waiting_users = get_waiting_line(AUTH_KEY)
        match_strategy(AUTH_KEY, waiting_users, time, TIME_LIMIT, GRADE_GAP_LIMIT)      # 대기 중인 유저들을 매칭

    print(get_score(AUTH_KEY))      # 점수 출력
