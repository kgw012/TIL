#swea 12704 '회전'(전용)

class Queue:
    def __init__(self, lst):
        self.que = lst
        self.capacity = len(lst)
        self.front = 0
        self.rear = 0

    def enque(self, item):
        self.que[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        return

    def deque(self):
        item = self.que[self.front]
        self.front = (self.front + 1) % self.capacity
        return item


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        N, M = map(int, input().split())
        lst = list(map(int, input().split()))

        que = Queue(lst)
        M %= N

        for _ in range(M):
            que.enque(que.deque())

        print('#{} {}'.format(t, que.que[que.front]))
