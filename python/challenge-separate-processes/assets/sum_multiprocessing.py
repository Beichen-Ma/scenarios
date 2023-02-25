import multiprocessing
import random
from typing import List

def compute_sum(data: List[int]) -> int:
    """Computes the sum of a list of integers."""
    return sum(data)

def sum_multiprocessing(data: List[int], parts: int, chunk_size: int) -> List[int]:
    # TODO: implement this function
    # Note: Do not change the existing code
    return results

if __name__ == '__main__':
    data = [random.randint(1, 100) for _ in range(1000000)]
    parts = 4
    chunk_size = len(data) // parts
    
    results = sum_multiprocessing(data, parts, chunk_size)
    
    total_sum = sum(result.get() for result in results)
    
    print(f'Total sum: {total_sum}')