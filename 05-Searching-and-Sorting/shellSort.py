from typing import List, Callable

def shell_sort(nums: List[int]) -> None: 
    """Sort the list of integers using shell sort, inplace.
    
    Note: 
        Shell sort is not stable. 
    
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
        

def shell_sort_using_insertion_sort(nums: List[int]) -> None:
    """
    Sorts a list of integers in place using the Shell sort algorithm.

    Shell sort is an optimized version of insertion sort that works by
    sorting elements far apart first and progressively reducing the gap
    between elements to be compared. This approach helps reduce the number
    of overall comparisons and shifts required compared to standard insertion sort.

    Args:
        nums (List[int]): The list of integers to be sorted.
    """
    n = len(nums)
    gap = n // 2  # Initial gap size

    # Gradually reduce the gap size until it becomes 0
    while gap > 0:
        # Perform gap insertion sort for each sublist
        for start_pos in range(gap):
            gap_insertion_sort(nums, start_pos, gap)

        gap //= 2  # Reduce the gap size
        # When gap == 1, the algorithm performs a standard insertion sort


def gap_insertion_sort(nums: List[int], start: int = 0, gap: int = 1) -> None:
    """
    Generalized insertion sort that supports a custom starting index and gap.

    If `start = 0` and `gap = 1`, this function behaves as a standard insertion sort.
    It can also be used as a subroutine in Shell sort, where the gap decreases over time.

    Args:
        nums (List[int]): The list of integers to sort.
        start (int, optional): The starting index for the sort. Defaults to 0.
        gap (int, optional): The gap between elements to compare and sort. Defaults to 1.
    """
    # Traverse the list starting from the specified index and gap
    for i in range(start + gap, len(nums), gap):
        current_num = nums[i]  # The element to be inserted in the sorted portion
        j = i - gap

        # Shift elements of the sorted portion to the right to make room
        while j >= start and nums[j] > current_num:
            nums[j + gap] = nums[j]
            j -= gap

        # Place the current element in its correct position
        nums[j + gap] = current_num
    
    
def test_shell_sort(shell_sort: Callable = shell_sort):
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


test_shell_sort(shell_sort)
test_shell_sort(shell_sort_using_insertion_sort)
