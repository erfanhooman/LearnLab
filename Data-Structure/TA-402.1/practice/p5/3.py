class Node:
    def __init__(self, value, priority=None):
        self.value = value
        self.priority = priority  # Used only for Priority Queue
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        new_node = Node(value)
        if not self.front:  # If the queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if not self.front:
            raise IndexError("Dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        if not self.front:  # If the queue is now empty
            self.rear = None
        return value

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def display(self):
        """Display the queue elements."""
        current = self.front
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, value, priority):
        """Add an element with its priority."""
        new_node = Node(value, priority)
        if not self.front or self.front.priority > priority:  # Insert at front
            new_node.next = self.front
            self.front = new_node
        else:
            # Traverse to find the right position
            current = self.front
            while current.next and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        """Remove and return the element with the highest priority."""
        if not self.front:
            raise IndexError("Dequeue from an empty priority queue")
        value = self.front.value
        self.front = self.front.next
        return value

    def is_empty(self):
        """Check if the priority queue is empty."""
        return self.front is None

    def display(self):
        """Display the priority queue elements."""
        current = self.front
        while current:
            print(f"({current.value}, priority={current.priority})", end=" -> ")
            current = current.next
        print("None")


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """Add an element to the top of the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Remove and return the top element of the stack."""
        if not self.top:
            raise IndexError("Pop from an empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """Return the top element without removing it."""
        if not self.top:
            raise IndexError("Peek from an empty stack")
        return self.top.value

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def display(self):
        """Display the stack elements."""
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
