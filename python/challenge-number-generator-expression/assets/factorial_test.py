import sys


sys.path.append("/home/labex/project")


import unittest
from factorial import factorial


def test_factorial(self):
    n = 5
    factorials = factorial(n)
    self.assertEqual(list(factorials), [1, 2, 6, 24, 120])


if __name__ == "__main__":
    unittest.main()
