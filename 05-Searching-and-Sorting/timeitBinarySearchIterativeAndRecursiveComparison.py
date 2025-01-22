from binarySearch import binary_search_iterative, binary_search_recursive
from binarySearch import binary_search_recursive_slice
from timeit import Timer
import random

LIST_SIZE = 1_000_000
NUMBER_OF_REPETITION = 1000

nums = list(range(LIST_SIZE))


t_iterative = Timer(f"binary_search_iterative(nums, random.randrange({LIST_SIZE}))",
                    "from __main__ import binary_search_iterative, random, nums")

t_recurisve_slice = Timer(f"binary_search_recursive_slice(nums, random.randrange({LIST_SIZE}))",
                          "from __main__ import binary_search_recursive_slice, random, nums")

t_recurisve = Timer(f"binary_search_recursive(nums, random.randrange({LIST_SIZE}))",
                    "from __main__ import binary_search_recursive, random, nums")

print(f"Time taken for iterative binary search: {t_iterative.timeit(NUMBER_OF_REPETITION)}")
print(f"Time taken for recursive binary search: {t_recurisve.timeit(NUMBER_OF_REPETITION)}")
print(f"Time taken for recursive slice binary search: {t_recurisve_slice.timeit(NUMBER_OF_REPETITION)}")

Output = """
Time taken to for iterative binary search: 0.0062665820005349815
Time taken to for recursive binary search: 0.006477015998825664
Time taken to for recursive slice binary search: 8.322646041000553
"""