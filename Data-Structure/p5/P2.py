"""
2.py
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def construct_tree(self, in_order, post_order):
        if not in_order or not post_order:
            return None

        root_value = post_order.pop()
        root = TreeNode(root_value)

        in_order_index = in_order.index(root_value)

        root.right = self.construct_tree(in_order[in_order_index + 1:], post_order)
        root.left = self.construct_tree(in_order[:in_order_index], post_order)

        return root

    def pre_order_traversal(self, root):
        if root is not None:
            print(root.value, end=' ')
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def print_pre_order(self, in_order, post_order):
        self.root = self.construct_tree(in_order, post_order)
        print("Preorder Traversal:")
        self.pre_order_traversal(self.root)


if __name__ == "__main__":
    binary_tree = BinaryTree()
    in_order_example = [4, 2, 5, 1, 3]
    post_order_example = [4, 5, 2, 3, 1]

    binary_tree.print_pre_order(in_order_example, post_order_example)
