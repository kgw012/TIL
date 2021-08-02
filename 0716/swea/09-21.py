# -*- coding: utf-8 -*-

# 09-21.py

data_list = list(range(1, 21))
# expr1 = input('항목 x에 적용할 표현식을 입력하세요 : ')
# expr2 = input('항목 x를 필터링할 조건의 표현식을 입력하세요 : ')

expr1 = 'x + 3'
expr2 = 'x % 5 == 0'

map_list = list(map(lambda x: eval(expr1), data_list))
filter_list = list(filter(lambda x: eval(expr2), data_list))

print(f'map 함수의 적용 결과: {map_list}')
print(f'filter 함수의 적용 결과: {filter_list}')