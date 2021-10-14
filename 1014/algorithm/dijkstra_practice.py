adj = {
    'A' : [(3,'D'), (6,'C')],
    'B' : [(3,'A')],
    'C' : [(2,'D')],
    'D' : [(1,'C'), (1,'B')],
    'E' : [(4,'B'), (2,'D')],
}

import heapq


minheap = []
heapq.heappush(minheap, (0,'A'))

INF = int(21e8)
dist = {'A': INF, 'B' :INF, 'C' : INF, 'D': INF , 'E': INF}

while minheap:
    cost,now =  heapq.heappop(minheap) # 시작 -> now 의 비용 / 거리 탐색
    if dist[now] != INF : continue #결정되어있는경우
    dist[now] = cost #처음 탐색된경우 최소비용이 결정됨

    # next heapq 에 등록
    for w ,next in adj[now]: # A-> now (cost) +  now->next (w)
        heapq.heappush(minheap, (w+cost, next))

de = -1