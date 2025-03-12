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
    color: LightSkyBlue;  
  }

  .small-text {
    font-size: 0.75rem;
  }
---

# Let Array be Left-Justified
![bg right:40% w:500 left-justified](../Lecture-Data-Structure/restricted/a_left_justified_array.png)

 - Basically, we don’t have to follow any order when assigning new values to its elements
 - However, We might keep track of which elements are meaningful to application.
 - In most cases, the order in which we store the elements won’t matter.
 - Thus, we can simply add the new elements at the first unused index in the array and keep the array left-justified: 
 - That is, if we add k ≤ n elements to our array, they will be at the indexes from 0 to k-1.

# Design Unsorted Arrays Class <br> (core array with left-justified)

```python
Class UnsortedArray:
    def __init__(self, max_size, typecode="l"): pass
    def __len__(self): pass
    def __getitem__(self, index): pass
    def __repr__(self): pass
    def max_size(self): pass
    def insert(self, new_entry): pass
    def delete(self, index): pass
    def find(self, target): pass
    def traverse(self, callback): pass
```

# Adding / Delete an Element in Unsorted Array
![insert / delete elements in unsorted array](../Lecture-Data-Structure/restricted/unsorted_array_insert_delete.png)

[Code: unsorted array](../Lecture-Data-Structure/code/ch02c_unsorted_array.py)

# Lab
(1) Add a method in unsorted_array class to return max value
(2) Add a method in unsorted_array class to return min value
(3) Add a method in unsorted_array class to clear array