# Module providing an implementation for queue, using doubly-linked lists to store the elements.
import sys

sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/my_package"
)

from linked_lists.doubly_linked_list import DoublyLinkedList 

class Queue:
    def __init__(self):
        self._data = DoublyLinkedList()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)


    def is_empty(self):
        return self._data.is_empty()

    def enqueue(self, value):
        self._data.insert_to_back(value)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        return self._data.delete_from_front()

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print(queue.dequeue())
    print(queue)
    print(len(queue))