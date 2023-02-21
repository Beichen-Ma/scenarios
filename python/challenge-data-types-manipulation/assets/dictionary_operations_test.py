import sys

sys.path.append("/home/labex/project")

import unittest
from dictionary_operations import dictionary_operations

class TestDictionaryOperations(unittest.TestCase):
    def test_dictionary_operations(self):
        self.assertEqual(dictionary_operations({"key1": "value1", "key2": "value2"}), 
                         {"key1": "value1", "key2": "value2", "new_key": "new_value"})
        self.assertEqual(dictionary_operations({"key1": "value1", "remove_key": "value2"}), 
                         {"key1": "value1"})
        self.assertEqual(dictionary_operations({}), {"new_key": "new_value"})
        
if __name__ == "__main__":
    unittest.main()