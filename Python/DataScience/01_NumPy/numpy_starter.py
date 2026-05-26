"""NumPy starter exercises — array operations, indexing, broadcasting."""

import numpy as np

# --- Section 1: Array Operations ---
# Create arrays with np.array, np.zeros, np.arange; perform element-wise math
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print("Sum:", a + b)
print("Shape:", a.shape)
# TODO: Create a 3x3 matrix of ones and multiply every element by 2

# --- Section 2: Indexing and Slicing ---
# Use integer indexing, slicing, and boolean masks on 1D and 2D arrays
matrix = np.arange(12).reshape(3, 4)
print("Row 0:", matrix[0])
print("Column 1:", matrix[:, 1])
# TODO: Select all elements greater than 5 using a boolean mask

# --- Section 3: Broadcasting ---
# NumPy broadcasts smaller arrays across larger ones without explicit loops
row = np.array([[1, 2, 3]])
col = np.array([[10], [20], [30]])
print("Broadcast sum:\n", row + col)
# TODO: Normalize each column of a random 4x3 matrix to zero mean, unit variance
