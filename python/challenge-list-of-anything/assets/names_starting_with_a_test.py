import sys

sys.path.append("/home/labex/project")

import unittest
from names_starting_with_a import names_starting_with_a


class TestListComprehensions(unittest.TestCase):
    def test_sum_of_cubes(self):
        self.assertEqual(
            names_starting_with_a(["Alice", "Bob", "Charlie", "David", "Eva"]),
            ["Alice"],
        )
        self.assertEqual(names_starting_with_a(["App", "Orange"]), ["App"])


if __name__ == "__main__":
    unittest.main()
