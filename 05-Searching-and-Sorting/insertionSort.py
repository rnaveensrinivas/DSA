from typing import List

def insertion_sort(nums: List[int]) -> None:
    """
    Sort the list of integers using insertion sort, in place.
    
    Args:
        nums: List[int] that needs to be sorted.
    """
    for i in range(1, len(nums)): # item 0 is already sorted.
        current_num = nums[i]
        j = i - 1

        # Move elements of the sorted sublist that are greater than current_num
        # to one position ahead of their current position
        while j >= 0 and nums[j] > current_num:
            # nums[j] > current_num, gt makes the sort stable here. 
            nums[j + 1] = nums[j]
            j -= 1

        # Insert the current number into its correct position
        nums[j + 1] = current_num


test_cases = [
    ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),  # Random order
    ([5, 3, 8, 6, 2], [2, 3, 5, 6, 8]),  # Small random list
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted list
    ([9, 7, 5, 3, 1], [1, 3, 5, 7, 9]),  # Reverse order
    ([1], [1]),  # Single-element list
    ([], []),  # Empty list
    ([10, 10, 10], [10, 10, 10]),  # All elements are the same
]

for i, (input_list, expected) in enumerate(test_cases, 1):
    result = input_list[:]  # Create a copy to avoid modifying the original list
    insertion_sort(result)
    assert result == expected, f"Test case {i} failed: Got {result}, Expected {expected}"