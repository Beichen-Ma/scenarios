# Linear Algebra with NumPy

NumPy has a comprehensive set of functions for linear algebra operations. Here are a few examples:

## Open the Python Shell

Open the Python shell by typing the following command in the terminal.

```bash
python3
```

## Dot Product

The dot product of two arrays can be calculated using `np.dot()` function. The dot product of two arrays A and B is defined as the sum of the product of corresponding elements of A and B.

```python
import numpy as np

# create two arrays
a = np.array([1, 2])
b = np.array([3, 4])

# calculate dot product
dot_product = np.dot(a, b)

print(dot_product) # Output: 11
```

## Matrix Multiplication

Matrix multiplication can be performed using the `@` operator or the `np.matmul()` function.

Please read the following examples carefully.

```python
# create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# matrix multiplication
C = A @ B

print(C) # Output: [[19 22], [43 50]]
```

You can also get the results in another way.

```python
# create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# matrix multiplication
C = np.matmul(A,B)

print(C) # Output: [[19 22], [43 50]]
```

## Determinant and Inverse

The determinant and inverse of a matrix can be calculated using `np.linalg.det()` and `np.linalg.inv()` functions respectively.

```python
# create a matrix
A = np.array([[1, 2], [3, 4]])

# calculate determinant and inverse
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)

print(det_A) # Output: -2.0
print(inv_A) # Output: [[-2.   1. ], [ 1.5 -0.5]]
```

## Exercise

Now it's your turn to construct two arrays and use the `np.dot()` function to calculate the dot product. Use `@` or `np.matmul()`to calculate matrix multiplication and use `np.linalg.det()`and `np.linalg.inv()`functions to calculate matrix determinant and inverse matrix.S
