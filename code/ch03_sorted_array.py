import sys

sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/.venv/lib/python3.13/site-packages"
)
sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/my_package"
)
from arrays.core import Array


class SortedArray:
    """Return a new sorted array whose items are restricted by typecode, and
    that can contain at most `max_size` elements.
    """

    def __init__(self, max_size, typecode="l"):
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        # The actual number of elements stored in the array
        self._size = 0  # it is also the index of the next element to be inserted

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError(f"Index out of bound: {index}")
        return self._array[index]

    def __repr__(self):
        return f"SortedArray({repr(self._array)}" 
        # output: SortedArray(array('l', [1, 2, 4, 5, 6, 0, 0, 0, 0])
        # return f"SortedArray({repr(self._array._array[:self._size])})"
        # output: SortedArray(array('l', [1, 2, 4, 5, 6]))
        # return f"SortedArray({repr(self._array[:self._size])})"
        # output: Error not support 'slice'

    def max_size(self):
        return self._max_size

    def insert(self, value):
        """
        Functionality:
            Inserts the given value into the sorted array while maintaining the sorted order.
            If the array is already full, raises a ValueError.
            Otherwise, shifts elements to the right to make room for the new value and inserts it in the correct position to keep the array sorted.
        """

        if self._size >= self._max_size:
            raise ValueError(
                f"The array is already full, maximum size: {self._max_size}"
            )
        for i in range(self._size, 0, -1):
            if self._array[i - 1] <= value:
                # Found the right place for the element
                self._array[i] = value
                self._size += 1
                return
            else:
                self._array[i] = self._array[i - 1]
        # If it gets here, it means we need to add the new value as the first entry
        self._array[0] = value
        self._size += 1

    def linear_search(self, target):
        """
        Functionality:
            Performs a linear search over the values in the sorted array.
            Since the array is sorted, we can stop searching once we pass the point where the target value would be located.
            Returns the index of the target value if found, otherwise returns None.
        """

        for i in range(self._size):
            if self._array[i] == target:
                return i
            elif self._array[i] > target:
                # The array is sorted, we can't find the target in the rest of the array
                return None
        # Element not found, reached the end of the array
        return None

    def binary_search(self, target):
        """
        Functionality:
            Performs a binary search on the sorted array.
            Keeps track of left and right indices, and calculates the midpoint index.
            Checks if the midpoint value matches the target. If so, returns the midpoint index.
            Otherwise, recurses on either the left or right half of the array depending on if the
            midpoint value is greater than or less than the target.
            Returns the index if found, otherwise returns None if the target is not found.
        """

        left = 0
        right = self._size - 1
        while left <= right:
            mid_index = (left + right) // 2
            mid_val = self._array[mid_index]
            if mid_val == target:
                return mid_index
            elif mid_val > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return None

    def delete(self, target):
        """
        Functionality:
            Finds the index of the target value using the find method.
            If the target is not found, raises a ValueError.
            Otherwise, shifts all elements after the target to the left to fill in the gap.
            If it succeeds, it decrements the size of the array by 1.
        """

        index = self.binary_search(target)
        if index is None:
            raise ValueError(
                f"Unable to delete element {target}: the entry is not in the array"
            )

        # Must shift all the elements after the position of the target
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1

    def traverse(self, callback):
        """
        Functionality:
            Iterates over the values in the sorted array and applies the given callback function to each value.
        """

        for i in range(self._size):
            callback(self._array[i])


# test sorted array
if __name__ == "__main__":

    # initialization method
    a = SortedArray(9)
    a.insert(1)
    a.insert(2)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    print(f"Init: max_size:{a.max_size()}, current length: {len(a)}")
    print(f"{a = }")

    # insert value 3
    print("Insert:")
    a.insert(3)
    print(f"max_size:{a.max_size()}, current length: {len(a)}")
    print(f"{a = }")

    # delete value 4
    print("Delete:")
    a = SortedArray(9)
    a.insert(0)
    a.insert(1)
    a.insert(4)
    a.insert(7)
    a.insert(9)
    print(f"Init: max_size:{a.max_size()}, current length: {len(a)}")
    print(f"{a = }")
    a.delete(4)
    print(f"{a = }")

    # Searching
    a = SortedArray(9)
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.insert(6)
    a.insert(7)
    a.insert(9)
    a.insert(10)
    print(f"{a = }")
    print("Linear search:")
    index = a.linear_search(8)
    print(f"{index = }")
    print("Binary search:")
    index = a.binary_search(6)
    print(f"{index = }")
