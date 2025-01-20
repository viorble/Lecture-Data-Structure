import sys

print("which python:", sys.executable)
print("python version:", sys.version[0:6])
sys.path.append(
    "/Users/jacky/Library/Mobile Documents/com~apple~CloudDocs/交大教學/DSA/Lecture-Data-Structure/.venv/lib/python3.13/site-packages"
)
lib_path = sys.path
for i, p in enumerate(lib_path):
    print(f"{i}: {p}")

import numpy as np

my_array = np.array([1, 2, 3])
print(my_array)
