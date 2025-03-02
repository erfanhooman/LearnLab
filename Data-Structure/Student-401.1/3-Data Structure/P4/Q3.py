class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head
        self.n = 0

    def get(self, ind):
        if ind > self.size() or ind < 1:
            raise Exception('Out of list')
        x = self.head
        for i in range(ind):
            x = x.next
        return x

    def insert_after(self, x, data):
        y = Node(data)
        self.n += 1
        y.prev = x
        y.next = x.next
        x.next = y
        y.next.prev = y
        return y

    def delete(self, x):
        self.n -= 1
        if self.n == 0:
            raise Exception('Linked list is empty')
        x.prev.next = x.next
        x.next.prev = x.prev
        return x

    def find(self, val):
        x = self.head.next
        for i in range(self.size()):
            if x.data == val:
                return x
            x = x.next
        return None

    def size(self):
        return self.n

    def is_empty(self):
        return self.n == 0
