import timeit
import random

print(f"{'n':10s}{'list':>10s}{'dict':>10s}")

for i in range(1_000_000, 10_000_001, 1_000_000):

    t1 = timeit.Timer(f"""del x[random.randrange(len(x))]""", 
                      "from __main__ import random, x")
    x = list(range(i))
    list_time = t1.timeit(number=1000)

    t2 = timeit.Timer(f"""
while (index := random.randrange({i})) not in x: 
    pass
del x[index]""", "from __main__ import random, x")
    
    x = {j: j for j in range(i)}
    dict_time = t2.timeit(number=1000)

    print(f"{i:<10,}{list_time:>10.3f}{dict_time:>10.3f}")
    
Output = """
n               list      dict
1,000,000      0.472     0.002
2,000,000      0.960     0.001
3,000,000      1.170     0.001
4,000,000      1.563     0.001
5,000,000      1.965     0.001
6,000,000      2.291     0.001
7,000,000      2.579     0.001
8,000,000      2.824     0.001
9,000,000      3.290     0.001
10,000,000     3.544     0.001
"""