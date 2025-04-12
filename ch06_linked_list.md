---
marp: true
theme: default
class: invert
size: 16:9
paginate: true
footer: 國立陽明交通大學 電子與光子學士學位學程
headingDivider: 1
style: |
  section::after {
    content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
  }
  
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .columns img {
    width: 100%;
  }

  .red-text {
    color: red;
  }
  
  .blue-text {
    color: lightskyblue;  
  }

  .small-text {
    font-size: 0.50rem;
  }
---
# Chapter 6: Linked List
- What linked list can do better than array
- Types of linked list
  - Singly linked list
  - Sorted linked list
  - Doubly linked list

# What is a Linked List
A **linked list** is made of nodes
- Each node contains a single value 
- Each node also contains a link to the next node
  - Because the nodes are not in contiguous areas of memory
  - Need an extra piece of data to store the memory location of the next node
<div class="columns">
    <img src="restricted/linked_list.png">
    <img src="restricted/linked_list_node.png">
</div>

#  Linked List vs Array
- Elements of array are stored in contiguous memory 
- Nodes of linked list are not stored contiguously. The location of each linked node must be saved.
- A node in a linked node is a small data structure that stores a single value and a link to the next node.
![bg right:50% w:90%](restricted/linked_list_vs_array.png)

# Compare Linked List to Array
- More flexibility: not need allocate space in advance and no data copying cost when add elements
- Lack direct indexing
  - find an element in array: O(1)
  - find an element in linked list: O(n)
![bg right:50% w:90%](restricted/linked_list_vs_array.png)

# Singly Linked List (SLL)
<div class="columns">
    <img src="restricted/linked_list_singly.png">
    <img src="restricted/linked_list_singly_example.png">
</div>

- Head node
  - First element of a linked list, no other node points to it
  - Use a variable point to the head node
- Tail node
  - Last element of the list, not point to next node, point to Null
- Each node only knows its successor

# Requirements of Singly Linked List
<div class="columns">
    <img src="restricted/linked_list_implementation.png">
    <img src="restricted/linked_list_node_implementation.png">
</div>

# Implement Node Class
```python
class Node:
    def __init__(self, data, next_node = None):
        self._data = data
        self._next = next_node

    def data(self): # Return the data of the current node
        return self.?????

    def next(self): # Return the successor of the current node
        return self.?????

    def has_next(self): # Check if the node has a successor
        return self._next ?? ??? None

    def append(self, next_node): # Append next_node to the current node or None to indicate no successor.
        self._next = ?????????

    def __str__(self):
        return str(self.data())

    def __repr__(self):
        return f"Node(value: {repr(self._data)}, {id(self)}, next: {id(self._next) if self._next else None})"        
```

# Design Singly Linked List
- Do not need specify a initial size
- Do not need same data type
- Insert
  - Insert at the end of the list
  - Insert in front
- Search
- Delete
  - Delete by value
  - Delete from the front

# Design Singly Linked List - Insert
<div class="columns">
    <img src="restricted/linked_list_insert_at_the_end.png">
    <img src="restricted/linked_list_insert_in_front.png">
</div>

# Implement Singly Linked List - Insert
```python
import sys
sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/my_package")

from linked_list.singly_linked_node import ????

class SinglyLinkedList:
    def __init__(self):
        # _head: The head node of the list. Initialized to None.
        self._head = None

    def insert_to_back(self, data): # Append a node to the end of the list.
        current = self._head
            if current is None: # empty single linked list
                self._head = ????(????)
            else:
                while current.????() is not None:
                    current = current.next()
                current.append(????(????))

    def insert_in_front(self, data): # Add a node in front.
        old_head = self.?????
        self._head = Node(data, ????????)
```

# Implement Singly Linked List - Helper Function
```python
    def traverse(self, functor):
        # Traverse the linked list to put data into a list after applying functor to each node's data.
        current = self._head
        result = []
        while current is not None:
            result.append(functor(current.data()))
            current = current.next()
        return result
    def __len__(self):  # Return the length of the linked list.
        return ???(self.traverse(lambda x: x))
    def __repr__(self):
        return f'SinglyLinkedList({"->".join(self.traverse(repr))})'
    def __str__(self):
        return "->".join(self.traverse(str))
    def size(self):  # Return the length of the linked list.
        size = 0
        current = self.?????
        while current is not None:
            size += 1
            current = current.????()
        return ????
    def is_empty(self):
        return self._head is ????
```

# Design Singly Linked List - Search
<div class="columns">
    <img src="restricted/linked_list_search.png">
</div>
Time complexity O(n)

