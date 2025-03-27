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
# Chapter 5: Dynamic Arrays
There are many examples of real-world applications where we need to be flexible and resize a data structure to meet an increasing demand.<br> 
**Dynamic Arrays** enable the ability to adjust array size. 
- Find strategies to give us the flexibility
- Discuss how to implement dynamic arrays.

# The Limitation of Static Arrays -> Fixed Size
Because arrays are implemented as a <span class="red-text">contiguous block of memory</span>.<br>
Once a fixed size array full:
- A new, larger array must be created.
- Elements must be transferred from the old array to the new one.
- It is expensive.
![bg right:50% w:80% fix size full](restricted/fix_size_array_full.png)

# Two Strategies to Fulfill Demand
![bg right:50% w:80% fix size full](restricted/tradeoffs_fixed_size.png)
- Allocating a small array, then increase size when needed
 <span class="blue-text">busy to move data</span>
- Allocating a large array
  <span class="blue-text">waste memory</span>

# Dynamic Arrays
- Dynamic arrays are implemented upon static arrays
- That’s natural that we have to pay the cost of resizing the array from time to time.
- The key to dynamic arrays is to find a strategy using to <span class="blue-text">grow and shrink the underlying static arrays</span>.


# How to Grow Array Size
- When should we resize the array? 
  - Already full
  - Near full
- How much larger should the new array be?
  - Grow by one element
  - Grow by X elements
  - Double the size 
- What should we do when we delete elements? Should we shrink the array as well?
  - Halve on delete
  - Smarter shrinking 

# Approaches to Grow Array
A comparison of the number of assignments for strategies to insert 100 elements into a
dynamic array

<style scoped>
table {
  font-size: 0.60rem;
}
</style>
Approach | # of expression |Total|Big O
---------|---------------------|--------|-----
Increase size by 1| 1 + 2 + 3 + 4 + … + 98 + 99| 4950 | O(n**2)
Increase size by 4| 1 + 5 + 9 + 13 +… + 93 + 97 |1225 | O(n**2)
Double the size |1 + 2 + 4 + 8 + 16 + 32 + 64 |127 | O(n)

![bg right:40% w:100% fix size full](restricted/apply_strategy_arrays.png)
><span class="small-text">'Double the size'的複雜度：https://stackoverflow.com/questions/19146037/efficiency-of-growing-a-dynamic-array-by-a-fixed-constant-each-time</span>
><span class="small-text">等比數列的和：https://zh.wikipedia.org/zh-tw/等比数列</span>

# Approaches to Shrink Array

<div class="columns">
<div>
    <span class="blue-text">Halve on delete:</span> shrink array by halving it as soon as 50% of its elements are unused
</div>

<div>
  <span class="blue-text">Smarter shrinking:</span> shrink array by halving until only 25% of the array is used
</div>

</div>

<div class="columns">
    <img src="restricted/halve_on_delete.png" alt="halve on delete">
    <img src="restricted/smarter_shrinking.png" alt="smarter shrinking">
</div>

# Implementing a Dynamic Array
- We start with an array of size one (unless the client specifies an initial capacity).
- If we need to insert a new element and the static array is already filled to its maximum capacity, we resize the array by doubling its size.
- After we remove an element from the array, we resize the array by halving its size if only a quarter of the maximum capacity is filled.
- The elements will be stored in the same order as they are inserted.
- When an element is deleted from the array, the elements after it are shifted to fill the hole left by the removed element.

# The DynamicArray Class
```python
class DynamicArray():
    def __init__(self, initial_capacity=1, typecode="l"): pass
    def __len__(self): pass
    def __getitem__(self, index): pass
    def __repr__(self): pass
    def _is_full(self): pass
    def _double_size(self): pass
    def _halve_size(self): pass
    def is_empty(self): pass
    def insert(self, value): pass
    def find(self, target): pass
    def delete(self, target): pass
```

# Insert Elements into Dynamic Array
![bg right:50% w:100%](restricted/dynamic_array_insert.png)

# Delete Elements from Dynamic Array
![bg right:50% w:100%](restricted/dynamic_array_delete.png)
