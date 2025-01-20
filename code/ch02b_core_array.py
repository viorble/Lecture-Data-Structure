import array


class Array:
    """Return a new array whose items are restricted by typecode, and
    that can contain at most `size` elements.

    Arrays behave very much like Python list, except that
    the type of objects stored in them is constrained. The type is specified
    at object creation time by using a type code, which is a single character.
    The following type codes are defined:

        Type code   C Type             Minimum size in bytes
        'b'         signed integer     1
        'B'         unsigned integer   1
        'u'         Unicode character  2
        'h'         signed integer     2
        'H'         unsigned integer   2
        'i'         signed integer     2
        'I'         unsigned integer   2
        'l'         signed integer     4
        'L'         unsigned integer   4
        'q'         signed integer     8
        'Q'         unsigned integer   8
        'f'         floating point     4
        'd'         floating point     8

     Parameters:
         max_capacity (int): The maximum number of elements the array can hold.
         typecode (str, optional): The typecode of the array. Defaults to 'l' for int.

    """

    def __init__(self, size, typecode="l"):
        if size <= 0:
            raise ValueError(f"Invalid array size (must be positive): {size}")
        self._size = size
        self._array = array.array(typecode, [0] * size)

    def __len__(self):
        """
        Return the number of elements in the array.

        Parameters:
            None

        Returns:
            int: The number of elements in the array.
        """

        return self._size

    def __getitem__(self, index):
        """
        Get the value at the given index.

        Parameters:
            index (int): The index to get the value from.

        Returns:
            Union[int, float]: The value at the given index.
        """

        if index < 0 or index >= self._size:
            raise IndexError("array index out of range")
        return self._array[index]

    def __setitem__(self, index, val):
        """
        Set the value at the given index.

        Parameters:
            index (int): The index to set the value at.
            val (Union[int, float]): The value to set.

        Returns:
            None
        """

        if index < 0 or index >= self._size:
            raise IndexError("array assignment index out of range")
        self._array[index] = val

    def __repr__(self):
        """
        Return the string representation of the array.

        Parameters:
            None

        Returns:
            str: The string representation of the array.
        """

        return repr(self._array)


if __name__ == "__main__":
    a = Array(5)
    print(f"{a = }")  # __repr__
    print(f"{len(a) = }")  # __len__
    print(f"{a[0] = }")  # __getitem__

    b = Array(3, "f")
    b[2] = 3.51  # __setitem__
    print(f"{b[2]=:.2f}")
    print(b)
