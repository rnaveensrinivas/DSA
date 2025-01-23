from bubbleSort import bubble_sort
from selectionSort import selection_sort
from insertionSort import insertion_sort
from shellSort import shell_sort_using_insertion_sort as shell_sort
from mergeSort import merge_sort_index as merge_sort
from quickSort import quick_sort
import timeit
import random

NUMBER_OF_REPETITION = 1000
LIST_SIZE = 500

random.seed(3)

nums = list(range(LIST_SIZE))
random.shuffle(nums)

sorts = [
    'bubble_sort', 
    'selection_sort', 
    'insertion_sort', 
    'shell_sort', 
    'merge_sort', 
    'quick_sort'
    ]

for sort in sorts: 
    t = timeit.Timer(f"{sort}(nums)", 
                     f"from __main__ import {sort}, nums")

    print(f"{sort} time:\t\t{t.timeit(NUMBER_OF_REPETITION)}")


Output = """
bubble_sort time:		0.023969898000359535
selection_sort time:	0.957801443999415
insertion_sort time:	0.029603638000480714
shell_sort time:		0.3048978060014633
merge_sort time:		0.3804853089986864
quick_sort time:		0.28122100600012345

Expectations:
bubble_sort: The time is expected to be fast but higher compared to most of the others.
selection_sort: This will likely take the longest time due to its O(n^2) complexity.
insertion_sort: Should be faster than bubble and selection sort, but slower than shell, merge, and quick sort.
shell_sort: Expected to be faster than bubble, selection, and insertion sorts.
merge_sort: Should perform well, likely slower than quick sort but faster than insertion, selection, and bubble sorts.
quick_sort: Expected to be the fastest for the random data due to its O(n log n) average time complexity.

Is the output expected?
Yes, the output seems to align with these expectations:

bubble_sort: Very fast, which is expected for small list sizes.
selection_sort: Takes the longest, as anticipated due to its O(n^2) time complexity.
insertion_sort: Slower than bubble sort, as expected.
shell_sort: Faster than the others, except quick sort, which is what we expect.
merge_sort: Also reasonably fast but slower than quick sort.
quick_sort: The fastest, as expected, given the list size and random data.
"""