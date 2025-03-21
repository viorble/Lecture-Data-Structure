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
    width: 60%;
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
# Big-O Notation: A Framework for Measuring Algorithm Efficiency
![bg right:50% w:600 Check algorithm goodness](../Lecture-Data-Structure/restricted/check_algorithm_goodness.png)

# Measure Terms of Algorithm Performance
- Time complexity
- Memory space complexity

# Measure Methods of Algorithm Performance
**[Profiling 效能分析]** Implement the algorithm and run code on various **inputs** to measure time and memory it takes. <br>
```python
from time import time
start time = time()
run algorithm
end time = time()
elapsed = end time− start time
```
**[Asymptotic analysis 漸近分析]** Find mathematical formulas that describe how an algorithm behaves **as a function of its <u>input</u>**.
![bg right:40% w:1000 big O](https://cdn.hashnode.com/res/hashnode/image/upload/v1657289969914/jdsAxrEyZ.JPG?auto=compress,format&format=webp)

# Calculate Operations of an Algorithm
```python
def add_up_to(n):
    sum = 0                  # 1 op
    for i in range(1, n+1):  # n ops
        sum += i             # n ops 
    return sum               # 1 op
# total: (2n + 2) ops
```
```python
def add_up_to(n):
    return (1 + n) * n / 2   # 3 op
# total:  3 ops, regardless of the size of n
```

# Big-O Classify Growth Rate
- Big-O notation is used to **classify** algorithms according to how their <u>run time</u> or <u>space requirements</u> grow as the input size grows.
![bg right:60% w:90%](restricted/big_O_growth_rate.png)

# Big-O Definition
- f(n): function of algorithm's running time, n is the size of input
- We can find two linear functions (n and n/2) as a pair, which bounds f(n), when n > 3
- Define O(n) is a class of functions which grow as fast as straight lines, like n, 10n, n/10
- Since n, n/2 belongs to O(n), we write f(n)=O(n) that means f(n) belongs to O(n) class
<div class="middle-grid">
    <img src="restricted/fn_equal_on.png">
    <img src="restricted/common_growth_function.png">
</div>

# Big-O Arithmetic
Based on the definition of Big-O notation, f(n) = O(n), we do not care which straight line pair can bound f, as long as there is one pair when n is large enough.
<div class="middle-grid">
    <img src="restricted/y_eaual_n.png">
    <img src="restricted/line_3n_plus_5.png">
</div>

# Asymptotically Equivalent
- For asymptotic analysis, two lines are considered asymptotically equivalent
    - Two functions f(n) = n and g(n) = 3n are considered equivalent
    - Their growth is of the same order of magnitude (同一個量級).
- When comparing two algorithms, we compare their order of magnitude in terms of their Big-O complexity respectively.

# Four Rules to Find Big O Complexity of an Algorithm
- Rule 1: Worst case
- Rule 2: Remove the constants
- Rule 3: Different inputs different variables

```python
n = 10  # 1 op
m = 5   # 1 op
for i in range(n):         # Loop 1 n ops
    for j in range(m):     # Loop 2 m ops
        print(i, j)
# The algorithm is  O(n * m) , as n and m represent independent inputs that multiply together.        
```
- Rule 4: Drop nondominant terms

**[Question]** Find Big O complexity of an algorithm with the time complexity 20n³ + 5n + 7
**[Answer]** Using the rules, this can be simplified to O(n³)
https://dev.to/coderjay06/four-rules-for-big-o-1915

# The Big O of Linear Search
```python
def linear_search(self, target):
    for i in range(self._size):      # repeat F(n) times
        if self._array[i] == target: # cost: O(1)
            return i                 # cost: O(1)
        elif self._array[i] > target:# cost: O(1)
            return None              # cost: O(1)
    return None                      # cost: O(1)
```
- The formula for the running time of linear search is 
  T(n) = F(n) * (2 * O(1)) + O(1) 
       = F(n) * O(1) + O(1) 
       = O(F(n))
- F(n) = how many times the for loop is repeated = n
- T(n) = O(n)

# The Big O of Binary Search
```python
def binary_search(self, target):
    left = 0                              # O(1)
    right = self._size - 1                # O(1)
    while left <= right:                  # G(n) iterations
        mid_index = (left + right) // 2     # O(1)
        mid_val = self._array[mid_index]    # O(1)
        if mid_val == target:               # O(1)
            return mid_index                # O(1)
        elif mid_val > target:              # O(1)
            right = mid_index - 1           # O(1)
        else
            left = mid_index + 1            # O(1)
    return None                          # O(1)
```
- The formula for the running time of linear search is 
  T(n) = 2 * O(1) + G(n) * 4 * O(1) + O(1) = O(G(n))
- G(n) = how many times the for loop is repeated = logn
- T(n) = O(logn)

# Lab
Using big-O notation and asymptotic analysis, derive the running time used for insert, delete, and traverse on sorted arrays. How do they compare to the same methods on unsorted arrays?