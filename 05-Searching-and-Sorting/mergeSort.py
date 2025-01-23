from typing import List, Callable

def merge_sort_slice(nums: List[int]) -> None:
    """
    Sorts a list of integers in-place using the merge sort algorithm with slicing.
    
    Merge sort is a divide-and-conquer algorithm that recursively splits the list
    into halves, sorts each half, and merges them back together.

    Args:
        nums (List[int]): The list of integers to sort.
    """
    if len(nums) <= 1:
        return  # A single-element list is already sorted
    
    # Divide the list into two halves
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    
    # Recursively sort each half
    merge_sort_slice(left)
    merge_sort_slice(right)
    
    # Merge the two sorted halves
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # makes the sort stable.
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements from left or right
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1


def merge_sort_index(nums: List[int], l: int = 0, r: int = None) -> None:
    """
    Sorts a list of integers in-place using the merge sort algorithm with indices.
    
    Merge sort is a divide-and-conquer algorithm that recursively splits the list
    into halves (using indices), sorts each half, and merges them back together.

    Args:
        nums (List[int]): The list of integers to sort.
        l (int, optional): The starting index of the sublist to sort. Defaults to 0.
        r (int, optional): The ending index of the sublist to sort. Defaults to the last index.
    """
    if r is None:
        r = len(nums) - 1
    
    if l >= r:
        return  # Base case: A single element or empty range is already sorted

    # Divide the list into two halves
    mid = (l + r) // 2
    merge_sort_index(nums, l, mid)
    merge_sort_index(nums, mid + 1, r)
    
    # Merge the two sorted halves
    temp = []
    i, j = l, mid + 1
    while i <= mid and j <= r:
        if nums[i] <= nums[j]: # makes the sort stable. 
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1

    # Copy remaining elements from the left or right half
    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= r:
        temp.append(nums[j])
        j += 1

    # Place sorted elements back into the original list
    nums[l:r + 1] = temp


def test_merge_sort(merge_sort: Callable[[List[int]], None]) -> None:
    """
    Tests a merge sort function using various test cases to ensure correctness.

    Args:
        merge_sort (Callable[[List[int]], None]): The merge sort function to test.
    """
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),  # Standard unsorted list
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),                            # Already sorted list
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),                            # Reverse sorted list
        ([4, 2, 4, 3, 2, 1], [1, 2, 2, 3, 4, 4]),                      # List with duplicates
        ([42], [42]),                                                  # Single element list
        ([], []),                                                      # Empty list
        ([3, -1, -7, 8, 0, 5], [-7, -1, 0, 3, 5, 8]),                  # List with negative numbers
        ([i for i in range(1000, 0, -1)], [i for i in range(1, 1001)]),# Large list in reverse order
        ([0, 0, 0, 0], [0, 0, 0, 0]),                                  # List with all identical elements
    ]
    
    for nums, expected in test_cases:
        input_list = nums[:]  # Make a copy to avoid in-place modifications affecting others
        merge_sort(input_list)
        assert input_list == expected, f"Failed for input {nums}: got {input_list}, expected {expected}"


test_merge_sort(merge_sort_slice)
test_merge_sort(merge_sort_index)
