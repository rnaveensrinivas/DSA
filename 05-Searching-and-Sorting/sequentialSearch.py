from typing import List, Callable
import random

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


LIST_SIZE = 100_000

def test_sequential_search(sequential_search: Callable):
    # Test cases for the sequential_search method
    test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    
    # Test for valid targets in the list
    assert sequential_search(test_list, 13) == True  # Target exists in the list
    assert sequential_search(test_list, 32) == True  # Target exists in the list
    assert sequential_search(test_list, 19) == True  # Target exists in the list

    # Test for invalid target not in the list
    assert sequential_search(test_list, 3) == False  # Target does not exist
    assert sequential_search(test_list, 99) == False  # Target does not exist
    
    # Test with an empty list
    assert sequential_search([], 10) == False  # Empty list should return False

    # Test with list containing a single element
    assert sequential_search([10], 10) == True  # List with the target
    assert sequential_search([5], 10) == False  # List with a non-target

    # Test with an ordered list
    ordered_list = [1, 2, 5, 7, 8, 10, 15, 20]
    assert sequential_search(ordered_list, 7, is_ordered=True) == True  # Target exists
    assert sequential_search(ordered_list, 10, is_ordered=True) == True  # Target exists
    assert sequential_search(ordered_list, 4, is_ordered=True) == False  # Target does not exist
    assert sequential_search(ordered_list, 25, is_ordered=True) == False  # Target is larger than all elements

    # Test for large list
    large_list = random.sample(range(LIST_SIZE * 2), LIST_SIZE)
    assert sequential_search(large_list, -1) == False # will not find -1

    # Test for performance
    large_list_sorted = list(range(LIST_SIZE))  # Sorted list from 0 to 9,999,999
    assert sequential_search(large_list_sorted, LIST_SIZE - 1, is_ordered=True) == True  # Last element in a sorted list
    assert sequential_search(large_list_sorted, LIST_SIZE + 1, is_ordered=True) == False  # Element not in the list

    # Test for repeated elements in the list
    repeated_list = [1] * 1000 + [2] * 1000 + [3] * 1000  # List with repeated values
    assert sequential_search(repeated_list, 2) == True  # Should find the element
    assert sequential_search(repeated_list, 4) == False  # Should not find the element

    # print(f"All tests passed for {sequential_search.__name__}!")

if __name__ == "__main__":
    # Call the test function
    test_sequential_search(sequential_search)

