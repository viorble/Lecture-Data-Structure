---
marp: true
theme: default
paginate: true
---
# Linear Search on Unsorted Array
![bg right:50% w:600 Linear search on unsorted array](https://www.freecodecamp.org/news/content/images/2023/07/image-66.png)
## Time complexity: O(n)
- n = 4 -> 4 ops
- n = 100 -> 100 ops
- n = 1024 -> 1024 ops
- n = 1,048,576 -> 1,048,576 ops

---
# Binary Search on Sorted Array
![bg right:50% w:600 Binary search on sorted array](https://www.freecodecamp.org/news/content/images/2023/07/image-65.png)
## Time complexity: O(log n)
- n = 4 -> 2 ops
- n = 100 -> 7 ops <br> (removed elements from 100->50->25->13->7->4->20->1)
- n = 1024 -> 10 ops
- n = 1,048,576 -> 20 ops

---
# Design Sorted Arrays Class
![Sorted array func diagram](../Lecture-Data-Structure/restricted/sorted_array_func_diagram.png)

---
# Implement Sorted Arrays Class
```python
class SortedArray:

    def __init__(self, max_size, typecode="l"): pass
    def __len__(self): pass
    def __getitem__(self, index): pass
    def __repr__(self): pass
    def __iter__(self): pass
    def max_size(self): pass
    def insert(self, value): pass
    def linear_search(self, target): pass
    def binary_search(self, target): pass
    def delete(self, target): pass
```
---

# Insert and Delete an Element on Sorted Array
![bg right:60% w:600 Sorted array insert and remove](../Lecture-Data-Structure/restricted/sorted_array_insert_remove.png)

---
# Search an Element on Sorted Array
![bg right:60% w:600 Search on sorted array](../Lecture-Data-Structure/restricted/sorted_array_search.png)

---
# Lab
Implement the traverse method for sorted arrays. Then use it to print all the elements in the array in an ascending sequence.