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
  .small-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .small-grid img {
    width: 50%;
  }
  .middle-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .middle-grid img {
    width: 75%;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }
  .grid img {
    width: 100%;
  }
  .red-text {
    color: red;
  }
  
  .blue-text {
    color: blue;  
  }

  .small-text {
    font-size: 0.75rem;
  }
---
# What is a Array
- Array is a data structure consisting of a collection of elements, of same memory size, each identified by an index. 
- Memory address of an element can be computed by 
  [array_start_address] + ([size] * [index])
- Static Arrays, Sorted Arrays, Dynamic Arrays

![bg right:40% w:500 array memory](../Lecture-Data-Structure/restricted/array_memory_address.png)

---
# Arrays
- Key characteristics
  - It stores a collection of data
  - Its elements can be accessed by index
  - Elements don’t have to be accessed sequentially
- Implementing arrays as a core language feature
  - Arrays are allocated in memory as a single, uninterrupted block of memory with
sequential locations.
  - Arrays are restricted to storing data of the same type to quickly know the memory address of each element.
  - [**Static Arrays**] The size of arrays (# of elements) must be decided when the array is created, and that size can’t be changed.

---
# Arrays in Python

Class          |Fixed Size|Fixed Type|Implementation
---------------|----------|-----------------|--------------
**list**       |NO    |NO               |dynamic array like
**array.array**|NO    |YES              |dynamic array like
**Numpy.array**|YES   |YES              |static array

[Code: array-like in Python](../Lecture-Data-Structure/code/ch02a_python_array_like.py)

---
### Implement Arrays as a Core Language Feature
  - allocated in continuous memory
  - restricted to storing data of the same type
  - size of arrays must be decided when the array is created

### The core array class will have the following methods:
  - Initialize: create an array with a given size and type
  - Create: initiate an array
  - Get the value at a given index
  - Get the number of elements in the array
  - Display the array

[Code: core array](../Lecture-Data-Structure/code/ch02b_core_array.py)

---
# Lab
Use class Array to create an array object
- size is 10
- store 4 integers
