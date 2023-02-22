import sys

sys.path.append("/home/project")

import unittest
from concat_strings import concat_strings


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

class TestConcatStrings(unittest.TestCase):
    def test_file_lines(self):
        self.assertLessEqual(count_lines('concat_strings.py'), 3)

    def test_symbol(self):
        f = open('concat_strings.py', "r").read()
        self.assertNotIn(';', f)

    def test_concat_strings(self):
        strings = ['Hello', 'World']
        result = concat_strings(strings)
        self.assertEqual(result, 'HelloWorld')

        strings = ['This', 'is', 'a', 'test']
        result = concat_strings(strings)
        self.assertEqual(result, 'Thisisatest')

        strings = []
        result = concat_strings(strings)
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()
