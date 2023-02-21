import sys


sys.path.append("/home/labex/project")


import unittest
from even_numbers import even_numbers


def test_even_numbers(self):
    numbers = [1, 2, 3, 4, 5]
    even_numbers = even_numbers(numbers)
    self.assertEqual(list(even_numbers), [2, 4])


if __name__ == "__main__":
    unittest.main()
