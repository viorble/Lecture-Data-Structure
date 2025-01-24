---
marp: true
theme: default
paginate: true
---
# Big-O Notation: A Framework for Measuring Algorithm Efficiency
![bg right:50% w:600 Check algorithm goodness](../Lecture-Data-Structure/restricted/check_algorithm_goodness.png)

---
# Measure Terms of Algorithm Performance
- Time
- Memory space
---
# Measure Methods of Algorithm Performance
**[Profiling 效能分析]** Implement the algorithm and run code on various **inputs** to measure time and memory it takes. <br>
```python
from time import time
start time = time()
run algorithm
end time = time()
elapsed = end time− start time
```
**[Asymptotic analysis 漸近分析]** Find mathematical formulas that describe how an algorithm behaves as a function of its **input**.
![bg right:40% w:1000 big O](https://cdn.hashnode.com/res/hashnode/image/upload/v1657289969914/jdsAxrEyZ.JPG?auto=compress,format&format=webp)

---
# Big-O Notation


---
# Four Rules to Find Big O Complexity of an Algorithm
- Rule 1: Worst case
- Rule 2: Remove the leading constants
- Rule 3: Different terms for inputs
```python
for i in range(n):         # Loop 1 depends on n
    for j in range(m):     # Loop 2 depends on m
        print(i, j)
# The algorithm is  O(n * m) , as n and m represent independent inputs that multiply together.        
```
- Rule 4: Drop nondominant terms

**[Question]** Find Big O complexity of an algorithm with the time complexity 20n³ + 5n + 7
**[Answer]** Using the rules, this can be simplified to O(n³)