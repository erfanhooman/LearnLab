class Node:
    """A node in the singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Singly Linked List implementation."""
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

    def reverse(self):
        """Reverse the singly linked list."""
        prev = None
        current = self.head

        while current:
            next_node = current.next  # Save the next node
            current.next = prev      # Reverse the current node's pointer
            prev = current           # Move prev to the current node
            current = next_node      # Move to the next node

        self.head = prev  # Update the head to the new front of the list
