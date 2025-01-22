from typing import List, Callable

def binary_search_iterative(nums: List[int], target: int) -> bool: 
    """Perform an iterative binary search to find the target value in a sorted list.

    Args:
        nums (List[int]): The list of integers, assumed to be sorted in ascending order.
        target (int): The value to search for in the list.

    Returns:
        bool: True if the target value is found in the list, False otherwise.
    """
    l = 0
    r = len(nums) - 1
    
    while l <= r: 
        m = (l + r) // 2
        
        if nums[m] == target: 
            return True
        elif nums[m] < target: 
            l = m + 1  # Search the right half
        else:  # nums[m] > target
            r = m - 1  # Search the left half
    
    return False

def binary_search_recursive(nums: List[int], target: int, l: int = 0, r: int = None) -> bool: 
    """Perform a recursive binary search to find the target value in a sorted list.

    Args:
        nums (List[int]): The list of integers, assumed to be sorted in ascending order.
        target (int): The value to search for in the list.
        l (int, optional): The left index of the current search range (default is 0).
        r (int, optional): The right index of the current search range (default is None, which is set to len(nums)-1).

    Returns:
        bool: True if the target value is found in the list, False otherwise.
    """
    if r is None:  # Initialize r if not provided
        r = len(nums) - 1

    if l > r:  # Base case: invalid range
        return False

    m = (l + r) // 2
        
    if nums[m] == target: 
        return True
    elif nums[m] > target: 
        return binary_search_recursive(nums, target, l, m - 1)  # Search the left half
    else:  # nums[m] < target
        return binary_search_recursive(nums, target, m + 1, r)  # Search the right half


def binary_search_recursive_slice(nums: List[int], target: int) -> bool:
    """Perform a recursive binary search to find the target value in a sorted list.

    Args:
        nums (List[int]): The list of integers, assumed to be sorted in ascending order.
        target (int): The value to search for in the list.

    Returns:
        bool: True if the target value is found in the list, False otherwise.
        
    Note: 
        Modifying this function to return index, is not straightforward.
    """

    if len(nums) == 0:
        return False

    m = len(nums) // 2  # Find the middle element
    
    if nums[m] == target:
        return True
    elif nums[m] > target:
        return binary_search_recursive_slice(nums[:m], target)  # Search the left half
    else:  # nums[m] < target
        return binary_search_recursive_slice(nums[m+1:], target)  # Search the right half



def test_binary_search(binary_search: Callable):
    # Test cases for all binary search methods
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test for valid target at different positions
    assert binary_search(nums, 1) == True  # Target is at the beginning
    assert binary_search(nums, 10) == True  # Target is at the end
    assert binary_search(nums, 5) == True  # Target is in the middle
    assert binary_search(nums, 6) == True  # Target is in the list
    assert binary_search(nums, 7) == True  # Target is towards the end

    # Test for invalid target outside the range of the list
    assert binary_search(nums, 0) == False  # Target is less than all elements
    assert binary_search(nums, 11) == False  # Target is greater than all elements

    # Test for empty list
    assert binary_search([], 6) == False  # Empty list should return False

    # Test for list with only one element
    assert binary_search([5], 5) == True  # Target is the only element
    assert binary_search([5], 4) == False  # Target is less than the only element
    assert binary_search([5], 6) == False  # Target is greater than the only element

    # Test for list with two elements
    assert binary_search([1, 3], 1) == True  # Target is the first element
    assert binary_search([1, 3], 3) == True  # Target is the second element
    assert binary_search([1, 3], 2) == False  # Target is between the elements

    # Test for large list
    large_nums = list(range(1, 10001))  # List from 1 to 10000
    assert binary_search(large_nums, 5000) == True  # Target is in the middle
    assert binary_search(large_nums, 10000) == True  # Target is the last element
    assert binary_search(large_nums, 1) == True  # Target is the first element
    assert binary_search(large_nums, 10001) == False  # Target is greater than all elements

    # Test for negative numbers
    negative_nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    assert binary_search(negative_nums, -10) == True  # Target is the first element
    assert binary_search(negative_nums, -1) == True  # Target is the last element
    assert binary_search(negative_nums, -6) == True  # Target is in the middle
    assert binary_search(negative_nums, 0) == False  # Target is not in the list
    assert binary_search(negative_nums, -11) == False  # Target is less than all elements

    # print(f"All tests passed for {binary_search.__name__}!")

if __name__ == "__main__":
    # Call the test function for each binary search method
    test_binary_search(binary_search_iterative)
    test_binary_search(binary_search_recursive)
    test_binary_search(binary_search_recursive_slice)
