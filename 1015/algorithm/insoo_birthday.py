# swea 1795 '인수의 생일 파티'

import heapq

if __name__ == '__main__':
    T = int(input())

    INF = 21e8

    for t in range(1, T + 1):
        N, M, X = map(int, input().split())
        e_dict = dict()

        for _ in range(M):
            x, y, c = map(int, input().split())
            e_dict[x] = e_dict.get(x, [])
            e_dict[x].append((y, c))
        
        x_way = [INF] * (N + 1)
        x_way[X] = 0

        for i in range(1, N + 1):
            if i == X:
                continue
            
            way_list = [INF] * (N + 1)
            c = 0
            node = i
            go_x_heap = [(c, node)]

            while go_x_heap:
                c, node = heapq.heappop(go_x_heap)
                if node == X:
                    x_way[i] = c
                    e_dict[i] = e_dict.get(i, [])
                    e_dict[i].append((X, c))
                    break
                
                for n_node, n_c in e_dict.get(node, []):
                    c2 = c + n_c
                    if c2 >= way_list[n_node]:
                        continue
                
                    way_list[n_node] = c2
                    heapq.heappush(go_x_heap, (c2, n_node))
        
        home_way_list = [INF] * (N + 1)
        home_way_list[X] = 0
        go_home_heap = [(0, X)]
        while go_home_heap:
            c, node = heapq.heappop(go_home_heap)

            for n_node, n_c in e_dict.get(node, []):
                c2 = c + n_c
                if c2 >= home_way_list[n_node]:
                    continue

                home_way_list[n_node] = c2
                heapq.heappush(go_home_heap, (c2, n_node))

        answer = 0
        for i in range(1, N + 1):
            answer = max(answer, x_way[i] + home_way_list[i])
        
        print(f'#{t} {answer}')
            
