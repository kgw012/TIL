# 1. 평균 점수 구하기
def get_dict_avg(score_dict):
    # total = 0

    # for score in score_dict.values():
    #     total += score
    
    # return total / len(score_dict)
    return sum(score_dict.values()) / len(score_dict)

print(get_dict_avg({
    'python': 80,
    'algorithm': 90,
    'django': 89,
    'web': 83,
}))


# 2. 혈액형 분류하기
def count_blood(blood_list):
    # blood_dict = {
    #     'A': 0,
    #     'B': 0,
    #     'O': 0,
    #     'AB': 0,
    # }

    # for blood in blood_list:
    #     blood_dict[blood] += 1
    
    # return blood_dict

    blood_dict = {}

    for blood in blood_list:
        blood_dict[blood] = blood_dict.get(blood, 0) + 1

    return blood_dict

print(count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB'
]))