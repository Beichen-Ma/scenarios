import sys


sys.path.append("/home/labex/project")


import unittest
from running_total import running_total


def test_running_total(self):
    numbers = [1, 2, 3, 4, 5]
    running_totals = running_total(numbers)
    self.assertEqual(list(running_totals), [1, 3, 6, 10, 15])


if __name__ == "__main__":
    unittest.main()
