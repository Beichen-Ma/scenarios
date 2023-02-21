import sys


sys.path.append("/home/labex/project")


import unittest
from square_numbers import square_numbers


class TestGeneratorExpressions(unittest.TestCase):
    def test_square_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        squared_numbers = square_numbers(numbers)
        self.assertEqual(list(squared_numbers), [1, 4, 9, 16, 25])


if __name__ == "__main__":
    unittest.main()
