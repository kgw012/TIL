# 주차장 요금 정산. 정답.

import math

def calc_time(in_time, out_time):
    in_h, in_m = map(int, in_time.split(':'))
    out_h, out_m = map(int, out_time.split(':'))

    result = (out_h - in_h) * 60 + (out_m - in_m)
    return result


def calc_fee(fees, time):
    min_time, min_price, per_time, per_price = fees

    if time <= min_time:
        return min_price

    fee = min_price + math.ceil(((time - min_time) / per_time)) * per_price
    return fee


def solution(fees, records):

    car_dict = dict()
    car_list = []
    for record in records:
        time, car, inout = record.split()

        if car not in car_dict:
            car_dict[car] = {
                'time': 0,
                'IN': '',
                'OUT': '',
            }
            car_list.append(car)

        car_dict[car][inout] = time

        if inout == 'OUT':
            car_dict[car]['time'] += calc_time(car_dict[car]['IN'], car_dict[car]['OUT'])
            car_dict[car]['IN'] = ''
            car_dict[car]['OUT'] = ''

    answer = []
    car_list.sort()
    for car in car_list:
        if car_dict[car]['IN']:
            car_dict[car]['OUT'] = '23:59'
            car_dict[car]['time'] += calc_time(car_dict[car]['IN'], car_dict[car]['OUT'])
            car_dict[car]['IN'] = ''
            car_dict[car]['OUT'] = ''

        answer.append(calc_fee(fees, car_dict[car]['time']))

    return answer


if __name__ == '__main__':
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    print(solution(fees, records))