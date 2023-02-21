import sys

sys.path.append("/home/labex/project")

import unittest
from square_of_numbers import square_of_numbers


class TestListComprehensions(unittest.TestCase):
    def test_sum_of_cubes(self):
        self.assertEqual(square_of_numbers([1, 4]), [1, 16])
        self.assertEqual(
            square_of_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
        )
        self.assertEqual(square_of_numbers([10, 15]), [100, 225])


if __name__ == "__main__":
    unittest.main()
