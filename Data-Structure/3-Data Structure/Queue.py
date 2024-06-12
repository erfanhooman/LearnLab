"""
Queue:
    - FIRST IN FIRST OUT
"""

# -0:5 -1:5 -2: -3: -4: -5: -6:


class _Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0

    def enqueue(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.Q[(self.num + self.first) % self.max_size] = item
        self.num += 1

    def dequeue(self):
        if self.num == 0:
            raise Exception("Queue empty")
        item = self.Q[self.first]
        self.first = (self.first + 1) % self.max_size
        self.num -= 1
        return item

    def front(self):
        if self.num == 0:
            raise Exception("Queue empty")
        return self.Q[self.first]

    def end_Q(self):
        if self.num == 0:
            raise Exception("Queue empty")
        return self.Q[(self.num + self.first - 1) % self.max_size]

    def index(self, idx):
        if idx > self.max_size:
            raise Exception("The IDX is not Available")
        index = self.Q[(self.first + idx - 1) % self.max_size]
        return index

    def first_IDX(self):
        return self.first

    def is_empty(self):
        return self.num == 0

    def size(self):
        return self.num

    def is_full(self):
        return self.num >= self.max_size
