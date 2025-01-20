import sys

sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/.venv/lib/python3.13/site-packages"
)

# implement array by list
my_list = [1, 3.14, "Hello", ["a", "b", "c"]]  # not same data types
my_list.append("World")  # not fixed size
print(my_list[4])  # direct access by index
print(
    id(my_list[0]), id(my_list[1]), id(my_list[2])
)  # not continuous memory allocation

# implement array by array
from array import array

my_array = array("i", [1, 2, 3])  # same data types
my_array.append(4)  # not fixed size
print(my_array[3])  # direct access by index
print(id(my_array[0]), id(my_array[1]), id(my_array[2]))  # continuous memory allocation

# implement array by numpy.array
import numpy as np

my_np_array = np.array([1, 2, 3])  # same data types
print(my_np_array[2])  # direct access by index

for i in range(len(my_np_array)):
    print(
        f"Element {i}: Value = {my_np_array[i]}, Address = {my_np_array.ctypes.data + i * my_np_array.itemsize}"
    )
