# Use List to simulate a sorted array
# Assume a is a sorted array with max size 9
# and it contains 5 elements now
# we want to insert value 3 into the array and keep its order


def insert(arr, s, v):

    for i in range(s, 0, -1):
        if arr[i - 1] <= v:
            # Found the right place for the element
            arr[i] = v
            s += 1
            return (arr, s)
        else:
            arr[i] = arr[i - 1]
            arr[i - 1] = None
    arr[0] = v
    s += 1
    return arr, s


# insert value at middle
my_array = [1, 2, 4, 5, 6, None, None, None, None]
current_size = 5
value = 3  # Value to insert
new_array, new_size = insert(my_array, current_size, value)
print(f"{new_array=}, {new_size=}")

# insert value at beginning
my_array = [1, 2, 4, 5, 6, None, None, None, None]
current_size = 5
value = 0  # Value to insert
new_array, new_size = insert(my_array, current_size, value)
print(f"{new_array=}, {new_size=}")

# insert value at end
my_array = [1, 2, 4, 5, 6, None, None, None, None]
current_size = 5
value = 7  # Value to insert
new_array, new_size = insert(my_array, current_size, value)
print(f"{new_array=}, {new_size=}")
