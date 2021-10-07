# swea 13115 '이진 탐색'

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N, M = map(int, input().split())

        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))

        a_list.sort()

        answer = 0

        for b_num in b_list:
            l = 0
            r = N - 1
            m = (l + r) // 2

            flag = b_num < a_list[m]

            while l <= r:
                m = (l + r) // 2

                if b_num == a_list[m]:
                    answer += 1
                    break

                if b_num < a_list[m]:
                    if not flag:
                        break
                    
                    flag = False
                    r = m - 1
                else:
                    if flag:
                        break
                    
                    flag = True
                    l = m + 1
        
        print(f'#{t} {answer}')
