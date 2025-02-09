import sys

sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/.venv/lib/python3.13/site-packages"
)
sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/code"
)
from arrays.core import Array


class DynamicArray:
    """Return a new dynamic _unsorted_ array whose items are restricted by typecode.
    The initial capacity of the array is by default 1, but this can be changed
    by passing a value for the initial_capacity argument.
    """

    def __init__(self, initial_capacity=1, typecode="l"):
        self._array = Array(initial_capacity, typecode)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index >= self._size:
            raise IndexError(f"Index out of bound: {index}")
        return self._array[index]

    def __repr__(self):
        return f"DynamicArray({repr(self._array._array[:self._size])})"

    def _is_full(self):
        return self._size >= self._capacity

    def _double_size(self):
        old_array = self._array
        self._array = Array(self._capacity * 2, self._typecode)
        self._capacity *= 2  # does it correctly update the capacity?
        print(f"Double size: {self._capacity}")
        for i in range(self._size):
            self._array[i] = old_array[i]

    def _halve_size(self):
        old_array = self._array
        self._array = Array(self._capacity // 2, self._typecode)
        self._capacity //= 2
        for i in range(self._size):
            self._array[i] = old_array[i]

    def is_empty(self):
        return len(self) == 0

    def insert(self, value):

        if self._is_full():
            self._double_size()

        # By now, we are sure that self._size < len(self._array)
        self._array[self._size] = value
        self._size += 1

    def find(self, target):

        for i in range(self._size):
            if self._array[i] == target:
                return i
        # Element not found, reached the end of the array
        return None

    def delete(self, target):

        index = self.find(target)
        if index is None:
            raise ValueError(
                f"Unable to delete element {target}: the entry is not in the array"
            )

        # Must shift all the elements after the position of the target
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1

        # Check if we should shrink the array
        if self._capacity > 1 and self._size <= self._capacity / 4:
            self._halve_size()


# test dynamic array
if __name__ == "__main__":

    # initialization method
    a = DynamicArray()
    a.insert(1)
    a.insert(2)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    print(f"Init: capacity:{a._capacity}, current length: {len(a)}")
    print(f"{a = }")

    # insert value 3
    print("Insert:")
    a.insert(3)
    print(f"{a = }")

    # delete value 4
    print("Delete:")
    a.delete(4)
    print(f"{a = }")

    # find
    print("Find:")
    print("index", a.find(3))

    # delete
    print(f"capacity:{a._capacity}, current length: {len(a)}")
    print(a)
    a.delete(3)
    a.delete(2)
    print(f"capacity:{a._capacity}, current length: {len(a)}")
    print(a)
    a.delete(1)
    print(f"capacity:{a._capacity}, current length: {len(a)}")
    print(a)
