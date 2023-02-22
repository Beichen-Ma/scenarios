import sys

sys.append('/home/project')

import os
import unittest
from folder_create import folder_create


class TestFolderCreate(unittest.TestCase):

    def test_folder_already_exists(self):
        folder_name = "test_folder"
        os.mkdir(folder_name)
        self.assertTrue(os.path.isdir(folder_name))
        folder_create(folder_name)
        self.assertTrue(os.path.isdir(folder_name))
        os.rmdir(folder_name)

    def test_folder_create(self):
        folder_name = "test_folder"
        if os.path.isdir(folder_name):
            os.rmdir(folder_name)
        self.assertFalse(os.path.isdir(folder_name))
        folder_create(folder_name)
        self.assertTrue(os.path.isdir(folder_name))
        os.rmdir(folder_name)


if __name__ == '__main__':
    unittest.main()