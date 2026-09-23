import numpy as np

# Creating a NumPy array
arr = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:", arr)

# 1. Indexing
print("First element:", arr[0])
print("Third element:", arr[2])
print("Last element:", arr[-1])

# 2. Slicing
print("First three elements:", arr[:3])
print("Elements from index 2 to 4:", arr[2:5])
print("Alternate elements:", arr[::2])

# 3. Reshaping
matrix = arr.reshape(2, 3)
print("Reshaped Array:")
print(matrix)

# 4. Vectorized Operations
print("Addition:", arr + 5)
print("Multiplication:", arr * 2)
print("Square:", arr ** 2)

# 5. Vectorized Array-to-Array Operation
arr2 = np.array([1, 2, 3, 4, 5, 6])

print("Addition of arrays:", arr + arr2)
print("Multiplication of arrays:", arr * arr2)