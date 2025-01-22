from typing import List

def shell_sort(nums: List[int]) -> None: 
    """Sort the list of integers using shell sort, inplace
    
    Args: 
        nums: List of itegers that needs to be sorted.
    """
    
    n = len(nums)
    # gap determines the distance between elements in the sublists to be sorted.
    gap = n // 2
    
    while gap > 0: 
        # perform insertion sort for this gap size
        
        for i in range(gap, n):
            temp = nums[i]
            j = i
            
            while j >= gap and nums[j - gap] > temp: 
                nums[j] = nums[j - gap]
                j -= gap
            
            nums[j] = temp
            
        gap //= 2
        # gap is reduced until it reaches 1, 
        # where it performs a standard insertion sort.
        
    
def test_shell_sort():
    """Test the shell_sort function with various cases."""
    # Case 1: Standard unsorted list
    nums = [64, 34, 25, 12, 22, 11, 90]
    shell_sort(nums)
    assert nums == [11, 12, 22, 25, 34, 64, 90], f"Failed: {nums}"

    # Case 2: Already sorted list
    nums = [1, 2, 3, 4, 5]
    shell_sort(nums)
    assert nums == [1, 2, 3, 4, 5], f"Failed: {nums}"

    # Case 3: Reverse sorted list
    nums = [5, 4, 3, 2, 1]
    shell_sort(nums)
    assert nums == [1, 2, 3, 4, 5], f"Failed: {nums}"

    # Case 4: List with duplicate elements
    nums = [4, 2, 4, 3, 2, 1]
    shell_sort(nums)
    assert nums == [1, 2, 2, 3, 4, 4], f"Failed: {nums}"

    # Case 5: Single element list
    nums = [42]
    shell_sort(nums)
    assert nums == [42], f"Failed: {nums}"

    # Case 6: Empty list
    nums = []
    shell_sort(nums)
    assert nums == [], f"Failed: {nums}"

    # Case 7: Large list
    nums = [i for i in range(1000, 0, -1)]  # Reverse order
    shell_sort(nums)
    assert nums == [i for i in range(1, 1001)], f"Failed: {nums}"

    # Case 8: List with negative numbers
    nums = [3, -1, -7, 8, 0, 5]
    shell_sort(nums)
    assert nums == [-7, -1, 0, 3, 5, 8], f"Failed: {nums}"


if __name__ == "__main__": 
    # Run the tests
    test_shell_sort()
