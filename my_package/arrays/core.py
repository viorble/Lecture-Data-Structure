import array


class Array:
    """
    A core array class that uses the built-in array module and provides basic functionality

    According to built-in array, the type is specified at object creation time by using a type code (https://docs.python.org/3/library/array.html)
    Two type codes are used in this class:

        Type code   C Type             Minimum size in bytes
        'l'         signed integer     4
        'f'         floating point     4

     Parameters:
         size: The maximum number of elements the array can hold.
         typecode: the typecode of the array. Defaults to 'l' for int.

    """

    def __init__(self, size, typecode="l"):
        if size <= 0:
            raise ValueError(f"Invalid array size (must be positive): {size}")
        self._size = size
        self._array = array.array(typecode, [0] * size)

    def __len__(self):
        # return the number of elements in the array.
        return self._size

    def __getitem__(self, index):
        # Get the value at the given index.
        if index < 0 or index >= self._size:
            raise IndexError("array index out of range")
        return self._array[index]

    def __setitem__(self, index, val):
        # Set the value at the given index.
        if index < 0 or index >= self._size:
            raise IndexError("array assignment index out of range")
        self._array[index] = val

    def __repr__(self):
        # Return the string representation of the array.
        return repr(self._array)