import array

class Array:
    """
    A core Array class built upon the built-in array module and provides basic functionality

    According to built-in array, the type is specified at object creation time by using a type code
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
        self._array = array.array(typecode, [0] * size) # set default value to 0

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

    
if __name__ == "__main__":
    # test cases to validate the functions of module 
    a = Array(5)  # _init__
    print(len(a)) # __len__
    a[0] = 2      # __setitem__
    print(a[0])   # __getitem__
    print(a)      # __repr__

    b = Array(5, "f")
    b[2] = 1.25
    print(b)
    
    # c = Array(-1, "l")  # error case of __init__
    # foo = a[7]          # error case of __getitem__
    # a[7] = 20           # error case of __setitem__

