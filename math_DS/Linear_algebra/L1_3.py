import numpy as np

# Given
A = np.array([[1,-1,1], [0,1,0], [-1,2,1]])
B = np.array([[0.5,1.5,-0.5], [0,1,0], [0.5,-0.5,0.5]])

print(np.matmul(A,B))
print(np.matmul(B,A))

# transposing
print(A.T)
print(B.T)