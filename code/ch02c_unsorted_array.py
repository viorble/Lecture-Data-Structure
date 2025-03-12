import sys

'''sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/.venv/lib/python3.13/site-packages"
)
'''
'''
sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/my_package"
)
'''

from pathlib import Path
package_path = Path.cwd() / "my_package"
sys.path.append(str(package_path))

from arrays.core import Array

class UnsortedArray:
    """Return a new unsorted array whose items are restricted by typecode, and that can contain at most `max_size` elements. The unsorted array is left adjusted

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


# test unsorted array
if __name__ == "__main__":

    # initialization method
    a = UnsortedArray(9)
    a.insert(0)
    a.insert(7)
    a.insert(-1)
    a.insert(3)
    print(f"Init: max_size:{a.max_size()}, current length: {len(a)}")
    print(f"{a[1]=}")
    try:
        print(f"{a[6]=}")
    except IndexError as e:
        print(e)
    print(a)
    print()

    # insert method
    print("Insert:")
    a.insert(-2)  # insert value -2
    print(a)
    print(f"max_size:{a.max_size()}, current length: {len(a)}")
    print()

    # delete method
    print("Delete:")
    a.delete(2)  # delete index 2, its value is -1
    print(a)
    print(f"max_size:{a.max_size()}, current length: {len(a)}")
    print()

    # find method
    print("Find:")
    print("index:", a.find(7))  # find value 7
    print("index:", a.find(10))  # find value 2
    print()

    # traverse method
    print("Traverse:")
    a.traverse(print)
    a.traverse(lambda x: print(x, end=" "))
