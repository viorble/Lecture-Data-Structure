"""
           1
         /    \
        3      6
     /    \   /   \
     4    5   7    9
"""

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# create a binary tree
root = TreeNode(1)
node3 = TreeNode(3)
node6 = TreeNode(6)
node4 = TreeNode(4)
node5 = TreeNode(5)
node7 = TreeNode(7)
node9 = TreeNode(9)
root.left = node3
root.right = node6
node3.left = node4
node3.right = node5
node6.left = node7
node6.right = node9

# BFS: level order traversal
queue = deque()
result = []
queue.append(root)
while queue:
    node = queue.popleft()
    result.append(node.value)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)

print(result)
