class Node:
    """
    A singly linked node. Each node contains data and a reference to the next node.

    Attributes:
        data: The data held in the node. Can be any arbitrary object.
        _next: A reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Parameters:
        - data: The data for the node. Can be any arbitrary object.
        - next_node: The next Node in the list. Defaults to None.
        """
        self._data = data
        self._next = next_node

    def __str__(self):
        return str(self.data())

    def __repr__(self):
        return f"Node(value: {repr(self._data)}, {id(self)}, next: {id(self._next) if self._next else None})"

    def data(self):
        return self._data

    def next(self):
        # Return the successor of the current node.
        return self._next

    def has_next(self):
        # Check if the node has a successor.
        return self._next is not None

    def append(self, next_node):
        """
        Append a node to the current one.
        next_node: The node to append after the current node, or None to indicate no successor.
        """
        self._next = next_node


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.append(node2)
    node2.append(node3)
    print(str(node1))
    print(repr(node1))
    print(repr(node2))
    print(repr(node3))
    print(node1)

    print(node1.data())
    print(repr(node1.next()))
    print(node1.has_next(), node3.has_next())