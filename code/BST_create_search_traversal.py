"""
[7, 5, 9, 10, 6, 8, 3]
           7
         /    \
        5      9
     /    \   /   \
    3     6   8    10
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


def search_node(node, value):
    if node is None:
        return f"{value} not found"
    if node.value == value:
        return f"{value} found"
    elif value < node.value:
        return search_node(node.left, value)
    else:
        return search_node(node.right, value)


def dfs_pre_order(node):
    if node is None:
        return
    print(node.value, end=" ")
    dfs_pre_order(node.left)
    dfs_pre_order(node.right)


def dfs_in_order(node):
    if node is None:
        return
    dfs_in_order(node.left)
    print(node.value, end=" ")
    dfs_in_order(node.right)


def dfs_post_order(node):
    if node is None:
        return
    dfs_post_order(node.left)
    dfs_post_order(node.right)
    print(node.value, end=" ")


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


root = TreeNode(7)
insert_node(root, 5)
insert_node(root, 9)
insert_node(root, 10)
insert_node(root, 6)
insert_node(root, 8)
insert_node(root, 3)


print("DFS: pre-order traversal", end=" ")
dfs_pre_order(root)  # 7 5 3 6 9 8 10
print()

print("DFS: in-order traversal", end=" ")
dfs_in_order(root)  # 3 5 6 7 8 9 10
print()

print("DFS: post-order traversal", end=" ")
dfs_post_order(root)  # 3 6 5 8 10 9 7
print()

print("BFS: level order traversal", bfs(root))  # [7, 5, 9, 3, 6, 8, 10]
print()

print(search_node(root, 8))
print(search_node(root, 1))
