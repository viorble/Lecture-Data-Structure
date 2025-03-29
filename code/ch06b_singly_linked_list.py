import sys

sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/my_package")

from linked_list.singly_linked_node import Node

class SinglyLinkedList:
    """
    This class models a singly-linked list data structure.

    A singly-linked list consists of nodes where each node has a reference to the next node in the list.

    Functionality:
    - Stores nodes containing arbitrary data.
    - Supports common linked list operations like insertion, deletion, search and traversal.
    """

   # --- SinglyLinkedList methods ---


    def __init__(self):
    # _head: The head node of the list. Initialized to None.

        self._head = None

    def __len__(self):
    # Return the length of the linked list.
        return len(self.traverse(lambda x: x))

    def __repr__(self):
        return f'SinglyLinkedList({"->".join(self.traverse(repr))})'

    def __str__(self):
        """
        Functionality: Traverses the linked list using the traverse() method, passing in repr() to convert each node to a string.
                       Joins the node string representations with '->' and returns the result.
        """
        return '->'.join(self.traverse(str))

    def size(self):
    # Return the length of the linked list.
        size = 0
        current = self._head
        while current is not None:
            size += 1
            current = current.next()
        return size


    def is_empty(self):
        return self._head is None


    def insert_in_front(self, data):
    # Add a node to the beginning of the list.

        old_head = self._head
        self._head = Node(data, old_head)


    def insert_to_back(self, data):
        # Append a node to the end of the list.

        current = self._head
        if current is None:
            self._head = Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(Node(data))


    def get(self, index):
        """
        Get the data at the given index.

        Parameters:
            index (int): The index of the element to retrieve, starting from the head of the list.
        
        Returns:
            Any: A deep copy of the data at the given index if found.
        
        Error Handling:
            Raising an IndexError if index is invalid.
        """
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


    def traverse(self, functor):
        """
        Traverse the linked list and apply a function to each node's data.

        Parameters:
            functor (Callable): The function (or functor) to apply to each node's data.

        Returns:
            List[Any]: A list containing the result of applying the function 
                    to each node's data.
        """

        current = self._head
        result = []
        while current is not None:
            result.append(functor(current.data()))
            current = current.next()
        return result


    def _search(self, target):
        # Search the list for a node with the data matching `target`, and return the node found.
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None

    def search(self, predicate):
        """
        Search the list for the first node whose data matches the predicate function.
        
        Parameters:
            predicate (Callable): The predicate function to evaluate node data against.
                                Should accept a single parameter for the node data.
                                
        Returns:
            Optional[Any]: The first element for which predicate(element) is True, 
                        or None if no match is found.
        """
        current = self._head
        while current is not None:
            if predicate(current.data()):
                return current.data()
            current = current.next()
        return None


    def delete(self, target):
        """
        Delete the first node with the given data from the list.

        Parameters:
            target (Any): The data value to delete from the list.

        Returns:
            None

        Error Handling:
            If no match is found after full traversal, raises a ValueError.
        """

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
        # If it gets here, it hasn't found the target
        raise ValueError(f'No element with value {target} was found in the list.')


    def delete_from_front(self):
        """
        Delete the first node in the list and return the data it held.

        Parameters:
            None

        Returns:
            The data held by the node that was deleted from the front.

        Error Handling:
            If the list is empty, raises a ValueError.
        """

        if self.is_empty():
            raise ValueError('Delete on an empty list.')
        data = self._head.data()
        self._head = self._head.next()
        return data

if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.insert_in_front(1)
    sll.insert_in_front(2)
    sll.insert_to_back(3)
    print(sll)
    print(repr(sll))  # Output: SinglyLinkedList(2->1->3)
    # print('length = ', len(sll))  # Output: 0

    # print(sll)  # Output: 2->1->3
    # print(sll.size())  # Output: 3
    # print(sll.get(1))  # Output: 1
    # sll.delete(1)
    # print(sll)  # Output: 2->3
    # print(sll.search(lambda x: x == 3))  # Output: 3
    # print(sll.traverse(str))  # Output: ['2', '3'] 
    # print(sll.is_empty())  # Output: False
    # sll.delete_from_front()
    # print(sll)  # Output: 3
    # print(sll.size())  # Output: 1 
    # sll.delete(3)
    # print(sll)  # Output: (empty list) 
    # print(sll.is_empty())  # Output: True
    # print(len(sll))  # Output: 0
    # # sll.delete(4)  # Uncommenting this line will raise a ValueError: No element with value 4 was found in the list.
    # # sll.get(0)  # Uncommenting this line will raise a ValueError: Index out of bounds
    # # sll.insert_to_back(4)
    # # print(sll)  # Output: 4 
    # # print(sll.size())  # Output: 1
    # # sll.delete_from_front()  # Output: 4
    # # print(sll)  # Output: (empty list)
    # # print(sll.size())  # Output: 0
    # # print(sll.is_empty())  # Output: True