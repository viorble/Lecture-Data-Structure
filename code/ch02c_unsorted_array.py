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


if __name__ == "__main__":
    a = UnsortedArray(5)
    print(f"max_size:{a.max_size()}, current length: {len(a)}")
    print(a)
    a.insert(10)
    a.insert(20)
    a.insert(30)
    a.insert(40)
    print(a)
    # a.delete(2)
    # print(a)
    # print(a.find(20))
    # print(a.find(30))
    # print(a.find(100))
    # a.traverse(print)
    # print(a.max_size())
    # try:
    #     a.insert(100)
    # except ValueError as e:
    #     print(e)
    # try:
    #     a.delete(100)
    # except ValueError as e:
    #     print(e)
    # try:
    #     a.delete(1)
    #     a.delete(1)
    #     a.delete(1)
    #     a.delete(1)
    #     a.delete(1)
    # except ValueError as e:
    #     print(e)
    # print(a)
