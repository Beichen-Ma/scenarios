import sys

sys.path.append("/home/labex/project")

import unittest
from list_operations import list_operations

class TestListOperations(unittest.TestCase):
    def test_list_operations(self):
        self.assertEqual(list_operations([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(list_operations([6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(list_operations([1, 2, 2, 3, 4, 4, 5, 6, 6]), [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()