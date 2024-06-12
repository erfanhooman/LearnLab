class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            current = self.head.prev
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if not self.head:
            print("Empty list")
            return None

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    def reverse(self):
        if not self.head:
            return

        current = self.head
        while True:
            current.next, current.prev = current.prev, current.next
            current = current.prev
            if current == self.head:
                break
