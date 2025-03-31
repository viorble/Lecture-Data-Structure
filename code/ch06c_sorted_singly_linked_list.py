import sys

sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/my_package")

from linked_list.singly_linked_list import SinglyLinkedList
from linked_list.singly_linked_node import Node

class SortedSinglyLinkedList(SinglyLinkedList):
    #A sorted version of the singly-linked lists.

    def insert_in_front(self, data):
        raise NotImplementedError('This method is not available for sorted lists')

    def insert_to_back(self, data):
        raise NotImplementedError('This method is not available for sorted lists')

    def insert(self, new_data):
        # Insert a new value into the sorted singly linked list.
        current = self._head
        previous = None
        while current is not None:
            if current.data() >= new_data:
                if previous is None:
                    self._head = Node(new_data, current)    # Add the element at the beginning of the list
                else:
                    previous.append(Node(new_data, current))    # General case
                return
            previous = current
            current = current.next()
        if previous is None:
            self._head = Node(new_data)    # The list is empty
        else:
            previous.append(Node(new_data, None))    # Add the element at the end of the list

if __name__ == "__main__":
    # Test the SortedSinglyLinkedList class
    foo = SortedSinglyLinkedList()
    foo.insert(3)
    foo.insert(1)
    foo.insert(2)
    print(foo)  # Expected output: 1->2->3          
