# tree.py

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree(self, in_order, pre_order):
        if not in_order or not pre_order:
            return None

        root_value = pre_order.pop(0)
        root = TreeNode(root_value)
        in_order_index = in_order.index(root_value)

        root.left = self.build_tree(in_order[:in_order_index], pre_order)
        root.right = self.build_tree(in_order[in_order_index + 1:], pre_order)

        return root

    def subtree_size(self, root):
        if root is None:
            return 0
        return 1 + self.subtree_size(root.left) + self.subtree_size(root.right)

    def left_child_subtree_size(self, in_order, pre_order):
        self.root = self.build_tree(in_order, pre_order)

        if self.root is not None and self.root.left is not None:
            return self.subtree_size(self.root.left)
        else:
            return 0