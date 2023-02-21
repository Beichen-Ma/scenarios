import sys

sys.path.append("/home/labex/project")

import unittest
from word_lengths import word_lengths


class TestListComprehensions(unittest.TestCase):
    def test_sum_of_cubes(self):
        self.assertEqual(
            word_lengths(["apple", "banana", "cherry", "date"]), [5, 6, 6, 4]
        )
        self.assertEqual(word_lengths(["Monday", "Tuesday"]), [6, 7])
        self.assertEqual(word_lengths(["hello", "world"]), [5, 5])


if __name__ == "__main__":
    unittest.main()
