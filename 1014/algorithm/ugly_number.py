# swea 13153 'ugly number'

import heapq

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        num_list = list(map(int, input().split()))

        res_list = [0] * 1500

        min_heap = [1]
        idx = 0
        prev = -1

        while idx < 1500:
            num = heapq.heappop(min_heap)
            if num == prev:
                continue
            
            heapq.heappush(min_heap, num * 2)
            heapq.heappush(min_heap, num * 3)
            heapq.heappush(min_heap, num * 5)

            prev = num
            res_list[idx] = num
            idx += 1
        
        print(f'#{t}', end=' ')
        
        for i in range(N):
            num_list[i] = res_list[num_list[i] - 1]
        
        print(*num_list)
