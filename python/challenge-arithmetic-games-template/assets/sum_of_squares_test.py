import sys

sys.path.append("/home/labex/project")

import unittest
from sum_of_squares import sum_of_squares


class TestMathOperators(unittest.TestCase):
    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(5), 55)
        self.assertEqual(sum_of_squares(10), 385)
        self.assertEqual(sum_of_squares(20), 2870)


if __name__ == "__main__":
    unittest.main()
