import sys

sys.path.append("/home/project")

import unittest
from sum_n import sum_n

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

class TestSumN(unittest.TestCase):

    def test_file_lines(self):
        self.assertLessEqual(count_lines('sum_n.py'), 3)

    def test_symbol(self):
        f = open('sum_n.py', "r").read()
        self.assertNotIn(';', f)
    
    def test_sum_n(self):
        self.assertEqual(sum_n(0), 0)
        self.assertEqual(sum_n(1), 0)
        self.assertEqual(sum_n(2), 1)
        self.assertEqual(sum_n(3), 3)
        self.assertEqual(sum_n(10), 45)

if __name__ == '__main__':
    unittest.main()
