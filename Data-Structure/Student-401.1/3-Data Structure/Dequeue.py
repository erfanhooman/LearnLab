
# front <- [1, 2, 3, 4, 5] -> back

class DoubleEndedQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0

    def push_back(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.Q[(self.num + self.first) % self.max_size] = item
        print("Push_back at index:", (self.num + self.first) % self.max_size)
        self.num += 1

    def push_front(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.first = (self.first - 1) % self.max_size
        print("Push_front at index:", self.first)
        self.Q[self.first] = item
        self.num += 1

    def pop_front(self):
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

    def pop_back(self):
        if self.num == 0:
            raise Exception("Queue empty")
        self.num -= 1
        return self.Q[(self.num + self.first) % self.max_size]

    def back(self):  # New
        if self.num == 0:
            raise Exception("Queue empty")
        return self.Q[(self.num + self.first - 1) % self.max_size]

    def is_empty(self):
        return self.num == 0

    def size(self):
        return self.num

    def is_full(self):
        return self.num >= self.max_size

