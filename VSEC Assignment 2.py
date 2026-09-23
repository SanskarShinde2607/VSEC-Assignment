import numpy as np

# Create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
print("\nMatrix Addition:")
print(A + B)

# Matrix Subtraction
print("\nMatrix Subtraction:")
print(A - B)

# Matrix Multiplication
print("\nMatrix Multiplication:")
print(A @ B)

# Transpose
print("\nTranspose of A:")
print(A.T)

# Determinant
print("\nDeterminant of A:")
print(np.linalg.det(A))

# Inverse
print("\nInverse of A:")
print(np.linalg.inv(A))

# Statistical Operations
data = np.array([10, 20, 30, 40, 50])

print("\nStatistical Data:")
print(data)

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Sum:", np.sum(data))
