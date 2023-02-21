import sys

sys.path.append("/home/labex/project")

import unittest
from string_manipulation import string_manipulation

class TestStringManipulation(unittest.TestCase):
    def test_string_manipulation(self):
        self.assertEqual(string_manipulation("Hello World"), "dlrow olleh")
        self.assertEqual(string_manipulation("Python"), "nohtyp")
        self.assertEqual(string_manipulation("Data Types"), "setypatad")
        
if __name__ == "__main__":
    unittest.main()