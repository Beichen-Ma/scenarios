import sys

sys.path.append("/home/labex/project")

import unittest
from reverseiterator import ReverseIterator

class TestReverseIterator(unittest.TestCase):
    def test_iterator(self):
        it = ReverseIterator([1, 2, 3, 4, 5])
        self.assertEqual(next(it), 5)
        self.assertEqual(next(it), 4)
        self.assertEqual(next(it), 3)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), None)

    def test_empty_iterator(self):
        it = ReverseIterator([])
        self.assertEqual(next(it), None)

if __name__ == '__main__':
    unittest.main()