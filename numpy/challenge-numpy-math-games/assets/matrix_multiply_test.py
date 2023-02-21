import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np
from matrix_multiply import matrix_multiply

class TestMatrixMultiply(unittest.TestCase):
    def test_matrix_multiply_2d(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[5, 6], [7, 8]])
        result = matrix_multiply(a, b)
        expected = np.array([[19, 22], [43, 50]])
        np.testing.assert_array_equal(result, expected)

    def test_matrix_multiply_1d_2d(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([5, 6])
        result = matrix_multiply(a, b)
        expected = np.array([17, 39])
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()