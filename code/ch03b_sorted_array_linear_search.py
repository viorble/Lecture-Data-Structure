# Use List to simulate a sorted array
# Assume a is a sorted array with max size 9
# and it contains 5 elements now

def linear_search(arr, s, v):

    for i in range(0, s):
        if arr[i] == v:
            # Found the right place for the element
            return i
        elif arr[i] > v:
            return None
    return None


# value is existed in sorted array
my_array = [1, 2, 4, 5, 6, None, None, None, None]
current_size = 5
value = 4  # Value to insert
index = linear_search(my_array, current_size, value)
print(f"{index = }")

# value is not existed in sorted array
my_array = [1, 2, 4, 5, 6, None, None, None, None]
current_size = 5
value = 3  # Value to insert
index = linear_search(my_array, current_size, value)
print(f"{index = }")
