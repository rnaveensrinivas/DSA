from typing import List

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
