from typing import List

def bubble_sort(nums: List[int]) -> None:
    """Sorts a list of integers in ascending order using bubble sort, in place.
    
    Args:
        nums (List[int]): List of integers to sort.
    """
    for i in range(len(nums), 0, -1): 
        is_swapped = False
        for j in range(1, i):
            if nums[j - 1] > nums[j]: 
                nums[j - 1], nums[j] = nums[j], nums[j - 1] 
                is_swapped = True
        if not is_swapped: 
            break

# Example usage
nums = list(range(10, 0, -1))
print("Before sorting:", nums)
bubble_sort(nums)
print("After sorting:", nums)
