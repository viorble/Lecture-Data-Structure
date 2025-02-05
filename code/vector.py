class Vector:
    """
    Represent a vector in a multidimensional space.

    """

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self._coords)[1:-1] + ">"  # adapt list representation


########

a = Vector(5)
b = Vector(5)
c = Vector(5)
d = Vector(0)

print("a: ", a, "dimension:", len(a))
print("b: ", b, "dimension:", len(b))

a[2] = 3
b[3] = 2

print("a: ", a, "dimension:", len(a))
print("b: ", b, "dimension:", len(b))

c = a + b  # overload + operator

print("c:", c)  # overloaded str operator

total = 0
for entry in c:  # implicit iteration via __len__ and __getitem__
    total += entry
print("Total:", total)

if bool(d):  # Uses implied meaning of bool function
    print("The vector has non zero length")
else:
    print("The vector has zero length")
