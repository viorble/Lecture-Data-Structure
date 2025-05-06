"""A class modeling the nodes of the binary search tree."""


class Node:
    @staticmethod
    def _node_str(node):
        return str(node) if node is not None else ""

    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def __str__(self):
        left_str = Node._node_str(self._left)
        right_str = Node._node_str(self._right)
        return f"{self._value} ({left_str})({right_str})"

    def __repr__(self):
        left_node_id = id(self._left)
        right_node_id = id(self._right)
        return f"BST Node Address: {id(self)} (left: {left_node_id})(right: {right_node_id})"

    def value(self):
        return self._value

    def left(self):
        return self._left

    def right(self):
        return self._right

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node

    def find_min_in_subtree(self):
        # Return the node with the smallest value in the subtree rooted at the node, and its parent
        parent = None
        node = self
        while node.left() is not None:
            parent = node
            node = node.left()
        return node, parent

    def find_max_in_subtree(self):
        # Return the node with the largest value in the subtree rooted at the node, and its parent.
        parent = None
        node = self
        while node.right() is not None:
            parent = node
            node = node.right()
        return node, parent


if __name__ == "__main__":
    # Test the Node class
    node10 = Node(10)
    node5 = Node(5)
    node15 = Node(15)
    node10.set_left(node5)
    node10.set_right(node15)
    print(node10)
    min_node, min_parent = node10.find_min_in_subtree()
    print("min_node:", min_node)
    print("min_node_parent:", min_parent)
    max_node, max_parent = node10.find_max_in_subtree()
    print("max_node:", max_node)
    print("max_node_parent:", max_parent)