# Implement Singly Linked List - Search
```python
    def search(self, target):
        current = self._head
        while current is not None:
            if current.data() ?? target:
                return ???????
            current = current.????()
        return ????
```
# Design Singly Linked List - Delete
<div class="columns">
    <img src="restricted/linked_list_delete_1.png">
    <img src="restricted/linked_list_delete_2.png">
</div>
What is the time complexity?

# Implement Singly Linked List - Delete
```python
    def delete(self, target):
    # Delete the first node with the given data from the list.
        current = self.?????
        previous = ????
        while current is not None:
            if current.data() == target:
                if previous is None:
                    self._head = current.next()
                else:
                    ????????.append(???????.????())
                return
            previous = current
            current = current.next()
        raise ValueError(f"No element with value {target} was found.")
        # If get here, no found
```

# Sorted Linked List
<div class="columns">
    <img src="restricted/linked_list_sorted.png">
</div>

Traverse the list to find the right place to insert the new value
- Find the node after which the new value should be added
- Update the links in the list to include the node that stores the new value

# Implement Sorted Linked List
```python
def insert(self, new_data):
        # Insert a new value into the sorted singly linked list.
        current = self._head
        previous = None
        while current is not None:
            if current.data() ?? new_data:
                if previous is None:
                    self._head = Node(new_data, ???????)    # Add the element at the beginning of the list
                else:
                    ????????.append(Node(new_data, ???????))    # General case
                return
            previous = ???????
            current = current.????()
        if previous is None:
            self._head = Node(new_data)    # The list is ?????
        else:
            previous.append(Node(new_data, None))    # Add the element at the ??? of the list
```
# Doubly Linked List (DLL)
<div class="columns">
    <img src="restricted/linked_list_singly_example_2.png">
    <img src="restricted/linked_list_doubly_example.png">
</div>

- If we have a link to a single node of the list, we can reach any other node in the
list, both before and after it.
- Weak points
  - Each node of a DLL takes up more space than SLL.
  - Each node insertion or deletion action, we need update two links.

# Doubly Linked Node
<div class="columns">
    <img src="restricted/double_linked_list_node.png">
</div>

# Implement Doubly Linked Node
```python
class DoublyLinkedNode:
    def __init__(self, data):
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
        self._next = ?????????
        if next_node is not None:
            next_node.????? = self

    def prev(self):  # return the predecessor of the current node.
        return self._prev

    def has_prev(self):  # check if the node has a predecessor
        return self._prev is not None

    def prepend(self, prev_node):  # prepend a node to the current one.
        self.????? = prev_node
        if prev_node is not None:
            prev_node._next = ????
```

# Design Doubly Linked List - Insert
<div class="columns">
    <img src="restricted/double_linked_list_insert_at_front.png">
    <img src="restricted/double_linked_list_insert_at_end.png">
    <img src="restricted/double_linked_list_insert_in_middle.png">
</div>

# Implement Doubly Linked List - Insert
```python
import sys
sys.path.append("/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/my_package")
from linked_list.doubly_linked_node import DoublyLinkedNode

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def insert_in_front(self, data):
        if self._head is None: # empty list
            self._tail = self._head = DoublyLinkedNode(data)
        else:
            old_head = self.?????
            self._head = DoublyLinkedNode(data)
            self._head.append(????????)

    def insert_to_back(self, data):
        if self._tail is None:
            self._tail = self._head = DoublyLinkedNode(data)
        else:
            old_tail = self.?????
            self._tail = DoublyLinkedNode(data)
            self._tail.prepend(????????)

    def insert_in_middle(self, data, index):
        pass # Homework       
```

# Implement Doubly Linked List - Delete
```python
    def delete(self, target):
        node = self.search(target)
        if node is None:
            raise ValueError(f"No element with value {target} was found")
        if node.prev() is None:  # Delete node from front
            self._head = node.next()
            if self._head is None:  # only one element in the list
                self.????? = None
            else:
                self._head.prepend(????)
        elif node.next() is None:  # Delete node from back
            self._tail = node.????()
            self._tail.append(None)
        else:
            node.prev().append(node.next())
    
    def delete_from_front(self):
        if self.is_empty():
            raise ValueError("Delete on an empty list.")
        data = self._head.data()
        self._head = self._head.????()
        if self._head is ????:
            self._tail = None
        else:
            self._head.prepend(????)
        return data
    
    def delete_from_back(self):
        if self.is_empty():
            raise ValueError("Delete on an empty list.")
        data = self._tail.data()
        self._tail = self._tail.????()
        if self._tail is None:
            self._head = None
        else:
            self._tail.??????(None)
        return data
```


# Homework
DSA HW (F)
