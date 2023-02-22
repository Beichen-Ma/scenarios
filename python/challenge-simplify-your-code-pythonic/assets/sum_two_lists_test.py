import sys

sys.path.append("/home/labex/project")

import unittest

from sum_two_lists import sum_two_lists


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


class TestSumTwoLists(unittest.TestCase):
    
    def test_file_lines(self):
        self.assertLessEqual(count_lines('sum_two_lists.py'), 3)

    def test_symbol(self):
        f = open('sum_two_lists.py', "r").read()
        self.assertNotIn(';', f)

    def test_sum_lists(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        expected_sum_list = [5, 7, 9]
        self.assertEqual(sum_two_lists(list1, list2), expected_sum_list)

        list1 = [0, 0, 0]
        list2 = [0, 0, 0]
        expected_sum_list = [0, 0, 0]
        self.assertEqual(sum_two_lists(list1, list2), expected_sum_list)
        
        list1 = [10, -5, 3, 8]
        list2 = [5, 10, 2, -3]
        expected_sum_list = [15, 5, 5, 5]
        self.assertEqual(sum_two_lists(list1, list2), expected_sum_list)

    

if __name__ == '__main__':
    unittest.main()
