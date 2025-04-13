# Module providing an implementation for doubly-linked list.
import sys

sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/my_package"
)

from linked_lists.doubly_linked_node import DoublyLinkedNode


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def traverse(self, functor):
        current = self._head
        result = []
        while current is not None:
            result.append(functor(current.data()))
            current = current.next()
        return result

    def __len__(self):
        return len(self.traverse(lambda x: x))

    def __repr__(self):
        return f'DoublyLinkedList({"<->".join(self.traverse(repr))})'

    def __str__(self):
        return "<->".join(self.traverse(str))

    # def __iter__(self):
    #     current = self._head
    #     while current is not None:
    #         data = current.data()
    #         current = current.next()
    #         yield data

    def size(self):
        size = 0
        current = self._head
        while current is not None:
            size += 1
            current = current.next()
        return size

    def is_empty(self):
        return self._head is None

    def insert_in_front(self, data):
        if self._head is None:
            self._tail = self._head = DoublyLinkedNode(data)
        else:
            old_head = self._head
            self._head = DoublyLinkedNode(data)
            self._head.append(old_head)

    def insert_to_back(self, data):
        if self._tail is None:
            self._tail = self._head = DoublyLinkedNode(data)
        else:
            old_tail = self._tail
            self._tail = DoublyLinkedNode(data)
            self._tail.prepend(old_tail)

    def insert_in_middle(self, data, index):
        pass # Homework       

    def get(self, index):
        if index < 0:
            raise IndexError("Index must be non-negative")
        current = self._head
        current_index = 0
        while current_index < index and current is not None:
            current = current.next()
            current_index += 1
        if current is None:
            raise IndexError("Index out of bounds")
        # Here we know that we are at the right index
        return current.data()

    def indexing(self, target):
        # Search the list for a node with the data matching `target`.
        current = self._head
        i = 0
        while current is not None:
            if current.data() == target:
                return (i)
            current = current.next()
            i += 1
        return None
    
    def search(self, target):
        # Search the list for a node with the data matching `target`.
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None

    def delete(self, target):
        node = self.search(target)
        if node is None:
            raise ValueError(f"No element with value {target} was found in the list.")
        if node.prev() is None:
            # Delete node from front
            self._head = node.next()
            if self._head is None:
                # In case the list's head was the only element in the list
                self._tail = None
            else:
                self._head.prepend(None)
        elif node.next() is None:
            # Delete node from back
            self._tail = node.prev()
            # We know tail can't be None, because node.prev() != None
            self._tail.append(None)
        else:
            node.prev().append(node.next())
            # del node

    def delete_from_front(self):
        if self.is_empty():
            raise ValueError("Delete on an empty list.")
        data = self._head.data()
        self._head = self._head.next()
        if self._head is None:
            self._tail = None
        else:
            self._head.prepend(None)
        return data

    def delete_from_back(self):
        if self.is_empty():
            raise ValueError("Delete on an empty list.")
        data = self._tail.data()
        self._tail = self._tail.prev()
        if self._tail is None:
            self._head = None
        else:
            self._tail.append(None)
        return data
    
if __name__ == "__main__":
    foo = DoublyLinkedList()
    foo.insert_in_front(1)
    foo.insert_in_front(2)
    foo.insert_to_back(3)
    foo.insert_to_back(4)
    print(foo)
    print(repr(foo))
    print(len(foo))
    print(foo.size())
    print(foo.is_empty())
    print("index 0:", foo.get(0))
    print("position of value 3:", foo.indexing(3))
    foo.delete(3)
    print("after delete 3:", foo)
    foo.delete_from_front()
    print("after delete from front:", foo)
    foo.delete_from_back()
    print("after delete from back:", foo)