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


# value is existed in sorted array
my_array = [1, 2, 4, 5, 6, None, None, None, None]
current_size = 5
value = 2  # Value to insert
index = binary_search(my_array, current_size, value)
print(f"{index = }")

# value is not existed in sorted array
my_array = [1, 2, 4, 5, 6, None, None, None, None]
current_size = 5
value = 3  # Value to insert
index = binary_search(my_array, current_size, value)
print(f"{index = }")
