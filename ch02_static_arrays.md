---
marp: true
theme: default
paginate: true
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

[Array in Python](../Lecture-Data-Structure/code/grokking_ds/ch02_array_in_python.py)

---
# Implement Arrays as a Core Language Feature
  - allocated in continuous memory
  - restricted to storing data of the same type
  - size of arrays must be decided when the array is created

#### The core array class will have the following methods:
    - Initialize: create an array with a given size and type
    - Create: initiate an array
    - Get the value at a given index
    - Get the number of elements in the array
    - Display the array

---
# Lab
Use class Array to create an array object
- size is 10
- store 4 integers
- traverse the array to print all elements