from quickSort import quick_sort
import timeit
import random

NUMBER_OF_REPETITION = 1000
LIST_SIZE = 500

random.seed(3)

nums = list(range(LIST_SIZE))
random.shuffle(nums)

t = timeit.Timer("quick_sort(nums, use_median_of_three=False)", "from __main__ import quick_sort, nums")
t_median = timeit.Timer("quick_sort(nums)", "from __main__ import quick_sort, nums")

print(f"Time taken when using left_mark as pivot:       {t.timeit(NUMBER_OF_REPETITION)}")
print(f"Time taken when using median of three as pivot: {t_median.timeit(NUMBER_OF_REPETITION)}")

Output = """
Time taken when using left_mark as pivot:       3.303563198998745
Time taken when using median of three as pivot: 0.26630578699951
"""