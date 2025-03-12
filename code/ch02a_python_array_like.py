import sys
sys.path.append("/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/.venv/lib/python3.13/site-packages")

# implement array by list
print('--- implement array by list ---')
my_list = [1, 3.14, "Hello", ["a", "b", "c"]]  # not same data types
my_list.append("4")  # not fixed size
print(my_list)
print()

# implement array by array
print('--- implement array by array.array ---')
from array import array
my_array = array("l", [1, 2, 3])  # same data types, l is signed integer
print(my_array[0])  # get the value at the given index
my_array[1] = 100  # set the value at the given index
my_array.append(4)  # not fixed size, can be appended
print(repr(my_array))
print(my_array)
print()

# implement array by numpy.array
print('--- implement array by numpy.array ---')
import numpy as np
my_np_array = np.array([1, 2, 3])  # same data types
# numpy array is a static array, it can not be appended directly. Need create a new array
new_np_array = np.append(my_np_array,4) 
print(my_np_array)
print(new_np_array)

