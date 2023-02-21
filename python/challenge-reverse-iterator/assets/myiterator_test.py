import sys

sys.path.append("/home/labex/project")


from myiterator import MyIterator

import unittest
class TestMyIterator(unittest.TestCase):
    def test_iterator(self):
        it = MyIterator(2, 5)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 3)
        self.assertEqual(next(it), 4)
        self.assertEqual(next(it), 5)
        self.assertEqual(next(it), None)

    def test_empty_iterator(self):
        it = MyIterator(0, 0)
        self.assertEqual(next(it), 0)
        self.assertEqual(next(it), None)

if __name__ == '__main__':
    unittest.main()