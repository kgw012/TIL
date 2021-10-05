# swea 13071 '화물 도크'

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        arr = []
        for _ in range(N):
            arr.append(tuple(map(int, input().split())))
        
        arr.sort(key=lambda x: (x[1], x[0]))

        answer = 0
        time = 0

        for i in range(N):
            if time <= arr[i][0]:
                time = arr[i][1]
                answer += 1
        
        print(f'#{t} {answer}')