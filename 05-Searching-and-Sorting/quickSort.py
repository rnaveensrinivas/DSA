from typing import List, Callable

def quick_sort(nums: List[int], l: int = 0, r: int = None) -> None:
    """Sort the given list of integers using quick sort, in-place.
    
    Args: 
        nums: List of integers that need to be sorted.
        l: Left marker, defaults to 0.
        r: Right marker, defaults to len(nums) - 1.
    """
    
    if r is None: 
        r = len(nums) - 1  # Default the right marker if it's not passed.
        
    if l >= r:  # Base case: if the sublist has one or no elements.
        return
    
    pivot = nums[l]  # Use the leftmost element as the pivot
    i, j = l + 1, r
    
    while True:
        while i <= r and nums[i] <= pivot:  # Increment i until a value greater than the pivot is found.
            i += 1
        while nums[j] >= pivot and j > l:  # Decrement j until a value less than the pivot is found.
            j -= 1
        
        if i > j:  # If the indices cross, stop the loop.
            break
        else:  # Otherwise, swap the elements at i and j.
            nums[i], nums[j] = nums[j], nums[i]
    
    # Place the pivot in the correct position.
    nums[l], nums[j] = nums[j], nums[l]
    
    # Recursively sort the two partitions.
    quick_sort(nums, l, j - 1)  # Sort left partition.
    quick_sort(nums, j + 1, r)  # Sort right partition.


def test_quick_sort():
    # Test 1: General test case
    nums = [64, 34, 25, 12, 22, 11, 90]
    quick_sort(nums)
    assert nums == [11, 12, 22, 25, 34, 64, 90], f"Test 1 failed: {nums}"

    # Test 2: Empty list
    nums = []
    quick_sort(nums)
    assert nums == [], f"Test 2 failed: {nums}"

    # Test 3: Single-element list
    nums = [42]
    quick_sort(nums)
    assert nums == [42], f"Test 3 failed: {nums}"

    # Test 4: Already sorted list
    nums = [1, 2, 3, 4, 5]
    quick_sort(nums)
    assert nums == [1, 2, 3, 4, 5], f"Test 4 failed: {nums}"

    # Test 5: Reverse-sorted list
    nums = [5, 4, 3, 2, 1]
    quick_sort(nums)
    assert nums == [1, 2, 3, 4, 5], f"Test 5 failed: {nums}"

    # Test 6: List with duplicates
    nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    quick_sort(nums)
    assert nums == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9], f"Test 6 failed: {nums}"

    # Test 7: Large numbers
    nums = [1000000, 500000, 2000000, 0, -1000000]
    quick_sort(nums)
    assert nums == [-1000000, 0, 500000, 1000000, 2000000], f"Test 7 failed: {nums}"

    # Test 8: List with negative numbers
    nums = [-1, -5, -3, -4, -2]
    quick_sort(nums)
    assert nums == [-5, -4, -3, -2, -1], f"Test 8 failed: {nums}"

    # Test 9: List with all equal elements
    nums = [7, 7, 7, 7, 7]
    quick_sort(nums)
    assert nums == [7, 7, 7, 7, 7], f"Test 9 failed: {nums}"

    # Test 10: Larger random list
    nums = [12, 9, 23, 4, 56, 78, 3, 2, 90]
    quick_sort(nums)
    assert nums == [2, 3, 4, 9, 12, 23, 56, 78, 90], f"Test 10 failed: {nums}"

if __name__ == "__main__":  
    test_quick_sort()