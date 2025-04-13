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

  .middle-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }
  .middle-grid img {
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
# Chapter 8: Queue
![bg right:50% w:90%](../Lecture-Data-Structure/restricted/queue_ice_cream.png)
- **Queue** is a container that allows elements to be added or removed according to FIFO rule (first in, first out).

# Requirements of a Queue
Queue follows FIFO rule, we design its interface with only two methods:
- Enqueue(): insert an element into the queue
- Dequeue(): remove the least recently added element from the queue and return it

<div class="columns">
    <img src="restricted/queue_operations.png">
    <img src="restricted/queue_illustration.png">
</div>

# Consider Data Structures to Implement Queue
- Static array
- Dynamic array (complicated)
- Doubly linked list
- Stack (complicated)
<div class="middle-grid">
    <img src="restricted/queue_static_array.png">
    <img src="restricted/queue_static_array_full.png">
    <img src="restricted/queue_linked_list.png">
</div>

# Design Queue by Static Array
When 'Rear' reaches the end of static array and there are some unused space at the front.
- Move all elements in the queue toward the start of the array. This means an O(n) overhead. It is inefficient.
- Circular queue

<div class="middle-grid">
    <img src="restricted/queue_circular_1.png">
    <img src="restricted/queue_circular_2.png">
    <img src="restricted/queue_circular_3.png">

</div>

# Comparison of Possible Implementations
Alt|Enqueue| Dequeue()| Dynamic size
---|---------|----------|-------------
Static array| O(1)| O(1)| No
Dynamic array| O(n)|O(n)|Yes
Doubly linked list | O(1)| O(1)| Yes

# Implement Queue by Doubly Linked List
```python
class Queue:
    def __init__(self):
        self._data = ????????????????()
    def __len__(self):
        return ???(self._data)
    def __str__(self):
        return str(self._data)
    def is_empty(self):
        return self._data.is_empty()
    def enqueue(self, value):
        self._data.??????????????(value)
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        return self._data.?????????????????()
```

# Implement Queue by Stack Array - Init and Helper
```python
def pop(self):
    if self.is_empty():
        raise ValueError("Cannot pop from an empty stack")
    return self._data.?????????????????()

def peek(self):
    if self.is_empty():
        raise ValueError("Cannot peek at an empty stack")
    return self._data.?????.data()
```

# Theory vs. the Real World
- Considering Big O
  - Stack by SLL: O(1)
  - Stack by Dynamic array: O(n), but if a large number of operations is performed, their amortized (攤銷的) cost can be considered O(1).
- Considering implementation
  - You shouldn’t implement your own library unless it’s absolutely necessary
  - If the library is critical for your application and can become a bottleneck, you should profile it.
  - You shouldn’t profile all your code though. Focus on the critical sections where optimization will improve efficiency the most.

# Profiling Example
- Class Stack in stack.py coded by SLL
- Class StackArray in stack_dynamic_array.py coded by List to simulate dynamic array

<div class="columns">
    <img src="restricted/stack_profiling_1.png">
    <img src="restricted/stack_profiling_2.png">
</div>

- Python provides an optimized, extremely efficient implementation for list. This
code is usually written in C and compiled for use in Python
- With linked lists, we must allocate a new node on each call to push and then
destroy a Node object on each pop. Allocating the memory and creating the
objects takes time.

# Stack Application - Evaluating Expression
- Infix notation: 3 + 2
- Postfix notation: 3 2 +
- In infix notation, 3 + 2 * 4 == 3 + (2 * 4) based on operator precedence, if we want to add 3 and 2 first, the formula will be (3 + 2) * 4
- In postfix notation, we use 3 2 4 * + and 3 2 + 4 * respectively
- 
<div class="columns">
    <img src="restricted/stack_postfix_1.png">
    <img src="restricted/stack_postfix_2.png">
</div>

# Recap
- A stack is a container that abides by the LIFO policy.
- Stacks provide two operations: push and pop. No other way to insert or delete elements, and search is generally not allowed.
- A stack can be implemented using either arrays or linked lists to store its elements.
  - Using dynamic arrays, push and pop take O(n) time in the worst case, but O(1) amortized time (over a large number of operations).
  - Using SLLs, push and pop take O(1) time in the worst case.
- The amortized performance of the two implementations is close, and profiling can help you understand which of the two implementations is more efficient in a
given programming language.

# Homework
DSA HW (G)