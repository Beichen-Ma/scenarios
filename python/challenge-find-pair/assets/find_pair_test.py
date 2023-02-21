import sys

sys.path.append("/home/labex/project")

import unittest

from typing import List, Tuple
from find_pair import find_pair

class TestFindPair(unittest.TestCase):
    def test_find_pair(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(find_pair(nums, target), (0, 1))

        nums = [3, 2, 4]
        target = 6
        self.assertEqual(find_pair(nums, target), (1, 2))

        nums = [3, 3]
        target = 6
        self.assertEqual(find_pair(nums, target), (0, 1))

        nums = [1, 2, 3, 4, 5]
        target = 10
        self.assertEqual(find_pair(nums, target), ())

if __name__ == '__main__':
    unittest.main()