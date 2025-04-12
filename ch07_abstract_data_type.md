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
# Chapter 7: Abstract Data Types
- **Abstract data type (ADT)** is a mathematical model for data types, defined by its behavior from the point of view of data users specifically in terms of 
  - possible values
  - possible operations
  - behavior of operations 
- Data structures we learned before, which are concrete representations of data, and are the point of view of an implementer, not a user.
- ADT example: a STACK has push/pop operations that follow a Last-In-First-Out rule, and can be concretely implemented using either a list or an array.

# Three-Level Hierarchy
- **Abstract data type**: a theoretical concept that describes at a high level how data can be organized and the operations that can be performed on the data.
- **Data structure**: how data is organized in memory (or disk!) and the internal representation details of the DS
- **Implementation**: choose a programming language and translate the DS into code.
![bg right:40% w:90%](../Lecture-Data-Structure/restricted/abstract_data_type.png)

# A Simple ADT: Bag (Shopping Cart)
![bg right:35% w:90%](../Lecture-Data-Structure/restricted/bag_diagram.png)
A bag is a collection of objects with 2 methods:
- insert(x)— allow a client to add a single element to the bag. The order of insertion is not important.
- iterate() — allow a client to go through all the elements in the bag. The order in which elements are iterated is not guaranteed.
- Data structure : Singly Link
- Implementation: Python

# Implementation of Bag
```python
class Bag:
    def __init__(self):
        self._data = SinglyLinkedList()

    def insert(self, value):
        self._data.insert_in_front(value)

    def traverse(self):
        return self._data.traverse()        
```