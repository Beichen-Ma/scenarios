import sys

sys.append('/home/labex/project')

import os
import shutil
import tempfile
import unittest

from folder_delete import folder_delete

class TestFolderDelete(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_folder = os.path.join(self.test_dir, "test_folder")
        os.mkdir(self.test_folder)
        self.test_file = os.path.join(self.test_folder, "test_file.txt")
        with open(self.test_file, "w") as f:
            f.write("test file content")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_folder_delete(self):
        self.assertTrue(os.path.isdir(self.test_folder))
        file_count = folder_delete(self.test_folder)
        self.assertFalse(os.path.isdir(self.test_folder))
        self.assertEqual(file_count, 1)

    def test_folder_delete_not_exist(self):
        nonexistent_folder = os.path.join(self.test_dir, "nonexistent_folder")
        self.assertFalse(os.path.isdir(nonexistent_folder))
        file_count = folder_delete(nonexistent_folder)
        self.assertEqual(file_count, 0)

if __name__ == '__main__':
    unittest.main()