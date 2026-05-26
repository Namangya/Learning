"""NumPy reference notes — dtypes, ufuncs, linear algebra."""

import numpy as np

# --- dtypes ---
arr = np.array([1, 2, 3], dtype=np.float64)
print(arr.dtype)  # float64

# --- ufuncs (universal functions) ---
x = np.array([1.0, 4.0, 9.0])
print(np.sqrt(x))       # element-wise sqrt
print(np.exp(x))         # element-wise exp

# --- linear algebra ---
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
print(np.dot(A, b))      # matrix-vector multiply
print(np.linalg.det(A))  # determinant
print(np.linalg.inv(A))  # inverse
