def calcDistance(num, ptr):
    num -= 1
    ptr -= 1

    num_i = int(num / 3)
    num_j = int(num % 3)
    ptr_i = int(ptr / 3)
    ptr_j = int(ptr % 3)
    
    distance = abs(num_i - ptr_i) + abs(num_j - ptr_j)
    return distance

def solution(numbers, hand):

    l_ptr = 10
    r_ptr = 12

    answer = ''
    for num in numbers:
        if(num == 0):
            num = 11

        if (num - 1) % 3 == 0:
            l_ptr = num
            answer += 'L'
        elif (num - 2) % 3 == 0:
            l_dis = calcDistance(num, l_ptr)
            r_dis = calcDistance(num, r_ptr)
            if(l_dis > r_dis):
                r_ptr = num
                answer += 'R'
            elif(l_dis < r_dis):
                l_ptr = num
                answer += 'L'
            else:
                if(hand == 'right'):
                    r_ptr = num
                    answer += 'R'
                else:
                    l_ptr = num
                    answer += 'L'
        else:
            r_ptr = num
            answer += 'R'

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
result = "LRLLLRLLRRL"

print(solution(numbers, hand))