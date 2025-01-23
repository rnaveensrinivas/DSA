from typing import List, Callable
from insertionSort import insertion_sort

PARTITION_LIMIT = 64

def quick_sort(nums: List[int], l: int = 0, r: int = None,
               use_median_of_three: bool = True,
               use_insertion_sort: bool = True,
               partition_limit: int = PARTITION_LIMIT) -> None:
    """
    Sort the given list of integers using the quick sort algorithm, in-place.

    Quick sort is a divide-and-conquer algorithm that partitions the list into two
    sublists around a pivot element, recursively sorting each sublist. It selects a pivot 
    and partitions the list such that all elements less than the pivot are placed to the left 
    and all elements greater than the pivot are placed to the right. The process is repeated 
    recursively for each sublist.

    The pivot selection can be done using:
    - The leftmost element of the sublist (default behavior).
    - The median of the first, middle, and last elements of the sublist (when `use_median_of_three` is `True`).

    This version of quick sort is **not stable** as it does not preserve the relative order of elements 
    with equal values.

    Additionally, for sublists smaller than a specified `partition_limit`, Insertion Sort is used 
    instead of Quick Sort if `use_insertion_sort` is set to `True`. The partitioning limit is controlled 
    by the `partition_limit` parameter, which defaults to `PARTITION_LIMIT`.

    Args:
        nums (List[int]): The list of integers to sort.
        l (int, optional): The leftmost index of the current sublist. Defaults to 0.
        r (int, optional): The rightmost index of the current sublist. Defaults to len(nums) - 1.
        use_median_of_three (bool, optional): Determines whether to use the median of three rule 
                                               for pivot selection. Defaults to True.
        use_insertion_sort (bool, optional): Determines whether to use Insertion Sort for small sublists. 
                                              Defaults to True.
        partition_limit (int, optional): The size threshold below which Insertion Sort is used. 
                                          Defaults to `PARTITION_LIMIT`.

    Returns:
        None: The function sorts the list in-place.
    """
    if r is None:
        r = len(nums) - 1  # Default the right marker to the last index.
    
    if l >= r:
        return  # Base case: sublist with one or no elements is already sorted.
    
    if use_insertion_sort and len(nums) <= partition_limit: 
        # perform insertion sort
        insertion_sort(nums)
    else: 
        # perform quick sort
        
        # Partition the list and get the pivot index.
        split_index = partition(nums, l, r, use_median_of_three)
        
        # Recursively sort the sublists before and after the pivot.
        quick_sort(nums, l, split_index - 1, use_median_of_three)
        quick_sort(nums, split_index + 1, r, use_median_of_three)


def median_of_three(nums: List[int], l: int, m: int, r: int) -> int:
    """
    Select the median of three elements from the list: the first, middle, and last element.

    Args:
        nums (List[int]): The list of integers.
        l (int): Index of the first element.
        m (int): Index of the middle element.
        r (int): Index of the last element.

    Returns:
        int: The index of the median element among nums[l], nums[m], and nums[r].
    """
    # Create a list of tuples with (value, index) for the three candidates
    possible_pivots = [(nums[l], l), (nums[m], m), (nums[r], r)]
    # Sort based on the values and select the middle one
    median = sorted(possible_pivots)[1]
    return median[1]  # Return the index of the median element


def partition(nums: List[int], l: int, r: int, 
              use_median_of_three: bool = True) -> int:
    """
    Partition the list into two parts: elements less than or equal to the pivot
    on the left, and elements greater than the pivot on the right.
    
    If `use_median_of_three` is True, the pivot is chosen as the median of the first,
    middle, and last elements. Otherwise, the pivot is selected as the leftmost element.

    Args:
        nums (List[int]): The list to partition.
        l (int): The starting index of the sublist.
        r (int): The ending index of the sublist.
        use_median_of_three (bool): Whether to use the median-of-three rule for pivot selection.
                                    Default is True, meaning the median of the first, middle, and last elements will be used.
                                    If False, the leftmost element (nums[l]) will be used as the pivot.
    
    Returns:
        int: The index of the pivot after partitioning.
    """
    if use_median_of_three: 
        pivot_index = median_of_three(nums, l, (l + r) // 2, r)
        pivot = nums[pivot_index]  # Get the pivot value
    else: 
        pivot_index = l
        pivot = nums[l]

    # Swap the pivot to the start of the list for simplicity
    nums[pivot_index], nums[l] = nums[l], nums[pivot_index]
    pivot_index = l  # Update pivot index to the start
    i = l + 1        # Pointer for the left partition
    j = r            # Pointer for the right partition

    while True:
        # Move `i` to the right while elements are <= pivot
        while i <= r and nums[i] <= pivot:
            i += 1
        
        # Move `j` to the left while elements are > pivot
        while nums[j] > pivot:
            j -= 1

        if i > j:  # If pointers cross, the partitioning is done
            break

        # Swap elements at `i` and `j` to maintain partition order
        nums[i], nums[j] = nums[j], nums[i]

    # Place the pivot in its correct position by swapping with `nums[j]`
    nums[pivot_index], nums[j] = nums[j], nums[pivot_index]

    return j  # Return the final position of the pivot


def quick_sort_(nums: List[int], l: int = 0, r: int = None) -> None:
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
    i, j = l, r
    
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
    quick_sort_(nums, l, j - 1)  # Sort left partition.
    quick_sort_(nums, j + 1, r)  # Sort right partition.


def test_quick_sort(quick_sort: Callable[[List[int]], None]) -> None:
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

test_quick_sort(quick_sort)
test_quick_sort(quick_sort_)