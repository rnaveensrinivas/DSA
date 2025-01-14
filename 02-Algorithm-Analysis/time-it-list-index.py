from timeit import Timer
import random

NUMBER_OF_REPETITIONS = 1000

t1 = Timer("_ = x[random.randrange(len(x))]", 
           "from __main__ import random, x")

print(f"{'Size':13s}{'Time Taken':<15s}")
for i in range(1_000_000, 10_000_001, 1_000_000):
    
    x = list(range(i))
    time_taken = t1.timeit(number=NUMBER_OF_REPETITIONS)
    
    print(f"{i:<13,d}{time_taken:>1.14f}")

Output = """
Size         Time Taken     
1,000,000    0.00100655200004
2,000,000    0.00112365099994
3,000,000    0.00113600199984
4,000,000    0.00117080200016
5,000,000    0.00119689600069
6,000,000    0.00116394999986
7,000,000    0.00090565200026
8,000,000    0.00089447200025
9,000,000    0.00097068200012
10,000,000   0.00099536499965
"""