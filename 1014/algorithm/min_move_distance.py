# swea 13165 '최소 이동 거리'

import heapq

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N, E = map(int, input().split())
        
        adj = dict()

        for _ in range(E):
            s, e, w = map(int, input().split())
            adj[s] = adj.get(s, list())
            adj[s].append((e, w))
        
        INF = 21e8
        w_list = [INF] * (N + 1)

        w = 0
        node = 0
        min_heap = [(w, node)]
        while min_heap:
            w, node = heapq.heappop(min_heap)

            if node == N:
                break

            for n_node, n_w in adj.get(node, list()):
                if w + n_w >= w_list[n_node]:
                    continue

                heapq.heappush(min_heap, (w + n_w, n_node))
                w_list[n_node] = w + n_w
        
        print(f'#{t} {w}')
