import sys

sys.append('/home/project')

import os
import shutil
import tempfile
import unittest

from file_move import file_move

class TestFileMove(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_file_move(self):
        # create a test file
        test_file_path = os.path.join(self.test_dir, "test_file.txt")
        with open(test_file_path, "w") as f:
            f.write("test file content")
        self.assertTrue(os.path.isfile(test_file_path))

        # move the test file to a test folder
        test_folder_path = os.path.join(self.test_dir, "test_folder")
        self.assertFalse(os.path.isdir(test_folder_path))
        file_move(test_file_path, test_folder_path)
        self.assertFalse(os.path.isfile(test_file_path))
        self.assertTrue(os.path.isfile(os.path.join(test_folder_path, "test_file.txt")))

    def test_file_move_file_not_exist(self):
        # try to move a non-existent file to a test folder
        test_file_path = os.path.join(self.test_dir, "nonexistent_file.txt")
        test_folder_path = os.path.join(self.test_dir, "test_folder")
        self.assertFalse(os.path.isfile(test_file_path))
        self.assertFalse(os.path.isdir(test_folder_path))
        file_move(test_file_path, test_folder_path)
        self.assertFalse(os.path.isfile(os.path.join(test_folder_path, "nonexistent_file.txt")))

    def test_file_move_folder_not_exist(self):
        # try to move a test file to a non-existent folder
        test_file_path = os.path.join(self.test_dir, "test_file.txt")
        with open(test_file_path, "w") as f:
            f.write("test file content")
        test_folder_path = os.path.join(self.test_dir, "nonexistent_folder")
        self.assertTrue(os.path.isfile(test_file_path))
        self.assertFalse(os.path.isdir(test_folder_path))
        file_move(test_file_path, test_folder_path)
        self.assertFalse(os.path.isfile(test_file_path))
        self.assertTrue(os.path.isfile(os.path.join(test_folder_path, "test_file.txt")))

if __name__ == '__main__':
    unittest.main()