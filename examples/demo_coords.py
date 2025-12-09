import numpy as np
from src.coords import swap

coords = np.array([
    [10, 20, 30, 40, 1],
    [5,  8,  12, 16, 2]
])
print("Original:")
print(coords)
print("Swapped:")
print(swap(coords))
