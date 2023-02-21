import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np
from multiply_arrays import multiply_arrays


class TestMultiplyArrays(unittest.TestCase):
    def test_multiply_arrays_1d(self):
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        result = multiply_arrays(a, b)
        expected = np.array([4, 10, 18])
        np.testing.assert_array_equal(result, expected)

    def test_multiply_arrays_2d(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[5, 6], [7, 8]])
        result = multiply_arrays(a, b)
        expected = np.array([[5, 12], [21, 32]])
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()