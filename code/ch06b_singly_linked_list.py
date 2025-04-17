import sys

sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/my_package"
)

from linked_lists.singly_linked_node import Node


class SinglyLinkedList:
    """
    This class models a singly-linked list data structure and have insertion, deletion, search and traversal functions.
    """

    def __init__(self):  # _head: The head node of the list. Initialized to None.
        self._head = None

    def traverse(self, functor):
        # Traverse the linked list to put data into a list after applying functor to each node's data.
        current = self._head
        result = []
        while current is not None:
            result.append(functor(current.data()))
            current = current.next()
        return result

    def __len__(self):  # Return the length of the linked list.
        return len(self.traverse(lambda x: x))

    def __repr__(self):
        return f'SinglyLinkedList({"->".join(self.traverse(repr))})'

    def __str__(self):
        return "->".join(self.traverse(str))

    def size(self):  # Return the length of the linked list.
        size = 0
        current = self._head
        while current is not None:
            size += 1
            current = current.next()
        return size

    def is_empty(self):
        return self._head is None

    def insert_in_front(self, data):  # Add a node to the beginning of the list.
        old_head = self._head
        self._head = Node(data, old_head)

    def insert_to_back(self, data):  # Append a node to the end of the list.
        current = self._head
        if current is None:
            self._head = Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(Node(data))

    def get(self, index):  # Get the data at the given index.
        pass  # homework

    def search(self, target):
        # Search the list for a node with the data matching `target`.
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None

    def delete(
        self, target
    ):  # Delete the first node with the given data from the list.
        current = self._head
        previous = None
        while current is not None:
            if current.data() == target:
                if previous is None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()
        raise ValueError(
            f"No element with value {target} was found."
        )  # If get here, no found

    def delete_from_front(self):  # Delete the first node
        pass  # homework


if __name__ == "__main__":
    foo = SinglyLinkedList()
    foo.insert_to_back(1)
    foo.insert_to_back(2)
    foo.insert_in_front(0)
    print("STR:", foo, "REPR:", repr(foo))
    print(len(foo), foo.size())
    print(foo.search(0))
    # test empty list deletion
    boo = SinglyLinkedList()
    try:
        boo.delete(0)
    except ValueError as e:
        print(e)
    # test delete first node
    boo = SinglyLinkedList()
    boo.insert_to_back(1)
    boo.insert_to_back(2)
    boo.insert_to_back(3)
    boo.delete(1)
    print(boo)
    # test delete last node
    boo = SinglyLinkedList()
    boo.insert_to_back(1)
    boo.insert_to_back(2)
    boo.insert_to_back(3)
    boo.delete(3)
    print(boo)
    # test delete middle node
    boo = SinglyLinkedList()
    boo.insert_to_back(1)
    boo.insert_to_back(2)
    boo.insert_to_back(3)
    boo.delete(2)
    print(boo)
