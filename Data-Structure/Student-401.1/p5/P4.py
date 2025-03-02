class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)

        return root

    def find_lowest_common_ancestor(self, root, value1, value2):
        if root is None:
            return None

        if root.key > value1 and root.key > value2:
            return self.find_lowest_common_ancestor(root.left, value1, value2)

        if root.key < value1 and root.key < value2:
            return self.find_lowest_common_ancestor(root.right, value1, value2)

        return root


if __name__ == "__main__":
    binary_tree = BinaryTree()
    values_to_insert = [6, 2, 8, 0, 4, 7, 9, 3, 5]

    for value in values_to_insert:
        binary_tree.root = binary_tree.insert_node(binary_tree.root, value)

    value1_to_find = 2
    value2_to_find = 0

    lowest_common_ancestor_node = binary_tree.find_lowest_common_ancestor(binary_tree.root, value1_to_find,
                                                                          value2_to_find)

    if lowest_common_ancestor_node is not None:
        print("Lowest Common Ancestor of nodes", value1_to_find, "and", value2_to_find, "is",
              lowest_common_ancestor_node.key)
    else:
        print("No Lowest Common Ancestor found.")