# Use List to simulate a sorted array
# Assume a is a sorted array with max size 9
# and it contains 5 elements now


def binary_search(arr, s, v):

    left = 0
    right = s - 1
    while left <= right:
        mid_index = (left + right) // 2
        mid_val = arr[mid_index]
        if mid_val == v:
            return mid_index
        elif mid_val > v:
            right = mid_index - 1
        else:
            left = mid_index + 1
    return None


def delete(arr, s, v):
    index = binary_search(arr, s, v)
    if index is None:
        raise ValueError(f"{v} not found in the array")
    for i in range(index, s - 1):
        arr[i] = arr[i + 1]
    arr[s - 1] = None
    return arr, s - 1


# value is existed in sorted array
my_array = [1, 2, 4, 5, 6, None, None, None, None]
current_size = 5
value = 2  # Value to delete
new_array, new_size = delete(my_array, current_size, value)
print(f"{new_array = }, {new_size = }")

# value is not existed in sorted array
my_array = [1, 2, 4, 5, 6, None, None, None, None]
current_size = 5
value = 3  # Value to delete
try:
    new_array, new_size = delete(my_array, current_size, value)
    print(f"{new_array = }, {new_size = }")  # This line should not be executed
except ValueError as e:
    print(e)
