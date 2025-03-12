import sys

sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/.venv/lib/python3.13/site-packages"
)
sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/code"
)
from arrays.core import Array


class UnsortedArray:
    """Return a new unsorted array whose items are restricted by typecode, and that can contain at most `max_size` elements.

    Parameters:
    max_size (int): The maximum number of elements the array can hold.
    typecode (str, optional): The typecode of the array. Defaults to 'l' for int.
    """

    def __init__(self, max_size, typecode="l"):
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        # The actual number of elements stored in the array
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError(f"Index out of bound: {index}")
        return self._array[index]

    def __repr__(self):
        return f"UnsortedArray({repr(self._array._array[:self._size])})"

    def max_size(self):
        return self._max_size

    def insert(self, new_entry):
        if self._size >= len(self._array):
            raise ValueError("The array is already full")
        else:
            self._array[self._size] = new_entry
            self._size += 1

    def delete(self, index):
        if self._size == 0:
            raise ValueError("Delete from an empty array")
        elif index < 0 or index >= self._size:
            raise ValueError(f"Index {index} out of range.")
        else:
            self._array[index] = self._array[self._size - 1]
            self._size -= 1

    def find(self, target):
        for index in range(0, self._size):
            if self._array[index] == target:
                return index
        # Couldn't find the target
        return None

    def traverse(self, callback):
        for index in range(self._size):
            callback(self._array[index])

    def max_min(self):
        if self._size == 0:
            raise ValueError("Empty array")
        max_value = self._array[0]
        min_value = self._array[0]
        max_index = 0
        min_index = 0
        for index in range(1, self._size):
            if self._array[index] > max_value:
                max_value = self._array[index]
                max_index = index
            if self._array[index] < min_value:
                min_value = self._array[index]
                min_index = index
        return f"{max_index=}, {max_value=}, {min_index=}, {min_value=}"

    def clear(self):
        self._size = 0


a = UnsortedArray(5)
a.insert(1)
a.insert(-1)
a.insert(3)
a.insert(0)
print(a)
print(a.max_min())
a.clear()
print(f"max_size:{a.max_size()}, current length: {len(a)}")
print(a)
