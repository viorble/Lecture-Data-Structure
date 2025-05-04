"""Module providing an implementation for stack, using singly-linked lists to store the elements."""
import sys

sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/my_package"
)

from heaps.heap import Heap

def k_largest_elements(arr, k):
    heap = Heap(element_priority=lambda x: -x)
    for i in range(len(arr)):
        if len(heap) >= k:
            if heap.peek() < arr[i]:
                heap.top()
                heap.insert(arr[i])
        else:
            heap.insert(arr[i])
    print(heap)        
    return heap.top()

# main
nums = [8, 7, 4, 3, 2, 1, 6]
k = 4
print(k_largest_elements(nums, k)) 