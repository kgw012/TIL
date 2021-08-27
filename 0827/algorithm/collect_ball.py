# 정올 3427 '볼 모으기'

N = int(input())
balls = input()

cnt_list = []

parse_ball = balls.lstrip('R')
cnt_list.append(parse_ball.count('R'))
parse_ball = balls.lstrip('B')
cnt_list.append(parse_ball.count('B'))
parse_ball = balls.rstrip('R')
cnt_list.append(parse_ball.count('R'))
parse_ball = balls.rstrip('B')
cnt_list.append(parse_ball.count('B'))

print(min(cnt_list))
