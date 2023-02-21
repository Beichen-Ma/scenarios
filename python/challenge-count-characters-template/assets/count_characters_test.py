import sys


sys.path.append("/home/labex/project")


import inspect
import unittest
from count_characters import count_characters


class TestCountCharacters(unittest.TestCase):
    def test_documentation(self):
        # Check that the function has a docstring
        self.assertIsNotNone(count_characters.__doc__)

        # Check that the docstring includes information about the parameters
        self.assertIn("str", count_characters.__doc__)

        # Check that the docstring includes information about the return value
        self.assertIn("dict", count_characters.__doc__)

    def test_code_comments(self):
        # Check that the function has comments explaining what is being done
        function_code = inspect.getsource(count_characters)
        self.assertNotEqual(function_code.find("# "), -1)


if __name__ == "__main__":
    unittest.main()
