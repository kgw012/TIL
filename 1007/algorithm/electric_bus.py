# swea 13118 '전기버스 2'

if __name__ == '__main__':
    T = int(input())
    
    for t in range(1, T + 1):
        input_lst = list(map(int, input().split()))
        N = input_lst[0]
        lst = input_lst[1:]

        idx = 0
        answer = 0

        if lst[0] >= len(lst):
            print(f'#{t} {answer}')
            continue

        while True:
            max_idx = 0
            next_idx = 0

            for i in range(idx + 1, idx + lst[idx] + 1):
                if i + lst[i] > max_idx:
                    max_idx = i + lst[i]
                    next_idx = i
            
            if max_idx >= len(lst):
                answer += 1
                break

            idx = next_idx
            answer += 1
        
        print(f'#{t} {answer}')
        