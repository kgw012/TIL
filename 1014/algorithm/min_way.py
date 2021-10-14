# 백준 1753 '최단경로'
# https://www.acmicpc.net/problem/1753

from sys import stdin, stdout
import heapq

if __name__ == '__main__':
    V, E = map(int, stdin.readline().split())
    K = int(stdin.readline())
    adj = dict()

    INF = 21e8
    w_list = dict()

    for i in range(1, V + 1):
        w_list[i] = INF

    for _ in range(E):
        u, v, w = map(int, stdin.readline().split())
        adj[u] = adj.get(u, [])
        adj[u].append((v, w))
    
    w_list[K] = 0

    min_heap = []
    heapq.heappush(min_heap, (0, K))

    while min_heap:
        w, node = heapq.heappop(min_heap)
        e_list = adj.get(node, list())

        for n_node, n_w in e_list:
            if w + n_w >= w_list[n_node]:
                continue
            
            heapq.heappush(min_heap, (w + n_w, n_node))
            w_list[n_node] = w + n_w
    
    answer = ''
    for i in range(1, V + 1):
        if w_list[i] == INF:
            answer += 'INF\n'
        else:
            answer += str(w_list[i]) + '\n'
    
    stdout.write(answer)
    stdout.flush()
    stdout.close()
    