import sys

sys.path.append("/home/labex/project")

import unittest
from sum_of_fibonacci import sum_of_fibonacci


class TestMathOperators(unittest.TestCase):
    def test_sum_of_fibonacci(self):
        self.assertEqual(sum_of_fibonacci(0), 0)
        self.assertEqual(sum_of_fibonacci(1), 1)
        self.assertEqual(sum_of_fibonacci(5), 7)
        self.assertEqual(sum_of_fibonacci(10), 88)
        self.assertEqual(sum_of_fibonacci(20), 10945)


if __name__ == "__main__":
    unittest.main()
