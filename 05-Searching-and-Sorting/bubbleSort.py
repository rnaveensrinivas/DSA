from typing import List

def bubble_sort(nums: List[int]) -> None:
    """Sorts a list of integers in ascending order using short bubble sort, in place.
    
    Args:
        nums (List[int]): List of integers to sort.
    """
    for i in range(len(nums), 0, -1): 
        is_swapped = False
        for j in range(1, i):
            if nums[j - 1] > nums[j]: 
                # lt operator makes it stable. 
                # But this may vary from implementation to implementation.
                
                nums[j - 1], nums[j] = nums[j], nums[j - 1] 
                is_swapped = True
                
        if not is_swapped: # Early stopping
            break


# Test cases to verify the correctness of the bubble_sort function
test_cases = [
    # Basic test cases
    ([5, 3, 8, 4, 2], [2, 3, 4, 5, 8]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse order

    # Edge cases
    ([], []),  # Empty list
    ([1], [1]),  # Single element
    ([2, 1], [1, 2]),  # Two elements

    # Duplicates
    ([4, 2, 4, 3, 2], [2, 2, 3, 4, 4]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),  # All identical

    # Negative numbers
    ([0, -1, -3, 2, 1], [-3, -1, 0, 1, 2]),
    ([-5, -10, -5, -1], [-10, -5, -5, -1]),
]


# Run the test cases
for input_list, expected_output in test_cases:
    bubble_sort(input_list)
    assert input_list == expected_output, f"Test failed for input {input_list}: Expected {expected_output}"