# 1. List의 합 구하기

def list_sum(my_list):
    total = 0

    for num in my_list:
        total += num
    
    return total

print(list_sum([1, 2, 3, 4, 5]))


# 2. Dictionary로 이루어진 List의 합 구하기

def dict_list_sum(my_list):
    sum_age = 0

    for my_dict in my_list:
        sum_age += my_dict['age']
    
    return sum_age


print(dict_list_sum([
    {'name': 'kim', 'age': 12},
    {'name': 'lee', 'age': 4}
]))


# 3. 2차원 List의 전체 합 구하기

def all_list_sum(my_list):
    sum_list = 0

    for inner_list in my_list:
        for num in inner_list:
            sum_list += num

    return sum_list

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))