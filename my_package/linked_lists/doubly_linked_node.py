# Module providing an implementation for doubly-linked node.


class DoublyLinkedNode:
    """
    A node in a doubly linked list. Each node contains data and references to the next and previous nodes in the list.
    Attributes:
        data: The data held in the node. Can be any arbitrary object.
        _next: A reference to the next node in the list.
        _prev: A reference to the previous node in the list.
    """

    def __init__(self, data):
        """
        Initialize a new DoublyLinkedNode object. The links to previous and next nodes are set to None
        Use append and prepend methods to link to other nodes.
        """
        self._data = data
        self._next = None
        self._prev = None

    def __str__(self):
        return str(self.data())

    def __repr__(self):
        return f"DoublyLinkedNode(value:{self._data}, address:{id(self)}, previous:{id(self._prev) if self._prev else None}, next:{id(self._next) if self._next else None})"

    def data(self):
        return self._data

    def next(self):  # return the successor of the current node.
        return self._next

    def has_next(self):
        return self._next is not None

    def append(self, next_node):  # append a node to the current one
        self._next = next_node
        if next_node is not None:
            next_node._prev = self

    def prev(self):  # return the predecessor of the current node.
        return self._prev

    def has_prev(self):  # check if the node has a predecessor
        return self._prev is not None

    def prepend(self, prev_node):  # prepend a node to the current one.
        self._prev = prev_node
        if prev_node is not None:
            prev_node._next = self


if __name__ == "__main__":
    # Example usage of the DoublyLinkedNode class
    node1 = DoublyLinkedNode(1)
    node2 = DoublyLinkedNode(2)
    node3 = DoublyLinkedNode(3)
    print(node1, node2, node3)
    node1.append(node2)  # Link node1 to node2
    node3.prepend(node2)  # Link node3 back to node2
    print(repr(node1), repr(node2), repr(node3), sep="\n")
    print("Node 1 next:", node1.next().data())
    print("Node 2 prev:", node2.prev().data())
    print(f"Node 1, 2, 3 data: {node1.data()}, {node2.data()}, {node3.data()}")
    print(
        node1.has_next(),
        node1.has_prev(),
        node2.has_next(),
        node2.has_prev(),
        node3.has_next(),
        node3.has_prev(),
    )
