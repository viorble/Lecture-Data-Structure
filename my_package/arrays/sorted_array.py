from arrays.core import Array


class SortedArray:
    """Return a new sorted array whose items are restricted by typecode, and
    that can contain at most `max_size` elements.
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
        return f"SortedArray({repr(self._array._array[:self._size])})"

    def max_size(self):
        return self._max_size

    def insert(self, value):
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
        for i in range(self._size):
            if self._array[i] == target:
                return i
            elif self._array[i] > target:
                # The array is sorted, we can't find the target in the rest of the array
                return None
        # Element not found, reached the end of the array
        return None

    def binary_search(self, target):
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
        for i in range(self._size):
            callback(self._array[i])
