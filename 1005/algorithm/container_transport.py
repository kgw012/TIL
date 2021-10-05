# swea 13070 '컨테이너 운반'

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N, M = map(int, input().split())
        containers = list(map(int, input().split()))
        trucks = list(map(int, input().split()))

        containers.sort()
        trucks.sort()

        answer = 0

        while containers and trucks:
            if containers[-1] <= trucks[-1]:
                answer += containers.pop()
                trucks.pop()
            else:
                containers.pop()
        
        print(f'#{t} {answer}')
        