"""
[10, 5, 15, 3, 7, 18]
           10
         /    \
        5      15
     /    \      \
    3     7       18
"""

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# create a binary search tree based on the values [7, 5, 9, 10, 6, 8, 3]


def insert_node(node, value):
    if value < node.value:
        if node.left is None:
            node.left = TreeNode(value)
            print("inserted", value)
        else:
            insert_node(node.left, value)
    else:
        if node.right is None:
            node.right = TreeNode(value)
            print("inserted", value)
        else:
            insert_node(node.right, value)


def bfs(node):
    queue = deque()
    result = []
    queue.append(node)
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


root = TreeNode(10)
insert_node(root, 5)
insert_node(root, 15)
insert_node(root, 3)
insert_node(root, 7)
insert_node(root, 18)

print("BFS: level order traversal", bfs(root))

sum = 0
low = 7
high = 15

if root:
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if low <= node.value <= high:
            sum += node.value
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print("Sum of nodes in the range", low, "and", high, "is", sum)
