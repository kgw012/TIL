# n을 k진수로 바꾸고, 조건에 맞는 소수 구하기. 정답

def parse_k(n, k):
    tmp = ''
    while n:
        num = n % k
        tmp += str(num)
        n //= k

    result = ''
    for i in range(len(tmp)-1, -1, -1):
        result += tmp[i]

    return result


def prime_check(n):
    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    string_list = parse_k(n, k).split('0')
    num_list = []
    for s in string_list:
        if s:
            num_list.append(int(s))
    answer = 0

    for num in num_list:
        if prime_check(num):
            answer += 1

    return answer


if __name__ == '__main__':
    n = 1000000
    k = 3
    print(parse_k(n, k))
    print(solution(n, k))