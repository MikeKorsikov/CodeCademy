# Additional Linear Algebra Operations

import numpy as np
# Represent the following system in NumPy matrix/vector form, then solve for x, y, and z

# Given
'''
4x + z = 2
-y + 2z - 3x = 0
.5y - x - 1.5z = -4
'''
# Coefficient matrix A
A = np.array([
    [4, 0, 1],       # Coefficients from the first equation
    [-3, -1, 2],     # Coefficients from the second equation
    [-1, 0.5, -1.5]  # Coefficients from the third equation
])

# Constant vector b
b = np.array([2, 0, -4])

# Solve for [x, y, z]
x, y, z = np.linalg.solve(A, b)

# Print the solution
print("Solution [x, y, z]:", x, y, z)

#
# Coefficient matrix A
A = np.array([
    [2, 0, -2, 3],   # Coefficients from the first equation
    [-1, 4, -1, 0],  # Coefficients from the second equation
    [3, -1, -2, 2],  # Coefficients from the third equation
    [-2, -1, 3, 0]   # Coefficients from the fourth equation
])

# Constant vector b
b = np.array([4, 1, 2, -2])

# Solve for [a, b, c, d]
a, b, c, d = np.linalg.solve(A, b)

# Print the solution
print("Solution [a, b, c, d]:", a, b, c, d)