import sys

sys.path.append("/home/labex/project")

import unittest
from get_grade import get_grade

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

class TestGetGrade(unittest.TestCase):

    def test_file_lines(self):
        self.assertLessEqual(count_lines('get_grade.py'), 5)    

    def test_symbol(self):
        f = open('get_grade.py', "r").read()
        self.assertNotIn(';', f)

    def test_score_90_to_100(self):
        self.assertEqual(get_grade(90), 'A')
        self.assertEqual(get_grade(100), 'A')

    def test_score_80_to_89(self):
        self.assertEqual(get_grade(80), 'B')
        self.assertEqual(get_grade(89), 'B')

    def test_score_70_to_79(self):
        self.assertEqual(get_grade(70), 'C')
        self.assertEqual(get_grade(79), 'C')

    def test_score_60_to_69(self):
        self.assertEqual(get_grade(60), 'D')
        self.assertEqual(get_grade(69), 'D')

    def test_score_0_to_59(self):
        self.assertEqual(get_grade(0), 'E')
        self.assertEqual(get_grade(59), 'E')

if __name__ == '__main__':
    unittest.main()
