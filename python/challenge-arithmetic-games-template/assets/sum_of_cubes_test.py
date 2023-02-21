import sys

sys.path.append("/home/labex/project")

import unittest
from sum_of_cubes import sum_of_cubes


class TestMathOperators(unittest.TestCase):
    def test_sum_of_cubes(self):
        self.assertEqual(sum_of_cubes(5), 225)
        self.assertEqual(sum_of_cubes(10), 3025)
        self.assertEqual(sum_of_cubes(20), 44100)


if __name__ == "__main__":
    unittest.main()
