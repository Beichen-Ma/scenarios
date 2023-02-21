import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np
from transpose_array import transpose_array

class TestTransposeArray(unittest.TestCase):
    def test_transpose_array_2d(self):
        a = np.array([[1, 2], [3, 4]])
        result = transpose_array(a)
        expected = np.array([[1, 3], [2, 4]])
        np.testing.assert_array_equal(result, expected)

    def test_transpose_array_3d(self):
        a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        result = transpose_array(a)
        expected = np.array([[[1, 5], [3, 7]], [[2, 6], [4, 8]]])
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()