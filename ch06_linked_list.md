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
    width: 50%;
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
  - Circular linked list

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

# Singly Linked List
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

# Implementing Singly Linked List
