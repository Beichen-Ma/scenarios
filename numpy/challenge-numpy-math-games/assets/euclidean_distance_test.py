import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np
from euclidean_distance import euclidean_distance

class TestEuclideanDistance(unittest.TestCase):
    def test_euclidean_distance(self):
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        self.assertAlmostEqual(euclidean_distance(a, b), 5.196152422706632)

        a = np.array([0, 0, 0])
        b = np.array([0, 0, 0])
        self.assertAlmostEqual(euclidean_distance(a, b), 0.0)

        a = np.array([1, 2, 3, 4])
        b = np.array([4, 5, 6])
        self.assertAlmostEqual(euclidean_distance(a, b), 5.916079783099616)

if __name__ == '__main__':
    unittest.main()