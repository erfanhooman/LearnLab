class Node:
    """A node in the linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A simple linked list."""
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a node to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        """Display the linked list."""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def find(self, value, start_node=None):
        """
        Find the first node with the given value, starting from a specified node.

        Args:
            value: The value to search for.
            start_node: The node to start searching from (default: head).

        Returns:
            The first node with the given value or None if not found.
        """
        if start_node is None:
            current = self.head
        else:
            current = start_node

        while current:
            if current.value == value:
                return current
            current = current.next

        return None  # Value not found

    def find_node(self, value):
        """Helper method to locate the first occurrence of a node with the given value."""
        return self.find(value)
    