"""
original tree
           4
         /    \
        2      7
     /    \   /   \
    1     3   6    9
"""

"""
Invert tree.
           4
         /    \
        7      2
     /    \   /   \
    9     6   3    1
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# create a binary tree
root = TreeNode(4)
node2 = TreeNode(2)
node7 = TreeNode(7)
node1 = TreeNode(1)
node3 = TreeNode(3)
node6 = TreeNode(6)
node9 = TreeNode(9)

root.left = node2
root.right = node7
node2.left = node1
node2.right = node3
node7.left = node6
node7.right = node9


# DFS
def invert_tree(node):
    if node is None:
        return

    node.left, node.right = node.right, node.left
    invert_tree(node.left)
    invert_tree(node.right)


def pre_order(node):
    if node is None:
        return
    print(node.value, end=" ")
    pre_order(node.left)
    pre_order(node.right)


print("Original: pre-order traversal")
pre_order(root)  # 4 2 1 3 7 6 9

invert_tree(root)
print("Invert: pre-order traversal")
pre_order(root)  # 4 7 9 6 2 3 1
