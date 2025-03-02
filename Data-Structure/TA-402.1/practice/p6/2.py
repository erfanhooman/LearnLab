# Python program to check if a tree is BST

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# Function to find max value in the subtree
def maxValue(node):
    if node is None:
        return float('-inf')
    return max(node.data, maxValue(node.left), maxValue(node.right))


# Function to find min value in the subtree
def minValue(node):
    if node is None:
        return float('inf')
    return min(node.data, minValue(node.left), minValue(node.right))


# Returns true if the binary tree is a BST
def isBST(node):
    if node is None:
        return True

    # Check if the max of the left subtree is greater than current node
    if node.left and maxValue(node.left) >= node.data:
        return False

    # Check if the min of the right subtree is smaller than
    # or equal to current node
    if node.right and minValue(node.right) <= node.data:
        return False

    # Recursively check if left and right subtrees are BSTs
    return isBST(node.left) and isBST(node.right)


if __name__ == "__main__":

    # Create a sample binary tree
    #      4
    #    /   \
    #   2     5
    #  / \
    # 1   3

    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    if isBST(root):
        print("True")
    else:
        print("False")