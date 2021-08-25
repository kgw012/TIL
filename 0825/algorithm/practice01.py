class Queue:
    def __init__(self, capacity):
        self.que = [0] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0

    def enque(self, item):
        self.que[self.rear] = item
        self.rear += 1
        return

    def deque(self):
        item = self.que[self.front]
        self.front += 1
        return item


if __name__ == '__main__':
    que = Queue(10)

    que.enque(3)
    que.enque(7)
    que.enque(5)

    print(que.deque())
    print(que.deque())