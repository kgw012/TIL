# swea 1970 '쉬운 거스름돈'

if __name__ == '__main__':
    T = int(input())

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for t in range(1, T + 1):
        N = int(input())
        changes = [0] * 8
        
        for i in range(8):
            if N >= money[i]:
                changes[i] += N // money[i]
                N %= money[i]
        
        print(f'#{t}')
        print(*changes)