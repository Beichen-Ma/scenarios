import sys

sys.path.append("/home/labex/project")

import unittest
from date_flip import date_flip


class TestDateFlip(unittest.TestCase):
    def test_date_flip(self):
        date_str = "2020-10-01"
        result = date_flip(date_str)
        self.assertEqual(result, "01-10-2020")

        date_str = "2021-07-12"
        result = date_flip(date_str)
        self.assertEqual(result, "12-07-2021")

        date_str = "1999-12-31"
        result = date_flip(date_str)
        self.assertEqual(result, "31-12-1999")


if __name__ == "__main__":
    unittest.main()
