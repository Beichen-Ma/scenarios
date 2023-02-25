import sys

sys.path.append("/home/labex/project")

import unittest
import multiprocessing
import random
from typing import List
from sum_multiprocessing import sum_multiprocessing

def compute_sum(data: List[int]) -> int:
    """Computes the sum of a list of integers."""
    return sum(data)

class TestMultiprocessing(unittest.TestCase):
    def test_sum_multiprocessing(self):
        data = [random.randint(1, 100) for _ in range(1000000)]
        parts = 4
        chunk_size = len(data) // parts
        
        results = sum_multiprocessing(data, parts, chunk_size)
        
        total_sum = sum(result.get() for result in results)
        
        self.assertEqual(total_sum, sum(data), 'Incorrect sum computed.')

if __name__ == '__main__':
    unittest.main()