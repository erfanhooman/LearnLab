""" Trees """

"""
Tree Declare in Bad Way
"""

vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parent = {
    3: 3,
    9: 3,
    4: 3,
    2: 9,
    10: 4,
    6: 4,
    5: 4,
    7: 6,
    8: 2,
    1: 8
}

children = {}
for vertex in vertices:
    children[vertex] = []

for vertex in vertices:
    if children[parent[vertex]] != vertex:
        children[parent[vertex]].append(vertex)

"""
Tree in LeftMostChildRight
"""


class NodeTree:
    def __init__(self, label):
        self.label = label
        self.parent = None
        self.left_child = None
        self.right_sib = None


class Tree:
    def __init__(self):
        self.root = None

    def assign_root(self, label):
        if self.root is None:
            self.root = NodeTree(label)

    def add_new_node(self, parent, label):
        new_node = NodeTree(label)
        new_node.parent = parent
        if parent.left_child is None:
            parent.left_child = new_node
        else:
            temp = parent.left_child
            while temp.right_sib is not None:
                temp = temp.right_sib
            temp.right_sib = new_node
        return None


def in_order(tree, node):  # left -> root -> right
    order_list = []
    if node is None:
        return order_list

    child = node.left_child
    order_list.extend(tree.in_order(child))  # left subtree
    while child is not None:
        child = child.right_sibling
        order_list.extend(tree.in_order(child))  # right subtree
    order_list.append(node.label)  # root

    return order_list


def post_order(tree, node):  # root -> left -> right
    order_list = []
    if node is None:
        return order_list

    child = node.left_child
    while child is not None:
        order_list.extend(tree.post_order(child))  # left subtree
        child = child.right_sibling  # right subtree

    order_list.append(node.label)  # root

    return order_list


def pre_order(tree, node):
    order_list = []
    if node is None:
        return order_list

    order_list.append(node.label)  # root
    child = node.left_child
    while child is not None:
        order_list.extend(tree.pre_order(child))  # left subtree
        child = child.right_sibling  # right subtree

    order_list.append(node.label)
    order_list.extend(pre_order(tree, node.left.label))
    order_list.extend(pre_order(tree, node.right.label))

    return order_list


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(inorder, preorder):
    if not inorder or not preorder:
        return None

    root_data = preorder.pop(-1)
    root = TreeNode(root_data)
    inorder_index = inorder.index(root_data)

    root.left = build_tree(inorder[:inorder_index], preorder)
    root.right = build_tree(inorder[inorder_index + 1:], preorder)

    return root


def postorder_traversal(root):
    result = []
    if root:
        result.extend(postorder_traversal(root.left))
        result.extend(postorder_traversal(root.right))
        result.append(root.data)
    return result


inorder_sequence = [4, 2, 5, 1, 3]
preorder_sequence = [1, 2, 4, 5, 3]

root_node = build_tree(inorder_sequence, preorder_sequence)
postorder_result = postorder_traversal(root_node)

print("پیمایش Postorder:", postorder_result)
