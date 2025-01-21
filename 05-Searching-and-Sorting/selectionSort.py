from typing import List
def selection_sort(nums: List[int]) -> None: 
    """Perform selection sort on a given list of integers in-place.

    Args:
        nums (List[int]): List of integers to be sorted.
    """
    
    for i in range(len(nums)-1, 0, -1): 
        greatest_elem_index = i
        
        # Find the largest element in the unsorted portion
        for j in range(i): 
            if nums[j] > nums[greatest_elem_index]: 
                greatest_elem_index = j
                
        nums[i], nums[greatest_elem_index] = nums[greatest_elem_index], nums[i]
        

def test_selection_sort():
    # Test cases
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),  # Random order
        ([5, 3, 8, 6, 2], [2, 3, 5, 6, 8]),  # Small random list
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted list
        ([9, 7, 5, 3, 1], [1, 3, 5, 7, 9]),  # Reverse order
        ([1], [1]),  # Single-element list
        ([], []),  # Empty list
        ([10, 10, 10], [10, 10, 10]),  # All elements are the same
    ]
    
    for i, (input_list, expected) in enumerate(test_cases):
        selection_sort(input_list)  # Sort in-place
        assert input_list == expected, f"Test case {i+1} failed: {input_list} != {expected}"
    

if __name__ == "__main__": 
    test_selection_sort()
