# vectors
# dot product
# matrices 
# Need to review vectors and matrices again out of CodeCademy

import numpy as np

# Given vectors
vector_1 = np.array([-2,-6,2,3])
vector_2 = np.array([4,1,-3,8])
vector_3 = np.array([5,-7,9,0])

matrix = np.column_stack((vector_1, vector_2, vector_3))
print(matrix)

print(matrix.shape)

# print third column
print(matrix[:,2])