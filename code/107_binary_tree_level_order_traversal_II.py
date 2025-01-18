"""
           3
         /    \
        9      20
              /   \
             15    7
"""

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# create a binary tree
root = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

root.left = node9
root.right = node20
node20.left = node15
node20.right = node7


# BFS: level order traversal
def level_order_traversal(root):
    if not root:
        return []

    queue = deque()
    result = []
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if current_level:
            result.append(current_level)

    return list(reversed(result))


print(level_order_traversal(root))
