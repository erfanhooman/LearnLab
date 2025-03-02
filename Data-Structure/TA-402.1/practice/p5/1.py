class HistoryStack:
    def __init__(self, size_limit=100):
        self.items = []
        self.size_limit = size_limit

    def push(self, item):
        if len(self.items) >= self.size_limit:
            raise OverflowError("Stack overflow: cannot push more items")
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []
        self.min_stack = []
        self.operation_history = HistoryStack()

    def enqueue(self, value):
        """Add an element to the back of the queue."""
        self.items.append(value)
        self.operation_history.push(({value}, "append"))

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if not self.is_empty():
            removed = self.items.pop(0)
            self.operation_history.push(({removed}, "removed"))

            if removed == self.min_stack[0]:
                self.min_stack.pop(0)

            return removed
        raise IndexError("Dequeue from empty queue")

    def get_smallest(self):
        """Return the smallest element in the queue in O(1) time."""
        if not self.is_empty():
            return self.min_stack[0]
        raise ValueError("Queue is empty, no smallest element")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.items)

    def view_history(self):
        """Return the history of enqueue and dequeue operations."""
        return self.operation_history

    def undo(self):
        """Remove and return the front element of the queue."""
        raise NotImplementedError
