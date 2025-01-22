from binarySearch import binary_search_iterative
from sequentialSearch import sequential_search
from timeit import Timer
import random

LIST_SIZE = 1_000_000
NUMBER_OF_REPETITION = 1000

nums = list(range(LIST_SIZE))


t_binary = Timer(f"binary_search_iterative(nums, random.randrange({LIST_SIZE}))",
                 "from __main__ import binary_search_iterative, random, nums")

t_sequential = Timer(f"sequential_search(nums, random.randrange({LIST_SIZE}))",
                     "from __main__ import sequential_search, random, nums")

print(f"Time taken for binary search: {t_binary.timeit(NUMBER_OF_REPETITION)}")
print(f"Time taken for sequential search: {t_sequential.timeit(NUMBER_OF_REPETITION)}")

Output = """
Time taken for binary search: 0.005996863999826019
Time taken for sequential search: 9.777105162000225
"""