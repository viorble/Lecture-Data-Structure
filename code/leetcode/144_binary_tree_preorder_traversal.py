"""
           1
            \
             2
            /
           3
"""

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# create a binary tree
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
root.left = None
root.right = node2
node2.left = node3
node2.right = None


# DFS: pre-order traversal
def pre_order(node):
    if node is None:
        return
    result.append(node.value)
    pre_order(node.left)
    pre_order(node.right)
    return result


result = []
print("DFS: pre-order traversal", pre_order(root))
