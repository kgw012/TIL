# swea 4366 '정식이의 은행업무'

def parse_num10(num, N):
    num_10 = 0

    for i in range(len(num)):
        num_10 += int(num[i]) * (N ** (len(num) - i - 1))
    
    return num_10


def find(num2, num3):
    num2_10 = parse_num10(num2, 2)
    
    num2_set = set()
    for i in range(len(num2)):
        num2_set.add(num2_10 ^ (1<<i))
    
    num3_list = list(num3)
    num3_check = ['0', '1', '2']

    for i in range(len(num3_list)):
        save_num = num3_list[i]
        for c in num3_check:
            if num3_list[i] == c:
                continue

            num3_list[i] = c
            num3_10 = parse_num10(num3_list, 3)
            if num3_10 in num2_set:
                return num3_10
            num3_list[i] = save_num
    
    return -1


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        num2 = input()
        num3 = input()

        num = find(num2, num3)

        print(f'#{t} {num}')
