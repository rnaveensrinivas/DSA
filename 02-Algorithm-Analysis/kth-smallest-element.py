from random import random, randrange

SIZE = 1_000_000
arr = [random() for _ in range(SIZE)]

sorted_arr = sorted(arr)
k = randrange(SIZE)

print(f"{k=} smallest element: {sorted_arr[k]}")