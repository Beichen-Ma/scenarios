import sys

sys.path.append("/home/project")

import unittest

from flatten_list import flatten_list

def count_lines(file_name: str) -> int:
    with open(file_name, "r") as f:
        lines = f.readlines()
        docstring = False
        count = 0
        for line in lines:
            if line.strip().startswith("\"\"\""):
                docstring = not docstring
                continue
            if not docstring:
                count += 1
        return count

class TestFlattenList(unittest.TestCase):
    def test_file_lines(self):
        self.assertLessEqual(count_lines('flatten_list.py'), 3)

    def test_symbol(self):
        f = open('flatten_list.py', "r").read()
        self.assertNotIn(';', f)
    
    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_flat_list(self):
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])

    def test_nested_list(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4, 5], [6], [], [7, 8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()