import sys


sys.path.append("/home/labex/project")


import unittest
from fibonacci import fibonacci


def test_fibonacci(self):
    n = 5
    fibonacci_numbers = fibonacci(n)
    self.assertEqual(list(fibonacci_numbers), [0, 1, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()
