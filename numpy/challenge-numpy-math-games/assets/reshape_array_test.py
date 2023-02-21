import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np
from reshape_array import reshape_array

class TestReshapeArray(unittest.TestCase):
    def test_reshape_array_1d_to_2d(self):
        a = np.array([1, 2, 3, 4, 5, 6])
        shape = (2, 3)
        result = reshape_array(a, shape)
        expected = np.array([[1, 2, 3], [4, 5, 6]])
        np.testing.assert_array_equal(result, expected)

    def test_reshape_array_2d_to_1d(self):
        a = np.array([[1, 2], [3, 4]])
        shape = (4,)
        result = reshape_array
        a = np.array([[1, 2], [3, 4]])
        shape = (4,)
        result = reshape_array(a, shape)
        expected = np.array([1, 2, 3, 4])
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()