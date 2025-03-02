"""
Insertion.py
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def construct_tree(self, in_order, pre_order):
        if not in_order or not pre_order:
            return None

        root_value = pre_order[0]
        root = TreeNode(root_value)

        root_index = in_order.index(root_value)

        root.left = self.construct_tree(in_order[:root_index], pre_order[1:1 + root_index])
        root.right = self.construct_tree(in_order[root_index + 1:], pre_order[1 + root_index:])

        return root

    def post_order_traversal(self, node):
        result = []
        if node:
            result.extend(self.post_order_traversal(node.left))
            result.extend(self.post_order_traversal(node.right))
            result.append(node.value)
        return result

    def print_post_order(self, in_order, pre_order):
        self.root = self.construct_tree(in_order, pre_order)
        post_order_result = self.post_order_traversal(self.root)
        for value in post_order_result:
            print(value, end=" ")


if __name__ == "__main__":
    binary_tree = BinaryTree()
    in_order_example = [4, 2, 5, 1, 3]
    pre_order_example = [1, 2, 4, 5, 3]

    binary_tree.print_post_order(in_order_example, pre_order_example)
