import random
from typing import List

LIST_SIZE = 10_000_000

def sequential_search(nums: List[int], target: int, is_ordered: bool = False) -> bool:
    """
    Perform a sequential search to check if a target value exists in a list.

    Parameters:
        nums (List[int]): The list of integers to search within.
        k (int): The target value to search for.
        is_ordered (bool, optional): 
            - If True, assumes the list is sorted in ascending order and enables early termination.
            - Defaults to False, treating the list as unordered.

    Returns:
        bool: 
            - True if the target value `k` is found in the list.
            - False otherwise.
    """
    for num in nums:
        if num == target:
            return True
        elif is_ordered and num > target: 
            return False
    return False

# Test cases
test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))  # Expected: False
print(sequential_search(test_list, 13))  # Expected: True

# Performance test with large list
large_list = random.sample(range(LIST_SIZE * 2), LIST_SIZE)
print(sequential_search(large_list, -1))  # Expected: False (very unlikely)
