class Node:
    """A node in the circular linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    """Circular Linked List implementation."""
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a node to the circular linked list."""
        new_node = Node(value)
        if not self.head:  # If the list is empty
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        """Display the circular linked list."""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(Back to head)")

    def reverse(self):
        """Reverse the circular linked list."""
        if not self.head or self.head.next == self.head:
            return  # List is empty or has only one node

        prev = None
        current = self.head
        next_node = None

        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

            if current == self.head:
                break

        self.head.next = prev
        self.head = prev
