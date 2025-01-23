from quickSort import quick_sort
import timeit
import random

NUMBER_OF_REPETITION = 1000
LIST_SIZE = 1_000

random.seed(3)

nums = list(range(LIST_SIZE))
random.shuffle(nums)

t = timeit.Timer("quick_sort(nums, use_insertion_sort=False)", "from __main__ import quick_sort, nums")
print(f"Quick sort alone:                                    {t.timeit(NUMBER_OF_REPETITION)}")

i = 2
while i <= 64: 
    
    t_partition = timeit.Timer(f"quick_sort(nums, partition_limit={i})", 
                               "from __main__ import quick_sort, nums")
    print(f"Quick sort and insertion sort (parition limit = {i}):", 
          f"{t_partition.timeit(NUMBER_OF_REPETITION)}")

    i *= 2

Output = """
Quick sort alone:                                    0.6083690579998802
Quick sort and insertion sort (parition limit = 2): 0.6127442389988573
Quick sort and insertion sort (parition limit = 4): 0.6060488289986097
Quick sort and insertion sort (parition limit = 8): 0.6085725049997563
Quick sort and insertion sort (parition limit = 16): 0.6079755400005524
Quick sort and insertion sort (parition limit = 32): 0.6095996629992442
Quick sort and insertion sort (parition limit = 64): 0.610165178999523

"""