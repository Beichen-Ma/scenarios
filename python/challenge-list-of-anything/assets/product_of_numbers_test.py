import sys

sys.path.append("/home/labex/project")

import unittest
from product_of_numbers import product_of_numbers


class TestListComprehensions(unittest.TestCase):
    def test_sum_of_cubes(self):
        self.assertEqual(product_of_numbers([1, 2], [3, 4]), [3, 8])
        self.assertEqual(
            product_of_numbers([1, 2, 3, 4], [10, 20, 30, 40]), [10, 40, 90, 160]
        )
        self.assertEqual(product_of_numbers([6, 7], [3, 9]), [18, 63])


if __name__ == "__main__":
    unittest.main()
