# 백준 1916 '최소비용 구하기'
# https://www.acmicpc.net/problem/1916

from sys import stdin
import heapq

if __name__ == '__main__':
    N = int(stdin.readline())
    M = int(stdin.readline())

    dist = dict()

    INF = 21e8
    w_list = [INF] * (N + 1)

    for _ in range(M):
        n1, n2, w = map(int, stdin.readline().split())
        dist[n1] = dist.get(n1, [])
        dist[n1].append((n2, w))
    
    U, V = map(int, stdin.readline().split())

    w = 0
    min_heap = [(w, U)]
    while min_heap:
        w, n = heapq.heappop(min_heap)
        if n == V:
            break

        for n_n, n_w in dist.get(n, []):
            if n_w + w >= w_list[n_n]:
                continue

            heapq.heappush(min_heap, (w + n_w, n_n))
            w_list[n_n] = w + n_w
        
    print(w)
