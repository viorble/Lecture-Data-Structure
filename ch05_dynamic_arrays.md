---
marp: true
theme: default
paginate: true
---
# The Limitation of Static Arrays - Fixed Size
Because arrays are implemented as a contiguous block of memory. Once a fixed size array full, a new, larger array must be created, and elements must be transferred from the old array to the new one. It is expensive
![bg right:50% w:600 fix size full](restricted/fix_size_array_full.png)

---
# Tradeoffs
![bg right:50% w:600 fix size full](restricted/tradeoffs_fixed_size.png)
- Allocating a small array; busy to move data.
- Allocating a large array; waste memory.

---
# Dynamic Arrays
- Dynamic arrays are implemented with static arrays
- We still have to pay the price of allocating a new array and throwing away the old one every time we
need to resize it. 
- The key to dynamic arrays is 'what makes them a good compromise'; the strategy we use to grow and shrink the underlying static arrays.
- That’s natural that we have to pay the cost of resizing the array from time to time.

---
# How Can We Grow an Array’s Size?
- When should we resize the array?
- How much larger should the new array be?
- What should we do when we delete elements? Should we shrink the array as well?

---
# Applying the Strategies to Arrays
A comparison of the number of assignments for strategies to insert 100 elements into a
dynamic array
Strategy | # of expression |Total|Big O
---------|---------------------|--------|-----
Increase by 1| 1+2+3+4+ … +98+99| 4851 | O(n**2)
Increase by 4| 1+5+9+ … +93+97 |1225 | O(n**2)
Double size |1+2+3+6+12+32+64 |127 | O(n)

![bg right:30% w:400 fix size full](restricted/apply_strategy_arrays.png)

---
# Should Also Shrink Arrays
Havle on delete vs Smarter shrinking
<style>
.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}
.grid img {
    width: 50%;
}
</style>

<div class="grid">
    <img src="restricted/halve_on_delete.png" alt="halve on delete">
    <img src="restricted/smarter_shrinking.png" alt="smarter shrinking">
</div>