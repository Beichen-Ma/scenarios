import sys

sys.path.append("/home/labex/project")

import unittest
from even_numbers import even_numbers


class TestListComprehensions(unittest.TestCase):
    def test_sum_of_cubes(self):
        self.assertEqual(even_numbers([1, 2, 3, 4]), [2, 4])
        self.assertEqual(even_numbers([2, 6, 7, 3, 1, 8]), [2, 6, 8])
        self.assertEqual(
            even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 4, 6, 8, 10]
        )


if __name__ == "__main__":
    unittest.main()
