from typing import List, Callable

def merge_sort_slice(nums: List[int]) -> None: 
    """Sort the list of integers using merge sort, in-place.
    
    Args: 
        nums: List of integers that needs to be sorted.
    """
    
    if len(nums) <= 1:
        return nums[:]
    else:  
        # dividing
        mid = len(nums) // 2
        nums[:mid] = merge_sort_slice(nums[:mid])
        nums[mid:] = merge_sort_slice(nums[mid:])
        
        # merging
        temp = [] 
        i = 0
        j = mid
        
        while i < mid and j < len(nums): 
            if nums[i] <= nums[j]: 
                temp.append(nums[i])
                i += 1
            else: 
                temp.append(nums[j])
                j += 1
        
        if i < mid: 
            temp.extend(nums[i: mid])
        elif j < len(nums):
            temp.extend(nums[j:len(nums)])
    
        nums[:] = temp[:]
        return nums[:]    
            
            
def merge_sort_index(nums: List[int], l: int = 0, r: int = None) -> None: 
    """Sort the list of integers using merge sort, in-place.
    
    Args: 
        nums: List of integers that needs to be sorted.
    """
    
    if r is None: 
        r = len(nums)-1
    
    if l >= r: 
        return
    
        
    # dividing
    mid = (l + r) // 2
    merge_sort_index(nums, l, mid)
    merge_sort_index(nums, mid+1, r)
    
    # merging
    temp = [] 
    i = l
    j = mid+1
    
    while i <= mid and j <= r: 
        if nums[i] <= nums[j]: 
            temp.append(nums[i])
            i += 1
        else: 
            temp.append(nums[j])
            j += 1
    
    if i <= mid: 
        temp.extend(nums[i:mid+1])
    elif j <= r:
        temp.extend(nums[j:r+1])

    nums[l:r+1] = temp[:]
        
        
def test_merge_sort(merge_sort: Callable) -> None:
    
    # Case 1: Standard unsorted list
    nums = [64, 34, 25, 12, 22, 11, 90]
    merge_sort(nums)
    assert nums == [11, 12, 22, 25, 34, 64, 90]

    # Case 2: Already sorted list
    nums = [1, 2, 3, 4, 5]
    merge_sort(nums)
    assert nums == [1, 2, 3, 4, 5]

    # Case 3: Reverse sorted list
    nums = [5, 4, 3, 2, 1]
    merge_sort(nums)
    assert nums == [1, 2, 3, 4, 5]

    # Case 4: List with duplicate elements
    nums = [4, 2, 4, 3, 2, 1]
    merge_sort(nums)
    assert nums == [1, 2, 2, 3, 4, 4]

    # Case 5: Single element list
    nums = [42]
    merge_sort(nums)
    assert nums == [42]

    # Case 6: Empty list
    nums = []
    merge_sort(nums)
    assert nums == []

    # Case 7: List with negative numbers
    nums = [3, -1, -7, 8, 0, 5]
    merge_sort(nums)
    assert nums == [-7, -1, 0, 3, 5, 8]

    # Case 8: Large list
    nums = [i for i in range(1000, 0, -1)]  # Reverse order
    merge_sort(nums)
    assert nums == [i for i in range(1, 1001)]
    
if __name__ == "__main__": 
    test_merge_sort(merge_sort=merge_sort_slice)
    test_merge_sort(merge_sort=merge_sort_index)